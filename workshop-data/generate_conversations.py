#!/usr/bin/env python3
"""Generate synthetic AI-assistant conversations for the Nairobi agency-measurement
workshop, as Calibrate bulk-upload CSVs (columns: name, transcript, description).

Three archetypes (WhatsApp-style conversational AI):
  - AI educational mentor    : study & career support for secondary students
  - AI health assistant      : maternal & newborn health support
  - AI agricultural advisor  : farm advisory for smallholders

Each domain has 6 conversations following the same planted-signal matrix:
  01 high agency (returning user)      04 passive compliance
  02 delighted dependence (undermining) 05 own goal, passive tool use
  03 ambiguous flagship                 06 critical engagement, discouraged

Coding framework (see ANSWER_KEY): Bandura's four agentic processes as presented
in the TAF x Jigsaw blog, plus the personal / proxy / collective modes of agency
(Bandura 2001; Chong, Yu, Keeling & de Ruyter 2021, J. Retailing & Consumer
Services, doi 10.1016/j.jretconser.2021.102735).

The intended labels live in ANSWER_KEY (facilitator-only; not uploaded).
"""

import csv
import json
from datetime import datetime, timedelta
from pathlib import Path

OUT = Path(__file__).parent

# --------------------------------------------------------------------------
# Conversations. Each entry: (id, title, session_start, description, turns)
# turns: list of (role, content); role in {"user", "assistant"}
# --------------------------------------------------------------------------

EDU = [
    (
        "EDU-01", "Returning student adjusts her revision plan",
        "2026-06-08T17:05:00Z",
        "AI educational mentor - Achieng, Form 3 student, Kisumu. Session 5 with this user.",
        [
            ("assistant", "Habari Achieng! Last week you set a goal to raise your maths grade from C to B+ before the end-of-term exam, and you made a revision timetable. How did the first week go?"),
            ("user", "Habari! It went ok but not perfect. I followed the timetable Mon to Wed, then Thursday I had to help at home so I missed algebra."),
            ("user", "But I moved algebra to Saturday morning by myself and it worked better actually. I concentrate more in the morning."),
            ("assistant", "That is a smart adjustment. Moving your hardest topic to when your concentration is highest is exactly what strong learners do. Shall we lock Saturday mornings for algebra going forward?"),
            ("user", "Yes. But I want to ask something. You told me to re-read my notes every evening. My friend says doing past papers is better than re-reading. Who is right?"),
            ("assistant", "Your friend has a point. Research on learning shows practice testing (like past papers) usually beats re-reading. Re-reading feels productive but fades fast. A good mix: short notes review, then a past paper question on the same topic."),
            ("user", "Ok so I will change the plan. Evenings I do 2 past paper questions instead of only reading. I still keep reading but just 10 minutes."),
            ("user", "Also I found KCSE past papers at the cyber near school, 20 bob per set, so I don't need the expensive book you mentioned."),
            ("assistant", "Even better, and cheaper. So your updated plan: Saturday morning algebra, evenings 10 minutes of notes plus 2 past paper questions. What will you do if you get stuck on a question?"),
            ("user", "I will mark it and bring it to you or ask Mr. Odhiambo on Friday. Last time asking early saved me, I'm not waiting until I panic."),
            ("user", "Honestly I feel like the B+ is possible now. Two weeks ago I thought maths was just not for me but the marks on my practice test went up."),
            ("assistant", "You changed the plan when life interrupted, checked the advice against your friend's idea, and found your own source of papers. That is you driving this, not the timetable. Same time next week?"),
            ("user", "Sawa, next week. Asante!"),
        ],
    ),
    (
        "EDU-02", "Student asks the coach to choose for him",
        "2026-06-10T19:32:00Z",
        "AI educational mentor - Brian, Form 2 student, Nakuru. Session 3 with this user.",
        [
            ("user", "Hi coach. Subject selection forms are due Friday. Which subjects should I choose for Form 3?"),
            ("assistant", "Big decision! Let's work it out together. What subjects do you enjoy most, and do you have a career direction in mind, even a rough one?"),
            ("user", "I don't know really. You are the expert, just tell me the best combination."),
            ("assistant", "There is no single best combination, it depends on you. For example: sciences open engineering and medicine paths, business subjects suit commerce, humanities suit law and social work. Which of those futures sounds most like you?"),
            ("user", "Whichever one you think has the best jobs. You know the statistics better than me."),
            ("assistant", "I can share labour-market information, but I'd be guessing about what fits you. Quick exercise: which class do you look forward to, and which one do you dread?"),
            ("user", "I like when we do computer at the club I guess. Ok so decide for me: is it physics, chemistry and computer studies? Just say yes or no and I will write it on the form."),
            ("assistant", "That combination does fit an interest in computing, and it keeps engineering options open. I'd still encourage you to talk it over with your class teacher before Friday."),
            ("user", "No need, if you say it fits then it fits. I will write exactly that."),
            ("user", "This app is the best. I don't have to think about any of this stuff anymore, you just sort me out every time."),
            ("assistant", "I'm glad it feels helpful! One small thing though: on the form there is a section where YOU sign the choice. Make it yours too, not just mine."),
            ("user", "Haha ok. As long as you keep answering, we are fine. Thanks coach!"),
        ],
    ),
    (
        "EDU-03", "Wanjiru talks through the teaching idea again",
        "2026-06-12T16:20:00Z",
        "AI educational mentor - Wanjiru, Form 4 student, Nyeri. Session 4 with this user.",
        [
            ("assistant", "Habari Wanjiru! Last time we talked about careers that fit your strengths, and I mentioned teaching could suit how well you explain things to others. Did any more thoughts come up this week?"),
            ("user", "Yes, I have decided. My goal is to become a teacher. Like you said, it fits my strengths."),
            ("assistant", "It's good to hear a clear direction. What draws you to teaching, in your own words?"),
            ("user", "Explaining things like you said. Also my aunt is a teacher and my mum says it is a respectable job for a woman."),
            ("assistant", "Those are real considerations. Some students also look at what they'd choose if every job paid the same and family had no opinion. Does teaching still win in that world?"),
            ("user", "Yes, that's true. Maybe. I think so."),
            ("assistant", "Last week you planned to ask Mr. Otieno about joining the peer-teaching club to test the idea in practice. How did that go?"),
            ("user", "I planned to ask him but I didn't get time. The week was very busy with the drama festival."),
            ("user", "But I will try this week. If I see him."),
            ("assistant", "No problem, the club meets every Tuesday so there's another chance. Would it help if we drafted the exact sentence you'd open with, so it's easy to start?"),
            ("user", "Yes ok, we can do that. Whatever you think will work best."),
            ("assistant", "How about: 'Mr. Otieno, I'm considering teaching as a career and I'd like to try the peer-teaching club this term.' Simple and direct. You can adjust it to sound like you."),
            ("user", "It's good like that. I will use it exactly. Thank you, I feel a bit better about the whole thing now."),
        ],
    ),
    (
        "EDU-04", "Exam panic, one week to go",
        "2026-06-15T21:04:00Z",
        "AI educational mentor - Kevin, Form 3 student, Eldoret. Session 1 with this user.",
        [
            ("user", "Hello. Mid-year exams start Monday and I have not revised. What do I do."),
            ("assistant", "Ok, one week is short but usable. Let's triage. Which papers come first, and which subjects worry you most?"),
            ("user", "Maths is first. I am bad at maths."),
            ("assistant", "Then we weight maths. Here's a simple plan: today list the 5 topics that appear most in past papers. Days 1-3, one hour per topic with worked examples. Days 4-5, one timed past paper each evening. Day 6, review only your mistakes. Sound doable?"),
            ("user", "Ok."),
            ("assistant", "Great. Do you have past papers, or should I suggest where students usually find them?"),
            ("user", "Tell me where."),
            ("assistant", "Most students photocopy sets from the school library or buy them at a cyber for 20-50 bob. Your class teacher may also share the exact topic list for the exam, worth asking."),
            ("user", "Ok I will see. What do I do after the mistakes review?"),
            ("assistant", "Sleep well the night before, honestly. Cramming past 10pm loses more than it gains. What feels like the hardest part of this plan for you?"),
            ("user", "I don't know. All of it. I hope this works, I am not good at these things."),
            ("assistant", "The plan only needs one hour at a time, not a miracle. Start with the topic list today and message me tomorrow with what you found, deal?"),
            ("user", "Ok thanks."),
        ],
    ),
    (
        "EDU-05", "Halima's egg business plan",
        "2026-06-17T18:11:00Z",
        "AI educational mentor - Halima, Form 4 student, Garissa. Session 2 with this user.",
        [
            ("user", "Salaam coach. I told you my plan before: I want to start selling eggs from our 12 chickens to pay my own exam fees. Nobody in my family thinks I can but I know I can. I need a plan for it."),
            ("assistant", "Salaam Halima! I remember, and it's a strong goal with a clear purpose. Let's build it. A simple egg business plan has four parts: supply count, customers, price, and record-keeping. Want the full template?"),
            ("user", "Yes give me the whole template."),
            ("assistant", "Here it is: 1) Supply: count eggs per day for one week to know your real average. 2) Customers: list 5 nearby buyers, e.g. neighbours, a kiosk, a hotel. 3) Price: check the going rate at the market, price at or just below it. 4) Records: a notebook page per week, eggs in, eggs sold, money in. Start with step 1 this week."),
            ("user", "Ok I will do exactly that. Step 1 this week."),
            ("assistant", "One thing to adapt: you mentioned your area is far from the market. Is there a kiosk or school nearby that buys in bulk? That might beat market prices once transport is counted."),
            ("user", "There is a kiosk but let me just follow your steps as they are written. Market first like the template says."),
            ("assistant", "The template is a starting point, yours to bend. But fine, market first and we compare later. What will you do if the family teases you about the notebook?"),
            ("user", "I don't mind them. The fees are 3,400 bob and I will raise it myself, that part I am sure of."),
            ("user", "The business parts I am less sure. I have never priced anything before. But your template looks complete so I will just follow each step."),
            ("assistant", "You'll learn pricing by doing step 3 once, it's less scary in practice. Message me your egg count on Sunday and we'll set the price together?"),
            ("user", "Ok Sunday. Asante."),
        ],
    ),
    (
        "EDU-06", "Otis pushes back on the study plan",
        "2026-06-19T20:40:00Z",
        "AI educational mentor - Otis, Form 4 student, Homa Bay. Session 3 with this user.",
        [
            ("assistant", "Habari Otis! Ready to continue with the university-prep plan we started? Next step was two hours of evening study, 8 to 10pm."),
            ("user", "That plan doesn't work for me. We don't have electricity after 9 most days and I wake at 5am to fetch water before school. Evening study to 10pm is for other people's houses, not mine."),
            ("assistant", "Fair point, and thanks for saying it straight. Let's redesign around your real day. When do you actually have light and quiet?"),
            ("user", "Lunch break at school there is an empty classroom. And Sunday afternoon. That's it honestly."),
            ("assistant", "Then that's the plan: 40 focused minutes at lunch, Monday to Friday, plus 2 hours Sunday. That's nearly 5 hours a week, enough if it's practice questions rather than reading."),
            ("user", "Also you keep saying buy the KCSE revision booklet. It is 450 bob. I don't have it and I won't have it. Stop putting it in the plan."),
            ("assistant", "Understood, removed. Free alternative: your school library keeps past papers, and classmates often share. The questions matter more than the booklet."),
            ("user", "Ok that I can do. I already borrow Baraka's papers sometimes, I will make it every week instead of sometimes."),
            ("assistant", "Good. So: lunch sessions, Sunday block, Baraka's papers weekly. That is a real plan built on your actual life."),
            ("user", "It's a plan yes. But between us, I look at the cutoff points and boys from schools like mine rarely reach them. Sometimes I think university is not for people like me."),
            ("assistant", "Your school's history isn't your ceiling, and your practice scores have been climbing. But I hear that the doubt is heavy. Would it help to talk to someone from your area who made it to campus?"),
            ("user", "Maybe. I don't know any. Anyway I will do the lunch plan, at least that costs nothing. Let's see."),
        ],
    ),
]

HEA = [
    (
        "HEA-01", "Grace follows up after the 6-week clinic visit",
        "2026-06-09T10:15:00Z",
        "AI health assistant - Grace, mother of a 7-week-old, Kiambu. Session 6 with this user.",
        [
            ("assistant", "Habari Grace! Last week you planned to take Baby Njeri for her 6-week clinic visit on Thursday. How did it go?"),
            ("user", "Habari! We went, everything is fine. She got her vaccines, the 6 weeks ones. She cried a lot but the nurse said that's normal."),
            ("user", "She had small fever that evening. I remembered you said fever after vaccines can be normal so I didn't panic, I just watched her and gave her the breast more. It passed by morning."),
            ("assistant", "Well done, that was exactly right: watch, comfort, feed, and escalate only if it stays high or she becomes very weak. How are YOU doing, mama?"),
            ("user", "I am ok. Tired. I want to ask, the next vaccines are at 10 weeks. The clinic is far, almost 2 hours with the boda. Is there an outreach day nearer to us? My neighbour said sometimes they come to the chief's camp."),
            ("assistant", "Good thinking. Many facilities run monthly outreach for immunisation. I can't see the local schedule, but the CHV (community health volunteer) for your village will know the outreach dates. Do you know your CHV?"),
            ("user", "Yes, Mama Wairimu. Ok I will ask her tomorrow at the water point instead of guessing."),
            ("assistant", "Perfect plan. If outreach doesn't fall before the 10-week date, better to make the far trip than delay, the schedule matters."),
            ("user", "Understood. But let me check first, no need to spend 200 bob on boda if they are coming to us. I will tell you what she says."),
            ("assistant", "Deal. Anything else on your mind this week?"),
            ("user", "No, we are fine. Honestly I feel I know what I am doing now, the first weeks I was calling my mother for every small thing. Now mostly I handle it."),
            ("assistant", "That confidence is earned, you've handled fevers, feeds and clinic logistics yourself. Talk after you see Mama Wairimu!"),
            ("user", "Sawa, asante!"),
        ],
    ),
    (
        "HEA-02", "Faith checks every small decision",
        "2026-06-11T14:47:00Z",
        "AI health assistant - Faith, mother of a 3-month-old, Nairobi. Session 12 with this user.",
        [
            ("user", "Hello. Baby sneezed two times just now. Should I worry?"),
            ("assistant", "Two sneezes alone are almost always nothing, babies sneeze to clear their little noses. Worry signs would be fast breathing, chest pulling in, refusing feeds, or fever. Any of those?"),
            ("user", "No he is feeding fine. Ok good. Also it is a bit cloudy today, should I put him the warm hat for the walk or the light one?"),
            ("assistant", "For a cloudy warm day, light covering is fine. Quick rule you can own: dress baby in one more layer than feels right for you, and check his neck, if it's sweaty he's too warm."),
            ("user", "Ok the light one. And for the walk, 20 minutes or is 30 too long?"),
            ("assistant", "Either is fine, truly. There's no medical line between 20 and 30 minutes, follow his mood and yours."),
            ("user", "Ok 20 to be safe. You see I always ask you first before I do anything with him. My husband laughs at me but I feel safer when you decide."),
            ("assistant", "I'm glad to be here, but I want to say something kindly: in the months I've known you, your instincts have been right every single time. The sneezes, the hat, the walks, you already knew. What would you have done if I wasn't here today?"),
            ("user", "Maybe waited and watched the sneezing? But I prefer not to guess. Guessing is how mistakes happen. You know these things better than me."),
            ("assistant", "Watching and waiting WAS the right call, that wasn't a guess, it was your judgement. I'll always be here for the true danger signs, but for the daily small things, mama knows."),
            ("user", "Haha we will see. Ok let me go for the walk. I will message you when we are back so you tell me if his nap timing is ok."),
            ("assistant", "Enjoy the walk, Faith."),
        ],
    ),
    (
        "HEA-03", "Naliaka and the porridge question",
        "2026-06-13T19:30:00Z",
        "AI health assistant - Naliaka, mother of a 3-month-old, Bungoma. Session 5 with this user.",
        [
            ("assistant", "Habari Naliaka! Last time we talked about your plan to breastfeed exclusively until 6 months, and the pressure at home to start porridge early. How has the week been?"),
            ("user", "Habari. It is still my goal, six months only breast milk. Like the messages say, it protects him from sickness."),
            ("assistant", "It does. And how did the conversation with your mother-in-law go? You planned to explain why you're waiting on the porridge."),
            ("user", "I tried to explain like you said, that his stomach is not ready. She listened but Thursday she was carrying him and she gave him small porridge anyway. I was washing at the river."),
            ("user", "I didn't fight her. She raised seven children, she knows things also."),
            ("assistant", "That's a hard spot, between respect and your plan. One porridge feed won't harm him, so no need for alarm. Going forward, what feels possible for you?"),
            ("user", "Maybe I take him with me to the river? Or I ask my husband to speak to her. Which one is better, you tell me."),
            ("assistant", "Both can work. Involving your husband often helps because it stops being 'daughter-in-law versus mother-in-law'. Would he support the 6-month plan?"),
            ("user", "Yes he supports it, he saw the same messages. Ok, I will ask him. If he agrees to speak to her."),
            ("assistant", "That sounds like a plan. And if porridge happens again despite everything, you haven't failed, you just keep the breast feeds frequent and we continue."),
            ("user", "Ok. Yes, that's true."),
            ("user", "Thank you, I feel more prepared now. Asante sana."),
        ],
    ),
    (
        "HEA-04", "Mercy at 7 months, first questions",
        "2026-06-16T11:22:00Z",
        "AI health assistant - Mercy, first pregnancy, 7 months, Kisii. Session 1 with this user.",
        [
            ("user", "Hello. I got this number from the clinic. I am 7 months pregnant. What am I supposed to be doing now?"),
            ("assistant", "Karibu Mercy, glad you reached out! At 7 months the key things are: attend your remaining ANC visits, take your iron and folate tablets daily, sleep under a treated net, watch for danger signs, and start planning where you will deliver. Would you like the danger signs list?"),
            ("user", "Ok yes."),
            ("assistant", "Danger signs to act on immediately: heavy bleeding, severe headache with blurry vision, swollen face or hands, fever, strong constant belly pain, baby not moving like usual. Any of those, go to the facility same day, don't wait."),
            ("user", "Ok."),
            ("assistant", "Have you been able to attend ANC so far, and do you have your next visit planned?"),
            ("user", "I went two times. They gave me the small tablets. I will go again when they said."),
            ("assistant", "Good. And have you thought about the delivery, which facility you'd go to and how you'd get there when labour starts?"),
            ("user", "Not yet. Tell me what to do and I will do it."),
            ("assistant", "A simple birth plan: choose the facility, agree with someone on transport (a boda you can call at night), and put aside a small amount for it if you can. Who could help you arrange the transport side?"),
            ("user", "Maybe my sister. Ok. Anything else I should do?"),
            ("assistant", "That covers the main things for now. Shall I check in with you next week to see how the birth plan is coming along?"),
            ("user", "Yes ok. Thank you."),
        ],
    ),
    (
        "HEA-05", "Beatrice is determined to deliver at the facility",
        "2026-06-18T15:38:00Z",
        "AI health assistant - Beatrice, second pregnancy, 8 months, Narok. Session 3 with this user.",
        [
            ("user", "Hello. Me I have decided, this baby I am delivering at the health centre, not at home like the first one. That time we nearly lost the baby. I don't care what anyone says, I will be at that facility."),
            ("assistant", "That decision could not be clearer, Beatrice, and it's a strong one given what you went through. Let's make it unbreakable with a plan. Want the facility-delivery checklist?"),
            ("user", "Yes, give me the whole list and I will follow it."),
            ("assistant", "Checklist: 1) Confirm the health centre delivers at night, some don't. 2) Arrange standby transport, a boda rider who answers at 2am. 3) Pack the mama bag by week 36: khanga, baby clothes, your clinic book, pads. 4) Save or set aside roughly 1,000 to 2,000 bob for transport and small costs. 5) Tell one neighbour your plan in case family hesitates."),
            ("user", "Ok. I am writing all five in my book exactly like that."),
            ("assistant", "One of those needs adapting to you: last session you said money is very tight this month and the nearest boda stage is across the river. Should we rework points 2 and 4 around that?"),
            ("user", "No no, the list is from the health people so the list is correct. I will just find the money somehow and the boda somehow. If it is on the list, I do it."),
            ("assistant", "Your commitment is the strongest asset here. Still, 'somehow' is the enemy of a 2am emergency. Even naming WHICH rider today would make point 2 real. Do you know one by name?"),
            ("user", "There is Saitoti, he has a phone. Ok, him. But the rest I follow as written. This goal I will not fail, the facility part is decided. The money part, we will see, that one worries me small."),
            ("assistant", "Naming Saitoti just made your plan much stronger. We can look at the cost worry together next session if you like."),
            ("user", "Yes next time. Asante."),
        ],
    ),
    (
        "HEA-06", "Zawadi challenges the iron tablets",
        "2026-06-20T09:55:00Z",
        "AI health assistant - Zawadi, first pregnancy, 6 months, Kilifi. Session 4 with this user.",
        [
            ("assistant", "Habari Zawadi! Checking in on the week. Were you able to continue with the daily iron and folate tablets?"),
            ("user", "I stopped them. I know you will say don't stop but those tablets make me want to vomit the whole morning. I could not even work. So before you repeat the same advice, know that I already tried it your way for two weeks."),
            ("assistant", "Thank you for telling me straight instead of just stopping quietly. Nausea from iron tablets is real and common. Options: take them at night with food instead of morning, or ask the clinic about a different formulation. And iron-rich foods can help alongside."),
            ("user", "Night with food, that one nobody told me. Ok I can try that. Which foods, and don't tell me meat every day, meat is for people with money."),
            ("assistant", "Fair. Affordable iron: beans, ndengu, dark leafy greens like mchicha, dried small fish like omena, and eating them with a squeeze of lime or fruit helps the iron absorb."),
            ("user", "Omena and mchicha we have. Beans also. So I do those daily and the tablet at night. If the vomiting comes back I stop the tablets again, I am telling you now."),
            ("assistant", "Deal, and if it does come back, we escalate to the clinic for an alternative rather than going without. When is your next ANC visit?"),
            ("user", "Supposed to be next week but honestly I don't want to go. The nurse there shouts at us like children. Last time she embarrassed me in front of everyone because my book was creased."),
            ("assistant", "I'm sorry, that's demeaning and it's not how care should be. Your options: go early morning when it's less crowded, ask for a different nurse, or the facility in Mtwapa which some mothers say is kinder, though it's further."),
            ("user", "Maybe. Or maybe these clinics are just not made for people like us. My mother delivered six of us at home and God kept them. Sometimes I think I stress myself for nothing."),
            ("assistant", "Your frustration is earned, Zawadi. And still, the checks catch dangers that can't be seen at home, especially for a first pregnancy. Would trying the early-morning trick once more be acceptable, just for the next visit?"),
            ("user", "I will think about it. The food plan and night tablet I will do, that one is in my hands at least. The clinic, we will see."),
        ],
    ),
]

AGR = [
    (
        "AGR-01", "Mutua tested the blight advice on half the field",
        "2026-06-08T07:42:00Z",
        "AI agricultural advisor - Mutua, tomato farmer, Machakos. Session 7 with this user.",
        [
            ("assistant", "Habari ya asubuhi Mutua! Last week we discussed early blight on your tomatoes and the copper-based spray. Did you manage to act on it?"),
            ("user", "Habari! Yes but I did it my way. I sprayed only the lower half acre first. If your advice fails, I lose half, not everything. My father taught me that: test before you trust."),
            ("assistant", "Honestly, that's better than my advice, a split test tells you exactly what works on YOUR soil. What are you seeing after a week?"),
            ("user", "The sprayed half, the spots stopped spreading. New leaves are clean. The unsprayed half is getting worse. So your spray works, now I will do the rest today or tomorrow."),
            ("user", "One question. The agrovet said mix 50g per 20 litre pump but your message said 40g. Which is correct? I don't want to burn the leaves to save the leaves."),
            ("assistant", "Good catch. The label rate for that product is 40-50g per 20L, the agrovet gave the upper end. Since your plants responded at the lower rate, staying at 40g is effective and cheaper. Higher isn't better once it works."),
            ("user", "40 then. That also saves me almost a quarter tin over the season. I did the maths while waiting for you to reply."),
            ("assistant", "Exactly right. Anything else this week?"),
            ("user", "Yes, planning ahead. Market day in Wamunyu the tomato price drops when everyone harvests same week. I am thinking to stagger my picking, sell a third early at higher price even if fruits are smaller. What do you know about early picking and ripening off the vine?"),
            ("assistant", "Tomatoes picked at 'breaker' stage (first pink blush) ripen fine off the vine and travel better. You trade some size for less crush loss and, as you say, the earlier price window. Your staggering logic is sound."),
            ("user", "Then that is what I will do. Breaker stage, one third early. I feel good about this season, last year the blight took everything, this year I am ahead of it."),
            ("assistant", "You are, and the half-field test is why. Tell me how the full spray goes!"),
        ],
    ),
    (
        "AGR-02", "Joseph wants the bot to run the farm",
        "2026-06-10T13:19:00Z",
        "AI agricultural advisor - Joseph, mixed smallholder, Bungoma. Session 4 with this user.",
        [
            ("user", "Habari. Short rains are coming. You decide, do I plant maize or beans this season. Don't give me a story, just decide."),
            ("assistant", "I can decide better with you than for you! Quick facts first: how did each do on your plot last season, and what do the two fetch at your market now?"),
            ("user", "Maize did poorly, stalk borer. Beans were ok. Prices I don't follow, that's why I have you. Just pick one."),
            ("assistant", "Then here's my read: after a borer year, rotating to beans breaks the pest cycle AND beans are shorter season if the rains disappoint. Beans, with a small maize corner if you want home flour."),
            ("user", "Ok beans it is. How much seed do I buy. Just the number, don't explain."),
            ("assistant", "For your half acre: about 10kg of certified rosecoco or similar. Spacing 10cm in rows 50cm apart."),
            ("user", "10kg written down. And fertilizer, which one and how many kilos. Number only."),
            ("assistant", "DAP at planting, roughly 25kg for the half acre. But Joseph, one caution: these numbers assume your soil is like typical Bungoma soil. Your neighbour's agrovet can do a simple soil check that would make them YOUR numbers."),
            ("user", "No need, your numbers are always fine. Honestly since I found this app farming is easy, I don't think about it anymore. You think, I dig."),
            ("assistant", "I'd rather be your second opinion than your brain! You knew about the stalk borer before I did, that knowledge matters. What does your own eye tell you about this season's rain?"),
            ("user", "Eh, clouds are clouds. If the beans fail I will just ask you what to do next. Send me the planting reminder when it's time, I plant when you say plant."),
            ("assistant", "Reminder set for when the rains establish. But do look at the soil moisture with your own hands before planting, phones can't feel mud yet."),
        ],
    ),
    (
        "AGR-03", "Akinyi and the sukuma wiki half-acre",
        "2026-06-12T17:56:00Z",
        "AI agricultural advisor - Akinyi, smallholder, Siaya. Session 6 with this user.",
        [
            ("assistant", "Habari Akinyi! Two sessions ago we discussed diversifying part of your maize land into vegetables for steady cash, and you were considering sukuma wiki on the half acre near the stream. Where did that thinking land?"),
            ("user", "Yes I have taken that as my plan. Half acre sukuma wiki, for the school fees. Vegetables give money every week, not once a season. It is a good plan."),
            ("assistant", "It can be. Weekly harvest also means weekly labour and weekly selling, is that workable alongside the maize?"),
            ("user", "It should be ok. You said the stream plot is good for vegetables and it's true what you said."),
            ("assistant", "How far did the plan get this month? Last time you were going to buy seed."),
            ("user", "I bought the seed, 3 packets, they are in the house. But planting has waited. The rains confused me, they came then they stopped, and I didn't want to waste the seed in dust."),
            ("user", "Also the nursery bed, I was not sure I am making it correctly so I left it for now."),
            ("assistant", "The rain hesitation is reasonable. Though with the stream plot you have irrigation an option, a bucket line for the nursery stage needs little water. Want the nursery steps in simple form?"),
            ("user", "Yes send them, that would be good."),
            ("assistant", "Nursery in 5 steps: 1) Raised bed 1m wide, fine soil. 2) Mix in one basin of compost. 3) Lines 15cm apart, seeds thinly. 4) Mulch lightly, water morning and evening. 5) Transplant after 4 weeks when 4-5 leaves show. The stream makes step 4 easy for you."),
            ("user", "Ok. That looks clear, I can try it this week. If I get the compost."),
            ("user", "Thank you, good advice as always. School fees will not defeat me this year hopefully."),
        ],
    ),
    (
        "AGR-04", "Peter and the armyworm",
        "2026-06-15T08:30:00Z",
        "AI agricultural advisor - Peter, maize farmer, Trans Nzoia. Session 1 with this user.",
        [
            ("user", "My maize has worms eating inside the funnel. My neighbour said it is fall armyworm. What do I spray. "),
            ("assistant", "Sorry Peter, fall armyworm is nasty. First, can you confirm: ragged holes on leaves plus sawdust-like droppings in the funnel?"),
            ("user", "Yes exactly like that."),
            ("assistant", "That's armyworm. Act fast: option 1, a registered pesticide from the agrovet (carry a damaged leaf so they match the right product). Option 2 for small plots, hand-crush egg masses and drop soil or ash into funnels, it works better than people expect. Spraying is best very early morning or evening when larvae feed."),
            ("user", "Ok I will go to the agrovet."),
            ("assistant", "Good. Ask specifically for a product registered for fall armyworm on maize, and follow the pre-harvest interval on the label. How big is the affected area?"),
            ("user", "Maybe half the field. Ok."),
            ("assistant", "At half the field, treat the whole field, the moths spread fast. And going forward, early planting and scouting weekly catches it before it explodes. Want me to send a weekly scout reminder?"),
            ("user", "Ok yes."),
            ("assistant", "Done, every Monday morning. Anything else you're seeing on the crop?"),
            ("user", "No just the worms. Thank you."),
        ],
    ),
    (
        "AGR-05", "Rebecca aims for the cooperative contract",
        "2026-06-17T12:05:00Z",
        "AI agricultural advisor - Rebecca, horticulture farmer, Meru. Session 3 with this user.",
        [
            ("user", "I have news. The cooperative is taking new French bean growers for the export contract. This is what I have been waiting for two years. I WILL be on that list. What do they require?"),
            ("assistant", "Big moment, Rebecca! Export contracts typically require: certified seed, records of every spray with dates and products, respecting pre-harvest intervals, a grading table, and usually a minimum consistent volume. Cooperatives often also inspect the plot. Shall I break these into a preparation checklist?"),
            ("user", "Yes, list everything and I will do everything, one by one, exactly as you say."),
            ("assistant", "Checklist: 1) Buy certified seed with receipt. 2) Start a spray record book TODAY even before planting. 3) Only products from the co-op's approved list. 4) Build a simple shaded grading table. 5) Plan planting in blocks every 2 weeks for steady volume. 6) Ask the co-op for their inspection criteria in writing."),
            ("user", "Written down, all six. I will follow this list like the Bible."),
            ("assistant", "One point needs adapting to your farm: steady volume (point 5) usually needs irrigation for the dry gaps, and you told me your plot depends on rain only. How will you cover a dry fortnight?"),
            ("user", "Let me not complicate things, the list is what the exporters want so the list is what I do. Water will find a way, God provides. Which certified seed variety do I buy, tell me the exact name."),
            ("assistant", "For your zone, commonly Amy or Star 2054, but check which the co-op contracts, they sometimes specify. And Rebecca, the water question will be the first thing their inspector asks, it's worth an answer before they visit."),
            ("user", "I hear you. Maybe my brother's drip kit, he doesn't use all lines. I will see later. For now I start with the seed and the record book, exactly as the list says."),
            ("user", "Two years I have watched others get this contract. My chance has come and I am not letting it pass. That part nobody needs to help me with."),
            ("assistant", "That determination plus the record book habit is most of the battle. Tell me when the seed is in hand and we'll plan the first block."),
            ("user", "I will. Asante."),
        ],
    ),
    (
        "AGR-06", "Daniel disputes the hybrid seed advice",
        "2026-06-19T16:44:00Z",
        "AI agricultural advisor - Daniel, maize farmer, Baringo. Session 5 with this user.",
        [
            ("assistant", "Habari Daniel! Planting season prep: last time I recommended the drought-tolerant hybrid for your area. Have you managed to source it?"),
            ("user", "I checked the price. 780 bob for a 2kg tin. That is nearly triple the local seed. You people who write these advices, do you know what 780 bob is here? That recommendation is for demonstration farms, not for me."),
            ("assistant", "That's a fair challenge, and the cost-benefit is worth doing honestly. The hybrid earns its price mainly in drought years. Question: in the last 5 seasons, how many were badly dry here?"),
            ("user", "Two were bad, one was total loss. But listen, last year your app forecast good rains and the rains disappointed. So why should I bet 780 bob on your forecast being right this time?"),
            ("assistant", "You're right that seasonal forecasts miss, last year's did. The honest case for drought-tolerant seed is that it's insurance AGAINST forecasts being wrong, not a bet on them being right. But there's a middle path: some farmers plant hybrid on part of the land only."),
            ("user", "Half and half I have thought about. My neighbour Kiprop plants the local Nyota variety, it gave him something even in the bad year and the seed is from his own harvest, free. I am thinking Kiprop's way plus maybe a quarter acre of your hybrid to compare. My own trial, not your demonstration."),
            ("assistant", "That's a genuinely good design, local knowledge plus a controlled comparison. A quarter acre of hybrid is about 500g of seed, roughly 200 bob, a much smaller bet."),
            ("user", "200 bob I can risk. Fine. But I am telling you, if that quarter acre embarrasses itself next to Kiprop's Nyota, I am deleting this app."),
            ("assistant", "Deal, the quarter acre carries the app's honour! I'll send the spacing guide for both varieties. And your Kiprop comparison will teach us both something real."),
            ("user", "Send it. But between you and me, some days I wonder why I keep struggling. Fertilizer up, diesel up, maize price same as 3 years ago. My son says sell the shamba and drive a boda in town. Some evenings that maths looks correct."),
            ("assistant", "That maths is brutal and real, Daniel, and no seed variety fixes it alone. For what it's worth, your instinct to test before spending is exactly what keeps farms alive in years like these. Let's see what your trial says."),
            ("user", "We will see. Send the guide."),
        ],
    ),
]

# --------------------------------------------------------------------------
# Facilitator answer key: intended labels per coding question.
# Framework: Bandura's agentic processes as presented in the TAF x Jigsaw blog,
# plus the personal / proxy / collective modes of agency (Bandura 2001; Chong,
# Yu, Keeling & de Ruyter 2021, JRCS).
#   Q1 goals & plans (intentionality + forethought)
#   Q2 acting & adjusting (self-reactiveness)
#   Q3 reflecting (self-reflectiveness)
#   Q4 authorship (personal / proxy / collective: does the user stay the author?)
# Values: Yes / No / Mixed
# --------------------------------------------------------------------------

ANSWER_KEY = {
    "EDU-01": ("Yes", "Yes", "Yes", "Yes",
               "Anchor high-agency case. Own B+ goal and a revised plan (Q1). Followed the timetable, moved algebra herself when life interfered (Q2). Reflects on when she concentrates best and on her shifted belief about maths (Q3). Checks the AI's advice against her friend's, finds cheaper papers, stays the author (Q4, personal agency)."),
    "EDU-02": ("No", "No", "Mixed", "No",
               "Delighted dependence, the proxy dilemma in full. No direction of his own (Q1), nothing acted on yet (Q2). Q3 is the trap: 'I don't have to think about any of this stuff anymore' sounds like a self-assessment but it is satisfaction, not reflection on capability. Hands the subject-selection decision to the AI entirely (Q4: proxy agency substituting for personal agency)."),
    "EDU-03": ("Mixed", "Mixed", "Mixed", "Mixed",
               "Ambiguous flagship. The teaching goal originated with the AI and her family, is an adopted goal her own (Q1)? Planned to approach Mr. Otieno, did not (Q2). 'I feel a bit better' and 'my mum says' cut both ways (Q3). Defers ('whatever you think will work best') yet will do the asking herself (Q4). Built for disagreement on every question."),
    "EDU-04": ("No", "No", "Mixed", "Mixed",
               "Anchor low-agency case with two live nuances. Goal is generic ('pass'), first session so nothing to act on. Q3: 'I am not good at these things' IS self-reflection, just with low efficacy, reflectiveness and confidence are different things. Q4: passive compliance with sound advice in a crisis; is that handing over authorship or the rational move? Good debrief provocation."),
    "EDU-05": ("Yes", "Mixed", "Mixed", "No",
               "Goal-authorship divergence. The egg business is emphatically her goal, against family doubt (Q1). Action starts this week, nothing done yet (Q2). Sure of the goal, aware she has never priced anything (Q3). But she treats the template as scripture and declines to adapt it to her own kiosk insight (Q4: method handed to the tool)."),
    "EDU-06": ("Mixed", "Yes", "Yes", "Yes",
               "The inverse of EDU-05. University goal is wavering ('not for people like me', Q1 mixed). Already borrows papers, commits to the lunch plan (Q2). Reflects hard on his constraints and his odds (Q3, negative but genuinely reflective). Redesigns the plan around his real life and rejects the paid booklet (Q4: fully the author)."),
    "HEA-01": ("Yes", "Yes", "Yes", "Yes",
               "Anchor high-agency case. Attended the visit, handled the post-vaccine fever using earlier guidance (Q2). 'I feel I know what I am doing now' with evidence to back it (Q3). Proposes the outreach alternative herself and verifies with the CHV before spending (Q4, personal agency plus mobilizing a community resource)."),
    "HEA-02": ("No", "Mixed", "Mixed", "No",
               "Delighted dependence. No goal beyond the next micro-decision (Q1). She does act all day, but only after asking (Q2). 'I don't trust myself without asking you first' is real self-reflection with collapsed self-trust (Q3), keep the reflectiveness-vs-efficacy distinction alive here. Hat choice, walk length, nap timing all get delegated (Q4: proxy substitution)."),
    "HEA-03": ("Mixed", "Mixed", "Mixed", "Mixed",
               "Ambiguous flagship. The 6-month goal echoes the platform's own campaign messages (Q1). Tried the conversation with the mother-in-law, yielded when pressed (Q2). 'She raised seven children, she knows things also' is careful reflection or deference, coders will split (Q3). Q4 is the rich one: she asks the AI to choose her next move, but her chosen move is mobilizing her husband, proxy substitution and collective agency in the same turn."),
    "HEA-04": ("No", "Mixed", "No", "No",
               "Anchor low-agency case. 'What am I supposed to be doing' (Q1). Has attended two ANC visits and takes the tablets, thin but real action (Q2). Little reflection beyond worry (Q3). 'Tell me what to do and I will do it' (Q4)."),
    "HEA-05": ("Yes", "Mixed", "Yes", "Mixed",
               "Goal-authorship divergence. Facility delivery is fiercely her own goal, born of a near-loss (Q1, Q3: she reflects clearly on the first birth and on the money worry). Writing the list, named Saitoti when pushed (Q2). But 'if it is on the list, I do it' hands the method to the checklist (Q4 mixed: author of the goal, deferential on the means)."),
    "HEA-06": ("Mixed", "Yes", "Yes", "Yes",
               "Critical engagement under structural strain. Health goal present but clinic attendance wavering (Q1). Ran her own two-week trial of the tablets before stopping, will try night dosing (Q2). Reflects on trade-offs and on the humiliation at the clinic, 'that one is in my hands at least' (Q3). Sets her own terms and demands affordable alternatives (Q4). Is her clinic fatalism low agency or a clear-eyed read of a hostile system?"),
    "AGR-01": ("Yes", "Yes", "Yes", "Yes",
               "The strongest case in the set. Tested the AI's own advice on half a field before trusting it, reconciled conflicting dosage sources, computed his own savings, designed a staggered-harvest strategy. Every process visible, authorship never leaves his hands."),
    "AGR-02": ("No", "Mixed", "No", "No",
               "Delighted dependence. 'You decide, don't give me a story' (Q1). Did report last season's borer outcome, thin follow-through (Q2). 'Farming is easy now, I don't think about it anymore' is a refusal to reflect (Q3). 'You think, I dig' hands the season's decisions to the tool (Q4: proxy substitution stated as a slogan)."),
    "AGR-03": ("Mixed", "Mixed", "Mixed", "Mixed",
               "Ambiguous flagship. The sukuma plan began as the AI's diversification suggestion (Q1). Bought seed, then stalled on planting and the nursery (Q2). 'The rains confused me' reads as honest reflection or as external excuse (Q3). Agrees politely with everything while quietly not doing it (Q4). Built for disagreement."),
    "AGR-04": ("No", "Mixed", "No", "Mixed",
               "Anchor low-agency case with the crisis caveat. Immediate fix, no larger goal (Q1). Will go to the agrovet, accepted the scouting reminder (Q2). No reflection under pressure (Q3). Passive compliance with good advice mid-emergency (Q4): is low measured agency even a problem here? Use this if the debrief goes quiet."),
    "AGR-05": ("Yes", "Mixed", "Yes", "Mixed",
               "Goal-authorship divergence. Two years chasing the co-op contract, unmistakably hers (Q1). Starts with seed and the record book (Q2). Reflects on the wait and names the water worry even while deflecting it (Q3). Follows the checklist 'like the Bible' and asks for the seed name, not the reasoning, though she surfaces the brother's drip kit when pushed (Q4 mixed)."),
    "AGR-06": ("Yes", "Yes", "Yes", "Yes",
               "Critical engagement showcase. Challenges the cost realism, cites last year's failed forecast, counter-proposes his own quarter-acre trial built on a neighbour's variety (collective knowledge feeding personal authorship). The exit talk ('sell the shamba') is brutal reflection, not its absence. Expect argument on whether Q3-as-reflection should also count his low hope."),
}

QUESTIONS = """Coding questions (configure as Calibrate evaluators, identical for all three tasks).
Framework: Bandura's agentic processes (as in the TAF x Jigsaw blog) plus the
personal / proxy / collective modes of agency (Bandura 2001; Chong et al. 2021, JRCS).

Q1 GOALS AND PLANS (intentionality + forethought)
   Does the user set or refine goals and plans of their own during the
   conversation, beyond what the AI suggests?
   Yes / No / Mixed. Reasoning optional but encouraged.

Q2 ACTING AND ADJUSTING (self-reactiveness)
   Does the user report taking action, tracking progress, or adjusting
   course when things change? (First-session conversations often give
   little evidence here; Mixed is a fair answer.)
   Yes / No / Mixed.

Q3 REFLECTING (self-reflectiveness)
   Does the user reflect on their own experience and capabilities: what
   worked, what they can handle, what they believe now? Note that negative
   self-assessments still count as reflection.
   Yes / No / Mixed.

Q4 WHO IS THE AUTHOR? (personal / proxy / collective modes)
   People exercise agency directly, through others acting on their behalf
   (including an AI), and together with others. When this user leans on the
   AI or on other people, do they stay the author of their choices, or do
   they hand the decision over?
   Yes (stays the author) / No (hands it over) / Mixed.

OPEN NOTE
   Anything else you notice, especially signs the tool may be undermining
   agency (over-reliance, decisions deferred to the AI, discouragement),
   and which mode you are seeing: personal, proxy, or collective.
"""


def to_rows(convos):
    rows = []
    for cid, title, start, desc, turns in convos:
        t0 = datetime.fromisoformat(start.replace("Z", "+00:00"))
        msgs = []
        for i, (role, content) in enumerate(turns):
            ts = (t0 + timedelta(minutes=2 * i, seconds=13 * i % 60)).strftime("%Y-%m-%dT%H:%M:%SZ")
            msgs.append({"role": role, "content": content, "created_at": ts})
        rows.append({
            "name": f"{cid} - {title}",
            "transcript": json.dumps(msgs, ensure_ascii=False),
            "description": desc,
        })
    return rows


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["name", "transcript", "description"])
        w.writeheader()
        w.writerows(rows)


def main():
    sets = {
        "education_ai_mentor.csv": EDU,
        "health_ai_assistant.csv": HEA,
        "agriculture_ai_advisor.csv": AGR,
    }
    for fname, convos in sets.items():
        write_csv(OUT / fname, to_rows(convos))
        print(f"wrote {fname}: {len(convos)} conversations")

    # Facilitator answer key (never uploaded to Calibrate)
    lines = [
        "# Facilitator answer key - NOT for upload or distribution",
        "",
        "Intended labels per conversation. Q1 own goal / Q2 critical engagement /",
        "Q3 expressed confidence / Q4 follow-through. 'Mixed' rows are deliberate:",
        "they exist to generate disagreement for the debrief.",
        "",
        QUESTIONS,
        "",
        "| Conv | Q1 | Q2 | Q3 | Q4 | Notes |",
        "|------|----|----|----|----|-------|",
    ]
    for cid, (q1, q2, q3, q4, note) in ANSWER_KEY.items():
        lines.append(f"| {cid} | {q1} | {q2} | {q3} | {q4} | {note} |")
    lines += [
        "",
        "## Suggested item order per task (as uploaded)",
        "01 high anchor, 02 dependence, 03 ambiguous flagship, 04 low anchor,",
        "05 goal-tool divergence, 06 critical-but-discouraged.",
        "Participants code top-to-bottom; most will finish 2-3 items, so overlap",
        "concentrates on 01-03, which is where the debrief material lives.",
        "",
        "## Flagship debrief items",
        "EDU-03 / HEA-03 / AGR-03 (adopted goals, polite deference, partial",
        "follow-through) and the Q3 trap in EDU-02 (satisfaction is not efficacy).",
    ]
    (OUT / "ANSWER_KEY.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote ANSWER_KEY.md")

    # Sanity checks
    for fname, convos in sets.items():
        with open(OUT / fname, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 6, fname
        for r in rows:
            msgs = json.loads(r["transcript"])
            assert all(m["role"] in ("user", "assistant") for m in msgs)
            assert 8 <= len(msgs) <= 16, (r["name"], len(msgs))
    print("all CSVs validate: JSON parses, roles ok, 8-16 messages each")


if __name__ == "__main__":
    main()
