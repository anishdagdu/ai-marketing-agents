"""Renders workflow.gif: the Finnish Marketing agents with the orchestrator and JEV model router, animated.

Run: python3 finnish-marketing-agents/scripts/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../docs/workflow.gif'),
    accent=BLUE, kicker='FINNISH MARKETING AGENTS', title='Finnish marketing end to end, routed by JEV', platforms='Google · Meta · LinkedIn · Snapchat', count=4,
    orch_file='finnish-marketing-orchestrator', jev_file='finnish-jev-router',
    stages=[
        ('1 · Research', BLUE, ['Website sentiment', 'Competitor sentiment'], 'Standard', 'Research', '3 praise themes · 2 competitor gaps'),
        ('2 · Plan', PINK, ['Strategy', 'Content calendar'], 'Deep', 'Plan', 'Pillars + 30-day calendar'),
        ('3 · Write', AMBER, ['Ad copy · 4 networks'], 'Standard', 'Write', '48 ads in Finnish + English'),
        ('4 · QA', TEAL, ['fi ↔ en + limits'], 'Fast', 'QA', 'All under character limits'),
    ],
    rules=['4 approval gates', 'Nothing is published', 'Native Finnish copy', 'Ad policy checked', 'Never enters passwords', 'Drafts labelled AI ·'],
    data=[('Website', BLUE), ('Reviews', AMBER), ('Meta Ad Library', VIOLET)],
    leak=('Brief in', 'Launch in Finland · 4 channels'), route=('JEV routes 6 tasks', '2 fast · 3 standard · 1 deep (strategy)'), final='Calendar + ads to approve · JEV saved ~50%', outro='Nothing is published without your OK',
))
