# Architecture

```
User brief
   │
   ▼
finnish-marketing-orchestrator ── routes single requests directly
   │
   ├─► finnish-content-calendar
   │     1 Research: website · competitor sentiment · Meta Ad Library   [Gate 1]
   │     2 Strategy: pillars · organic vs paid                           [Gate 2]
   │     3 Calendar (fi + en) + ads-briefs.md                            [Gate 3]
   │
   ├─► finnish-ads-copywriter (parallel per platform)
   │     4 Google · Meta · LinkedIn · Snapchat ad copy
   │     5 Translation fi⇄en + QA (char_count.py, compliance)
   │
   ▼
6 You approve                                                          [Gate 4]
7 Measure → new briefs (monthly loop)
```

- Agents are defined in `src/agents/` and linked into `.claude/agents/`.
- Shared rules: `prompts/system/finnish-rules.md`. Schemas: `src/types/output-schemas.md`.
- Agents pass file paths to each other, not pasted text.
- Nothing is published automatically.
