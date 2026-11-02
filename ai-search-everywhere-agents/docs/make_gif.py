"""Renders ai-search-workflow.gif: the AI Search Everywhere agents with the orchestrator and JEV model router, animated.

Run: python3 ai-search-everywhere-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/jev_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from jev_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, 'ai-search-workflow.gif'),
    accent=BLUE, kicker='AI SEARCH EVERYWHERE', title='Rank on Google and in AI answers', platforms='Google · ChatGPT · Perplexity', count=9,
    orch_file='se-orchestrator', jev_file='se-jev-router',
    stages=[
        ('1 · Foundations', BLUE, ['SEO', 'AIO'], 'Fast', 'Foundations', 'Crawl OK · 3 pages blocked to AI bots'),
        ('2 · Answers', VIOLET, ['AEO', 'GEO'], 'Standard', 'Answers', '8 FAQ rewrites · cited in 2 of 5 AI engines'),
        ('3 · Experience', AMBER, ['SXO'], 'Standard', 'Experience', 'Landing page: 2 CTA fixes, LCP 3.1s'),
        ('4 · Rank + report', GREEN, ['Rankings', 'Weekly report'], 'Deep', 'Rank', '14 striking-distance keywords · top-5 roadmap'),
    ],
    rules=['Every site change needs your OK', 'Drafts only', 'Never edits robots.txt live', 'Never buys links', 'Never deletes pages', 'Items labelled AI ·'],
    data=[('Search Console', BLUE), ('Ahrefs / Semrush', AMBER), ('GA4', GREEN), ('AI answers', VIOLET)],
    leak=('Leak found', 'Traffic flat · AI answers cite competitors'), route=('JEV routes 7 tasks', '3 fast · 3 standard · 1 deep (roadmap)'), final='Ranked actions · JEV saved ~55% vs all-Opus', outro='Drafts only · you publish every change',
))
