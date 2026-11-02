"""Renders website-audit-agents-workflow.gif: the 10 audit agents with the run.py orchestrator
and the JEV model router, animated.

Run: python3 website-audit-agents/docs/make_gif.py  (needs Pillow; not needed by run.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, "website-audit-agents-workflow.gif"),
    accent=BLUE, kicker="WEBSITE AUDIT AGENTS", title="Website speed & site health audit",
    platforms="PageSpeed · Ahrefs · Search Console", count=10,
    orch_file="run.py", jev_file="agents/jev_router.py",
    orch_lines=["Runs the 10 agents", "Builds one scorecard"],
    stages=[
        ("1 · Speed", BLUE, ["Core Web Vitals", "Conversion leakage", "Speed backlog", "Tag bloat", "Accessibility"],
         "Fast", "Speed", "LCP 3.4s on 2 revenue pages"),
        ("2 · Search", VIOLET, ["Site health", "Crawl integrity", "Striking distance", "Backlinks"],
         "Fast", "Search", "38 broken links · 11 keywords at 4-15"),
        ("3 · Alerts", AMBER, ["Regression alerts"], "Fast", "Alerts", "2 new fails vs last run"),
        ("4 · Summary", GREEN, ["Claude summary"], "Standard", "Summary", "Top 3 priorities with owners"),
    ],
    outs=[("Scorecard in reports/", "doc"), ("GitHub Issue", "check"), ("Slack alert", "bolt")],
    rules=["Read-only on your site", "Free data sources", "Fixes are a checklist",
           "No passwords stored", "Never deletes pages", "Owner on every action"],
    data=[("PageSpeed Insights", BLUE), ("Ahrefs Webmaster", AMBER), ("Search Console", GREEN)],
    leak=("Monday run", "GitHub Actions starts the speed check"),
    route=("JEV picks the model", "Agents are code · JEV routes the Claude summary"),
    final="Scorecard + Issue · Sonnet this week, Opus on bad weeks",
    outro="Read-only · your team ships the fixes", loop="every Monday",
))
