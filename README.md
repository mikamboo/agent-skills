# Agent Skills — Local Claude Marketplace

A personal collection of **Claude skills** — reusable AI capabilities invoked directly
from any conversation with a simple command or natural language phrase.

---

## Quick Setup

> Run once per machine. After that, skills are automatically available in every new project.

```bash
# 1. Clone the repo
git clone https://github.com/mikamboo/agent-skills
cd agent-skills

# 2. Register the local marketplace (user-level, permanent)
claude plugin marketplace add ./

# 3. Install the skill pack into your current project
claude plugin install business-skills@kevatech-agent-skills --scope project

# 4. Verify
claude plugin list
```

To make the skills available globally across all projects (instead of per-project):

```bash
claude plugin install business-skills@kevatech-agent-skills --scope user
```

---

## Available Skills

### `tech-blog-writer`

> **Plugin:** `business-skills@kevatech-agent-skills`
> **Trigger:** `/tech-blog-writer` or describe a blog post naturally

**What it does:** Turns a topic, a rough content draft, and optional reference links or
file attachments into a complete, publication-ready Markdown blog post — ready for Astro,
Next.js, Hugo, Jekyll, or any Markdown-based CMS.

**What it produces:**

| Element               | Content                                                              |
| --------------------- | -------------------------------------------------------------------- |
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

### `business-presentation`

> **Plugin:** `business-skills@kevatech-agent-skills`
> **Trigger:** `/business-presentation` or describe a business idea naturally

**What it does:** Turns any business idea description into a complete, investor-ready HTML
presentation file. Open it in a browser and print to PDF.

**What it produces:**

| Section                 | Content                                        |
| ----------------------- | ---------------------------------------------- |
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
| --------------------------------------- | --------------------- |
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

### `frontend-design`

> **Plugin:** `business-skills@kevatech-agent-skills`
> **Trigger:** `/frontend-design` or ask to build any web UI, component, or page

**What it does:** Generates production-grade, visually distinctive frontend code — HTML/CSS/JS,
React, Vue, or any web framework — with a bold, intentional aesthetic that avoids generic
AI-slop patterns.

**What it produces:**

| Element            | Content                                                              |
| ------------------ | -------------------------------------------------------------------- |
| Working code       | HTML/CSS/JS, React, Vue, or as requested                            |
| Aesthetic direction| One committed visual style: brutalist, editorial, retro-futuristic, luxury, etc. |
| Typography         | Distinctive, characterful font pairings (never Inter/Arial/Roboto)  |
| Motion & interaction | CSS animations and micro-interactions tuned to the aesthetic      |
| Visual details     | Backgrounds, textures, shadows, gradients — never default solid fills |

**Process:**

1. Understands the purpose, audience, and any technical constraints
2. Commits to a bold aesthetic direction before writing a single line
3. Implements working, production-ready code with meticulous attention to detail

**Usage examples:**

```
Build a landing page for a cybersecurity startup. Dark, technical, serious.
```

```
Create a React dashboard component for fitness tracking data. Make it feel premium.
```

```
/frontend-design — a personal portfolio page for a motion designer
```

---

### `pdf`

> **Plugin:** `business-skills@kevatech-agent-skills`
> **Trigger:** `/pdf` or any request involving a `.pdf` file

**What it does:** Handles any PDF task — reading, extracting text/tables, merging, splitting,
rotating, watermarking, form-filling, encryption, image extraction, and OCR on scanned PDFs.

**Operations supported:**

| Task                  | Description                                          |
| --------------------- | ---------------------------------------------------- |
| Read / extract        | Text, tables, images, and metadata from PDFs         |
| Merge / split         | Combine multiple PDFs or split into individual pages |
| Form fill             | Fill fillable fields or annotate non-fillable forms  |
| Transform             | Rotate pages, add watermarks, encrypt/decrypt        |
| OCR                   | Make scanned PDFs text-searchable                    |
| Create                | Generate new PDFs programmatically                   |

**Process:**

1. Identifies the operation needed from the user's description
2. Selects the appropriate Python library (`pypdf`, `reportlab`, `pdfplumber`, etc.)
3. Uses helper scripts in `skills/pdf/scripts/` for complex operations
4. Returns the result or writes the output file

**Usage examples:**

```
Extract all text from report.pdf
```

```
Merge invoice_jan.pdf, invoice_feb.pdf, and invoice_mar.pdf into one file.
```

```
Fill in the form fields in application.pdf with my data: name = John, date = 2026-05-24
```

---

### `skill-creator`

> **Plugin:** `business-skills@kevatech-agent-skills`
> **Trigger:** `/skill-creator` or ask to create, improve, or benchmark a skill

**What it does:** Guides the full lifecycle of skill development — from capturing intent and
writing a first draft, to running evaluations, iterating on results, and optimising the
skill's trigger description.

**What it supports:**

| Task                    | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| Create from scratch     | Interview user, draft SKILL.md, write test cases                |
| Improve existing skill  | Identify weaknesses, rewrite, re-evaluate                       |
| Run evals               | Execute test prompts and review qualitative + quantitative results |
| Benchmark               | Measure performance with variance analysis across multiple runs |
| Optimise description    | Improve the skill's trigger description for better activation   |

**Process:**

1. Assesses where the user is in the skill lifecycle
2. Asks targeted questions about intent, inputs, outputs, and success criteria
3. Drafts or edits the `SKILL.md`, writes test prompts, runs evaluations
4. Uses `skills/skill-creator/scripts/` for benchmarking and report generation
5. Iterates until the skill meets the quality bar

**Usage examples:**

```
I want to create a skill that summarises meeting transcripts.
```

```
My tech-blog-writer skill isn't triggering reliably — help me fix the description.
```

```
/skill-creator — run a full benchmark on the business-presentation skill
```

---

## Repository Structure

```
agent-skills/
├── README.md                              ← This file — marketplace index
├── CLAUDE.md                             ← Project instructions for Claude
├── .claude/
│   └── settings.json                     ← Project-level enabled plugins
├── .claude-plugin/                        ← Marketplace root (compliant with plugin spec)
│   └── marketplace.json                  ← Marketplace manifest (kevatech-agent-skills)
├── out/                                   ← Generated output files
└── skills/                               ← All skill definitions
    ├── business-presentation/            ← Skill: business presentation generator
    │   ├── SKILL.md                      ← Skill instructions (read by Claude)
    │   ├── assets/
    │   │   └── template.html            ← HTML/CSS/Chart.js presentation template
    │   └── references/
    │       ├── sections-guide.md        ← Section content guidelines + colour themes
    │       └── user-info-guide.md       ← Info extraction + sector financial benchmarks
    ├── tech-blog-writer/                 ← Skill: tech blog post generator
    │   └── SKILL.md
    ├── frontend-design/                  ← Skill: production-grade frontend UI generator
    │   └── SKILL.md
    ├── pdf/                              ← Skill: PDF read/write/form-fill operations
    │   ├── SKILL.md
    │   ├── reference.md
    │   ├── forms.md
    │   └── scripts/                     ← Helper Python scripts for PDF tasks
    └── skill-creator/                    ← Skill: create and iterate on new skills
        ├── SKILL.md
        ├── agents/
        ├── assets/
        ├── references/
        └── scripts/
```

---

## Adding a New Skill

1. Create a directory under `skills/your-skill-name/`
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

4. Register it in the marketplace manifest `.claude-plugin/marketplace.json`:

```json
{
  "name": "kevatech-agent-skills",
  "plugins": [
    {
      "name": "business-skills",
      "source": "./",
      "skills": [
        "./skills/business-presentation",
        "./skills/tech-blog-writer",
        "./skills/your-skill-name"
      ]
    }
  ]
}
```

5. Update this README with the new skill entry.

6. Reinstall the plugin to pick up changes:

```bash
claude plugin update business-skills@kevatech-agent-skills
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

[`out/sido-deco-presentation.html`](./skills/business-presentation/sido-deco-presentation.html) — a home-decoration business presentation
generated from a brief description. Open in any browser.

---

## Marketplace Info

| Field            | Value                                    |
| ---------------- | ---------------------------------------- |
| Marketplace name | `kevatech-agent-skills`                  |
| Plugin pack      | `business-skills`                        |
| Manifest         | `.claude-plugin/marketplace.json`        |
| Scope (current)  | `project`                                |
| Skills count     | 5                                        |
