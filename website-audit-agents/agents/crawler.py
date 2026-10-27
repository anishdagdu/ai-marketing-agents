"""Small free site crawler, used when no Ahrefs Site Audit export is available.
Checks status codes, redirect chains, titles, meta descriptions, noindex and orphan pages."""
import gzip
import re
import urllib.error
import urllib.parse
import urllib.request
from collections import deque

from .common import USER_AGENT


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def _fetch(url):
    """Fetch without following redirects. Returns (status, location, body)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip"})
    try:
        with _opener.open(req, timeout=20) as r:
            ctype = r.headers.get("Content-Type", "")
            raw = r.read(3_000_000) if "html" in ctype or "xml" in ctype else b""
            if raw[:2] == b"\x1f\x8b":  # some servers gzip even when not asked
                raw = gzip.decompress(raw)
            return r.status, None, raw.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location"), ""
    except Exception:
        return 0, None, ""


def resolve(url, max_hops=10):
    """Follow redirects manually so we can count the chain."""
    chain = [url]
    status, loc, body = _fetch(url)
    while status in (301, 302, 303, 307, 308) and loc and len(chain) <= max_hops:
        url = urllib.parse.urljoin(url, loc)
        chain.append(url)
        status, loc, body = _fetch(url)
    return status, chain, body


def sitemap_urls(site, limit):
    urls, todo, seen = [], [site.rstrip("/") + "/sitemap.xml"], set()
    while todo and len(urls) < limit:
        sm = todo.pop()
        if sm in seen:
            continue
        seen.add(sm)
        status, _, body = resolve(sm)
        if status != 200:
            continue
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", body)
        if "<sitemapindex" in body:
            todo.extend(locs)
        else:
            urls.extend(locs)
    return urls[:limit]


def _meta(body, name):
    m = re.search(r'<meta[^>]+name=["\']%s["\'][^>]*content=["\']([^"\']*)' % name, body, re.I) or \
        re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]*name=["\']%s["\']' % name, body, re.I)
    return m.group(1).strip() if m else None


def crawl(site, max_pages=200):
    host = urllib.parse.urlparse(site).netloc
    in_sitemap = sitemap_urls(site, max_pages)
    queue = deque([site] + in_sitemap)
    seen, pages, linked = set(), [], set()
    while queue and len(pages) < max_pages:
        url = queue.popleft().split("#")[0]
        if url in seen:
            continue
        seen.add(url)
        status, chain, body = resolve(url)
        t = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
        robots = (_meta(body, "robots") or "").lower()
        pages.append({
            "url": url, "status": status, "redirect_hops": len(chain) - 1, "final_url": chain[-1],
            "title": re.sub(r"\s+", " ", t.group(1)).strip() if t else None,
            "meta_description": _meta(body, "description"),
            "noindex": "noindex" in robots,
        })
        for href in re.findall(r'<a[^>]+href=["\']([^"\'#]+)', body, re.I):
            link = urllib.parse.urljoin(chain[-1], href).split("#")[0]
            if urllib.parse.urlparse(link).netloc == host:
                linked.add(link.rstrip("/"))
                if link not in seen:
                    queue.append(link)
    orphans = [u for u in in_sitemap if u.rstrip("/") not in linked and u.rstrip("/") != site.rstrip("/")]
    return {"pages": pages, "orphans": orphans, "sitemap_count": len(in_sitemap)}
