"""Renders hubspot-agents-workflow.gif: the HubSpot agents with the orchestrator and JEV model router, animated.

Run: python3 hubspot-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../hubspot-agents-workflow.gif'),
    accent=AMBER, kicker='HUBSPOT AGENTS', title='An AI team for your whole HubSpot', platforms='HubSpot · Shopify · Stripe', count=16,
    orch_file='hs-orchestrator', jev_file='hs-jev-router',
    stages=[
        ('1 · Fix the CRM', BLUE, ['CRM setup', 'Data hygiene', 'Integrations'], 'Fast', 'Fix the CRM', 'Orders + MRR synced to contacts'),
        ('2 · Convert', VIOLET, ['Forms & pages', 'Lead scoring', 'Sales pipeline'], 'Standard', 'Convert', 'New lead score · stuck deals get a sequence'),
        ('3 · Bring traffic', AMBER, ['SEO + AI search', 'Social', 'Ads + audiences'], 'Standard', 'Traffic', 'Ads target scored segments'),
        ('4 · Bring back', PINK, ['Email', 'Workflows', 'Help desk'], 'Standard', 'Bring back', 'Nurture + failed-payment flows, off'),
        ('5 · Measure', TEAL, ['Reports', 'Stripe revenue'], 'Deep', 'Measure', 'Attribution · MRR · churn readout'),
    ],
    rules=['Every write needs your OK', 'Drafts + workflows off', 'Never refunds in Stripe', 'Slack posts need a yes', 'Never deletes records', 'Assets labelled AI ·'],
    data=[('HubSpot CRM', AMBER), ('Shopify', GREEN), ('Stripe', VIOLET)],
    leak=('Leak found', 'Plenty of leads · few become deals'), route=('JEV routes 9 tasks', '3 fast · 5 standard · 1 deep (revenue)'), final='Ranked actions · JEV saved ~60% vs all-Opus', outro='Drafts only · you publish, send and turn on',
))
