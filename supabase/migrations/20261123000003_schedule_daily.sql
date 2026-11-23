-- 매일 07:00 KST(= 22:00 UTC) ielts-daily 함수를 호출한다.
-- 실행 전 Vault에 두 값을 넣어둔다 (SQL Editor):
--   select vault.create_secret('https://imzxbyjsxxfotgpuquuj.supabase.co', 'ielts_project_url');
--   select vault.create_secret('<IELTS_CRON_SECRET과 같은 값>', 'ielts_cron_secret');
create extension if not exists pg_cron;
create extension if not exists pg_net;

select cron.unschedule('ielts-daily') where exists (select 1 from cron.job where jobname = 'ielts-daily');

select cron.schedule(
  'ielts-daily',
  '0 22 * * *',
  $$
  select net.http_post(
    url := (select decrypted_secret from vault.decrypted_secrets where name = 'ielts_project_url') || '/functions/v1/ielts-daily',
    headers := jsonb_build_object(
      'Content-Type', 'application/json',
      'x-cron-secret', (select decrypted_secret from vault.decrypted_secrets where name = 'ielts_cron_secret')
    ),
    body := '{}'::jsonb
  );
  $$
);
