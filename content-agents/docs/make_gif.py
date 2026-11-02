"""Renders content-agents-workflow.gif: the Content agents with the orchestrator and JEV model router, animated.

Run: python3 content-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../content-agents-workflow.gif'),
    accent=PINK, kicker='CONTENT AGENTS', title='Social content from real sentiment research', platforms='Instagram · LinkedIn · TikTok · Postiz', count=6,
    orch_file='content-orchestrator', jev_file='content-jev-router',
    stages=[
        ('1 · Research', BLUE, ['Website sentiment', 'Competitor sentiment'], 'Standard', 'Research', '3 praise themes · 2 gaps competitors miss'),
        ('2 · Plan', PINK, ['Calendar planner'], 'Deep', 'Plan', '30-day calendar on 5 platforms'),
        ('3 · Publish', GREEN, ['Postiz publisher'], 'Fast', 'Publish', '28 posts queued as drafts'),
    ],
    rules=['Two checkpoints with you', 'Posts scheduled as drafts', 'Never posts without OK', 'Never enters passwords', 'Never deletes posts', 'Posts labelled AI ·'],
    data=[('Website', BLUE), ('Reviews + social', AMBER), ('Postiz', GREEN)],
    leak=('Brief in', 'Engagement down · posts off-brand'), route=('JEV routes 5 tasks', '2 fast · 2 standard · 1 deep (calendar)'), final='Calendar to approve · JEV saved ~45% vs all-Opus', outro='You approve the calendar · Postiz schedules',
))
