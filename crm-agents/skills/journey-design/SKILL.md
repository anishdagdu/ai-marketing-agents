---
name: journey-design
description: Turns a CRM goal written in plain language into a journey spec with audience, entry and exit rules, steps, control group and success metric. Use when building or reviewing a CRM journey.
---

# Journey design

## Template
Fill in every field. If one can't be filled, say why.

```
Journey:         <name>
Goal:            <user's words>
Success metric:  <one number, e.g. digital activation within 14 days>
Audience:        <NBA + segment from outputs/scores.csv>, RG band = low only for promotions
Size:            <players>   Control: <5–10%> random, held out of every step
Entry:           <event or score change>
Exit:            goal reached | RG flag turns on | unsubscribed | 21 days passed
Steps:
  day N · channel · purpose · copy brief · gatekeepers: RG → contact policy
Tests:           <max 2 variables, from crm-test-optimiser>
Review date:     <entry + 14 days>, read with uplift-readout
Approved by:     <name, date>   (blank = draft)
```

## Good practice
- 3–4 steps at most. Each step needs a new reason to act, not the same offer again.
- Lead with value (results, digital tickets, convenience) before any jackpot hook.
- The first step goes on the channel the player already uses. Move channel later.
- Add a mermaid flowchart so the platform team can build it.

## Ready-made patterns
| Goal | Entry | Steps |
|---|---|---|
| Shop to app | Retail purchase, no app login | d1 SMS app link → d3 push digital tickets → d7 in-app "check results instantly" |
| Churn win-back | Churn risk up 0.3+ | d0 push usual game + jackpot → d3 email → d7 in-app reminder |
| New player onboarding | First deposit | d0 welcome + limits → d2 how to play their game → d7 results feature |
