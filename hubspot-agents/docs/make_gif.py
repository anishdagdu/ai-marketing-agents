"""Renders hubspot-agents-workflow.gif: the HubSpot agents with the orchestrator, animated.

Run: python3 hubspot-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../hubspot-agents-workflow.gif'),
    accent=AMBER, kicker='HUBSPOT AGENTS', title='An AI team for your whole HubSpot', platforms='HubSpot · Shopify · Stripe', count=16,
    orch_file='hs-orchestrator',
    stages=[
        ('1 · Fix the CRM', BLUE, ['CRM setup', 'Data hygiene', 'Integrations'], 'Standard', 'Fix the CRM', 'Orders + MRR synced to contacts'),
        ('2 · Convert', VIOLET, ['Forms & pages', 'Lead scoring', 'Sales pipeline'], 'Medium', 'Convert', 'New lead score · stuck deals get a sequence'),
        ('3 · Bring traffic', AMBER, ['SEO + AI search', 'Social', 'Ads + audiences'], 'Medium', 'Traffic', 'Ads target scored segments'),
        ('4 · Bring back', PINK, ['Email', 'Workflows', 'Help desk'], 'Medium', 'Bring back', 'Nurture + failed-payment flows, off'),
        ('5 · Measure', TEAL, ['Reports', 'Stripe revenue'], 'Deep', 'Measure', 'Attribution · MRR · churn readout'),
    ],
    rules=['Every write needs your OK', 'Drafts + workflows off', 'Never refunds in Stripe', 'Slack posts need a yes', 'Never deletes records', 'Assets labelled AI ·'],
    data=[('HubSpot CRM', AMBER), ('Shopify', GREEN), ('Stripe', VIOLET)],
    leak=('Leak found', 'Plenty of leads · few become deals'), final='Ranked actions', outro='Drafts only · you publish, send and turn on',
))
