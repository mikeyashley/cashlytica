# Cashlytica marketing site: SEO and editorial audit

Audit date: 2026-10-30. Scope: every public page (58) of `cashlytica.com`, the repo at `/Users/michael/Documents/GitHub/cashlytica` (branch `main`), and `.github/workflows/deploy.yml`.
Status: read-only. No page, partial, script or workflow was changed. Nothing is committed. This file is the only addition.

Read first, as asked: `NORMS.md`, `docs/PRD.md`, `docs/remaining-tasks.md`, `docs/weekly-growth-report-2026-07-07.md`. Product claims are checked against the code-verified inventory (`/tmp/cashlytica-tas-features.md`, identical to `docs/audit-2026-10/tas-features.md`), which existed when this audit finished.

## 1. What matters most, in order

1. **Internal strategy documents are public.** `https://cashlytica.com/docs/PRD.md`, `/docs/remaining-tasks.md` and `/docs/weekly-growth-report-2026-07-07.md` all return HTTP 200 today. `build.py` skips `.git`, `.github`, `__pycache__` and `scripts` but not `docs/`, so the whole folder is deployed. The growth report contains the GA4 property ID and Search Console property. **This audit file, and the inventory beside it, would be published the same way if committed and pushed.** `NORMS.md` is not exposed (it is in `SKIP_FILES`). Fix the build skip list before committing anything under `docs/`.
2. **Planning language is printed to buyers.** Every one of the 58 pages carries the footer sentence "Traffic, proof, and conversion for finance teams..." and the line "Public brand: Cashlytica." Beyond the footer, at least 26 pages contain body or meta text addressed to the site's editors rather than the buyer (examples in section 4.4). One meta description reads "Show why a manual spreadsheet workflow is the easiest comparison to win."
3. **The proof numbers contradict each other.** Homepage: $18,240 potential annual savings. Samples hub and board briefing: $1,800. Sample audit report page: $720 on $2,280 of annualised fees. The hub calls the samples "real" and "Cassius-generated"; the report page says "synthetic example, not a customer report".
4. **Several product claims are false or unsupported against the code** (section 5): the Free tier "forecast basics", "intraday positioning", "does not move money" as an absolute, "upload bank statements" with no mention that PDF is unsupported, a "Treasurer" rung the plan inventory does not contain, and "Cassius starts working the first session".
5. **The content is thin.** Median page: 140 words. 43 of 58 pages are under 200 words; 34 are under 150; only 7 reach 300. The site is 10,421 visible words in total. Search Console (week to 2026-07-06): 0 clicks, 46 impressions, average position about 80. At that position breadth does not help; fewer, deeper pages would.
6. **Cannibalisation is built in.** Seven pages target the 13-week forecast, nine the idle-cash cluster, four "bank fee audit", and two have an identical H1 ("Cash Position Dashboard"). Map in section 4.3. The recommendation takes 58 pages to 39.
7. **Conversion plumbing cannot answer the PRD's question.** Every app-bound CTA, whatever its label, goes to `app.cashlytica.com/register/` with no source parameter. There is no pricing page, no contact path (no `mailto:` anywhere), and the click classifier in `shared/analytics.js` mislabels many internal links as `registration_start`.
8. **Technical gaps:** all 57 social images are SVG (generally not rendered by Facebook, LinkedIn or X); no favicon link on any page; no BreadcrumbList; `www.cashlytica.com` serves 200 instead of redirecting; sitemap has no `lastmod`; only 5 pages carry any date.

## 2. Method and caveats

- Built the site with `CASHLYTICA_APP_ORIGIN=https://app.cashlytica.com python3 build.py` into a scratch directory (58 pages) and parsed the rendered HTML. The repo build default is `http://localhost:5173`; the workflow sets the production origin, so the published output was the one measured.
- **Words** = visible text outside `<header>`, `<footer>` and `<nav>`, so CTA bands are included and the footer is not. Treat as ±5%.
- **Internal links** = unique body links to other pages (header and footer navigation excluded); "in" counts pages that link to this URL from their body. Hubs therefore look less linked than they are: every page links to every hub through the header.
- **GA4** column: the gtag snippet (`G-W1L7GJDSHX`) and `shared/analytics.js` are both loaded on all 58 pages via `shared/head-assets.html`. Events are inferred from reading `analytics.js` and the inline scripts; I did not open GA4, so which events are marked as key events is not verified.
- Live checks were GET/HEAD requests to `cashlytica.com`. External links: the AFP deep link on the ECR page redirects to the AFP home page (effectively broken); the J.P. Morgan link returns 200; the two Kyriba links return 403 to `curl` (likely bot blocking, not confirmed).
- Competitor facts on the Kyriba pages are the pages' own, dated 2026-10-21; I did not re-verify them.

### Legend for the table

`T`/`M` = title / meta description length in characters (`↑` over limit: title over 60, meta over 160; `↓` meta under 70). `C✓` canonical equals the page URL. `H1✓` exactly one H1. `LD` = JSON-LD types; `(dM)` = has `dateModified`. `OG:svg` = og:image present and an SVG; `TW:none` = no twitter:image. CTA destinations are shown as rendered with the production origin.

## 3. Per-page table

| URL | Apparent target query | Words | Title / meta / canonical / H1 / JSON-LD / OG | Internal links (body) | CTA and destination | GA4 | Verdict | Reason |
|---|---|---:|---|---|---|---|---|---|
| `/` | ai treasury software / "treasury intelligence" (brand-led, no search target) | 468 | T52 M138 C✓ H1✓ LD:Org+WebSite+SoftApp OG:svg | 8 out / 1 in | "Start with Cassius: $99 audit"; "Run a $99 bank fee audit" → app /register/ | ✓ | **Revise** | Leads with "Cassius" and AI claims instead of the PRD hero; $18,240 example contradicts the samples; ladder has an unverified Treasurer rung and "intraday positioning". |
| `/compare/` | (hub) treasury comparisons | 273 | T59 M88 C✓ H1✓ LD:none OG:svg | 5 out / 7 in | "Run the audit" → app /register/ | ✓ | **Revise** | Internal-voice copy ("What these pages should answer"); lists five pages, two of which should go. |
| `/compare/cashlytica-vs-kyriba/` | cashlytica vs kyriba / kyriba alternative | 719 | T52 M151 C✓ H1✓ LD:Article (dM) OG:svg | 4 out / 2 in | "Run the audit" → app /register/ | ✓ | **Keep** | 719 words, dated, vendor-sourced, hedged: the standard for the other compare pages. One claim ("your team executes") needs fixing. |
| `/compare/cashlytica-vs-mercury/` | cashlytica vs mercury | 139 | T34 M69↓ C✓ H1✓ LD:Article OG:svg | 3 out / 1 in | "Run the audit" → app /register/ | ✓ | **Merge → /compare/** | Mercury is a bank, not a treasury-analytics rival; 139 words of unsourced, internal-voice copy. |
| `/compare/cashlytica-vs-ramp/` | cashlytica vs ramp | 209 | T31 M95 C✓ H1✓ LD:Article OG:svg | 3 out / 1 in | "Run the audit" → app /register/ | ✓ | **Merge → /compare/** | Ramp is spend management; 209 words, unsourced, internal-voice copy. |
| `/compare/cashlytica-vs-spreadsheets/` | treasury spreadsheet alternative / excel cash forecasting | 133 | T39 M72 C✓ H1✓ LD:Article OG:svg | 3 out / 3 in | "Run the audit" → app /register/ | ✓ | **Revise** | The PRD calls it the highest-converting comparison; 133 words, and the meta description reads "the easiest comparison to win". |
| `/compare/cashlytica-vs-trovata/` | cashlytica vs trovata / trovata alternative | 139 | T34 M75 C✓ H1✓ LD:Article OG:svg | 3 out / 1 in | "Run the audit" → app /register/ | ✓ | **Revise** | Direct competitor; 139 words with undated, unsourced claims; rebuild to the Kyriba page standard. |
| `/faq/` | (trust page) cashlytica faq / $99 audit faq | 328 | T14 M89 C✓ H1✓ LD:FAQPage OG:svg | 2 out / 2 in | "Run the audit" → app /register/ | ✓ | **Revise** | Has the PRD questions but three answers are wrong or incomplete (statement formats, money movement, refund); no pricing answer. |
| `/for/` | (hub) personas | 104 | T51 M74 C✓ H1✓ LD:none OG:svg | 5 out / 5 in | "See the audit" → app /register/ | ✓ | **Revise** | Becomes the single persona page with sections once the five pages are merged. |
| `/for/cfos/` | (none) cfo treasury | 77 | T19 M57↓ C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "See the briefing"; "For hub" | ✓ | **Merge → /for/** | 77 words from one three-bullet template; no search demand; internal-voice sentence. |
| `/for/controllers/` | (none) controller reconciliation | 68 | T26 M79 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "See reconciliation"; "For hub" | ✓ | **Merge → /for/** | 68 words from the same template; "cleaner matching" is an unverified claim. |
| `/for/finance-teams/` | (none) finance team cash workflow | 74 | T28 M65↓ C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "Open the learn hub"; "For hub" | ✓ | **Merge → /for/** | 74 words from the same template. |
| `/for/founders/` | (none) startup cash runway | 87 | T23 M71 C✓ H1✓ LD:Article OG:svg | 3 out / 1 in | "Run the audit" → app /register/ | ✓ | **Merge → /for/** | 87 words from the same template. |
| `/for/mid-market-companies/` | treasury for mid-market companies | 72 | T35 M73 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "See the product"; "For hub" | ✓ | **Merge → /learn/treasury-management-software/** | 72 words; the same query as the TMS page; "no six-figure implementation" is unsupported. |
| `/learn/` | treasury guides (hub) | 246 | T54 M76 C✓ H1✓ LD:none OG:svg | 12 out / 17 in | "Start here" → app /register/ | ✓ | **Revise** | Links only 11 of 24 articles; ECR and Kyriba pricing are not on it; CTA copy is internal-voice. |
| `/learn/13-week-cash-forecast/` | 13 week cash forecast (GSC top query, pos ~84) | 147 | T45 M163↑ C✓ H1✓ LD:Article OG:svg | 3 out / 7 in | no app CTA; internal: "Use the template"; "Forecast template" | ✓ | **Revise** | Best organic opportunity but 147 words; needs a worked example, inline template and sources; absorb the weekly-cadence and mistakes notes. |
| `/learn/bank-analysis-statements/` | bank analysis statement | 149 | T47 M80 C✓ H1✓ LD:Article OG:svg | 3 out / 4 in | "Run the audit" → app /register/ | ✓ | **Revise** | Distinct query but 149 words; needs an annotated example statement and a link to ECR. |
| `/learn/bank-fee-audit/` | bank fee audit | 315 | T40 M162↑ C✓ H1✓ LD:Article (dM) OG:svg | 3 out / 7 in | "Run the $99 audit" → app /register/ | ✓ | **Revise** | Strongest learn page on the wedge (worked math ties); benchmark source unstated, no datePublished, four-way overlap with use-case, sample and calculator. |
| `/learn/bank-reconciliation-automation/` | bank reconciliation automation | 101 | T43 M81 C✓ H1✓ LD:Article OG:svg | 4 out / 3 in | no app CTA; internal: "See cash position"; "Treasury automation" | ✓ | **Revise** | 101 words; rewrite as manual-vs-automated and scope any product claim to human-confirmed bank/books matching. |
| `/learn/best-treasury-software-for-mid-market-companies/` | best treasury software for mid-market companies | 141 | T60 M95 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "Explore use cases"; "Treasury management software" | ✓ | **Merge → /learn/treasury-management-software/** | Same meta description and near-identical lead as the TMS page; names no alternatives, so cannot satisfy a "best" query. |
| `/learn/cash-forecast-accuracy/` | cash forecast accuracy | 123 | T35 M80 C✓ H1✓ LD:Article OG:svg | 4 out / 7 in | no app CTA; internal: "See the forecast sample"; "13-week forecast" | ✓ | **Revise** | 123 words; add MAPE/WAPE formula with a worked example and link the template. |
| `/learn/cash-forecast-vs-cash-flow-statement/` | cash forecast vs cash flow statement | 124 | T49 M81 C✓ H1✓ LD:Article OG:svg | 4 out / 0 in | no app CTA; internal: "Build the forecast"; "13-week forecast" | ✓ | **Revise** | Distinct definitional query but an orphan (0 body links in, not on the hub); add a comparison table. |
| `/learn/cash-position-dashboard/` | cash position dashboard | 119 | T36 M82 C✓ H1✓ LD:Article OG:svg | 4 out / 7 in | no app CTA; internal: "See the forecast sample"; "Treasury software" | ✓ | **Revise** | Keep as the informational target; the use-case page has the identical H1 and must be merged or differentiated. |
| `/learn/common-13-week-forecast-mistakes/` | 13 week cash flow forecast mistakes | 126 | T45 M64↓ C✓ H1✓ LD:Article OG:svg | 3 out / 1 in | no app CTA; internal: "See the forecast sample"; "13-week forecast" | ✓ | **Merge → /learn/13-week-cash-forecast/** | 126 words of generic advice; one inbound link; folds into the pillar as a section. |
| `/learn/common-business-bank-fees/` | business bank fees | 137 | T38 M75 C✓ H1✓ LD:Article OG:svg | 3 out / 4 in | "Run the $99 audit" → app /register/ | ✓ | **Revise** | Make it the fee-by-fee reference with sourced ranges; currently overlaps wire benchmarks and the audit page. |
| `/learn/corporate-cash-yield-benchmarks/` | corporate cash yield benchmarks | 135 | T44 M74 C✓ H1✓ LD:Article OG:svg | 4 out / 8 in | no app CTA; internal: "Check idle cash yield"; "Idle cash" | ✓ | **Revise** | Title promises benchmarks; page has no numbers. Needs a dated, sourced rate table or it should be merged into idle-cash-drag. |
| `/learn/earnings-credit-rate/` | earnings credit rate | 436 | T56 M160 C✓ H1✓ LD:Article (dM) OG:svg | 3 out / 1 in | "Run the audit" → app /register/ | ✓ | **Keep** | Best article on the site: formula, worked example (arithmetic verified), two sources, dateModified. Only one body link in and not on the hub. |
| `/learn/how-much-cash-should-a-business-keep/` | how much cash should a business keep | 125 | T50 M102 C✓ H1✓ LD:Article OG:svg | 4 out / 2 in | no app CTA; internal: "Estimate yield drag"; "Idle cash" | ✓ | **Revise** | 125 words; absorb operating-vs-reserve and add a months-of-expenses worked example. |
| `/learn/how-to-negotiate-bank-fees/` | how to negotiate bank fees | 147 | T39 M76 C✓ H1✓ LD:Article OG:svg | 3 out / 2 in | "Run the audit" → app /register/ | ✓ | **Revise** | Internal voice ("Cashlytica should help buyers..."); add a call script/email and a worked ask. |
| `/learn/idle-cash-drag/` | idle cash drag / cost of idle cash | 205 | T27 M73 C✓ H1✓ LD:Article OG:svg | 4 out / 4 in | no app CTA; internal: "Check idle cash yield"; "Idle cash" | ✓ | **Revise** | Becomes the idle-cash pillar; add a worked example that matches the calculator and absorb idle-cash. |
| `/learn/idle-cash/` | idle cash | 134 | T22 M89 C✓ H1✓ LD:Article OG:svg | 4 out / 8 in | no app CTA; internal: "Check idle cash yield"; "Idle cash drag" | ✓ | **Merge → /learn/idle-cash-drag/** | 134 words; the definition duplicates the drag page; title is 22 characters. |
| `/learn/kyriba-pricing/` | kyriba pricing | 695 | T49 M159 C✓ H1✓ LD:Article (dM) OG:none TW:none | 4 out / 1 in | no app CTA; internal: "View the sample report" | ✓ | **Keep** | Sourced, dated, hedged, with a usable quote checklist. Missing og:image/twitter:image; one body link in; not on the hub. |
| `/learn/money-market-funds-vs-treasury-bills-vs-sweep-accounts/` | money market funds vs treasury bills vs sweep accounts | 214 | T67↑ M85 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "Check idle cash yield"; "Idle cash" | ✓ | **Revise** | Real query, 214 words, no table, yields, risks or sources; title is 67 characters. |
| `/learn/operating-cash-vs-reserve-cash/` | operating cash vs reserve cash | 116 | T43 M99 C✓ H1✓ LD:Article OG:svg | 4 out / 3 in | no app CTA; internal: "Check idle cash yield"; "Idle cash" | ✓ | **Merge → /learn/how-much-cash-should-a-business-keep/** | 116 words; the same decision as the cash-buffer page. |
| `/learn/treasury-automation-for-finance-teams/` | treasury automation | 107 | T50 M86 C✓ H1✓ LD:Article OG:svg | 3 out / 2 in | "Open the audit path" → app /register/ | ✓ | **Merge → /learn/treasury-management-software/** | 107 words; its automation list reads as a product description (alerts, reconciliation matching) that the inventory does not support. |
| `/learn/treasury-kpis/` | treasury kpis | 129 | T26 M72 C✓ H1✓ LD:Article OG:svg | 4 out / 3 in | no app CTA; internal: "See the product outputs"; "Treasury software" | ✓ | **Revise** | 129 words; KPIs have no definitions or formulas; distinct intent worth keeping. |
| `/learn/treasury-management-software/` | treasury management software (GSC: "treasury reporting software", pos ~79) | 200 | T66↑ M95 C✓ H1✓ LD:Article OG:svg | 4 out / 7 in | no app CTA; internal: "Explore use cases"; "Cash position dashboard" | ✓ | **Revise** | Pillar for the treasury cluster; needs a category explainer, named alternatives and sources, and should absorb best-treasury and automation. |
| `/learn/weekly-cash-forecasting-for-cfos/` | weekly cash forecasting | 123 | T45 M81 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "Open the forecast sample"; "13-week forecast" | ✓ | **Merge → /learn/13-week-cash-forecast/** | 123 words; the cadence section belongs in the pillar. |
| `/learn/wire-transfer-fee-benchmarks/` | wire transfer fee benchmarks / business wire fees | 156 | T41 M91 C✓ H1✓ LD:Article OG:svg | 3 out / 3 in | "Run the audit" → app /register/ | ✓ | **Revise** | Promises benchmarks and gives no numbers; needs dated, sourced bank-published ranges or a merge into common-business-bank-fees. |
| `/samples/` | (hub) sample outputs | 322 | T42 M98 C✓ H1✓ LD:none OG:svg | 4 out / 15 in | no app CTA; internal: "Start with the audit"; "See the forecast" | ✓ | **Revise** | Calls the samples "real" and "Cassius-generated"; quotes $1,800 savings that the report page does not support ($720). |
| `/samples/13-week-forecast/` | sample 13 week cash flow forecast | 124 | T29 M83 C✓ H1✓ LD:Article OG:svg | 3 out / 11 in | "Explore the product" → app /register/ | ✓ | **Revise** | Shows 4 weeks with 2 filled, not 13; "golden fixtures" in the meta description; internal "Source shape" notes. |
| `/samples/bank-fee-audit-report/` | sample bank fee audit report | 224 | T34 M146 C✓ H1✓ LD:Article (dM) OG:svg | 3 out / 7 in | "Run the $99 audit" → app /register/ | ✓ | **Keep** | Best proof asset: labelled synthetic, arithmetic ties ($190, $2,280, $720). Other pages must be brought into line with it. |
| `/samples/board-briefing/` | board cash briefing sample | 157 | T27 M112 C✓ H1✓ LD:Article OG:svg | 3 out / 6 in | "Explore the product" → app /register/ | ✓ | **Revise** | $1,800 conflicts with the report; $3.5M excess cash sits beside a ~$1M forecast; board packs are Director-only and the page does not say so. |
| `/samples/idle-cash-recommendation/` | idle cash recommendation sample | 103 | T37 M89 C✓ H1✓ LD:Article OG:svg | 3 out / 4 in | "Check idle cash yield" → app /register/ | ✓ | **Revise** | 103 words; exposes service names and "golden fixture"; no worked reasoning. |
| `/security/` | (trust page) cashlytica security | 217 | T19 M69↓ C✓ H1✓ LD:Article OG:svg | 1 out / 4 in | "Run the audit" → app /register/ | ✓ | **Revise** | Missing the PRD items (encryption, bank-feed posture); "ask us" with no contact path. Verified controls exist and can be stated; SOC 2/SSO must not be. |
| `/templates/` | (hub) finance templates | 64 | T61↑ M69↓ C✓ H1✓ LD:none OG:svg | 1 out / 1 in | "Use the template" → app /register/ | ✓ | **Merge → /templates/13-week-cash-forecast/** | 64 words and one item; a hub adds nothing until there is a second template. |
| `/templates/13-week-cash-forecast/` | 13 week cash flow forecast template | 157 | T43 M83 C✓ H1✓ LD:Article OG:svg | 3 out / 5 in | "Generate the forecast" → app /register/ | ✓ | **Revise** | Says "copy into a spreadsheet" but supplies six row names, no table or download; fails the template intent. |
| `/tools/` | (hub) cash calculators | 148 | T61↑ M64↓ C✓ H1✓ LD:none OG:svg | 2 out / 1 in | "Run the audit" → app /register/ | ✓ | **Revise** | 148 words with internal-voice copy ("turn interest into intent"); fine as a hub once rewritten. |
| `/tools/bank-fee-calculator/` | bank fee calculator | 169 | T32 M89 C✓ H1✓ LD:WebApp OG:svg | 3 out / 3 in | "Run the audit"; "Run the $99 audit" → app /register/ | ✓ +calculator_complete | **Revise** | Labels total fees x 12 as "estimated annual overpayment"; it never estimates an overpayment. Fix label or add a benchmark input. |
| `/tools/idle-cash-calculator/` | idle cash calculator / cash yield calculator | 169 | T33 M56↓ C✓ H1✓ LD:WebApp OG:svg | 3 out / 9 in | "Check idle cash in Cashlytica"; "Run the audit" → app /register/ | ✓ +calculator_complete | **Keep** | Formula is sound ((balance - buffer) x spread); default 4.75% available yield is unsourced and should be labelled an assumption. |
| `/use-cases/` | (hub) use cases | 167 | T48 M93 C✓ H1✓ LD:none OG:svg | 7 out / 11 in | "Run a bank fee audit" → app /register/ | ✓ | **Revise** | Internal-voice copy; shrinks to three entries after the merges. |
| `/use-cases/13-week-cash-forecast/` | 13 week cash forecast software | 172 | T36 M78 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "See the sample"; "Use cases hub" | ✓ | **Merge → /learn/13-week-cash-forecast/** | Fourth page on the same query (learn, template, sample); no differentiated commercial content. |
| `/use-cases/bank-fee-audit/` | bank fee audit service / cost ($99) | 93 | T29 M89 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "See sample report"; "Use cases hub" | ✓ | **Revise** | 93 words, no app CTA; make it the transactional $99 page (what you upload, what you get, refund) so it stops competing with the learn page. |
| `/use-cases/board-reporting/` | board cash reporting | 86 | T30 M80 C✓ H1✓ LD:Article OG:svg | 4 out / 2 in | no app CTA; internal: "See the sample"; "Use cases hub" | ✓ | **Merge → /samples/board-briefing/** | 86 words; board packs are Director-only and the page does not say so. |
| `/use-cases/cash-position-dashboard/` | cash position dashboard | 163 | T38 M84 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "Open sample forecast"; "Use cases hub" | ✓ | **Merge → /learn/cash-position-dashboard/** | Identical H1 and query as the learn page; 163 words. |
| `/use-cases/cfo-treasury-advisor/` | (none) title says "operating levels", slug says "advisor" | 96 | T44 M80 C✓ H1✓ LD:Article OG:svg | 3 out / 1 in | "Get started" → app /register/ | ✓ | **Revise** | Title, slug and hub label disagree; "ongoing relationship" is unverified. Best home for the missing pricing/levels content. |
| `/use-cases/idle-cash-yield/` | idle cash yield | 171 | T30 M104 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "Check idle cash yield"; "Use cases hub" | ✓ | **Merge → /learn/idle-cash-drag/** | Same query as the idle-cash pages and the calculator; claims "why the move is safe" without support. |
| `/use-cases/reconciliation/` | cash reconciliation software | 79 | T29 M99 C✓ H1✓ LD:Article OG:svg | 4 out / 1 in | no app CTA; internal: "See the samples"; "Use cases hub" | ✓ | **Merge → /learn/bank-reconciliation-automation/** | 79 words; product matching is human-confirmed with no write-back, so claims need care. |

Totals: 58 pages. **Keep 5, Revise 34, Merge 19.** After the merges the site has 39 pages. Every merged URL should get a 301 to the target shown; none are recommended for deletion without one. The verdicts are recommendations for the owner, not decisions.

## 4. Cross-site problems

### 4.1 Exposed and operational

| Problem | Evidence | Why it matters |
|---|---|---|
| `docs/` is deployed | `build.py` `SKIP_DIRS = {'.git', '.github', '__pycache__', 'scripts'}`; live `/docs/PRD.md`, `/docs/remaining-tasks.md`, `/docs/weekly-growth-report-2026-07-07.md` return 200 | Competitors and buyers can read the strategy, backlog and analytics IDs. Robots allows everything, so they are crawlable. |
| `www` is not canonicalised | `https://www.cashlytica.com/` returns 200 with the apex canonical; `http://` does 301 to https. The 2026-07-07 report flagged Search Console showing both hosts. | Duplicate hosts split signals; the canonical tag only partly mitigates. |
| No `.htaccess` or redirect map in the repo | Repo root listing | Nothing here can express the 19 recommended 301s, the www redirect, or a custom 404. Redirects would have to go in a new `.htaccess` that the build copies. |
| Tailwind runtime from `cdn.tailwindcss.com` on every page | `shared/head-assets.html` | The CDN build is development-oriented; it blocks render and adds layout shift. Not measured here. |

### 4.2 Thin and duplicate pages

- 43 pages under 200 words; the learn articles are mostly three short lists under a one-sentence definition.
- Five `/for/` pages share one template and differ by about five bullets (68 to 87 words each).
- The "benchmarks" pages (`wire-transfer-fee-benchmarks`, `corporate-cash-yield-benchmarks`) contain no numbers.
- `learn/treasury-management-software` and `learn/best-treasury-software-for-mid-market-companies` share one meta description and an identical opening sentence.
- `/templates/` is a hub for one template (64 words).
- Pages that already meet a reasonable standard: `compare/cashlytica-vs-kyriba` (719), `learn/kyriba-pricing` (695), `learn/earnings-credit-rate` (436), `samples/bank-fee-audit-report`, `faq`, `learn/bank-fee-audit`.

### 4.3 Keyword cannibalisation

| Query | Pages competing | Suggested split |
|---|---|---|
| 13 week cash forecast | `learn/13-week-cash-forecast`, `templates/13-week-cash-forecast`, `use-cases/13-week-cash-forecast`, `samples/13-week-forecast`, `learn/common-13-week-forecast-mistakes`, `learn/weekly-cash-forecasting-for-cfos`, `learn/cash-forecast-accuracy` | One pillar (informational), one template (the "template" query), one sample (proof); fold the use-case, mistakes and weekly notes into the pillar. Search Console's best query is "13-week cash forecasting" (93 impressions, position about 85). |
| idle cash | `learn/idle-cash`, `idle-cash-drag`, `how-much-cash-should-a-business-keep`, `operating-cash-vs-reserve-cash`, `corporate-cash-yield-benchmarks`, `money-market-funds-vs-treasury-bills-vs-sweep-accounts`, `use-cases/idle-cash-yield`, `tools/idle-cash-calculator`, `samples/idle-cash-recommendation` | Pillar = idle-cash-drag; calculator and sample stay; cash-buffer page absorbs operating-vs-reserve; MMF/T-bill page and the benchmarks page stay only if they carry sourced rates. |
| bank fee audit | `learn/bank-fee-audit`, `use-cases/bank-fee-audit`, `samples/bank-fee-audit-report`, `tools/bank-fee-calculator` (home also) | Learn = "what it is"; use-case = transactional "$99 audit service"; sample = proof; calculator = tool. Titles currently all start "Bank Fee Audit". |
| cash position dashboard | `learn/cash-position-dashboard`, `use-cases/cash-position-dashboard` | Same H1, same query. Merge the use-case into the learn page. |
| treasury management software | `learn/treasury-management-software`, `learn/best-treasury-software-for-mid-market-companies`, `learn/treasury-automation-for-finance-teams`, `for/mid-market-companies` | One pillar; the others fold in. |
| reconciliation | `learn/bank-reconciliation-automation`, `use-cases/reconciliation`, `for/controllers` | One page, with honest scope (bank/books matching is human-confirmed, no write-back). |
| board reporting | `use-cases/board-reporting`, `samples/board-briefing`, `for/cfos` | Sample is the page; board packs are Director-only and should be said so. |
| Kyriba | `compare/cashlytica-vs-kyriba`, `learn/kyriba-pricing` | Intentional and correctly cross-linked (comparison versus pricing). Keep both. |

### 4.4 Internal voice in public copy

Sentences written as instructions to the editor, each live today:

- Footer (all 58 pages): "Traffic, proof, and conversion for finance teams..." and "Public brand: Cashlytica."
- `/compare/cashlytica-vs-mercury/`: "Cashlytica should emphasize neutrality across the accounts the company already uses..."
- `/compare/cashlytica-vs-trovata/`: "Cashlytica should feel more like an advisor..." and "The page should make the difference obvious without pretending the categories are the same."
- `/compare/`: "What these pages should answer" and "the page should stay honest, specific, and useful".
- `/faq/`: "The FAQ should make the next step feel obvious and safe."
- `/security/`: "The trust story should give buyers enough clarity to proceed without guessing about the basics."
- `/tools/` and both calculators: "The calculator should create enough curiosity that the buyer wants to see the actual report."
- `/templates/`: "Offer a template before asking for a signup."
- `/for/*`: "The page should make the CFO feel that the product is built for their style of review." and "Position the product as right-sized and practical."
- `/learn/how-to-negotiate-bank-fees/`: "Cashlytica should help buyers gather the line items, benchmark them..."
- `/learn/treasury-management-software/`: "Keeps the public story grounded in real outputs."
- `/samples/`: "Why these are real samples".
- Engineering terms: "golden fixtures" (13-week sample and idle-cash sample, including their meta descriptions), `ReportingService`, `ForecastService`, `BoardPackService`.

### 4.5 Contradictory proof numbers

| Source | Figure |
|---|---|
| `/` example finding | $18,240 annual savings (wire fees 32% above range, duplicate monthly fee, idle cash 1.8% below) |
| `/samples/` and `/samples/board-briefing/` | $1,800 annual savings from the fee audit |
| `/samples/bank-fee-audit-report/` | $190 monthly fees, $2,280 annualised, **$720** opportunity ($480 + $240); arithmetic checks |
| `/learn/bank-fee-audit/` | Same $480 example; consistent with the report page |
| `/samples/board-briefing/` | $3.5M excess cash, beside a forecast whose balance is about $1.0M to $1.1M |
| `/samples/13-week-forecast/` | Titled 13-week; shows 4 weeks, weeks 3 and 4 blank; forecast start 2026-06-01 (five months old) |

The PRD asked for a concrete homepage example, but the homepage example is the only figure not labelled illustrative anywhere on the page, and it matches no sample.

### 4.6 Links, orphans and hubs

- **Broken internal links: 0** across all 58 pages. **Sitemap vs pages: exact match** (58 and 58, no extras, no omissions).
- `/learn/` links 11 of the 24 articles. Unlisted: `bank-reconciliation-automation`, `best-treasury-software-for-mid-market-companies`, `cash-forecast-vs-cash-flow-statement`, `common-13-week-forecast-mistakes`, `common-business-bank-fees`, `earnings-credit-rate`, `how-much-cash-should-a-business-keep`, `how-to-negotiate-bank-fees`, `kyriba-pricing`, `money-market-funds-vs-treasury-bills-vs-sweep-accounts`, `operating-cash-vs-reserve-cash`, `treasury-automation-for-finance-teams`, `weekly-cash-forecasting-for-cfos`. The hub's own copy names ECR and negotiation but links neither.
- `learn/cash-forecast-vs-cash-flow-statement` is a true orphan: no body links in and not on the hub.
- The homepage links to the learn hub, compare hub, security, samples and one calculator, but not to the bank fee calculator or any individual learn article (the PRD asked for links to top articles and tools).
- The header has no Templates or Pricing link; `/templates/` has one inbound body link.
- 28 of 58 pages have no link to the app other than the header and footer. That includes 17 of 24 learn articles, 4 of the 5 persona pages (`/for/cfos`, `/controllers`, `/finance-teams`, `/mid-market-companies`) and 6 of the 7 use-case pages (all but `cfo-treasury-advisor`). Those pages rely on internal links to reach a CTA, and the learn pages that do convert are the bank-fee ones.

### 4.7 Dates and freshness

- No page shows a published date. No Article JSON-LD has `datePublished`; only 5 pages have `dateModified` (all 2026-10-21): the Kyriba comparison, Kyriba pricing, ECR, bank-fee-audit, and the sample audit report.
- `sitemap.xml` has no `lastmod`; every entry is `monthly`; priority 1.0 for the home page and 0.8 for the other 57.
- Visible "Reviewed October 21, 2026" appears only on the two Kyriba pages (nine days old; fine).
- Sample fixtures carry stale dates: forecast start 2026-06-01, audit month January 2026.
- Docs are stale: `remaining-tasks.md` (updated 2026-06-14) lists all tasks done except one blocked; `PRD.md` "Current State" still describes three learn pages; the only growth report is from 2026-07-07, and its instrumentation gaps pre-date `shared/analytics.js` (first committed 2026-08-08).

### 4.8 Unsourced claims

Only 3 of 58 pages cite any external source (`compare/cashlytica-vs-kyriba`, `learn/kyriba-pricing`, `learn/earnings-credit-rate`). Unsourced and presented as fact or benchmark:

- Wire fee "typical range" with no figure; "yield assumptions should use a real benchmark" with none given; the calculator's default 4.75% "available yield".
- Homepage: "Wire fees: 32% above expected range", "Idle cash: earning 1.8% below available alternatives".
- Competitor characterisations on the Mercury, Ramp and Trovata pages ("Modern SMB banking workflows", "Established treasury category presence") with no source or date, against the Kyriba page's standard of dated vendor citations.
- Benchmarks used by the bank fee audit ("compares them to a benchmark baseline"): the source of the baseline is never stated, only that the sample's $25 and $15 comparison rates are illustrative.
- ECR page: formula and worked example verified by arithmetic ($900,000 x 1.50% x 30 / 365 = $1,109.59; $1,500 - $1,109.59 = $390.41). Its AFP deep link now lands on the AFP home page.

### 4.9 "TAS" in public copy

**None.** Case-insensitive whole-word search across the rendered site (HTML, XML, JS) and the repository source found no "TAS" or "Tas". It appears only in `docs/PRD.md` and `docs/remaining-tasks.md` as the instruction not to use it (and those docs are themselves public, see 4.1). Related naming risks:

- **"Cassius"** appears 13 times in the homepage's visible text and meta (18 counting social tags and structured data), including its title, H1, meta description and JSON-LD, plus once on the samples hub and once on `use-cases/cfo-treasury-advisor`. The PRD's public brand is Cashlytica and its recommended hero is "You're losing cash. Cashlytica shows you where." The name does exist in the product code (it is a UI panel), but what it can do is not in the feature inventory. Owner decision needed.
- Old ladder language: the PRD bans "Cash Intelligence", "Optimize → Operate → Execute" and Connected as a standalone rung. "Cash intelligence" survives only in the homepage `SoftwareApplication` JSON-LD description, not in visible copy. The buyer-visible ladder is Free, Fee Audit, Analyst, Manager, Director, Treasurer.

### 4.10 Metadata and structured data

- All 58 pages: unique title, one H1, canonical correct, og:title/description/image/url/type and twitter:card present, `lang` and viewport present. Titles over 60 characters: 4; meta under 70 characters: 8; over 160: 2.
- 32 titles use the pattern "X — Cashlytica", several repeating the brand ("Cashlytica vs Mercury — Cashlytica"); use-case titles read "Bank Fee Audit for Cashlytica".
- Duplicate meta description: TMS and best-treasury-software. Duplicate H1: both cash-position-dashboard pages.
- **og:image is SVG on 57 pages and absent on `learn/kyriba-pricing`** (which also has `twitter:card=summary` and no twitter:image). Most social scrapers do not render SVG; PNG or JPEG is the reliable choice.
- **No favicon link on any page.**
- **No BreadcrumbList** on any page, though the PRD asks for it on learn pages. Article JSON-LD has author and publisher as the organisation only.
- Home JSON-LD: `Organization` has no logo or `sameAs`; `SoftwareApplication` has no `offers`; descriptions say "Cassius-led AI treasury services".
- `FAQPage` JSON-LD exists with 8 questions matching the page.

### 4.11 Conversion and analytics

- **Every app-bound CTA goes to `https://app.cashlytica.com/register/` with no query string,** whether labelled "Run the $99 audit", "Check idle cash yield", "Generate the forecast" or "Explore the product". The PRD's "app handoff by source page" cannot be measured from the site side, and a visitor who clicks "Run the $99 audit" lands on a generic signup.
- No pricing is shown except $99. The inventory shows Analyst at $199 a month, Manager $1,499, Director $5,999 (sales-led) in the app; whether those may be published is an owner decision (inventory open question 4).
- No contact route: no `mailto:`, form or sales link, although Director is sales-led and `/security/` says "Ask us for our tenant-isolation explanation".
- `shared/analytics.js` classifies clicks by regex on the link's href and text:
  - Anything containing "audit" or "register" fires both `registration_start` and `cta_click`, so links such as "Sample audit report", "Bank fee audit →" and the security card (its text contains "audit") are recorded as registration starts. Simulating the classifier over the rendered site gives 13 distinct link-text and target pairs that misfire this way, none of them register links.
  - "sample" or "report" in the text fires `report_view`, a click event, so a visitor who lands directly on a sample page from search is never counted.
  - "calculator" in an href fires `calculator_start` on the link click, not on first input.
  - There is no login-click event; `data-analytics-label` is not used anywhere.
  - Only the two calculators fire `calculator_complete` (on button click).
- Compared with the 2026-07-07 report's gaps: CTA, form, email and calculator events now exist in code, but they are noisy; scroll depth and login clicks are still missing.

### 4.12 Missing against the PRD

`/case-studies/` (PRD section 8) was never built, so the homepage "Proof" block has no case study or benchmark; no pricing page; no about or contact page; no email-capture offer (checklists); no BreadcrumbList or `SoftwareApplication` offers; the homepage does not use the PRD hero and shows six ladder rungs (with Fee Audit) where the PRD lists five.

## 5. Product claims register

Marked against `/tmp/cashlytica-tas-features.md`.
**TRUE** = the inventory shows a shipped path matching the claim as worded. **FALSE** = the inventory contradicts it or lists it under "must not claim". **UNVERIFIED** = the inventory marks the area PARTIAL or says nothing, or the claim concerns conditions the code cannot establish. Note the inventory's own caveat: SHIPPED means code exists, not that it is deployed; the release checklist says "not ready for release" (2026-10-25).

| # | Page | Claim (as published or closely paraphrased) | Verdict | Basis |
|---|---|---|---|---|
| H1 | `/` (title, H1, meta, JSON-LD) | "AI treasury services powered by Cassius", "AI treasury advisor", "intelligent treasury partner" | UNVERIFIED | No AI-advisor row in the inventory; chat is user-initiated; decision memos exist. |
| H2 | `/` | Cassius "reviews your data, finds fee leakage" | TRUE | Bank fee audit SHIPPED. |
| H3 | `/` | "spots idle cash" | TRUE | Idle-balance detection exists. |
| H4 | `/` | "turns the findings into CFO-defensible next steps" (recommendations) | UNVERIFIED | Yield recommendations PARTIAL: venue rates and availability unverified. |
| H5 | `/` | "Start with the $99 fee audit", "$99 one-time audit" | TRUE | $99 one-time charge. |
| H6 | `/` | "No long implementation. Cassius starts working the first session." | UNVERIFIED | End-to-end onboarding not accepted; Free has zero connections. |
| H7 | `/` | Cassius "keeps going with monitoring" / "keeps working" | UNVERIFIED | Continuous monitoring and delivery cadence UNVERIFIED. |
| H8 | `/` | Example finding: "$18,240 ... Wire fees 32% above expected range ... duplicate monthly fee ... Idle cash earning 1.8% below alternatives" | UNVERIFIED | No source; contradicts the sample pages ($720, $1,800). |
| H9 | `/` | Free: "Preview fees, yield, or forecast basics without a sales call" | FALSE | Free is the fee teaser and public tools only; forecasts start at Analyst. |
| H10 | `/` | Fee Audit: "$99 one-time audit that identifies overpayments and credits forward" | TRUE | One-time $99 credit on the first subscription invoice when eligible. |
| H11 | `/` | Analyst: "Cash visibility, fee audits, forecasts, alerts, and grounded recommendations" | TRUE | Matches the Analyst entitlements; alert cadence not promised. |
| H12 | `/` | Manager: "Connected feeds, accounting data" | UNVERIFIED | Plaid/QBO/Xero PARTIAL; live acceptance open. |
| H13 | `/` | Manager: "intraday positioning" | FALSE | "Real-time" and "guaranteed intraday balances" are on the must-not-claim list. |
| H14 | `/` | Manager: "reconciliation" | UNVERIFIED | Bank/books matches need human confirmation, no write-back; "automatic reconciliation" is must-not-claim. |
| H15 | `/` | Director: "board packs, covenants, ... multi-entity views" | TRUE | Board packs, debt/covenants and entities shipped (Director). |
| H16 | `/` | Director: "Yield, FX, concentration, credit" | UNVERIFIED | FX/concentration are listed under Manager; yield PARTIAL; "credit" not in the inventory. |
| H17 | `/`, `/faq/` | A "Treasurer" rung: "Supervised recommendations under dual control; your team executes" | UNVERIFIED | No Treasurer plan in pricing; the nearest item is the separate sales-granted Execution module. High priority. |
| H18 | `/` | Sample audit: "Read a full fee audit before you buy" | FALSE | The sample is a one-month, two-line synthetic excerpt. |
| H19 | `/` | "If it does not [find value], you still get useful signal and a clear next step" | TRUE | A purchased audit is refunded when no meaningful finding; the site never says so. |
| S1 | `/samples/` | "Real sample outputs", "Cassius-generated artifacts, not placeholder mockups", "Actual sample outputs" | FALSE | Report page: "synthetic example"; others: "illustrative", "fixture"; footer: "Sample figures are illustrative". |
| S2 | `/samples/`, `/samples/board-briefing/` | "$1,800 annual savings identified in the fee audit" | FALSE | The report page derives $720 from the same $190 and $35 inputs. |
| S3 | `/samples/` | Figures "taken from the current Cashlytica service outputs and fixtures" | UNVERIFIED | Fixtures not examined by the inventory. |
| S4 | `/samples/13-week-forecast/` | "Model version v1.0.0", "confidence 0.98", "Seasonality: thin data / industry priors" | UNVERIFIED | Forecast SHIPPED; these fields are not inventoried. |
| S5 | `/samples/13-week-forecast/` | Scenarios (optimistic / pessimistic) | TRUE | Forecast scenarios shipped. |
| S6 | `/samples/board-briefing/` | Board pack with cash position, forecast, fee audit, actions | TRUE | Director board packs shipped; the page omits that it is Director-only. |
| S7 | `/samples/board-briefing/` | "$3,500,000 in excess cash" | UNVERIFIED | Fixture; inconsistent with the ~$1M forecast on the sibling page. |
| S8 | `/samples/idle-cash-recommendation/` | "The exact recommendation structure produced by the current ReportingService" | UNVERIFIED | Service not inventoried; yield recommendations PARTIAL. |
| S9 | `/samples/bank-fee-audit-report/` | "$190 fees, $2,280 annualised, $720 opportunity; not a customer report" | TRUE | Arithmetic ties; labelled synthetic. |
| F1 | `/faq/` | "Upload the bank statements or analysis statements you want reviewed" | FALSE | Accepted: CSV, XLSX, BAI2, MT940. PDF statement intake is not supported, and most statements are PDFs. |
| F2 | `/faq/` | "Can I redact statements? Yes, but keep the fee lines visible" | UNVERIFIED | Redaction handling is not inventoried. |
| F3 | `/faq/` | "Does Cashlytica move money? No ... does not move money" | FALSE | A payment-execution path exists (sandbox default, sales-granted module, policy and dual control) and Manager+ stage payments. True only for the audit and Analyst. |
| F4 | `/faq/` | "software and advisory support" | UNVERIFIED | No human advisory service in the inventory. |
| F5 | `/faq/` | "an automated review of your fee data" | TRUE | The report code analyses stored transactions. |
| F6 | `/faq/` | "What happens if no savings are found? ... straightforward answer" | TRUE | Incomplete: the code refunds the audit; the site never states the refund. |
| F7 | `/faq/` | "Analyst is the first paid operating level for cash visibility, fee audits, forecasts, alerts, and grounded recommendations" | TRUE | Matches Analyst. |
| F8 | `/faq/` | "Do I need live bank connections? No ... uploaded documents" | TRUE | Uploads shipped; feeds are Manager+. |
| F9 | `/faq/` | Audit "can be credited forward" to Analyst, Manager, Director or Treasurer | TRUE for Analyst, Manager, Director; UNVERIFIED for Treasurer | $99 credit on first subscription invoice when eligible; eligibility terms are not stated on the site. |
| SEC1 | `/security/` | "Customer isolation ... who can see what" | TRUE | Company scoping and roles are enforced in routes. Database-level isolation is not established. |
| SEC2 | `/security/` | "The product analyzes and recommends" (as the whole description) | FALSE | Omits payment staging and the execution module. |
| SEC3 | `/security/` | "not a bank, not a money transmitter" / "decision-support layer, not a custody layer" | UNVERIFIED | Legal posture; the code cannot establish it. |
| SEC4 | `/security/` | "Minimum necessary data ... the workflow should stay narrow" | UNVERIFIED | Process claim, not code. |
| C1 | `/compare/cashlytica-vs-kyriba/` | "Positioning across connected accounts, with related cash-analysis workflows" | UNVERIFIED | Bank feeds PARTIAL. |
| C2 | same | "13-week forecasts, forecast-versus-actual review, and sample outputs" | TRUE | Forecast and accuracy views shipped. |
| C3 | same, `/learn/kyriba-pricing/` | "$99 one-time bank-fee audit" | TRUE | |
| C4 | same | "Decision support and recommendations; your team executes financial actions." | FALSE | Stated as a blanket; payment staging and a gated execution path exist. |
| C5 | same, `/learn/kyriba-pricing/` | Kyriba facts (10,000+ banks, no public price, module list), "reviewed October 21, 2026" | UNVERIFIED | Third-party claims cited to kyriba.com; not re-verified. |
| C6 | `/compare/cashlytica-vs-mercury/` | Cashlytica is "neutral across banks", "works across banks" | UNVERIFIED | Plaid where supported plus uploads; "universal bank coverage" is must-not-claim. |
| C7 | Mercury, Ramp, Trovata pages | Competitor characterisations (bank-native, spend controls, "established treasury category presence") | UNVERIFIED | Third-party, undated, unsourced. |
| C8 | `/compare/cashlytica-vs-trovata/` | The system will "explain what the numbers mean and what to do next" | UNVERIFIED | Recommendations PARTIAL; chat is user-initiated. |
| C9 | `/compare/cashlytica-vs-spreadsheets/` | "a repeatable operating workflow, a cleaner audit trail" | UNVERIFIED | Audit logs exist; the trail's coverage of forecast edits is not inventoried. |
| C10 | `/for/mid-market-companies/` | "without a six-figure implementation or a staffed treasury department", "Fast setup", "Right-sized pricing motion" | UNVERIFIED | No implementation evidence; Director list is $5,999 a month. |
| L1 | `/learn/bank-fee-audit/` | "Groups fee lines and compares them to a benchmark baseline. Surfaces the biggest dollar deltas first." | UNVERIFIED | Report exists; the benchmark source is not established. |
| L2 | `/learn/bank-fee-audit/` | "Turns the findings into a report the CFO can take to the bank" | TRUE | Audit report and PDF shipped. |
| L3 | `/learn/treasury-management-software/` | "Expands into ongoing monitoring when there is enough value" | UNVERIFIED | Continuous monitoring cadence UNVERIFIED. |
| L4 | TMS and best-treasury pages | Selection criteria used as self-description: "multi-bank neutrality", "fast setup" | UNVERIFIED | As C6 and C10. |
| L5 | `/learn/cash-forecast-vs-cash-flow-statement/` | "Use Cashlytica to keep both grounded in the same source data." | UNVERIFIED | A cash-flow statement PDF exists; same-source behaviour not inventoried. |
| L6 | `/learn/treasury-automation-for-finance-teams/` | Automation candidates presented as what Cashlytica does: forecast updates, reconciliation matching, briefing generation, alerting, fee comparison | UNVERIFIED | Briefing and fee analysis shipped; alert cadence and automatic matching are not. |
| L7 | `/learn/how-to-negotiate-bank-fees/` | "Cashlytica should help buyers gather the line items, benchmark them, and ask for the specific adjustment" | UNVERIFIED | Benchmarking source unestablished; the sentence is also editor-voice. |
| U1 | `/use-cases/13-week-cash-forecast/` | "Weekly ending cash by bucket or account", "clear risk flags", "variance notes travel with the number" | UNVERIFIED | Forecast, overrides and actuals shipped; flags and variance notes are not inventoried. |
| U2 | `/use-cases/bank-fee-audit/` | "The audit gives the team a concrete number" | TRUE | |
| U3 | `/use-cases/board-reporting/` | "board-ready language ... concise and defensible" | TRUE | Director board packs only; tier not disclosed. |
| U4 | `/use-cases/cash-position-dashboard/` | "Cash by account, entity, or bucket" | TRUE | Cash position shipped by entity and account. |
| U5 | same | "Change from the prior period", "flags for what moved the number" | UNVERIFIED | Not inventoried. |
| U6 | `/use-cases/cfo-treasury-advisor/` | "a treasury operating relationship with recurring briefs", "Cassius should keep working as data changes" | UNVERIFIED | Weekly and daily memo endpoints exist; cadence and any human relationship are not established. |
| U7 | `/use-cases/idle-cash-yield/` | "recommendation explains why the move is safe", "compared against realistic alternatives" | UNVERIFIED | Venue rates and availability UNVERIFIED. |
| U8 | `/use-cases/reconciliation/`, `/for/controllers/` | "Exceptions need a clear queue", "cleaner matching", "better trust in the underlying data" | UNVERIFIED | Matches need human confirmation; no write-back. |
| T1 | `/tools/bank-fee-calculator/` | Output "Estimated annual overpayment" | FALSE | Output is the entered monthly fees x 12 (total fees), never an overpayment. |
| T2 | `/tools/idle-cash-calculator/` | Yield drag = (balance - buffer) x (available - current yield) | TRUE | Code does exactly this; the 4.75% default is an unsourced assumption. |
| TP1 | `/templates/13-week-cash-forecast/` | "Pulls the same logic into a live system", "pairs the forecast with recommendations and a briefing" | UNVERIFIED | "Live" is must-not-claim; weekly briefing is shipped. |
| TP2 | `/templates/13-week-cash-forecast/` | CTA "Generate the forecast" leads to signup | UNVERIFIED | Free cannot generate a forecast; forecasts start at Analyst. Expectation mismatch. |

Counts: 70 claims. TRUE 22, FALSE 10, UNVERIFIED 37, and one split row (F9: TRUE for Analyst, Manager and Director, UNVERIFIED for Treasurer). The FALSE rows are H9, H13, H18, S1, S2, F1, F3, SEC2, C4 and T1.
Two truths that the site understates, both useful: the audit **is** refunded when no meaningful finding (H19, F6) and the $99 **is** credited against the first subscription invoice (F9). Stating both plainly would answer the PRD's FAQ questions better than the current wording.

Not claimed anywhere on the site, and so far correct: SOC 2, SSO, NetSuite/Sage, direct bank protocols, real-time balances ("real-time" does not appear in the copy), guaranteed savings or accuracy. The sample audit page and the Kyriba pages are careful on guarantees; keep that standard.

## 6. Deploy workflow review (`.github/workflows/deploy.yml`) — reported, not changed

The richiest fix was commit `636d62e` ("Pin the deploy workflow to Ubuntu 24.04, which Playwright supports"). Comparison:

| Item | Cashlytica today | richiest (current) | Assessment |
|---|---|---|---|
| Runner | `ubuntu-latest` | `ubuntu-24.04` | **The Playwright break does not affect this repo today**: there is no `package.json`, Node setup or Playwright step. It will recur the day an e2e job is added on `ubuntu-latest`. Pin `ubuntu-24.04` when adding one. |
| Tests before deploy | None. Deploys on every push to `main` | `test` job with `needs: test`; also runs on pull requests | No gate at all: a broken build, a leaked `localhost:5173`, a sitemap mismatch or a missing include publishes straight away. |
| Triggers | `push` to `main` only | push and pull request | Nothing is checked on a PR. |
| FTP protocol | No `protocol:` set | `protocol: ftps`, `port: 21` | The action's default is plain FTP, so credentials and files would go unencrypted unless the host forces TLS. Verify against the v4.3.5 README and the host; set `protocol: ftps` if the host supports it. |
| Server dir | `server-dir: /` | `${{ secrets.FTP_PATH }}` | Fine if `/` is the web root; confirm. |
| Build safety | `build.py` falls back to `http://localhost:5173` if `CASHLYTICA_APP_ORIGIN` is unset | n/a | The workflow sets it, so output is correct today. A cheap post-build assertion (no `localhost`, no `{{APP_ORIGIN}}`, no `docs/`) would stop a regression. |
| IndexNow | Submits all 58 URLs on every push, including docs-only pushes | Same pattern | Harmless but noisy; also a failure here fails the job after files were already uploaded. |
| Concurrency | None | None | Two quick pushes can race the FTP sync. |

Also relevant from section 4.1: the build copies `docs/`. A pre-deploy check that the output tree contains only intended paths is the matching control.

## 7. Decisions needed from the owner before any edits

1. Remove `docs/` from the deploy now (and confirm the three live files disappear after the next deploy). Hold this audit and `tas-features.md` out of `main` until then.
2. Is "Cassius" a public brand name? If not, the homepage, JSON-LD and three other pages change; if so, what may it be said to do?
3. May plan prices ($199, $1,499, $5,999) and the 30-day trial be published? The inventory cannot confirm live Stripe prices or that the trial is offered to every buyer.
4. Is there a "Treasurer" tier? The inventory shows an Execution add-on, not a tier. Also decide how the site describes payments honestly: staging and approvals exist, execution is separately granted, and live rails are not accepted for release.
5. Agree the consolidation: 58 to 39 pages (section 3), with a redirect file.
6. The statement-format limit (no PDF) should reach the FAQ and the audit page before more traffic arrives, because the $99 audit is the primary conversion.
7. Social images: replace SVG with PNG/JPEG (1200x630) and add a favicon.
