// 매일 아침 pg_cron이 호출 → 오늘 행을 슬랙 채널에 보낸다.
// 인증: x-cron-secret 헤더를 Vault의 ielts_cron_secret과 비교 (DB 함수 ielts_check_cron_secret)
// 수동 테스트: SQL Editor에서 README의 "수동 테스트" 쿼리 실행
import { db, getDay, getProgress, getQuizFor, getReview, type Row, todayInSeoul } from "../_shared/db.ts";
import { renderDaily } from "../_shared/render.ts";
import { slackApi } from "../_shared/slack.ts";
import { renderExtras, renderNote, renderQuiz } from "../_shared/thread.ts";

// 메인 메시지 스레드에 정리 노트 → 추가 표현 → 퀴즈 순서로 단다
async function postThread(row: Row, token: string, channel: string, threadTs: string) {
  const post = (msg: Record<string, unknown>) =>
    slackApi("chat.postMessage", token, { channel, thread_ts: threadTs, unfurl_links: false, unfurl_media: false, ...msg });
  if (row.note) {
    await post(renderNote(row.note, { frame: row.frame, lessonTitle: row.lesson_title, lessonUrl: row.lesson_url }));
  }
  if (row.extras) await post(renderExtras(row.extras));
  const quiz = await getQuizFor(row);
  if (quiz.items.length) await post(renderQuiz(row.day, quiz.items, { review: quiz.review, revealed: false }));
}

Deno.serve(async (req) => {
  const secret = req.headers.get("x-cron-secret");
  const { data: authorized, error: authError } = secret
    ? await db.rpc("ielts_check_cron_secret", { p_secret: secret })
    : { data: false, error: null };
  if (authError) throw authError;
  if (!authorized) return new Response("unauthorized", { status: 401 });

  const url = new URL(req.url);
  const day = url.searchParams.get("day") ?? todayInSeoul();
  const force = url.searchParams.get("force") === "1";
  const threadOnly = url.searchParams.get("thread_only") === "1"; // 이미 보낸 메시지에 스레드만 달기

  const row = await getDay(day);
  if (!row) return Response.json({ ok: true, skipped: `학습표에 ${day} 행이 없음` });
  const channel = Deno.env.get("SLACK_CHANNEL_ID")!;
  const token = Deno.env.get("SLACK_BOT_TOKEN")!;

  if (threadOnly) {
    if (!row.slack_ts) return Response.json({ ok: false, error: "아직 보낸 메시지가 없음" }, { status: 400 });
    await postThread(row, token, row.slack_channel ?? channel, row.slack_ts);
    return Response.json({ ok: true, day, thread: row.slack_ts });
  }
  if (row.slack_ts && !force) return Response.json({ ok: true, skipped: "이미 보냄", ts: row.slack_ts });
  const message = renderDaily(row, await getReview(row), await getProgress());

  const sent = await slackApi("chat.postMessage", token, { channel, ...message, unfurl_links: false });

  const { error } = await db
    .from("ielts_days")
    .update({ slack_channel: sent.channel, slack_ts: sent.ts, sent_at: new Date().toISOString() })
    .eq("day", day);
  if (error) throw error;

  await postThread(row, token, sent.channel, sent.ts);
  return Response.json({ ok: true, day, ts: sent.ts });
});
