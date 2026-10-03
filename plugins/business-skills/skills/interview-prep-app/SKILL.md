---
name: interview-prep-app
description: >
  Use this skill whenever the user wants to prepare for a job interview and can supply (or reference) a CV/resume and a job posting or job description, even informally, like "prépare-moi pour cet entretien", "aide-moi à préparer mon entretien chez X", "help me prep for this interview", "here's the JD and my CV". Builds a single self-contained HTML web app tailored to that specific candidate and that specific role, using a fixed, proven design system (pipeline sidebar, 8 sections, interactive self-quiz): company briefing, elevator pitch with timer, one flagship STAR story, likely technical and behavioral questions, strengths-mapping table with an honest blind spot, questions to ask, and verified recent proof points. Also use it to regenerate, translate or update an existing prep app when the CV or posting changes. Works for any profile, with extra defaults for technical, platform, DevOps, AI and engineering roles. Trigger proactively even if the user only pastes a job posting next to an uploaded CV without saying "interview": that combination is the intent signal.
---

# Interview Prep App

Turns a CV + a job posting into a tailored, single-file interview-prep web app. Content is grounded in what this candidate actually did and what this role actually asks for. The **design and structure are fixed** (see section 5) so every app looks and behaves the same; only the content changes.

Bundled files:
- `assets/template.html`: the shell. Full CSS, tab/theme/timer/quiz engine, FR/EN interface strings, one commented example of every component. Always start from it.

## 0. Gather inputs

Required: a CV and a job posting (pasted, uploaded, or a URL to `web_fetch`). If either is missing, ask; never invent one.

- CVs may live in **project files** (`/mnt/project/`) as well as uploads. If the user says "I updated my resumes", re-read them from disk with `pdftotext -layout`; the copy in context may be stale.
- If the user keeps several CV variants (e.g. a DevOps CV and an AI Engineer CV), pick the one whose positioning matches the role, use the other only to complete facts, and say which one you used in one line.
- Read every CV fully before anything else.

## 1. Plan and confirm before building

Unless already specified, ask exactly two single-select questions with `ask_user_input_v0`, preceded by one line stating which CV you will use:

```
Q1: Format: Référence simple / Référence + quiz interactif / Référence + flashcards
Q2: Profondeur: Concises (points clés) / Détaillées (réponses prêtes à réciter)
```

Ask nothing else. For a regeneration or translation request on an existing app, skip this step and reuse the previous answers.

## 2. Research the company and the role's real context

Run 2-5 targeted searches; never rely on memory for time-sensitive facts:
- Latest results or key figures (date every number, e.g. "at end of June 2026"). If the posting quotes an older figure, note the discrepancy in the sources line.
- The company's distinctive operating model and anything the posting names that has a current-events dimension (an in-house platform, a modernisation programme, a vendor ecosystem, a recent deal).
- Recent sensitive news (legal, regulatory, layoffs). If found, include it as an amber "context to know, not to raise" note with a one-line way to handle it if asked. Never make it the headline.

Also `web_fetch` the candidate's linked profiles (blog, GitHub, Credly) to find recent, verifiable proof points. A link can only be fetched if it appears in the conversation or documents.

Paraphrase everything. Follow copyright rules.

## 3. Extract from the CV (accuracy rules learned the hard way)

- **Certifications: list only those printed on the CV, with their exact dates.** Never add a certification from memory or a past conversation. If a validity end date is in the past, mark it as lapsed and tell the candidate to present it as "held", not "current".
- Dates of the latest role: if variants disagree, flag it; if the role has ended, add a note asking the candidate to prepare one neutral sentence on availability.
- **One flagship experience** = the past role or project closest to the *core problem* of the posting (not the most recent). It must be a production system the candidate built or ran. Pick a second one as "backup story" for the sector (e.g. finance).
- Results not quantified on the CV: never invent numbers. Write the qualitative result, then a `.todo` highlight listing exactly what to quantify.
- Real gaps vs the posting: name them. One becomes the blind-spot card.
- Flag anything verified online but missing from the CV (e.g. a newly passed certification) so the candidate can add it.

## 4. Build the content: 8 sections, in this order

| # | id | Nav label EN / FR | Content rules |
|---|---|---|---|
| 1 | `brief` | Briefing | Headline = a claim about what makes the company distinctive for *this role* (e.g. "A bank that runs its own platform"). Facts grid (3-5 dated figures) + sources line. Business paragraph + bullets. One green "what this means for the interview" note. Team paragraph + work-streams list mirroring the posting's missions (3-6). "Tech stack, decoded": every named tool, what it is, why it's there, what to ask. Optional amber sensitive-context note. |
| 2 | `pitch` | Pitch | 4 paragraphs: who I am / most recent role / flagship proof / why here, why now. 35-50 s spoken. Timer below. Then a short "if the interview switches language" paragraph and an amber note for anything to adapt (availability, date discrepancy). |
| 3 | `star` | Flagship story / Expérience clé | Headline = project name. Lede says why it's the closest match. S/T/A/R grid (Action as bullets). "Bridge to {company}" paragraph naming the company's own tools. "Backup story" paragraph. |
| 4 | `qs` | Likely questions / Questions | Themes = the posting's requirement groups (green theme labels). Each question is a `<details>` with 2-4 bullets. Concise depth = "points to raise, not answers to memorise". Include behavioral questions and the predictable "why this role given your profile" question. |
| 5 | `quiz` | Quiz | 10-15 items drawn from section 4, biased toward judgement and architecture. Show question, reveal key points, self-rate, running score, replay "to review" only. |
| 6 | `map` | Strengths / Atouts | Table: requirement / asset with Strong or Partial pill / CV proof. Strong rows first. Proof cites CV entries only. Then exactly one blind-spot card: why it will be probed, a one-sentence admission + transposition script, and homework. |
| 7 | `ask` | Questions to ask / Questions à poser | 4-6 questions, each tied to a work-stream with a `.why` line. One may honestly cover a partial match. |
| 8 | `proof` | Proof points / Faits d'armes | Lede states when the items were verified. Each item: title, one line on why it matters for this role, link only if verified. Unverified items say so. End with a green note on which proofs to lead with for this role. |

Flashcard format (Q1 option 3): keep the same quiz engine; it already works as reveal-and-rate flashcards. Reference-only format: remove the quiz section and its nav item, and renumber the dots.

## 5. Design system (fixed, do not redesign)

Copy `assets/template.html` to `/mnt/user-data/outputs/<company>-<role-slug>.html` and fill it. Do **not** change the `<style>` block or the script engine. Only replace `{{PLACEHOLDERS}}`, duplicate the commented component blocks as needed, fill `QUIZ`, and set `UI_LANG`. Reading `frontend-design` is not needed: the design decisions below are already made and approved by the user.

What the template encodes, so you can apply it faithfully:
- **Concept**: the 8 sections are stages in a release pipeline. The left rail draws a vertical line with numbered dots; the active stage is filled ink, and visited stages turn green, "like a change promoted to prod". This is the one memorable element; everything else stays quiet.
- **Palette** (light / dark tokens on `:root`): paper `#F2F4F3`, surface `#FFFFFF`, ink `#10263A`, muted `#566673`, rule `#D3DADE`, go green `#1E6B52` (+ soft `#E2F0EA`), risk amber `#A86A12` (+ soft `#F7ECD9`), focus `#2F5FD0`. Green = strengths and "what it means". Amber = gaps, warnings, todos. Nothing else gets color.
- **Type**: Source Serif 4 for headlines, figures, pitch and quiz question; Instrument Sans for everything else. Sentence case only, no all-caps labels, no single-word accents in headlines.
- **Layout**: 280 px sticky rail + content column max 900 px, line length under 70ch. Below 860 px the rail becomes a sticky horizontal scrolling tab bar.
- **Components**: facts grid, auto-numbered work-streams, green / amber notes, serif pitch block with timer, S/T/A/R grid, `<details>` accordions under green theme labels, quiz card with progress bar and score, scrollable table with Strong / Partial pills, amber-bordered blind-spot card, proof list.
- **Behavior**: one section visible at a time (app, not article); theme toggle in memory; quiz state in JS variables only, never browser storage; respects reduced motion; safe-area padding for phones.
- **Interface language**: set `UI_LANG` to `"fr"` or `"en"`. All buttons, nav labels and quiz strings switch automatically. Write the content in the same language.

Before publishing:
1. `grep -o '{{[A-Z_]*}}' file.html` returns nothing.
2. Syntax-check the engine: extract the content after the last `<script>` and run `node --check`.
3. Remove unused optional blocks (sensitive note, flashcards) rather than leaving them empty.

## 6. Deliver

If the `Artifact` tool is available, publish the HTML with it (favicon: one emoji matching the company's sector, kept stable across republishes). For a later regeneration, translation or CV update, republish **to the same artifact** by passing its `url`, so the user keeps one link. Without the Artifact tool, `present_files` the HTML.

In the chat reply, keep it short: what the app contains, the 2-4 choices that matter (flagship story, blind spot, CV variant used), and what the candidate must do before the interview (quantify results, verify dates, add missing certifications). Cite researched facts.

## 7. Tech, platform, DevOps and AI role defaults

- Name the exact platform, product or vendor ecosystem the posting references, and decode every tool in the stack.
- In the strengths table, map cloud, Kubernetes, observability and security certifications against infra-shaped requirements even when the posting uses other words.
- When the role is process-heavy (release management, CAB, ITIL, ITSM) and the candidate is build-heavy, that mismatch is the blind spot: script the honest admission plus the GitOps or traceability transposition.
- When the candidate's profile leans AI but the role does not, put AI in second place everywhere and prepare the "why this role" answer.

## 8. Language and honesty

Default to the job posting's language. If the posting is bilingual, follow the user's request language, and add a note that the interview may switch. When the user asks for another language, translate everything, including `UI_LANG`. Never fabricate company facts, certifications, outcomes or links. When something can't be verified, say so in the app.
