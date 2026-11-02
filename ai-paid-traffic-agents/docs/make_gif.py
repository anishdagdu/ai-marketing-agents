"""Renders ai-paid-traffic-workflow.gif: the AI Paid Traffic agents with the orchestrator, animated.

Run: python3 ai-paid-traffic-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../ai-paid-traffic-workflow.gif'),
    accent=BLUE, kicker='AI PAID TRAFFIC', title='Paid ads end to end', platforms='Meta · Google · TikTok', count=10,
    orch_file='pt-orchestrator',
    stages=[
        ('1 · Plan', BLUE, ['Research', 'Strategy'], 'Medium', 'Plan', 'Avatar + 3 angles · KPI targets set'),
        ('2 · Create', PINK, ['Creative'], 'Medium', 'Create', '12 hooks · 3 UGC scripts · 4 statics'),
        ('3 · Launch', AMBER, ['Meta', 'Google', 'TikTok'], 'Medium', 'Launch', 'Campaigns built paused on 3 platforms'),
        ('4 · Track', TEAL, ['Tracking'], 'Standard', 'Track', 'Pixel + CAPI OK · UTMs on every ad'),
        ('5 · Scale', VIOLET, ['Scale'], 'Deep', 'Scale', 'ROAS drop traced to creative fatigue'),
    ],
    rules=['Every write needs your OK', 'New campaigns built paused', 'Never changes budgets', 'Never enters payment details', 'Never deletes ads', 'Items labelled AI ·'],
    data=[('Meta Ads', BLUE), ('Google Ads', GREEN), ('TikTok Ads', INK), ('Windsor.ai / exports', CYAN)],
    leak=('Leak found', 'CPA up 22% on Meta · Google steady'), final='Ranked actions', outro='Built paused · you launch and change budgets',
))
