// 슬랙 API 호출과 요청 서명 검증 (Deno / Web Crypto)

const enc = new TextEncoder();

export async function verifySlackSignature(
  signingSecret: string,
  timestamp: string | null,
  signature: string | null,
  rawBody: string,
  nowSec = Math.floor(Date.now() / 1000),
): Promise<boolean> {
  if (!timestamp || !signature) return false;
  // 5분 넘게 지난 요청은 재전송 공격으로 보고 거부
  if (Math.abs(nowSec - Number(timestamp)) > 60 * 5) return false;

  const key = await crypto.subtle.importKey(
    "raw", enc.encode(signingSecret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"],
  );
  const mac = await crypto.subtle.sign("HMAC", key, enc.encode(`v0:${timestamp}:${rawBody}`));
  const computed = "v0=" + [...new Uint8Array(mac)].map((b) => b.toString(16).padStart(2, "0")).join("");

  // 길이가 같을 때만 상수 시간 비교
  if (computed.length !== signature.length) return false;
  let diff = 0;
  for (let i = 0; i < computed.length; i++) diff |= computed.charCodeAt(i) ^ signature.charCodeAt(i);
  return diff === 0;
}

export async function slackApi(method: string, token: string, body: Record<string, unknown>) {
  const res = await fetch(`https://slack.com/api/${method}`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json; charset=utf-8" },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (!data.ok) throw new Error(`Slack ${method} 실패: ${data.error}`);
  return data;
}

export async function respond(responseUrl: string, body: Record<string, unknown>) {
  await fetch(responseUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}
