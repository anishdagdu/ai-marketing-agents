"""Orchestrator: runs the 10 audit agents, writes the scorecard, and (optionally) asks Claude
for an executive summary.

    python run.py --mode weekly    # agents 1-5 + alerts (speed, every Monday)
    python run.py --mode monthly   # all 10 agents (full audit, 1st of the month)
"""
import argparse
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agents.common import ROOT, load_config, http_post_json  # noqa: E402
from agents import speed_agents, search_agents  # noqa: E402

ICON = {"pass": "🟢", "warn": "🟡", "fail": "🔴", "skipped": "⚪"}


def run_agents(cfg, mode, prev):
    agents = speed_agents.AGENTS + (search_agents.AGENTS if mode == "monthly" else [])
    out = []
    for fn in agents:
        print("Running", fn.__name__, "...", flush=True)
        try:
            r = fn(cfg, prev) if fn.__module__.endswith("search_agents") else fn(cfg)
        except Exception as e:
            r = {"id": int(fn.__name__.split("_")[1]), "name": fn.__name__, "status": "skipped", "kpi": "-",
                 "value": None, "target": "-", "findings": ["Agent error: " + str(e)], "actions": [], "owner": "-"}
        out.append(r)
    print("Running agent_10_alerts ...", flush=True)
    out.append(search_agents.agent_10_alerts(cfg, out, prev))
    return out


def claude_summary(cfg, results):
    """Executive summary from Claude. Skipped when ANTHROPIC_API_KEY is not set."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return None
    slim = [{k: r[k] for k in ("name", "status", "kpi", "value", "target", "actions", "owner")} for r in results]
    prompt = (
        "You are the VP of Marketing Analytics. Below are this period's website audit results for {}.\n"
        "Write a short executive summary for the leadership team: 1) overall health in one sentence, "
        "2) the top 3 priorities with owner and expected business impact, 3) any risks. Plain language, "
        "under 200 words, markdown bullets.\n\n{}").format(cfg["site"], json.dumps(slim, indent=1))
    try:
        resp = http_post_json("https://api.anthropic.com/v1/messages", {
            "model": cfg.get("claude_model", "claude-sonnet-5-5"), "max_tokens": 800,
            "messages": [{"role": "user", "content": prompt}]},
            headers={"x-api-key": key, "anthropic-version": "2023-06-01"})
        return "".join(b.get("text", "") for b in resp.get("content", []))
    except Exception as e:
        return "_Claude summary failed: {}_".format(e)


def write_report(cfg, mode, results, summary):
    today = date.today().isoformat()
    lines = ["# Website audit scorecard - {}".format(cfg["site"]),
             "_{} run, {}_".format(mode.title(), today), ""]
    if summary:
        lines += ["## Executive summary (Claude)", summary, ""]
    lines += ["## Scorecard", "", "| # | Agent | Status | KPI | Value | Target | Owner |",
              "|---|---|---|---|---|---|---|"]
    for r in results:
        lines.append("| {id} | {name} | {icon} {status} | {kpi} | {value} | {target} | {owner} |".format(
            icon=ICON[r["status"]], **r))
    for r in results:
        lines += ["", "### {}. {} {}".format(r["id"], r["name"], ICON[r["status"]])]
        lines += ["- " + f for f in r["findings"]]
        if r["actions"]:
            lines += ["", "**Next actions**"] + ["- [ ] " + a for a in r["actions"]]
    rep_dir = os.path.join(ROOT, "reports")
    os.makedirs(os.path.join(rep_dir, "history"), exist_ok=True)
    md_path = os.path.join(rep_dir, "{}-{}.md".format(today, mode))
    with open(md_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    snap = {"date": today, "mode": mode, "site": cfg["site"], "agents": results}
    with open(os.path.join(rep_dir, "history", "latest-{}.json".format(mode)), "w") as f:
        json.dump(snap, f, indent=1)
    with open(os.path.join(rep_dir, "latest.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    return md_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["weekly", "monthly"], default="monthly")
    ap.add_argument("--config", default=None)
    args = ap.parse_args()
    cfg = load_config(args.config)
    prev_path = os.path.join(ROOT, "reports", "history", "latest-{}.json".format(args.mode))
    prev = json.load(open(prev_path)) if os.path.exists(prev_path) else None
    results = run_agents(cfg, args.mode, prev)
    path = write_report(cfg, args.mode, results, claude_summary(cfg, results))
    print("\nReport written:", path)
    for r in results:
        print(" {} {:>2}. {:<36} {}".format(ICON[r["status"]], r["id"], r["name"], r["value"]))
    if os.environ.get("FAIL_ON_CRITICAL") and any(r["status"] == "fail" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
