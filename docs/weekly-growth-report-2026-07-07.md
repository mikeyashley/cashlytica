# Cashlytica Weekly Growth Report

Pull date: 2026-07-07
GA4 property: Cashlytica (`properties/539910273`), timezone `America/New_York`
Search Console property: `sc-domain:cashlytica.com`

## 1. Summary
- Search Console visibility improved a bit week over week, but clicks are still flat at zero and CTR is still 0%.
- The best organic opportunity is still the 13-week cash forecasting cluster: it has the most impressions, but average position is still far from page one.
- GA4 traffic is small and noisy; 28-day volume is higher than the prior 28 days, but the landing-page report is mostly `(not set)`, so conversion interpretation is limited.
- No custom CTA / form / email / register / login events are being captured yet, so conversion trend tracking is not trustworthy.

## 2. Search Console
7-day window: 2026-06-30 to 2026-07-06

- Clicks: 0 vs 0
- Impressions: 46 vs 33 last week (+39%)
- CTR: 0% vs 0%
- Average position: 79.8 vs 80.5 last week (slightly better)

Top query opportunity:
- `13-week cash forecasting` — 93 impressions, avg position 84.6, 0 clicks
- Secondary: `treasury reporting software` — 29 impressions, avg position 78.8, 0 clicks

Top page opportunity:
- `/learn/13-week-cash-forecast/` — 127 impressions, avg position 84.1, 0 clicks
- Secondary: `/learn/treasury-management-software/` — 39 impressions, avg position 80.3, 0 clicks

Notes:
- No material page is currently sitting in the 8–20 position band; the visible page rows are still mostly in the 30–80 range.
- Search Console is showing both `cashlytica.com` and `www.cashlytica.com` URLs for the same content, so canonical / redirect consistency should be checked.
- No explicit crawl error surfaced in the available API snapshot.

## 3. GA4
GA4 property: Cashlytica (`properties/539910273`)

7-day window: 2026-06-30 to 2026-07-06
- Users: 9 vs 22 last week
- Sessions: 9 vs 22 last week
- Engagement rate: 11.1% vs 4.5% last week
- Average session duration: 3.5s vs 10.2s last week

28-day window: 2026-06-09 to 2026-07-06
- Users: 129 vs 11 prior 28 days
- Sessions: 129 vs 11 prior 28 days
- Engagement rate: 2.3% vs 9.1% prior 28 days
- Average session duration: 13.3s vs 4.4s prior 28 days

Top landing-page signal:
- `(not set)` is the biggest row in the landing-page report, which makes the landing-page story unreliable.
- The homepage `/` is the only clearly visible site landing page in the report, but it is a very small sample.

Notable source / medium and device pattern:
- Traffic is overwhelmingly `(direct) / (none)`.
- Desktop drives almost all sessions.

## 4. Conversion / CTA
- CTA clicks: not tracked in GA4
- Form starts: not tracked in GA4
- Form submits: not tracked in GA4
- Email clicks: not tracked in GA4
- Register clicks: not tracked in GA4
- Login clicks: not tracked in GA4
- Calculator interactions: not tracked in GA4
- Sample report views: not tracked in GA4

Trust level:
- Not enough instrumentation to trust conversion trend movement yet.
- Current GA4 data is mostly default events only (`scroll`, `first_visit`, `session_start`, `page_view`, `user_engagement`).

## 5. Action for next week
- Upgrade `/learn/13-week-cash-forecast/` so the first screen answers the exact query, then add a clear CTA to the forecast template and the $99 audit.

## 6. Instrumentation gaps
- No custom events for CTA clicks, register/login clicks, calculator usage, sample report views, form starts, form submits, or email clicks.
- Landing-page reporting is degraded by `(not set)` rows.
- Search Console host duplication (`www` vs non-`www`) should be cleaned up or at least verified.

## 7. Viability check
- Live Search Console access: yes
- Live GA4 access: yes
- Property mapping confirmed: yes
- Weekly report structure ready: yes
