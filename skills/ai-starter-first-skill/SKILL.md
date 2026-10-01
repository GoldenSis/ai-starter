---
name: ai-starter-first-skill
description: Turns one recurring manual task into a working Claude skill with the owner, in three moves - watch how it is done today, cut the steps that add nothing, then write the skill and test it on one real example. Used by the ai-starter onboarding at step 5; also usable alone when someone says "build me a skill for X".
---

# First skill: audit, optimise, automate

Never automate a task before it has been written down and trimmed. An automated mess is a faster mess.

## 1 · Audit: how it is done today

Ask the owner to walk through the task in writing, step by step, as they did it the last time. Numbered steps, one action each. Ask for one real example of the input (the email, the request, the file) and the output they produced for it. If they have the connectors, offer to pull the last real example yourself and ask them to confirm it is typical.

Write the steps to `ai-starter/skills/<task-slug>/audit.md`. Count them.

## 2 · Optimise: cut what adds nothing

Go through the steps and mark each one: keep, merge, drop, or move to Claude. A step is dropped when its output is never used. Two steps merge when the second only reformats the first. Propose the shorter list, with the count before and after, and one line per change. Ask the owner to confirm or push back. The owner decides; record the final list.

Also record the rule for the cases the skill must not handle alone: money above an amount, a complaint, a legal question, a new customer. These go to a human, and the skill says so.

## 3 · Automate: write the skill

Write `ai-starter/skills/<task-slug>/SKILL.md` from `templates/skill-template.md`:

- frontmatter `name` and a `description` that says when to use it, in the owner's words,
- inputs (where the request arrives, what fields matter),
- the trimmed steps, each as an instruction to Claude,
- the output format, with the owner's real example as the model,
- the hand-to-a-human rules,
- what the skill never does: it never sends, never pays, never deletes. It drafts, and the owner sends.

Run the skill check on it (the `ai-starter-skill-check` skill, script `python3 <plugin>/skills/ai-starter-skill-check/scripts/skill_lint.py ai-starter/skills/<task-slug>`) and fix any FAIL before going on.

Copy the skill into the place the owner's client reads skills from (`.claude/skills/` in Claude Code; the skills folder in Cowork or the desktop app) and tell them the path. Ask before copying.

## 4 · Test on one real example

Run the skill on the real example from the audit. Show the output next to the owner's own output. Ask: is this right, what would you change? Fix and rerun once. Stop there; a second round belongs to tomorrow, with a second example.

Record in `ai-starter/skills/<task-slug>/test.md`: the input, the output, the owner's verdict, the date. Then return to the onboarding for step 6, or, if run alone, print where the files are and how to run the skill.
