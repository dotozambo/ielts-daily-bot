"""학습표 데이터(data.py)로 supabase/migrations/..._seed.sql 생성"""
import json, re
from datetime import date, timedelta
from data import rows, LINK, N, R, T

START = date(2026, 11, 24)
END = START + timedelta(days=len(rows) - 1)

def d(m, dd):
    return date(2026 if m >= 11 else 2027, m, dd)

def parse_review(label, day):
    """복습일의 '11/24 ~ 11/28 전체' 같은 라벨을 실제 날짜 목록으로 변환"""
    m = re.match(r"(\d+)/(\d+) ~ (\d+)/(\d+)", label)
    if not m:
        return []
    a, b = d(int(m[1]), int(m[2])), d(int(m[3]), int(m[4]))
    return [a + timedelta(days=i) for i in range((b - a).days + 1)]

def parse_expr(e):
    m = re.match(r"^(.*) \(([^()]*)\)$", e)
    return {"en": m[1], "ko": m[2]} if m else {"en": e, "ko": ""}

def q(v):
    if v is None:
        return "null"
    return "'" + str(v).replace("'", "''") + "'"

values = []
for i, (typ, topic, lesson, lk, exprs, frame, mission, rev) in enumerate(rows):
    day = START + timedelta(days=i)
    ex = [parse_expr(e) for e in exprs if e and e != "(직접 채우기)"]
    if rev is None:
        rdates = [day - timedelta(days=k) for k in (1, 3, 7) if day - timedelta(days=k) >= START]
    else:
        rdates = parse_review(rev, day)
    week = ((day - START).days + 1) // 7 + 1
    values.append("(" + ", ".join([
        q(day.isoformat()), str(week), q(typ), q(topic),
        q(None if lesson == "—" else lesson), q(LINK[lk] if lk else None),
        q(json.dumps(ex, ensure_ascii=False)) + "::jsonb",
        q(frame), q(mission), q(rev),
        "array[" + ",".join(q(x.isoformat()) for x in rdates) + "]::date[]",
    ]) + ")")

sql = """-- IELTS 일일 학습표 시드 (scripts/gen_seed.py로 생성)
insert into public.ielts_days
  (day, week, kind, topic, lesson_title, lesson_url, expressions, frame, mission, review_label, review_dates)
values
""" + ",\n".join(values) + """
on conflict (day) do update set
  week = excluded.week, kind = excluded.kind, topic = excluded.topic,
  lesson_title = excluded.lesson_title, lesson_url = excluded.lesson_url,
  expressions = excluded.expressions, frame = excluded.frame, mission = excluded.mission,
  review_label = excluded.review_label, review_dates = excluded.review_dates;
"""
open("../supabase/migrations/20261123000002_seed_ielts_days.sql", "w").write(sql)
print("rows:", len(values), START, END)
