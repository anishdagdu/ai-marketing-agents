"""Renders mmp-agents-workflow.gif: the MMP agents with the orchestrator, animated.

Run: python3 mmp-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../mmp-agents-workflow.gif'),
    accent=BLUE, kicker='MMP AGENTS', title='An AI team for AppsFlyer, Adjust and every MMP', platforms='AppsFlyer · Adjust · Branch', count=22,
    orch_file='mmp-orchestrator',
    stages=[
        ('1 · Measure', BLUE, ['Attribution', 'SAN reconcile', 'Lookback windows', 'SKAN + AAK'], 'Medium', 'Measure', 'Meta claims 18% more installs'),
        ('2 · Signals', VIOLET, ['Postbacks', 'In-app events', 'Ad revenue', 'Raw data export'], 'Standard', 'Signals', '2 events not posting back'),
        ('3 · Protect', RED, ['Fraud: real time', 'Fraud: after', 'Privacy + consent', 'Clean room'], 'Medium', 'Protect', '7% installs flagged as fraud'),
        ('4 · Analyze', AMBER, ['Cost + ROAS', 'Cohorts + LTV', 'Creative', 'Incrementality'], 'Deep', 'Analyze', 'D30 ROAS 82% · 1 network not incremental'),
        ('5 · Activate', TEAL, ['Deep linking', 'Web, CTV, PC', 'Audiences', 'AI copilot'], 'Standard', 'Activate', '3 audiences ready to sync'),
    ],
    rules=['Every MMP change needs your OK', 'Never changes budgets', 'Never touches the SDK', 'Consent respected', 'Never deletes data', 'Items labelled AI ·'],
    data=[('AppsFlyer / Adjust', BLUE), ('Ad networks + cost', AMBER), ('Warehouse + CRM', GREEN)],
    leak=('Leak found', "ROAS looks fine · revenue doesn't"), final='Ranked actions', outro='Recommendations only · you change the MMP',
))
