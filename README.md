# Measuring Agency in AI Products: Nairobi Onsite

Talk + hands-on coding workshop (~65 min) for Agency Fund grantees, funders, and staff.
Participants code synthetic AI-assistant conversations for agency signals in Calibrate,
then compare their labels against each other and against an LLM judge running the
same rubric.

## Contents

| Path | What |
|------|------|
| `index.html` + `slides/` | 14-slide HTML deck (TAF web design system). Double-click `index.html`; arrow keys to present; works offline. |
| `agency-measurement-deck.pdf` | Vector PDF export of the deck (backup / sharing). |
| `workshop-data/generate_conversations.py` | Source of truth for the 18 synthetic conversations and the coding rubric. Edit here, re-run to regenerate. |
| `workshop-data/education_ai_mentor.csv` | 6 conversations, AI educational mentor (upload to Calibrate as annotation task 1). |
| `workshop-data/health_ai_assistant.csv` | 6 conversations, AI health assistant (task 2). |
| `workshop-data/agriculture_ai_advisor.csv` | 6 conversations, AI agricultural advisor (task 3). |
| `workshop-data/ANSWER_KEY.md` | Facilitator-only: intended labels, exact evaluator wording for Calibrate, debrief notes. Do not upload or distribute. |
| `workshop-materials/qr-cards-template.html` | Print sheet for labeller-link QR cards. Paste real Calibrate links into the `LINKS` object, open in a browser, print, cut. |
| `workshop-materials/facilitation-crib.html` | One-page run of show, Calibrate setup checklist, contingencies, debrief ammunition. Print it. |
| `docs/` | Reference papers, including Chong, Yu, Keeling & de Ruyter (2021, JRCS), the source for the modes-of-agency coding question. |

## Deck outline

1. Cover
2. The agency flywheel (the Agency Fund's foundation; AI marked as a touchpoint at every station of the loop)
3. AI expanding personal, proxy, and collective agency (three synthetic mini-conversations)
4. AI undermining the same three modes (three more; every one looks fine on an engagement dashboard)
5. What agency is: Bandura's four observable processes and Sen's capability approach, with blog examples and links
6. The blog's 2x2 (agency w.r.t. end goals vs. the tool x internally experienced vs. externally expressed), with the blog's on/off-platform examples
7. The four-level evaluation framework, wording verbatim from eval.playbook.org.ai; agency measurement sits at Level 3
8. The blog's three steps: define locally, measure with the right tools on the right data at the right moment, validate iteratively
9. Scope caveat: transcript coding is one way in, suited to conversational products, not the whole toolbox
10. Part 2 divider
11. Workshop launch (domain card piles, QR labeller links, individual coding then table adjudication)
12. The coding rubric (stays projected during coding)
13. Debrief: live Calibrate agreement view, LLM judge comparison, the scaling argument
14. Close: agency measurement is interesting, necessary, and complex; start anyway (blog, Claude skill, NotebookLM, eval playbook)

## The coding rubric

Grounded in Bandura's agentic processes as presented in the TAF x Jigsaw blog, plus
Bandura's three modes of agency as applied to AI chatbots by Chong et al. (2021):

1. **Goals and plans** (intentionality + forethought)
2. **Acting and adjusting** (self-reactiveness)
3. **Reflecting** (self-reflectiveness; negative self-assessments count)
4. **Who is the author?** (personal / proxy / collective: deliberate delegation vs. handing decisions over)
5. Open note, including undermining signs and which mode of agency appears

Answers are Yes / No / Mixed with optional reasoning. Exact wording in `ANSWER_KEY.md`.

## The signal matrix behind the conversations

Each domain has the same six planted profiles (intended labels in `ANSWER_KEY.md`):

1. High agency, returning user (anchor)
2. Delighted dependence (the proxy dilemma; satisfaction without reflection)
3. Ambiguous flagship (built for disagreement)
4. Passive compliance (anchor, with a crisis caveat worth debating)
5. Strong own goal, method handed to the tool
6. Critical engagement under discouragement or structural strain

## Regenerating or editing

```bash
cd workshop-data && python3 generate_conversations.py   # rewrites CSVs + answer key
node shoot.mjs slides _verify                            # re-screenshot slides
node export_deck_pdf.mjs --slides slides --out agency-measurement-deck.pdf
```
