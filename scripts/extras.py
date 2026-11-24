# 매일 추가 표현: 구문 5개 + 단어 5개 (새 표현을 배우는 날만)
# P(구문, 뜻, 예문) / Wd(단어, IPA, 뜻, 예문)
from notes_lib import P, Wd

EXTRAS = {}


def X(day, phrases, words):
    EXTRAS[day] = {"phrases": phrases, "words": words}


# ───────── 1주차 ─────────
X("2026-11-24",
  [P("drop out of school", "학교를 중퇴하다", "Some students drop out of school because they need to earn money."),
   P("a well-rounded education", "균형 잡힌 교육", "Sport and music are part of a well-rounded education."),
   P("lifelong learning", "평생 학습", "Lifelong learning is essential in a fast-changing job market."),
   P("put pressure on ~", "~에게 압박을 주다", "Many parents put too much pressure on their children to get good grades."),
   P("apply for a scholarship", "장학금을 신청하다", "I applied for a scholarship to study abroad.")],
  [Wd("curriculum", "/kəˈrɪkjələm/", "교육과정", "The school curriculum should include more practical subjects."),
   Wd("graduate", "/ˈɡrædʒuət/", "졸업생 (명사)", "Many graduates struggle to find a job in their field."),
   Wd("literacy", "/ˈlɪtərəsi/", "읽고 쓰는 능력", "Computer literacy is as important as reading today."),
   Wd("vocational", "/vəʊˈkeɪʃənl/", "직업의, 직업 교육의", "Vocational courses prepare students for specific jobs."),
   Wd("academic", "/ˌækəˈdemɪk/", "학문의, 학업의", "Some students are good at academic subjects, while others prefer hands-on work.")])

X("2026-11-25",
  [P("pay attention in class", "수업에 집중하다", "It is harder for children to pay attention in class when they are tired."),
   P("at any time", "언제든지", "With online courses, students can study at any time."),
   P("ask questions", "질문하다", "In a classroom, students can ask questions immediately."),
   P("study from home", "집에서 공부하다", "Studying from home saves time and money."),
   P("motivate students to ~", "학생들이 ~하도록 동기를 주다", "Good teachers motivate students to work harder.")],
  [Wd("flexible", "/ˈfleksəbl/", "유연한", "Online learning is more flexible than classroom learning."),
   Wd("distraction", "/dɪˈstrækʃn/", "방해 요소, 주의를 흩뜨리는 것", "Phones are a major distraction for students."),
   Wd("discipline", "/ˈdɪsəplɪn/", "규율, 자제력", "Studying online requires a lot of self-discipline."),
   Wd("isolated", "/ˈaɪsəleɪtɪd/", "고립된", "Some online learners feel isolated from other students."),
   Wd("concentrate", "/ˈkɒnsntreɪt/", "집중하다", "I can't concentrate when there is a lot of noise.")])

X("2026-11-26",
  [P("work from home", "재택근무를 하다", "Many companies now allow employees to work from home two days a week."),
   P("a nine-to-five job", "평범한 사무직 (9시~5시 일)", "I don't want a nine-to-five job; I prefer flexible hours."),
   P("get promoted", "승진하다", "She got promoted after only two years."),
   P("be under a lot of pressure", "압박을 많이 받다", "Doctors are often under a lot of pressure at work."),
   P("change careers", "직업을 바꾸다", "More people are changing careers in their thirties and forties.")],
  [Wd("colleague", "/ˈkɒliːɡ/", "직장 동료", "I get on well with most of my colleagues."),
   Wd("employer", "/ɪmˈplɔɪə(r)/", "고용주", "Employers value communication skills."),
   Wd("deadline", "/ˈdedlaɪn/", "마감일", "I work long hours when there is a tight deadline."),
   Wd("unemployment", "/ˌʌnɪmˈplɔɪmənt/", "실업", "Youth unemployment is a serious problem in many countries."),
   Wd("stressful", "/ˈstresfl/", "스트레스가 많은", "My job can be stressful, but it is never boring.")])

X("2026-11-27",
  [P("in other words,", "다시 말해", "Prices have doubled. In other words, people can buy half as much."),
   P("on top of that,", "게다가 (구어)", "It's cheap. On top of that, it's really close to my house."),
   P("as a consequence,", "그 결과로 (격식)", "Sea levels are rising. As a consequence, some islands may disappear."),
   P("for instance,", "예를 들어 (For example과 같은 뜻)", "Many jobs require teamwork. For instance, nurses work closely with doctors."),
   P("because of + 명사", "~ 때문에 (말하기·쓰기 모두)", "I was late because of the traffic.")],
  [Wd("furthermore", "/ˌfɜːðəˈmɔː(r)/", "더욱이 (격식)", "Furthermore, online courses are often cheaper."),
   Wd("nevertheless", "/ˌnevəðəˈles/", "그럼에도 불구하고", "The job is stressful. Nevertheless, I enjoy it."),
   Wd("consequently", "/ˈkɒnsɪkwəntli/", "결과적으로", "Fewer people are having children. Consequently, the population is getting older."),
   Wd("similarly", "/ˈsɪmələli/", "마찬가지로", "Children need exercise. Similarly, adults need to stay active."),
   Wd("whereas", "/ˌweərˈæz/", "반면에", "My brother loves sport, whereas I prefer reading.")])

X("2026-11-28",
  [P("despite + 명사/-ing", "~에도 불구하고", "Despite the high cost, many students choose to study abroad."),
   P("even though + 문장", "비록 ~이지만 (although보다 강조)", "Even though I was tired, I finished my homework."),
   P("to sum up,", "요약하자면", "To sum up, both sides have valid points."),
   P("on balance,", "모든 걸 고려하면", "On balance, I believe the advantages outweigh the disadvantages."),
   P("the advantages outweigh the disadvantages", "장점이 단점보다 크다", "In my view, the advantages of online learning outweigh the disadvantages.")],
  [Wd("whereby", "/weəˈbaɪ/", "그것에 의하여 (격식, 제도 설명)", "There is a system whereby students can borrow money for tuition."),
   Wd("thus", "/ðʌs/", "따라서 (격식)", "Prices rose; thus, sales fell."),
   Wd("moreover", "/mɔːrˈəʊvə(r)/", "게다가 (격식)", "Moreover, public transport reduces pollution."),
   Wd("hence", "/hens/", "그래서 (격식, 짧게)", "The city is crowded, hence the high rents."),
   Wd("overall", "/ˌəʊvərˈɔːl/", "전반적으로", "Overall, I think the policy has been successful.")])

# ───────── 2주차 ─────────
X("2026-11-30",
  [P("scroll through social media", "소셜 미디어를 계속 넘겨보다", "I often scroll through social media before I go to sleep."),
   P("go viral", "(영상·글이) 퍼지다, 화제가 되다", "Her video went viral overnight."),
   P("screen time", "화면 보는 시간", "Parents should limit their children's screen time."),
   P("log on / log off", "접속하다 / 접속을 끊다", "I log off from work apps at the weekend."),
   P("stay up late", "늦게까지 깨어 있다", "Teenagers often stay up late playing games.")],
  [Wd("device", "/dɪˈvaɪs/", "기기", "Most people have more than one device."),
   Wd("notification", "/ˌnəʊtɪfɪˈkeɪʃn/", "알림", "I turn off notifications when I need to focus."),
   Wd("cyberbullying", "/ˈsaɪbəbʊliɪŋ/", "사이버 괴롭힘", "Cyberbullying is a serious problem in schools."),
   Wd("isolation", "/ˌaɪsəˈleɪʃn/", "고립", "Too much time online can lead to social isolation."),
   Wd("convenient", "/kənˈviːniənt/", "편리한", "Online shopping is very convenient.")])

X("2026-12-01",
  [P("lose their jobs", "일자리를 잃다", "Many factory workers may lose their jobs to robots."),
   P("keep up with technology", "기술 변화를 따라가다", "Older people sometimes find it hard to keep up with technology."),
   P("in the long run", "장기적으로", "In the long run, AI will create new types of jobs."),
   P("a double-edged sword", "양날의 검", "Technology is a double-edged sword."),
   P("rely on ~", "~에 의존하다", "Many companies rely on AI to answer customer questions.")],
  [Wd("automation", "/ˌɔːtəˈmeɪʃn/", "자동화", "Automation has changed the way factories work."),
   Wd("innovation", "/ˌɪnəˈveɪʃn/", "혁신", "Innovation is the key to economic growth."),
   Wd("obsolete", "/ˈɒbsəliːt/", "더 이상 쓰이지 않는, 구식이 된", "Some jobs may become obsolete in the next twenty years."),
   Wd("surveillance", "/sɜːˈveɪləns/", "감시", "Some people worry about government surveillance."),
   Wd("retrain", "/ˌriːˈtreɪn/", "재교육하다, 재교육을 받다", "Workers need to retrain when their jobs change.")])

X("2026-12-02",
  [P("global warming", "지구 온난화", "Global warming is causing more extreme weather."),
   P("rising sea levels", "해수면 상승", "Rising sea levels threaten coastal cities."),
   P("extreme weather", "극단적인 날씨, 이상 기후", "Extreme weather such as floods is becoming more common."),
   P("harmful to the environment", "환경에 해로운", "Plastic bags are harmful to the environment."),
   P("cut down trees", "나무를 베다", "Large areas of forest are cut down every year.")],
  [Wd("deforestation", "/ˌdiːˌfɒrɪˈsteɪʃn/", "삼림 벌채", "Deforestation destroys the homes of many animals."),
   Wd("pollutant", "/pəˈluːtənt/", "오염 물질", "Cars release pollutants into the air."),
   Wd("drought", "/draʊt/", "가뭄", "The drought destroyed the crops."),
   Wd("endangered", "/ɪnˈdeɪndʒəd/", "멸종 위기의", "Pandas are an endangered species."),
   Wd("toxic", "/ˈtɒksɪk/", "유독한", "Factories should not release toxic waste into rivers.")])

X("2026-12-03",
  [P("go green", "친환경적으로 살다", "Many companies are trying to go green."),
   P("raise awareness of ~", "~에 대한 인식을 높이다", "Schools should raise awareness of environmental issues."),
   P("single-use plastics", "일회용 플라스틱", "Some countries have banned single-use plastics."),
   P("carbon footprint", "탄소 발자국", "Flying increases your carbon footprint."),
   P("make a difference", "변화를 만들다, 효과가 있다", "Even small changes can make a difference.")],
  [Wd("recycle", "/ˌriːˈsaɪkl/", "재활용하다", "We recycle paper, glass and plastic at home."),
   Wd("sustainable", "/səˈsteɪnəbl/", "지속 가능한", "We need more sustainable ways of producing food."),
   Wd("conservation", "/ˌkɒnsəˈveɪʃn/", "보존, 보호", "Wildlife conservation needs government funding."),
   Wd("incentive", "/ɪnˈsentɪv/", "장려책, 인센티브", "Tax incentives can encourage people to buy electric cars."),
   Wd("biodegradable", "/ˌbaɪəʊdɪˈɡreɪdəbl/", "생분해성의", "Biodegradable bags break down naturally.")])

X("2026-12-04",
  [P("a growing number of ~", "점점 더 많은 ~", "A growing number of people are working from home."),
   P("these days / nowadays", "요즘 (today 대신)", "These days, most people own a smartphone."),
   P("has a negative effect on ~", "~에 부정적 영향을 미치다 (bad for 대신)", "Stress has a negative effect on health."),
   P("play an important role in ~", "~에서 중요한 역할을 하다", "Parents play an important role in a child's education."),
   P("in my view,", "내 생각에는 (In my opinion 대신)", "In my view, governments should do more.")],
  [Wd("significant", "/sɪɡˈnɪfɪkənt/", "상당한, 중요한 (big 대신)", "There has been a significant increase in car use."),
   Wd("individual", "/ˌɪndɪˈvɪdʒuəl/", "개인 (person 대신)", "Every individual can help protect the environment."),
   Wd("beneficial", "/ˌbenɪˈfɪʃl/", "이로운 (good 대신)", "Regular exercise is beneficial for mental health."),
   Wd("decline", "/dɪˈklaɪn/", "감소하다 (decrease 대신)", "The number of smokers has declined."),
   Wd("numerous", "/ˈnjuːmərəs/", "수많은 (many 대신)", "There are numerous benefits to learning a language.")])

X("2026-12-05",
  [P("affect vs effect", "affect(동사) / effect(명사)", "Stress can affect your health. It has a bad effect on your sleep."),
   P("fewer vs less", "fewer + 복수 명사 / less + 불가산", "There are fewer cars and less pollution."),
   P("the number of vs a number of", "~의 수(단수 동사) / 몇몇의(복수 동사)", "The number of students is rising. A number of students are absent."),
   P("most people (✗ most of people)", "대부분의 사람들", "Most people use social media every day."),
   P("each / every + 단수 명사", "각각의, 모든", "Every student has a laptop.")],
  [Wd("accommodation", "/əˌkɒməˈdeɪʃn/", "숙소 (영국식 불가산)", "It is hard to find cheap accommodation in London."),
   Wd("furniture", "/ˈfɜːnɪtʃə(r)/", "가구 (불가산)", "We bought some new furniture for the living room."),
   Wd("research", "/rɪˈsɜːtʃ/", "연구 (불가산)", "More research is needed on this topic."),
   Wd("knowledge", "/ˈnɒlɪdʒ/", "지식 (불가산)", "Travelling increases your knowledge of other cultures."),
   Wd("traffic", "/ˈtræfɪk/", "교통량 (불가산)", "There is a lot of traffic in the city centre.")])

# ───────── 3주차 ─────────
X("2026-12-07",
  [P("break the law", "법을 어기다", "People who break the law should be punished."),
   P("serve a sentence", "형을 살다", "He is serving a five-year sentence for robbery."),
   P("a minor crime / a serious crime", "경범죄 / 중범죄", "Shoplifting is a minor crime, while murder is a serious crime."),
   P("be released from prison", "출소하다", "Many people struggle to find work after they are released from prison."),
   P("a criminal record", "전과 기록", "It is hard to get a job if you have a criminal record.")],
  [Wd("offence", "/əˈfens/", "범죄, 위법 행위 (영국 철자)", "Drink-driving is a serious offence."),
   Wd("victim", "/ˈvɪktɪm/", "피해자", "Victims of crime need support."),
   Wd("punishment", "/ˈpʌnɪʃmənt/", "처벌", "The punishment should fit the crime."),
   Wd("theft", "/θeft/", "절도", "Car theft has fallen in recent years."),
   Wd("justice", "/ˈdʒʌstɪs/", "정의, 사법", "The justice system should be fair to everyone.")])

X("2026-12-08",
  [P("give someone a second chance", "~에게 다시 기회를 주다", "Young offenders deserve a second chance."),
   P("get into trouble", "말썽을 일으키다, 곤란해지다", "Teenagers with nothing to do may get into trouble."),
   P("job training", "직업 훈련", "Job training helps prisoners find work after release."),
   P("the root causes of crime", "범죄의 근본 원인", "We need to tackle the root causes of crime, such as poverty."),
   P("peer pressure", "또래 압력", "Peer pressure can lead teenagers to commit crimes.")],
  [Wd("poverty", "/ˈpɒvəti/", "가난", "Poverty is one of the main causes of crime."),
   Wd("deterrent", "/dɪˈterənt/", "억지책, 범죄를 막는 것", "Heavy fines act as a deterrent."),
   Wd("fine", "/faɪn/", "벌금; 벌금을 물리다", "He was fined for driving too fast."),
   Wd("juvenile", "/ˈdʒuːvənaɪl/", "청소년의 (격식)", "Juvenile crime has increased in some areas."),
   Wd("reform", "/rɪˈfɔːm/", "개혁; 개선하다", "Prison reform is needed to reduce reoffending.")])

X("2026-12-09",
  [P("allocate funds to ~", "~에 예산을 배정하다", "The government should allocate more funds to education."),
   P("the public sector / the private sector", "공공 부문 / 민간 부문", "Many graduates want to work in the public sector."),
   P("a waste of money", "돈 낭비", "Some people think space exploration is a waste of money."),
   P("the taxpayer", "납세자 (세금을 내는 국민)", "The new stadium was paid for by the taxpayer."),
   P("a top priority", "최우선 순위", "Healthcare should be a top priority for the government.")],
  [Wd("budget", "/ˈbʌdʒɪt/", "예산", "The education budget has been cut again."),
   Wd("infrastructure", "/ˈɪnfrəstrʌktʃə(r)/", "사회 기반 시설", "Good infrastructure attracts foreign companies."),
   Wd("policy", "/ˈpɒləsi/", "정책", "The new policy aims to reduce unemployment."),
   Wd("citizen", "/ˈsɪtɪzn/", "시민", "Every citizen has the right to free education."),
   Wd("subsidise", "/ˈsʌbsɪdaɪz/", "보조금을 주다", "The government subsidises public transport.")])

X("2026-12-10",
  [P("stay in shape", "몸매·건강을 유지하다", "I go swimming twice a week to stay in shape."),
   P("a balanced diet", "균형 잡힌 식단", "A balanced diet includes fruit, vegetables and protein."),
   P("a sedentary lifestyle", "앉아서 지내는 생활 방식", "Office workers often have a sedentary lifestyle."),
   P("put on weight", "살이 찌다", "I put on weight when I stopped exercising."),
   P("prevention is better than cure", "예방이 치료보다 낫다", "Governments should remember that prevention is better than cure.")],
  [Wd("obesity", "/əʊˈbiːsəti/", "비만", "Childhood obesity is rising in many countries."),
   Wd("nutrition", "/njuˈtrɪʃn/", "영양", "Schools should teach children about nutrition."),
   Wd("life expectancy", "/laɪf ɪkˈspektənsi/", "기대 수명", "Life expectancy in Korea is over 80 years."),
   Wd("well-being", "/ˌwelˈbiːɪŋ/", "건강, 행복, 복지", "Exercise is good for both physical and mental well-being."),
   Wd("chronic", "/ˈkrɒnɪk/", "만성의", "Smoking can cause chronic diseases.")])

X("2026-12-11",
  [P("brand loyalty", "브랜드 충성도", "Companies try to build brand loyalty from a young age."),
   P("impulse buying", "충동구매", "Online ads encourage impulse buying."),
   P("on sale", "할인 중인", "I only buy clothes when they are on sale."),
   P("a must-have item", "꼭 가져야 할 물건", "Ads make every new phone look like a must-have item."),
   P("value for money", "가격 대비 가치, 가성비", "This laptop is good value for money.")],
  [Wd("commercial", "/kəˈmɜːʃl/", "(TV·라디오) 광고 방송", "I usually skip the commercials on YouTube."),
   Wd("materialistic", "/məˌtɪəriəˈlɪstɪk/", "물질만능주의의", "Advertising makes society more materialistic."),
   Wd("influence", "/ˈɪnfluəns/", "영향을 미치다", "Celebrities influence what young people buy."),
   Wd("sponsor", "/ˈspɒnsə(r)/", "후원하다; 후원자", "Many sports events are sponsored by big companies."),
   Wd("endorse", "/ɪnˈdɔːs/", "(유명인이 상품을) 광고·보증하다", "Famous athletes often endorse sports brands.")])

X("2026-12-12",
  [P("breaking news", "속보", "I saw the breaking news on my phone."),
   P("a news outlet", "언론사", "Many news outlets now publish stories online first."),
   P("follow the news", "뉴스를 챙겨 보다", "I don't follow the news very closely."),
   P("freedom of the press", "언론의 자유", "Freedom of the press is important in a democracy."),
   P("spread rumours", "소문을 퍼뜨리다", "Social media makes it easy to spread rumours.")],
  [Wd("journalist", "/ˈdʒɜːnəlɪst/", "기자", "Journalists should check their facts carefully."),
   Wd("biased", "/ˈbaɪəst/", "편향된", "Some newspapers are politically biased."),
   Wd("publish", "/ˈpʌblɪʃ/", "출판하다, 게재하다", "The article was published last week."),
   Wd("subscription", "/səbˈskrɪpʃn/", "구독", "I pay for a monthly news subscription."),
   Wd("broadcast", "/ˈbrɔːdkɑːst/", "방송하다", "The match was broadcast live on TV.")])

# ───────── 4주차 (Speaking) ─────────
X("2026-12-14",
  [P("I've lived there for ~ years", "거기서 ~년째 살고 있어요", "I've lived in Seoul for about ten years."),
   P("It's changed a lot", "많이 변했어요", "My hometown has changed a lot since I was a child."),
   P("within walking distance", "걸어갈 수 있는 거리에", "There's a supermarket within walking distance."),
   P("get a bit noisy", "좀 시끄러워지다", "It can get a bit noisy at night."),
   P("I'd like to move to ~", "~로 이사 가고 싶어요", "One day, I'd like to move to the countryside.")],
  [Wd("neighbourhood", "/ˈneɪbəhʊd/", "동네", "My neighbourhood is quiet and safe."),
   Wd("spacious", "/ˈspeɪʃəs/", "넓은", "Our living room is quite spacious."),
   Wd("cosy", "/ˈkəʊzi/", "아늑한", "My apartment is small but cosy."),
   Wd("suburb", "/ˈsʌbɜːb/", "교외", "I live in a suburb about 30 minutes from the city centre."),
   Wd("lively", "/ˈlaɪvli/", "활기찬", "The area is very lively at the weekend.")])

X("2026-12-15",
  [P("unwind after work", "퇴근 후 쉬다", "I usually watch a drama to unwind after work."),
   P("binge-watch", "(드라마를) 몰아서 보다", "I binge-watched a whole series last weekend."),
   P("take up a hobby", "취미를 시작하다", "I took up running last year."),
   P("I'm not really a fan of ~", "~을 별로 안 좋아해요", "I'm not really a fan of horror films."),
   P("from time to time", "가끔", "I go to the cinema from time to time.")],
  [Wd("plot", "/plɒt/", "줄거리", "The plot was a bit confusing."),
   Wd("gripping", "/ˈɡrɪpɪŋ/", "손에 땀을 쥐게 하는", "It was a gripping thriller."),
   Wd("cast", "/kɑːst/", "출연진", "The film has an amazing cast."),
   Wd("pastime", "/ˈpɑːstaɪm/", "취미, 여가 활동", "Reading is my favourite pastime."),
   Wd("subtitles", "/ˈsʌbtaɪtlz/", "자막", "I watch English films with subtitles.")])

X("2026-12-16",
  [P("I'm a big fan of ~", "~을 아주 좋아해요", "I'm a big fan of spicy food."),
   P("grab a bite to eat", "간단히 뭘 먹다", "Let's grab a bite to eat before the film."),
   P("I can't stand ~", "~을 정말 못 참겠어요, 싫어해요", "I can't stand very sweet food."),
   P("follow the latest trends", "최신 유행을 따르다", "I don't really follow the latest fashion trends."),
   P("a special occasion", "특별한 날", "I only wear a suit on special occasions.")],
  [Wd("cuisine", "/kwɪˈziːn/", "(나라·지역의) 요리", "I love Italian cuisine."),
   Wd("takeaway", "/ˈteɪkəweɪ/", "포장 음식 (영국식)", "We often get a takeaway on Friday nights."),
   Wd("outfit", "/ˈaʊtfɪt/", "옷차림 한 벌", "I bought a new outfit for the wedding."),
   Wd("fashionable", "/ˈfæʃnəbl/", "유행하는", "My sister always wears fashionable clothes."),
   Wd("ingredient", "/ɪnˈɡriːdiənt/", "재료", "Fresh ingredients make a big difference.")])

X("2026-12-17",
  [P("a role model", "롤모델", "My father has always been my role model."),
   P("go out of their way to ~", "일부러 애써서 ~하다", "She always goes out of her way to help others."),
   P("keep calm under pressure", "압박 속에서 침착하다", "He keeps calm under pressure."),
   P("learn a lot from ~", "~에게서 많이 배우다", "I learned a lot from my first teacher."),
   P("someone I can rely on", "믿고 의지할 수 있는 사람", "My best friend is someone I can rely on.")],
  [Wd("generous", "/ˈdʒenərəs/", "너그러운, 인심 좋은", "My uncle is very generous with his time."),
   Wd("determined", "/dɪˈtɜːmɪnd/", "의지가 강한", "She was determined to pass the exam."),
   Wd("inspiring", "/ɪnˈspaɪərɪŋ/", "영감을 주는", "Her story is really inspiring."),
   Wd("supportive", "/səˈpɔːtɪv/", "힘이 되어 주는", "My parents have always been very supportive."),
   Wd("admire", "/ədˈmaɪə(r)/", "존경하다", "I admire people who work hard.")])

X("2026-12-18",
  [P("off the beaten track", "사람들이 잘 모르는 (한적한 곳)", "The café is a bit off the beaten track."),
   P("a breath of fresh air", "기분 전환이 되는 것", "Going to the mountains is a breath of fresh air."),
   P("take in the view", "경치를 감상하다", "I sat on a bench and took in the view."),
   P("it's well worth a visit", "가 볼 만한 가치가 충분해요", "If you're in Busan, the market is well worth a visit."),
   P("a hidden gem", "숨은 명소", "This little bookshop is a hidden gem.")],
  [Wd("scenery", "/ˈsiːnəri/", "경치 (불가산)", "The scenery in Jeju is beautiful."),
   Wd("atmosphere", "/ˈætməsfɪə(r)/", "분위기", "The café has a relaxing atmosphere."),
   Wd("landmark", "/ˈlændmɑːk/", "랜드마크, 명소", "N Seoul Tower is a famous landmark."),
   Wd("breathtaking", "/ˈbreθteɪkɪŋ/", "숨이 멎을 듯한", "The view from the top is breathtaking."),
   Wd("tranquil", "/ˈtræŋkwɪl/", "고요한 (peaceful 대신)", "The temple is very tranquil in the early morning.")])

X("2026-12-19",
  [P("to be fair,", "공정하게 말하면", "To be fair, it wasn't completely his fault."),
   P("it turned out that ~", "알고 보니 ~였다", "It turned out that he was lost."),
   P("at first, ... but then ...", "처음엔 ~했지만 그다음엔", "At first I was nervous, but then I started to enjoy it."),
   P("I'll never forget ~", "~을 절대 잊지 못할 거예요", "I'll never forget the look on his face."),
   P("it was a turning point", "그것이 전환점이었어요", "Moving abroad was a turning point in my life.")],
  [Wd("grateful", "/ˈɡreɪtfl/", "고마워하는", "I was grateful for his help."),
   Wd("embarrassed", "/ɪmˈbærəst/", "창피한", "I felt really embarrassed when I fell over."),
   Wd("relieved", "/rɪˈliːvd/", "안도한", "I was relieved when I found my wallet."),
   Wd("unexpected", "/ˌʌnɪkˈspektɪd/", "예상치 못한", "It was a completely unexpected gift."),
   Wd("rewarding", "/rɪˈwɔːdɪŋ/", "보람 있는", "Volunteering is a very rewarding experience.")])

# ───────── 5주차 ─────────
X("2026-12-21",
  [P("I was very disappointed with ~", "~에 매우 실망했습니다", "I was very disappointed with the service at your restaurant."),
   P("as soon as possible", "가능한 한 빨리", "Please let me know as soon as possible."),
   P("I have attached ~", "~을 첨부했습니다", "I have attached a copy of my receipt."),
   P("Please do not hesitate to contact me", "언제든 연락 주세요", "Please do not hesitate to contact me if you need more information."),
   P("I would appreciate it if you could ~", "~해 주시면 감사하겠습니다", "I would appreciate it if you could reply by Friday.")],
  [Wd("refund", "/ˈriːfʌnd/", "환불", "I would like a full refund."),
   Wd("inconvenience", "/ˌɪnkənˈviːniəns/", "불편", "The delay caused me a lot of inconvenience."),
   Wd("faulty", "/ˈfɔːlti/", "결함이 있는", "The kettle I bought was faulty."),
   Wd("compensation", "/ˌkɒmpenˈseɪʃn/", "보상", "I believe I am entitled to some compensation."),
   Wd("unacceptable", "/ˌʌnəkˈseptəbl/", "용납할 수 없는", "Waiting two hours for a table is unacceptable.")])

X("2026-12-22",
  [P("on the whole,", "대체로", "On the whole, I think people are happier now."),
   P("it's hard to say, but ~", "단정하긴 어렵지만", "It's hard to say, but I think prices will keep rising."),
   P("there are pros and cons", "장단점이 있어요", "There are pros and cons to living in a big city."),
   P("as far as I know,", "내가 아는 한", "As far as I know, most schools teach English from age eight."),
   P("from my point of view,", "내 관점에서는", "From my point of view, families are less close than before.")],
  [Wd("generation", "/ˌdʒenəˈreɪʃn/", "세대", "The older generation prefers phone calls."),
   Wd("tendency", "/ˈtendənsi/", "경향", "There is a tendency for young people to marry later."),
   Wd("inevitable", "/ɪnˈevɪtəbl/", "피할 수 없는", "Some change is inevitable."),
   Wd("trend", "/trend/", "추세, 유행", "Working from home is a growing trend."),
   Wd("perspective", "/pəˈspektɪv/", "관점", "Travel gives you a different perspective on life.")])

X("2026-12-23",
  [P("How are things with you?", "요즘 어떻게 지내?", "How are things with you? I hope work isn't too busy."),
   P("I can't wait to ~", "빨리 ~하고 싶어", "I can't wait to see you!"),
   P("Let me know if ~", "~하면 알려줘", "Let me know if you can come."),
   P("Guess what?", "있잖아, 그거 알아?", "Guess what? I've got a new job!"),
   P("It would be great if you could ~", "~해 주면 정말 좋겠어", "It would be great if you could help me move.")],
  [Wd("housewarming", "/ˈhaʊswɔːmɪŋ/", "집들이", "I'm having a housewarming party next week."),
   Wd("catch up", "/kætʃ ʌp/", "(근황을) 나누다, 밀린 얘기를 하다", "Let's meet for coffee and catch up."),
   Wd("invitation", "/ˌɪnvɪˈteɪʃn/", "초대", "Thanks for the invitation."),
   Wd("celebrate", "/ˈselɪbreɪt/", "축하하다", "We're going out to celebrate my birthday."),
   Wd("directions", "/dəˈrekʃnz/", "길 안내", "I've sent you directions to my new place.")])

X("2026-12-24",
  [P("rush hour", "출퇴근 시간대", "The subway is packed during rush hour."),
   P("get stuck in traffic", "차가 막혀 꼼짝 못 하다", "I got stuck in traffic for an hour."),
   P("move to the city", "도시로 이사하다", "Many young people move to the city for work."),
   P("a sense of community", "공동체 의식", "Small towns often have a strong sense of community."),
   P("the pace of life", "생활 속도", "The pace of life in Seoul is very fast.")],
  [Wd("overcrowded", "/ˌəʊvəˈkraʊdɪd/", "과밀한", "Big cities are becoming overcrowded."),
   Wd("pedestrian", "/pəˈdestriən/", "보행자", "The city centre should be for pedestrians only."),
   Wd("residential", "/ˌrezɪˈdenʃl/", "주거의", "I live in a quiet residential area."),
   Wd("rent", "/rent/", "집세; 세 들다", "Rent in the city centre is very expensive."),
   Wd("outskirts", "/ˈaʊtskɜːts/", "변두리, 외곽", "We live on the outskirts of the city.")])
