"""JEV model router: picks the Claude model for the executive summary from how messy the
audit results are, and logs each decision to reports/jev-routing-log.csv.

Standard (Haiku) when everything passes, Medium (Sonnet) for normal weeks, Deep (Opus) when
several revenue-critical checks fail at once or results swing hard against last run.
"""
import csv
import os
from datetime import date

from agents.common import ROOT

TIERS = {"standard": "claude-haiku-5-5", "medium": "claude-sonnet-5-5", "deep": "claude-opus-5-5"}


def score(results, prev=None):
    """0-2 points each on money at stake, ambiguity, reasoning depth, blast radius, novelty."""
    fails = [r for r in results if r["status"] == "fail"]
    warns = [r for r in results if r["status"] == "warn"]
    skipped = [r for r in results if r["status"] == "skipped"]
    money = 2 if any(r["id"] in (1, 2) for r in fails) else (1 if fails else 0)  # CWV / conversion leakage
    ambiguity = 2 if len(skipped) >= 3 else (1 if skipped else 0)
    depth = 2 if len(fails) >= 3 else (1 if len(fails) + len(warns) >= 3 else 0)
    blast = 1 if len(fails) >= 2 else 0
    novelty = 0
    if prev:
        before = {a["id"]: a["status"] for a in prev.get("agents", [])}
        new_fails = [r for r in fails if before.get(r["id"]) != "fail"]
        novelty = 2 if len(new_fails) >= 2 else (1 if new_fails else 0)
    else:
        novelty = 1
    return money + ambiguity + depth + blast + novelty, (money, ambiguity)


def choose(cfg, results, prev=None):
    """Returns (tier, model, points). A fixed claude_model in config.json overrides JEV."""
    points, (money, ambiguity) = score(results, prev)
    tier = "standard" if points <= 2 else ("medium" if points <= 5 else "deep")
    if tier == "standard" and (money == 2 or ambiguity == 2):
        tier = "medium"
    model = cfg.get("claude_model") or TIERS[tier]
    log(tier, model, points)
    return tier, model, points


def log(tier, model, points):
    path = os.path.join(ROOT, "reports", "jev-routing-log.csv")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "task", "agent", "tier", "model", "score", "escalated", "outcome"])
        w.writerow([date.today().isoformat(), "executive summary", "run.py", tier, model, points, "n", ""])
