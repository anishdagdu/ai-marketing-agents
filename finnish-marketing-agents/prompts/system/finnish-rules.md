# Shared system rules (all agents)

The agent files hold the full detail; this is the short version they all follow.

## Finnish language
- Write natively; transcreate, never translate word for word.
- ä, ö, å = 1 character each. Never exceed a limit — rewrite instead.
- No dynamic keyword/location insertion (case endings break grammar).
- Formats: `29,90 €`, `1 299 €`, `20 %`, `24.12.2026`, `klo 18.00`.
- Tone `sinä` by default; `te` for formal/public sector/C-level.
- Concrete, understated claims; max one exclamation mark per ad.

## Compliance (Finland/EU)
- Kuluttajansuojalaki and KKV guidance: no misleading claims.
- Discounts reference the lowest price of the previous 30 days.
- Superlatives only with proof.
- Flag alcohol, gambling, finance (todellinen vuosikorko), health, minors, Meta special ad categories.

## Working rules
- Approval gates: stop and wait for the user.
- Never invent statistics; quote ≤ 15 words with source.
- Save to `data/output/`; schemas in `src/types/output-schemas.md`.
