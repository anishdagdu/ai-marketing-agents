"""Agents 6-10: search visibility and site health.
Data source order: Ahrefs API token -> Ahrefs Webmaster Tools CSV export -> free built-in crawler / GSC export."""
import json
import os
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date

from .common import (result, skipped, read_csv, col, num, ahrefs_api, data_path)
from .crawler import crawl

_crawl_cache = {}


def _crawl(cfg):
    if "c" not in _crawl_cache:
        _crawl_cache["c"] = crawl(cfg["site"], cfg.get("max_crawl_pages", 200))
    return _crawl_cache["c"]


def agent_06_site_health(cfg, prev=None):
    """Site-wide health score (0-100): share of crawled pages with no critical issue."""
    rows = read_csv(data_path(cfg, "ahrefs_site_audit"))
    if rows:  # Ahrefs Site Audit export of pages with issues
        bad = {col(r, "url", "page url", "address") for r in rows
               if (col(r, "importance", "severity", "issue type") or "").lower() in ("error", "critical")}
        total = cfg.get("ahrefs_total_pages") or max(len(rows), 1)
        source = "Ahrefs Site Audit export"
    else:
        pages = _crawl(cfg)["pages"]
        if not pages:
            return skipped(6, "Site health score", "Could not crawl " + cfg["site"], "SEO")
        bad = {p["url"] for p in pages if p["status"] >= 400 or p["status"] == 0 or not p["title"]}
        total = len(pages)
        source = "built-in crawler ({} pages)".format(total)
    score = round(100 * (1 - len(bad) / total)) if total else 0
    status = "pass" if score >= 90 else ("warn" if score >= 75 else "fail")
    findings = ["Source: " + source, "{} of {} pages have a critical issue".format(len(bad), total)] + sorted(bad)[:10]
    return result(6, "Site health score", status, "Health Score", score, ">= 90", findings,
                  [] if status == "pass" else ["Clear critical errors first (see agent 7 for the detailed list)"], "SEO")


def agent_07_crawl_integrity(cfg, prev=None):
    """Broken pages, redirect chains, duplicate/missing titles and orphan pages."""
    c = _crawl(cfg)
    pages = c["pages"]
    if not pages:
        return skipped(7, "Crawl budget & link equity", "Could not crawl " + cfg["site"], "SEO + Engineering")
    broken = [p for p in pages if p["status"] >= 400 or p["status"] == 0]
    chains = [p for p in pages if p["redirect_hops"] > 1]
    no_title = [p for p in pages if p["status"] == 200 and not p["title"]]
    no_desc = [p for p in pages if p["status"] == 200 and not p["meta_description"]]
    dup = {t: n for t, n in Counter(p["title"] for p in pages if p["title"] and p["status"] == 200).items() if n > 1}
    findings = (
        ["Broken ({}): ".format(p["status"]) + p["url"] for p in broken[:10]]
        + ["Redirect chain ({} hops): {}".format(p["redirect_hops"], p["url"]) for p in chains[:10]]
        + ["Missing title: " + p["url"] for p in no_title[:5]]
        + ["Duplicate title x{}: {}".format(n, t) for t, n in list(dup.items())[:5]]
        + ["Orphan page (in sitemap, no internal links): " + u for u in c["orphans"][:10]]
        + ["{} pages missing meta description".format(len(no_desc))]
    )
    critical = len(broken) + len(chains)
    status = "pass" if critical == 0 and not c["orphans"] else ("warn" if critical <= 3 else "fail")
    actions = []
    if broken:
        actions.append("Redirect or restore {} broken URLs".format(len(broken)))
    if chains:
        actions.append("Point {} redirect chains straight at the final URL".format(len(chains)))
    if c["orphans"]:
        actions.append("Add internal links to {} orphan pages".format(len(c["orphans"])))
    return result(7, "Crawl budget & link equity", status, "Broken pages + redirect chains", critical, "0",
                  findings, actions, "SEO + Engineering")


def agent_08_striking_distance(cfg, prev=None):
    """Keywords ranking in positions 4-15: the cheapest traffic wins."""
    lo, hi = cfg.get("striking_distance", [4, 15])
    rows = read_csv(data_path(cfg, "ahrefs_organic_keywords")) or read_csv(data_path(cfg, "gsc_queries"))
    if not rows:
        api = ahrefs_api("site-explorer/organic-keywords", {
            "target": cfg["site"], "date": date.today().isoformat(), "country": cfg.get("country", "us"),
            "select": "keyword,best_position,volume,sum_traffic,best_position_url", "limit": 1000})
        rows = [{"keyword": r.get("keyword"), "position": r.get("best_position"), "volume": r.get("volume"),
                 "url": r.get("best_position_url")} for r in (api or {}).get("keywords", [])]
    if not rows:
        return skipped(8, "Striking-distance keywords",
                       "Add an Ahrefs 'Organic keywords' or Search Console 'Queries' CSV to data/ (see README)",
                       "SEO + Content")
    kws = []
    for r in rows:
        pos = num(col(r, "position", "current position", "best_position", "avg. position"), 999)
        vol = num(col(r, "volume", "search volume", "impressions"))
        kw = col(r, "keyword", "top queries", "query")
        if kw and lo <= pos <= hi:
            kws.append((kw, pos, vol, col(r, "url", "current url", "best_position_url") or ""))
    top3 = sum(1 for r in rows if num(col(r, "position", "current position", "best_position", "avg. position"), 999) <= 3)
    kws.sort(key=lambda k: -k[2])
    findings = ["Keywords in top 3: {}".format(top3)] + \
               ["'{}' - pos {:.0f}, volume {:.0f} {}".format(k, p, v, u) for k, p, v, u in kws[:15]]
    actions = ["Refresh content + add internal links to the page ranking for '{}'".format(k) for k, *_ in kws[:5]]
    return result(8, "Striking-distance keywords", "warn" if kws else "pass",
                  "Keywords in pos {}-{}".format(lo, hi), len(kws), "Move 5/month into top 3", findings, actions,
                  "SEO + Content")


def agent_09_backlinks(cfg, prev=None):
    """Referring-domain growth, lost high-value links and suspicious domains."""
    rows = read_csv(data_path(cfg, "ahrefs_referring_domains"))
    if not rows:
        api = ahrefs_api("site-explorer/refdomains", {
            "target": cfg["site"], "select": "domain,domain_rating,dofollow_links", "limit": 1000})
        rows = [{"domain": r.get("domain"), "dr": r.get("domain_rating")} for r in (api or {}).get("refdomains", [])]
    if not rows:
        return skipped(9, "Backlink authority", "Add an Ahrefs 'Referring domains' CSV to data/ (see README)", "SEO + PR")
    doms = {}
    for r in rows:
        d = col(r, "domain", "referring domain")
        if d:
            doms[d] = num(col(r, "dr", "domain rating", "domain_rating"))
    prev_doms = {}
    if prev:
        for a in prev.get("agents", []):
            if a["id"] == 9:
                prev_doms = a.get("raw", {}).get("domains", {})
    new = sorted(set(doms) - set(prev_doms))
    lost = sorted(set(prev_doms) - set(doms), key=lambda d: -prev_doms[d])
    lost_valuable = [d for d in lost if prev_doms[d] >= 50]
    low_quality = sorted(d for d, dr in doms.items() if dr < 5)
    net = len(new) - len(lost)
    status = "fail" if lost_valuable else ("pass" if net >= 0 else "warn")
    findings = ["Referring domains: {} (net {:+d} since last run)".format(len(doms), net)] + \
               ["New: " + d for d in new[:10]] + \
               ["Lost (DR {:.0f}): {}".format(prev_doms[d], d) for d in lost[:10]] + \
               ["{} domains with DR < 5 - review for spam".format(len(low_quality))]
    actions = ["Reach out to reclaim link from " + d for d in lost_valuable[:5]]
    out = result(9, "Backlink authority", status, "Referring domains (net new)", "{} ({:+d})".format(len(doms), net),
                 "Net growth monthly", findings, actions, "SEO + PR")
    out["raw"] = {"domains": doms}
    return out


def agent_10_alerts(cfg, current, prev=None):
    """Compares this run with the last one and raises alerts. Optional Slack webhook."""
    alerts = []
    revenue = {u.rstrip("/") for u in cfg["revenue_pages"]}
    for p in _crawl(cfg)["pages"]:
        if p["noindex"] and p["url"].rstrip("/") in revenue:
            alerts.append("CRITICAL: revenue page set to noindex - " + p["url"])
        if p["url"].rstrip("/") in revenue and p["status"] >= 400:
            alerts.append("CRITICAL: revenue page returns {} - {}".format(p["status"], p["url"]))
    rank = {"pass": 0, "warn": 1, "fail": 2, "skipped": -1}
    if prev:
        old = {a["id"]: a for a in prev.get("agents", [])}
        for a in current:
            o = old.get(a["id"])
            if o and rank[a["status"]] > rank.get(o["status"], -1) >= 0:
                alerts.append("{} got worse: {} -> {} ({} {} -> {})".format(
                    a["name"], o["status"], a["status"], a["kpi"], o["value"], a["value"]))
    else:
        alerts.append("First run - baseline saved. Alerts start from the next run.")
    status = "fail" if any(a.startswith("CRITICAL") for a in alerts) else ("warn" if len(alerts) > 1 or (prev and alerts) else "pass")
    hook = os.environ.get("SLACK_WEBHOOK_URL")
    if hook and alerts and prev:
        try:
            body = json.dumps({"text": "Website audit alerts for {}:\n- ".format(cfg["site"]) + "\n- ".join(alerts)}).encode()
            urllib.request.urlopen(urllib.request.Request(hook, data=body, headers={"Content-Type": "application/json"}), timeout=15)
        except Exception as e:
            alerts.append("Slack alert failed: " + str(e))
    return result(10, "Early-warning alerts", status, "Open alerts", len(alerts), "0", alerts or ["No regressions"],
                  ["Investigate alerts within 7 days"] if alerts and prev else [], "Marketing Ops")


AGENTS = [agent_06_site_health, agent_07_crawl_integrity, agent_08_striking_distance, agent_09_backlinks]
