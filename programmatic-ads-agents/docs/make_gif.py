"""Renders programmatic-agents-workflow.gif: the 20 CM360 / DV360 / TTD agents, animated.

Run: python3 programmatic-ads-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, "..", "programmatic-agents-workflow.gif"),
    accent=BLUE, kicker="PROGRAMMATIC AGENTS", title="An AI team for CM360, DV360 and TTD",
    platforms="CM360 · DV360 · TTD", count=20, orch_file="pg-orchestrator",
    stages=[
        ("1 · Measure first", TEAL, ["Floodlight", "Verification", "CM360 trafficking"], "Standard",
         "Measure first", "Floodlight OK · IVT 2.1% · tags QA'd"),
        ("2 · Plan", BLUE, ["Media plan", "Audiences + UID2", "Deals + supply"], "Medium",
         "Plan", "Move CTV to TTD · keep YouTube on DV360"),
        ("3 · Buy", AMBER, ["DV360 buyer", "TTD buyer", "YouTube", "CTV · audio", "Retail media"], "Medium",
         "Buy", "New line items built paused · 3 PG deals"),
        ("4 · Optimise", PINK, ["Bidding", "Frequency", "Pacing", "Dynamic creative"], "Standard",
         "Optimise", "Freq cap 4/wk · 2 lines under-pacing"),
        ("5 · Prove", GREEN, ["Attribution", "Lift tests", "Clean room"], "Deep",
         "Prove", "CM360 dedup: 31% of DSP claims overlap"),
    ],
    rules=["Every write needs your OK", "New items built paused", "Never changes budgets",
           "Never accepts deal terms", "Never deletes data", "Items labelled AI ·"],
    data=[("CM360", BLUE), ("DV360", GREEN), ("The Trade Desk", AMBER), ("Windsor.ai / exports", CYAN)],
    leak=("Leak found", "CPA up 18% · DV360 and TTD both claim the same sales"),
    final="Ranked actions for you to approve",
    outro="Built paused · you launch, unpause and change budgets",
))
