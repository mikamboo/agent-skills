"""Fail if any SKILL.md description is missing or exceeds the 1024-character limit."""
import glob
import sys

import yaml

LIMIT = 1024
failed = False

for path in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
    text = open(path, encoding="utf-8").read()
    parts = text.split("---", 2)
    frontmatter = yaml.safe_load(parts[1]) if len(parts) == 3 else None
    description = (frontmatter or {}).get("description")
    if not description:
        print(f"FAIL {path}: missing description")
        failed = True
        continue
    length = len(" ".join(str(description).split()))
    status = "FAIL" if length > LIMIT else "ok  "
    print(f"{status} {path}: {length}/{LIMIT}")
    failed = failed or length > LIMIT

sys.exit(1 if failed else 0)
