"""Renders gtm-agent-workflow.gif: the GTM Health agents with the orchestrator, animated.

Run: python3 gtm-health-agent/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../gtm-agent-workflow.gif'),
    accent=BLUE, kicker='GTM HEALTH AGENT', title='Weekly Google Tag Manager audit', platforms='GTM · GA4', count=3,
    orch_file='gtm-orchestrator',
    stages=[
        ('1 · Collect', BLUE, ['Containers', 'Tags + triggers', 'Variables'], 'Standard', 'Collect', '4 containers · 312 tags read'),
        ('2 · Audit', AMBER, ["Won't-fire checks", 'Consent + duplicates'], 'Standard', 'Audit', "6 tags can't fire · 2 duplicates"),
        ('3 · Diagnose', PINK, ['Root causes', 'vs last week'], 'Medium', 'Diagnose', 'New break: v41 removed a trigger'),
        ('4 · Report', GREEN, ['Weekly report'], 'Medium', 'Report', 'Fixes ranked by revenue impact'),
    ],
    rules=['Read-only in GTM', 'Fixes are suggestions', 'Never publishes a version', 'Never enters passwords', 'Never deletes tags', 'Ranked by impact'],
    data=[('GTM MCP', BLUE), ('GA4 (optional)', AMBER)],
    leak=('Monday 8:00', 'Weekly audit starts'), final='Fix list', outro='Read-only · you make and publish the fixes',
))
