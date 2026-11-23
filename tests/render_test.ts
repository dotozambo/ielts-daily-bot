function assert(c: unknown, m = "assert failed") { if (!c) throw new Error(m); }
function assertEquals(a: unknown, b: unknown) { if (JSON.stringify(a) !== JSON.stringify(b)) throw new Error(`${JSON.stringify(a)} != ${JSON.stringify(b)}`); }
import { daysBetween, renderDaily, renderMeanings } from "../supabase/functions/_shared/render.ts";
import { verifySlackSignature } from "../supabase/functions/_shared/slack.ts";

const day = {
  day: "2026-11-25", week: 1, kind: "신규" as const, topic: "Education 2: 온라인 vs 교실",
  lesson_title: "Education Vocabulary", lesson_url: "https://ieltsliz.com/education-vocabulary-school-and-university/",
  expressions: [{ en: "online learning", ko: "온라인 학습" }],
  frame: "In my opinion, ... because ...", mission: "의견 3문장", review_label: null,
  review_dates: ["2026-11-24"], done: false,
};
const review = [{ day: "2026-11-24", expressions: [{ en: "tuition fees", ko: "등록금" }] }];
const prog = { done: 1, total: 40, examDate: "2027-01-03" };

Deno.test("일일 메시지: 헤더/복습은 영어만/버튼 2개/D-day", () => {
  const m = renderDaily(day, review, prog);
  const json = JSON.stringify(m.blocks);
  assert(json.includes("11/25 (수) · 1주차"));
  assert(json.includes("tuition fees"));
  assert(!json.includes("등록금"), "복습 뜻이 미리 보이면 안 됨");
  const actions = (m.blocks as any[]).find((b) => b.type === "actions");
  assertEquals(actions.elements.map((e: any) => e.action_id), ["ielts_done", "ielts_show_meanings"]);
  assert(json.includes("D-39"));
  console.log(JSON.stringify(m, null, 1));
});

Deno.test("완료 상태: 완료 버튼 사라짐", () => {
  const m = renderDaily({ ...day, done: true }, review, prog);
  const actions = (m.blocks as any[]).find((b) => b.type === "actions");
  assertEquals(actions.elements.map((e: any) => e.action_id), ["ielts_show_meanings"]);
});

Deno.test("뜻 보기", () => {
  assert(renderMeanings(review).includes("tuition fees — 등록금"));
});

Deno.test("D-day 계산", () => assertEquals(daysBetween("2027-01-02", "2027-01-03"), 1));

Deno.test("슬랙 서명 검증 (슬랙 공식 예시 값)", async () => {
  // https://api.slack.com/authentication/verifying-requests-from-slack 의 예시
  const secret = "8f742231b10e8888abcd99yyyzzz85a5";
  const ts = "1531420618";
  const body = "token=xyzz0WbapA4vBCDEFasx0q6G&team_id=T1DC2JH3J&team_domain=testteamnow&channel_id=G8PSS9T3V&channel_name=foobar&user_id=U2CERLKJA&user_name=roadrunner&command=%2Fwebhook-collect&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT1DC2JH3J%2F397700885554%2F96rGlfmibIGlgcZRskXaIFfN&trigger_id=398738663015.47445629121.803a0bc887a14d10d2c447fce8b6703c";
  const sig = "v0=a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503";
  assert(await verifySlackSignature(secret, ts, sig, body, 1531420618));
  assert(!(await verifySlackSignature(secret, ts, sig, body + "x", 1531420618)));
  assert(!(await verifySlackSignature(secret, ts, sig, body, 1531420618 + 600)), "오래된 요청 거부");
});
