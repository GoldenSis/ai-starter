# AI Starter

A plugin for Claude that onboards a business onto AI without a consultant on the phone. Install it, run one command, answer a few written questions, and Claude ends up knowing your company, holding a written audit of the tasks that eat your week, and running one skill that removes the one you would pay the most to be rid of.

Made by [Plus de Fun Agency](https://plusdefun.ch), Geneva.

## What it does

Seven steps, each one resumable. Stop whenever you like and come back.

| Step | What happens | What you give |
|---|---|---|
| 0 | Welcome, and consent for what will be read | a yes |
| 1 | Connect your tools (mail, calendar, documents, chat) | which ones you use |
| 2 | Interview | seven short written answers |
| 3 | Four context files so Claude knows your business and writes like you | permission to read ten sent emails, or three sentences typed on the spot |
| 4 | Process scan: sent mail and calendar sampled, recurring tasks found and scored | permission for the sample |
| 5 | First skill: the task written down, trimmed, turned into a skill, tested on one real example | one real example and its output |
| 6 | Ledger: everything built, where it lives, how to run it | nothing |

## What it never does

It never sends an email or a message, never pays, never deletes. It drafts; you send. Nothing it reads leaves your Claude account. Plus de Fun sees none of your data. Passwords, keys and bank details are dropped if they show up in what you paste.

## Install

In Claude Code:

```
/plugin marketplace add GoldenSis/ai-starter
/plugin install ai-starter@plusdefun
```

Then, in the folder where you want the files to live:

```
/ai-starter:start
```

`/ai-starter:status` shows where you are. `/ai-starter:start 5` re-runs a step. `/ai-starter:start reset` starts over without deleting what was built.

In Claude Cowork or the desktop app, add the plugin from the same repository through Settings, Plugins.

## Where the files go

Everything lands in `ai-starter/` inside your project folder:

```
ai-starter/
  state.json          where you are
  tools.md            what is connected
  interview.md        your answers, verbatim
  context/            company.md · brand-voice.md · preferences.md
  CLAUDE.md           the short instruction file that points at them
  process-audit.md    the tasks found, scored, one recommended
  skills/<task>/      audit.md · SKILL.md · test.md
  ledger.md           what was built, in plain words
```

## Languages

It answers in the language you write in, and writes the context files in that language.

## Help

For a build bigger than one skill: arnaud.chretien@plusdefun.ch.

## Licence

MIT.
