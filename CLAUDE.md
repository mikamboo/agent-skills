# Claude Instructions for Agent Skills

This is a **Claude Code plugin marketplace** (`smartb-skills-marketplace`) with reusable AI capabilities
for business presentations and technical blog writing.

## Project Context

- **Type:** Claude Code plugin marketplace, spec-compliant (`.claude-plugin/marketplace.json` at repo
  root, one plugin with its own `.claude-plugin/plugin.json`)
- **Plugin:** `business-skills` — lives in `plugins/business-skills/`
- **Location:** `plugins/business-skills/skills/` — skill definitions live here
- **Current skills:** `tech-blog-writer`, `business-presentation`, `interview-prep-app`
- **Scope:** Project-level enabled in `.claude/settings.json`

## Working with Skills

### Skill Structure
Each skill lives in `plugins/business-skills/skills/{skill-name}/` with:
- `SKILL.md` — the complete instruction set for Claude to follow (this is the "brain" of the skill)
- `assets/` — templates, examples, static content used in output
- `references/` — reference docs loaded into context during execution

### When Testing/Developing Skills
1. Always read `{skill-name}/SKILL.md` first to understand the complete workflow
2. Reference files are noted under `## Resources` in SKILL.md
3. Don't modify templates directly without understanding the placeholder system
4. Skills detect input language automatically and respond in kind

### When Adding a New Skill
1. Create `plugins/business-skills/skills/your-skill-name/SKILL.md` with YAML frontmatter and instructions
2. Add any assets or references to subdirectories
3. Register it in `plugins/business-skills/.claude-plugin/plugin.json`'s `skills` array
4. Bump `plugin.json`'s `version` (semver)
5. Update `README.md` and `docs/index.html` with usage examples
6. Run `claude plugin validate .` locally, then open a PR (see `CONTRIBUTING.md`) — CI runs the same
   validation and a CODEOWNERS review is required before merge
7. After merge, run `claude plugin update business-skills@smartb-skills-marketplace` to reload

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Marketplace index and skill documentation |
| `CONTRIBUTING.md` | How to add/update skills, versioning, PR workflow |
| `.claude/settings.json` | Project-level plugin configuration |
| `.claude-plugin/marketplace.json` | Marketplace manifest |
| `plugins/business-skills/.claude-plugin/plugin.json` | Plugin manifest (name, version, skills[]) |
| `plugins/business-skills/skills/*/SKILL.md` | Skill definitions (core instructions for Claude) |
| `docs/index.html` | Browsable marketplace dashboard |
| `.github/workflows/validate.yml` | CI gate running `claude plugin validate .` on PRs |
| `.github/workflows/claude-code-review.yml` | Automated Claude review on every pull request |

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

# Validate the marketplace and plugin manifests
claude plugin validate .

# Update skills after changes to the plugin or skill definitions
claude plugin update business-skills@smartb-skills-marketplace

# Install skills in another project
claude plugin install business-skills@smartb-skills-marketplace --scope project
```

## Branch & PR Convention

Main branch: `main` — no direct pushes, all changes go through a pull request that must pass the
`validate` CI check and a CODEOWNERS review (see `CONTRIBUTING.md`).
Feature branches: `copilot/descriptor` (e.g., `copilot/add-tech-blog-writer-skill`)

## Pull Request Review

Every PR is also reviewed automatically by Claude (`.github/workflows/claude-code-review.yml`, needs the `CLAUDE_CODE_OAUTH_TOKEN` repo secret). The reviewer reads this file, so keep it accurate. When reviewing, check that:
- a new skill has valid `SKILL.md` frontmatter and is registered in `plugin.json` with a version bump
- files referenced in `SKILL.md` exist under `assets/` or `references/`
- `README.md` and `docs/index.html` document the skill

---

**Last updated:** 2026-10-03
