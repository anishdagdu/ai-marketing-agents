"""Renders shopify-agents-workflow.gif: the Shopify agents with the orchestrator, animated.

Run: python3 shopify-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../shopify-agents-workflow.gif'),
    accent=GREEN, kicker='SHOPIFY AGENTS', title='An AI team for your whole Shopify store', platforms='Shopify · GA4 · Klaviyo', count=16,
    orch_file='sh-orchestrator',
    stages=[
        ('1 · Fix the store', BLUE, ['Store setup', 'Debugger', 'Catalog', 'Inventory'], 'Standard', 'Fix the store', '3 broken apps · 12 SKUs out'),
        ('2 · Convert', VIOLET, ['Conversion', 'Support', 'Shipping & returns'], 'Medium', 'Convert', 'PDP fixes · returns copy'),
        ('3 · Bring traffic', AMBER, ['SEO + AI search', 'Content & social', 'Paid ads'], 'Medium', 'Traffic', 'Collections rewritten for search'),
        ('4 · Bring back', PINK, ['Email & SMS', 'Retention'], 'Standard', 'Bring back', 'Win-back flow drafted'),
        ('5 · Measure', TEAL, ['Analytics', 'Profit & pricing'], 'Deep', 'Measure', '2 SKUs lose money after ads'),
    ],
    rules=['Every write needs your OK', 'Drafts + duplicate theme', 'Never changes ad budgets', 'Never refunds orders', 'Never deletes products', 'Items labelled AI ·'],
    data=[('Shopify store', GREEN), ('GA4 + ads', AMBER), ('Klaviyo', VIOLET)],
    leak=('Leak found', 'Traffic up · conversion down 0.6 pts'), final='Ranked actions', outro='Drafts only · you publish and change budgets',
))
