# 메인 메시지의 '📌 오늘 할 일' — 블로그에서만 할 수 있는 것 + Listening·Reading 실전 연습
# 블로그 할 일은 각 Liz 페이지 구성을 직접 확인하고 적었다 (2026-11-24 기준).
# T(종류, 할 일, 링크, 분)   종류: blog / listening / reading / mock

L = "https://ieltsliz.com/"
BC = "https://takeielts.britishcouncil.org/"
LISTEN_1 = BC + "prepare-test/free-ielts-practice-tests/listening-practice-test-1"
LISTEN_2 = BC + "take-ielts/prepare/free-ielts-english-practice-tests/listening-2/section-1"
READ_GT = BC + "take-ielts/prepare/free-ielts-english-practice-tests/reading/general-training"
FAMILIAR = BC + "prepare/ielts-free-practice-mock-tests/ielts-familiarisation-test"

EDU = L + "education-vocabulary-school-and-university/"
TECH = L + "technology-vocabulary-for-speaking/"
ENV = "http://www.ieltsliz.com/world-environmental-problems-vocabulary"
URBAN = L + "ielts-topic-urban-planning-design/"
LETTER = L + "ielts-letter-writing-essential-tips/"
P1 = L + "ielts-speaking-part-1-topics/"
W2 = L + "ielts-writing-task-2/"


def T(kind, text, url, minutes):
    return {"kind": kind, "text": text, "url": url, "minutes": minutes}


TODOS = {
    "2026-11-24": [T("blog", "교육 어휘 목록(약 75개) 훑고, 빈칸 연습문제 첫 세트 풀기 (발음 오디오도 있어요)", EDU, 15)],
    "2026-11-25": [T("blog", "같은 페이지의 남은 빈칸 연습문제 풀기 + 남녀공학 주제 영상 보기", EDU, 15)],
    "2026-11-26": [T("blog", "Part 1 질문 목록에서 Work·Study 질문(각 10개 정도)을 소리 내 답해 보기", P1, 15)],
    "2026-11-27": [T("blog", "기능별 연결어 목록 보고, 빈칸 연습문제 풀기 (정답 해설 있음)", L + "linking-words-for-writing/", 15)],
    "2026-11-28": [T("blog", "연결어 빈칸 5문제 풀기 (오늘 미션)", L + "ielts-writing-task-2-practice-with-linking-words/", 10),
                   T("listening", "British Council 공식 Listening Test 1 (4파트, 30분) → 채점 → 틀린 문제는 스크립트로 확인", LISTEN_1, 45)],
    "2026-11-30": [T("blog", "짧은 읽기 글 + 빈칸 문제 풀고, Part 1 모범 답안 1개 읽기", TECH, 15)],
    "2026-12-01": [T("blog", "같은 페이지 아래 'Part 3 기술 질문' 링크에서 질문 2개 골라 소리 내 답하기", TECH, 10)],
    "2026-12-02": [T("blog", "환경 문제 10개: 오디오 듣고 빈칸 채우기 1~5번 (Listening 연습도 돼요)", ENV, 15),
                   T("reading", "British Council 공식 GT Reading Test 1 — Section 1 (20분)", READ_GT, 20)],
    "2026-12-03": [T("blog", "환경 오디오 빈칸 6~10번 마저 풀기", ENV, 15)],
    "2026-12-04": [T("blog", "바꿔 말하기 페이지는 글이 짧고 영상 중심이에요. 사이드바 영상만 보면 충분 (댓글 Q&A는 선택)", L + "ielts-vocabulary-paraphrasing-tips/", 10)],
    "2026-12-05": [T("blog", "detrimental 예문 6개 소리 내 읽기", L + "detrimental-vocabulary-sample-sentence/", 5),
                   T("reading", "GT Reading Test 1 — Section 2 (20분)", READ_GT, 20)],
    "2026-12-07": [T("blog", "범죄 어휘(약 90개)를 섹션별 오디오와 함께 훑고, 빈칸 12문제 풀기", L + "crime-and-punishment-vocabulary/", 20)],
    "2026-12-08": [T("blog", "범죄 어휘 빈칸 7문제 풀기 (오늘 미션)", L + "crime-vocabulary-exercise/", 10)],
    "2026-12-09": [T("blog", "Speaking 질문 4개의 모범 답안 읽기 + Task 2 문제 7개 중 하나 골라 개요만 짜기", L + "government-vocabulary-word-lists/", 15),
                   T("reading", "GT Reading Test 1 — Section 3 (20분)", READ_GT, 20)],
    "2026-12-10": [T("blog", "Task 2 허브의 '모범 에세이' 목록에서 건강 주제 에세이 1편 읽기", W2, 15)],
    "2026-12-11": [T("blog", "광고 어휘 발음 오디오 듣기 + 빈칸 7문제 풀기", L + "advertising-vocabulary-and-pronunciation/", 15)],
    "2026-12-12": [T("blog", "신문 어휘(약 40개) + 빈칸 8문제 + 오류 고치기 8문제", "http://www.ieltsliz.com/newspaper-vocabulary", 20),
                   T("listening", "British Council 공식 Listening Test 2 (30분) → 채점 → 스크립트 확인", LISTEN_2, 45)],
    "2026-12-14": [T("blog", "Part 1 질문 목록에서 Hometown·Home 질문(각 10개 정도)을 소리 내 답하기", P1, 15)],
    "2026-12-15": [T("blog", "영화 장르 12개 리스닝 퀴즈 (설명 듣고 장르 맞히기)", L + "types-of-films-vocabulary/", 10)],
    "2026-12-16": [T("blog", "옷·액세서리 단어를 격식/비격식으로 분류하는 연습", L + "clothes-vocabulary/", 10),
                   T("reading", "GT Reading Test 2 전체 (3섹션, 60분) — 실전처럼 시간 재기", READ_GT, 60)],
    "2026-12-17": [T("blog", "큐카드 29개 중 '사람' 카드 2개를 골라 1분 메모만 해 보기", L + "ielts-speaking-part-2-topics/", 10)],
    "2026-12-18": [T("blog", "도시 어휘 25개 훑고, Part 3 모범 답안 5개 읽기", URBAN, 15)],
    "2026-12-19": [T("blog", "어려운 큐카드 5개의 팁 펼쳐 보고, 하나 골라 2분 말하기", L + "ielts-speaking-part-2-difficult-topics", 15),
                   T("listening", "Listening Test 1 다시 듣기 — 스크립트를 보며 틀렸던 부분 받아쓰기", LISTEN_1, 30)],
    "2026-12-21": [T("blog", "편지 쓰기 팁 11개 섹션 읽고, 아래 모범 편지 링크에서 항의 편지 1통 읽기", LETTER, 20)],
    "2026-12-22": [T("blog", "Speaking 허브의 모범 답안 목록에서 Part 3 답안 1개 읽기 (환경·기술 중)", L + "ielts-speaking-free-lessons-essential-tips/", 10)],
    "2026-12-23": [T("blog", "편지 페이지의 모범 편지 링크에서 친구에게 쓰는 편지 1통 읽기", LETTER, 10)],
    "2026-12-24": [T("blog", "도시 페이지의 Task 2 문제 5개 중 하나 골라 개요만 짜기", URBAN, 10)],
    "2026-12-26": [T("blog", "Task 2 주제별 질문 목록(100개 이상)을 훑고, 약한 주제 1개 골라 개요 짜기", W2, 15)],
    "2026-12-27": [T("mock", "British Council 공식 모의시험(Familiarisation Test, General Training): Listening + Reading 실전. 두 영역 결과는 무료로 확인돼요", FAMILIAR, 100)],
    "2026-12-30": [T("listening", "Listening Test 2 다시 듣기 — 스크립트 보며 따라 말하기 (감 유지)", LISTEN_2, 30)],
    "2027-01-02": [T("blog", "시험 당일 팁 페이지에서 'On the Day' 섹션(준비물·시간)만 읽기", L + "ielts-exam-tips-on-the-day/", 10)],
}
