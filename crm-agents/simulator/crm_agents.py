"""CRM Agents: 10 agents sharing one data layer.

The RG Guardian can veto any message before it is sent.
Run: python3 crm_agents.py
"""
from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from datetime import datetime

random.seed(7)

AUDIT_LOG: list[dict] = []


def log(agent: str, player_id: str, decision: str, reason: str) -> None:
    """Every agent decision is logged so it can be explained to auditors."""
    AUDIT_LOG.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "agent": agent, "player": player_id,
        "decision": decision, "reason": reason,
    })


# ---------------------------------------------------------------- data layer
@dataclass
class Player:
    id: str
    channel: str                 # "retail" or "digital"
    favourite_game: str
    weekly_draws: list[int]      # 1 = played that week, newest last
    avg_weekly_spend: float
    language: str = "fi"
    opted_in: bool = True
    # RG signals
    limit_raised_recently: bool = False
    late_night_share: float = 0.0
    deposit_speed_up: float = 1.0
    session_len_change: float = 1.0
    chasing_losses: bool = False
    messages_this_week: int = 0
    # filled by agents
    segment: str = ""
    churn_risk: float = 0.0
    ltv_12m: float = 0.0
    rg_score: float = 0.0
    next_best_action: str = ""


@dataclass
class Message:
    player_id: str
    kind: str          # "promo" or "care"
    channel: str
    content: str
    predicted_uplift: float
    journey: str
    variant: str = ""


# ---------------------------------------------------------------- agent 1
class Player360Agent:
    name = "1 Player 360 & Segmentation"

    def run(self, p: Player) -> None:
        recent = sum(p.weekly_draws[-4:])
        cadence = "Weekly" if recent >= 3 else "Occasional" if recent else "Lapsed"
        risk = "high risk" if p.rg_score >= 0.6 else "low risk"
        p.segment = f"{cadence} {p.favourite_game} player, {p.channel}, {risk}"
        log(self.name, p.id, "segment", p.segment)


# ---------------------------------------------------------------- agent 8
class RGGuardianAgent:
    """Highest priority. Can veto any outgoing promotion."""
    name = "8 RG Guardian"
    HIGH = 0.6  # changed only with human approval

    def score(self, p: Player) -> float:
        s = 0.0
        s += 0.25 if p.limit_raised_recently else 0
        s += 0.25 * min(p.late_night_share / 0.4, 1)
        s += 0.2 if p.chasing_losses else 0
        s += 0.15 * min(max(p.deposit_speed_up - 1, 0), 1)
        s += 0.15 * min(max(p.session_len_change - 1, 0), 1)
        p.rg_score = round(s, 2)
        return p.rg_score

    def review(self, p: Player, msg: Message) -> Message | None:
        self.score(p)
        if msg.kind == "care":
            return msg
        if p.rg_score >= self.HIGH:
            log(self.name, p.id, "VETO + escalate to player care",
                f"rg_score={p.rg_score}")
            return Message(p.id, "care", msg.channel,
                           "Haluatko asettaa pelirajan? Set a limit in 2 taps.",
                           0.0, msg.journey)
        log(self.name, p.id, "pass", f"rg_score={p.rg_score}")
        return msg


# ---------------------------------------------------------------- agent 2
class PredictiveScoringAgent:
    name = "2 Predictive Scoring"

    def run(self, p: Player, rg: RGGuardianAgent) -> None:
        missed = sum(1 for x in p.weekly_draws[-3:] if x == 0)
        p.churn_risk = round(min(0.3 + 0.15 * missed, 0.95), 2)
        p.ltv_12m = round(p.avg_weekly_spend * 52 * (1 - p.churn_risk), 2)
        rg.score(p)
        if p.rg_score >= rg.HIGH:
            p.next_best_action = "care_message"   # never an offer
        elif p.churn_risk >= 0.6:
            p.next_best_action = "winback_journey"
        elif p.channel == "retail":
            p.next_best_action = "shop_to_app_journey"
        else:
            p.next_best_action = "keep_warm"
        log(self.name, p.id, p.next_best_action,
            f"churn={p.churn_risk} ltv={p.ltv_12m} rg={p.rg_score}")


# ---------------------------------------------------------------- agent 9
class ContactPolicyAgent:
    name = "9 Contact Policy"
    WEEKLY_PROMO_CAP = 3

    def filter(self, p: Player, msgs: list[Message]) -> list[Message]:
        care = [m for m in msgs if m.kind == "care"]
        promos = sorted((m for m in msgs if m.kind == "promo"),
                        key=lambda m: m.predicted_uplift, reverse=True)
        room = max(self.WEEKLY_PROMO_CAP - p.messages_this_week, 0)
        kept = promos[:min(room, 1)]  # one winner per send window
        for m in promos[len(kept):]:
            log(self.name, p.id, "drop", f"{m.journey}: cap or lower uplift")
        return care + kept


# ---------------------------------------------------------------- agent 7
class PersonalisationAgent:
    name = "7 Personalisation"
    COPY = {
        "fi": "{game}: jättipotti {jackpot} - pelaa ennen arvontaa!",
        "sv": "{game}: jackpott {jackpot} - spela före dragningen!",
        "en": "{game}: jackpot {jackpot} - play before the draw!",
    }

    def render(self, p: Player, msg: Message, jackpot: str) -> Message:
        if msg.kind == "promo":
            msg.content = self.COPY[p.language].format(
                game=p.favourite_game, jackpot=jackpot)
        return msg


# ---------------------------------------------------------------- agent 6
class OptimisationAgent:
    """Thompson-sampling bandit. Reward = incremental conversion, never spend."""
    name = "6 Self-Optimising Test"

    def __init__(self, arms: list[str]):
        self.stats = {a: [1, 1] for a in arms}  # beta(alpha, beta)

    def choose(self) -> str:
        return max(self.stats, key=lambda a: random.betavariate(*self.stats[a]))

    def update(self, arm: str, converted: bool) -> None:
        self.stats[arm][0 if converted else 1] += 1


# ---------------------------------------------------------------- agent 5
class UpliftAgent:
    name = "5 Uplift & Control Group"
    HOLDOUT = 0.10

    def __init__(self):
        self.results: dict[str, dict] = {}

    def assign(self, journey: str, p: Player) -> bool:
        """True = player is held back as control."""
        r = self.results.setdefault(journey, {"t": [], "c": []})
        control = random.random() < self.HOLDOUT
        return control

    def record(self, journey: str, control: bool, outcome: int) -> None:
        self.results[journey]["c" if control else "t"].append(outcome)

    def report(self, journey: str) -> dict:
        r = self.results[journey]
        t = sum(r["t"]) / max(len(r["t"]), 1)
        c = sum(r["c"]) / max(len(r["c"]), 1)
        se = ((t * (1 - t) / max(len(r["t"]), 1)) +
              (c * (1 - c) / max(len(r["c"]), 1))) ** 0.5
        lift = (t - c) * 100
        return {"journey": journey, "treated": len(r["t"]), "control": len(r["c"]),
                "uplift_pts": round(lift, 1),
                "ci95": [round(lift - 196 * se, 1), round(lift + 196 * se, 1)],
                "flag_stop": lift - 196 * se <= 0}


# ---------------------------------------------------------------- agent 3
class JourneyOrchestratorAgent:
    name = "3 Journey Orchestrator"
    JOURNEYS = {
        "winback_journey": [("day 0", "push"), ("day 3", "email"), ("day 7", "in-app")],
        "shop_to_app_journey": [("day 1", "sms"), ("day 3", "push"), ("day 7", "in-app")],
    }

    def plan(self, p: Player, channel: str) -> list[Message]:
        if p.next_best_action == "care_message":
            return [Message(p.id, "care", "in-app", "", 0.0, "care")]
        steps = self.JOURNEYS.get(p.next_best_action)
        if not steps:
            return []
        day, _ = steps[0]
        uplift = round(p.churn_risk * 0.1 + random.uniform(0, 0.02), 3)
        return [Message(p.id, "promo", channel, "", uplift,
                        p.next_best_action, variant=day)]


# ---------------------------------------------------------------- agent 4
class RealTimeTriggerAgent:
    name = "4 Real-Time Trigger"

    def on_event(self, event: str, players: list[Player], rg: RGGuardianAgent,
                 cp: ContactPolicyAgent) -> list[Message]:
        sent = []
        for p in players:
            if not p.opted_in:
                continue
            msg = Message(p.id, "promo", "push", event, 0.05, "trigger:" + event)
            msg = rg.review(p, msg)
            for m in cp.filter(p, [msg]):
                sent.append(m)
        return sent


# ---------------------------------------------------------------- agent 10
class InsightsCalendarAgent:
    name = "10 Insights & Calendar"
    CALENDAR = ["Tue: Eurojackpot draw", "Sat: Lotto draw", "Dec 6: Independence Day"]

    def weekly_summary(self, reports: list[dict], vetoes: int, sent: int) -> str:
        lines = ["Weekly CRM summary", f"- Messages sent: {sent}",
                 f"- Promotions blocked by RG Guardian: {vetoes}"]
        for r in reports:
            verdict = ("not significant yet (stop if repeated next cycle)"
                       if r["flag_stop"] else "suggest always-on")
            lines.append(f"- {r['journey']}: {r['uplift_pts']:+} pts vs control "
                         f"(95% CI {r['ci95']}), {verdict}")
        lines.append("- Coming up: " + "; ".join(self.CALENDAR))
        return "\n".join(lines)


# ---------------------------------------------------------------- pipeline
def make_players(n: int = 400) -> list[Player]:
    games = ["Lotto", "Eurojackpot", "Keno", "Vakio"]
    out = []
    for i in range(n):
        risky = random.random() < 0.08
        out.append(Player(
            id=f"P{i:04d}",
            channel=random.choice(["retail", "digital", "digital"]),
            favourite_game=random.choice(games),
            weekly_draws=[random.choice([0, 1, 1]) for _ in range(6)],
            avg_weekly_spend=round(random.uniform(2, 25), 2),
            language=random.choice(["fi"] * 8 + ["sv", "en"]),
            limit_raised_recently=risky,
            late_night_share=random.uniform(0.3, 0.6) if risky else random.uniform(0, 0.1),
            deposit_speed_up=random.uniform(1.5, 2) if risky else 1.0,
            chasing_losses=risky and random.random() < 0.7,
            messages_this_week=random.randint(0, 3),
        ))
    return out


def run() -> None:
    players = make_players()
    a1, a2, rg = Player360Agent(), PredictiveScoringAgent(), RGGuardianAgent()
    orch, cp, pers = JourneyOrchestratorAgent(), ContactPolicyAgent(), PersonalisationAgent()
    opt = OptimisationAgent(["push@evening", "push@morning", "email@evening", "email@morning"])
    up, ins, trig = UpliftAgent(), InsightsCalendarAgent(), RealTimeTriggerAgent()

    sent = 0
    for p in players:
        a2.run(p, rg)                      # score first (includes RG score)
        a1.run(p)                          # then segment
        arm = opt.choose()
        msgs = orch.plan(p, arm.split("@")[0])
        msgs = [m2 for m in msgs if (m2 := rg.review(p, m))]   # gatekeeper 1
        msgs = cp.filter(p, msgs)                               # gatekeeper 2
        for m in msgs:
            if m.kind == "promo":
                control = up.assign(m.journey, p)
                base = 0.25 if m.journey == "winback_journey" else 0.15
                lift = 0.0 if control else (0.05 if "evening" in arm else 0.03)
                converted = random.random() < base + lift
                up.record(m.journey, control, int(converted))
                if not control:
                    opt.update(arm, converted)
                    pers.render(p, m, "€70M")
                    sent += 1
            else:
                sent += 1

    # real-time trigger: jackpot crosses threshold
    digital = [p for p in players if p.channel == "digital"][:50]
    trig_sent = trig.on_event("Eurojackpot €70M", digital, rg, cp)
    sent += len(trig_sent)

    vetoes = sum(1 for e in AUDIT_LOG if e["decision"].startswith("VETO"))
    reports = [up.report(j) for j in up.results]
    print(ins.weekly_summary(reports, vetoes, sent))
    print("\nBandit state:", {a: s for a, s in opt.stats.items()})
    promos_to_risky = sum(1 for p in players if p.rg_score >= rg.HIGH
                          and p.next_best_action != "care_message")
    print(f"At-risk players sent promotions: {promos_to_risky} (target 0)")

    with open("audit_log.json", "w") as f:
        json.dump(AUDIT_LOG, f, indent=1)
    print(f"Audit log: {len(AUDIT_LOG)} decisions written to audit_log.json")


if __name__ == "__main__":
    run()
