# Cashlytica content plan: drop / revise / create (draft, 2026-10-30)

Built from scratch, not from the existing page list: what Tas does today (`tas-features.md`, SHIPPED first, PARTIAL only with its honest scope, nothing on the must-NOT-claim list), crossed with what a finance lead at a 1-to-15-entity company on QuickBooks Online or Xero searches for, then checked against the verdicts in `seo-editorial-audit.md`. Every page names the one Tas screen that answers its question, using the app's own navigation and tab labels (`frontend/src/App.tsx`, `pages/hubs/*.tsx`).

Status: planning only. No page, partial or script was changed for this file. Nothing is committed.

## How to read this

- **Queries are hypotheses, not volume data.** Search Console showed 46 impressions and 0 clicks in the week to 2026-07-06, so there is no demand evidence on this site. Targets come from the job a buyer is doing, and each P1 page should be checked against Search Console after about six weeks.
- **Screen names** are written `Nav > Tab (Component.tsx)`. Tas nav labels: Overview, Cash, Forecast, Savings found, Data sources, Payables, Receivables, Reports, Debt & covenants, Investments & FX, Settings. Tab labels below are the ones in the hub files.
- **Tier gating in the UI** is noted where it limits what a page may say. Design partners get full access, but a public page must not imply a screen is available on a plan that lacks it. Plans and pricing are not published (owner decision: "set with design partners"), so no page below names a price or a tier ladder.
- **Not on the plan, by rule:** anything on the inventory's must-NOT-claim list: live or production-ready, real-time or intraday, direct bank APIs, NetSuite or other ERPs, automatic reconciliation or write-back, "moves your money" as a general feature, guaranteed accuracy or savings, SOC 2, SSO, unlimited banks or entities.

## Priority rule

Tas is pre-release and the site's job is to recruit five design partners.

- **P1:** a CFO, controller or treasurer with a live 13-week-forecast, multi-bank, multi-entity or bank-fee problem would search for it, and the page makes the design-partner offer credible (it shows a shipped screen doing that exact job). About ten pages.
- **P2:** long-term search value, or a fix that matters but does not move recruitment this quarter.
- **P3:** later, or the feature is PARTIAL and the page should wait until a design partner has used it.

## 1. Drop / merge (301 the URL, keep the useful parts)

Starting point: the audit's 58 to 39 consolidation, plus two further merges forced by the owner decisions made since (marked **new**). `/design-partners/` was added after the audit, so the site is 59 pages today and 38 after these merges. `.htaccess` now exists in the repo; each row below becomes one `RewriteRule ^old/?$ /target/ [R=301,L]`, and each old URL leaves `sitemap.xml` (the build derives the sitemap from the pages, so deleting the file does that).

| Page | Merge into (301 target) | Why |
|---|---|---|
| `/compare/cashlytica-vs-mercury/` | `/compare/` | Mercury is a bank, not a treasury-analytics rival; 139 unsourced words. Keep one paragraph on "bank dashboard vs. multi-bank view" in the hub. |
| `/compare/cashlytica-vs-ramp/` | `/compare/` | Ramp is spend management; 209 unsourced words. Same treatment. |
| `/for/cfos/` | `/for/` | 77 words from one three-bullet template; no search demand of its own. |
| `/for/controllers/` | `/for/` | 68 words, same template; "cleaner matching" is an unverified claim. |
| `/for/finance-teams/` | `/for/` | 74 words, same template. |
| `/for/founders/` | `/for/` | 87 words, same template. `/for/` becomes one persona page with a section per role. |
| `/for/mid-market-companies/` | `/learn/treasury-management-software/` | Same query as the TMS pillar; "no six-figure implementation" is unsupported. |
| `/learn/best-treasury-software-for-mid-market-companies/` | `/learn/treasury-management-software/` | Same meta description and near-identical lead; names no alternatives, so it cannot satisfy a "best" query. |
| `/learn/treasury-automation-for-finance-teams/` | `/learn/treasury-management-software/` | 107 words; its automation list reads as a product description the inventory does not support. |
| `/learn/common-13-week-forecast-mistakes/` | `/learn/13-week-cash-forecast/` | 126 generic words, one inbound link; becomes a "mistakes" section in the pillar. |
| `/learn/weekly-cash-forecasting-for-cfos/` | `/learn/13-week-cash-forecast/` | The cadence section belongs in the pillar. |
| `/use-cases/13-week-cash-forecast/` | `/learn/13-week-cash-forecast/` | Fourth page on one query (learn, template, sample, use case). |
| `/learn/idle-cash/` | `/learn/idle-cash-drag/` | 134 words; the definition duplicates the drag page. |
| `/use-cases/idle-cash-yield/` | `/learn/idle-cash-drag/` | Same query as the calculator and drag page; "why the move is safe" is unsupported. |
| `/learn/operating-cash-vs-reserve-cash/` | `/learn/how-much-cash-should-a-business-keep/` | The same decision as the cash-buffer page. |
| `/use-cases/cash-position-dashboard/` | `/learn/cash-position-dashboard/` | Identical H1 and query; 163 words. |
| `/use-cases/reconciliation/` | `/learn/bank-reconciliation-automation/` | 79 words; product matching is human-confirmed with no write-back, so the claims need one careful home. |
| `/use-cases/board-reporting/` | `/samples/board-briefing/` | 86 words; board packs are Director-tier and the use case never says so. |
| `/templates/` | `/templates/13-week-cash-forecast/` | A one-item hub adds nothing until there is a second template. |
| `/use-cases/bank-fee-audit/` (**new**) | `/learn/bank-fee-audit/` | The audit planned to make it the transactional "$99 audit" page. With the $99 audit no longer promoted, it is a fourth page on the same query. |
| `/use-cases/cfo-treasury-advisor/` (**new**) | `/design-partners/` | The audit planned it as the home for the operating-level and pricing content. That content is not being published; the design-partner page now answers "what do I get and what does it cost". Title, slug and hub label disagreed anyway. |

After these merges `/use-cases/` has one page left (`/use-cases/` hub only, nothing to list). Recommend dropping the hub too, folding its three jobs into `/` and `/for/`, and 301ing it to `/for/`. That is one more merge and would take the site to 37; it is left out of the totals because it was not in the audit and needs your call.

## 2. Revise (32 pages)

Verdict Revise in the audit, minus the two moved to section 1. The five Keep pages are in the next table.

| P | Page | Target query | Change | Tas screen |
|---|---|---|---|---|
| P1 | `/learn/13-week-cash-forecast/` | 13 week cash flow forecast | **Pillar.** Absorbs the three merged pages. A worked 13-week example end to end (opening cash, receipts, disbursements, closing, minimum-cash line), where each line comes from (bank balance, AR/AP aging, payroll calendar), and a weekly review routine. Add a "mistakes" section and sources. Do not promise accuracy. | Forecast > Forecast (`Forecast.tsx`); edits in Forecast > Edit (`EditForecast.tsx`) |
| P1 | `/templates/13-week-cash-forecast/` | 13 week cash flow forecast template | Fail today: says "copy into a spreadsheet" and gives six row names. Ship a real table on the page plus a downloadable CSV/XLSX with formulas and a filled example. Include a note on mapping QuickBooks/Xero exports to the rows. | Forecast > Forecast (`Forecast.tsx`), Forecast > Edit (overrides) |
| P1 | `/compare/cashlytica-vs-spreadsheets/` | excel cash forecasting alternative / treasury spreadsheet alternative | Highest-converting comparison in the PRD; 133 words and an editor-voice meta. Rebuild: where spreadsheets are the right answer, where they break (version drift, multi-bank consolidation, bank vs. book check), a table, no overclaiming. | Forecast > Scenarios (`Scenarios.tsx`), Cash > Position (`CashPosition.tsx`) |
| P1 | `/learn/bank-fee-audit/` | bank fee audit / how to audit bank fees | Becomes the single wedge page (absorbs the use-case page). Keep the worked math, add an annotated statement excerpt, a sourced benchmark basis and `datePublished`. Describe the bank fee review as something design partners get; no $99 pitch. | Savings found > Fee review (`AuditReport.tsx`) |
| P1 | `/faq/` | (trust page) cashlytica faq | Rewritten once already for formats and cost. Still to do: money movement answer (F3 below), what the pre-release program is, which banks connect (Plaid where supported), what is not supported (PDF statements, ERPs other than QuickBooks Online and Xero), data handling. Add `FAQPage` entries for each. | Data sources > Upload (`Upload.tsx`), Data sources > Connections (`Integrations.tsx`) |
| P1 | `/samples/13-week-forecast/` | sample 13 week cash flow forecast | Shows 4 weeks with 2 filled, not 13. Show all 13 weeks (synthetic, labelled), the minimum-cash line and one scenario, and drop the "golden fixture" and "Source shape" notes. This is the strongest proof asset for the offer. | Forecast > Forecast (`Forecast.tsx`), Forecast > Scenarios |
| P1 | `/security/` | (trust page) cashlytica security | Buyers share bank data with a pre-release product, so this page decides applications. State only verified controls: password auth with login throttling, encrypted sensitive fields, audit logs, role checks, company scoping. Say how bank feeds connect (Plaid where supported) and what is read-only. No SOC 2, no SSO, no "end-to-end". Add a contact route (the `mailto:` now exists). | Settings > Team (`TeamMembers.tsx`), Data sources > Connections |
| P2 | `/` | (brand) cash position and forecasting for finance teams | Hero already leads with the program. Still to do: title/meta/JSON-LD (`"Cassius-led AI treasury services"`), the $18,240 example that contradicts the samples, and the "How Cassius works" band, per your Cassius decision. | Overview (`Dashboard.tsx`), Cash > Position |
| P2 | `/compare/` | treasury software comparison | Hub for three pages after the merges (Kyriba, Trovata, spreadsheets) plus the short Mercury/Ramp paragraph. Remove editor-voice copy. | None (index page) |
| P2 | `/compare/cashlytica-vs-trovata/` | cashlytica vs trovata / trovata alternative | Direct competitor; 139 words with undated claims. Rebuild to the Kyriba page standard: vendor-sourced, dated, hedged. **Deliver.** | Cash > Position, Forecast > Forecast |
| P2 | `/learn/` | treasury guides | Link all remaining articles (11 of 24 were listed); add ECR and Kyriba pricing; fix the CTA copy. | None (index page) |
| P2 | `/learn/bank-analysis-statements/` | bank analysis statement | Distinct query, 149 words. Annotated example statement, fee code glossary, link to ECR. **Deliver** (fee code names). | Savings found > Fee review (`AuditReport.tsx`), Data sources > Upload |
| P2 | `/learn/bank-reconciliation-automation/` | bank reconciliation automation | Absorbs the use-case page. Manual vs. automated, honestly scoped: Tas shows book balances beside bank balances and proposes payment matches a person confirms; it does not post to the ledger. Link the new bank-vs-books page. | Cash > Bank & books (`Reconciliation.tsx`) |
| P2 | `/learn/cash-forecast-accuracy/` | cash forecast accuracy | Add MAPE/WAPE formulas with a worked example; link the template. No accuracy guarantee. | Forecast > Forecast (actuals and accuracy views) |
| P2 | `/learn/cash-forecast-vs-cash-flow-statement/` | cash forecast vs cash flow statement | Distinct definitional query but an orphan; add a comparison table and link it from the hub and the pillar. | Reports > Other reports (cash-flow statement; Director-gated screen) |
| P2 | `/learn/cash-position-dashboard/` | cash position dashboard | Informational target; absorbs the use-case page. Show what a cash position report contains and what "available vs. current" means. | Cash > Position (`CashPosition.tsx`) |
| P2 | `/learn/common-business-bank-fees/` | business bank fees | The fee-by-fee reference with sourced ranges; separate from wire benchmarks. **Deliver.** | Savings found > Fee review |
| P2 | `/learn/wire-transfer-fee-benchmarks/` | wire transfer fee benchmarks / business wire fees | Promises benchmarks and gives no numbers. Add dated, sourced, bank-published ranges for named banks or merge into the fees page. **Deliver.** | Savings found > Fee review |
| P2 | `/learn/how-much-cash-should-a-business-keep/` | how much cash should a business keep | Absorbs operating-vs-reserve. Months-of-expenses worked example, sources. | Forecast > Forecast (minimum-cash line) |
| P2 | `/learn/how-to-negotiate-bank-fees/` | how to negotiate bank fees | Remove "Cashlytica should help buyers". Add a call script, an email, a worked ask. | Savings found > Fee review |
| P2 | `/learn/idle-cash-drag/` | idle cash drag / cost of idle cash | Idle-cash pillar; absorbs two pages; worked example that matches the calculator. Educational; yield figures dated. **Deliver.** | Savings found > Idle cash & recommendations (PARTIAL: venue rates unverified; do not quote Tas yields) |
| P2 | `/learn/treasury-kpis/` | treasury kpis | 129 words and no formulas; define each KPI with a formula and a worked number. | Overview (`Dashboard.tsx`) |
| P2 | `/learn/treasury-management-software/` | treasury management software | Pillar for the treasury cluster; absorbs three pages. Category explainer, named alternatives, honest scope for a pre-release tool. **Deliver.** | Cash > Position, Forecast > Forecast |
| P2 | `/samples/` | sample treasury outputs | Remove "real" and "Cassius-generated"; drop $1,800 (claims S1, S2). Label every sample synthetic. | None (index page) |
| P2 | `/samples/board-briefing/` | board cash briefing sample | $1,800 conflicts with the report page; $3.5M excess cash beside a ~$1M forecast; say board packs are a Director-tier output. | Reports > Board pack (`Reports.tsx`, Director-gated) |
| P2 | `/tools/` | cash calculators | Rewrite as a plain hub; remove "turn interest into intent". | None (index page) |
| P2 | `/tools/bank-fee-calculator/` | bank fee calculator | Fix the label (claim T1): "Annual fees at this rate", not "overpayment". Optionally add a benchmark input so an overpayment can be estimated, with the benchmark sourced. | Savings found > Fee review |
| P3 | `/samples/idle-cash-recommendation/` | idle cash recommendation sample | 103 words; exposes service names and "golden fixture". Rewrite with the reasoning and labelled synthetic; wait until yields are verified. | Savings found > Idle cash & recommendations (PARTIAL) |
| P3 | `/learn/corporate-cash-yield-benchmarks/` | corporate cash yield benchmarks | Title promises benchmarks with no numbers. Add a dated, sourced rate table or merge into idle-cash-drag. **Deliver.** | None (educational) |
| P3 | `/learn/money-market-funds-vs-treasury-bills-vs-sweep-accounts/` | money market funds vs treasury bills vs sweep accounts | Real query, 214 words. Table of instruments, risks, dated yields, sources; fix the 67-character title. **Deliver.** | None (educational; Tas shows no specific instrument claims) |
| P3 | `/use-cases/` | (hub) | One page left under it after the merges (see section 1 note); recommend dropping it. | None |
| P3 | `/for/` | persona pages | Becomes the single persona page after four merges; hold until the P1 pages are live. | None |

### Keep (5), with the one fix each needs

| Page | Fix |
|---|---|
| `/compare/cashlytica-vs-kyriba/` | Replace the "your team executes" line (claim C4); add a visible last-reviewed date next to the 2026-10-21 `dateModified`; re-verify Kyriba facts. **Deliver.** |
| `/learn/earnings-credit-rate/` | Fix the AFP link that redirects to the AFP home page; link from the hub; add a visible last-reviewed date. **Deliver.** |
| `/learn/kyriba-pricing/` | Add og/twitter image, link from the hub, add a visible last-reviewed date. **Deliver.** |
| `/samples/bank-fee-audit-report/` | The reference sample: keep as the standard the other samples are brought into line with. |
| `/tools/idle-cash-calculator/` | Label the 4.75% default yield as an assumption with a source and date. **Deliver.** |

## 3. Create (12 new pages for shipped features nobody on the site covers)

| P | Working title | Target query | Tas screen (SHIPPED unless noted) |
|---|---|---|---|
| P1 | BAI2 and MT940 bank files: what they contain, how to get them from your bank, and how to load them | bai2 file format / mt940 file format / bank statement file formats | Data sources > Upload (`Upload.tsx`; CSV, XLSX, BAI2, MT940; PDF not supported). Say plainly that PDF statements cannot be loaded. |
| P1 | How to see cash across multiple entities and banks in one place | consolidated cash position multiple entities / multi-entity cash management | Cash > Position (`CashPosition.tsx`) and Cash > Entities (`Entities.tsx`, "Entity Group"). Honest scope: the Entities tab is Manager-tier in the UI hub while the entitlements file lists consolidation at Analyst; confirm before stating a tier. No intercompany claims (netting is Director advisory only). |
| P1 | Bank balance vs. book balance: why they differ and how to compare them each week | bank balance vs book balance / difference between bank and book cash | Cash > Bank & books (`Reconciliation.tsx`; Manager-tier). Honest scope: shows book balances (QuickBooks Online, Xero) beside bank observations and proposes payment matches that a person confirms; no write-back, no marking invoices paid, not "automatic reconciliation". PARTIAL (live QuickBooks/Xero acceptance unverified), so write it as method first, product second. |
| P2 | Scenario forecasting for cash: best, base and worst case | cash flow scenario analysis / best case worst case cash forecast | Forecast > Scenarios (`Scenarios.tsx`, "Scenario Planner") |
| P2 | Using AR and AP aging to build the first six weeks of a cash forecast | accounts payable aging cash forecast / ar aging cash forecast | Data sources > Upload (AR and AP aging uploads) |
| P2 | A weekly cash report for the CFO: what goes in it | weekly cash report / weekly cash position report | Reports > Other reports (weekly briefing PDF, `Reports.tsx`, Director-gated screen). Honest scope: the weekly decision memo endpoint is Analyst, the PDF briefing screen is Director; say which. No cadence promise. |
| P2 | Forecasting cash from QuickBooks Online and Xero data | quickbooks cash flow forecast / xero cash flow forecast | Data sources > Connections (`Integrations.tsx`), Forecast > Forecast. PARTIAL: read-only sync of balances, bills and invoices; live acceptance unverified. Publish after a design partner has connected one. **Deliver** (names QuickBooks and Xero features; sourced and dated). |
| P2 | Daily cash position report: what it should show | cash position report / daily cash report template | Cash > Position (`CashPosition.tsx`): current vs. available, source evidence, freshness. No "real-time". |
| P2 | Is it safe to connect your bank to a finance tool? | is plaid safe / connect bank account to software safe | Data sources > Connections (`Integrations.tsx`, Plaid link). Describe Plaid's role and Tas's controls only; no SOC 2, no "bank-grade". PARTIAL. **Deliver** (names Plaid; sourced and dated). |
| P3 | Running the weekly cash meeting: an agenda and the three numbers to bring | weekly cash meeting agenda / cash review meeting | Cash > Position, Forecast > Forecast |
| P3 | Early warning for a cash shortfall: what to watch and how far ahead | cash shortfall early warning / liquidity warning | Overview > Needs attention (`Alerts.tsx`). PARTIAL: no continuous-monitoring or delivery-cadence claim. |
| P3 | Dual control for payments: how approvals should work | payment approval workflow / dual control payments | Payments > Approvals (`Approvals.tsx`). PARTIAL and execution is a separately granted module; write as educational only. |

Considered and left out: debt and covenant tracking, FX, concentration, intercompany netting (Director features the inventory does not list as SHIPPED, and not a 1-to-15-entity buyer's first search), yield routing and payment execution (gated or sandbox-default; recruiting copy must not lead with them).

## 4. P1 wave (10 pages)

| # | Page | Type |
|---|---|---|
| 1 | `/learn/13-week-cash-forecast/` | revise (pillar; absorbs 4 merges) |
| 2 | `/templates/13-week-cash-forecast/` | revise |
| 3 | `/samples/13-week-forecast/` | revise |
| 4 | `/compare/cashlytica-vs-spreadsheets/` | revise |
| 5 | `/learn/bank-fee-audit/` | revise (absorbs the use-case page) |
| 6 | `/faq/` | revise |
| 7 | `/security/` | revise |
| 8 | BAI2 and MT940 bank files | create |
| 9 | Cash across multiple entities and banks | create |
| 10 | Bank balance vs. book balance | create |

Why these: a forecasting, multi-bank or fee problem lands on 1 to 5 (forecast, template, sample, spreadsheet alternative, fee wedge); 6 and 7 are what an applicant reads before sharing bank data; 8 to 10 are the three shipped differentiators the competing pages do not cover (statement formats a spreadsheet user can actually load, entity consolidation, and the bank/books check) and each answers an eligibility question in the offer ("QuickBooks or Xero", "several banks", "1 to 15 entities", "CSV, Excel, BAI2 or MT940").

## 5. "Deliver" pages: sources and a last-reviewed date

Rule: any page that names a bank, vendor, fee benchmark, ECR rate, yield or product feature of someone else's must carry (a) a sources list with links to the primary source, (b) a visible "Last reviewed: YYYY-MM-DD" line, and (c) `dateModified` in its JSON-LD. The site has no data layer, so facts live in the page; keep one `Sources` block per page and review quarterly, re-checking every link (the AFP link on the ECR page is already dead).

| Page | What needs sources |
|---|---|
| `/compare/cashlytica-vs-kyriba/` | Kyriba facts (dated 2026-10-21); re-verify, add last-reviewed |
| `/compare/cashlytica-vs-trovata/` | Trovata facts (rebuild) |
| `/compare/` (Mercury and Ramp paragraphs) | Vendor facts after the merge |
| `/learn/kyriba-pricing/` | Pricing statements and the quote checklist's sources |
| `/learn/earnings-credit-rate/` | ECR formula and rate sources; fix the AFP link |
| `/learn/bank-analysis-statements/` | Fee code names and statement layouts |
| `/learn/common-business-bank-fees/` | Named bank fee ranges |
| `/learn/wire-transfer-fee-benchmarks/` | Bank-published wire fees |
| `/learn/idle-cash-drag/` | Yield figures |
| `/learn/corporate-cash-yield-benchmarks/` | Rate table |
| `/learn/money-market-funds-vs-treasury-bills-vs-sweep-accounts/` | Yields, risks, instrument definitions |
| `/learn/treasury-management-software/` | Named alternatives and their capabilities |
| `/tools/idle-cash-calculator/` | The 4.75% default yield |
| `/tools/bank-fee-calculator/` | Benchmark input, if added |
| New: BAI2/MT940 | Format specifications (Bank Administration Institute for BAI2; SWIFT for MT940) |
| New: QuickBooks and Xero forecast | Vendor feature statements |
| New: Is it safe to connect your bank | Plaid's own documentation |

## 6. Product claims that must change regardless of priority (FALSE rows in the claims register)

Status checked against the current site source on 2026-10-30, after the two follow-up edits.

| # | Page | Claim | Status now | Fix |
|---|---|---|---|---|
| H9 | `/` | Free tier "forecast basics" | Fixed (tier ladder removed) | None |
| H13 | `/` | "intraday positioning" | Fixed (tier ladder removed) | None |
| H18 | `/` | "Read a full fee audit before you buy" | Fixed | None |
| F1 | `/faq/` | "Upload the bank statements" with no format list | Fixed (formats named, PDF unsupported) | None |
| S1 | `/samples/` | "Real sample outputs", "Cassius-generated artifacts, not placeholder mockups" | **Open** | Call every sample synthetic and illustrative |
| S2 | `/samples/`, `/samples/board-briefing/` | "$1,800 annual savings identified in the fee audit" | **Open** | Use the report page's $720 on $2,280, or remove the figure |
| F3 | `/faq/` | "Does Cashlytica move money? No" as an absolute | **Open** | Say Cashlytica analyzes and recommends and, during the design-partner program, does not initiate payments; payment staging and a separately granted execution module exist but are not part of the program |
| SEC2 | `/security/` | "analyzes and recommends" as the whole description | **Open** | Add payment staging and the gated execution module, or scope the sentence to the design-partner program |
| C4 | `/compare/cashlytica-vs-kyriba/` | "your team executes financial actions" | **Open** | Same scoping as F3 |
| T1 | `/tools/bank-fee-calculator/` (also echoed on `/`, `/tools/`, `/learn/common-business-bank-fees/`) | "Estimated annual overpayment" | **Open** | Rename to annual fees, or add a sourced benchmark |

Two lines I added in the last pass need the same care: the homepage's "Cashlytica analyzes and recommends; it does not initiate payments." is stated without the "during the program" qualifier your design-partner small print has. Fix the homepage line to match the small print. The Plaid sentences on `/faq/` and `/design-partners/` are your wording and are consistent with the inventory ("primarily Plaid where supported"), but MX code also exists and its customer path is unverified, so keep the wording "Plaid where your bank supports it" and nothing broader.

## 7. Totals

| | Pages |
|---|---:|
| Today (58 audited + `/design-partners/`) | 59 |
| Drop / merge (301) | -21 |
| After merges | 38 |
| of which Revise | 32 |
| of which Keep (with fixes) | 5 |
| of which `/design-partners/` | 1 |
| Create | +12 |
| **Total after the plan** | **50** |

By priority: **P1 = 10** (7 revisions, 3 new). **P2 = 26** (20 revisions, 6 new). **P3 = 8** (5 revisions, 3 new). The 5 Keep pages and the 10 claim fixes in section 6 are done alongside, not scheduled as waves. If the `/use-cases/` hub is also dropped, the total is 49.

## 8. Recommendation on sequencing

Do the safe work first, in one batch, before any new writing: fix the five open FALSE claims (section 6), remove the editor-voice copy that still sits on hubs and persona pages, and ship the 21 merges with their 301s, because redirects and false claims are cheap and every new page links into this structure. Then write the P1 wave in two passes: first the forecasting cluster (pillar, template, sample, spreadsheet comparison), because it is the page set that carries the only organic signal the site has (the 13-week query, around position 84), then the trust and differentiator pages (FAQ, security, BAI2/MT940, multi-entity, bank vs. books), written so each ends on the apply link and can be quoted in a reply to an applicant. Hold every PARTIAL-feature page (QuickBooks/Xero forecast, Plaid safety, alerts, approvals) until at least one design partner has used that screen and the claim can be checked against what happened, and hold all pricing, tier and plan content until the program ends. Measure with the new `design_partner_apply` event by `source_page` and with Search Console, and expect the P2 and P3 waves to be re-sorted by what the first five applicants asked about.
