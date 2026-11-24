"""정리 노트(notes_w*.py) + 추가 표현(extras.py) → DB 업데이트 SQL과 테스트용 JSON 생성"""
import json
from datetime import date, timedelta
from notes_w1 import W1
from notes_w2 import W2
from notes_w3 import W3
from notes_w4 import W4
from notes_w5 import W5
from extras import EXTRAS
from data import rows

START = date(2026, 11, 24)
NOTES = {**W1, **W2, **W3, **W4, **W5}
days = [(START + timedelta(days=i)).isoformat() for i in range(len(rows))]

missing = [d for d in days if d not in NOTES]
assert not missing, f"노트 없는 날: {missing}"

# 새 표현이 있는 날은 노트 항목 수가 학습표 표현 수와 같아야 한다
for i, (typ, topic, lesson, lk, exprs, *_rest) in enumerate(rows):
    d = days[i]
    real = [e for e in exprs if e and e != "(직접 채우기)"]
    n = NOTES[d]
    assert len(n["items"]) == len(real), f"{d}: 표현 {len(real)}개 vs 노트 {len(n['items'])}개"
    if real:
        assert d in EXTRAS, f"{d}: 추가 표현 없음"
        assert len(EXTRAS[d]["phrases"]) == 5 and len(EXTRAS[d]["words"]) == 5, d
        assert n.get("quiz") and len(n["quiz"]) == 4, f"{d}: 퀴즈 4문항 필요"

def q(v):
    return "null" if v is None else "'" + json.dumps(v, ensure_ascii=False).replace("'", "''") + "'::jsonb"

out, stmts = [], []
for d in days:
    n = NOTES[d]
    note = {"summary": n["summary"], "items": n["items"], "frame_tip": n.get("frame_tip"), "extra": n.get("extra")}
    rec = {"day": d, "note": note, "quiz": n.get("quiz"), "model": n.get("model"), "extras": EXTRAS.get(d)}
    out.append(rec)
    stmts.append(f"update public.ielts_days set note = {q(note)}, quiz = {q(rec['quiz'])}, model = {q(rec['model'])}, extras = {q(rec['extras'])} where day = '{d}';")

open("../supabase/migrations/20261124000002_seed_notes.sql", "w").write(
    "-- 정리 노트·퀴즈·모범 답안·추가 표현 (scripts/gen_notes.py로 생성)\n" + "\n".join(stmts) + "\n")
json.dump(out, open("../data/notes.json", "w"), ensure_ascii=False)
n_items = sum(len(NOTES[d]["items"]) for d in days)
print("days", len(days), "items", n_items, "extras days", len(EXTRAS), "sql bytes", sum(len(s) for s in stmts))
