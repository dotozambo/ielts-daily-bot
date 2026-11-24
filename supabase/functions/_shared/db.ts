import { createClient } from "npm:@supabase/supabase-js@2";
import type { Day, Progress, ReviewItem } from "./render.ts";
import type { Extras, Model, Note, QuizItem } from "./thread.ts";
import { pickReviewQuiz } from "./thread.ts";

export const EXAM_DATE = Deno.env.get("IELTS_EXAM_DATE") ?? "2027-01-03";

// Edge Function에는 SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY가 자동으로 들어있다
export const db = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
  { auth: { persistSession: false } },
);

export function todayInSeoul(): string {
  return new Date(Date.now() + 9 * 3600 * 1000).toISOString().slice(0, 10);
}

export type Row = Day & {
  slack_channel: string | null;
  slack_ts: string | null;
  note: Note | null;
  quiz: QuizItem[] | null;
  model: Model | null;
  extras: Extras | null;
  model_ts: string | null;
};

export async function getDay(day: string): Promise<Row | null> {
  const { data, error } = await db.from("ielts_days").select("*").eq("day", day).maybeSingle();
  if (error) throw error;
  return data;
}

export async function getReview(d: Day): Promise<ReviewItem[]> {
  if (!d.review_dates?.length) return [];
  const { data, error } = await db
    .from("ielts_days")
    .select("day, expressions")
    .in("day", d.review_dates)
    .order("day", { ascending: false });
  if (error) throw error;
  return (data ?? []) as ReviewItem[];
}

export async function getProgress(): Promise<Progress> {
  const total = await db.from("ielts_days").select("day", { count: "exact", head: true });
  const done = await db.from("ielts_days").select("day", { count: "exact", head: true }).eq("done", true);
  if (total.error) throw total.error;
  if (done.error) throw done.error;
  return { total: total.count ?? 0, done: done.count ?? 0, examDate: EXAM_DATE };
}

// 오늘 퀴즈: 자체 퀴즈가 있으면 그것, 없으면(복습일) 복습 대상 날짜들의 퀴즈를 모은다
export async function getQuizFor(row: Row): Promise<{ items: QuizItem[]; review: boolean }> {
  if (row.quiz?.length) return { items: row.quiz, review: false };
  if (!row.review_dates?.length) return { items: [], review: true };
  const { data, error } = await db
    .from("ielts_days")
    .select("day, quiz")
    .in("day", row.review_dates)
    .order("day", { ascending: true });
  if (error) throw error;
  const quizzes = (data ?? []).map((r) => (r.quiz ?? []) as QuizItem[]);
  return { items: pickReviewQuiz(quizzes), review: true };
}
