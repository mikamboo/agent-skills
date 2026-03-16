# Agent Skills — Local Claude Code Marketplace

A personal collection of **Claude Code skills** — reusable AI capabilities invoked directly
from any conversation with a simple command or natural language phrase.

Skills live in [`claude/skills/`](./claude/skills/). The [`claude/`](./claude/) directory is
registered as a local Claude Code marketplace (`kevatech-agent-skills`).

---

## Quick Setup

> Run once per machine. After that, skills are automatically available in every new project.

```bash
# 1. Clone the repo
git clone https://github.com/mikamboo/agent-skills
cd agent-skills

# 2. Register the local marketplace (user-level, permanent)
claude plugin marketplace add ./claude

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

## Repository Structure

```
agent-skills/
├── README.md                              ← This file — marketplace index
├── .claude/
│   └── settings.json                     ← Project-level enabled plugins
└── claude/                               ← Marketplace root
    ├── .claude-plugin/
    │   └── marketplace.json              ← Marketplace manifest (kevatech-agent-skills)
    ├── K-BOUTIQUE.html                   ← Example output (Gabon proximity retail)
    └── skills/
        ├── business-presentation/        ← Skill: business presentation generator
        │   ├── SKILL.md                  ← Skill instructions (read by Claude)
        │   ├── assets/
        │   │   └── template.html        ← HTML/CSS/Chart.js presentation template
        │   └── references/
        │       ├── sections-guide.md    ← Section content guidelines + colour themes
        │       └── user-info-guide.md   ← Info extraction + sector financial benchmarks
        └── tech-blog-writer/            ← Skill: tech blog post generator
            └── SKILL.md                 ← Skill instructions (read by Claude)
```

---

## Adding a New Skill

1. Create a directory under `claude/skills/your-skill-name/`
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

4. Register it in the marketplace manifest `claude/.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "business-skills",
      "skills": ["./skills/business-presentation", "./skills/your-skill-name"]
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

[`claude/K-BOUTIQUE.html`](./claude/K-BOUTIQUE.html) — a proximity retail boutique project
generated for a Gabonese context (in French). Open in any browser.

---

## Marketplace Info

| Field            | Value                                    |
| ---------------- | ---------------------------------------- |
| Marketplace name | `kevatech-agent-skills`                  |
| Plugin pack      | `business-skills`                        |
| Manifest         | `claude/.claude-plugin/marketplace.json` |
| Scope (current)  | `project`                                |
| Skills count     | 2                                        |
