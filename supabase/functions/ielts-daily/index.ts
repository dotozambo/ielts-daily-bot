// 매일 아침 pg_cron이 호출 → 오늘 행을 슬랙 채널에 보낸다.
// 인증: x-cron-secret 헤더를 Vault의 ielts_cron_secret과 비교 (DB 함수 ielts_check_cron_secret)
// 수동 테스트: SQL Editor에서 README의 "수동 테스트" 쿼리 실행
import { db, getDay, getProgress, getReview, todayInSeoul } from "../_shared/db.ts";
import { renderDaily } from "../_shared/render.ts";
import { slackApi } from "../_shared/slack.ts";

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

  const row = await getDay(day);
  if (!row) return Response.json({ ok: true, skipped: `학습표에 ${day} 행이 없음` });
  if (row.slack_ts && !force) return Response.json({ ok: true, skipped: "이미 보냄", ts: row.slack_ts });

  const channel = Deno.env.get("SLACK_CHANNEL_ID")!;
  const token = Deno.env.get("SLACK_BOT_TOKEN")!;
  const message = renderDaily(row, await getReview(row), await getProgress());

  const sent = await slackApi("chat.postMessage", token, { channel, ...message, unfurl_links: false });

  const { error } = await db
    .from("ielts_days")
    .update({ slack_channel: sent.channel, slack_ts: sent.ts, sent_at: new Date().toISOString() })
    .eq("day", day);
  if (error) throw error;

  return Response.json({ ok: true, day, ts: sent.ts });
});
