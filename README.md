# AI Starter

Works with any AI: Claude, ChatGPT, Gemini, Perplexity, DeepSeek, Codex, Pi, Hermes — one assistant or several.

AI Starter onboards a business onto AI without a consultant on the phone. You answer a few written questions. At the end your assistant knows your company, you hold a written audit of the tasks that eat your week, and one skill handles the task you would pay the most to be rid of.

Made by [Plus de Fun Agency](https://plusdefun.ch), Geneva. Version française : [README.fr.md](README.fr.md).

## What it does

Seven steps, each one resumable. Stop whenever you like and come back.

| Step | What happens | What you give |
|---|---|---|
| 0 | Welcome, and consent for what will be read | a yes |
| 1 | Connect your tools (mail, calendar, documents, chat) | which ones you use |
| 2 | Interview | seven short written answers |
| 3 | Context files so your assistant knows your business and writes like you | permission to read ten sent emails, or three sentences typed on the spot |
| 4 | Process scan: sent mail and calendar sampled, recurring tasks found and scored | permission for the sample, or 20 sent emails pasted in |
| 5 | First skill: the task written down, trimmed, turned into a skill, tested on one real example; a second AI may check it | one real example and its output |
| 6 | Ledger: everything built, where it lives, how to run it | nothing |

## What it never does

It never sends an email or a message, never pays, never deletes. It drafts; you send. Nothing it reads leaves your own AI account, and Plus de Fun sees none of your data. Passwords, keys and bank details are dropped if they show up in what you paste.

## Install

### Claude Code (plugin)

```
/plugin marketplace add GoldenSis/ai-starter
/plugin install ai-starter@plusdefun
```

Then `/ai-starter:start` in the folder where the files should live. `/ai-starter:status` shows where you are, `/ai-starter:check` checks a skill, `/ai-starter:start 5` re-runs a step, `/ai-starter:start reset` starts over without deleting what was built. In Claude Cowork or the desktop app, add the plugin from the same repository through Settings, Plugins.

### Codex, Pi, Hermes, and any agent that reads SKILL.md skills

```
git clone https://github.com/GoldenSis/ai-starter
sh ai-starter/install.sh --dry-run   # see what it would do
sh ai-starter/install.sh
```

The script finds the agents on your machine and copies the four skills into each one's skills folder (`--link` symlinks instead, `--uninstall` removes them). It never replaces a different skill with the same name unless you add `--force`.

| Tool | Skills folder | Source |
|---|---|---|
| Claude Code | `~/.claude/skills` | Claude Code docs, Skills |
| Codex | `~/.agents/skills` | OpenAI Codex docs, Skills |
| Pi | `~/.agents/skills` (also reads `~/.pi/agent/skills`) | Pi docs, `skills.md` |
| Hermes | `~/.hermes/skills` | Hermes docs, Skills |

Codex and Pi share `~/.agents/skills`, so the script writes one copy there; a second copy in `~/.pi/agent/skills` would make Pi warn about duplicate names. Codex's older `~/.codex/skills` folder no longer appears in its docs for personal skills, so the script leaves it alone.

No slash commands outside Claude Code: say **start AI Starter**, **AI Starter status**, **AI Starter step 5** or **check my skills**.

**Windows:** copy the four folders in `skills\` into `%USERPROFILE%\.claude\skills`, `%USERPROFILE%\.agents\skills` or `%USERPROFILE%\.hermes\skills`, whichever your agent uses.

### ChatGPT, Gemini, Perplexity, DeepSeek and other chat AIs

The whole playbook is one file: [`kit/AI-STARTER.md`](kit/AI-STARTER.md). The prompt to paste is in [`kit/START-PROMPT.md`](kit/START-PROMPT.md).

- **ChatGPT:** create a Project (or a custom GPT), paste the start prompt into its instructions, and add `AI-STARTER.md` to its files.
- **Gemini:** create a Gem the same way, with the file under Knowledge. Google says Gems on personal accounts become skills from November 2026.
- **Perplexity:** create a Space the same way.
- **DeepSeek, Mistral Le Chat, claude.ai or any other chat:** paste the start prompt and attach the file.

If the assistant cannot read your mailbox, the process scan asks you to paste about 20 recent sent emails and a two-week calendar export instead.

## Using several AIs

Step 5 can hand the finished skill to a second AI to find what would go wrong, and the ledger records which AI built it and which checked it. The skill itself is plain Markdown, so the same file works as a SKILL.md for an agent, as a ChatGPT project or GPT instruction, as a Gem or as a Space.

## Where the files go

```
ai-starter/
  state.json          where you are
  tools.md            what is connected
  interview.md        your answers, verbatim
  context/            company.md · brand-voice.md · preferences.md
  AGENTS.md           the short instruction file that points at them
  CLAUDE.md           one line, @AGENTS.md, so Claude Code reads the same rules
  process-audit.md    the tasks found, scored, one recommended
  skills/<task>/      audit.md · SKILL.md · test.md
  ledger.md           what was built, in plain words
```

In a chat AI, the assistant shows each file for you to save, or to add to the Project, Gem or Space.

## For maintainers

The skills in `skills/` are the only source. After editing one, run `python3 kit/build.py` to rebuild the kit and `python3 skills/ai-starter-skill-check/scripts/skill_lint.py skills/` to check them.

## Help

For a build bigger than one skill: arnaud.chretien@plusdefun.ch.

## Licence

MIT.
