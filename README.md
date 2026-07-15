# Measuring Agency in AI Products: Nairobi Onsite

Talk + hands-on coding workshop (~65 min) for Agency Fund grantees, funders, and staff.
Participants code synthetic AI-assistant conversations for agency signals in Calibrate,
then compare their labels against each other and against an LLM judge running the
same rubric.

**Live deck:** <https://agency-fund.github.io/taf-nairobi-agency-measurement-slides/>
(deployed from `main` by `.github/workflows/pages.yml`)

## Contents

| Path | What |
|------|------|
| `index.html` + `slides/` | 14-slide HTML deck (TAF web design system). Double-click `index.html`; arrow keys to present; works offline. |
| `agency-measurement-deck.pdf` | Vector PDF export of the deck (backup / sharing). |
| `workshop-data/generate_conversations.py` | Source of truth for the 30 synthetic conversations and the coding rubric. Edit here, re-run to regenerate. |
| `workshop-data/education_ai_mentor.csv` | 10 conversations, AI mentor inside a school entrepreneurship programme (Calibrate annotation task 1). |
| `workshop-data/health_ai_assistant.csv` | 10 conversations, post-visit patient follow-up line of a clinic network (task 2). |
| `workshop-data/agriculture_ai_advisor.csv` | 10 conversations, FarmerChat-style advisory bot for smallholders (task 3). |
| `workshop-data/calibrate_ids.json` | UUIDs of the live Calibrate evaluators, tasks, and items (workspace: TAF Onsite Workshop on calibrate.learning.org.ai). |
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

One simple **binary** question (Yes/No) per node of the TAF agency flywheel (deck slide 2):

1. **Belief or aspiration shift** — new or changed sense of what is possible; lost hope counts too, note the direction
2. **Specific action or decision** — stated concrete plans or completed actions; "maybe" doesn't count
3. **Links action to a life outcome** — income, harvest, health, fees, said by the user themselves
4. **Uses past experience** — refers to a past success/failure and uses it; the interpretation can be wrong and still count
5. Open note, especially the loop turning backwards: discouragement, over-reliance, decisions handed to the AI

Binary on purpose: borderline cases force a choice, and the forced choices generate
the disagreement the debrief runs on. Exact wording in `ANSWER_KEY.md`.

## The signal matrix behind the conversations

Each domain has the same ten planted profiles (intended labels in `ANSWER_KEY.md`),
with engagement varied on purpose — power users through two-line drive-bys —
because real traffic is mostly casual and "No" must be a comfortable label:

1. Power user, high anchor (long)
2. Delighted dependence
3. Ambiguous flagship (built for disagreement)
4. Casual transactional (short)
5. Strong own goal, method handed to the tool
6. Critical engagement under structural strain
7. Casual user with one latent spark (short)
8. Drive-by info question (all-No is the correct answer)
9. Negative loop (narrowing beliefs still code Yes on Q1)
10. Returning user with visible follow-through

The scenarios are grounded in real deployment patterns: a school
entrepreneurship programme where the AI supplements a standard curriculum
(Udhyam-style), a clinic network's post-visit patient line (Penda-style), and
a FarmerChat-style agronomy Q&A bot. Registers are calibrated against style
analysis of small samples of real Udhyam, Noora Health, and Digital Green
message data (no real user content is reproduced): terse user turns, one-word
acknowledgments, tapped suggestion-chips, message bursts with delayed replies,
duplicate re-sent queries, and formulaic structured AI responses.

## Regenerating or editing

```bash
cd workshop-data && python3 generate_conversations.py   # rewrites CSVs + answer key
node shoot.mjs slides _verify                            # re-screenshot slides
node export_deck_pdf.mjs --slides slides --out agency-measurement-deck.pdf
```
