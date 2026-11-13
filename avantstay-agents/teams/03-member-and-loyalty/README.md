# Team 3: Member and Loyalty

![Member and Loyalty workflow](workflow.gif)

**Goal:** Grow Members Club and referrals.

**Part of the role it answers:** Rebuild "follow-up"; CAC by funnel stage

**Offerings and audience:** Members Club, referral, concierge, app, discount-code page (member)

## Agents (9)

| Agent | One-line job | Inputs / tools | Output |
|---|---|---|---|
| [`av-member-member-savings-calculator`](../../agents/av-member-member-savings-calculator.md) | Shows the real saving for a given stay under the cap and eligibility rule | Ledger, booking total | "You save $X" line per stay |
| [`av-member-checkout-upsell-tester`](../../agents/av-member-checkout-upsell-tester.md) | Designs tests of when the membership offer appears | Statsig, checkout events | Test plan and readout |
| [`av-member-repeat-guest-prospector`](../../agents/av-member-repeat-guest-prospector.md) | Scores past guests by likelihood of a second stay | BQ booking history | Ranked audience for member ads |
| [`av-member-referral-loop-agent`](../../agents/av-member-referral-loop-agent.md) | Triggers the referral ask after check-out and tracks credits | Segment, referral data | Sequence draft and credit liability report |
| [`av-member-renewal-and-churn-agent`](../../agents/av-member-renewal-and-churn-agent.md) | Flags members unlikely to renew and proposes a save offer | Membership billing data | Save list and message drafts |
| [`av-member-coupon-intent-agent`](../../agents/av-member-coupon-intent-agent.md) | Keeps the discount-code page and its ads accurate | Ledger, search terms | Page copy and ad drafts |
| [`av-member-concierge-upsell-agent`](../../agents/av-member-concierge-upsell-agent.md) | Proposes add-ons by property and party type | Upgrade catalogue, booking data | Pre-arrival offer sequences |
| [`av-member-app-adoption-agent`](../../agents/av-member-app-adoption-agent.md) | Moves booked guests into the app before arrival | App events, Segment | Install prompts and adoption report |
| [`av-member-affirm-and-protection-agent`](../../agents/av-member-affirm-and-protection-agent.md) | Tests where pay-later and Allianz cover appear in the funnel | Checkout events | Placement tests and attach-rate report |



[Back to all teams](../../README.md)
