# Agent tests

Run each prompt and check the expected result.

## finnish-ads-copywriter
| Test | Prompt | Pass if |
|---|---|---|
| Limits | Google RSA for a Finnish bike shop | `char_count.py` prints OK |
| Long words | Headline for "lattialämmitysjärjestelmä" (underfloor heating) | No headline > 30; reads naturally |
| No keyword insertion | Search ads for Helsinki, Tampere, Turku | Separate fixed variants with correct cases, no `{KeyWord:}` |
| Formats | Offer 1299 € with 15 % off until 24.12 | Shows `1 299 €`, `15 %`, `24.12.` |
| Compliance | "Suomen halvin pikalaina" | Superlative and credit flagged; todellinen vuosikorko required |
| 30-day rule | "-50 % kaikesta" | Flags Omnibus lowest-price requirement |
| en → fi | Paste English Meta ad with a pun | Transcreated, pun replaced, note explains |
| fi → en | Paste Finnish LinkedIn ad | Literal + natural columns |
| All types | "Meta, all campaign types" | Awareness, Traffic, Engagement, Leads, App, Sales + lead form |

## finnish-content-calendar
| Test | Prompt | Pass if |
|---|---|---|
| Dates | 4 weeks from a given Monday | Every date in range, weekdays correct |
| Holidays | Period covering 6.12. | Itsenäisyyspäivä included |
| No invented data | Competitor with few reviews | Says data is thin, no fake percentages |
| Ad Library | Competitor with active FI ads | Meta Ad Library table filled |
| Bilingual | Any calendar | Hook/Caption/CTA have fi + en columns |
