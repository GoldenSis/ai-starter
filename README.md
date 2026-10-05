# AI Starter

**English** · [Français](README.fr.md)

Your AI learns your business in about 30 minutes, then takes over one repetitive task for you.
You get an AI that knows your business and writes like you, a list of the tasks it could do, and one task it already does.
For business owners and small teams. Nothing technical to know. Works with ChatGPT, Gemini, Claude and the others.

### ➜ Start here (no installation): https://plusdefun.ch/ai-starter/

## How it works in 3 steps

1. **You give one file to your AI** — ChatGPT, Gemini, Claude…
2. **It asks you simple questions** for about 30 minutes.
3. **It takes over a first repetitive task**, tested on a real example.

You can stop at any point and pick up later.

## What you get

- **Your AI knows your business and writes like you.** Your offer, your customers, your tone, your usual greetings.
- **A list of the tasks it could do for you**, ranked by the time they cost you each week.
- **One task it now does for you**, tested on a real case from your week. Quotes, follow-ups, replies to the same question: whichever you would most like to be rid of.

## What it never does

- It never sends an email or a message. It writes drafts; you send.
- It never pays and never deletes anything.
- It reads nothing without your yes. Your data stays in your own AI account; Plus de Fun sees none of it.
- Passwords and bank details are dropped if they show up.

## Prefer to do it yourself?

1. Download [`kit/AI-STARTER.md`](kit/AI-STARTER.md) (the download arrow at the top right of the file page).
2. Open your AI, attach the file and paste the start message from [`kit/START-PROMPT.md`](kit/START-PROMPT.md).
3. Answer its questions. To pick up later, write **start AI Starter**.

If your AI cannot read your mailbox, it will ask you to paste about 20 recent sent emails instead.

## Help

Made by [Plus de Fun Agency](https://plusdefun.ch), Geneva. For a bigger project: arnaud.chretien@plusdefun.ch.

Licence: MIT.

## For developers

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

### Chat AIs: projects, Gems, Spaces

The whole playbook is one file: [`kit/AI-STARTER.md`](kit/AI-STARTER.md) (French: [`kit/AI-STARTER.fr.md`](kit/AI-STARTER.fr.md)). The prompt to paste is in [`kit/START-PROMPT.md`](kit/START-PROMPT.md).

- **ChatGPT:** create a Project (or a custom GPT), paste the start prompt into its instructions, and add `AI-STARTER.md` to its files.
- **Gemini:** create a Gem the same way, with the file under Knowledge. Google says Gems on personal accounts become skills from November 2026.
- **Perplexity:** create a Space the same way.
- **DeepSeek, Mistral Le Chat, claude.ai or any other chat:** paste the start prompt and attach the file.

### The seven steps, for reference

Each step is resumable. With the owner the playbook says "routine" for a skill and "summary" for the ledger.

| Step | What happens | What the owner gives |
|---|---|---|
| 0 | Welcome, and consent for what will be read | a yes |
| 1 | Connect tools (mail, calendar, documents, chat) | which ones they use |
| 2 | Interview | seven short written answers |
| 3 | Context files: company, brand voice, preferences | ten sent emails to read, or three sentences typed on the spot |
| 4 | Process scan: recurring tasks found and scored | a sample of sent mail and calendar, or 20 emails pasted |
| 5 | First skill: written down, trimmed, built, tested on one real example; a second AI may check it | one real example and its output |
| 6 | Ledger: everything built, where it lives, how to run it | nothing |

### Using several AIs

Step 5 can hand the finished skill to a second AI to find what would go wrong, and the ledger records which AI built it and which checked it. The skill itself is plain Markdown, so the same file works as a SKILL.md for an agent, as a ChatGPT project or GPT instruction, as a Gem or as a Space.

### Where the files go

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

### For maintainers

The skills in `skills/` are the source for agents and for the English kit. The French kit is built from native French copies in `kit/fr/` (one per skill body, plus `kit/fr/templates/`); change both in the same commit. Then run `python3 kit/build.py` to rebuild the kits, `python3 kit/build.py --check` to confirm they are current, and `python3 skills/ai-starter-skill-check/scripts/skill_lint.py skills/` to check the skills.
