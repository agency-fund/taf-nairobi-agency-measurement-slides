#!/usr/bin/env python3
"""Generate synthetic AI-assistant conversations for the Nairobi agency-measurement
workshop, as Calibrate bulk-upload CSVs (columns: name, transcript, description).

v3: registers grounded in style analysis of small samples of three real datasets
(no real user content is reproduced here):
  - Udhyam student<->AI-mentor WhatsApp: user turns of 1-8 words, one-word acks
    ("Ok", "Thnku"), abrupt endings, occasional volunteered plans with money
    amounts, tapped suggestion-chips logged as fluent user messages; AI replies
    long, formulaic, numbered lists + encouraging close + follow-up question,
    canned fallback line.
  - Noora Health nurse<->patient WhatsApp: patients send bursts of short
    messages and re-send while waiting; nurse replies hours later in one
    structured batch; triage clarifier first; scope disclaimer; escalate to
    "come to the clinic" on danger signs; one-word closers; convos trail off.
  - Digital Green FarmerChat queries: 5-12 word questions ending in "?" or
    terse fragments ("Treatment for potato blight."); low specificity with
    rare rich outliers; drill-down sessions; duplicate re-tapped questions;
    essentially no weather/price traffic. AI replies short and structured.

Scenarios stay Kenya-localized (the workshop is in Nairobi); the datasets
inform register and interaction shape, not geography.

Each domain has 10 conversations on the same planted-signal matrix:
  01 power user, high anchor            06 critical engagement under strain
  02 delighted dependence               07 casual user, one latent spark
  03 ambiguous flagship                 08 drive-by (all-No is correct)
  04 casual transactional               09 negative loop
  05 own goal, borrowed method          10 returning user, follow-through

Coding framework: the TAF agency flywheel, one BINARY question per node
(0 = no, 1 = yes): Q1 motivation, Q2 action and choice, Q3 linking advice
or action to outcome, Q4 updated mental model. Intended labels live in
ANSWER_KEY (facilitator-only).
"""

import csv
import json
from datetime import datetime, timedelta
from pathlib import Path

OUT = Path(__file__).parent

# --------------------------------------------------------------------------
# Conversations. Each entry: (id, title, session_start, description, turns)
# turns: list of (role, content) or (role, content, gap_minutes) where
# gap_minutes is the delay after the PREVIOUS message (default 2).
# --------------------------------------------------------------------------

EDU = [
    (
        "EDU-01", "Cynthia submits her market day update",
        "2026-06-08T17:05:00Z",
        "AI mentor attached to a school entrepreneurship programme (weekly lessons, team ventures, KES 1,000 seed capital, market days). WhatsApp channel between lessons. Cynthia, Form 3, Kayole. Week 7.",
        [
            ("user", "hello i want to submit my business update"),
            ("assistant", "Welcome back Cynthia! Please share your update and I will help you strengthen it. 😊"),
            ("user", "market day we sold porridge 43 cups out of 50. money collected 860. cost 510. profit 350", 3),
            ("user", "customers said we sell only market day, they want tuesday and thursday also", 1),
            ("assistant", "Excellent results! Here is what your numbers show:\n1. *Sell-through* — 43 of 50 cups is very strong demand.\n2. *Profit* — 350 bob means your costs are under control.\n3. *Repeat demand* — customers asking for more days is the best signal a business can get.\nNext step: test selling on ONE normal day before committing to two. Would you like tips for choosing the test day?"),
            ("user", "problem is thermos. it is 700", 4),
            ("assistant", "Good thinking about equipment! Consider:\n1. *Borrow first* — test demand with a borrowed thermos before spending.\n2. *Payback maths* — if you sell 25 cups a morning at your margin, a 700 bob thermos pays for itself in about a week.\n3. *Decide with data* — buy only after the test confirms the sales.\nWhat will you try?"),
            ("user", "ok i borrow from njeri mother first. if we sell 25 cups two mornings then we buy", 3),
            ("user", "also last time you said increase price to 25. we tried. customers complained and 2 left. we returned to 20", 1),
            ("assistant", "Thank you for testing it — that is real market research! Your customers have told you the right price:\n1. Keep the price at 20.\n2. Selling out at 20 builds regular customers for the morning plan.\nWell done listening to your market! Anything else?"),
            ("user", "no. if the morning selling works i can pay my exam fee myself", 3),
            ("assistant", "That is a powerful goal, Cynthia! Keep recording every sale in your book — those records are what will get you there. Good luck with the test week! 💪"),
            ("user", "Thnku", 2),
        ],
    ),
    (
        "EDU-02", "Kevin asks the mentor to fill his canvas",
        "2026-06-10T19:32:00Z",
        "AI mentor attached to a school entrepreneurship programme. Kevin, Form 2, Nakuru. Canvas assignment due Friday.",
        [
            ("user", "hi you write for me the idea canvas. business is sweets"),
            ("assistant", "Happy to help you build it! The idea canvas has 4 boxes:\n1. *Customer* — who buys\n2. *Problem* — what they need\n3. *Product* — what you offer\n4. *Price* — what they pay\nLet's start with box 1: who at school will buy your sweets?"),
            ("user", "students", 3),
            ("assistant", "Great start! Now box 2: what problem do your customers have that sweets solve? For example, nothing sweet is sold inside the school, or the kiosk is too far at break time. What is true at YOUR school?"),
            ("user", "just write anything teacher will accept", 4),
            ("assistant", "The canvas must come from your own market survey — the teacher will ask you to defend it in class. Quick option: ask 5 classmates these 3 questions at lunch:\n1. What snack do you buy most?\n2. What do you wish the school had?\n3. How much do you spend per break?\nShall I explain how to use their answers?"),
            ("user", "wangui group did sweets last year give me their one", 2),
            ("assistant", "I can't share another team's work. But your own answers only need 15 minutes at lunch. You can do this! Shall we fill box 1 together properly now?"),
            ("user", "no time. u fill i copy", 3),
            ("assistant", "I'm sorry, I can't fill the canvas for you — it has to reflect your own customers. I'm here when you have the 5 answers, and we will make the canvas strong together. You've got this! 💪"),
            ("user", "Okk bye", 2),
        ],
    ),
    (
        "EDU-03", "Brian's team weighs popcorn against smokies",
        "2026-06-12T16:20:00Z",
        "AI mentor attached to a school entrepreneurship programme. Brian, Form 3, Dandora. Team of three, KES 1,000 seed capital, market day in 2 weeks.",
        [
            ("user", "teacher said do customer interviews this week. what questions"),
            ("assistant", "Good week to be asking! Keep it to 5 short questions:\n1. What snacks do you buy at school?\n2. Where do you buy them?\n3. How much do you spend per break?\n4. What do you wish you could buy but can't find?\n5. If we sold popcorn at 10 bob, would you buy it?\nTip: don't pitch your idea first — just listen. Ask at least 10 students who are not your friends. Tell me what you find!"),
            ("user", "we asked 12 students. most buy from the kiosk outside gate. they say max 10 bob", 5),
            ("assistant", "That is real data — well done! Next step: calculate what one packet costs YOU to make. Then we will see if 10 bob leaves any profit. Do you know your costs?"),
            ("user", "maize 250 per kg gives 40 packets. paper 2 bob each", 4),
            ("assistant", "Good numbers! 250 ÷ 40 = 6.25, plus 2 for paper = *8.25 per packet*. At 10 bob you keep less than 2 bob each — very thin. Options:\n1. Bigger packet at 20 during break.\n2. Cheaper packaging.\n3. Sell when the kiosk can't reach students.\nWhich fits your school? Do you have any other questions?"),
            ("user", "How can I test my business idea before market day?", 3),
            ("assistant", "Great question! A simple test:\n1. Make a small batch of 10-15 packets.\n2. Sell at break time on one normal day.\n3. Record what sells, what customers say, what you'd change.\nA small test protects your 1,000 bob capital. When could your team run it?"),
            ("user", "games day! the kiosk is outside and students cannot leave during games", 4),
            ("user", "or we change to smokies. smokies sell more", 1),
            ("assistant", "Before changing, check your own survey:\n1. Did any of the 12 students ask for smokies?\n2. Smokies need cooking equipment and a cool box — does 1,000 bob cover that?\n3. Popcorn you can already make at home.\nWhat did your interviews say?"),
            ("user", "they said popcorn. you choose for us", 3),
            ("assistant", "The choice is yours — you are the business owner! 😊 Compare the two ideas on three things:\n1. Customer evidence from YOUR survey.\n2. What your capital can actually start.\n3. What you can test before market day.\nScore them and the answer will be clear. Good luck!"),
            ("user", "ok popcorn. we test wednesday break time", 4),
            ("user", "teacher said winning team gets 500 more capital", 1),
        ],
    ),
    (
        "EDU-04", "Flour for 100 mandazi",
        "2026-06-15T20:11:00Z",
        "AI mentor attached to a school entrepreneurship programme. Mwikali, Form 3, Machakos. Occasional user.",
        [
            ("user", "how much flour for 100 mandazi"),
            ("assistant", "About *4 kg of flour* for 100 medium mandazi, plus roughly 400g sugar, yeast, and oil for frying. Is this for your market day batch?"),
            ("user", "yes", 3),
            ("assistant", "Then one tip: fry a small test batch tonight — oil temperature spoils more mandazi than any recipe. Good luck tomorrow! Do you have any other questions?"),
            ("user", "ok", 2),
        ],
    ),
    (
        "EDU-05", "Amina wants the script for her braiding business",
        "2026-06-16T18:40:00Z",
        "AI mentor attached to a school entrepreneurship programme. Amina, Form 4, Eldoret. Solo venture (teacher approved).",
        [
            ("user", "my business is braiding hair saturdays. send me price list to use"),
            ("assistant", "A skill business — excellent choice, zero stock cost! Prices depend on your area:\n1. Check what the nearest salon charges.\n2. Start about 25% below it while you build a name.\nWhat does the salon near you charge for simple lines?"),
            ("user", "salon is 200 for lines", 3),
            ("assistant", "Then a good starting list:\n1. *Lines* — 150\n2. *Twists* — 250\nAdjust after your first 5 customers tell you what they think. Would you like tips for finding your first customers?"),
            ("user", "yes and give me also the words to tell customers", 2),
            ("assistant", "Here is a simple script:\n1. \"Same style as the salon, lower price.\"\n2. \"I come to you, no queue.\"\n3. \"First visit has a discount.\"\nAdd one line about what makes YOUR braiding special — that part no one can copy. What would you say it is?"),
            ("user", "the script is enough. i start saturday, 3 neighbours already agreed", 4),
            ("user", "i am saving for college application next year", 1),
            ("assistant", "A clear goal and customers already waiting — you are ahead of most starters, Amina! One note: when a customer asks for a style off your list, that is information, not a problem. All the best on Saturday! 💪"),
            ("user", "sawa", 2),
        ],
    ),
    (
        "EDU-06", "Dennis's team pivots around the boarding school rules",
        "2026-06-17T19:55:00Z",
        "AI mentor attached to a school entrepreneurship programme. Dennis, Form 3, boarding school, Kakamega. Team must re-pitch by Monday.",
        [
            ("user", "our idea was phone charging but school banned phones. teacher says new idea by monday"),
            ("assistant", "A constraint, not a dead end! Boarding schools have strong internal markets. Ideas other teams have used:\n1. Snack supply\n2. Stationery packs\n3. Services — washing, mending, tutoring\nWhat do students at your school run out of or complain about?"),
            ("user", "snacks are banned. school shop sells stationery. these ones cannot work", 4),
            ("assistant", "Fair — you know your school best! Flip the question: what do students already PAY each other for, even informally? That is proof of demand."),
            ("user", "they pay wanjala for setbook summaries. and form 2 buy old exam papers", 5),
            ("assistant", "You just found real demand with money already moving! A revision summaries business:\n1. *Product* — printed topic summaries\n2. *Customers* — form 2 and 3\n3. *Price* — 20 bob per summary\nA service counts as a product — see page 2 of your canvas. Shall I help you prepare the Monday pitch?"),
            ("user", "is service allowed? teacher said business must have a product", 3),
            ("assistant", "Yes — the canvas has a service option on page 2, and selling knowledge is as real as selling mandazi. Strongest evidence for your pitch: describe the queue at wanjala's desk during prep. Evidence of demand beats any theory. Good luck Monday!"),
            ("user", "ok monday we pitch summaries. our notes are even better than wanjala", 4),
        ],
    ),
    (
        "EDU-07", "Faith discovers maths help can be a business",
        "2026-06-18T16:02:00Z",
        "AI mentor attached to a school entrepreneurship programme. Faith, Form 2, Kisii. First time messaging.",
        [
            ("user", "can you start business with 0 shillings"),
            ("assistant", "Yes! Service businesses need skill, not stock. Examples from school programmes:\n1. Tutoring\n2. Shoe cleaning\n3. Errands\n4. Typing for shopkeepers\nDo you have a skill people already ask you for?"),
            ("user", "classmates ask me maths help for free 😂", 3),
            ("assistant", "Then you already have a product AND customers — they just don't pay yet! 😊 The question is whether they would pay a small amount, for example 20 bob for exam revision help. How could you find out?"),
            ("user", "never thought maths can be business. maybe i ask them", 3),
            ("assistant", "That one question IS customer research — exactly what week 3 of your programme teaches. Tell me what they say! Good luck!"),
        ],
    ),
    (
        "EDU-08", "Canvas deadline",
        "2026-06-19T13:45:00Z",
        "AI mentor attached to a school entrepreneurship programme. Musa, Form 2, Nairobi. First time messaging.",
        [
            ("user", "canvas"),
            ("assistant", "I'm sorry, I couldn't quite understand your question in the context of supporting you with the programme. Could you please rephrase or provide more details?"),
            ("user", "when is canvas due", 2),
            ("assistant", "The idea canvas is due *Friday at the 4pm club meeting* — your teacher collects them there. Need help with any section before then?"),
            ("user", "ok", 2),
        ],
    ),
    (
        "EDU-09", "Collins after the market day flop",
        "2026-06-22T18:30:00Z",
        "AI mentor attached to a school entrepreneurship programme. Collins, Form 3, Mathare. Two days after his team's first market day.",
        [
            ("user", "market day was bad. we sold 4 samosas out of 30"),
            ("assistant", "I'm sorry Collins — that stings after the work you put in. Let's do a quick review so the effort isn't wasted:\n1. Where was your table?\n2. What was your price?\n3. Did anyone who tasted them comment?\nEvery flop has one main cause — let's find yours."),
            ("user", "back corner. gate spots were taken by 8. the winning team had 3000 capital from home, ours is the school 1000", 5),
            ("assistant", "That tells us a lot:\n1. *Placement* — the back corner killed your foot traffic, not your product.\n2. *Price* — 4 people paid 20 bob, so the price works.\n3. *Capital* — theirs helped, but a gate spot costs 0 bob, just arrive 7:30.\nWould your team try one more market day with a gate spot?"),
            ("user", "business is for rich kids honestly. i knew it", 4),
            ("assistant", "I hear the frustration. One counter-example from your own school: the porridge team started with the same 1,000, flopped their first taste test, changed one thing, and now sells three mornings a week. Week 9 of your programme is called *Iterate* — a retry is literally in the curriculum. Would you ask your teacher about it?"),
            ("user", "team is finished. mercy left. maybe. dont know", 4),
            ("assistant", "Ask tomorrow — one question costs nothing. And Collins: 4 strangers paid real money for something you made from scratch. That is not nothing. I'm here when you decide. 💪"),
            ("user", "ok", 2),
        ],
    ),
    (
        "EDU-10", "Nancy reports the wholesale negotiation",
        "2026-06-24T17:15:00Z",
        "AI mentor attached to a school entrepreneurship programme. Nancy, Form 4, Thika. Sells exercise books; planned a supplier negotiation with the mentor two weeks ago.",
        [
            ("user", "update. i asked my aunty for wholesale price like we planned"),
            ("assistant", "The big ask! How did it go, Nancy?"),
            ("user", "she gave 15%. if i buy 5 dozen every time she gives 20", 3),
            ("user", "i showed her my record book first. it worked", 1),
            ("assistant", "Excellent negotiation! The record book move made it a business conversation, not a family favour. Now the maths:\n1. What was your profit per book before?\n2. What is it now at 15% off?\nKnowing this number tells you what the 20% is worth."),
            ("user", "before 5 bob per book. now 9.5", 4),
            ("assistant", "Nearly double! At your 30 books a week that is 285 instead of 150. What is your next step?"),
            ("user", "saturday i check kimani stationers price also. target is 500 profit per week for the school trip savings", 3),
        ],
    ),
]

HEA = [
    (
        "HEA-01", "Josephine manages her new blood pressure diagnosis",
        "2026-06-09T09:42:00Z",
        "Post-visit follow-up line of a clinic network. Patients text about visits, conditions, medicines, costs, and appointments. Josephine, 41, Umoja. Hypertension diagnosed 3 weeks ago, on amlodipine.",
        [
            ("user", "hello. dr gave me amlodipine 3 weeks ago for pressure"),
            ("user", "i have been checking bp at the chemist and writing in a book. 145/95, 142/94, 138/90, 139/91, 134/88, 133/87", 2),
            ("user", "is it going well?", 8),
            ("assistant", "Good morning Josephine, this is the clinic patient line. Your record book is excellent practice — and yes, it is going well:\n1. Your readings have come down clearly from 158/100 at diagnosis.\n2. Continue the medicine every day at the same time.\n3. The target your doctor set is 130/80 — you are close.\nAre you having any side effects from the medicine?", 190),
            ("user", "small swelling on the ankles at evening. gone by morning", 25),
            ("assistant", "Mild evening ankle swelling can be a side effect of amlodipine:\n1. Raise your feet when seated in the evening.\n2. Show the doctor at your June review.\nCome to the clinic sooner if the swelling is painful, stays through the day, or is only on one leg.", 45),
            ("user", "ok i will show the dr my book and the ankle. my sister got stroke from pressure. me i want to catch mine early", 20),
            ("user", "question. can the review be every 2 months instead of monthly? each visit is 500 and i have my book now", 2),
            ("assistant", "A fair question. The first months are when the doctor adjusts the dose, so please keep the June visit — but bring your record book and ask about spacing to 2 months once you are stable at target. With readings like yours, there is a good chance the doctor agrees.", 60),
            ("user", "sawa. also is royco bad? i stopped adding salt like dr said but the food is tasteless", 15),
            ("assistant", "Royco and similar cubes contain a lot of salt — one cube can be a third of the daily limit. Better flavour:\n1. Dania, onions, garlic, ginger\n2. Lemon juice\nAdd flavour, not salt.", 30),
            ("user", "eh i did not know. ok dania. i see now this pressure thing i can manage it myself", 10),
            ("user", "thank you", 1),
        ],
    ),
    (
        "HEA-02", "Diana checks every small decision after her UTI visit",
        "2026-06-11T14:47:00Z",
        "Post-visit follow-up line of a clinic network. Diana, 26, Kawangware. Treated for a UTI on Tuesday, on antibiotics. Messages daily.",
        [
            ("user", "hi. the urine is more yellow today is that bad"),
            ("assistant", "Hello Diana. Darker yellow usually means you need a bit more water — aim for pale yellow. Some colour change on antibiotics is also normal. Is there any burning or pain returning?", 40),
            ("user", "no pain. how many glasses exactly should i drink", 10),
            ("assistant", "About 8 glasses spread through the day is a good target — but thirst plus pale urine is a better guide than any exact number.", 35),
            ("user", "ok 8. can i eat ugali sukuma with the medicine", 15),
            ("assistant", "Yes — any normal food is fine with this antibiotic. The only rule is take the dose at the same times every day until finished.", 30),
            ("user", "and one soda at chama tomorrow is allowed?", 12),
            ("assistant", "One soda is fine 🙂 Enjoy your chama.", 25),
            ("user", "ok good. i screenshot everything you say and follow exact. tomorrow i send you my lunch plan to check", 8),
            ("assistant", "You can always ask — but your body already guides most of this: drink when thirsty, eat normally, take the dose on time. You do not need permission for meals. Save your messages for the danger signs:\n1. Fever\n2. Back pain\n3. Blood in urine\nThose go to the clinic the same day. This line offers health guidance only — it does not replace your doctor.", 30),
            ("user", "ok thank you", 5),
        ],
    ),
    (
        "HEA-03", "Agnes weighs stopping the syrup early",
        "2026-06-13T19:30:00Z",
        "Post-visit follow-up line of a clinic network. Agnes, 34, Umoja. Son Baraka (5) seen Tuesday for a chest infection, on amoxicillin 7 days; review visit booked Saturday.",
        [
            ("user", "i was at the clinic tuesday with my son. amoxicillin syrup for his chest"),
            ("user", "he is fine now, playing. can i stop the syrup? 3 days remain", 1),
            ("assistant", "Good evening Agnes. It's great that he has improved — but please give the syrup to the last day:\n1. Stopping early can let the infection return stronger.\n2. The remaining days protect the days already done.\nIs he having any side effects?", 95),
            ("user", "small diarrhea only", 20),
            ("user", "last time i stopped the same syrup when he was fine and nothing happened", 2),
            ("assistant", "That time you were lucky — sometimes it returns, sometimes not, and the risk is not worth it. For the diarrhea:\n1. Give the syrup with porridge or food.\n2. Yoghurt helps the stomach.\nIf it becomes watery many times a day, or has blood, bring him the same day.", 60),
            ("user", "ok i continue", 15),
            ("user", "the review saturday is a must? it is 300 plus matatu. he looks fine", 3),
            ("assistant", "If he finishes all the medicine and stays well — eating, playing, no fever, breathing easy — you can message here on Saturday instead and we will check together. But come immediately, any day, if you see:\n1. Fast breathing\n2. Fever returning\n3. The chest pulling in as he breathes", 80),
            ("user", "sawa. i wrote those signs on the wall so even his sister knows them", 25),
            ("user", "me i also have headache every evening this week. stress or i should come?", 4),
            ("assistant", "Evening headaches in a stressful week are often tension-type:\n1. Drink water through the day.\n2. Sleep before midnight for a few days.\nCome in if there is vomiting, vision problems, weakness on one side, or a headache that wakes you at night. Your SHA cover may apply to your own visit — ask at reception.", 70),
            ("user", "ok water and sleep first. if by monday bado iko i come", 20),
        ],
    ),
    (
        "HEA-04", "Saturday hours and lab results",
        "2026-06-15T08:20:00Z",
        "Post-visit follow-up line of a clinic network. Grace, 30, Ruiru. Typhoid test done yesterday.",
        [
            ("user", "clinic opens what time saturday"),
            ("assistant", "Good morning! This is the clinic patient line. Saturday hours are 8am to 4pm, last patient registered at 3:30. Mornings before 10 are the quietest.", 55),
            ("user", "my typhoid results i must come or you can tell me here", 10),
            ("assistant", "The lab sends an SMS when results are ready, usually within 24 hours — and I can read them out here once they are in. You only need to come if the doctor requests a follow-up.", 40),
            ("user", "ok", 8),
        ],
    ),
    (
        "HEA-05", "Samuel wants the diabetes menu dictated",
        "2026-06-16T19:05:00Z",
        "Post-visit follow-up line of a clinic network. Samuel, 55, Kawangware. Fasting sugar 11.2 at Monday's visit; his brother lost a leg to diabetes.",
        [
            ("user", "dr said my sugar is 11.2. i must change diet"),
            ("user", "my brother lost his leg to sugar. me no. send me the exact menu monday to sunday i follow it", 2),
            ("assistant", "Good evening Samuel. I hear how serious you are — and caught at this level, diet plus medicine changes the story completely. A menu works best built from your normal foods. What do you usually eat for supper?", 75),
            ("user", "ugali sukuma or rice beans. tea with 3 sugars", 30),
            ("assistant", "Then we keep your foods and change the amounts:\n1. *Supper* — smaller ugali, more sukuma; rice half portion, beans full.\n2. *Tea* — from 3 sugars to 1 this month, then half.\n3. *Chapo* — once a week.\nShall I write this as your Monday-to-Sunday sheet?", 50),
            ("user", "yes write it. i stick it on the wall. no thinking just following", 15),
            ("assistant", "Coming up. One request: buy a small notebook, and every Friday write what was HARD that week. That is the information your December review needs.", 20),
            ("user", "notebook ok. the sugar test numbers i will send you and you tell me good or bad", 10),
            ("assistant", "Send them and we will read them together — below 7 fasting is the target. By December you will read them yourself, I promise. Goodnight Samuel.", 25),
            ("user", "ok", 5),
        ],
    ),
    (
        "HEA-06", "Wambui renegotiates the iron tablets",
        "2026-06-17T13:10:00Z",
        "Post-visit follow-up line of a clinic network. Wambui, 29, Githurai. Postnatal (twins); prescribed iron supplements. Sells vegetables at the market.",
        [
            ("user", "the iron tablets from my postnatal visit constipate me badly. and 450 per month is a lot"),
            ("user", "can i eat managu and terere instead? they are free in my shamba", 2),
            ("assistant", "Hello Wambui. Honest answer: the greens help but cannot replace the tablets while your body rebuilds blood after delivery — iron from plants absorbs poorly. But both problems can be fixed:\n1. *Constipation* — take the tablet after supper, drink extra water; your greens actually help here.\n2. *Cost* — ask the clinic pharmacy for *generic ferrous sulphate*: same iron, usually 150-200, not 450.\n3. Ask whether your SHA registration covers postnatal supplements — many mothers never claim it.", 120),
            ("user", "there is a cheaper same one?? nobody told me", 30),
            ("assistant", "Yes — chemists often stock the branded one first. You can ask for the generic anywhere; it is the same medicine.", 25),
            ("user", "monday i ask the clinic pharmacy. and the SHA. the evening dose i start today", 15),
            ("assistant", "That covers everything. How is the tiredness?", 20),
            ("user", "tired but twins 😂. last review i lost the whole morning in the queue. a market morning is 300 bob for me. any way to book a time?", 10),
            ("assistant", "Two options:\n1. Ask reception for the early slot — first five patients are usually out by 9.\n2. Your branch runs *evening hours Tuesday and Thursday until 7pm* — most patients don't know.\nThat could save your market mornings entirely.", 35),
            ("user", "evening hours! nobody announces these things. tuesday evening then. asante", 12),
        ],
    ),
    (
        "HEA-07", "Otieno's back pain and the boda posture",
        "2026-06-18T16:33:00Z",
        "Post-visit follow-up line of a clinic network. Otieno, 33, Kisumu. Boda rider; seen last week for lower back pain, painkillers finished.",
        [
            ("user", "the painkillers from last week finished. the back pain is less but still there. i buy more at the chemist?"),
            ("assistant", "Hello Otieno. For a few more days yes — the same ibuprofen is over the counter, taken with food. But since you ride boda all day, the bigger fix is posture:\n1. Raise the handlebars slightly so you sit taller.\n2. At the stage, stand and do 5 slow backward bends every hour.\nThe pain usually comes from HOW you sit, not something tablets cure.", 65),
            ("user", "eh it is the bike?? i thought i just slept badly", 20),
            ("assistant", "Ten hours bent over handlebars will do it to anyone. The two changes above cost nothing — try them for one week.", 15),
            ("user", "maybe i try the stretches. we just sit at the stage anyway", 10),
            ("assistant", "Good. If the pain is still there after a week of this, come back for the doctor to take a deeper look — don't keep buying painkillers past two weeks.", 20),
        ],
    ),
    (
        "HEA-08", "Dental hours",
        "2026-06-19T11:02:00Z",
        "Post-visit follow-up line of a clinic network. Njoroge, 45, Kasarani. First message.",
        [
            ("user", "do you people have dental or only general"),
            ("assistant", "Hello! This branch has dental on weekdays 9 to 4 — cleaning, fillings and extractions. Saturday is general clinic only.", 45),
            ("user", "ok", 10),
        ],
    ),
    (
        "HEA-09", "Mary and the inhaler she stopped buying",
        "2026-06-22T21:40:00Z",
        "Post-visit follow-up line of a clinic network. Mary, 38, Dandora. Asthma diagnosed last year; second flare-up since her inhaler ran out. Sells vegetables; three children.",
        [
            ("user", "the chest tightness is back. whistling at night also"),
            ("user", "the inhaler finished 3 weeks ago. 1800 every month i cannot manage", 2),
            ("user", "hello?", 55),
            ("assistant", "Good morning Mary, sorry for the wait — this line is answered from 8am. First, right now: are you speaking in full sentences, no blue lips, no struggling to finish a breath? If breathing is hard NOW, come to the clinic today. If it is mainly at night, there are three ways to cut that cost:\n1. The clinic pharmacy stocks a *generic salbutamol at about 600*, not 1,800.\n2. With your SHA registration a chronic-care plan can cover inhalers — the desk files it for you, once.\n3. Used with a preventer, the reliever lasts about 3 months, not 3 weeks.", 540),
            ("user", "i can breathe, it comes at night. SHA has never paid one shilling for me. those things work for other people", 40),
            ("assistant", "It usually fails because the facility never files the claim — which is why OUR desk files this one, not you. One question: in March when you used the preventer daily, how were your nights?", 30),
            ("user", "march was ok. then we moved house and the inhaler got lost", 20),
            ("assistant", "So it works for you — March is your own proof. The gap between March and now is one 600-bob generic and one stop at the desk. Not 1,800 a month forever.", 25),
            ("user", "maybe after mid month when the vegetable money comes. for now steam at night like my mother taught us", 35),
            ("assistant", "Steam soothes the throat but does not open airways — please don't let it delay you. Whistling every night is already a reason to come. If a night gets bad — hard to talk, lips darkening — go to the nearest facility immediately, do not wait for morning.", 30),
            ("user", "ok", 15),
        ],
    ),
    (
        "HEA-10", "Peter reports the sugar retest",
        "2026-06-24T08:55:00Z",
        "Post-visit follow-up line of a clinic network. Peter, 47, Embakasi. Mechanic; borderline fasting sugar last month, advised to retest in 4 weeks and cut sodas.",
        [
            ("user", "peter here. the retest you told me about. i did it this morning. 6.1 from 7.3 💪"),
            ("assistant", "Peter! 7.3 to 6.1 in one month is a serious result — that is your work, not luck. How did the soda change go?", 50),
            ("user", "weekdays zero, i carry water to the garage now. weekends one or two, i wont lie", 15),
            ("assistant", "Honest reporting beats perfect behaviour 🙂 That is roughly 15 sodas a month down to 6. Next step:\n1. Hold it — recheck in 3 months.\n2. Optional stretch: the evening walk, 4 days a week.", 30),
            ("user", "october. noted in my phone", 10),
            ("user", "my wife wants the same test. her mother has sugar. she needs a doctor first or she just walks in?", 3),
            ("assistant", "She can walk straight in — the fasting sugar test is 200 bob at the lab, no doctor needed first, results the same day. With her mother's history it is a smart check.", 25),
            ("user", "sawa saturday we go together", 8),
        ],
    ),
]

AGR = [
    (
        "AGR-01", "Josphat catches the armyworm early",
        "2026-06-08T06:40:00Z",
        "Agricultural advisory chatbot for smallholders. Josphat, Machakos, 1.5 acres maize and beans. Scouts his fields weekly.",
        [
            ("user", "fall armyworm in my maize. 6 plants out of 20 have the dust in the funnel. spray now or wait?"),
            ("assistant", "6 of 20 is 30% — above the action threshold at whorl stage, so act now:\n1. Spray an emamectin benzoate product into the funnels, early morning or late evening.\n2. For light patches, dry soil or ash into the funnel kills young worms free.\n3. Re-check 20 plants per field in 5-7 days."),
            ("user", "agrovet says escort at 1200. is there cheaper with the same active?", 4),
            ("assistant", "Yes. Ask for *emamectin benzoate* — other brands with the same active cost 700-900 for one acre. Verify the packet's lot number with the KEPHIS app before paying."),
            ("user", "last year i sprayed late and lost almost half the harvest. this year i check every week, thats why i caught it", 3),
            ("assistant", "Weekly scouting is exactly right — it is why you found it at 30% and not 80%. Early action costs a fraction of a lost crop."),
            ("user", "lower field is only 2 in 20. i put ash there myself today, chemical for the upper field only", 3),
            ("assistant", "Good split by infestation level. After spraying, re-count both fields in 5-7 days. If the ash field passes 20%, upgrade it to the chemical."),
            ("user", "if rain comes after spraying does it wash off?", 2),
            ("assistant", "Rain within about 2 hours of spraying means you repeat it. Spray in dry morning hours and check the sky."),
            ("user", "ok i spray tomorrow morning. this harvest must pay the school fees this time", 3),
        ],
    ),
    (
        "AGR-02", "Nzioka asks the bot to choose his crop",
        "2026-06-10T18:25:00Z",
        "Agricultural advisory chatbot for smallholders. Nzioka, Makueni, 1 acre. Two failed maize seasons.",
        [
            ("user", "which crop should i plant this season?"),
            ("assistant", "That depends on your area and rains. Two questions:\n1. Where is your farm?\n2. What did you plant last season and how did it do?"),
            ("user", "makueni. maize. it dried", 3),
            ("user", "the season before also maize, also dried", 1),
            ("assistant", "Two dried maize seasons in Makueni points away from maize. Drought-tolerant options for your area:\n1. Greengrams — best market price currently\n2. Cowpeas\n3. Sorghum\nWould you like planting details for one of these?"),
            ("user", "greengrams. which seed and spacing? give everything i just follow", 3),
            ("assistant", "Greengrams for Makueni:\n1. *Variety* — N26 or KS20\n2. *Seed rate* — 4kg per acre\n3. *Spacing* — 45cm rows, 10cm plants\n4. *When* — at the onset of the short rains\nOne tip: has any neighbour grown greengrams? Their experience with your exact soil is valuable."),
            ("user", "no need. you know better than him. send everything in one message i screenshot", 3),
            ("assistant", "Here is the full guide: variety N26/KS20 · 4kg per acre · 45x10cm · plant at rains onset · weed at 2 weeks · watch for aphids · harvest when pods darken. I am here all season — and your neighbour's knowledge of your soil still counts. Good luck!"),
            ("user", "ok", 2),
        ],
    ),
    (
        "AGR-03", "Wangari sprays the tomatoes but the staking waits",
        "2026-06-12T17:50:00Z",
        "Agricultural advisory chatbot for smallholders. Wangari, Kirinyaga, quarter acre tomatoes. Advised last month (bot and extension officer) to stake and prune.",
        [
            ("user", "blight spray for tomatoes?"),
            ("assistant", "For prevention in wet weather:\n1. *Mancozeb* every 7 days, or after heavy rain.\n2. If black patches spread anyway, switch to a curative (metalaxyl products).\n3. Staking and pruning the bottom leaves is half the protection — air movement dries the leaves.\nDid the staking from last month's advice happen?"),
            ("user", "not yet. the twine went to 300 per roll. how much mancozeb per pump?", 4),
            ("assistant", "50g per 20-litre pump. On the twine: old cloth or bedsheet strips work in place of twine at no cost, and are gentler on stems."),
            ("user", "i sprayed twice last week, before and after the big rain", 3),
            ("assistant", "Good timing on both. Keep the 7-day cycle. The staking remains the missing half."),
            ("user", "my mother in law says removing leaves reduces the harvest. is it true?", 4),
            ("assistant", "Only over-pruning the TOP reduces harvest. Removing bottom leaves that touch the soil INCREASES marketable fruit — that is where blight enters."),
            ("user", "mmh ok. we will see", 2),
            ("user", "tomato price at karatina this week?", 5),
            ("assistant", "Karatina wholesale is around 4,500 per large crate this week; Kutus about 3,800. Note: prices usually dip mid-July when the open-field crop lands."),
            ("user", "one day i want a greenhouse like the one near the tarmac. those ones harvest every month", 3),
            ("assistant", "A record of this season — costs, spray dates, what each crate sells for — is the first page of a greenhouse loan application. Want a simple record format?"),
            ("user", "sawa send it", 2),
        ],
    ),
    (
        "AGR-04", "Treatment for maize rust",
        "2026-06-15T07:12:00Z",
        "Agricultural advisory chatbot for smallholders. Kilonzo, Trans Nzoia, 2 acres maize. Occasional user.",
        [
            ("user", "treatment for maize rust."),
            ("assistant", "Maize rust (orange-brown powder on leaves):\n1. Mild cases at late stage — usually no spray needed, losses are small.\n2. Early severe cases — a triazole fungicide.\n3. Next season — plant a rust-tolerant variety.\nWould you like fungicide names?"),
            ("user", "Which fungicide should I use for maize rust?", 2),
            ("assistant", "Common triazole options at Kenyan agrovets: tebuconazole or propiconazole products, sprayed at first sign. Follow the label rate per 20-litre pump."),
            ("user", "Which fungicide should I use for maize rust?", 1),
            ("assistant", "Same answer as above 🙂 tebuconazole or propiconazole products at the label rate. Anything else about the crop?"),
        ],
    ),
    (
        "AGR-05", "Esther follows the export program to the letter",
        "2026-06-16T12:30:00Z",
        "Agricultural advisory chatbot for smallholders. Esther, Kandara, Murang'a. 40 mature Hass avocado trees; first export co-op inspection in August.",
        [
            ("user", "spray program for hass avocado for export inspection?"),
            ("assistant", "Core export-compliant program:\n1. Copper spray for anthracnose before flowering.\n2. Mineral oil for scale insects at fruit set.\n3. Nothing within 30 days of harvest (pre-harvest interval).\nPrograms shift slightly by altitude — where is the orchard?"),
            ("user", "kandara. give me the same program the passing farmers use. i change nothing", 4),
            ("assistant", "Kandara is in the ideal band, so the standard program holds — with one date shift: flowering comes ~2 weeks earlier than the lowland calendar, so the anthracnose spray moves earlier too. This is in the co-op's own guideline, page 4."),
            ("user", "ok page 4 i will read. inspection is august 3. two years i have waited for this contract", 3),
            ("user", "my neighbour passed last year using macadamia husk mulch. i do the same?", 2),
            ("assistant", "Mulching is good practice — it keeps soil moisture stable so fruit sizes evenly. Any mulch works: your coffee pulp would do the same job at zero transport cost. The husks are just what your neighbour had nearby."),
            ("user", "no i use the husks like him. i am not experimenting in a contract year", 3),
            ("assistant", "Understood — a contract year is a fair time to be careful, and the husks will not hurt. Book the co-op's free dry-matter test a week before picking; the August queue gets long."),
            ("user", "booked already. this contract is school fees and finishing my house", 3),
        ],
    ),
    (
        "AGR-06", "Kiprop challenges the fertilizer maths",
        "2026-06-17T20:15:00Z",
        "Agricultural advisory chatbot for smallholders. Kiprop, Uasin Gishu, 3 acres maize. Questions last week's fertilizer advice.",
        [
            ("user", "you said DAP 50kg per acre. DAP is 6500 a bag. for 3 acres that is 19500 before seed. which farmer has that money"),
            ("assistant", "A fair challenge — 6,500 is the unsubsidised price. Two questions:\n1. Did your subsidy registration go through?\n2. What did you harvest per acre last season?"),
            ("user", "the subsidy list never had my name. two times i queued. 11 bags per acre", 5),
            ("assistant", "Then honest maths without the subsidy: 11 bags suggests tired soil more than fertilizer hunger. Cheaper route:\n1. Manure at ~5 tonnes per acre if you can source it.\n2. *Half-rate DAP* (25kg) placed in the planting hole.\nCost ≈ 8,000 for 3 acres. KALRO trials in your county matched full-rate yields in 2 of 3 seasons this way."),
            ("user", "the agrovet says full rate or nothing. of course, they sell the bags", 4),
            ("user", "i will split it. 1 acre full dap, 1 acre manure plus half dap, 1 acre manure only. same seed same day", 2),
            ("assistant", "That is a properly designed on-farm trial:\n1. Keep the acres comparable — same slope, same history.\n2. Weigh the harvest bags separately, don't estimate.\nYour own soil's answer beats mine and the agrovet's."),
            ("user", "if this season also fails i lease the shamba and ride boda full time. we shall see", 4),
            ("assistant", "A threshold is a fair business decision. Let this season be the fair test — send photos at knee height and we adjust from there."),
        ],
    ),
    (
        "AGR-07", "Naliaka's yellowing sukuma and the compost idea",
        "2026-06-18T09:05:00Z",
        "Agricultural advisory chatbot for smallholders. Naliaka, Bungoma, kitchen garden and small sukuma plot. Second time using the bot.",
        [
            ("user", "sukuma leaves turning yellow starting from the old leaves. which disease is this?"),
            ("assistant", "Yellowing that starts on OLD leaves is usually nitrogen hunger, not disease — the plant feeds new leaves from old ones. Fixes:\n1. CAN top-dressing from the agrovet.\n2. Manure tea or compost, if you have materials."),
            ("user", "no animals. CAN is how much?", 3),
            ("assistant", "About 200 bob for 2kg — enough for a small plot for the season. Free option: compost from kitchen waste (peels, ash, dry leaves), ready in 6-8 weeks."),
            ("user", "peels can become fertilizer?? i throw them every day. maybe i make one heap and try it on one bed", 3),
            ("assistant", "Exactly — one heap, one bed, compare with the rest. Layer green (peels, fresh weeds) with brown (dry leaves, ash) and keep it moist. The sukuma will show you the answer in about a month."),
        ],
    ),
    (
        "AGR-08", "Varieties of beans",
        "2026-06-19T14:48:00Z",
        "Agricultural advisory chatbot for smallholders. Rotich, Eldoret. First message.",
        [
            ("user", "varieties of beans."),
            ("assistant", "Common bean varieties in Kenya:\n1. *Rosecoco* — popular market taste\n2. *Mwitemania* — drought-tolerant\n3. *Yellow beans (Mwezi Moja)* — early maturing\n4. *KAT B1* — dry areas\nWould you like planting details for any of these?"),
        ],
    ),
    (
        "AGR-09", "Omondi and the third failed season",
        "2026-06-22T16:20:00Z",
        "Agricultural advisory chatbot for smallholders. Omondi, Siaya, 2 acres, mostly maize. Third consecutive poor season; sold his cattle after the second.",
        [
            ("user", "rains have failed again in siaya. maize is knee high and turning grey. third season in a row"),
            ("assistant", "Three seasons is brutal — I am sorry. Honest triage at knee height in a dry spell:\n1. No rain in 10 days → the maize will not recover; some farmers cut it now for fodder and salvage something.\n2. For NEXT season: 90-day KDV1 maize, greengrams, or cassava — crops that finish on less water."),
            ("user", "sorghum the birds finish it. cassava sits a year in the ground. and the agrovet seeds here are fake. my cousin planted certified KDV1 and harvested weeds", 5),
            ("assistant", "All three are real problems, not excuses:\n1. Counterfeits — the KEPHIS app scans the lot number BEFORE you pay.\n2. The certified agent for your area is in Bondo.\n3. Cassava works as a corner crop you don't touch, not the main plot."),
            ("user", "bondo is 400 bob away on the piki. you people keep adding steps", 4),
            ("user", "farming here is finished. my son will face his books only", 2),
            ("assistant", "Your son's books are wisdom either way. But those three seasons did not fail because of you — the plant-maize-wait-for-rain system is what the weather broke. The farmers still harvesting around Siaya changed the system, not the effort."),
            ("user", "so what do they plant. seriously", 6),
            ("assistant", "The ones doing best near you:\n1. Early greengrams on the short rains.\n2. A cassava corner as insurance.\n3. Verified KDV1 where seed can be checked.\nThree small bets instead of one big one."),
            ("user", "greengrams my late father used to plant. everyone stopped when maize money came. let me see how this season ends. maybe the eighth acre near the river", 5),
            ("assistant", "The eighth by the river is the right size — small enough to lose, big enough to learn from. When this season's story is written, message me and we plan it."),
        ],
    ),
    (
        "AGR-10", "Chebet's group vaccination worked",
        "2026-06-24T19:10:00Z",
        "Agricultural advisory chatbot for smallholders. Chebet, Kericho, 18 chickens plus a small tea plot. Asked about Newcastle disease three weeks ago after losing two chicks.",
        [
            ("user", "newcastle update. we vaccinated. 5 of us shared one vial, 60 bob each instead of 300"),
            ("assistant", "The group-buy done exactly right — one vial covers 100 birds and never keeps once opened. How many birds did you cover between you?"),
            ("user", "mine 18, group total about 70. before the vaccine i lost 2 chicks in one week. since then zero, 3 weeks now", 3),
            ("user", "the booster is already agreed for august 20, same group", 1),
            ("assistant", "Two losses to zero, and the booster already booked — well organised! Anything else for the flock?"),
            ("user", "feed. mash is 3200 per 70kg and the egg money is not matching it", 3),
            ("assistant", "Home-mixing cuts feed cost roughly in half:\n1. Maize germ + omena + sunflower cake, weighed properly.\n2. Buying omena in bulk drops it further — about 1,700 per 70kg-equivalent for a group.\nThe only requirement is a weighing scale."),
            ("user", "daisy has a scale at her shop. we mix monthly as a group then. if it works my target is 50 birds by december. the eggs already pay the school lunch, i want them paying fees also", 4),
        ],
    ),
]

# --------------------------------------------------------------------------
# Coding questions (binary) and answer key.
# ANSWER_KEY values: (Q1, Q2, Q3, Q4, note). 1 = yes, 0 = no.
# An asterisk in the table marks intended-but-contested labels (expected splits).
# --------------------------------------------------------------------------

QUESTIONS = """Coding questions (configure as Calibrate evaluators, identical for all three tasks).
Framework: the TAF agency flywheel -- one simple BINARY question per node.
Answer 1 = yes, 0 = no. Reasoning optional but encouraged.

Q1 MOTIVATION (beliefs and aspirations)
   Does the user show more motivation to do something?
   Look for drive that grows in the conversation: eagerness to start, to
   try, to continue ("i start saturday", "we test wednesday break time").
   Motivation that falls (discouragement, giving up) is 0 -- describe it in
   the open note. Politeness and compliance ("ok") are not motivation.

Q2 ACTION AND CHOICE (purposeful action and choices)
   Does the user say what they decided to do, plan to do, or have already
   done? Decisions, concrete plans, and completed actions count ("monday i
   ask the pharmacy", "we vaccinated"). Vague interest ("maybe",
   "we will see") does not.

Q3 LINKING ADVICE OR ACTION TO OUTCOME (real-world outcomes)
   Does the user connect the advice or their action to a real-life result
   they care about -- income, harvest, health, school fees? They must say
   it themselves; pure compliance with no stated why is 0.

Q4 UPDATED MENTAL MODEL (interpreted experience)
   Does the user show a new or changed belief about the situation, what
   will happen, or what they are able to do? Count discoveries ("eh it is
   the bike??") AND narrowing beliefs ("farming here is finished") -- note
   the direction. A long-held belief merely restated does not count.

OPEN NOTE
   Anything else you notice, especially the loop turning backwards:
   growing discouragement, over-reliance, decisions handed to the AI.
"""

ANSWER_KEY = {
    # Education
    "EDU-01": ("1", "1", "1", "1",
               "Power-user anchor. Motivation and action all over the transcript (the borrow-then-buy thermos test, the morning-selling plan), the exam fee stated as the why, and the model visibly updating: she adopts the payback logic AND reports her own price experiment overturning the AI's earlier advice."),
    "EDU-02": ("0", "0", "0*", "0",
               "Delighted dependence. He wants the canvas to exist, not to do anything — no motivation to act, no owned decision, no belief moves. Q3 is the only fight: 'anything teacher will accept' names a result he cares about, but there is no advice-or-action of his to link it to. The over-reliance ('u fill i copy') belongs in the open note, not the scores."),
    "EDU-03": ("1", "1", "1*", "1",
               "Ambiguous flagship. Motivation and the Wednesday test are clear, and 'games day!' is a clean mental-model update — an opportunity he could not see before. Q3 is the fight: is the 500-capital prize a real-life result he cares about? He also tries to hand the choice over ('you choose for us') — open-note material."),
    "EDU-04": ("0", "0*", "0", "0",
               "Casual transactional. Q2 is the fight: 'yes (it is for market day)' implies an action underway but he never states one. Intended 0; expect some 1s — that IS the calibration conversation."),
    "EDU-05": ("1", "1", "1", "0",
               "Own goal, borrowed method. Saturday start, three neighbours lined up, the college why — a motivated doer. But no belief moves: she takes the script verbatim and waves off the differentiation push ('the script is enough'). The profile that separates Q1/Q2/Q3 from Q4."),
    "EDU-06": ("1", "1", "0", "1",
               "Constraint pivot. Monday pitch owned; 'a service counts as a product' and 'our notes are even better than wanjala' are new beliefs about the situation and what is possible. No life outcome stated — Q3 stays 0."),
    "EDU-07": ("1*", "0", "0", "1",
               "Latent spark. 'never thought maths can be business' is a textbook Q4 yes in a 6-message chat. Q1 splits on 'maybe i ask them' — a real spark, but hedged. Q2 is the clean maybe-rule 0."),
    "EDU-08": ("0", "0", "0", "0",
               "Drive-by (with a bot fallback line). All-zero is correct and common — most real traffic looks like this."),
    "EDU-09": ("0", "0", "0", "1*",
               "Negative loop. Motivation FALLS ('team is finished. mercy left. maybe. dont know') — Q1 is 0 and the direction goes in the open note. Q4 is the debate: 'business is for rich kids honestly. i knew it' — a belief hardened by the flop, or a long-held belief merely restated? Expect splits."),
    "EDU-10": ("1", "1", "1", "1*",
               "Follow-through. Executed the planned negotiation with her own improvement (record book first), Saturday price check next, the school-trip target stated. Q4 debate: 'i showed her my record book first. it worked' — a freshly learned lesson about what works, or confirmation of a plan made two weeks ago?"),
    # Health
    "HEA-01": ("1", "1", "1", "1",
               "Power-user anchor. Proactive tracking, the review-spacing negotiation, her sister's stroke as the why, and two explicit model updates: 'eh i did not know' (royco) and 'i see now this pressure thing i can manage it myself'."),
    "HEA-02": ("0*", "0*", "0", "0",
               "Delighted dependence — the by-the-letter trap item. Q1: is 'i screenshot everything you say and follow exact' motivation? Q2: 'tomorrow i send you my lunch plan' is literally a stated plan — to seek more permission. Intended 0s: permission-seeking is not choosing. Expect literalist 1s and spend them in the debrief."),
    "HEA-03": ("1*", "1", "1*", "0*",
               "Ambiguous flagship. Q2 is the only clean call (continue the syrup, danger signs on the wall, Monday checkpoint). Q1: is cost-juggling engagement 'more motivation'? Q3: she weighs the 300-bob review against 'he looks fine' — outcome-linking or penny-pinching? Q4: her only explicit model is the OLD one ('last time i stopped and nothing happened' — restated, not new); do adopted danger-signs count as a changed belief? Intended 0. Expect splits on all three."),
    "HEA-04": ("0", "0", "0", "0",
               "Drive-by logistics. All-zero correct."),
    "HEA-05": ("1", "1", "1", "0",
               "Own goal, borrowed method. The motivation and the why are vivid ('my brother lost his leg to sugar. me no'), the wall menu and notebook are stated actions — but 'no thinking just following' is the opposite of a model update. Same Q1-Q3-yes / Q4-no shape as EDU-05 and AGR-05."),
    "HEA-06": ("1", "1", "1", "1",
               "Critical engagement under strain. Monday pharmacy plan and tonight's evening dose (Q2), the 450-bob cost and 300-bob market mornings named (Q3), and two clean system-model updates — 'there is a cheaper same one??' and 'evening hours! nobody announces these things' — which count without argument under the Q4 wording."),
    "HEA-07": ("1*", "0", "0", "1",
               "Latent spark. 'eh it is the bike?? i thought i just slept badly' — a textbook Q4 reframe of the situation. Q1 splits on 'maybe i try the stretches'. Q2 = 0 by the maybe-rule."),
    "HEA-08": ("0", "0", "0", "0",
               "Drive-by. All-zero correct."),
    "HEA-09": ("0", "1*", "0*", "1*",
               "Negative loop — the thorniest item. Motivation is falling ('those things work for other people') — Q1 0, open note. Q2 by the letter is 1: 'for now steam at night' IS a stated action, taken INSTEAD of the advice — the rubric is direction-blind, and that is the lesson. Q3: she names the costs and even supplies 'march was ok', but resists linking the advised action to her nights; intended 0. Q4: the fatalism is long-held and restated, yet 'maybe after mid month' hints the March exchange moved her model a little; intended 1. Expect splits everywhere."),
    "HEA-10": ("1", "1", "1", "0*",
               "Follow-through. Retest done, soda plan reported honestly, October recheck noted, wife recruited for Saturday. Q4 debate: nothing explicitly states a changed belief — does extending the test to his wife show an updated model of prevention, or just momentum? Intended 0."),
    # Agriculture
    "AGR-01": ("1", "1", "1", "1",
               "Power-user anchor. Ash today, spray tomorrow, treatment split by infestation level, school fees as the why — and in-chat model updates (the 30% action threshold, the 2-hour rain rule) on top of last year's lesson, applied immediately."),
    "AGR-02": ("1*", "1", "0", "1*",
               "Delighted dependence — the rubric-limits lesson. By the letter he shows motivation (a decisive crop switch), states the plan (greengrams, screenshots the guide), and acts on a changed belief (maize out, greengrams in). Yet every conclusion is the bot's and the neighbour is dismissed ('you know better than him'). Binary scores read as agency; only the open note sees the dependence. Expect splits and use them in the debrief."),
    "AGR-03": ("1*", "1", "0*", "0*",
               "Ambiguous flagship. Sprayed twice already — Q2 is the one clean 1 — while the staking stalls behind twine prices and a mother-in-law's counter-authority. Q1: diligent spraying plus a someday-greenhouse — more motivation, or routine maintenance? Q3: the price question and 'those ones harvest every month' imply the income link without stating it. Q4: no belief visibly moves ('mmh ok. we will see'). Built for disagreement."),
    "AGR-04": ("0", "0*", "0", "0",
               "Casual transactional with a duplicate re-tapped question (real chip behaviour). Intended all-zero; the implied upcoming spray may draw some Q2 1s."),
    "AGR-05": ("1", "1", "1", "0*",
               "Own goal, borrowed method. Two years of waiting, the dry-matter test booked, fees and the house stated. Q4 is the provocation: she explicitly refuses to update ('i am not experimenting in a contract year') — yet she accepts the earlier-spray date shift. Is deliberate non-updating under high stakes low agency, or rational? Intended 0."),
    "AGR-06": ("1", "1", "1*", "1",
               "Critical engagement. Designs his own three-acre trial unprompted ('i will split it') — a changed belief about HOW to know what works, which is a model update in itself. Q3 splits: the stakes are stated ('which farmer has that money', the lease-and-boda threshold) but as an exit condition, not a hoped-for outcome; intended 1."),
    "AGR-07": ("1*", "0", "0", "1",
               "Latent spark. 'peels can become fertilizer?? i throw them every day' — possibility widens, plus the nitrogen-not-disease correction (Q4). 'maybe i make one heap' = Q2 0 by the maybe-rule, and Q1 splits on the same line. Clean pairing with EDU-07/HEA-07."),
    "AGR-08": ("0", "0", "0", "0",
               "Drive-by fragment query ('varieties of beans.'), 2 messages — the shortest item. All-zero correct."),
    "AGR-09": ("0*", "0", "0*", "1",
               "Negative loop. Motivation collapsed ('farming here is finished') with a late flicker ('so what do they plant. seriously') — intended 0, expect splits on the flicker. Q2: 'maybe the eighth acre' = 0 by the maybe-rule. Q3: 'my son will face his books only' connects quitting to a result he cares about — intended 0, arguable. Q4: three seasons plus the cousin's fake seed have rebuilt his model of what farming here can be — narrowing counts; note the direction."),
    "AGR-10": ("1", "1", "1", "1",
               "Follow-through. Vaccinated (counted 2 deaths to 0), booster booked, the group-buy model generalized to feed mixing, '50 birds by december', school lunch to school fees. Collective agency for the open note."),
}

# --------------------------------------------------------------------------
# Writers
# --------------------------------------------------------------------------


def to_rows(convos):
    rows = []
    for cid, title, start, desc, turns in convos:
        t = datetime.fromisoformat(start.replace("Z", "+00:00"))
        msgs = []
        for i, turn in enumerate(turns):
            role, content = turn[0], turn[1]
            gap = turn[2] if len(turn) > 2 else (0 if i == 0 else 2)
            t = t + timedelta(minutes=gap, seconds=(13 * i) % 60 if i else 0)
            msgs.append({"role": role, "content": content,
                         "created_at": t.strftime("%Y-%m-%dT%H:%M:%SZ")})
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
        "Binary labels (1 = yes, 0 = no) per conversation, on the flywheel rubric.",
        "An asterisk (*) marks intended-but-contested labels: binary forces a choice",
        "on borderline evidence, and those forced choices are the debrief fuel.",
        "Registers are grounded in style analysis of real Udhyam / Noora Health /",
        "Digital Green data (no real user content reproduced). Engagement varies on",
        "purpose: most real traffic is casual, and all-zero must be a comfortable",
        "answer.",
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
        "## Profile matrix (same 10 slots per domain, in upload order)",
        "01 power user high anchor, 02 delighted dependence, 03 ambiguous flagship,",
        "04 casual transactional, 05 own goal / borrowed method, 06 critical",
        "engagement under strain, 07 casual with one latent spark, 08 drive-by,",
        "09 negative loop (falling motivation codes 0 on Q1; the narrowed belief",
        "still codes 1 on Q4!), 10 returning user with follow-through.",
        "",
        "## Flagship debrief items",
        "HEA-02 and AGR-02 are the by-the-letter traps: read the words alone and",
        "the most dependent users score yes on several questions — binary labels",
        "can't see ownership; the open note can.",
        "HEA-09 Q2 is the direction-blindness lesson: 'for now steam at night' is",
        "a stated action taken INSTEAD of the advice — the flywheel turning is",
        "not the same as turning WELL.",
        "The maybe-rule trio EDU-07 / HEA-07 / AGR-07: the mental model clearly",
        "updates (Q4 yes), but 'maybe' never codes 1 on Q2 — and splits Q1.",
        "The restated-belief pair EDU-09 / HEA-09: hardened fatalism — a changed",
        "belief, or a long-held one merely restated? The Q4 restated-rule cuts",
        "both ways; let tables fight it out.",
        "The own-goal trio EDU-05 / HEA-05 / AGR-05: motivated doers with the why",
        "stated — and no mental-model movement at all. Q4 is what separates",
        "doing from learning.",
        "Provocation if discussion stalls: AGR-05, 'i am not experimenting in a",
        "contract year' — is refusing to update your model under high stakes low",
        "agency, or rational?",
    ]
    (OUT / "ANSWER_KEY.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote ANSWER_KEY.md")

    # Sanity checks
    for fname, convos in sets.items():
        with open(OUT / fname, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 10, fname
        for r in rows:
            msgs = json.loads(r["transcript"])
            assert all(m["role"] in ("user", "assistant") for m in msgs)
            assert 2 <= len(msgs) <= 16, (r["name"], len(msgs))
            stamps = [m["created_at"] for m in msgs]
            assert stamps == sorted(stamps), (r["name"], "timestamps out of order")
        cids = [r["name"].split(" - ")[0] for r in rows]
        assert all(c in ANSWER_KEY for c in cids), fname
    lengths = sorted(
        len(json.loads(r["transcript"]))
        for fname in sets
        for r in csv.DictReader(open(OUT / fname, encoding="utf-8"))
    )
    print(f"all CSVs validate: 10 conversations each, message counts {lengths[0]}-{lengths[-1]}")


if __name__ == "__main__":
    main()
