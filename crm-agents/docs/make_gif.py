"""Renders crm-agents-architecture.gif: the CRM agents with the orchestrator, animated.

Run: python3 crm-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../crm-agents-architecture.gif'),
    accent=VIOLET, kicker='CRM AGENTS', title='Player CRM with RG first', platforms='Gaming · Retail · App', count=12,
    orch_file='crm-orchestrator',
    stages=[
        ('1 · Know', BLUE, ['Player 360', 'Predictive scoring'], 'Medium', 'Know', '1 profile per player · churn scores'),
        ('2 · Design', VIOLET, ['Journey designer', 'Real-time trigger', 'Personalisation'], 'Medium', 'Design', 'Win-back journey · 3 steps · copy in fi/sv/en'),
        ('3 · Protect', RED, ['RG guardian', 'Contact policy'], 'Deep', 'Protect', '214 at-risk players removed'),
        ('4 · Learn', TEAL, ['Uplift & control', 'Test optimiser', 'Insights & calendar'], 'Medium', 'Learn', '+4.1% uplift vs control'),
    ],
    rules=['Drafts only · you approve', 'RG guardian can veto', '5–10% control group', 'Quiet hours + caps', 'Never deletes players', 'Items labelled AI ·'],
    data=[('Gaming platform', BLUE), ('Loyalty card', AMBER), ('App + web events', VIOLET)],
    leak=('Leak found', 'Lapsed Lotto players up 18%'), final='Journeys to approve', outro='Drafts only · your platform team builds',
))
