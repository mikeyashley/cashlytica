#!/usr/bin/env python3
"""Local dev server with SSI support for Cashlytica."""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = Path(__file__).resolve().parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8035
APP_ORIGIN = os.environ.get('CASHLYTICA_APP_ORIGIN', 'http://localhost:5173')
INCLUDE_RE = re.compile(r'<!--#include\s+virtual=["\']([^"\']+)["\']\s*-->')
PLACEHOLDER_RE = re.compile(r'\{\{APP_ORIGIN\}\}')


def render(path: Path, seen: set[Path] | None = None) -> str:
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
            return f'<!-- SSI not found: {rel} -->'
        return render(included, seen.copy())

    text = INCLUDE_RE.sub(repl, text)
    text = PLACEHOLDER_RE.sub(APP_ORIGIN, text)
    return text


class Handler(SimpleHTTPRequestHandler):
    def _resolve(self):
        path = self.path.split('?', 1)[0]
        fs_path = ROOT / path.lstrip('/')
        if fs_path.is_dir():
            fs_path = fs_path / 'index.html'
        return fs_path

    def _serve_html(self, include_body: bool):
        fs_path = self._resolve()
        if fs_path.suffix == '.html' and fs_path.is_file():
            body = render(fs_path).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            if include_body:
                self.wfile.write(body)
            return True
        return False

    def do_GET(self):
        if not self._serve_html(include_body=True):
            super().do_GET()

    def do_HEAD(self):
        if not self._serve_html(include_body=False):
            super().do_HEAD()

    def log_message(self, format, *args):
        print(f'  {self.address_string()} {format % args}')


if __name__ == '__main__':
    os.chdir(ROOT)
    print(f'Cashlytica dev server → http://localhost:{PORT}')
    HTTPServer(('', PORT), Handler).serve_forever()
