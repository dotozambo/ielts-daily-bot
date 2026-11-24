# 5~6주차 (12/21 ~ 1/2) 정리 노트
from notes_lib import I, Q

W5 = {}

W5["2026-12-21"] = dict(
    summary="GT Writing Task 1은 150단어 이상의 편지를 20분 안에 써요. 문제에 나온 bullet point 3개에 빠짐없이 답하는 게 Task Achievement의 핵심이에요. 받는 사람에 따라 격식(Dear Sir or Madam) / 반격식(Dear Mr Kim) / 비격식(Dear Tom)으로 나뉘어요.",
    items=[
        I("I am writing to complain about ~", "~에 대해 항의하려고 씁니다",
          "편지 첫 문장에서 목적을 밝혀요. 진행형(am writing)이 정석이에요.",
          [("w", "I am writing to complain about the room I stayed in at your hotel last weekend."),
           ("w", "I am writing to complain about a faulty washing machine I bought from your shop.")],
          "✗ I write to complain → I am writing / ✗ complain for → about",
          "complain", "/kəmˈpleɪn/", "I am writing to complain about"),
        I("I am writing to enquire about ~", "~에 대해 문의하려고 씁니다",
          "영국식 enquire, 미국식 inquire 둘 다 OK.",
          [("w", "I am writing to enquire about the evening English courses at your college."),
           ("w", "I am writing to enquire about the apartment advertised on your website.")],
          "✗ enquire for → enquire about",
          "enquire", "/ɪnˈkwaɪə(r)/", "I am writing to enquire about"),
        I("I would be grateful if you could ~", "~해 주시면 감사하겠습니다",
          "격식 있는 요청. would와 맞춰 could를 써요.",
          [("w", "I would be grateful if you could refund the cost of the room."),
           ("w", "I would be grateful if you could send me more information about the fees.")],
          "✗ I would be grateful if you can → could",
          "grateful", "/ˈɡreɪtfl/", "I would be grateful if you could"),
        I("I look forward to hearing from you.", "답장 기다리겠습니다",
          "격식 편지의 마지막 문장. to는 전치사라 뒤에 -ing가 와요.",
          [("w", "I look forward to hearing from you soon."),
           ("w", "I look forward to your reply.")],
          "✗ I look forward to hear from you → hearing",
          "forward", "/ˈfɔːwəd/", "I look forward to hearing from you"),
        I("Yours faithfully, / Yours sincerely,", "맺음말 (격식)",
          "Dear Sir or Madam(이름 모름)이면 Yours faithfully, Dear Mr Park(이름 앎)이면 Yours sincerely.",
          [("w", "Dear Sir or Madam, ... Yours faithfully, Kim Minsoo"),
           ("w", "Dear Mr Park, ... Yours sincerely, Kim Minsoo")],
          "인사말과 맺음말이 안 맞으면 감점 포인트예요.",
          "faithfully", "/ˈfeɪθfəli/", "yours faithfully"),
    ],
    frame_tip="첫 문장에서 편지의 목적을 밝힐 때 써요. regarding = about (격식). 예: I am writing regarding the parcel I ordered last week.",
    extra="*🧭 격식 편지 구조 (150~180단어)*\n"
          "• Dear Sir or Madam,\n"
          "• *1문단*: 목적 (I am writing to ...)\n"
          "• *2~3문단*: bullet point 3개를 하나씩 (각 2~3문장)\n"
          "• *마지막 문단*: 요청 (I would be grateful if you could ...) + I look forward to hearing from you.\n"
          "• Yours faithfully, + 이름",
    quiz=[
        Q("틀린 곳 고치기: “I look forward to hear from you.”", "I look forward to *hearing* from you."),
        Q("Dear Sir or Madam으로 시작하면 맺음말은?", "Yours faithfully,"),
        Q("틀린 곳 고치기: “I would be grateful if you can help me.”", "... if you *could* help me."),
        Q("전치사: I am writing to complain ___ the noise.", "about"),
    ],
    model=dict(
        text="Dear Sir or Madam,\n\n"
             "I am writing to complain about the room I stayed in at your hotel from 5 to 7 December. I had booked a double room with a sea view, but when I arrived, I was given a small room facing the car park.\n\n"
             "(가운데 문단: bullet point 2~3에 대한 내용)\n\n"
             "I would be grateful if you could refund the difference in price between the two rooms. I look forward to hearing from you.\n\n"
             "Yours faithfully,\nKim Minsoo",
        why=["첫 문단에 목적(complain) + 구체적 상황(날짜, 예약한 방 vs 받은 방)을 넣었어요.",
             "마지막 문단은 원하는 해결책(refund) + 정해진 맺음 문장이에요.",
             "Dear Sir or Madam ↔ Yours faithfully를 맞췄어요."],
    ),
)

W5["2026-12-22"] = dict(
    summary="Part 3는 Part 2 주제를 사회 전체로 넓힌 토론 질문이에요. '나'에서 '사람들/사회'로 시점을 바꾸고, 과거·현재·미래를 비교하면 답이 깊어져요.",
    items=[
        I("I think the main reason is ...", "주된 이유는 ~ 같아요",
          "is 뒤에는 that절 또는 명사가 와요.",
          [("s", "I think the main reason is that people are busier than before."),
           ("s", "I think the main reason is the cost of housing.")],
          "✗ The main reason is because → The main reason is that",
          "reason", "/ˈriːzn/", "the main reason is"),
        I("That's a difficult question, but ...", "어려운 질문이지만",
          "생각할 시간을 벌어요. 시험 내내 한두 번만 쓰세요.",
          [("s", "That's a difficult question, but I'd say technology has made us less patient."),
           ("s", "That's a difficult question, but I think both have advantages.")],
          "매번 쓰면 외운 티가 나요.",
          None, None, "that's a difficult question"),
        I("In the future, I expect ...", "앞으로는 ~ 것 같아요",
          "expect 뒤에 (that) + 주어 + will + 동사.",
          [("s", "In the future, I expect more people will work from home."),
           ("s", "In the future, I expect AI will do many simple jobs.")],
          "✗ I expect people works → people will work",
          "expect", "/ɪkˈspekt/", "in the future I expect"),
        I("It's probably because ...", "아마 ~ 때문일 거예요",
          "확신이 없을 때 부드럽게 이유를 말해요.",
          [("s", "It's probably because young people use their phones more."),
           ("s", "It's probably because life in cities is so expensive.")],
          "probably 위치: be동사 뒤 / 일반동사 앞",
          "probably", "/ˈprɒbəbli/", "it's probably because"),
        I("compared to the past", "과거에 비해",
          "Compared to / with + 명사. 문장 앞에 쓰면 쉼표를 찍어요.",
          [("s", "Compared to the past, people travel abroad much more."),
           ("w", "Compared to the past, families today are much smaller.")],
          "✗ Compare to the past → Compared to the past",
          "compared", "/kəmˈpeəd/", "compared to the past"),
    ],
    frame_tip="과거와 현재를 대조할 때 써요. whereas = 반면에 (while로 바꿔도 돼요).",
    quiz=[
        Q("틀린 곳 고치기: “The main reason is because people are busy.”", "The main reason is *that* people are busy."),
        Q("형태: ______ to the past, prices are much higher. (compare)", "Compared"),
        Q("In the past people wrote letters, ______ nowadays they send messages.", "whereas"),
        Q("틀린 곳 고치기: “In the future, I expect people works from home.”", "... people *will work* from home."),
    ],
    model=dict(
        text="Q: How has technology changed the way people communicate?\n"
             "A: That's a difficult question, but I'd say technology has made communication much faster. In the past, people wrote letters or made phone calls, whereas nowadays we send messages instantly, even to people on the other side of the world. However, I think face-to-face conversations have become less common. It's probably because people find it easier to text than to talk. In the future, I expect video calls will become even more important, especially for work.",
        why=["과거(In the past) → 현재(nowadays) → 미래(In the future)로 시점을 옮기며 답했어요.",
             "변화 → 단점 → 이유 → 전망으로 1분 분량이에요.",
             "I가 아니라 people / we 시점으로 사회 전체를 이야기했어요."],
    ),
)

W5["2026-12-23"] = dict(
    summary="친구에게 쓰는 비격식 편지는 축약형(I'm, don't)과 구어 표현을 써도 돼요. 오히려 너무 딱딱하면 '어조(tone)'에서 감점돼요. 구조는 인사 → 목적 → bullet point 3개 → 마무리예요.",
    items=[
        I("It was great to hear from you.", "소식 들어서 반가웠어",
          "친구 편지의 첫 줄. Thanks for your letter.도 좋아요.",
          [("w", "Dear Tom, It was great to hear from you!"),
           ("w", "Thanks for your letter. It was great to hear your news.")],
          "친구에게 I am writing to inform you는 너무 격식 있어요.",
          None, None, "it was great to hear from you"),
        I("I'm writing to let you know that ~", "~를 알려주려고 편지 써",
          "let + 사람 + know (to 없이).",
          [("w", "I'm writing to let you know that I've moved to a new flat."),
           ("w", "I'm writing to let you know that I can't come to your party.")],
          "✗ let you to know → let you know",
          None, None, "let you know that"),
        I("Would you like to ~?", "~할래?",
          "초대·제안. Would you like to + 동사원형.",
          [("w", "Would you like to come over for dinner next Saturday?"),
           ("w", "Would you like to join us on the trip?")],
          "✗ Would you like come → to come",
          None, None, "would you like to come"),
        I("Sorry I couldn't ~", "~ 못해서 미안해",
          "make it = (모임에) 가다, 참석하다.",
          [("w", "Sorry I couldn't reply sooner; I've been really busy with work."),
           ("w", "Sorry I couldn't make it to your wedding.")],
          "make it을 알아두면 편지·말하기 모두에 유용해요.",
          None, None, "sorry I couldn't make it"),
        I("Hope to see you soon. / Best wishes,", "곧 보자 / 안부를 전하며",
          "친구 편지 맺음: Best wishes, / Take care, / Love, (가까운 사이).",
          [("w", "Hope to see you soon. Best wishes, Minsoo"),
           ("w", "Can't wait to see you! Love, Minsoo")],
          "친구에게 ✗ Yours faithfully",
          None, None, "hope to see you soon"),
    ],
    frame_tip="편지의 목적을 밝히는 비격식 버전이에요. 격식 편지의 I am writing to inform you that ...과 비교해서 기억하세요.",
    extra="*🧭 비격식 편지 구조 (150~180단어)*\n"
          "• Dear Jenny,\n"
          "• *1문단*: 안부 (It was great to hear from you!) + 목적 (I'm writing to let you know ...)\n"
          "• *2~3문단*: bullet point 3개 (축약형 OK: I'm, it's, don't)\n"
          "• *마지막*: Hope to see you soon! / Best wishes, + 이름",
    quiz=[
        Q("친구 편지 맺음말로 어색한 것: Best wishes / Yours faithfully / Take care", "Yours faithfully"),
        Q("틀린 곳 고치기: “Would you like come to my party?”", "Would you like *to come* ...?"),
        Q("Sorry I couldn't make ___ to your birthday.", "it"),
        Q("친구에게 맞게 바꾸기: “I am writing to inform you that I have moved.”", "*I'm writing to let you know that I've* moved."),
    ],
    model=dict(
        text="Dear Jenny,\n\n"
             "It was great to hear from you, and I'm glad your new job is going well!\n\n"
             "I'm writing to let you know that I've finally moved into my new apartment, and I'm having a small housewarming party. Would you like to come? It's on Saturday 10 January, from 6 p.m. The address is 25 Hangang-ro, Apartment 1203. It's only five minutes from Yongsan Station, so it's easy to find.\n\n"
             "I'm going to cook some Korean food, like bulgogi and japchae, so you don't need to bring anything to eat. But if you like, you could bring a dessert or something to drink. Also, feel free to bring your boyfriend. I'd love to meet him!\n\n"
             "Please let me know by Wednesday if you can come, so I know how much food to prepare.\n\n"
             "Hope to see you soon!\n\nBest wishes,\nMinsoo",
        why=["bullet point(날짜·장소, 음식, 가져올 것)를 문단마다 하나씩 다뤘어요.",
             "축약형과 느낌표로 친근한 어조를 유지했어요.",
             "약 160단어, 20분 안에 쓸 수 있는 분량이에요."],
    ),
)

W5["2026-12-24"] = dict(
    summary="도시 문제(교통 체증·집값·생활비)는 Task 2 '문제-해결' 유형 단골이에요. GT 편지 주제(이웃 소음, 이사)와도 겹쳐서 활용도가 높아요.",
    items=[
        I("traffic congestion", "교통 체증",
          "셀 수 없는 명사. 구어에선 traffic jam(셀 수 있음)을 많이 써요.",
          [("w", "Traffic congestion is a serious problem in most large cities."),
           ("s", "The traffic in Seoul is terrible during rush hour.")],
          "✗ traffic congestions / ✗ many traffic congestions",
          "congestion", "/kənˈdʒestʃən/", "traffic congestion"),
        I("commute to work", "통근하다",
          "commute는 동사·명사 둘 다 돼요 (my commute = 내 통근길).",
          [("w", "Many people spend two hours a day commuting to work."),
           ("s", "I commute to work by subway; it takes about 40 minutes.")],
          "✗ commute my work → commute to work",
          "commute", "/kəˈmjuːt/", "commute to work"),
        I("the cost of living", "생활비, 물가",
          "the를 붙여 고정 표현으로 써요.",
          [("w", "The cost of living in capital cities has risen sharply."),
           ("s", "The cost of living in Seoul is really high.")],
          "living cost보다 the cost of living이 자연스러워요.",
          None, None, "the cost of living"),
        I("affordable housing", "저렴한 주택",
          "housing은 셀 수 없는 명사(주택 전반). affordable = 감당할 수 있는 가격의.",
          [("w", "The government should build more affordable housing for young people."),
           ("s", "It's really hard to find affordable housing near my office.")],
          "✗ affordable housings",
          "affordable", "/əˈfɔːdəbl/", "affordable housing"),
        I("urban / rural areas", "도시 / 시골 지역",
          "rural 발음이 어려워요. 천천히 /ˈrʊərəl/.",
          [("w", "Young people are moving from rural areas to urban areas to find work."),
           ("s", "I grew up in a rural area, so city life was a big change for me.")],
          "발음: rural /ˈrʊərəl/ (루어럴)",
          "rural", "/ˈrʊərəl/", "rural areas"),
    ],
    frame_tip="해결 방법을 제시할 때 써요. by 뒤에는 명사나 -ing가 와요.",
    quiz=[
        Q("틀린 곳 고치기: “This problem can be solved by build more roads.”", "... by *building* more roads."),
        Q("The ______ of living in Seoul is very high.", "cost"),
        Q("틀린 곳 고치기: “There are many traffic congestions in my city.”", "There is *a lot of traffic congestion* in my city."),
        Q("I ______ to work by bus every day. (통근하다)", "commute"),
    ],
    model=dict(
        text="One of the main causes of traffic congestion is that too many people commute to work by car. This problem can be solved by improving public transport and making it cheaper, so that more people leave their cars at home.",
        why=["원인(One of the main causes) + 해결(can be solved by) + 결과(so that) 구조예요.",
             "2주차 환경 표현(public transport)을 재활용했어요.",
             "Task 2 본론 한 문단의 뼈대로 그대로 쓸 수 있어요."],
    ),
)

W5["2026-12-25"] = dict(
    summary="실전처럼 Writing 60분을 써 봐요. Task 1(편지)은 20분, Task 2(에세이)는 40분이에요. Task 2가 점수 비중이 더 크니 Task 1에서 시간을 넘기지 마세요.",
    items=[],
    extra="*📝 오늘의 실전 문제*\n\n"
          "*Task 1 (20분, 150단어 이상)*\n"
          "You recently bought a laptop online, but it arrived damaged. Write a letter to the company. In your letter:\n"
          "• describe what you bought\n• explain the problem\n• say what you would like the company to do\n\n"
          "*Task 2 (40분, 250단어 이상)*\n"
          "Some people think that the best way to improve public health is to build more sports facilities. Others think that other measures are needed. Discuss both views and give your own opinion.\n\n"
          "*⏱ 시간 배분*\n"
          "• Task 1: 계획 3분 → 쓰기 15분 → 검토 2분\n"
          "• Task 2: 계획 5분 → 쓰기 30분 → 검토 5분\n"
          "• 끝나고 막힌 표현을 메모해 두세요 (내일 채우기 재료)",
    quiz=None,
    model=dict(
        text="[Task 1 모범 답안]\n\nDear Sir or Madam,\n\n"
             "I am writing to complain about a laptop I ordered from your website on 15 December (order number 48213). It was a silver 14-inch model, and I paid for express delivery because I needed it for work.\n\n"
             "Unfortunately, when the parcel arrived, the box was badly damaged, and the laptop screen had a large crack across it. As a result, I cannot use the laptop at all. I have attached some photos of the damage to this letter.\n\n"
             "I would be grateful if you could send me a replacement as soon as possible. If this is not possible, I would like a full refund, including the delivery charge. I would also appreciate it if you could arrange for the damaged laptop to be collected from my address.\n\n"
             "I look forward to hearing from you.\n\nYours faithfully,\nKim Minsoo\n\n"
             "[Task 2 뼈대]\n"
             "서론: Some people believe that ..., while others argue that ... + 내 입장\n"
             "본론 1: 시설 찬성 — 접근성, 운동 습관 (take regular exercise)\n"
             "본론 2: 다른 방법 — junk food 광고 제한, 학교 교육 (lead a healthy lifestyle)\n"
             "결론: In conclusion, although ..., I believe that ...",
        why=["Task 1은 bullet point 3개를 문단마다 하나씩 다뤘어요 (약 170단어).",
             "Task 2는 3주차 건강 표현이 그대로 쓰이는 문제예요.",
             "실전에서 막힌 표현은 내일(12/26) 표현 칸에 직접 채워 넣으세요."],
    ),
)

W5["2026-12-26"] = dict(
    summary="어제 모의고사에서 막힌 표현을 내 것으로 만드는 날이에요. '틀린 문장 → 고친 문장 → 규칙' 3줄로 정리하면 시험 전까지 반복해서 볼 수 있어요.",
    items=[],
    extra="*📒 오류 노트 쓰는 법*\n"
          "```\n✗ I am writing to complain the laptop.\n✓ I am writing to complain about the laptop.\n규칙: complain about + 명사\n```\n"
          "• 어제 쓴 글에서 오류 5개를 골라 위 형식으로 적어요\n"
          "• Supabase `ielts_days` 테이블의 12/26 행 `expressions` 칸에 넣으면 이후 복습 메시지에 나와요\n"
          "   형식: `[{\"en\": \"complain about ~\", \"ko\": \"~에 대해 항의하다\"}]`\n"
          "• Liz의 최근 출제 주제 페이지에서 내가 약한 주제를 하나 골라 훑어보세요",
    quiz=None,
    model=None,
)

W5["2026-12-27"] = dict(
    summary="Speaking 실전 10분 연습이에요. Part 1 질문 6개 → Part 2 큐카드 1장을 쉬지 않고 이어서 녹음하세요.",
    items=[],
    extra="*🎤 오늘의 실전 순서*\n"
          "*Part 1 (4~5분)*\n"
          "1. Do you work or study?\n2. Do you like your hometown? Why?\n3. What do you do in your free time?\n"
          "4. How often do you use your phone?\n5. Do you prefer eating out or cooking at home?\n6. How do you usually get the news?\n\n"
          "*Part 2 (1분 준비 + 2분)*\n"
          "Describe a skill you would like to learn. You should say: what it is / why you want to learn it / how you would learn it / and explain how it would help you.\n\n"
          "*✅ 녹음 듣고 체크*: 답마다 이유가 하나 있었나? · 2분을 채웠나? · used to, I'd say 같은 표현을 썼나?",
    quiz=None,
    model=None,
)

_FINAL_TIP = ("*🔁 최종 복습 방법*\n"
              "• 아래 복습 목록의 영어 표현을 보고 한국어 뜻을 먼저 떠올리세요\n"
              "• 그다음 '복습 뜻 보기'로 확인 → 못 떠올린 표현만 메모\n"
              "• 메모한 표현으로 문장을 하나씩 소리 내 말해 보세요")

for _d, _wk in (("2026-12-28", "1주차 (교육·일·연결어)"), ("2026-12-29", "2주차 (기술·환경·바꿔 말하기)"),
                ("2026-12-30", "3주차 (범죄·정부·건강·광고·미디어)"), ("2026-12-31", "4주차 (Speaking)")):
    W5[_d] = dict(summary=f"{_wk} 표현을 다시 꺼내 보는 날이에요. 새 표현은 없어요.",
                  items=[], extra=_FINAL_TIP, quiz=None, model=None)

W5["2027-01-01"] = dict(
    summary="그동안 배운 문장 틀을 한 번에 보는 날이에요. 시험장에서 바로 꺼내 쓸 수 있게 소리 내 읽어 보세요.",
    items=[],
    extra="*✍️ Writing 문장 틀*\n"
          "• Some people believe that ..., while others argue that ...\n• It is often argued that ...\n"
          "• Although ..., I believe that ...\n• In my opinion, ... because ...\n"
          "• One advantage / disadvantage of ... is that ...\n• One of the main causes of ... is ...\n"
          "• One possible solution to this problem is to ...\n• This problem can be solved by ...\n"
          "• Instead of ..., governments should ...\n• ... can be detrimental to ...\n• In conclusion, ...\n\n"
          "*✉️ 편지*\n• I am writing to complain about / enquire about ...\n• I would be grateful if you could ...\n"
          "• I look forward to hearing from you. → Yours faithfully / sincerely\n• I'm writing to let you know that ... → Best wishes\n\n"
          "*🗣 Speaking*\n• To be honest, ... / Actually, ...\n• I'd say ..., mainly because ...\n• It depends on ... For example, ...\n"
          "• I used to ..., but now ...\n• I'd like to talk about ... The reason I chose ... is ...\n"
          "• Looking back, I think ...\n• In the past ..., whereas nowadays ...",
    quiz=None,
    model=None,
)

W5["2027-01-02"] = dict(
    summary="내일이 시험이에요. 새로 외우지 말고 컨디션을 챙기세요. 지금까지 40일 동안 쌓은 표현이면 충분해요.",
    items=[],
    extra="*✅ 시험 전날 체크*\n"
          "• 준비물·입실 시간은 접수 확인 메일 기준으로 다시 확인 (신분증은 접수할 때 쓴 것과 같은 것)\n"
          "• 시험장까지 가는 길과 걸리는 시간 확인\n\n"
          "*🧠 시험장에서 기억할 3가지*\n"
          "• Writing: Task 1은 20분에서 끊기. bullet point 3개 모두 답하기\n"
          "• Speaking: 답마다 이유 하나. 모르는 질문엔 I've never really thought about it, but ...\n"
          "• Listening·Reading: 한 문제에 오래 머물지 말고 넘어가기\n\n"
          "오늘은 문장 틀만 한 번 훑고 일찍 자요. 화이팅! 💪",
    quiz=None,
    model=None,
)
