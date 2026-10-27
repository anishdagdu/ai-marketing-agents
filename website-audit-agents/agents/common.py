"""Shared helpers: config, HTTP, data sources and the result format every agent returns."""
import csv
import json
import os
import urllib.parse
import urllib.request
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_AGENT = "website-audit-agents/1.0 (+https://github.com)"


def load_config(path=None):
    path = path or os.path.join(ROOT, "config.json")
    with open(path) as f:
        return json.load(f)


def http_get(url, headers=None, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "replace")


def http_post_json(url, payload, headers=None, timeout=120):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"Content-Type": "application/json", **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def result(agent_id, name, status, kpi, value, target, findings, actions, owner):
    """Standard output for every agent. status: pass | warn | fail | skipped."""
    return {
        "id": agent_id, "name": name, "status": status, "kpi": kpi,
        "value": value, "target": target, "findings": findings,
        "actions": actions, "owner": owner, "date": date.today().isoformat(),
    }


def skipped(agent_id, name, reason, owner):
    return result(agent_id, name, "skipped", "-", None, "-", [reason], [], owner)


# ---------- PageSpeed Insights (free) ----------

PSI_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
_psi_cache = {}


def pagespeed(url, strategy="mobile"):
    """One PSI call returns performance, accessibility, SEO, best-practices and field data.
    Cached so the five PageSpeed agents share a single call per URL."""
    key = (url, strategy)
    if key in _psi_cache:
        return _psi_cache[key]
    params = [("url", url), ("strategy", strategy)]
    for c in ("performance", "accessibility", "seo", "best-practices"):
        params.append(("category", c))
    api_key = os.environ.get("PAGESPEED_API_KEY")
    if api_key:
        params.append(("key", api_key))
    try:
        _, body = http_get(PSI_URL + "?" + urllib.parse.urlencode(params), timeout=120)
        data = json.loads(body)
    except Exception as e:  # keep the pipeline running if one URL fails
        msg = str(e)
        if "429" in msg and not api_key:
            msg += " - set a free PAGESPEED_API_KEY (see README)"
        data = {"error": msg}
    _psi_cache[key] = data
    return data


def psi_score(data, category):
    try:
        return round(data["lighthouseResult"]["categories"][category]["score"] * 100)
    except (KeyError, TypeError):
        return None


def psi_audit(data, audit_id):
    return data.get("lighthouseResult", {}).get("audits", {}).get(audit_id, {})


# ---------- Ahrefs (Webmaster Tools exports, or API token) ----------

def read_csv(path):
    """Read an Ahrefs/GSC CSV export. Ahrefs exports are often UTF-16 with tabs."""
    if not os.path.exists(path):
        return None
    for enc in ("utf-8-sig", "utf-16"):
        try:
            with open(path, encoding=enc, newline="") as f:
                sample = f.read(4096)
                f.seek(0)
                delim = "\t" if sample.count("\t") > sample.count(",") else ","
                return [{k.strip().lower(): (v or "").strip() for k, v in row.items() if k}
                        for row in csv.DictReader(f, delimiter=delim)]
        except UnicodeError:
            continue
    return None


def col(row, *names):
    """Find a column by any of several possible header names."""
    for n in names:
        if n in row and row[n] != "":
            return row[n]
    return None


def num(v, default=0.0):
    try:
        return float(str(v).replace(",", ""))
    except (TypeError, ValueError):
        return default


def ahrefs_api(endpoint, params):
    """Ahrefs API v3. Needs AHREFS_API_TOKEN (API access is a paid Ahrefs add-on).
    Returns None when no token is set, so agents fall back to CSV exports."""
    token = os.environ.get("AHREFS_API_TOKEN")
    if not token:
        return None
    url = "https://api.ahrefs.com/v3/" + endpoint + "?" + urllib.parse.urlencode(params)
    try:
        _, body = http_get(url, headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
        return json.loads(body)
    except Exception as e:
        return {"error": str(e)}


def data_path(cfg, key):
    return os.path.join(ROOT, cfg["data_dir"], cfg["exports"][key])
