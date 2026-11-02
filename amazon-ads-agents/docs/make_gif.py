"""Renders amazon-ads-agents-workflow.gif: the Amazon Ads agents with the orchestrator and JEV model router, animated.

Run: python3 amazon-ads-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../amazon-ads-agents-workflow.gif'),
    accent=AMBER, kicker='AMAZON ADS AGENTS', title='An AI team for Amazon Ads, routed by JEV', platforms='Sponsored Ads · DSP', count=14,
    orch_file='amz-orchestrator', jev_file='amz-jev-router',
    stages=[
        ('1 · Setup', BLUE, ['Product research', 'Keyword research', 'Competitor intel', 'Listing readiness'], 'Standard', 'Setup', 'Break-even ACoS 28% · listing 82/100'),
        ('2 · Build', VIOLET, ['Account architect', 'Sponsored Products', 'Sponsored Brands', 'Display & DSP'], 'Standard', 'Build', 'Bulk sheet: 9 campaigns, paused'),
        ('3 · Optimise', PINK, ['Search term harvest', 'Bid optimizer', 'Budget & pacing'], 'Deep', 'Optimise', '42 negatives · bids to target ACoS'),
        ('4 · Report', TEAL, ['Reporting'], 'Fast', 'Report', 'ACoS 31% → 26% · TACoS 9%'),
    ],
    rules=['Every write needs your OK', 'New campaigns built paused', 'Never changes budgets', 'Never enters payment details', 'Archive, never delete', 'Items labelled AI ·'],
    data=[('Amazon Ads', AMBER), ('Seller Central', BLUE), ('Bulk sheets', GREEN)],
    leak=('Leak found', 'ACoS 34% · 40% of spend on no-sale terms'), route=('JEV routes 12 tasks', '5 fast · 6 standard · 1 deep (bids)'), final='Ranked actions · JEV saved ~65% vs all-Opus', outro='Built paused · you launch and change budgets',
))
