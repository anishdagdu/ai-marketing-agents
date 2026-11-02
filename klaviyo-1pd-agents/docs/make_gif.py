"""Renders klaviyo-agents-workflow.gif: the Klaviyo 1PD agents with the orchestrator, animated.

Run: python3 klaviyo-1pd-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../klaviyo-agents-workflow.gif'),
    accent=VIOLET, kicker='KLAVIYO 1PD AGENTS', title='Email & SMS from first-party data', platforms='Klaviyo · Shopify', count=7,
    orch_file='kl-orchestrator',
    stages=[
        ('1 · Data', BLUE, ['Data foundation'], 'Standard', 'Data', 'Consent OK · 2 missing events'),
        ('2 · Segments', VIOLET, ['Segment architect'], 'Medium', 'Segments', 'RFM + intent: 9 segments'),
        ('3 · Flows', GREEN, ['Flow builder'], 'Medium', 'Flows', 'Browse + cart flows, in draft'),
        ('4 · Campaigns', AMBER, ['Campaign strategist'], 'Medium', 'Campaigns', 'Monthly calendar · 8 sends'),
        ('5 · Measure', PINK, ['Performance analyst'], 'Deep', 'Measure', 'RPR drop traced to Gmail placement'),
    ],
    rules=['Every write needs your OK', 'Flows built in draft', 'Campaigns never sent', 'Consent respected', 'Never deletes profiles', 'Items labelled AI ·'],
    data=[('Klaviyo', VIOLET), ('Shopify events', GREEN), ('Zero-party data', AMBER)],
    leak=('Leak found', 'Flow revenue down 15%'), final='Ranked actions', outro='Drafts only · you turn on flows and send',
))
