"""Uplift vs control with a 95% confidence interval.

Usage: python3 uplift.py results.csv [--min-lift 2]
CSV columns: group (treatment|control), converted (0/1), optional revenue, cost
"""
import argparse
import csv
import math


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--min-lift", type=float, help="lift in points to size a test for")
    args = ap.parse_args()

    g = {"treatment": {"n": 0, "conv": 0, "rev": 0.0}, "control": {"n": 0, "conv": 0, "rev": 0.0}}
    cost = 0.0
    with open(args.csv, newline="") as f:
        for row in csv.DictReader(f):
            k = row["group"].strip().lower()
            if k not in g:
                continue
            g[k]["n"] += 1
            g[k]["conv"] += int(float(row.get("converted") or 0))
            g[k]["rev"] += float(row.get("revenue") or 0)
            cost += float(row.get("cost") or 0)

    t, c = g["treatment"], g["control"]
    if not t["n"] or not c["n"]:
        raise SystemExit("Need both treatment and control rows.")
    pt, pc = t["conv"] / t["n"], c["conv"] / c["n"]
    se = math.sqrt(pt * (1 - pt) / t["n"] + pc * (1 - pc) / c["n"])
    lift = (pt - pc) * 100
    lo, hi = lift - 196 * se, lift + 196 * se
    inc_players = (pt - pc) * t["n"]
    inc_rev = (t["rev"] / t["n"] - c["rev"] / c["n"]) * t["n"]

    print(f"Treated: {t['n']}  Control: {c['n']}")
    print(f"Conversion: treatment {pt:.1%}  control {pc:.1%}")
    print(f"Uplift: {lift:+.1f} pts  (95% CI {lo:+.1f} to {hi:+.1f})")
    print(f"Incremental players: {inc_players:.0f}")
    print(f"Incremental revenue: {inc_rev:,.0f}")
    if cost and inc_players > 0:
        print(f"Cost per incremental player: {cost / inc_players:,.2f}")
    if lo > 0:
        print("Verdict: significant win. Keep it")
    elif hi < 0:
        print("Verdict: hurts results. Stop now")
    else:
        print("Verdict: not significant yet")

    if args.min_lift:
        d = args.min_lift / 100
        p = pc
        n = math.ceil((1.96 + 0.84) ** 2 * 2 * p * (1 - p) / d ** 2)
        print(f"Players needed per group to detect {args.min_lift:+.1f} pts (80% power): {n}")


if __name__ == "__main__":
    main()
