-- IELTS 일일 학습표: 하루 한 행
create table if not exists public.ielts_days (
  day           date primary key,
  week          int  not null,
  kind          text not null check (kind in ('신규', '주간 복습', '실전')),
  topic         text not null,
  lesson_title  text,
  lesson_url    text,
  expressions   jsonb not null default '[]'::jsonb,  -- [{ "en": "...", "ko": "..." }]
  frame         text,                                -- 문장 틀
  mission       text,
  review_label  text,                                -- 복습일 설명 (예: "11/24 ~ 11/28 전체")
  review_dates  date[] not null default '{}',         -- 이 날 복습할 날짜들
  done          boolean not null default false,
  done_at       timestamptz,
  memo          text,
  slack_channel text,
  slack_ts      text,                                -- 보낸 메시지 ts (완료 시 메시지 갱신용)
  sent_at       timestamptz,
  updated_at    timestamptz not null default now()
);

-- 봇은 service_role 키로만 접근. 브라우저(anon/authenticated) 접근은 막는다.
alter table public.ielts_days enable row level security;

create or replace function public.ielts_touch_updated_at()
returns trigger language plpgsql set search_path = '' as $$
begin
  new.updated_at := now();
  return new;
end $$;

drop trigger if exists ielts_days_touch on public.ielts_days;
create trigger ielts_days_touch before update on public.ielts_days
for each row execute function public.ielts_touch_updated_at();
