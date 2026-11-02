"""Renders shopify-agents-workflow.gif: the Shopify agents with the orchestrator and JEV model router, animated.

Run: python3 shopify-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../shopify-agents-workflow.gif'),
    accent=GREEN, kicker='SHOPIFY AGENTS', title='An AI team for your whole Shopify store', platforms='Shopify · GA4 · Klaviyo', count=16,
    orch_file='sh-orchestrator', jev_file='sh-jev-router',
    stages=[
        ('1 · Fix the store', BLUE, ['Store setup', 'Debugger', 'Catalog', 'Inventory'], 'Fast', 'Fix the store', '3 broken apps · 12 SKUs out'),
        ('2 · Convert', VIOLET, ['Conversion', 'Support', 'Shipping & returns'], 'Standard', 'Convert', 'PDP fixes · returns copy'),
        ('3 · Bring traffic', AMBER, ['SEO + AI search', 'Content & social', 'Paid ads'], 'Standard', 'Traffic', 'Collections rewritten for search'),
        ('4 · Bring back', PINK, ['Email & SMS', 'Retention'], 'Fast', 'Bring back', 'Win-back flow drafted'),
        ('5 · Measure', TEAL, ['Analytics', 'Profit & pricing'], 'Deep', 'Measure', '2 SKUs lose money after ads'),
    ],
    rules=['Every write needs your OK', 'Drafts + duplicate theme', 'Never changes ad budgets', 'Never refunds orders', 'Never deletes products', 'Items labelled AI ·'],
    data=[('Shopify store', GREEN), ('GA4 + ads', AMBER), ('Klaviyo', VIOLET)],
    leak=('Leak found', 'Traffic up · conversion down 0.6 pts'), route=('JEV routes 10 tasks', '4 fast · 5 standard · 1 deep (profit)'), final='Ranked actions · JEV saved ~60% vs all-Opus', outro='Drafts only · you publish and change budgets',
))
