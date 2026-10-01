---
name: ai-starter-skill-check
description: Checks a Claude skill, or a folder of skills, against the layout rules in Anthropic's skill best-practices guide, and proposes the fixes before changing anything. Use when someone runs /ai-starter:check, asks to check, audit, lint or review a skill, or after the first-skill step writes a new skill.
---

# Skill check

Half of the check is mechanical, so a script does it and gets the same answer every time. The other half needs judgement, and you do that part by reading the skill. Change nothing until the owner agrees.

## 1 · Run the script

```
python3 scripts/skill_lint.py <skill folder or folder of skills>
```

The script sits next to this file and needs only Python 3, nothing to install. Default target: `ai-starter/skills/` in the current folder, then `.claude/skills/`. It reports:

- **FAIL**: no `SKILL.md`, a missing or malformed `name`, a missing `description` or one over 1,024 characters, a body over 500 lines.
- **WARN**: a file Claude reaches from `SKILL.md` that runs over 100 lines with no contents list at the top; a file reached only through another file, which Claude may only skim; a Python package imported with no install line in `SKILL.md`; a reserved word in the name.

## 2 · Read for what a script cannot judge

Read `SKILL.md` and each file it links. For every step, ask: what goes wrong if Claude does this differently next time?

- **Nothing much** (drafting, summarising, choosing words): plain instructions are right. If the step is over-specified, with capital letters, "ALWAYS" or long lists of edge cases, propose cutting it. Current models do worse with older, over-prescriptive skills.
- **Something consequential** (money, deleting, sending, anything a customer sees): the step needs an exact command or a script, or a rule that hands the case to a human. Prose alone is not enough here.
- **Order matters** (check the data before building the report on it): the skill should carry a short checklist Claude copies and ticks off, and a check step that sends it back on failure ("if a figure does not match, return to step 2").

## 3 · Report, then wait

Print one table: finding, file, why it matters, proposed change. FAIL first, then WARN, then the judgement findings. Skip anything that is fine and say how many checks passed.

Ask the owner which changes to make. Make only those, rerun the script, and show the before and after counts. Never touch a skill that came from someone else's plugin; report on it and stop.

Reply in the language the person writes in.
