---
name: behavior-insights-workflow
description: Runs the behaviour analytics AI team end to end on Microsoft Clarity and Hotjar (route → capture → observe → ask why → fix and prove loop) using the ba-* agents and the JEV model router. Use when the user says "run the behaviour workflow", asks why visitors don't convert, wants a heatmap or recording review, or wants a weekly UX check.
---

# Behaviour analytics AI workflow (Microsoft Clarity · Hotjar) with JEV routing

```
          ┌───────────────────────────┐      ┌───────────────────────────┐
          │      ba-orchestrator      │ ───▶ │   ba-jev-router (JEV)     │
          │ finds the friction point  │ ◀─── │ fast · standard · deep    │
          └─────────────┬─────────────┘      └───────────────────────────┘
                        ▼
 1 CAPTURE         ba-install-privacy                      (stop here if tracking or masking is broken)
                        ▼
 2 OBSERVE (what)  ba-heatmap-analyst · ba-session-replay · ba-frustration-signals · ba-error-tracker
                        ▼
 3 ASK WHY         ba-survey-designer · ba-feedback-widget · ba-interview-recruiter
                        ▼
 4 FIX + PROVE     ba-funnel-analyst · ba-cro-reporter ──▶ you approve ──▶ back to orchestrator (weekly)
```

## Steps
0. **Route** – the orchestrator lists the tasks and asks `ba-jev-router` for a tier per task. Fast = haiku, standard = sonnet, deep = opus.
1. **Capture** – `ba-install-privacy` checks both tools record every template, respect consent and mask sensitive fields. If not, stop and fix that first.
2. **Observe** – heatmaps, recordings (Clarity Copilot summaries first), frustration signals and JS errors show *what* visitors do.
3. **Ask why** – surveys, the feedback widget and interviews show *why*. All are saved as drafts; the user switches them on.
4. **Fix and prove** – `ba-funnel-analyst` sizes the drop, `ba-cro-reporter` ranks fixes with ICE, writes test hypotheses and the weekly readout with JEV's cost summary. After a fix ships, the next weekly run checks the same metric. Schedule with the `schedule` skill if the user asks.

## JEV efficiency rules
- Start low, escalate on evidence. Split cheap counting from expensive deciding.
- Use free Clarity Copilot summaries before paid model time on replays.
- Reuse outputs from the last 7 days; batch fast checks; at most 2 deep tasks per weekly run.
- Log every decision to `outputs/jev-routing-log.csv`.

## Guardrails (apply to every agent)
- Every write in Clarity or Hotjar needs explicit approval in chat. Show the full list of changes first.
- Never turn masking off or record sensitive pages unmasked. Never collect credentials or payment data.
- Surveys, widgets, invites, Slack posts and tickets are drafts; the user publishes or sends them.
- Never edit the site, never delete recordings or responses. Name created items `AI · ` and tag them `ai-workflow`.

## Single requests
- "people aren't clicking the button" → `ba-heatmap-analyst` + `ba-frustration-signals`
- "checkout conversion dropped" → `ba-funnel-analyst` + `ba-error-tracker`
- "watch some recordings for me" → `ba-session-replay`
- "why do people leave" → `ba-survey-designer`
- "is Clarity set up right / is it GDPR-safe" → `ba-install-privacy`
- "what should we test next" → `ba-cro-reporter`
- "why is the AI bill high" → `ba-jev-router`
