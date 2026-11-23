-- 매일 07:00 KST(= 22:00 UTC) ielts-daily 함수를 호출한다.
create extension if not exists pg_cron;
create extension if not exists pg_net schema extensions;

-- cron 호출 인증용 시크릿: Vault에서 랜덤 생성 (어디에도 평문으로 남기지 않음)
select vault.create_secret(encode(extensions.gen_random_bytes(32), 'hex'), 'ielts_cron_secret', 'ielts-daily 호출 인증')
where not exists (select 1 from vault.secrets where name = 'ielts_cron_secret');

select vault.create_secret('https://imzxbyjsxxfotgpuquuj.supabase.co', 'ielts_project_url', 'ielts-daily 호출 주소')
where not exists (select 1 from vault.secrets where name = 'ielts_project_url');

-- Edge Function(service_role)이 헤더 값을 검증할 때만 쓰는 함수
create or replace function public.ielts_check_cron_secret(p_secret text)
returns boolean
language sql
security definer
set search_path = ''
as $$
  select exists (
    select 1 from vault.decrypted_secrets
    where name = 'ielts_cron_secret' and decrypted_secret = p_secret
  );
$$;
revoke all on function public.ielts_check_cron_secret(text) from public, anon, authenticated;
grant execute on function public.ielts_check_cron_secret(text) to service_role;

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
