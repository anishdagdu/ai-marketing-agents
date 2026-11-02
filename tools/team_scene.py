"""Shared layout for the agent-team GIFs: an orchestrator card, 3-5 stage bands of agents,
an approval column and a guardrails band.

Each set's docs/make_gif.py fills in a config dict and calls render(cfg). Needs gifkit.py.
Model routing (standard Haiku, medium Sonnet, deep Opus) lives in the agent files, not the GIF.
"""
from gifkit import *  # noqa: F401,F403


def render(cfg):
    stages = cfg["stages"]  # [(label, color, [agent chip labels], tier, callout title, callout text)]
    n = len(stages)
    accent = cfg.get("accent", BLUE)
    sx0, sx1, sg, sy0, sy1 = 290, 1050, 10, 140, 470
    sw = (sx1 - sx0 - sg * (n - 1)) / n
    sxs = [sx0 + i * (sw + sg) for i in range(n)]
    ox0, ox1 = 1070, 1240
    outs = cfg.get("outs", [("Ranked actions", "check"), ("Weekly readout", "doc"), ("Change log", "chart")])
    outs = [(("Change log", ic) if "JEV" in lab else (lab, ic)) for lab, ic in outs]
    oy = [200 + i * 54 for i in range(3)]

    lines = cfg.get("orch_lines", ["Finds the biggest leak", "Ranks every action"])
    lines = list(lines) + ["Briefs each stage", "Checks every result"][: max(0, 4 - len(lines))]
    nodes = {"orch": Node("orch", 40, 200, 260, 410, "Orchestrator", cfg["orch_file"], accent, "spark", "LEAD",
                          lines=lines)}
    links = {"orch>s0": (Path(curve(nodes["orch"].R(0), (sxs[0], 300))), accent)}
    for i in range(n - 1):
        links[f"s{i}>s{i+1}"] = (Path(curve((sxs[i] + sw, 300), (sxs[i + 1], 300))), stages[i + 1][1])
    links[f"s{n-1}>out"] = (Path(curve((sxs[-1] + sw, 300), (ox0, oy[1] + 20))), GREEN)
    links["out>orch"] = (Path(poly(((ox0 + ox1) / 2, oy[2] + 44), ((ox0 + ox1) / 2, 490), (150, 490), (150, 412))),
                         accent)

    appear = {"orch": 0.2, "out": 0.6 + 0.2 * n + 0.15, "band": 0.6 + 0.2 * n + 0.45}
    appear.update({f"s{i}": 0.6 + 0.2 * i for i in range(n)})
    rules = cfg["rules"]
    data = cfg["data"]

    def under(c, t, state):
        act = state["act"]
        for i, (lab, col, agents, *_rest) in enumerate(stages):
            key = f"s{i}"
            x0, x1 = sxs[i], sxs[i] + sw
            on = state["amt"] if act == key else 0.0
            if on:
                c.glow(x0, sy0, x1, sy1, col, 0.7 * on)
            band(c, x0, sy0, x1, sy1, lab, col, window(t, appear[key], appear[key] + 0.5))
            pitch = min(52, (sy1 - sy0 - 44) / max(1, len(agents)))
            for j, ag in enumerate(agents):
                y = sy0 + 36 + j * pitch
                chip(c, x0 + 8, y, x1 - 8, y + pitch - 10, ag, None, col,
                     window(t, appear[key] + 0.1 + j * 0.06, appear[key] + 0.5 + j * 0.06), on, 12.5)
        section_label(c, ox0, 172, "You approve", a=window(t, appear["out"], appear["out"] + 0.4))
        for i, (lab, ic) in enumerate(outs):
            on = state["amt"] if act == "out" else 0.0
            chip(c, ox0, oy[i], ox1, oy[i] + 44, lab, ic, GREEN,
                 window(t, appear["out"] + i * 0.08, appear["out"] + 0.4 + i * 0.08), on, 12.5)
        c.text(680, 497, cfg.get("loop", "weekly loop"), 12, "bold", accent, anchor="mm",
               a=window(t, appear["out"] + 0.3, appear["out"] + 0.7))
        a = window(t, appear["band"], appear["band"] + 0.5)
        band(c, 40, 512, 1240, 632, "Guardrails in every agent", accent, a)
        x = 60
        for r in rules:
            x += c.pill(x, 540, r, accent, size=12.5, weight="demi", a=a, h=28) + 10
        c.text(60, 594, "Data:", 13, "demi", INK, anchor="lm", a=a)
        x = 60 + c.text_w("Data:", 13, "demi") + 12
        for lab, col in data:
            x += c.pill(x, 580, lab, col, size=12.5, weight="demi", a=a, h=28) + 10

    def cb(i):
        dx = 60 if i == 0 else (-40 if i == n - 1 else 0)
        return (sxs[i] + sw / 2 + dx, sy1)

    steps = [Step(None, "orch", 0, 1.2, cfg["leak"][0], cfg["leak"][1], accent, side="top", callout_xy=(150, 200))]
    for i, (lab, col, agents, _tier, ctitle, ctext) in enumerate(stages):
        src = "orch>s0" if i == 0 else f"s{i-1}>s{i}"
        steps.append(Step(src, f"s{i}", 0.45 if i == 0 else 0.4, 1.2, ctitle, ctext, col, side="bottom",
                          callout_xy=cb(i)))
    final = cfg["final"].split(" · JEV")[0]
    steps.append(Step(f"s{n-1}>out", "out", 0.45, 1.6, "Your call", final, GREEN, side="bottom",
                      callout_xy=(1080, oy[2] + 44)))
    sc = [Scenario("Weekly check", cfg.get("scenario", "Orchestrator finds the leak · each stage acts on it"),
                   accent, steps, label="")]
    total = sum(len(s[2]) for s in stages) + 1
    count = cfg.get("count", total)
    title = cfg["title"].replace(", routed by JEV", "").replace(" routed by JEV", "")
    run_scene(out=cfg["out"], accent=accent, kicker=cfg["kicker"], title=title,
              sub="Orchestrator → " + " → ".join(s[0].split("· ")[-1].lower() for s in stages),
              right=[(f"{count} agents", AMBER), (cfg["platforms"], GREEN), ("You approve", BLUE)],
              nodes=nodes, links=links, appear=appear, scenarios=sc, build_end=appear["band"] + 0.75, under=under,
              dash_links=("out>orch",),
              build_caption=("WORKFLOW", f"{count} agents in {n} stages, led by one orchestrator", accent),
              outro_caption=("YOU APPROVE", cfg["outro"], accent))
