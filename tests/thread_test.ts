import { pickReviewQuiz, renderExtras, renderModel, renderNote, renderQuiz } from "../supabase/functions/_shared/thread.ts";

function assert(c: unknown, m = "assert failed") { if (!c) throw new Error(m); }
const notes = JSON.parse(await Deno.readTextFile(new URL("../data/notes.json", import.meta.url)));
const days = JSON.parse(await Deno.readTextFile(new URL("./days.json", import.meta.url)));
const dayRow = new Map(days.map((d: any) => [d.day, d]));
const byDay = new Map(notes.map((n: any) => [n.day, n]));

function checkMsg(label: string, m: { blocks: any[] }) {
  assert(m.blocks.length <= 50, `${label}: 블록 ${m.blocks.length}개`);
  for (const b of m.blocks) {
    const t = typeof b.text?.text === "string" ? b.text.text : (typeof b.elements?.[0]?.text === "string" ? b.elements[0].text : "");
    assert(t.length <= 3000, `${label}: 텍스트 ${t.length}자`);
    // 링크 형식 <url|label> 이 깨지지 않았는지
    for (const link of t.matchAll(/<(https?:[^|>]+)\|([^>]*)>/g)) assert(!link[1].includes(" "), `${label}: URL 공백 ${link[1]}`);
  }
}

Deno.test("40일 전부: 노트·추가 표현·퀴즈·모범 답안이 슬랙 한도 안", () => {
  let posted = 0;
  for (const n of notes) {
    const row = dayRow.get(n.day) as any;
    if (n.note.items.length || n.note.extra) {
      checkMsg(`${n.day} note`, renderNote(n.note, { frame: row.frame, lessonTitle: row.lesson_title, lessonUrl: row.lesson_url }));
      posted++;
    }
    if (n.extras) {
      checkMsg(`${n.day} extras`, renderExtras(n.extras));
      assert(n.extras.phrases.length === 5 && n.extras.words.length === 5);
    }
    const quiz = n.quiz ?? pickReviewQuiz(row.review_dates.map((d: string) => (byDay.get(d) as any)?.quiz ?? []));
    if (quiz.length) {
      checkMsg(`${n.day} quiz`, renderQuiz(n.day, quiz, { review: !n.quiz, revealed: false }));
      checkMsg(`${n.day} quiz-a`, renderQuiz(n.day, quiz, { review: !n.quiz, revealed: true }));
    }
    if (n.model) checkMsg(`${n.day} model`, renderModel(n.model));
  }
  assert(posted === 40, `노트 있는 날 ${posted}`);
});

Deno.test("복습 퀴즈: 최대 8문항, 같은 입력이면 같은 결과", () => {
  const qs = Array.from({ length: 5 }, (_, d) => Array.from({ length: 4 }, (_, i) => ({ q: `${d}-${i}`, a: "x" })));
  const a = pickReviewQuiz(qs), b = pickReviewQuiz(qs);
  assert(a.length === 8 && JSON.stringify(a) === JSON.stringify(b));
  assert(new Set(a.map((x) => x.q)).size === 8, "중복 없음");
});

Deno.test("정답은 버튼 누르기 전엔 안 보임 / & 이스케이프", () => {
  const n = byDay.get("2026-11-24") as any;
  const closed = JSON.stringify(renderQuiz(n.day, n.quiz, { review: false, revealed: false }));
  const open = JSON.stringify(renderQuiz(n.day, n.quiz, { review: false, revealed: true }));
  assert(!closed.includes("compulsory education") || closed.indexOf("→") === -1);
  assert(open.includes("→ compulsory education"));
  const crime = renderNote({ summary: "a & b", items: [], frame_tip: null, extra: null }, { frame: null, lessonTitle: "Crime & Punishment", lessonUrl: "https://x.com" });
  assert(JSON.stringify(crime).includes("Crime &amp; Punishment"));
});
