"""Renders crm-agents-architecture.gif: the CRM agents with the orchestrator and JEV model router, animated.

Run: python3 crm-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../crm-agents-architecture.gif'),
    accent=VIOLET, kicker='CRM AGENTS', title='Player CRM with RG first, routed by JEV', platforms='Gaming · Retail · App', count=12,
    orch_file='crm-orchestrator', jev_file='crm-jev-router',
    stages=[
        ('1 · Know', BLUE, ['Player 360', 'Predictive scoring'], 'Standard', 'Know', '1 profile per player · churn scores'),
        ('2 · Design', VIOLET, ['Journey designer', 'Real-time trigger', 'Personalisation'], 'Standard', 'Design', 'Win-back journey · 3 steps · copy in fi/sv/en'),
        ('3 · Protect', RED, ['RG guardian', 'Contact policy'], 'Deep', 'Protect', '214 at-risk players removed'),
        ('4 · Learn', TEAL, ['Uplift & control', 'Test optimiser', 'Insights & calendar'], 'Standard', 'Learn', '+4.1% uplift vs control'),
    ],
    rules=['Drafts only · you approve', 'RG guardian can veto', '5–10% control group', 'Quiet hours + caps', 'Never deletes players', 'Items labelled AI ·'],
    data=[('Gaming platform', BLUE), ('Loyalty card', AMBER), ('App + web events', VIOLET)],
    leak=('Leak found', 'Lapsed Lotto players up 18%'), route=('JEV routes 10 tasks', '3 fast · 6 standard · 1 deep (RG)'), final='Journeys to approve · JEV saved ~50% vs all-Opus', outro='Drafts only · your platform team builds',
))
