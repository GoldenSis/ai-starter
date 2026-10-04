---
name: ai-starter-process-scan
description: Finds the recurring manual tasks that eat a business owner's week by sampling their sent mail and calendar (with consent) and combining it with their interview answers. Produces a scored audit and recommends the first task to automate. Used by the ai-starter onboarding at step 4; also usable alone when someone asks "what should I automate first", "scan my week" or "AI Starter step 4".
---

# Process scan

Goal: a short written audit, `ai-starter/process-audit.md`, that names the three recurring tasks most worth automating and picks one to start with. Evidence over opinion: every candidate cites where it was seen.

## Consent first

Say what you will read, in one message, and wait for yes:

- the last 100 sent emails (subjects, recipients, first lines; you do not need bodies beyond that),
- the last four weeks of calendar events (titles, durations, attendees count),
- any folder they name.

If they say no to a source, skip it. If they say no to everything, build the audit from the interview alone and mark it "interview only".

## Reading

Use the connectors available in this session (Gmail, Google Calendar, Microsoft 365, Drive, or whatever step 1 confirmed). Read only what was agreed. Never send, label, archive or edit anything. Keep the raw sample out of the audit file; the audit contains counts and patterns, not the emails.

When no connector can reach the mailbox or calendar, do not stop. Offer the paste route: "Paste or attach about 20 of your recent sent emails (subject, recipient, first lines are enough) and an export of your calendar for the last two weeks." A calendar export is the `.ics` file Google Calendar or Outlook can save, or a screenshot of the week view. Tell them to remove anything they would not want read before pasting. Mark the audit "pasted sample" and use the smaller counts as they are.

What each chat assistant can reach, from its own help pages (check again if the menu has moved):

- ChatGPT: Gmail, Google Calendar and Outlook mail and calendar through Settings, Connectors. A Project holds instructions and files; a custom GPT holds instructions and knowledge files.
- Gemini: Gmail, Calendar and Drive through the Google Workspace app (Keep Activity must be on). A Gem holds instructions and files. Google says Gems on personal accounts become skills from November 2026.
- Perplexity: Gmail with Google Calendar, and Outlook.com, through Settings, Connectors; one primary calendar only. A Space holds instructions and files.
- DeepSeek: no mail or calendar connector found in its documentation, so use the paste route.
- Mistral Le Chat, claude.ai and others: not checked here. Ask the person what their assistant shows under connectors or apps; if nothing, use the paste route.

## Clustering

Group what you saw into recurring tasks. A task is recurring if it appears at least three times in the sample or once a week in the calendar. Typical clusters: replying to the same kind of request, sending the same document, chasing a payment or a signature, preparing the same report, scheduling, quoting, following up after a meeting.

For each cluster record: what the task is, how often (per week), rough minutes each time, who does it, which tool, and the evidence (for example "14 sent mails with 'devis' in the subject, 4 weeks").

## Scoring

Three columns, each 1 to 5:

- **Load**: hours per week it costs (minutes × frequency).
- **Sameness**: how similar each occurrence is. A task that is different every time scores 1.
- **Reach**: whether the assistant can do it with the connectors available and without sending anything on its own. A task that needs a tool not connected scores 1 until it is.

Rank by the product. Ties go to the task the owner named in interview question 4.

## Output

Write `ai-starter/process-audit.md` from `templates/process-audit.md` (relative to this file's folder):

1. Sources read, with counts, and what was declined.
2. Table of every cluster found (task, per week, minutes, tool, evidence).
3. Top three with scores and a two-line note each on what the skill would do and what stays with a human.
4. Recommendation: one task, one sentence why, and what the owner will need to supply for step 5 (an example input, the expected output, the rule for edge cases).

Present the top three as a table in chat and ask which to build. Do not start building here.
