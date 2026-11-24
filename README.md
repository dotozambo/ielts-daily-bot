# IELTS 일일 학습봇

매일 아침 7시(KST)에 슬랙 채널로 그날의 IELTS 표현·문장 틀·미션·복습을 보내는 봇.
메인 메시지 스레드에 📒 정리 노트(쓰임·예문·실수·발음) → 🌱 추가 표현(구문 5 + 단어 5) → 🧩 퀴즈가 달리고,
✅ 완료를 누르면 모범 답안이 스레드에 올라온다.
학습표 데이터는 Supabase `ielts_days` 테이블에 있고, 서버는 Supabase Edge Functions 두 개뿐이다.

```
pg_cron (07:00 KST) ──▶ ielts-daily ──▶ chat.postMessage ──▶ 슬랙 채널
슬랙 버튼 클릭 ──────▶ ielts-slack-actions ──▶ 완료 표시 / 복습 뜻 보기(나만 보기)
```

## 구성

| 경로 | 내용 |
|---|---|
| `supabase/migrations/..._create_ielts_days.sql` | 테이블 (하루 한 행, RLS 켜짐 → service_role만 접근) |
| `supabase/migrations/..._seed_ielts_days.sql` | 11/24 ~ 1/2 40일치 데이터 |
| `supabase/migrations/..._schedule_daily.sql` | pg_cron 스케줄 (Vault 값 필요) |
| `supabase/functions/ielts-daily` | 오늘 행을 슬랙으로 발송 (`x-cron-secret` 헤더로 보호) |
| `supabase/functions/ielts-slack-actions` | 슬랙 Interactivity (서명 검증) |
| `scripts/data.py`, `scripts/gen_seed.py` | 학습표 원본 데이터 → 시드 SQL 생성 |
| `slack-app-manifest.json` | 슬랙 앱 생성용 매니페스트 |

## 현재 상태

- Supabase 프로젝트 `ielts-daily-bot` (`imzxbyjsxxfotgpuquuj`, 서울): 테이블·40일 데이터·함수 2개·cron(매일 07:00 KST) 적용 완료
- cron 인증 시크릿은 Vault(`ielts_cron_secret`)에 랜덤 생성되어 있고, 함수가 DB 함수 `ielts_check_cron_secret`으로 검증한다
  (Edge Function 시크릿에 따로 넣을 필요 없음)

## 남은 설정 (슬랙)

1. api.slack.com/apps → Create New App → From an app manifest → `slack-app-manifest.json` 붙여넣기 → 워크스페이스에 설치
2. `OAuth & Permissions`의 Bot User OAuth Token(`xoxb-…`), `Basic Information`의 Signing Secret 확인
3. 봇을 받을 채널에서 `/invite @ielts-bot`, 채널 ID 복사 (채널 이름 클릭 → 맨 아래)
4. Supabase 대시보드 → Edge Functions → Secrets에 `SLACK_BOT_TOKEN`, `SLACK_SIGNING_SECRET`, `SLACK_CHANNEL_ID` 입력

## 수동 테스트

SQL Editor에서 (특정 날짜 메시지를 바로 보내 보기, 이미 보낸 날은 `&force=1`):

```sql
select net.http_post(
  url := 'https://imzxbyjsxxfotgpuquuj.supabase.co/functions/v1/ielts-daily?day=2026-11-24',
  headers := jsonb_build_object('x-cron-secret',
    (select decrypted_secret from vault.decrypted_secrets where name = 'ielts_cron_secret')),
  body := '{}'::jsonb
);
-- 결과 확인
select status_code, content from net._http_response order by id desc limit 1;
```

## 정리 노트 데이터

| 경로 | 내용 |
|---|---|
| `scripts/notes_w1.py` ~ `notes_w5.py` | 날짜별 정리 노트·퀴즈·모범 답안 |
| `scripts/extras.py` | 날짜별 추가 구문 5 + 단어 5 |
| `scripts/gen_notes.py` | 위 데이터 검증 후 `data/notes.json` + 업데이트 SQL 생성 |

고친 뒤 `cd scripts && python3 gen_notes.py` → 커밋·푸시 → SQL Editor에서 GitHub의 `data/notes.json`을
`net.http_get`으로 받아 `ielts_days`의 note·quiz·model·extras를 갱신한다 (커밋 SHA로 고정, md5 확인).

이미 보낸 날짜에 스레드만 다시 달기: `ielts-daily?day=YYYY-MM-DD&thread_only=1`

## 학습표 고치기

- 표현·미션 수정: Supabase Table Editor에서 `ielts_days` 행을 직접 고치면 다음 발송부터 반영
- 12/26처럼 표현을 직접 채우는 날도 `expressions` 칸에 `[{"en":"...","ko":"..."}]` 형식으로 입력
- 데이터를 통째로 바꿀 땐 `scripts/data.py` 수정 → `cd scripts && python3 gen_seed.py` → 시드 재실행 (완료 기록은 유지됨)

## 테스트

```bash
deno test --allow-read tests/
```
