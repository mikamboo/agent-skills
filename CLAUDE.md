# Claude Instructions for Agent Skills

This is a **Claude Code skill marketplace** project with reusable AI capabilities for custom usage like business presentations and technical blog writing.

## Project Context

- **Type:** Claude Code Marketplace of reusable skills
- **Location:** `./claude/skills/` — skill definitions live here
- **Current skills:** `tech-blog-writer`, `business-presentation`
- **Scope:** Project-level enabled in `.claude/settings.json`

## Working with Skills

### Skill Structure
Each skill lives in `claude/skills/{skill-name}/` with:
- `SKILL.md` — the complete instruction set for Claude to follow (this is the "brain" of the skill)
- `assets/` — templates, examples, static content used in output
- `references/` — reference docs loaded into context during execution

### When Testing/Developing Skills
1. Always read `{skill-name}/SKILL.md` first to understand the complete workflow
2. Reference files are noted under `## Resources` in SKILL.md
3. Don't modify templates directly without understanding the placeholder system
4. Skills detect input language automatically and respond in kind

### When Adding a New Skill
1. Create `claude/skills/your-skill-name/SKILL.md` with YAML frontmatter and instructions
2. Add any assets or references to subdirectories
3. Update `claude/.claude-plugin/marketplace.json` to register the skill
4. Update the README with usage examples
5. Run `claude plugin update business-skills@kevatech-agent-skills` to reload

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Marketplace index and skill documentation |
| `.claude/settings.json` | Project-level plugin configuration |
| `claude/.claude-plugin/marketplace.json` | Marketplace manifest |
| `claude/skills/*/SKILL.md` | Skill definitions (core instructions for Claude) |

## Code Quality Standards

- Skills are language-agnostic — always detect and respect input language
- Mark AI-generated estimates with **(est.)** for transparency
- Use Chart.js (CDN) for visualizations in HTML output
- Prefer clean, maintainable prompt structure over clever tricks
- Test skills against the documented examples in README

## Helpful Commands

```bash
# View registered plugins
claude plugin list

# Update skills after changes to marketplace or skill definitions
claude plugin update business-skills@kevatech-agent-skills

# Install skills in another project
claude plugin install business-skills@kevatech-agent-skills --scope project
```

## Branch Convention

Main branch: `main`
Feature branches: `copilot/descriptor` (e.g., `copilot/add-tech-blog-writer-skill`)

---

**Last updated:** 2026-03-16
