# Cashlytica repo norms

## Purpose
Cashlytica is a static marketing site for treasury / cash management content and conversion pages.
Treat the repository as the source for site content, page structure, SEO metadata, and deployment assets.

## Canonical sources
- `shared/*.html` contains the reusable shell partials.
- `build.py` renders the checked-in SSI source into a temporary deploy tree for publishing.
- `serve.py` is the local SSI preview server and default local port entrypoint.
- `sitemap.xml` should match the rendered HTML page inventory.
- `.github/workflows/deploy.yml` is the current publish path.
- `scripts/indexnow-submit.py` is the canonical IndexNow submit step.

If a rendered HTML file conflicts with the source partials or page HTML, fix the source pages / partials first, then rebuild the site.

## Repo shape
- Root HTML pages are public entrypoints.
- `learn/`, `tools/`, `samples/`, `compare/`, `use-cases/`, `for/`, `templates/`, `security/`, and `faq/` are page families.
- `og/` holds generated social images.
- Keep the root lean; avoid adding scratch files or duplicate docs.

## Local preview
- `serve.py` renders the checked-in SSI source locally.
- `serve.py` defaults to `http://localhost:8035` unless a port is passed on the command line.
- `build.py` defaults app handoff links to `http://localhost:5173`; override `CASHLYTICA_APP_ORIGIN` for production builds.
- If you preview pages locally, verify the rendered handoff links before assuming the published HTML is correct.

## Content and metadata rules
- Every public page should have:
  - one clear `<title>`
  - meta description
  - canonical URL
  - Open Graph and Twitter image metadata
  - a single clear H1
- Keep page-family copy consistent when a CTA or offer wording changes.
- Treat homepage, learn, samples, tools, compare, use-cases, for, security, FAQ, and templates as separate review surfaces.

## Navigation and handoff rules
- The public site should route clearly to the app handoff for login / register / get started actions.
- Do not hardcode local-preview values into published output.
- If the app origin changes, update the generator and any checked-in HTML together.

## Deployment rules
- The deploy workflow publishes the rendered site tree from a temporary build directory.
- Verify that any generated published artifact is the intended output.
- Rebuild or refresh the rendered tree before declaring a deploy-ready change complete.

## Hygiene rules
- Do not add stray scratch scripts, temp exports, or local cache files to the root.
- Keep docs short and source-of-truth driven.
- If a durable operating rule changes, update this file in the same pass.

## Verification before finishing changes
- Check the homepage in a browser.
- Check at least one hub page and one proof page.
- Confirm sitemap coverage still matches the HTML set.
- Confirm the app handoff links resolve to the intended origin.
- Confirm analytics / metadata changes appear consistently on the affected page family.
