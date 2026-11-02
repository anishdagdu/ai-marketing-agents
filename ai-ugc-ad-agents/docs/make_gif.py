"""Renders ai-ugc-agents-workflow.gif: the AI UGC Ad agents with the orchestrator, animated.

Run: python3 ai-ugc-ad-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py + tools/team_scene.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from team_scene import *  # noqa: E402,F403

render(dict(
    out=os.path.join(HERE, '../ai-ugc-agents-workflow.gif'),
    accent=VIOLET, kicker='AI UGC AD AGENTS', title='AI creator video ads', platforms='Higgsfield · Meta · TikTok', count=6,
    orch_file='ugc-orchestrator',
    stages=[
        ('1 · Plan', VIOLET, ['UGC director'], 'Deep', 'Plan', '4 creators · 12 hooks · 3 angles'),
        ('2 · Prompts', BLUE, ['Prompt engineer'], 'Medium', 'Prompts', 'Soul 2.0 image + Seedance video prompts'),
        ('3 · Check', AMBER, ['Compliance check'], 'Standard', 'Check', '2 claims softened · AI disclosure added'),
        ('4 · Generate', GREEN, ['Higgsfield operator'], 'Standard', 'Generate', '6 videos after your credit OK'),
    ],
    rules=['Credits spent only after your OK', 'Compliance check first', 'AI disclosure on every ad', 'Never enters payment details', 'Never posts ads', 'Files labelled AI ·'],
    data=[('Product brief', INK), ('Higgsfield', GREEN), ('Meta / TikTok policy', AMBER)],
    leak=('Brief in', 'New serum · TikTok + Reels · 6 ads'), final='6 ad videos', outro='You approve credits · you post the ads',
))
