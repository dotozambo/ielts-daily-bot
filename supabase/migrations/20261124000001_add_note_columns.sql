-- 정리 노트·퀴즈·모범 답안·추가 표현 칸과, 스레드 메시지 ts 기록
alter table public.ielts_days
  add column if not exists note     jsonb,  -- { summary, items[], frame_tip, extra }
  add column if not exists quiz     jsonb,  -- [{ q, a }]  (null이면 복습일: review_dates의 퀴즈를 모아서 냄)
  add column if not exists model    jsonb,  -- { text, why[] }  완료 버튼을 누르면 스레드에 게시
  add column if not exists extras   jsonb,  -- { phrases[], words[] }  추가 구문 5 + 단어 5
  add column if not exists model_ts text;   -- 모범 답안을 이미 게시했는지 (중복 방지)
