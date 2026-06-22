#!/usr/bin/env python3
"""Render Cashlytica SSI source into a temporary deploy tree."""
from __future__ import annotations

import argparse
import os
import re
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_ORIGIN = os.environ.get('CASHLYTICA_APP_ORIGIN', 'http://localhost:5173')
INCLUDE_RE = re.compile(r'<!--#include\s+virtual=["\']([^"\']+)["\']\s*-->')
PLACEHOLDER_RE = re.compile(r'\{\{APP_ORIGIN\}\}')
SKIP_DIRS = {'.git', '.github', '__pycache__', 'scripts'}
SKIP_FILES = {'build.py', 'serve.py', 'NORMS.md'}


def in_skipped_dir(path: Path, out_root: Path | None = None) -> bool:
    rel = path if isinstance(path, Path) else Path(path)
    if any(part in SKIP_DIRS for part in rel.parts):
        return True
    if out_root is not None:
        try:
            return path.resolve().is_relative_to(out_root.resolve())
        except Exception:
            return False
    return False


def expand(path: Path, seen: set[Path] | None = None) -> str:
    seen = seen or set()
    path = path.resolve()
    if path in seen:
        raise RuntimeError(f'Circular include detected: {path}')
    seen.add(path)
    text = path.read_text(encoding='utf-8')

    def repl(match: re.Match[str]) -> str:
        rel = match.group(1).lstrip('/')
        included = (ROOT / rel).resolve()
        if not included.exists():
            raise FileNotFoundError(f'Missing include: {rel} from {path}')
        return expand(included, seen.copy())

    text = INCLUDE_RE.sub(repl, text)
    text = PLACEHOLDER_RE.sub(APP_ORIGIN, text)
    return text


def url_for_rel(rel: Path) -> str:
    rel_str = rel.as_posix()
    if rel_str == 'index.html':
        return 'https://cashlytica.com/'
    if rel_str.endswith('/index.html'):
        return 'https://cashlytica.com/' + rel_str[:-len('index.html')]
    return 'https://cashlytica.com/' + rel_str


def render_html_sources(out_root: Path) -> list[str]:
    urls: list[str] = []
    for path in sorted(ROOT.rglob('*.html')):
        rel = path.relative_to(ROOT)
        if in_skipped_dir(rel, out_root=out_root):
            continue
        if path.parent.name == 'shared':
            continue
        out = out_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(expand(path), encoding='utf-8')
        urls.append(url_for_rel(rel))
    return urls


def copy_assets(out_root: Path) -> None:
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT)
        if in_skipped_dir(rel, out_root=out_root):
            continue
        if path.is_dir():
            continue
        if path.suffix == '.html' or path.name in SKIP_FILES:
            continue
        if rel.parts and rel.parts[0] == 'shared' and path.suffix == '.html':
            continue
        out = out_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, out)


def write_sitemap(out_root: Path, urls: list[str]) -> None:
    unique = sorted(set(urls))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in unique:
        priority = '1.0' if url == 'https://cashlytica.com/' else '0.8'
        lines.append(f'  <url><loc>{url}</loc><changefreq>monthly</changefreq><priority>{priority}</priority></url>')
    lines.append('</urlset>')
    (out_root / 'sitemap.xml').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def write_robots(out_root: Path) -> None:
    (out_root / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://cashlytica.com/sitemap.xml\n', encoding='utf-8')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Render Cashlytica site source into a deploy tree.')
    parser.add_argument('outdir', nargs='?', help='Output directory for rendered site')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.outdir:
        out_root = Path(args.outdir).expanduser().resolve()
        if out_root.exists():
            shutil.rmtree(out_root)
        out_root.mkdir(parents=True, exist_ok=True)
    else:
        out_root = Path(tempfile.mkdtemp(prefix='cashlytica-site-'))
    urls = render_html_sources(out_root)
    copy_assets(out_root)
    write_sitemap(out_root, urls)
    write_robots(out_root)
    print(f'Built {len(urls)} HTML pages into {out_root}')


if __name__ == '__main__':
    main()
