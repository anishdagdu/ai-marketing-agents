---
name: ugc-campaign
description: Runs the full AI UGC ad pipeline with the agent team - brief -> plan -> prompts -> compliance -> Higgsfield image and video. Use when the user says "make UGC ads", "run a UGC campaign", or "/ugc-campaign <brief>".
---

# UGC Campaign - orchestrator

You (the main session) coordinate four agents. Subagents can't call each other or ask the user questions, so you pass files between them and handle every approval.

## Steps

1. **Brief.** Get product, product URL, audience, platform, niche, number of ads (default 5). Pick a campaign slug, e.g. `glow-serum-oct`.
2. **Plan.** Agent `ugc-director` with the brief and slug -> `output/<slug>/plan.md`. Show the user the ad matrix table and ask if they want changes. Loop until approved.
3. **Prompts.** Agent `prompt-engineer` -> `output/<slug>/prompts.md`.
4. **Compliance.** Agent `ad-compliance-checker` -> `output/<slug>/compliance.md`.
   - If `NEEDS FIXES`: send the FIX items back to `prompt-engineer` (and to `ugc-director` if a script must change), then re-check. Max 2 rounds, then show the user what is left.
   - BLOCK items are dropped unless the user rewrites them.
5. **Stop here if the user only wants prompts.** Tell them the prompts are ready to paste into Higgsfield.
6. **Generate, one ad at a time.** Check Playwright is installed (`claude mcp list`; if missing, tell the user to run `claude mcp add playwright npx @playwright/mcp@latest`). The user must be logged in to higgsfield.ai in that browser.
   For each ad:
   - Agent `higgsfield-operator`: `campaign <slug>, ad <n>, phase image`.
   - It returns `AWAITING APPROVAL ... cost ...`. Show the user the cost and screenshot, and ask. On yes, SendMessage to that same agent: `APPROVED: ad <n> image`.
   - Repeat for phase `video` (costs more than images - say so).
   - On `BLOCKED`, stop and tell the user why.
7. **Wrap up.** Summarise: ads done, credits used, files, and the reminder from compliance.md to label the ads as AI-generated when uploading.

Never approve a Generate click on the user's behalf, and never batch approvals unless the user explicitly says "approve all for this campaign up to N credits" - then keep a running total and stop at the cap.
