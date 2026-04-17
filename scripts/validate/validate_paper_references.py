#!/usr/bin/env python3
"""Validate URLs in paper reference sections."""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPERS = [
    ROOT / "papers/recoverability_paper_final.md",
    ROOT / "papers/mhd_paper_upgraded.md",
    ROOT / "papers/bridge_paper.md",
    ROOT / "papers/ocp_core_paper.md",
]
OUT = ROOT / "data/generated/validations/paper_reference_validation.json"

MD_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
PLAIN_URL_RE = re.compile(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+")
DOI_RE = re.compile(r"10\.[0-9]{4,9}/[-._;()/:A-Za-z0-9]+")


def check_url(url: str, timeout: float = 12.0) -> dict[str, object]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (ReferenceValidationBot/1.0)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = getattr(resp, "status", 200)
            return {"ok": int(status) < 400, "status": int(status)}
    except urllib.error.HTTPError as e:
        if "doi.org" in url and int(e.code) == 403:
            return {"ok": True, "status": int(e.code), "note": "doi resolver blocked automated request"}
        return {"ok": False, "status": int(e.code), "error": str(e)}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "status": None, "error": str(e)}


def main() -> None:
    urls: dict[str, list[str]] = {}
    dois: dict[str, list[str]] = {}
    for paper in PAPERS:
        text = paper.read_text(encoding="utf-8")
        md_urls = MD_LINK_RE.findall(text)
        plain_urls = PLAIN_URL_RE.findall(text)
        cleaned = []
        for u in md_urls + plain_urls:
            cleaned.append(u.rstrip(".,;:"))
        found = sorted(set(cleaned))
        urls[str(paper)] = found
        doi_found = sorted(set(d.rstrip(".,;:") for d in DOI_RE.findall(text)))
        dois[str(paper)] = doi_found

    results: dict[str, object] = {}
    doi_results: dict[str, object] = {}
    failing: list[dict[str, object]] = []
    doi_failing: list[dict[str, object]] = []

    for paper, paper_urls in urls.items():
        paper_results = []
        for url in paper_urls:
            res = check_url(url)
            entry = {"url": url, **res}
            paper_results.append(entry)
            if not res["ok"]:
                failing.append({"paper": paper, **entry})
        results[paper] = paper_results

    for paper, paper_dois in dois.items():
        paper_results = []
        for doi in paper_dois:
            res = check_url(f"https://doi.org/{doi}")
            entry = {"doi": doi, **res}
            paper_results.append(entry)
            if not res["ok"]:
                doi_failing.append({"paper": paper, **entry})
        doi_results[paper] = paper_results

    summary = {
        "papers_checked": len(PAPERS),
        "total_urls": sum(len(v) for v in urls.values()),
        "failing_count": len(failing),
        "failing": failing,
        "total_dois": sum(len(v) for v in dois.values()),
        "doi_failing_count": len(doi_failing),
        "doi_failing": doi_failing,
    }

    payload = {"summary": summary, "results": results, "doi_results": doi_results}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
