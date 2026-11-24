# 4주차 (12/14 ~ 12/20) 정리 노트 — Speaking 주간
from notes_lib import I, Q

W4 = {}

W4["2026-12-14"] = dict(
    summary="Speaking Part 1은 4~5분 동안 일상 질문 10~12개가 나와요. 길게 말하기보다 '바로 답 + 이유나 예시 하나'가 핵심이에요. 고향·집은 거의 매번 첫 주제예요.",
    items=[
        I("I grew up in ~", "~에서 자랐어요",
          "grow up의 과거형 grew up. 수동태로 쓰지 않아요.",
          [("s", "I grew up in Busan, but I've lived in Seoul for ten years."),
           ("s", "I grew up in a small town, so I'm used to a quiet life.")],
          "✗ I was grown up in → I grew up in",
          "grew", "/ɡruː/", "I grew up in"),
        I("It's a fairly quiet area", "꽤 조용한 동네예요",
          "fairly / quite / pretty(구어) + 형용사로 정도를 조절해요.",
          [("s", "It's a fairly quiet area, so it's good for families."),
           ("s", "My neighbourhood is pretty busy at night because there are lots of restaurants.")],
          "✗ It's very quiet place → It's a very quiet place (관사 a)",
          "fairly", "/ˈfeəli/", "it's a fairly quiet"),
        I("a convenient location", "편리한 위치",
          "형용사 convenient, 명사 convenience.",
          [("s", "My apartment is in a convenient location, near a subway station."),
           ("s", "The best thing about my office is its convenient location.")],
          "✗ convenience location → convenient location",
          "convenient", "/kənˈviːniənt/", "convenient location"),
        I("I live in an apartment", "아파트에 살아요",
          "영국 flat, 미국 apartment 둘 다 OK. 관사 an 잊지 마세요.",
          [("s", "I live in an apartment on the 15th floor."),
           ("s", "Like most people in Korea, I live in an apartment.")],
          "✗ I live in apartment → in an apartment",
          "apartment", "/əˈpɑːtmənt/", "I live in an apartment"),
        I("The best thing about ~ is ...", "~의 가장 좋은 점은",
          "about을 써요. 반대는 The worst thing about ~ is ...",
          [("s", "The best thing about my hometown is the food."),
           ("s", "The best thing about living in Seoul is the public transport.")],
          "✗ The best thing of → about",
          None, None, "the best thing about"),
    ],
    frame_tip="답을 시작하면서 생각할 시간을 벌고 자연스럽게 들리게 해요. 매 답마다 쓰면 어색하니 2~3번에 한 번만. Actually는 '사실은(예상과 다르게)' 뉘앙스예요.",
    quiz=[
        Q("틀린 곳 고치기: “I was grown up in Daegu.”", "*I grew up* in Daegu."),
        Q("틀린 곳 고치기: “It's very convenience location.”", "It's *a* very *convenient* location."),
        Q("전치사: The best thing ___ my hometown is the beach.", "about"),
        Q("관사: “I live in ___ apartment near the river.”", "an"),
    ],
    model=dict(
        text="Q: Where are you from?\nA: I'm from Seoul, but actually I grew up in a small city called Cheongju. I moved to Seoul for university.\n\n"
             "Q: Do you like your hometown?\nA: Yes, I do. It's a fairly quiet area, and the best thing about it is that it's close to the mountains.\n\n"
             "Q: Do you live in a house or an apartment?\nA: I live in an apartment, like most people in Korea. It's in a convenient location, right next to a subway station.\n\n"
             "Q: What would you change about your home?\nA: To be honest, I'd like a bigger kitchen, because I enjoy cooking and ours is really small.",
        why=["모든 답이 '바로 답 + 디테일 하나'로 2문장이에요.",
             "Actually, To be honest를 한 번씩만 썼어요.",
             "답변 내용은 사실이 아니어도 돼요. 채점은 영어만 봐요."],
    ),
)

W4["2026-12-15"] = dict(
    summary="취미·영화는 Part 1 단골이고 Part 2(좋아하는 영화 묘사)로도 이어져요. 현재 취미 + 과거와 비교(used to)를 넣으면 문법 다양성 점수를 받아요.",
    items=[
        I("in my free time", "여가 시간에",
          "free time은 셀 수 없는 명사. spare time도 같은 뜻이에요.",
          [("s", "In my free time, I like going for walks along the river."),
           ("s", "I don't have much free time these days because of work.")],
          "✗ in my free times / ✗ at my free time",
          None, None, "in my free time"),
        I("I'm really into ~", "~에 푹 빠져 있어요",
          "into + 명사 / -ing. 구어에서 아주 자연스러운 표현이에요.",
          [("s", "I'm really into cooking at the moment."),
           ("s", "My friend is really into K-pop; she goes to every concert.")],
          "✗ I'm really into to cook → into cooking",
          None, None, "I'm really into"),
        I("an action film / a comedy", "액션 영화 / 코미디",
          "다른 장르: thriller, romantic comedy, documentary, animated film, horror film. 미국식은 movie.",
          [("s", "I usually watch action films because they're exciting."),
           ("s", "When I'm tired, I prefer a light comedy.")],
          "a comedy movie도 되지만 a comedy로 충분해요.",
          "comedy", "/ˈkɒmədi/", "action films"),
        I("It helps me relax", "긴장을 풀어줘요",
          "help + 사람 + 동사원형.",
          [("s", "Watching films helps me relax after work."),
           ("s", "Cooking helps me forget about stress.")],
          "✗ helps me relaxing → helps me relax",
          "relax", "/rɪˈlæks/", "helps me relax"),
        I("I used to ..., but now ...", "예전엔 ~했지만 지금은",
          "used to + 동사원형. 현재형 use to는 없어요.",
          [("s", "I used to go to the cinema every week, but now I watch everything on Netflix."),
           ("s", "I used to play computer games a lot, but now I don't have time.")],
          "✗ I used to going / 발음: used /juːst/ (유스트, 유즈드 아님)",
          "used", "/juːst/", "I used to"),
    ],
    frame_tip="선호·빈도 질문에 답할 때 써요. I'd say = I would say (단정 대신 부드럽게). mainly because로 이유를 하나 붙여요.",
    quiz=[
        Q("틀린 곳 고치기: “I used to playing tennis.”", "I used to *play* tennis."),
        Q("I'm really ______ hiking these days.", "into"),
        Q("틀린 곳 고치기: “Music helps me relaxing.”", "helps me *relax*"),
        Q("발음: used to의 used는? (유즈드 / 유스트)", "유스트 /juːst/"),
    ],
    model=dict(
        text="Q: What do you do in your free time?\nA: In my free time, I'm really into cooking. I try new recipes on weekends, and it helps me relax after a busy week.\n\n"
             "Q: What kind of films do you like?\nA: I'd say action films, mainly because they're exciting and easy to watch when I'm tired. But I also enjoy a good comedy.\n\n"
             "Q: How often do you watch films?\nA: I used to go to the cinema every week, but now I mostly watch films at home, maybe once or twice a week.",
        why=["현재(I'm into) + 과거(used to) 시제를 섞어서 문법 다양성을 보여줬어요.",
             "I'd say ..., mainly because ... 틀을 그대로 썼어요.",
             "각 답 2문장, 15~20초 분량이에요."],
    ),
)

W4["2026-12-16"] = dict(
    summary="음식·옷도 Part 1에 자주 나와요. “It depends”로 시작해서 두 가지 상황을 비교하면 답이 자연스럽게 길어져요.",
    items=[
        I("I prefer casual clothes", "편한 옷을 선호해요",
          "prefer A to B (than 아님).",
          [("s", "I prefer casual clothes, like jeans and T-shirts."),
           ("s", "I prefer comfortable clothes to fashionable ones.")],
          "✗ prefer A than B → prefer A to B",
          "casual", "/ˈkæʒuəl/", "casual clothes"),
        I("dress up for ~", "~을 위해 차려입다",
          "dress up = 격식 있게 차려입다. 그냥 옷을 입다는 get dressed.",
          [("s", "I only dress up for weddings or important meetings."),
           ("s", "People in Seoul often dress up for a night out.")],
          "dress up(차려입다)과 get dressed(옷을 입다)를 구분해요.",
          None, None, "dress up for"),
        I("home-cooked meals", "집밥",
          "home-made food도 같은 뜻이에요.",
          [("s", "Nothing beats my mum's home-cooked meals."),
           ("s", "I try to eat home-cooked meals because they're healthier.")],
          "하이픈 주의: home-cooked",
          "cooked", "/kʊkt/", "home-cooked meals"),
        I("eat out", "외식하다",
          "목적어 없이 써요.",
          [("s", "We usually eat out on Friday nights."),
           ("s", "Eating out is getting more expensive in Korea.")],
          "✗ eat out food / ✗ eat outside (밖에서, 즉 야외에서 먹다는 뜻이 돼요)",
          None, None, "eat out"),
        I("It depends on ~", "~에 따라 달라요",
          "depend on + 명사 / wh-절.",
          [("s", "It depends on the weather."),
           ("s", "It depends on who I'm with.")],
          "✗ It depends of / ✗ It's depend on",
          "depends", "/dɪˈpendz/", "it depends on"),
    ],
    frame_tip="“어느 쪽이 좋아요?” 질문에 상황별로 답할 때 써요. It depends로 끝내지 말고 반드시 For example로 두 상황을 보여주세요.",
    quiz=[
        Q("전치사: It depends ___ my mood.", "on"),
        Q("틀린 곳 고치기: “I prefer jeans than suits.”", "I prefer jeans *to* suits."),
        Q("틀린 곳 고치기: “We eat outside at a restaurant every Friday.”", "We *eat out* every Friday."),
        Q("I usually ______ ___ for weddings. (차려입다)", "dress up"),
    ],
    model=dict(
        text="Q: What kind of clothes do you usually wear?\nA: I prefer casual clothes, like jeans and a sweatshirt. I only dress up for special occasions, such as weddings.\n\n"
             "Q: Do you prefer eating out or cooking at home?\nA: It depends on how busy I am. For example, on weekdays I often eat out because I'm tired, but on weekends I enjoy home-cooked meals.\n\n"
             "Q: What's your favourite food?\nA: I'd say kimchi stew. It's simple, but it reminds me of my mum's cooking.",
        why=["It depends on → For example → but 구조로 두 상황을 비교했어요.",
             "such as로 예시를 들었어요.",
             "어제 틀(I'd say)도 재활용했어요."],
    ),
)

W4["2026-12-17"] = dict(
    summary="Part 2는 큐카드를 받고 1분 준비, 1~2분 말하기예요. 큐카드의 질문 4개(누구 / 어떻게 알게 됐나 / 어떤 사람인가 / 왜)를 순서대로 답하면 구조가 저절로 잡혀요.",
    items=[
        I("someone I really look up to", "정말 존경하는 사람",
          "look up to = admire (구어). 사람을 소개하는 첫 문장으로 좋아요.",
          [("s", "I'd like to talk about someone I really look up to, my old manager."),
           ("s", "I've always looked up to my grandfather.")],
          "✗ look up to at",
          None, None, "look up to"),
        I("get on well with ~", "~와 잘 지내다",
          "영국식이에요. 미국식은 get along with.",
          [("s", "We get on well with each other because we have similar interests."),
           ("s", "I didn't get on well with him at first.")],
          "✗ get well with → get on well with",
          None, None, "get on well with"),
        I("hard-working / patient", "성실한 / 인내심 있는",
          "형용사 뒤에 항상 예시를 붙이세요. 그래야 시간이 채워져요.",
          [("s", "She's incredibly hard-working; she's always the first to arrive."),
           ("s", "He's very patient with beginners.")],
          "발음: patient /ˈpeɪʃnt/ (페이션트)",
          "patient", "/ˈpeɪʃnt/", "very patient"),
        I("have a big influence on ~", "~에게 큰 영향을 주다",
          "전치사는 on. influence의 강세는 첫 음절이에요.",
          [("s", "My teacher had a big influence on my career."),
           ("s", "Living abroad had a big influence on the way I think.")],
          "✗ influence to → influence on",
          "influence", "/ˈɪnfluəns/", "big influence on"),
        I("I first met him/her when ...", "처음 만난 건 ~ 때예요",
          "first는 met 앞에 와요. 또는 for the first time.",
          [("s", "I first met her when I started my first job."),
           ("s", "I first met him when we were in the same class at university.")],
          "✗ I met him first time → for the first time",
          None, None, "I first met her when"),
    ],
    frame_tip="Part 2의 시작과 마무리 문장이에요. 시작: I'd like to talk about ... / 마무리: The reason I chose her is that ...",
    quiz=[
        Q("전치사: She had a big influence ___ me.", "on"),
        Q("틀린 곳 고치기: “I get well with my colleagues.”", "I *get on well with* my colleagues."),
        Q("발음: patient의 강세는? (PAY-shnt / pa-TIENT)", "첫 음절 PAY-shnt /ˈpeɪʃnt/"),
        Q("My father is someone I really look ___ ___.", "up to"),
    ],
    model=dict(
        text="I'd like to talk about someone I really look up to, my first manager at work. I first met her when I joined my company about ten years ago. I was very nervous at that time, because I had no experience.\n\n"
             "She was incredibly hard-working. She always arrived early, and she never left a problem unfinished. She was also very patient. When I made mistakes, she didn't get angry. Instead, she explained what went wrong and helped me fix it.\n\n"
             "We got on well with each other, even though she was much older than me. We often had lunch together and talked about our families and hobbies.\n\n"
             "The reason I chose her is that she had a big influence on my career. Because of her, I learned how to plan my work and communicate clearly. Now I try to treat new team members in the same way she treated me.\n\n"
             "We don't work together anymore, but we still keep in touch, and I sometimes ask her for advice.",
        why=["큐카드 순서(누구 → 만남 → 어떤 사람 → 왜)대로 말했어요. 약 2분 분량이에요.",
             "형용사(hard-working, patient)마다 구체적인 예시를 붙였어요.",
             "마지막에 현재 이야기(keep in touch)로 자연스럽게 마무리했어요."],
    ),
)

W4["2026-12-18"] = dict(
    summary="장소 묘사는 '위치 → 모습 → 거기서 하는 일 → 느낌' 순서로 말하면 돼요. 감각 표현(조용한, 붐비는)을 하나 넣으면 생생해져요.",
    items=[
        I("It's located in ~", "~에 있어요",
          "be located in / on / near. 능동태 locate로 쓰지 않아요.",
          [("s", "It's located in the north of Seoul, about an hour from my home."),
           ("s", "The café is located on a small street near the river.")],
          "✗ It locates in → It's located in",
          "located", "/ləʊˈkeɪtɪd/", "it's located in"),
        I("crowded / peaceful", "붐비는 / 평화로운",
          "get crowded (붐비게 되다)로도 자주 써요.",
          [("s", "It gets really crowded on weekends."),
           ("s", "Early in the morning it's very peaceful.")],
          "✗ It's crowd → It's crowded",
          "crowded", "/ˈkraʊdɪd/", "really crowded"),
        I("green spaces", "녹지 공간",
          "도시의 공원·숲 등을 통틀어 말할 땐 복수형이에요. Writing에도 좋아요.",
          [("s", "Seoul has more green spaces than people think."),
           ("w", "Cities need more green spaces where children can play.")],
          "전체를 말할 땐 green spaces (복수)",
          None, None, "green spaces"),
        I("a great place to unwind", "쉬기 좋은 곳",
          "unwind = relax. 발음 /ʌnˈwaɪnd/ (언와인드). wind가 '감다'라는 뜻일 때 발음이에요.",
          [("s", "The park is a great place to unwind after work."),
           ("s", "For me, the beach is the best place to unwind.")],
          "✗ 언윈드 (바람 wind 발음) → 언와인드",
          "unwind", "/ʌnˈwaɪnd/", "place to unwind"),
        I("I'd recommend it to ~", "~에게 추천하고 싶어요",
          "recommend + 사물 + to + 사람 / recommend + -ing.",
          [("s", "I'd recommend it to anyone who likes nature."),
           ("s", "I'd definitely recommend visiting it in autumn.")],
          "✗ I'd recommend to visit it → I'd recommend visiting it",
          "recommend", "/ˌrekəˈmend/", "I'd recommend it to"),
    ],
    frame_tip="가장 좋은 점을 강조할 때 써요. What I like most about it is that + 문장 / is + 명사.",
    quiz=[
        Q("틀린 곳 고치기: “The park locates near my house.”", "The park *is located* near my house."),
        Q("틀린 곳 고치기: “I'd recommend to visit it in spring.”", "I'd recommend *visiting* it in spring."),
        Q("The beach is a great place to ______. (쉬다, un-으로 시작)", "unwind"),
        Q("형태: “It gets really ______ on weekends.” (crowd)", "crowded"),
    ],
    model=dict(
        text="I'd like to talk about a park I like to visit, Seoul Forest. It's located in the east of Seoul, near the Han River, and it takes me about thirty minutes to get there by subway.\n\n"
             "It's a huge park with lots of green spaces, a small lake and some walking paths. There's also an area where you can see deer, which is quite unusual for a city park.\n\n"
             "I usually go there on Sunday mornings. I take a long walk, sometimes have a coffee, and just sit on a bench and watch people. It gets really crowded in the afternoon, but early in the morning it's very peaceful.\n\n"
             "What I like most about it is that it doesn't feel like you're in the city at all. After a stressful week, it's a great place to unwind.\n\n"
             "I'd recommend it to anyone who visits Seoul, especially people who like nature.",
        why=["위치 → 모습 → 하는 일 → 느낌 → 추천 순서예요.",
             "crowded / peaceful로 시간대에 따른 대비를 보여줬어요.",
             "오늘 표현 5개 + 문장 틀을 모두 썼어요."],
    ),
)

W4["2026-12-19"] = dict(
    summary="모르는 주제나 경험이 없는 큐카드가 나와도 멈추면 안 돼요. 시간을 버는 표현으로 시작하고, 비슷한 경험이나 지어낸 이야기로 2분을 채우세요. 내용이 사실인지는 채점하지 않아요.",
    items=[
        I("I've never really thought about it, but ...", "생각해 본 적은 없지만",
          "현재완료(I've never)가 자연스러워요.",
          [("s", "I've never really thought about it, but I'd say my favourite season is autumn."),
           ("s", "I've never really thought about it before, but I suppose I'm quite a patient person.")],
          "✗ I never thought about it (가능하지만 현재완료가 더 자연스러워요)",
          None, None, "never really thought about it"),
        I("If I had to choose, I'd say ...", "굳이 고르자면",
          "가정법이라 had ... would로 맞춰요.",
          [("s", "If I had to choose, I'd say summer, because I love the beach."),
           ("s", "If I had to choose one thing, I'd say my phone.")],
          "✗ If I have to choose, I would say → If I had to choose, I'd say",
          None, None, "if I had to choose"),
        I("a memorable experience", "기억에 남는 경험",
          "memorable의 강세는 첫 음절이에요.",
          [("s", "One memorable experience was my first trip abroad."),
           ("s", "Volunteering at a charity event was a really memorable experience.")],
          "발음: /ˈmemərəbl/ (MEM-er-a-ble)",
          "memorable", "/ˈmemərəbl/", "memorable experience"),
        I("It made me realise that ...", "~을 깨닫게 했어요",
          "make + 사람 + 동사원형. 영국식 realise, 미국식 realize.",
          [("s", "It made me realise that small actions can help people."),
           ("s", "The trip made me realise how lucky I am.")],
          "✗ made me to realise → made me realise",
          "realise", "/ˈrɪəlaɪz/", "made me realise"),
        I("Looking back, ...", "돌이켜보면",
          "Part 2 마무리에서 느낌이나 교훈을 말할 때 좋아요.",
          [("s", "Looking back, I think I was too nervous."),
           ("s", "Looking back, it was one of the best decisions I've ever made.")],
          "✗ Look back, ... → Looking back, ...",
          None, None, "looking back"),
    ],
    frame_tip="Part 2 마무리 문장이에요. 지금의 관점에서 그 경험을 평가하면 시제 다양성(과거 + 현재)도 보여줄 수 있어요.",
    quiz=[
        Q("틀린 곳 고치기: “It made me to realise that I was wrong.”", "It *made me realise* that I was wrong."),
        Q("시제: If I ___ to choose, I'd say coffee. (have / had)", "had"),
        Q("______ back, I think it was a good decision.", "Looking"),
        Q("강세: memorable — MEM-or-a-ble / me-MOR-a-ble", "첫 음절 MEM-or-a-ble"),
    ],
    model=dict(
        text="I'd like to talk about a time when I helped an elderly man at a subway station. It happened about two years ago, on a cold winter evening.\n\n"
             "I was on my way home from work when I saw an old man standing in front of the ticket machine. He looked confused, and people were just walking past him. To be honest, I was tired and wanted to go home, but I decided to ask if he needed help.\n\n"
             "It turned out that he didn't know how to use the machine, and he was also about to take the wrong line. I bought him a ticket and walked with him to the right platform. It only took about ten minutes, but he thanked me many times.\n\n"
             "It was a memorable experience, because it made me realise that small actions can really help people. Looking back, I almost didn't stop, and I'm glad I did. Since then, I try to pay more attention to people around me who might need help.",
        why=["언제 → 무슨 일 → 내가 한 일 → 느낀 점 순서예요.",
             "과거 시제로 이야기하고, 마지막에 현재(Since then, I try ...)로 마무리했어요.",
             "To be honest로 솔직한 감정을 넣으니 이야기가 자연스러워져요."],
    ),
)

W4["2026-12-20"] = dict(
    summary="Part 2 실전 연습이에요. 큐카드 3장을 1분 메모 → 2분 말하기로 연속해서 녹음해 보세요. 메모는 문장이 아니라 키워드로 쓰는 게 핵심이에요.",
    items=[],
    extra="*📝 1분 메모 예시* (Describe a time you helped someone)\n"
          "```\n누구/언제: old man · subway · 2 yrs ago · winter\n"
          "상황: confused · ticket machine · people walking past\n"
          "내가 한 일: bought ticket · walked to platform · 10 min\n"
          "느낌: memorable · made me realise · looking back\n```\n"
          "*✅ 녹음 듣고 체크*\n"
          "• 2분 가까이 말했나? (1분 30초 미만이면 디테일 추가)\n"
          "• 같은 단어를 반복하지 않았나? (good, nice → helpful, peaceful ...)\n"
          "• 과거 시제를 유지했나? (I go → I went)\n"
          "• 마무리 문장(Looking back / The reason I chose)이 있었나?",
    quiz=None,
    model=None,
)
