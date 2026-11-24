-- 메인 메시지의 '📌 오늘 할 일' (블로그 할 일 + Listening·Reading 연습)
alter table public.ielts_days add column if not exists todos jsonb;  -- [{ kind, text, url, minutes }]

-- 12/26: 열리지 않는 Liz '최근 출제 문제' 링크를 Task 2 주제별 질문 모음으로 교체
update public.ielts_days set
  lesson_title = 'IELTS Writing Task 2 (주제별 질문 100+)',
  lesson_url = 'https://ieltsliz.com/ielts-writing-task-2/',
  mission = '어제 모의고사 메모를 보고 약점 표현 5개 정리하기 + Liz의 주제별 Task 2 질문 목록에서 약한 주제 1개 골라 개요 짜기'
where day = '2026-12-26';
