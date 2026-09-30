---
description: Start or resume the AI Starter onboarding (connect tools, context files, process scan, first skill, ledger)
argument-hint: "[step-number | reset]"
---

Load the `ai-starter-onboarding` skill and follow it.

Arguments: `$ARGUMENTS`

- No argument: read `ai-starter/state.json` if it exists and continue from the first step not yet completed. If it does not exist, begin at step 0.
- A step number (0 to 6): run that step, even if already completed.
- `reset`: ask once for confirmation, then delete `ai-starter/state.json` and begin at step 0. Never delete the context files, the audit or the ledger on reset.

Reply in the language the person writes in.
