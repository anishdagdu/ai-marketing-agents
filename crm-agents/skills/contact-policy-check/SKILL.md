---
name: contact-policy-check
description: Checks a planned send list against frequency caps, quiet hours and channel priority, and resolves competing messages by predicted uplift. Use after the RG check and before any send.
---

# Contact policy check

## Input
A send list: `player_id, message_id, kind (promo|care|service), channel, planned_time, predicted_uplift`, plus each player's promotions sent in the last 7 days.

## Steps
1. Drop any promotion for a player with an RG flag. This is a safety net: `rg-risk-check` should already have removed it.
2. Care and service messages always stay and don't count towards the cap.
3. For each player, count promotions sent in the last 7 days. Room left = 3 − that count (minimum 0), and at most 1 a day.
4. If a player has more planned promotions than room, keep those with the highest `predicted_uplift` and drop the rest with reason `cap`.
5. Push and SMS planned between 21:00 and 08:00 move to 08:00 local time (reason `quiet_hours`).
6. If two kept messages share a window, use the higher-priority channel: in-app → push → email → SMS.

## Output
- `final_sends.csv`
- `dropped.csv` with a reason for each row: `cap`, `rg`, `quiet_hours`, or `lower_uplift`
- One summary line, for example: "1,240 planned → 1,050 kept, 150 dropped for cap, 40 moved for quiet hours"
