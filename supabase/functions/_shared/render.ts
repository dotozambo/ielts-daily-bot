// 슬랙 Block Kit 메시지 만들기 (DB/네트워크 의존 없음 → 테스트 쉬움)

export type Expression = { en: string; ko: string };
export type Todo = { kind: "blog" | "listening" | "reading" | "mock"; text: string; url: string; minutes: number };
export type Day = {
  day: string; // YYYY-MM-DD
  week: number;
  kind: "신규" | "주간 복습" | "실전";
  topic: string;
  lesson_title: string | null;
  lesson_url: string | null;
  expressions: Expression[];
  frame: string | null;
  mission: string | null;
  review_label: string | null;
  review_dates: string[];
  done: boolean;
  todos?: Todo[] | null;
};
export type ReviewItem = { day: string; expressions: Expression[] };
export type Progress = { done: number; total: number; examDate: string };

const WEEKDAYS = ["일", "월", "화", "수", "목", "금", "토"];

export function md(day: string): string {
  const [, m, d] = day.split("-").map(Number);
  return `${m}/${d}`;
}

function weekday(day: string): string {
  return WEEKDAYS[new Date(`${day}T00:00:00Z`).getUTCDay()];
}

export function daysBetween(from: string, to: string): number {
  return Math.round((Date.parse(`${to}T00:00:00Z`) - Date.parse(`${from}T00:00:00Z`)) / 86400000);
}

const section = (text: string) => ({ type: "section", text: { type: "mrkdwn", text } });
const TODO_ICON: Record<Todo["kind"], string> = { blog: "🔗 블로그", listening: "🎧 Listening", reading: "📖 Reading", mock: "📝 모의시험" };
const escMd = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function renderTodos(todos: Todo[]): string {
  const total = todos.reduce((n, t) => n + t.minutes, 0);
  const lines = todos.map((t) => `• *${TODO_ICON[t.kind]}* (${t.minutes}분) ${escMd(t.text)}  <${t.url}|열기>`);
  return `📌 *오늘 할 일* · 약 ${total}분\n${lines.join("\n")}`;
}
const context = (text: string) => ({ type: "context", elements: [{ type: "mrkdwn", text }] });
const divider = { type: "divider" };

// 슬랙 섹션 텍스트 한도(3000자) 안에 맞춘다
function clip(text: string, max = 2900): string {
  return text.length <= max ? text : text.slice(0, max - 1) + "…";
}

export function renderDaily(d: Day, review: ReviewItem[], p: Progress) {
  const blocks: unknown[] = [];
  const kindIcon = d.kind === "신규" ? "📘" : d.kind === "실전" ? "📝" : "🔁";

  blocks.push({
    type: "header",
    text: { type: "plain_text", text: `📅 ${md(d.day)} (${weekday(d.day)}) · ${d.week}주차`, emoji: true },
  });

  let title = `${kindIcon} *${d.topic}*`;
  if (d.lesson_url) title += `\n🔗 <${d.lesson_url}|${d.lesson_title ?? "오늘의 Liz 레슨"}>`;
  blocks.push(section(title));

  if (d.expressions.length) {
    blocks.push(divider);
    const lines = d.expressions.map((e) => `• *${e.en}* — ${e.ko}`).join("\n");
    blocks.push(section(`*오늘의 표현*\n${lines}`));
  }

  if (d.frame) blocks.push(section(`✍️ *문장 틀*\n\`${d.frame}\``));

  if (d.mission) {
    blocks.push(section(`🎯 *미션*\n${d.mission}\n_→ 이 메시지 스레드에 답장으로 남기기 · 📒 정리 노트는 스레드에_`));
  }

  if (d.todos?.length) blocks.push(section(renderTodos(d.todos)));

  const reviewExprs = review.flatMap((r) => r.expressions);
  if (reviewExprs.length) {
    blocks.push(divider);
    const dates = review.map((r) => md(r.day)).join(", ");
    // 복습은 영어만 보여준다. 뜻은 버튼을 눌러야 보인다 (먼저 떠올리기).
    const words = reviewExprs.map((e) => e.en).join("  ·  ");
    blocks.push(section(clip(`🔁 *복습* (${dates})\n뜻을 먼저 떠올려 보고, 버튼으로 확인하세요.\n${words}`)));
  } else if (d.review_label) {
    blocks.push(divider);
    blocks.push(section(`🔁 *복습 범위*: ${d.review_label}`));
  }

  const actions: unknown[] = [];
  if (d.done) {
    blocks.push(section("✅ *오늘 학습 완료!*"));
  } else {
    actions.push({
      type: "button",
      text: { type: "plain_text", text: "✅ 완료", emoji: true },
      style: "primary",
      action_id: "ielts_done",
      value: d.day,
    });
  }
  if (reviewExprs.length) {
    actions.push({
      type: "button",
      text: { type: "plain_text", text: "👀 복습 뜻 보기", emoji: true },
      action_id: "ielts_show_meanings",
      value: d.day,
    });
  }
  if (actions.length) blocks.push({ type: "actions", elements: actions });

  const dday = daysBetween(d.day, p.examDate);
  blocks.push(context(`시험까지 D-${dday} · 완료 ${p.done}/${p.total}일`));

  return {
    text: `${md(d.day)} IELTS: ${d.topic}`, // 알림 미리보기용
    blocks,
  };
}

export function renderMeanings(review: ReviewItem[]) {
  const parts = review
    .filter((r) => r.expressions.length)
    .map((r) => `*${md(r.day)}*\n` + r.expressions.map((e) => `• ${e.en} — ${e.ko}`).join("\n"));
  return clip(parts.join("\n\n") || "복습할 표현이 없어요.");
}
