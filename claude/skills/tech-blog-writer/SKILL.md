---
name: tech-blog-writer
description: >
  Generates a polished, publication-ready tech blog post in Markdown from user-provided topic,
  content draft, and optional reference links or file attachments. Use this skill whenever the
  user wants to write, draft, or produce a tech blog post, article, tutorial, how-to guide,
  tool comparison, or release notes — even if they only say "write a post about X" or "turn
  my notes into a blog post". Trigger also when the user provides rough notes, bullet points,
  or a messy draft and asks to clean it up into a publishable article. The skill fetches linked
  URLs and extracts curated code snippets from official docs or repositories when available.
---

# Tech Blog Writer Skill

Transforms raw user input — a topic, a content draft, and optional links or attachments — into
a complete, well-structured tech blog post written in Markdown, ready for static site generators
(Astro, Next.js, Hugo, Jekyll) or any Markdown-based CMS.

## Overview — What this skill produces

A single, self-contained **`.md` file** that:

- Contains valid YAML frontmatter (title, description, date, tags, author)
- Is structured with `##` main sections and `###` subsections
- Uses fenced code blocks with language identifiers, shell blocks, diff blocks, and inline code
- Includes a compelling introduction, well-organised body sections, and a conclusion with a
  call-to-action
- Cites all external references at the end

---

## Input Contract

| Input           | Required | Description                                                       |
|-----------------|----------|-------------------------------------------------------------------|
| `topic`         | ✅        | The subject or working title of the post                         |
| `content_draft` | ✅        | Raw notes, bullet points, or rough prose                         |
| `links`         | ✴️        | URLs to related posts, docs, GitHub repos, official references   |
| `attachments`   | ✴️        | Uploaded files (code files, markdown, PDFs, images)              |

---

## Process

Follow these three steps in order.

---

### STEP 1 — Ingest & fetch

1. Read the `topic` and `content_draft` provided by the user.
2. For each link provided:
   - Use the `web_fetch` tool to retrieve the page content.
   - If a link is **inaccessible or returns no content**, add a visible warning in your response:
     > ⚠️ Could not fetch `<url>` — skipping this reference and continuing.
   - From successfully fetched pages, extract **key curated code snippets** only (do not dump
     entire files). Prioritise: minimal reproducible examples, installation commands, config
     blocks, and API usage patterns.
3. For any uploaded attachments, read and extract relevant content in the same way.

---

### STEP 2 — Completeness check (loop if needed)

Evaluate whether the draft contains enough substance to write a quality post.

**Minimum bar to proceed:**
- At least 3 distinct technical ideas, steps, or concepts
- A clear intended audience (beginner / intermediate / advanced)
- At least one concrete example, use case, or code scenario

If the draft falls short, **ask targeted follow-up questions** before writing. Ask all missing
questions in a single message — do not spread them across multiple turns. Examples:

- *"What's the main takeaway you want readers to leave with?"*
- *"Who is the target audience — beginners or experienced developers?"*
- *"Do you have a code example or a real-world use case to anchor the post?"*
- *"Is there a specific framework, language, or tool version this applies to?"*
- *"Should this be a tutorial (step-by-step) or a conceptual deep dive?"*

Repeat this loop until the minimum bar is met. Once it is, proceed to Step 3.

---

### STEP 3 — Write the blog post

Produce the full Markdown blog post using the output structure defined below.
Write the finished Markdown to a file named:

```
[topic-slug]-post.md
```

in the current working directory (or one the user has indicated). Use kebab-case for the slug
(e.g. `getting-started-with-astro-post.md`).

After writing the file, tell the user:

- The file path
- Which static site generators or CMS platforms the frontmatter is compatible with
- Any follow-up suggestions (related topics, series ideas, SEO improvements)

---

## Output structure

```markdown
---
title: "Post Title"
description: "One-sentence summary for SEO and previews."
date: YYYY-MM-DD   # replace with today's date, e.g. 2026-03-16
tags: [tag1, tag2, tag3]
author: ""
---

## Introduction

Hook the reader in 2–3 sentences. State the problem being solved or the thing being learned.
Briefly mention what the post covers.

---

## Section title

Body content. Use `##` for main sections and `###` for subsections.

### Subsection (if needed)

...

## Code examples

Use the appropriate code block style:

- **Fenced blocks** for language-specific code:
  ```language
  // code here
  ```

- **Shell/terminal blocks** for CLI commands:
  ```bash
  npm install example-package
  ```

- **Diff blocks** for showing changes:
  ```diff
  - old line
  + new line
  ```

- **Inline code** for short references within prose: use `backticks`.

> 💡 **Tip:** Use callout blockquotes to highlight important notes or warnings.

## Conclusion

Summarise the key points. Include a call-to-action: link to docs, suggest next steps,
or invite comments.

---

*References:*
- [Link title](url)
```

---

## Code inclusion rules

- Include **key snippets only** — the minimal code needed to understand or replicate the concept.
- Prefer complete, runnable examples over fragments when the source provides them.
- Always specify the language identifier on fenced blocks (` ```js `, ` ```python `, etc.).
- If code is taken from an external source, add a comment attribution:
  ```js
  // Source: https://example.com/docs/getting-started
  ```
- Do **not** reproduce entire files or documentation pages — summarise in prose and link instead.

---

## Style guidelines

- **Tone**: Conversational but precise. Write like a knowledgeable peer, not a textbook.
- **Audience default**: Intermediate developer unless specified otherwise.
- **Headings**: Sentence case, descriptive (e.g. "Setting up the environment", not "Setup").
- **Lists**: Use bullet lists for unordered concepts; numbered lists for sequential steps only.
- **Length**: Aim for 600–1500 words of body content. Longer is fine for deep-dive tutorials.
- **Jargon**: Define acronyms on first use. Avoid unnecessary buzzwords.

---

## Quality checklist

Before finalising, verify:

- [ ] YAML frontmatter is complete (title, description, date, tags, author)
- [ ] `date` field uses `YYYY-MM-DD` format and reflects today's date
- [ ] `tags` array contains 3–6 relevant, lowercase tags
- [ ] Introduction hooks the reader and states what the post covers
- [ ] All `##` sections have meaningful, sentence-case headings
- [ ] Every code block has a language identifier
- [ ] Inline code is used for short references within prose
- [ ] At least one callout blockquote (`> 💡`) is present
- [ ] Conclusion has a clear call-to-action
- [ ] All referenced URLs appear in the *References* list at the end
- [ ] Any fetched-URL warnings are visible in the response (not hidden in the file)
- [ ] Tone is conversational but precise — no buzzword padding
- [ ] Post length is within the 600–1500 word target (or justified if longer)
- [ ] Output file is named `[topic-slug]-post.md` in kebab-case

---

## Scope

**In scope:**
- Tutorials and how-to guides
- Tool / library comparisons
- Conceptual deep dives and explainers
- Release notes and migration guides
- Architecture walkthroughs

**Out of scope:**
- Marketing copy or product announcements
- Non-technical articles
- Video scripts or presentation decks
