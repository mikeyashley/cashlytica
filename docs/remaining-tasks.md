# Cashlytica Marketing Website — Remaining Tasks

Updated: 2026-06-14

This file turns `docs/PRD.md` into an implementation backlog.
Each task should be concrete enough that a small coding model can finish it without guessing the product direction.

Status labels used below:
- `pending` = not started
- `in progress` = actively being worked
- `done` = verified complete
- `blocked` = dependent on another task or missing decision

Order matters. Do the tasks in sequence unless a later task explicitly depends on earlier work.

---

## Phase 1 — lock the homepage and navigation

### TASK-01 — Rewrite the homepage around one acquisition wedge

Status: done

Goal:
Make `/` behave like a conversion page instead of a product directory.

Current problem:
The current homepage is useful, but it splits attention across too many product routes and still reflects older ladder language.

What to do:
- Edit `/Users/michael/Documents/GitHub/cashlytica/index.html`.
- Keep the existing brand shell, but rewrite the content flow to match the PRD:
  1. hero
  2. problem statement
  3. example finding
  4. how it works
  5. product ladder
  6. sample outputs
  7. proof
  8. final CTA
- Make the primary CTA `Run a $99 bank fee audit`.
- Keep `Check idle cash yield` and `See sample report` as secondary CTAs only.
- Remove or de-emphasize any copy that makes the page feel like a general app launcher.
- Replace older ladder language in visible marketing copy with the buyer-facing ladder:
  - Free
  - Analyst
  - Manager
  - Director
  - Treasurer
- Make sure `Connected` only appears, if needed, as a Manager capability in explanatory copy.
- Add a visible proof block with a specific sample number, such as `- $18,240 annual cash leakage found`.
- Add one short section that explains the audit-to-advisor path in plain language.
- Keep the page visually clean and institutionally styled.

Implementation notes:
- Reuse existing Tailwind CDN styling if it is still the simplest path.
- Avoid adding a JS app or framework.
- Keep one H1 only.
- Use short paragraphs and scan-friendly cards.

Acceptance criteria:
- A visitor can understand the offer in under 10 seconds.
- The homepage has one obvious primary action.
- No primary marketing copy uses `TAS`.
- No primary marketing copy uses old ladder labels as the main story.

Files:
- `/Users/michael/Documents/GitHub/cashlytica/index.html`

---

### TASK-02 — Simplify the top navigation and footer to support acquisition

Status: done

Goal:
Make the shared chrome support SEO and conversion instead of exposing too many low-intent surfaces.

What to do:
- Review the header and footer on the homepage and learn pages.
- Keep links that support acquisition:
  - Home
  - Learn
  - Sample report / proof pages
  - Audit CTA
  - Login / Get started
- If a page family grows, add a learn index link and sample/proof links.
- Remove or demote any nav item that competes with the primary CTA.
- Ensure footer links point to canonical URLs only.
- Make sure every top-level page can reach the learn hub and the main conversion page.

Acceptance criteria:
- Header and footer reinforce the funnel.
- No confusing or redundant navigation paths remain.
- The learn and sample surfaces are reachable from every major page.

Files:
- `/Users/michael/Documents/GitHub/cashlytica/index.html`
- `/Users/michael/Documents/GitHub/cashlytica/learn/*.html`

---

## Phase 2 — build the learn hub and article shell

### TASK-03 — Create a canonical `/learn/` index page

Status: done

Goal:
Provide a hub that groups all learn content by buyer problem.

What to do:
- Create `/Users/michael/Documents/GitHub/cashlytica/learn/index.html`.
- Organize the page into 4 sections:
  - bank fees
  - cash forecasting
  - idle cash / yield
  - treasury management
- For each section, list the supporting pages with one-line descriptions.
- Include one CTA block at the end that routes to the audit or sample report.
- Add internal links to the existing learn pages and future pages.
- Make the page useful both for users and for search engines.

Acceptance criteria:
- `/learn/` exists and is reachable from the homepage and footer.
- Every learn article has a path back to the hub.
- The hub makes the content strategy obvious.

Files:
- `/Users/michael/Documents/GitHub/cashlytica/learn/index.html`

---

### TASK-04 — Standardize the article page template

Status: done

Goal:
Make all learn pages follow the same structure so they can scale.

What to do:
- Audit the three existing article pages:
  - `/learn/bank-fee-audit/`
  - `/learn/13-week-cash-forecast/`
  - `/learn/treasury-management-software/`
- Extract a consistent article structure:
  1. title block
  2. answer summary
  3. explanatory sections
  4. example or checklist
  5. CTA block
  6. related articles
- Make sure each article has:
  - one H1
  - one canonical title tag
  - one concise top answer
  - one primary CTA
  - one related-links block
- Keep formatting simple and repeatable.

Implementation notes:
- If you do not introduce includes or a generator, copy the same article shell pattern into every page.
- Keep meta tags, CTA wording, and footer patterns consistent.

Acceptance criteria:
- A new article can be created by copying an existing pattern.
- The article experience feels consistent across the site.

Files:
- `/Users/michael/Documents/GitHub/cashlytica/learn/bank-fee-audit/index.html`
- `/Users/michael/Documents/GitHub/cashlytica/learn/13-week-cash-forecast/index.html`
- `/Users/michael/Documents/GitHub/cashlytica/learn/treasury-management-software/index.html`
- all future `/learn/**/index.html` pages

---

## Phase 3 — expand search traffic pages

### TASK-05 — Expand the bank-fee content cluster

Status: done

Goal:
Own the search intent around bank fee leakage.

What to do:
Create the following pages and make them internally link to each other:
- `/learn/bank-analysis-statements/`
- `/learn/common-business-bank-fees/`
- `/learn/wire-transfer-fee-benchmarks/`
- `/learn/earnings-credit-rate/`
- `/learn/how-to-negotiate-bank-fees/`

Each page should:
- answer one exact search query
- explain the concept in plain language
- include a small example, table, or checklist
- link back to `/learn/bank-fee-audit/`
- end with a CTA to the audit or sample report

Suggested angles:
- bank analysis statements explained
- common bank fees businesses overpay
- wire fee benchmark ranges
- how earnings credit rate works
- how to ask a bank for credits or rate relief

Acceptance criteria:
- The cluster forms a tight internal-link group.
- Each page has a unique search purpose.
- Each page pushes readers toward the audit.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/learn/.../index.html` pages

---

### TASK-06 — Expand the forecasting content cluster

Status: done

Goal:
Capture searchers who want short-term liquidity planning help.

What to do:
Create the following pages:
- `/templates/13-week-cash-forecast/`
- `/learn/cash-forecast-vs-cash-flow-statement/`
- `/learn/cash-forecast-accuracy/`
- `/learn/weekly-cash-forecasting-for-cfos/`
- `/learn/common-13-week-forecast-mistakes/`

Each page should:
- define the topic in the first few sentences
- include a short checklist or example forecast structure
- link to `/learn/13-week-cash-forecast/`
- point to the template or sample forecast if available
- end with a CTA to generate or improve the forecast in Cashlytica

Acceptance criteria:
- There is a real forecast cluster with internal link density.
- The articles lead toward a useful action, not just education.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/learn/.../index.html` pages

---

### TASK-07 — Expand the idle-cash and yield content cluster

Status: done

Goal:
Own search terms around idle cash, reserve cash, and yield optimization.

What to do:
Create the following pages:
- `/learn/idle-cash/`
- `/learn/how-much-cash-should-a-business-keep/`
- `/learn/money-market-funds-vs-treasury-bills-vs-sweep-accounts/`
- `/learn/idle-cash-drag/`
- `/learn/operating-cash-vs-reserve-cash/`
- `/learn/corporate-cash-yield-benchmarks/`

Each page should:
- explain the concept in CFO language
- include a simple numeric example or benchmark table
- link to the idle-cash calculator once it exists
- link to the treasury and forecast pages
- end with a CTA to check idle cash yield or run the audit

Acceptance criteria:
- The site has a coherent idle-cash cluster.
- The content supports the product wedge instead of drifting into generic finance education.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/learn/.../index.html` pages

---

### TASK-08 — Expand the treasury-management cluster

Status: done

Goal:
Capture users searching for treasury software alternatives and workflows.

What to do:
Create the following pages:
- `/learn/best-treasury-software-for-mid-market-companies/`
- `/learn/cash-position-dashboard/`
- `/learn/treasury-automation-for-finance-teams/`
- `/learn/bank-reconciliation-automation/`
- `/learn/treasury-kpis/`

Each page should:
- explain the problem or category
- compare manual vs automated workflows where relevant
- link to `/learn/treasury-management-software/`
- send readers to a product or sample page
- avoid enterprise-only jargon unless it is being contrasted explicitly

Acceptance criteria:
- The treasury cluster supports a broader SEO footprint.
- Pages link back to the product surfaces.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/learn/.../index.html` pages

---

## Phase 4 — build tools and templates that convert

### TASK-09 — Build the bank fee calculator

Status: done

Goal:
Create a high-intent interactive page that estimates annual bank fee overpayment.

What to do:
- Create `/tools/bank-fee-calculator/index.html`.
- Use a plain HTML form and simple in-page calculation.
- Inputs should include:
  - monthly wire fees
  - ACH fees
  - analysis fees
  - service charges
  - number of accounts
- Output should show an estimated annual overpayment.
- Include a short explanation of what the estimate means.
- Add a CTA to the $99 audit.

Implementation notes:
- Keep the calculator simple and fast.
- If you use JavaScript, keep it in one small inline block or a tiny separate file.
- Don’t overcomplicate the math.

Acceptance criteria:
- A visitor can enter numbers and see an immediate estimate.
- The output pushes the user toward the audit.

Files:
- create `/Users/michael/Documents/GitHub/cashlytica/tools/bank-fee-calculator/index.html`

---

### TASK-10 — Build the idle-cash calculator

Status: done

Goal:
Create a simple estimator for yield drag on excess cash.

What to do:
- Create `/tools/idle-cash-calculator/index.html`.
- Inputs should include:
  - average cash balance
  - current yield
  - available yield
  - minimum operating buffer
- Output should estimate annual yield drag.
- Explain how the estimate is derived in plain language.
- Link the result to Cashlytica’s idle-cash analysis and the audit.

Acceptance criteria:
- The page computes a meaningful output from user input.
- The CTA routes the user to Cashlytica.

Files:
- create `/Users/michael/Documents/GitHub/cashlytica/tools/idle-cash-calculator/index.html`

---

### TASK-11 — Build the 13-week forecast template page

Status: done

Goal:
Give visitors a practical artifact they can use immediately.

What to do:
- Create `/templates/13-week-cash-forecast/index.html`.
- Provide either:
  - a downloadable template, or
  - a copyable table structure the user can paste into a spreadsheet.
- Include a short explanation of what goes in each row/column.
- Show how Cashlytica automates or improves the same workflow.
- Add a CTA to start free or generate the forecast in Cashlytica.

Acceptance criteria:
- The page is useful even before someone buys anything.
- The page creates trust and intent.

Files:
- create `/Users/michael/Documents/GitHub/cashlytica/templates/13-week-cash-forecast/index.html`

---

### TASK-12 — Build the sample bank-fee audit report page

Status: done

Goal:
Show the buyer what the product actually produces.

What to do:
- Create `/samples/bank-fee-audit-report/index.html`.
- Include sections that look like a real report:
  - summary of findings
  - fee overpayments
  - benchmark comparisons
  - recommended next steps
  - upgrade preview if appropriate
- Use believable sample numbers.
- Show that the report is CFO-friendly, not just a chart dump.
- Add a CTA to run the audit for their own company.

Acceptance criteria:
- The page feels like proof, not marketing copy.
- The sample report supports the primary CTA.

Files:
- create `/Users/michael/Documents/GitHub/cashlytica/samples/bank-fee-audit-report/index.html`

---

### TASK-13 — Build the sample forecast and briefing pages

Status: done

Goal:
Show the other key outputs buyers care about.

What to do:
Create:
- `/samples/13-week-forecast/index.html`
- `/samples/board-briefing/index.html`
- `/samples/idle-cash-recommendation/index.html`

Each page should:
- look like a concrete product output
- explain what the user is seeing
- include example numbers and a short interpretation
- end with a CTA into Cashlytica

Acceptance criteria:
- The samples feel like real deliverables.
- The sample set covers audit, forecast, and recommendation use cases.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/samples/.../index.html` pages

---

## Phase 5 — capture comparison traffic and buyer-specific intent

### TASK-14 — Build comparison pages for competitor and spreadsheet intent

Status: done

Goal:
Capture people already evaluating alternatives.

What to do:
Create:
- `/compare/cashlytica-vs-kyriba/index.html`
- `/compare/cashlytica-vs-trovata/index.html`
- `/compare/cashlytica-vs-ramp/index.html`
- `/compare/cashlytica-vs-mercury/index.html`
- `/compare/cashlytica-vs-spreadsheets/index.html`

Each page should include:
- who the competitor is for
- where the competitor is strong
- where Cashlytica is simpler or better for mid-market use cases
- pricing or implementation contrast
- a short best-fit table
- a clear CTA

Implementation notes:
- Be honest. Don’t fake enterprise parity.
- Frame the comparison around mid-market simplicity, speed to value, and treasury outputs.

Acceptance criteria:
- Each page targets one comparison search intent.
- The pages are specific enough to rank and convert.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/compare/.../index.html` pages

---

### TASK-15 — Build use-case landing pages

Status: done

Goal:
Create pages that match the buyer’s immediate job-to-be-done.

What to do:
Create:
- `/use-cases/bank-fee-audit/index.html`
- `/use-cases/idle-cash-yield/index.html`
- `/use-cases/13-week-cash-forecast/index.html`
- `/use-cases/cash-position-dashboard/index.html`
- `/use-cases/board-reporting/index.html`
- `/use-cases/reconciliation/index.html`
- `/use-cases/cfo-treasury-advisor/index.html`

Each page should include:
- pain statement
- symptoms
- how Cashlytica helps
- a sample result or report preview
- one CTA

Acceptance criteria:
- A visitor can self-select the use case that matches them.
- The pages support both search and paid conversion.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/use-cases/.../index.html` pages

---

### TASK-16 — Build buyer persona pages

Status: done

Goal:
Tailor the site to the audience that actually buys.

What to do:
Create:
- `/for/cfos/index.html`
- `/for/controllers/index.html`
- `/for-founders/index.html`
- `/for/finance-teams/index.html`
- `/for/mid-market-companies/index.html`

Each page should:
- describe the user’s main pain points
- explain which Cashlytica outputs matter most to them
- link to the relevant use cases, samples, and tools
- end with the most relevant CTA

Acceptance criteria:
- The site has clear messaging by persona.
- The pages do not read like duplicated filler.

Files:
- create new `/Users/michael/Documents/GitHub/cashlytica/for/.../index.html` pages

---

## Phase 6 — trust, FAQ, and commercial clarity

### TASK-17 — Build the security page

Status: done

Goal:
Reduce trust friction for finance buyers.

What to do:
- Create `/security/index.html`.
- Explain:
  - data handling
  - redacted uploads
  - tenant isolation
  - encryption
  - bank feed posture
  - software-not-bank posture
- Keep the page plain and direct.
- Link from the homepage and footer.

Acceptance criteria:
- A buyer can tell how Cashlytica handles sensitive finance data.
- The page answers the most obvious trust objections.

Files:
- create `/Users/michael/Documents/GitHub/cashlytica/security/index.html`

---

### TASK-18 — Build the FAQ page

Status: done

Goal:
Answer the high-friction questions that would otherwise kill conversion.

What to do:
- Create `/faq/index.html`.
- Cover questions such as:
  - What documents do I upload?
  - Can I redact statements?
  - Does Cashlytica move money?
  - How does the $99 audit work?
  - What happens if no savings are found?
  - What is Analyst?
  - Do I need live bank connections?
  - How does the audit credit work?
- Use concise answers.
- Add links to the relevant product, sample, or learn pages.

Acceptance criteria:
- The FAQ reduces uncertainty instead of adding more copy.

Files:
- create `/Users/michael/Documents/GitHub/cashlytica/faq/index.html`

---

### TASK-19 — Add clearer commercial motion to the page set

Status: done

Goal:
Make the site honest about what is self-serve and what is sales-assisted.

What to do:
- Audit all pages for motion clarity.
- Self-serve should be used for:
  - Free
  - Analyst
  - Manager
- Sales-assisted should be used for:
  - Director
  - Treasurer
- On pages for higher tiers, make the contact path explicit.
- On self-serve pages, route to the audit, calculator, or register path.

Acceptance criteria:
- Users are not promised a self-serve checkout for sales-assisted tiers.
- The site’s commercial ladder matches the PRD.

Files:
- homepage, product pages, comparison pages, use-case pages, and any checkout-linked page

---

## Phase 7 — SEO, metadata, and site hygiene

### TASK-20 — Standardize metadata across all pages

Status: done

Goal:
Make every page indexable and shareable with clear, unique metadata.

What to do:
For every page in the site:
- set a unique title tag
- set a unique meta description
- set canonical URL tags
- set Open Graph tags
- set Twitter card tags
- ensure exactly one H1

For article pages, also add:
- `Article` schema
- `datePublished` and `dateModified` if available
- publisher information

For product pages, also add:
- `SoftwareApplication` schema where appropriate
- product offer data if it fits the page

Acceptance criteria:
- No two major pages share the same title or description.
- The metadata matches the content on the page.

Files:
- all public HTML pages

---

### TASK-21 — Improve sitemap and robots coverage

Status: done

Goal:
Keep search engines aware of every public page.

What to do:
- Update `sitemap.xml` so it includes every public page that should be indexed.
- Keep canonical URLs consistent with the sitemap.
- Confirm `robots.txt` points to the sitemap.
- Exclude non-public or duplicate surfaces if needed.

Implementation notes:
- If the site grows further, create a small sitemap generation script so the file does not drift.
- Make sure new pages are added to the sitemap in the same change they are created.

Acceptance criteria:
- Search engines can discover the full public site.
- No important page is missing from the sitemap.

Files:
- `/Users/michael/Documents/GitHub/cashlytica/sitemap.xml`
- `/Users/michael/Documents/GitHub/cashlytica/robots.txt`

---

### TASK-22 — Add a consistent internal linking system

Status: done

Goal:
Make the site feel connected instead of isolated page-by-page.

What to do:
- Add related-links blocks to every learn page.
- Add links from learn pages to:
  - the audit
  - calculators
  - samples
  - comparison pages
- Add links from homepage sections into the learn and sample hubs.
- Add links from calculator and sample pages back into the audit or register path.

Acceptance criteria:
- A user can move naturally from content to proof to conversion.
- The internal link graph supports SEO.

Files:
- all learn pages
- all tools pages
- all sample pages
- homepage

---

### TASK-23 — Add a shared page pattern or generator if the page count starts to drift

Status: blocked

Goal:
Avoid copy-paste divergence as the page count grows.

What to do:
- If manual duplication becomes painful, add a lightweight shared pattern for repeated content blocks:
  - header
  - footer
  - CTA block
  - metadata block
- Keep it simple enough for a static site.
- Do not introduce a heavy framework unless the repo already needs it.

Acceptance criteria:
- New pages can be added without metadata or CTA drift.
- The site remains easy to edit as it grows.

Files:
- only if needed after the first round of page expansion

---

## Phase 8 — analytics and measurement

### TASK-24 — Make analytics useful for conversion decisions

Status: done

Goal:
Measure traffic quality and downstream action, not just pageviews.

What to do:
- Keep Google Analytics installed.
- Add event tracking for the main actions:
  - audit CTA clicks
  - calculator interactions
  - sample report views
  - register clicks
  - login clicks
  - comparison-page CTAs
- If possible, distinguish homepage traffic from learn-page traffic.
- Verify that the measurement ID is present on all public pages.

Acceptance criteria:
- The site can answer which pages create users.
- The main funnel actions are trackable.

Files:
- public HTML pages and any shared script block

---

### TASK-25 — Set up a weekly search and funnel review process

Status: done

Goal:
Turn SEO work into an operating habit.

What to do:
- Create a simple review checklist for Search Console / analytics.
- Review by page group:
  - homepage
  - learn pages
  - tools
  - samples
  - compare pages
- Track:
  - impressions
  - clicks
  - CTR
  - CTA clicks
  - calculator starts/completions
  - audit starts
  - register clicks
- Use the findings to decide what content to add next.

Acceptance criteria:
- The site has a repeatable improvement loop.
- Content decisions are based on traffic and conversion data.

Files:
- optional `docs/` note if you want the checklist documented separately

---

## Phase 9 — final verification

### TASK-26 — Run a full public-site QA pass

Status: done

Goal:
Verify that the public marketing site is coherent after the new pages are added.

What to do:
- Open the homepage in a browser.
- Verify the primary CTA, navigation, and proof sections.
- Open at least one page from each major surface:
  - learn
  - tools
  - samples
  - compare
  - use cases
  - persona pages
  - security
  - FAQ
- Check for broken links, missing titles, and mismatched CTA text.
- Confirm the site feels like one product, not a pile of pages.

Acceptance criteria:
- The public site is navigable and internally consistent.
- The funnel is obvious end-to-end.

Files:
- all public pages

---

## Delivery rule

Do not call the marketing site finished until the homepage, learn hub, calculator(s), sample report(s), comparison pages, trust pages, and sitemap are all live and internally linked.

The minimum launchable set is:
- homepage rewrite
- `/learn/`
- at least 6 supporting learn pages
- one calculator
- one sample report
- `/security/`
- `/faq/`
- sitemap coverage for every public page
