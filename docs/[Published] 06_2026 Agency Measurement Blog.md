# Measuring Agency in a Digital Context

*A Practitioner’s Guide from The Agency Fund and Google Jigsaw*

By Zezhen Wu, Beth Goldberg, Rachel Xu

## **![][image1]**

## 

[https://theagencyfund.substack.com/p/measuring-agency-in-a-digital-context](https://theagencyfund.substack.com/p/measuring-agency-in-a-digital-context)

## **Summary**

* **The Agency Fund and Google Jigsaw have co-developed a free set of resources and AI tools to help measure how digital and AI tools shape human agency in practice**: an open-source [Claude Skill](https://github.com/agency-fund/taf-skills/tree/main/ask-agency-measurement) that helps you brainstorm alongside this blog and a curated [NotebookLM](https://notebooklm.google.com/notebook/fc5c61b3-a3b8-462a-9ed2-9778d70f8386?authuser=1) with useful papers and measurement approaches.

* **Why should tech teams care about agency?** Research increasingly shows that digital and AI tools can expand human agency; but when poorly designed or implemented, they can also undermine it.

* **What is agency in the context of digital and AI tools?** Agency is a person’s capability to navigate toward the future they want. It can be experienced internally (e.g., feeling capable or empowered) or expressed externally through action. Agency may concern a user’s end goals independent of technology, or their ability to shape, control, and effectively use a tool in pursuit of those goals.

* **How do we measure agency?** It should be measured as an outcome, not inferred from engagement alone. Teams should specify what agency means for their specific users and contexts. We suggest three broad steps: 

1. Define agency for your local problem  
2. Choose the right measurement tools for the right type of on-platform or off-platform data, measured at the right moment  
3. Test and validate the measurement tools iteratively

## 

## **Why agency?**

Around the world, digital tools are expanding what people can imagine, decide, and act on at a greater scale. Despite growing concern that AI and other tools can [undermine or substitute for human agency](https://arxiv.org/abs/2601.19062), our experience suggests the opposite is often true: digital tools can significantly *expand* agency, especially when support is otherwise hard to access.

Consider these examples from our partners: 

* Indian farmers consulting [Digital Green’s FarmerChat](https://digitalgreen.org/farmer-chat/) after weather-related crop damage  
* Kenyan mothers getting maternal health advice from [Jacaranda Health’s PROMPTS](https://jacarandahealth.org/prompts/) and learning to communicate best practices with their family members  
* Brazilian teachers getting feedback from [Nova Escola’s](https://novaescola.org.br/tudo-sobre/planos-de-aula-por-whatsapp/) WhatsApp AI assistant on how to generate lesson plans to help students navigate difficult topics  
* Indian students using AI mentors to develop business ideas [(Udhyam](https://udhyam.org/)) or get feedback on their creative process ([The Apprentice Project](https://www.theapprenticeproject.org/))   
* Young Malians learners chatting and brainstorming in Bambara with an AI mentor and recording a video about their future goals [(Kabakoo Academies](https://www.kabakoo.africa/))   
* Local officials in [Kentucky](https://medium.com/jigsaw/how-one-of-the-fastest-growing-cities-in-kentucky-used-ai-to-plan-for-the-next-25-years-3b70c4fd1412) using AI to process 1 million+ resident ideas for city planning

But how can we tell whether a tool is expanding agency or undermining it? Not by usage metrics alone; a tool can look successful when many people use it often, but that doesn’t show whether it’s expanding users’ agency or improving their lives. We need to measure agency explicitly by answering three questions: **What is agency? Why should we measure it? And how can measurement show whether digital tools actually support it?**

Co-developed by [The Agency Fund](https://www.agency.fund/) and [Google Jigsaw](https://jigsaw.google/), this blog – and set of AI tools (see links below) – offers a primer for anyone building and evaluating digital tools that aim to expand rather than undermine agency. The Agency Fund approaches this from a global development lens, [investing in people’s capacity to author their own lives](https://theagencyfund.substack.com/p/how-to-build-human-agency); Jigsaw, an incubator within Google, builds technology to [narrow the divides between people’s desire to shape their world and their ability to do so](https://jigsaw.google/building-for-agency-ai-era/).

## 

## **What is agency?** 

In our view, agency is a person’s capability to navigate toward the future they want. But agency has no single fixed definition, since it’s shaped by who’s defining it and what problems they’re trying to solve. 

Two canonical theories offer useful starting points. In psychology, Albert Bandura’s [Social Cognitive Theory](https://pubmed.ncbi.nlm.nih.gov/11148297/) breaks agency into four internal processes: *intentionality* (making and committing to plans), *forethought* (setting goals and anticipating consequences), *self-reactiveness* (monitoring progress and adjusting course), and *self-reflectiveness* (reflecting on experience to update beliefs and future goals). This turns “agency” into something researchers can actually observe – for instance, whether students developing business ideas with an AI mentor set clear goals, weigh tradeoffs, revise plans, and reflect on feedback.

In economics and development, Amartya Sen’s [capability approach](https://ophi.org.uk/publication/WP-09) instead asks whether people have the freedom and capability to exercise agency. Can they pursue the goals they value (across domains like healthcare, mobility, income, and education), given the social constraints (like local norms, institutions, or family expectations) that shape their choices? Sen’s framework distinguishes ability from autonomy: someone may use a digital tool while still lacking agency (e.g., if they are acting under pressure or cannot translate usage into meaningful outcomes in their lives; see also [this paper](https://link.springer.com/article/10.1007/s11023-024-09665-1)).

For digital and AI tools specifically, [Jigsaw’s ethnographic research](https://medium.com/jigsaw/a-new-perspective-on-human-agency-for-the-ai-era-cd785faab026) with early AI adopters identified five dimensions of agency that AI can strengthen or weaken: *instrumental* (ability to get things done), *cognitive* (the ability to shape thinking), *affective* (the ability to navigate feelings), *social* (the ability to nurture connections), and *structural* (the ability to influence the systems governing their lives). 

Depending on a program’s goals, each of these frameworks offer useful dimensions of agency to measure.

## 

## **How is agency measured?**

Measuring agency is at least as hard as defining it. It’s *latent* (inferred from evidence, not observed directly), *multidimensional* (rarely captured by a single metric), *culturally situated* (what’s “agentic” varies by setting), and *context-specific* (e.g., measuring student-AI use differs from measuring farmer-AI use). Given these challenges, we suggest three broad steps.

**Step 1: Define agency for your local problem**

Define what agency means within your program’s theory of change. What kind of agency is the tool supposed to support? For whom? To what end? It helps to distinguish between two related **forms of agency**:

* **Agency with respect to the end goals:** Can users make progress toward outcomes they value, such as health, education, and livelihoods, whether through, around, or beyond the tool?  
* **Agency with respect to the digital tool:** Can users understand, question, adapt, control, and use the tool effectively in pursuit of their goals, including deciding when and how to rely on it?

Likewise, it’s worth distinguishing **how agency manifests**:

* **Internally experienced agency** as people’s thoughts and feelings  
* **Externally expressed agency** as people’s choices and actions

Use these distinctions to move from a broad idea of agency to a structured definition that fits your context, your problem, and the outcomes you’re trying to influence. Frameworks, like those highlighted above or others, can help make your definition more precise and theory-informed. 

**Step 2: Measure with the right tools, on the right data, at the right moment**

The next step is choosing *how* to measure agency. Measurement data can be collected *on-platform* (via in-app surveys, chatbot interactions, task behavior, or other digital traces) or *off-platform* (via phone/in-person surveys, interviews, observations, administrative records, or other sources). See the table below for hypothetical examples.

Self-report surveys are the most common tool, useful because agency partly depends on [how people interpret their own capabilities and make meaning](https://books.google.com/books?hl=zh-CN&lr=&id=YHt_M41uIuUC&oi=fnd&pg=PR9&dq=Acts+of+Meaning&ots=YMMtzyOKVc&sig=5aTrmWAl1QT0zAxyA6hsjD1sv6E). Existing instruments [range widely](https://link.springer.com/article/10.1007/s11205-021-02791-8), from multidimensional to narrower measures of agency (e.g., political, moral, sexual, or educational). In low- and middle-income countries, measurement often focuses on groups facing structural constraints, especially women and girls – as with the World Bank’s [MAGNET](https://blogs.worldbank.org/en/opendata/measuring-agency-what-we-know-and-where-we-go-here) group or the [Girls’ Agency Lab](https://girlsagencylab.com/). 

Note that self-reports carry real limits. They’re prone to [measurement bias](https://pmc.ncbi.nlm.nih.gov/articles/PMC5639921/), such as respondents giving answers they think are more socially acceptable. Surveys completed on-platform are typically short and can suffer from [low response rates](https://www.sciencedirect.com/science/article/pii/S2451958822000409). And their usefulness often depends on choosing measures that fit the context and are collected at the right moment.

Other forms of measurement can strengthen self-reports. Off-platform, direct observation or administrative records can be useful – for instance, teachers observing how students reason, revise their thinking, or make learning plans after getting AI advice, then connecting that to performance outcomes. On-platform, digital traces (behavioral data that is less prone to bias or survey dropout) can reveal what surveys miss, especially when linked to users’ goals. [Kizilcec and colleagues](https://rene.kizilcec.com/wp-content/uploads/2016/11/kizilcec2017srl.pdf), for example, combined survey and platform-log data from nearly 5,000 online-course students to assess how they set and navigated learning goals.

AI-based tools are opening further opportunities. [ThoughtTrace](https://arxiv.org/abs/2605.20087) links human-AI conversations to user’s reported reactions, helping infer agency behind what they say to chatbots. Open-source toolkits like Google’s [Langextract](https://developers.googleblog.com/introducing-langextract-a-gemini-powered-information-extraction-library/) and OpenAI’s [GABRIEL](https://openai.com/index/scaling-social-science-research/) scale this up, applying plain-language measurement prompts across thousands of human-AI conversations. With rigorous validation and privacy safeguards, these tools can help capture context-specific forms of agency that conventional surveys often miss.

Here’s a hypothetical example of how a team building an AI mentor for entrepreneurship might collect on- and off-platform agency data:

| Measuring agency: data collected on- and off-platform Hypothetical example: AI mentor to help learners develop a viable business idea |  |  |
| ----- | ----- | ----- |
|  | **Agency with respect to the end goals** | **Agency with respect to the digital tool**  |
| **Internally experienced agency** | **On-platform data:** Short in-app surveys probing users’ general sense of self-efficacy or perceived control over their ultimate goal over time (e.g., How confident is the user about developing a successful business idea? How much control do they feel over reaching their ultimate goal?) **Off-platform data:** Longer phone/in-person surveys using validated agency measures that *systematically* probe users’ general sense of self-efficacy or perceived control over their ultimate goal over time. | **On-platform data:** Short in-app surveys probing whether users felt able to understand, question, or adopt an AI mentor’s advice. **Off-platform data:** Longer phone/in-person surveys using validated agency measures that systematically probe users’ trust in AI and perceived dependence versus empowerment when using a tool. |
| **Externally expressed agency** | **On-platform data:** Longitudinal user signals of agency in AI conversation logs, especially those related to setting and navigating longer-term goals or demonstrating resilience despite difficulties. **Off-platform data:** Longer phone/in-person surveys tracking how users develop their business ideas; rubric-rated observations of ideas and pitches; or classroom observation of teamwork, ideally linked to downstream outcomes like business earnings. | **On-platform data:** Digital traces (e.g., interaction patterns or conversation logs) showing whether users understand, question, or adopt an AI mentor’s advice. **Off-platform data:** Observation or interview data (e.g., usability studies) on tool usage for developing business ideas. |

**Step 3: Test and validate your measurement tools iteratively**

Before using any measure to make claims about agency, test whether it actually measures what you intend. Look for the following evidence for your measures:

* A measure is **reliable** if it produces consistent results under similar conditions. 

* It has **construct validity** if it captures agency exactly as you define it, rather than a neighboring construct like mood or satisfaction. 

* It has **content validity** if it covers the parts of agency that matter in a given context, not only the parts that are easiest to ask about. 

* It has **criterion validity** if its scores align with real-world outcomes or behaviors we have reason to trust.

For surveys, check whether your questions fit your theory of agency and behave as expected statistically ([this paper](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2018.00149/full) is a good primer on psychometrics and survey design).

For LLM-based measurement, compare the model’s ratings against a gold-standard dataset (e.g., a sample of interactions coded by trained human reviewers using a clear rubric). Be explicit about what each data source can and cannot reveal: a transcript may show a user setting goals, but not whether they follow through. That’s why LLM-based measures work best alongside other data (see our [GenAI evaluation playbook](https://eval.playbook.org.ai/)). 

Treat agency measurement as an iterative process. Agency can shift across time and settings as programs evolve, so keep refining both your understanding of it and how you measure it.

## 

## **Tools for practitioners**

If one thing is clear, it’s that defining and measuring agency is genuinely difficult and far from settled. There’s still a great deal to learn and to debate, and we don’t think the right response is to wait for consensus. We’d rather give practitioners usable starting points and learn from how they’re put to work. So alongside this blog, we’re releasing two free, self-serve tools:

* An open-source **Claude Skill** called [***ask-agency-measurement***](https://github.com/agency-fund/taf-skills/blob/main/ask-agency-measurement/ask-agency-measurement.skill) that acts as a lightweight *companion and coach* for applying this blog in practice. It carries the core ideas behind how we think about agency and agency measurement, asks targeted questions to help you clarify your measurement challenge, and uses the context you provide to develop structured agency measurement reports grounded in the concepts and decision points discussed here (see [this GitHub Repo](https://github.com/agency-fund/taf-skills/tree/main) for details about installing the skill in Claude).   
* A curated [**NotebookLM**](https://notebooklm.google.com/notebook/fc5c61b3-a3b8-462a-9ed2-9778d70f8386?authuser=1) with foundational papers and validated scales, so practitioners can interrogate and learn from the academic source material directly.

The two tools serve different purposes:

* Use the **Claude skill** when you want to brainstorm agency measurement ideas through the frameworks presented in the blog, while connecting those ideas to your own project context.  
* Use **NotebookLM** when you need more domain-specific recommendations for theories and measures, based on a curated set of sources you can explore conversationally.

We chose this self-serve approach deliberately. AI has made expert knowledge easier to reach, yet many people still pose context-free questions to general-purpose models and act on the first answers they return. These tools are intended to be a knowledgeable, on-call expert.

\[Claude skill and NotebookLM demo\]: [Demos](https://drive.google.com/open?id=1E2sB_MiZlJgRKXvmRe5Boq_7PwQj7L98&usp=drive_fs)

## **Join us**

These tools will get better with use. Tell us where they help and where they fall short: open an issue on our [**GitHub Repo**](https://github.com/agency-fund/taf-skills/issues), fill out our [**feedback form**](https://forms.gle/9SuTGVF1yaJj2sFB6), or comment directly below.

Measuring agency well is critical for deploying AI well, and no single organization can solve this challenge on its own. The Agency Fund and Google Jigsaw will keep sharing what we learn from this collaboration, and we hope to keep the conversation open with the practitioners, researchers, and communities all asking the same question: how can digital and AI tools expand human agency rather than undermine it?

*Zezhen Wu is a Behavioral Scientist at The Agency Fund*. 

*Beth Goldberg is a Senior Fellow and Lecturer at Yale University.*

*Rachel Xu is the Head of Research & Development at Google Jigsaw.*

*We are grateful to Andra Oprisan and Amalia White (Stripe Partners) for their contributions to the resources included in the NotebookLM, and Temina Madon, James Walsh, Patricia Andrews Fearon, Kelly Zhang, Robert On, Sruthi Devan, Greg Larson (The Agency Fund), Ian Beacock (Google Jigsaw), and Hamsa Bastani and Osbert Bastani (University of Pennsylvania) for their thoughtful feedback and valuable suggestions throughout the development of this blog.*