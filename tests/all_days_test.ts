import { renderDaily } from "../supabase/functions/_shared/render.ts";
const days = JSON.parse(await Deno.readTextFile(new URL("./days.json", import.meta.url)));
const byDay = new Map(days.map((d: any) => [d.day, d]));
Deno.test("40일 전부 슬랙 한도 안에서 렌더링", () => {
  for (const d of days) {
    const review = d.review_dates.map((x: string) => byDay.get(x)).filter(Boolean)
      .map((r: any) => ({ day: r.day, expressions: r.expressions }));
    const m = renderDaily(d, review, { done: 0, total: 40, examDate: "2027-01-03" });
    if (m.blocks.length > 50) throw new Error(`${d.day} 블록 초과`);
    for (const b of m.blocks as any[]) if (b.text?.text?.length > 3000) throw new Error(`${d.day} 텍스트 초과`);
  }
  const sun = days.find((d: any) => d.day === "2026-11-29");
  const rv = sun.review_dates.map((x: string) => byDay.get(x));
  console.log(JSON.stringify(renderDaily(sun, rv, { done: 5, total: 40, examDate: "2027-01-03" }).blocks.map((b: any) => b.text?.text ?? b.type)));
});
