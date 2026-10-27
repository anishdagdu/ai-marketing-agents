"""Agents 1-5: speed, experience and compliance, powered by Google PageSpeed Insights (free)."""
from .common import pagespeed, psi_score, psi_audit, result, skipped

FIELD_METRICS = {
    "LARGEST_CONTENTFUL_PAINT_MS": ("LCP", 2500),
    "INTERACTION_TO_NEXT_PAINT": ("INP", 200),
    "CUMULATIVE_LAYOUT_SHIFT_SCORE": ("CLS", 10),  # CrUX reports CLS x100
}


def _pages(cfg):
    return cfg["revenue_pages"]


def _psi_errors(cfg, agent_id, name, owner):
    """If PageSpeed failed for every page, return a 'skipped' result explaining why."""
    errs = [pagespeed(u).get("error") for u in _pages(cfg)]
    if all(errs):
        return skipped(agent_id, name, "PageSpeed API error: " + errs[0], owner)
    return None


def _guard(agent_id, name, owner):
    def wrap(fn):
        def inner(cfg):
            return _psi_errors(cfg, agent_id, name, owner) or fn(cfg)
        inner.__name__ = fn.__name__
        inner.__doc__ = fn.__doc__
        return inner
    return wrap


def agent_01_cwv_baseline(cfg):
    """Share of revenue pages passing Core Web Vitals on real-user (field) data."""
    rows, passed, measured = [], 0, 0
    for url in _pages(cfg):
        d = pagespeed(url)
        field = d.get("loadingExperience", {})
        cat = field.get("overall_category")
        if cat is None or not field.get("metrics"):
            rows.append(url + ": no real-user data (low Chrome traffic); lab score only = "
                        + str(psi_score(d, "performance")))
            continue
        measured += 1
        ok = cat == "FAST"
        passed += ok
        parts = []
        for key, (label, _) in FIELD_METRICS.items():
            m = field["metrics"].get(key)
            if m:
                v = m["percentile"] / (100 if label == "CLS" else 1)
                parts.append("{}={}".format(label, v) + ("" if m["category"] == "FAST" else " (" + m["category"] + ")"))
        rows.append("{}: {} - {}".format(url, "PASS" if ok else "FAIL", ", ".join(parts)))
    if measured == 0:
        return result(1, "Core Web Vitals baseline", "warn", "% pages passing CWV (field)", "n/a", ">= 75%",
                      rows, ["Site lacks Chrome UX data; track lab scores until traffic grows"], "Engineering")
    pct = round(100 * passed / measured)
    status = "pass" if pct >= 75 else ("warn" if pct >= 50 else "fail")
    actions = [] if status == "pass" else ["Fix failing pages first, starting with the highest-revenue page"]
    return result(1, "Core Web Vitals baseline", status, "% pages passing CWV (field)", str(pct) + "%",
                  ">= 75%", rows, actions, "Engineering")


def agent_02_conversion_leakage(cfg):
    """Flags revenue pages where mobile LCP is slow enough to lose visitors before they see the offer."""
    slow, findings = [], []
    for url in _pages(cfg):
        d = pagespeed(url)
        lcp = psi_audit(d, "largest-contentful-paint").get("numericValue")
        if lcp is None:
            findings.append(url + ": could not measure")
            continue
        s = round(lcp / 1000, 2)
        findings.append("{}: mobile LCP {}s".format(url, s))
        if s > 2.5:
            slow.append((url, s))
    status = "pass" if not slow else ("warn" if all(s <= 4 for _, s in slow) else "fail")
    actions = ["{} loads in {}s - compare its GA4 bounce/conversion rate with fast pages to size the revenue loss".format(u, s)
               for u, s in slow]
    return result(2, "Conversion leakage from slow loads", status, "Revenue pages with LCP > 2.5s",
                  "{}/{}".format(len(slow), len(_pages(cfg))), "0", findings, actions, "Engineering + Growth")


def agent_03_speed_backlog(cfg):
    """Builds a ranked engineering backlog from Lighthouse 'opportunities' across all revenue pages."""
    totals = {}
    for url in _pages(cfg):
        audits = pagespeed(url).get("lighthouseResult", {}).get("audits", {})
        for aid, a in audits.items():
            det = a.get("details") or {}
            ms = det.get("overallSavingsMs") or 0
            if det.get("type") == "opportunity" and ms > 0:
                t = totals.setdefault(aid, {"title": a.get("title", aid), "ms": 0, "pages": 0})
                t["ms"] += ms
                t["pages"] += 1
    ranked = sorted(totals.values(), key=lambda t: -t["ms"])
    findings = ["{} - saves ~{:.1f}s across {} page(s)".format(t["title"], t["ms"] / 1000, t["pages"]) for t in ranked[:10]]
    total_s = sum(t["ms"] for t in ranked) / 1000
    status = "pass" if total_s < 1 else ("warn" if total_s < 5 else "fail")
    actions = ["Sprint ticket: " + t["title"] for t in ranked[:3]]
    return result(3, "Speed fix backlog", status, "Total potential time saved", "{:.1f}s".format(total_s),
                  "< 1s", findings or ["No major opportunities found"], actions, "Engineering")


def agent_04_tag_bloat(cfg):
    """Finds third-party scripts (pixels, chat, heatmaps) slowing the main thread."""
    vendors = {}
    worst_block = 0
    for url in _pages(cfg):
        a = psi_audit(pagespeed(url), "third-party-summary")
        block = (a.get("details") or {}).get("summary", {}).get("wastedMs", 0) or 0
        worst_block = max(worst_block, block)
        for item in (a.get("details") or {}).get("items", []):
            ent = item.get("entity")
            name = ent.get("text") if isinstance(ent, dict) else (ent or "unknown")
            v = vendors.setdefault(name, {"block": 0, "kb": 0})
            v["block"] = max(v["block"], item.get("blockingTime", 0) or 0)
            v["kb"] = max(v["kb"], (item.get("transferSize", 0) or 0) / 1024)
    ranked = sorted(vendors.items(), key=lambda kv: -kv[1]["block"])
    findings = ["{}: {:.0f}ms blocking, {:.0f}KB".format(n, v["block"], v["kb"]) for n, v in ranked[:10]]
    status = "pass" if worst_block < 250 else ("warn" if worst_block < 600 else "fail")
    actions = ["Review in GTM: remove, delay or load '{}' after user interaction".format(n)
               for n, v in ranked[:3] if v["block"] > 50]
    return result(4, "Marketing tag bloat", status, "Worst third-party blocking time", "{:.0f}ms".format(worst_block),
                  "< 250ms", findings or ["No third-party scripts detected"], actions, "Marketing Ops")


def agent_05_accessibility(cfg):
    """Accessibility score + top failing checks (ADA / European Accessibility Act exposure)."""
    scores, issues = [], {}
    for url in _pages(cfg):
        d = pagespeed(url)
        s = psi_score(d, "accessibility")
        if s is not None:
            scores.append((url, s))
        lh = d.get("lighthouseResult", {})
        refs = lh.get("categories", {}).get("accessibility", {}).get("auditRefs", [])
        for ref in refs:
            a = lh.get("audits", {}).get(ref["id"], {})
            if a.get("score") == 0:
                issues[a.get("title", ref["id"])] = issues.get(a.get("title", ref["id"]), 0) + 1
    if not scores:
        return skipped(5, "Accessibility & compliance", "PageSpeed returned no data", "Design + Engineering")
    low = min(s for _, s in scores)
    status = "pass" if low >= 90 else ("warn" if low >= 75 else "fail")
    findings = ["{}: {}".format(u, s) for u, s in scores] + \
               ["Fails on {} page(s): {}".format(n, t) for t, n in sorted(issues.items(), key=lambda kv: -kv[1])[:8]]
    actions = ["Fix: " + t for t, _ in sorted(issues.items(), key=lambda kv: -kv[1])[:3]]
    return result(5, "Accessibility & compliance", status, "Lowest accessibility score", low, ">= 90",
                  findings, actions, "Design + Engineering")


AGENTS = [
    _guard(1, "Core Web Vitals baseline", "Engineering")(agent_01_cwv_baseline),
    _guard(2, "Conversion leakage from slow loads", "Engineering + Growth")(agent_02_conversion_leakage),
    _guard(3, "Speed fix backlog", "Engineering")(agent_03_speed_backlog),
    _guard(4, "Marketing tag bloat", "Marketing Ops")(agent_04_tag_bloat),
    _guard(5, "Accessibility & compliance", "Design + Engineering")(agent_05_accessibility),
]
