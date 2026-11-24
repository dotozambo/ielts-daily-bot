// 슬랙 Interactivity Request URL. 버튼 클릭을 처리한다.
//  - ielts_done: 완료 표시 + 원래 메시지를 '완료' 상태로 갱신
//  - ielts_show_meanings: 복습 표현의 뜻을 나만 보이는 메시지로 보여줌
//  - ielts_quiz_answer: 퀴즈 메시지를 정답이 보이는 상태로 바꿈
//  완료 시 모범 답안이 있으면 스레드에 한 번 게시
import { db, getDay, getProgress, getQuizFor, getReview } from "../_shared/db.ts";
import { renderDaily, renderMeanings } from "../_shared/render.ts";
import { respond, slackApi, verifySlackSignature } from "../_shared/slack.ts";
import { renderModel, renderQuiz } from "../_shared/thread.ts";

Deno.serve(async (req) => {
  const raw = await req.text();
  const ok = await verifySlackSignature(
    Deno.env.get("SLACK_SIGNING_SECRET")!,
    req.headers.get("x-slack-request-timestamp"),
    req.headers.get("x-slack-signature"),
    raw,
  );
  if (!ok) return new Response("invalid signature", { status: 401 });

  const payload = JSON.parse(new URLSearchParams(raw).get("payload") ?? "{}");
  const action = payload.actions?.[0];
  if (payload.type !== "block_actions" || !action) return new Response("", { status: 200 });

  const day: string = action.value;
  const token = Deno.env.get("SLACK_BOT_TOKEN")!;

  // 슬랙은 3초 안에 응답을 원하므로 실제 처리는 응답 뒤에 이어서 한다
  const work = (async () => {
    const row = await getDay(day);
    if (!row) return;

    if (action.action_id === "ielts_done") {
      const { error } = await db
        .from("ielts_days")
        .update({ done: true, done_at: new Date().toISOString() })
        .eq("day", day);
      if (error) throw error;
      row.done = true;
      const channel = payload.channel?.id ?? row.slack_channel;
      const ts = payload.message?.ts ?? row.slack_ts;
      const message = renderDaily(row, await getReview(row), await getProgress());
      await slackApi("chat.update", token, { channel, ts, ...message });

      if (row.model && !row.model_ts) {
        const sent = await slackApi("chat.postMessage", token, { channel, thread_ts: ts, ...renderModel(row.model) });
        await db.from("ielts_days").update({ model_ts: sent.ts }).eq("day", day);
      }
    }

    if (action.action_id === "ielts_quiz_answer") {
      const quiz = await getQuizFor(row);
      await respond(payload.response_url, {
        replace_original: true,
        ...renderQuiz(day, quiz.items, { review: quiz.review, revealed: true }),
      });
    }

    if (action.action_id === "ielts_show_meanings") {
      await respond(payload.response_url, {
        response_type: "ephemeral",
        replace_original: false,
        text: renderMeanings(await getReview(row)),
      });
    }
  })().catch((e) => console.error("action 처리 실패", e));

  // @ts-ignore EdgeRuntime은 Supabase Edge Functions 런타임 전역
  EdgeRuntime.waitUntil(work);
  return new Response("", { status: 200 });
});
