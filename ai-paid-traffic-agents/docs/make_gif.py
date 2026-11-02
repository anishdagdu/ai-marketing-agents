"""Renders ai-paid-traffic-workflow.gif: the AI Paid Traffic agents with the orchestrator and JEV model router, animated.

Run: python3 ai-paid-traffic-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../ai-paid-traffic-workflow.gif'),
    accent=BLUE, kicker='AI PAID TRAFFIC', title='Paid ads end to end, routed by JEV', platforms='Meta · Google · TikTok', count=10,
    orch_file='pt-orchestrator', jev_file='pt-jev-router',
    stages=[
        ('1 · Plan', BLUE, ['Research', 'Strategy'], 'Standard', 'Plan', 'Avatar + 3 angles · KPI targets set'),
        ('2 · Create', PINK, ['Creative'], 'Standard', 'Create', '12 hooks · 3 UGC scripts · 4 statics'),
        ('3 · Launch', AMBER, ['Meta', 'Google', 'TikTok'], 'Standard', 'Launch', 'Campaigns built paused on 3 platforms'),
        ('4 · Track', TEAL, ['Tracking'], 'Fast', 'Track', 'Pixel + CAPI OK · UTMs on every ad'),
        ('5 · Scale', VIOLET, ['Scale'], 'Deep', 'Scale', 'ROAS drop traced to creative fatigue'),
    ],
    rules=['Every write needs your OK', 'New campaigns built paused', 'Never changes budgets', 'Never enters payment details', 'Never deletes ads', 'Items labelled AI ·'],
    data=[('Meta Ads', BLUE), ('Google Ads', GREEN), ('TikTok Ads', INK), ('Windsor.ai / exports', CYAN)],
    leak=('Leak found', 'CPA up 22% on Meta · Google steady'), route=('JEV routes 8 tasks', '2 fast · 5 standard · 1 deep (scale)'), final='Ranked actions · JEV saved ~60% vs all-Opus', outro='Built paused · you launch and change budgets',
))
