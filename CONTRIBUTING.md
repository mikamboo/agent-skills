# Contributing to smartb-skills-marketplace

## Adding or changing a skill

1. Add/edit a skill directory under `plugins/business-skills/skills/your-skill-name/`, with a
   `SKILL.md` (YAML frontmatter + instructions), and optional `assets/`/`references/` subfolders.
2. Register new skills in `plugins/business-skills/.claude-plugin/plugin.json`'s `skills` array.
3. Bump `plugin.json`'s `version` (semver):
   - `patch` — wording/content fixes that don't change behavior
   - `minor` — new skill added, or backward-compatible behavior change
   - `major` — breaking change (skill removed/renamed, trigger behavior changes significantly)
4. Update `README.md` and `docs/index.html` with the new/changed skill's description, triggers, and
   usage examples — both are kept in sync by hand since the marketplace is small.
5. Keep each skill's `description` frontmatter under 1024 characters (enforced in CI).
6. Validate locally before opening a PR:
   ```bash
   claude plugin validate .
   python3 scripts/check_skill_descriptions.py
   ```

## PR workflow

This repo is managed exclusively through pull requests — no direct pushes to `main`:

1. Branch off `main` (convention: `copilot/descriptor` or `<initials>/descriptor`).
2. Make your change, run `claude plugin validate .` locally.
3. Open a PR. The `validate` GitHub Actions check must pass, and a `CODEOWNERS` reviewer must approve
   before merging.
4. After merge, anyone with the marketplace installed picks up the change via:
   ```bash
   claude plugin update business-skills@smartb-skills-marketplace
   ```

Branch protection on `main` (required PR + passing `validate` check + CODEOWNERS review) is configured
in the GitHub repo settings, not in this repo's files.
