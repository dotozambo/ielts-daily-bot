// 메인 메시지 스레드에 다는 학습 메시지들: 정리 노트 / 추가 표현 / 퀴즈 / 모범 답안
// DB·네트워크 의존 없음 → 테스트하기 쉬움

export type Pron = { word: string | null; ipa: string | null; youglish: string; dict: string | null };
export type NoteItem = {
  en: string;
  ko: string;
  usage: string;
  examples: { type: "w" | "s"; text: string }[];
  mistake: string;
  pron: Pron;
};
export type Note = { summary: string; items: NoteItem[]; frame_tip: string | null; extra: string | null };
export type QuizItem = { q: string; a: string };
export type Model = { text: string; why: string[] };
export type Extras = {
  phrases: { en: string; ko: string; example: string; youglish: string }[];
  words: { en: string; ipa: string; ko: string; example: string; youglish: string; dict: string }[];
};

const MAX = 2900; // 섹션 텍스트 한도(3000자)보다 약간 작게

// 슬랙 mrkdwn 제어 문자 이스케이프 (링크·강조 표시는 우리가 따로 붙인다)
export function esc(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

const section = (text: string) => ({ type: "section", text: { type: "mrkdwn", text: text.slice(0, MAX) } });
const context = (text: string) => ({ type: "context", elements: [{ type: "mrkdwn", text: text.slice(0, MAX) }] });
const divider = { type: "divider" };

// 긴 텍스트를 줄 단위로 나눠 여러 섹션으로
function sections(text: string): unknown[] {
  const out: unknown[] = [];
  let buf = "";
  for (const line of text.split("\n")) {
    if ((buf + "\n" + line).length > MAX && buf) {
      out.push(section(buf));
      buf = line;
    } else {
      buf = buf ? buf + "\n" + line : line;
    }
  }
  if (buf) out.push(section(buf));
  return out;
}

function pronLine(p: Pron): string {
  const parts: string[] = [];
  if (p.word && p.ipa) parts.push(`${esc(p.word)} \`${p.ipa}\``);
  parts.push(`<${p.youglish}|문장 속 발음>`);
  if (p.dict) parts.push(`<${p.dict}|사전 발음>`);
  return "🔊 " + parts.join(" · ");
}

export function renderNote(
  note: Note,
  opts: { frame: string | null; lessonTitle: string | null; lessonUrl: string | null },
) {
  const blocks: unknown[] = [section(`📒 *정리 노트*\n${esc(note.summary)}`)];

  note.items.forEach((it, i) => {
    const lines = [
      `*${i + 1}. ${esc(it.en)}* — ${esc(it.ko)}`,
      pronLine(it.pron),
      `• 쓰임: ${esc(it.usage)}`,
      ...it.examples.map((e) => `${e.type === "w" ? "✍️" : "🗣"} _${esc(e.text)}_`),
      `⚠️ ${esc(it.mistake)}`,
    ];
    blocks.push(divider, section(lines.join("\n")));
  });

  if (opts.frame && note.frame_tip) {
    blocks.push(divider, section(`✍️ *문장 틀*  \`${esc(opts.frame)}\`\n${esc(note.frame_tip)}`));
  }
  if (note.extra) {
    blocks.push(divider, ...sections(note.extra)); // extra는 우리가 쓴 mrkdwn이라 그대로
  }
  if (opts.lessonUrl) {
    blocks.push(context(`🔗 원문 더 보기: <${opts.lessonUrl}|${esc(opts.lessonTitle ?? "IELTS Liz")}>`));
  }
  return { text: "📒 정리 노트", blocks };
}

export function renderExtras(x: Extras) {
  const phrases = x.phrases
    .map((p) => `• *${esc(p.en)}* — ${esc(p.ko)}  <${p.youglish}|🔊>\n      _${esc(p.example)}_`)
    .join("\n");
  const words = x.words
    .map((w) =>
      `• *${esc(w.en)}* \`${w.ipa}\` ${esc(w.ko)}  <${w.youglish}|🔊> <${w.dict}|사전>\n      _${esc(w.example)}_`
    )
    .join("\n");
  return {
    text: "🌱 추가 표현",
    blocks: [
      section("🌱 *추가 표현* — 구문 5 · 단어 5\n오늘 주제와 같이 쓰면 좋은 표현이에요. 예문을 소리 내 한 번씩 읽어 보세요."),
      divider,
      section(`*구문*\n${phrases}`),
      divider,
      section(`*단어*\n${words}`),
    ],
  };
}

// 복습일: 복습 대상 날짜들의 퀴즈를 모아 최대 n개를 고르게 뽑는다 (항상 같은 결과)
export function pickReviewQuiz(quizzes: QuizItem[][], n = 8): QuizItem[] {
  const all = quizzes.flat();
  if (all.length <= n) return all;
  return Array.from({ length: n }, (_, i) => all[Math.floor((i * all.length) / n)]);
}

export function renderQuiz(day: string, items: QuizItem[], opts: { review: boolean; revealed: boolean }) {
  const title = opts.review ? `🧩 *복습 퀴즈* (${items.length}문항)` : "🧩 *미니 퀴즈*";
  const body = items
    .map((it, i) => {
      const q = `${i + 1}. ${esc(it.q)}`;
      return opts.revealed ? `${q}\n      → ${esc(it.a)}` : q;
    })
    .join("\n");
  const blocks: unknown[] = [section(title), ...sections(body)];
  if (!opts.revealed) {
    blocks.push({
      type: "actions",
      elements: [{
        type: "button",
        text: { type: "plain_text", text: "🔑 정답 보기", emoji: true },
        action_id: "ielts_quiz_answer",
        value: day,
      }],
    });
  } else {
    blocks.push(context("틀린 문제는 메모해 두면 복습일에 다시 나와요."));
  }
  return { text: opts.review ? "🧩 복습 퀴즈" : "🧩 미니 퀴즈", blocks };
}

export function renderModel(m: Model) {
  const quoted = m.text
    .split("\n")
    .map((l) => (l.trim() ? `> ${esc(l)}` : ">"))
    .join("\n");
  const why = m.why.map((w) => `• ${esc(w)}`).join("\n");
  return {
    text: "✅ 모범 답안",
    blocks: [
      section("✅ *모범 답안* — 내가 쓴 답과 비교해 보세요"),
      ...sections(quoted),
      divider,
      section(`💡 *포인트*\n${why}`),
    ],
  };
}
