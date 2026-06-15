from pathlib import Path
from html import escape
import os, json, re

ROOT = Path('/Users/michael/Documents/GitHub/cashlytica')
BASE_URL = 'https://cashlytica.com'
BRAND = 'Cashlytica'
# Frontend application origin for auth handoff pages.
# Default local preview points at the Vite app on 5173; override for production builds.
APP_ORIGIN = os.environ.get('CASHLYTICA_APP_ORIGIN', 'http://localhost:5173')

def app_url(path: str) -> str:
    return f'{APP_ORIGIN}{path}' if APP_ORIGIN else path

NAV_ITEMS = [
    ('Home', '/'),
    ('Learn', '/learn/'),
    ('Tools', '/tools/'),
    ('Samples', '/samples/'),
    ('Compare', '/compare/'),
    ('Use cases', '/use-cases/'),
    ('For', '/for/'),
    ('Security', '/security/'),
    ('FAQ', '/faq/'),
]

FOOTER_GROUPS = [
    ('Explore', [('Home','/'),('Learn','/learn/'),('Tools','/tools/'),('Samples','/samples/'),('Compare','/compare/')]),
    ('Buyers', [('Use cases','/use-cases/'),('For CFOs','/for/cfos/'),('For controllers','/for/controllers/'),('For founders','/for/founders/')]),
    ('Trust', [('Security','/security/'),('FAQ','/faq/'),('Get started',app_url('/register/')),('Log in',app_url('/login/'))]),
]


def norm_path(rel_path: str) -> str:
    rel_path = rel_path.replace('\\', '/')
    if rel_path == 'index.html':
        return '/'
    if rel_path.endswith('/index.html'):
        return '/' + rel_path[:-len('index.html')]
    return '/' + rel_path


def canonical_url(rel_path: str) -> str:
    return BASE_URL + norm_path(rel_path)


def og_name(rel_path: str) -> str:
    p = norm_path(rel_path).strip('/')
    if not p:
        return 'home'
    return re.sub(r'[^a-z0-9]+', '-', p.lower()).strip('-')


def svg_for(title: str, subtitle: str) -> str:
    t = escape(title[:70])
    s = escape(subtitle[:120])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#12263b"/>
      <stop offset="55%" stop-color="#274b6b"/>
      <stop offset="100%" stop-color="#5b7ea6"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#g)"/>
  <rect x="70" y="70" width="1060" height="490" rx="42" fill="#ffffff" opacity="0.08" stroke="#ffffff" stroke-opacity="0.14"/>
  <text x="108" y="155" fill="#dce7f3" font-size="30" font-family="Inter, Arial, sans-serif" letter-spacing="4">CASHLYTICA</text>
  <text x="108" y="255" fill="#ffffff" font-size="66" font-weight="800" font-family="Inter, Arial, sans-serif">{t}</text>
  <text x="108" y="330" fill="#dce7f3" font-size="34" font-family="Inter, Arial, sans-serif">{s}</text>
  <rect x="108" y="395" width="220" height="54" rx="27" fill="#dce7f3" opacity="0.96"/>
  <text x="218" y="430" text-anchor="middle" fill="#12263b" font-size="24" font-weight="700" font-family="Inter, Arial, sans-serif">Cashlytica</text>
</svg>'''


def write_og(rel_path: str, title: str, subtitle: str) -> str:
    og_path = ROOT / 'og' / f'{og_name(rel_path)}.svg'
    og_path.parent.mkdir(parents=True, exist_ok=True)
    og_path.write_text(svg_for(title, subtitle), encoding='utf-8')
    return f'{BASE_URL}/og/{og_name(rel_path)}.svg'


def header_html() -> str:
    nav = ''.join(f'<a href="{href}" class="hover:text-slate-900">{label}</a>' for label, href in NAV_ITEMS)
    login_href = app_url('/login/')
    register_href = app_url('/register/')
    return f'''
<header class="sticky top-0 z-20 border-b border-slate-200 bg-white/80 backdrop-blur">
  <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-4 sm:px-6 lg:px-8">
    <a href="/" class="flex items-center gap-3">
      <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-brand-700 text-sm font-black text-white shadow-sm">C</div>
      <div>
        <p class="text-sm font-bold leading-none tracking-tight">Cashlytica</p>
        <p class="text-[10px] font-semibold uppercase tracking-[0.22em] text-slate-400">Treasury intelligence</p>
      </div>
    </a>
    <nav class="hidden flex-wrap items-center gap-5 text-sm font-medium text-slate-500 lg:flex">{nav}</nav>
    <div class="flex items-center gap-2">
      <a href="{login_href}" class="hidden rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm font-semibold hover:border-brand-200 hover:bg-brand-50 sm:inline-flex">Log in</a>
      <a href="{register_href}" class="inline-flex rounded-xl bg-brand-700 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-brand-800">Get started</a>
    </div>
  </div>
</header>'''


def footer_html() -> str:
    cols = []
    for title, links in FOOTER_GROUPS:
        links_html = ''.join(f'<li><a href="{href}" class="hover:text-slate-900">{label}</a></li>' for label, href in links)
        cols.append(f'<div><h3 class="text-sm font-semibold text-slate-900">{title}</h3><ul class="mt-3 space-y-2 text-sm text-slate-500">{links_html}</ul></div>')
    return f'''
<footer class="border-t border-slate-200 bg-white">
  <div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
    <div class="grid gap-8 md:grid-cols-4">
      <div class="md:col-span-1">
        <div class="flex items-center gap-3">
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-brand-700 text-sm font-black text-white shadow-sm">C</div>
          <div>
            <p class="text-sm font-bold leading-none tracking-tight">Cashlytica</p>
            <p class="mt-1 text-xs uppercase tracking-[0.22em] text-slate-400">Treasury intelligence</p>
          </div>
        </div>
        <p class="mt-4 max-w-sm text-sm leading-6 text-slate-500">Traffic, proof, and conversion for finance teams that need to find cash leakage, improve forecasts, and act on idle cash.</p>
      </div>
      {''.join(cols)}
    </div>
    <div class="mt-10 flex flex-wrap items-center justify-between gap-4 border-t border-slate-200 pt-6 text-xs text-slate-400">
      <p>© 2026 Cashlytica. Treasury intelligence for finance teams.</p>
      <p>Public brand: Cashlytica.</p>
    </div>
  </div>
</footer>'''


def shell(rel_path: str, title: str, description: str, body_html: str, og_type: str = 'website', schema=None) -> str:
    canon = canonical_url(rel_path)
    og_image = write_og(rel_path, title, description)
    schema_tag = ''
    if schema:
        schema_tag = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}" />
  <meta name="robots" content="index,follow" />
  <link rel="canonical" href="{canon}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{escape(title)}" />
  <meta property="og:description" content="{escape(description)}" />
  <meta property="og:site_name" content="Cashlytica" />
  <meta property="og:image" content="{og_image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{escape(title)}" />
  <meta name="twitter:description" content="{escape(description)}" />
  <meta name="twitter:image" content="{og_image}" />
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-W1L7GJDSHX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{ dataLayer.push(arguments); }}
    gtag('js', new Date());
    gtag('config', 'G-W1L7GJDSHX');
  </script>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{ theme: {{ extend: {{ colors: {{ brand: {{ 50:'#eef4fa', 100:'#dce7f3', 200:'#bfd1e4', 700:'#274b6b', 800:'#1d3a55', 900:'#12263b' }} }} }} }} }}
  </script>
  {schema_tag}
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen">
{header_html()}
{body_html}
{footer_html()}
</body>
</html>'''


def bullets(items):
    return '<ul class="space-y-2 text-slate-600">' + ''.join(f'<li class="flex gap-2"><span class="mt-2 h-1.5 w-1.5 rounded-full bg-brand-700 shrink-0"></span><span>{item}</span></li>' for item in items) + '</ul>'


def section(title, body):
    return f'<section class="mt-10"><h2 class="text-2xl font-bold tracking-tight text-slate-900">{title}</h2><div class="mt-3 space-y-4 text-base leading-7 text-slate-600">{body}</div></section>'


def related_links(links):
    return '<div class="mt-8 border-t border-slate-200 pt-6 flex flex-wrap gap-4 text-sm">' + ''.join(f'<a href="{href}" class="font-semibold text-brand-700 hover:text-brand-800 flex items-center gap-1">{label} <span aria-hidden="true">→</span></a>' for label, href in links) + '</div>'


def card(title, text, href=None):
    btn = f'<a href="{href}" class="mt-4 inline-flex items-center gap-2 text-sm font-semibold text-brand-700 hover:text-brand-800">Open <span aria-hidden="true">→</span></a>' if href else ''
    return f'<div class="rounded-[1.5rem] border border-slate-200 bg-white p-5 shadow-sm"><h3 class="text-lg font-bold text-slate-900">{title}</h3><p class="mt-2 text-sm leading-6 text-slate-600">{text}</p>{btn}</div>'


def hub(rel_path: str, title: str, description: str, eyebrow: str, h1: str, intro: str, sections: list, cta_h2: str, cta_p: str, cta_button: str, cta_href: str):
    section_html = ''.join(f'<section class="mt-10"><h2 class="text-2xl font-bold tracking-tight text-slate-900">{head}</h2><div class="mt-4 grid gap-4 md:grid-cols-2 xl:grid-cols-3">{"".join(cards)}</div></section>' for head, cards in sections)
    body = f'''
<main class="mx-auto max-w-6xl px-4 py-14 sm:px-6 lg:px-8">
  <div class="inline-flex rounded-full bg-brand-50 px-3 py-1 text-xs font-semibold uppercase tracking-[0.18em] text-brand-700">{eyebrow}</div>
  <h1 class="mt-4 text-4xl font-black tracking-tight text-slate-900 sm:text-5xl">{h1}</h1>
  <p class="mt-4 max-w-3xl text-lg leading-8 text-slate-600">{intro}</p>
  {section_html}
  <div class="mt-14 rounded-[1.5rem] border border-brand-100 bg-brand-50 p-6 sm:p-8">
    <h2 class="text-2xl font-black tracking-tight text-slate-900">{cta_h2}</h2>
    <p class="mt-2 text-sm leading-6 text-slate-600">{cta_p}</p>
    <a href="{cta_href}" class="mt-4 inline-flex items-center gap-2 rounded-xl bg-brand-700 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-brand-800">{cta_button} <span aria-hidden="true">→</span></a>
  </div>
</main>'''
    return shell(rel_path, title, description, body)


def article(rel_path: str, title: str, description: str, eyebrow: str, h1: str, intro_paras: list, sections: list, cta_h2: str, cta_p: str, cta_button: str, cta_href: str, related: list, og_type='article', schema_type='Article'):
    intro = ''.join(f'<p>{p}</p>' for p in intro_paras)
    sec_html = ''.join(section(head, bullets(items)) for head, items in sections)
    body = f'''
<main class="mx-auto max-w-4xl px-4 py-14 sm:px-6 lg:px-8">
  <div class="inline-flex rounded-full bg-brand-50 px-3 py-1 text-xs font-semibold uppercase tracking-[0.18em] text-brand-700">{eyebrow}</div>
  <h1 class="mt-4 text-4xl font-black tracking-tight text-slate-900 sm:text-5xl">{h1}</h1>
  <div class="mt-4 space-y-4 text-lg leading-8 text-slate-600">{intro}</div>
  {sec_html}
  <div class="mt-14 rounded-[1.5rem] border border-brand-100 bg-brand-50 p-6 sm:p-8">
    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-brand-700">{cta_h2}</p>
    <p class="mt-2 text-sm leading-6 text-slate-600">{cta_p}</p>
    <a href="{cta_href}" class="mt-4 inline-flex items-center gap-2 rounded-xl bg-brand-700 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-brand-800">{cta_button} <span aria-hidden="true">→</span></a>
  </div>
  {related_links(related)}
</main>'''
    schema = {
        '@context': 'https://schema.org',
        '@type': schema_type,
        'headline': h1,
        'description': description,
        'url': canonical_url(rel_path),
        'publisher': {'@type': 'Organization', 'name': BRAND, 'url': BASE_URL},
    }
    if schema_type == 'Article':
        schema['author'] = {'@type': 'Organization', 'name': BRAND}
    return shell(rel_path, title, description, body, og_type=og_type, schema=schema)


def calculator(rel_path: str, title: str, description: str, eyebrow: str, h1: str, intro: str, form_html: str, sections: list, cta_h2: str, cta_p: str, cta_button: str, cta_href: str, related: list):
    sec_html = ''.join(section(head, bullets(items)) for head, items in sections)
    body = f'''
<main class="mx-auto max-w-4xl px-4 py-14 sm:px-6 lg:px-8">
  <div class="inline-flex rounded-full bg-brand-50 px-3 py-1 text-xs font-semibold uppercase tracking-[0.18em] text-brand-700">{eyebrow}</div>
  <h1 class="mt-4 text-4xl font-black tracking-tight text-slate-900 sm:text-5xl">{h1}</h1>
  <p class="mt-4 max-w-3xl text-lg leading-8 text-slate-600">{intro}</p>
  <div class="mt-10 rounded-[1.5rem] border border-slate-200 bg-white p-6 shadow-sm">{form_html}</div>
  {sec_html}
  <div class="mt-14 rounded-[1.5rem] border border-brand-100 bg-brand-50 p-6 sm:p-8">
    <h2 class="text-2xl font-black tracking-tight text-slate-900">{cta_h2}</h2>
    <p class="mt-2 text-sm leading-6 text-slate-600">{cta_p}</p>
    <a href="{cta_href}" class="mt-4 inline-flex items-center gap-2 rounded-xl bg-brand-700 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-brand-800">{cta_button} <span aria-hidden="true">→</span></a>
  </div>
  {related_links(related)}
</main>'''
    schema = {
        '@context': 'https://schema.org',
        '@type': 'WebApplication',
        'name': h1,
        'description': description,
        'url': canonical_url(rel_path),
        'publisher': {'@type': 'Organization', 'name': BRAND, 'url': BASE_URL},
    }
    return shell(rel_path, title, description, body, schema=schema)


def write_pages(page_specs):
    urls = []
    for spec in page_specs:
        rel = spec['rel']
        kind = spec['kind']
        if kind == 'hub':
            html = hub(rel, spec['title'], spec['description'], spec['eyebrow'], spec['h1'], spec['intro'], spec['sections'], spec['cta_h2'], spec['cta_p'], spec['cta_button'], spec['cta_href'])
        elif kind == 'article':
            html = article(rel, spec['title'], spec['description'], spec['eyebrow'], spec['h1'], spec['intro'], spec['sections'], spec['cta_h2'], spec['cta_p'], spec['cta_button'], spec['cta_href'], spec['related'], spec.get('og_type', 'article'), spec.get('schema_type', 'Article'))
        elif kind == 'calculator':
            html = calculator(rel, spec['title'], spec['description'], spec['eyebrow'], spec['h1'], spec['intro'], spec['form_html'], spec['sections'], spec['cta_h2'], spec['cta_p'], spec['cta_button'], spec['cta_href'], spec['related'])
        elif kind == 'home':
            html = shell(rel, spec['title'], spec['description'], spec['body_html'], og_type='website', schema=spec['schema'])
        else:
            raise ValueError(f'Unknown kind: {kind}')
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding='utf-8')
        urls.append(canonical_url(rel))
    return urls


def write_sitemap(urls):
    unique = sorted(set(urls))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in unique:
        priority = '1.0' if url == BASE_URL + '/' else '0.8'
        lines.append(f'  <url><loc>{url}</loc><changefreq>monthly</changefreq><priority>{priority}</priority></url>')
    lines.append('</urlset>')
    (ROOT / 'sitemap.xml').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def write_robots():
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://cashlytica.com/sitemap.xml\n', encoding='utf-8')
