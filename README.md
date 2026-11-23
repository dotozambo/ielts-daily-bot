# IELTS 일일 학습봇

매일 아침 7시(KST)에 슬랙 채널로 그날의 IELTS 표현·문장 틀·미션·복습을 보내는 봇.
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

## 설정 순서

1. **슬랙 앱 만들기**: api.slack.com/apps → Create New App → From an app manifest →
   `slack-app-manifest.json` 붙여넣기 (`imzxbyjsxxfotgpuquuj`는 Supabase 프로젝트 ref로 바꾸기)
   → 워크스페이스에 설치 → `Bot User OAuth Token`(xoxb-…)과 `Signing Secret` 확인
2. 봇을 받을 채널에 초대: 채널에서 `/invite @ielts-bot`, 채널 ID 복사(채널 정보 하단)
3. **Edge Function 시크릿** (대시보드 → Edge Functions → Secrets):
   `SLACK_BOT_TOKEN`, `SLACK_SIGNING_SECRET`, `SLACK_CHANNEL_ID`, `IELTS_CRON_SECRET`(아무 긴 랜덤 문자열)
4. 마이그레이션 1·2 실행, 함수 배포
   (`ielts-daily`, `ielts-slack-actions` 모두 `--no-verify-jwt`: 각자 시크릿/서명으로 인증)
5. Vault에 `ielts_project_url`, `ielts_cron_secret` 넣고 마이그레이션 3 실행

## 수동 테스트

```bash
curl -X POST "https://imzxbyjsxxfotgpuquuj.supabase.co/functions/v1/ielts-daily?day=2026-11-24" \
  -H "x-cron-secret: $IELTS_CRON_SECRET"
# 이미 보낸 날을 다시 보내려면 &force=1
```

## 학습표 고치기

- 표현·미션 수정: Supabase Table Editor에서 `ielts_days` 행을 직접 고치면 다음 발송부터 반영
- 12/26처럼 표현을 직접 채우는 날도 `expressions` 칸에 `[{"en":"...","ko":"..."}]` 형식으로 입력
- 데이터를 통째로 바꿀 땐 `scripts/data.py` 수정 → `cd scripts && python3 gen_seed.py` → 시드 재실행 (완료 기록은 유지됨)

## 테스트

```bash
deno test --allow-read tests/
```
