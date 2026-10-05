---
name: ai-starter-first-skill
description: Turns one recurring manual task into a working skill for the owner's AI assistant, in three moves - watch how it is done today, cut the steps that add nothing, then write the skill and test it on one real example. Used by the ai-starter onboarding at step 5; also usable alone when someone says "build me a skill for X", "automate this task" or "AI Starter step 5".
---

# First skill: audit, optimise, automate

Never automate a task before it has been written down and trimmed. An automated mess is a faster mess.

With the owner, call what you build a "routine", never a skill, plugin or agent. `SKILL.md` stays the file name.

## 1 · Audit: how it is done today

Ask the owner to walk through the task in writing, step by step, as they did it the last time. Numbered steps, one action each. Ask for one real example of the input (the email, the request, the file) and the output they produced for it. If they have the connectors, offer to pull the last real example yourself and ask them to confirm it is typical.

Write the steps to `ai-starter/skills/<task-slug>/audit.md`. Count them.

## 2 · Optimise: cut what adds nothing

Go through the steps and mark each one: keep, merge, drop, or move to the assistant. A step is dropped when its output is never used. Two steps merge when the second only reformats the first. Propose the shorter list, with the count before and after, and one line per change. Ask the owner to confirm or push back. The owner decides; record the final list.

Also record the rule for the cases the routine must not handle alone: money above an amount, a complaint, a legal question, a new customer. These go to a human, and the routine says so.

## 3 · Automate: write the skill

Write `ai-starter/skills/<task-slug>/SKILL.md` from `templates/skill-template.md` (the path is relative to this file's folder). Keep it plain Markdown with the short frontmatter block on top: the same file then works as a skill for Claude, Codex, Pi or Hermes, and as instructions pasted into a chat AI, a ChatGPT project or custom GPT, a Gemini Gem or a Perplexity Space.

- frontmatter `name` and a `description` that says when to use it, in the owner's words,
- inputs (where the request arrives, what fields matter),
- the trimmed steps, each as an instruction to the assistant,
- the output format, with the owner's real example as the model,
- the hand-to-a-human rules,
- what the routine never does: it never sends, never pays, never deletes. It drafts, and the owner sends.

Run the skill check on it (the `ai-starter-skill-check` skill; its script sits next to this skill, `python3 ../ai-starter-skill-check/scripts/skill_lint.py ai-starter/skills/<task-slug>` from this folder) and fix any FAIL before going on. In a chat AI that cannot run scripts, do the checks in that skill by reading.

Then put the routine where the owner's AI will find it, and tell them the path. Ask before copying.

- Claude Code: `.claude/skills/<task-slug>/` in the project, or `~/.claude/skills/`. Cowork and the desktop app: the skills folder they use.
- Codex, Pi, and other tools that read the Agent Skills format: `.agents/skills/<task-slug>/` in the project, or `~/.agents/skills/`.
- Hermes: `~/.hermes/skills/<task-slug>/`.
- A chat AI (ChatGPT, Gemini, Perplexity, DeepSeek, Le Chat, claude.ai): paste the file into the instructions of a ChatGPT project or custom GPT, a Gemini Gem or a Perplexity Space, or attach it at the start of a chat. Give the owner the text to paste.

## 4 · Test on one real example

Run the routine on the real example from the audit. Show the output next to the owner's own output. Ask: is this right, what would you change? Fix and rerun once. Stop there; a second round belongs to tomorrow, with a second example.

Record in `ai-starter/skills/<task-slug>/test.md`: the input, the output, the owner's verdict, the date, and which AI built the routine.

## 5 · Optional: a second AI checks it

Offer this once; skip it if the owner says no. A different AI catches what the first one takes for granted. Give the owner this text to paste, with the routine file, into another AI (ChatGPT if you are Claude, Claude or Gemini if you are ChatGPT, and so on):

> Here is a routine another AI wrote for my business (instructions for one repetitive task). Do not rewrite it. List what would go wrong if you ran it on next week's real cases: a step that is unclear, a case it does not cover, anything it could send, pay or delete without me. Five points at most, most serious first.

When the owner brings the answer back, fix only what they agree with and note in `test.md` which AI checked the routine and what changed.

Then return to the onboarding for step 6, or, if run alone, print where the files are and how to run the routine.
