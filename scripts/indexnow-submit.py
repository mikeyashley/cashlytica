#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"
INDEXNOW_URL = "https://api.indexnow.org/indexnow"


def load_urls() -> list[str]:
    if SITEMAP.exists():
        urls = re.findall(r"<loc>(.*?)</loc>", SITEMAP.read_text(encoding="utf-8"))
        if urls:
            return list(dict.fromkeys(urls))
    base = os.environ["SITE_BASE"].rstrip("/")
    return [f"{base}/"]


def main() -> None:
    key = os.environ["INDEXNOW_KEY"]
    host = os.environ["SITE_HOST"]
    base = os.environ["SITE_BASE"].rstrip("/")
    urls = load_urls()

    payload = json.dumps(
        {
            "host": host,
            "key": key,
            "keyLocation": f"{base}/{key}.txt",
            "urlList": urls,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        INDEXNOW_URL,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        print(f"IndexNow response: {response.status} -- {len(urls)} URLs submitted")


if __name__ == "__main__":
    main()
