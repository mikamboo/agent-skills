# SmartB Skills Marketplace

A company Claude Code plugin marketplace hosting reusable **Claude skills** — invoked directly from any
conversation with a slash command or natural language.

> **Site:** [mikamboo.github.io/agent-skills](https://mikamboo.github.io/agent-skills/) — a browsable
> dashboard of the marketplace, plugins, and skills below (source: [`docs/index.html`](./docs/index.html)).

---

## Quick Setup

> Run once per machine. After that, the plugin is automatically available in every new project you enable
> it in.

```bash
# 1. Clone the repo
git clone https://github.com/mikamboo/agent-skills
cd agent-skills

# 2. Register the marketplace (user-level, permanent)
claude plugin marketplace add ./

# 3. Install the plugin into your current project
claude plugin install business-skills@smartb-skills-marketplace --scope project

# 4. Verify
claude plugin list
```

To make the skills available globally across all projects (instead of per-project):

```bash
claude plugin install business-skills@smartb-skills-marketplace --scope user
```

To pick up changes after a new release:

```bash
claude plugin marketplace update
claude plugin update business-skills@smartb-skills-marketplace
```

---

## Plugins

### `business-skills`

> **Marketplace:** `smartb-skills-marketplace`
> **Source:** `./plugins/business-skills`

Business productivity skills: presentation generation, tech blog writing and interview prep.

#### `tech-blog-writer`

> **Trigger:** `/tech-blog-writer` or describe a blog post naturally

**What it does:** Turns a topic, a rough content draft, and optional reference links or
file attachments into a complete, publication-ready Markdown blog post — ready for Astro,
Next.js, Hugo, Jekyll, or any Markdown-based CMS.

**What it produces:**

| Element               | Content                                                              |
| ---------------------- | -------------------------------------------------------------------- |
| YAML frontmatter      | title, description, date, tags, author                              |
| Introduction          | 2–3 sentence hook stating the problem and what the post covers      |
| Body sections         | `##` main sections + `###` subsections, sentence-case headings      |
| Code examples         | Fenced blocks (with language id), shell blocks, diff blocks         |
| Callout blockquotes   | 💡 tips and ⚠️ warnings                                              |
| Conclusion            | Key-point summary + call-to-action                                  |
| References            | Cited URLs at the end of the post                                   |

**Process:**

1. Reads topic and content draft, fetches any provided links with `web_fetch`
2. Checks completeness — asks targeted follow-up questions if draft lacks substance
3. Writes a polished `.md` file once the minimum quality bar is met

**In-scope post types:** Tutorials · How-to guides · Tool comparisons · Conceptual deep dives
· Release notes · Migration guides · Architecture walkthroughs

**Output file:** `[topic-slug]-post.md` in the current working directory.

**Usage examples:**

```
Write a blog post about getting started with Astro. Here are my rough notes: [paste notes]
```

```
Turn my bullet points into a publishable article about React Server Components.
```

```
/tech-blog-writer — topic: "Deploying a FastAPI app to Railway", draft: [paste draft]
```

```
Write a how-to guide comparing Zod and Yup for form validation in a Next.js project.
```

---

#### `business-presentation`

> **Trigger:** `/business-presentation` or describe a business idea naturally

**What it does:** Turns any business idea description into a complete, investor-ready HTML
presentation file. Open it in a browser and print to PDF.

**What it produces:**

| Section                 | Content                                        |
| ------------------------ | ----------------------------------------------- |
| Executive Summary       | 4 KPIs + value proposition                     |
| Company & Vision        | Mission, objectives, legal form                |
| Market Opportunity      | TAM/SAM/SOM with sourced data + chart          |
| Product / Service       | Categorised offering grid                      |
| Business Model          | Revenue streams, unit economics                |
| Competitive Landscape   | Named competitors + positioning chart          |
| SWOT Analysis           | 4-quadrant colour matrix                       |
| Go-To-Market            | Target profile, channels, launch plan          |
| Roadmap                 | Phase-by-phase timeline                        |
| Financial Projections   | Investment table + revenue forecast + 2 charts |
| Risk Analysis           | Colour-coded risk table with mitigations       |
| Growth & Scalability    | Expansion vectors                              |
| Key Success Factors     | Critical execution requirements                |
| Conclusion & Next Steps | Ask + immediate action list                    |

**Charts included (Chart.js):**

| Chart                                   | Section               |
| ----------------------------------------- | ----------------------- |
| TAM / SAM / SOM horizontal bars         | Market Opportunity    |
| Competitive positioning bars            | Competitive Landscape |
| Revenue projection (3-year grouped bar) | Financial Projections |
| Investment allocation donut             | Financial Projections |

**Process:**

1. Extracts all info silently from your description
2. **Deep web research** — fetches real market data, competitors, regulations
3. Asks ≤ 2 questions only if critical info is truly missing
4. Generates a self-contained `.html` file

**Multi-language:** Detects the language of your input and produces the document in that language.

**Output file:** `[company-slug]-presentation.html` in the current working directory.

**Usage examples:**

```
I want to open a modern pastry shop in Libreville, Gabon. Budget: 8 million FCFA.
```

```
Créer une présentation pour mon projet de livraison de repas à domicile à Douala.
```

```
Generate a business plan for a solar panel installation startup in Nairobi targeting SMEs.
```

```
/business-presentation — SaaS platform for HR management in West Africa
```

**Export to PDF:**
Open the generated `.html` in Chrome or Edge → `Ctrl+P` (or `Cmd+P`) → **Save as PDF**
→ Set margins to **None** for best results.

---

#### `interview-prep-app`

> **Trigger:** `/interview-prep-app` or share a CV and a job posting and ask for interview prep

**What it does:** Turns a CV and a job posting into a tailored, single-file HTML interview-prep
app. The design is fixed (a release-pipeline sidebar, light/dark theme, mobile tab bar); only the
content changes per candidate and role.

**What it produces (8 sections):**

| Section             | Content                                                                 |
| ------------------- | ----------------------------------------------------------------------- |
| Briefing            | Dated company facts, work-streams from the posting, decoded tech stack  |
| Pitch               | 4-paragraph elevator pitch with a built-in timer                        |
| Flagship story      | One STAR story closest to the role, plus a backup story                 |
| Likely questions    | Technical and behavioral questions grouped by the posting's themes     |
| Quiz                | Self-rated flashcard-style quiz with replay of items to review          |
| Strengths           | Requirement / asset / CV proof table and one honest blind-spot card     |
| Questions to ask    | 4-6 questions tied to the role's work-streams                           |
| Proof points        | Verified recent public work (blog, GitHub, certifications)              |

**Process:**

1. Reads the CV(s) and the job posting
2. Asks two questions: format (reference / quiz / flashcards) and depth (concise / detailed)
3. Researches the company with web search, dating every figure
4. Fills `assets/template.html` and delivers the app (as an Artifact when available)

**Multi-language:** Content and interface follow the job posting's language (FR/EN).

**Output file:** `<company>-<role-slug>.html`

**Usage examples:**

```
Prépare-moi pour cet entretien chez Société Générale. Voici mon CV et l'offre : [coller]
```

```
Help me prep for this interview. Here's the job description and my resume.
```

```
Update my interview prep app: my CV changed, and translate it to English.
```

---

## Repository Structure

```
agent-skills/
├── README.md                              ← This file — marketplace index
├── CLAUDE.md                              ← Project instructions for Claude
├── CONTRIBUTING.md                        ← How to add/update skills, versioning, PR workflow
├── CODEOWNERS                             ← Required reviewers for manifest/plugin/CI changes
├── .github/
│   └── workflows/
│       ├── validate.yml                  ← CI: `claude plugin validate .` on every PR
│       └── claude-code-review.yml        ← Claude reviews every pull request
├── .claude/
│   └── settings.json                     ← Project-level enabled plugins
├── .claude-plugin/
│   └── marketplace.json                  ← Marketplace manifest (smartb-skills-marketplace)
├── plugins/
│   └── business-skills/                  ← Plugin: business productivity skills
│       ├── .claude-plugin/
│       │   └── plugin.json               ← Plugin manifest (name, version, skills[])
│       └── skills/
│           ├── business-presentation/    ← Skill: business presentation generator
│           │   ├── SKILL.md              ← Skill instructions (read by Claude)
│           │   ├── assets/
│           │   │   └── template.html    ← HTML/CSS/Chart.js presentation template
│           │   └── references/
│           │       ├── sections-guide.md      ← Section content guidelines + colour themes
│           │       └── user-info-guide.md     ← Info extraction + sector financial benchmarks
│           ├── tech-blog-writer/         ← Skill: tech blog post generator
│           │   └── SKILL.md
│           └── interview-prep-app/       ← Skill: tailored interview prep web app
│               ├── SKILL.md
│               └── assets/
│                   └── template.html    ← Fixed-design app shell (CSS + JS engine)
└── docs/
    ├── index.html                        ← Browsable marketplace dashboard
    └── examples/
        └── sido-deco-presentation.html   ← Example output
```

---

## Adding a New Skill

1. Create a directory under `plugins/business-skills/skills/your-skill-name/`
2. Add a `SKILL.md` with YAML frontmatter:

```markdown
---
name: your-skill-name
description: >
  One-sentence description. Claude uses this to decide when to trigger the skill.
  Include trigger phrases.
---

# Skill Instructions

Step-by-step instructions for Claude to follow when the skill is invoked.
```

3. Optionally add:
   - `assets/` — templates, example files, images used in output
   - `references/` — reference docs loaded into context during execution

4. Register it in the plugin manifest `plugins/business-skills/.claude-plugin/plugin.json`:

```json
{
  "name": "business-skills",
  "version": "1.2.0",
  "skills": [
    "./skills/business-presentation",
    "./skills/tech-blog-writer",
    "./skills/interview-prep-app",
    "./skills/your-skill-name"
  ]
}
```

5. Bump the plugin's `version` (semver) and update this README and `docs/index.html`.

6. Open a PR (see [`CONTRIBUTING.md`](./CONTRIBUTING.md)). Once merged, install owners pick up changes with:

```bash
claude plugin update business-skills@smartb-skills-marketplace
```

---

## Skill Development Notes

- **`SKILL.md`** is the entire brain of a skill — write it like a detailed SOP for Claude.
- Reference files in `references/` are listed at the bottom of `SKILL.md` under `## Resources`.
  Claude reads them on demand using the `Read` tool during execution.
- Keep `assets/template.html` as a clean foundation — the skill fills in `__PLACEHOLDERS__`.
- Skills are language-agnostic: detect input language and respond in kind.
- Mark AI-estimated figures with **(est.)** to maintain document credibility.
- Prefer Chart.js (CDN) for data visualisations in HTML output — no extra files needed.

---

## Example Output

[`docs/examples/sido-deco-presentation.html`](./docs/examples/sido-deco-presentation.html) — a
home-decoration business presentation generated from a brief description. Open in any browser.

---

## Marketplace Info

| Field              | Value                                                    |
| ------------------- | --------------------------------------------------------- |
| Marketplace name   | `smartb-skills-marketplace`                              |
| Manifest           | `.claude-plugin/marketplace.json`                        |
| Plugin             | `business-skills` (`plugins/business-skills`)            |
| Plugin manifest    | `plugins/business-skills/.claude-plugin/plugin.json`     |
| Scope (current)    | `project`                                                |
| Skills count       | 3                                                        |
