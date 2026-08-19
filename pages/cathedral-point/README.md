# Cathedral Point — Verona, WI — Page Build Notes

**File:** `cathedral-point-v1.html`
**URL slug (target):** `https://integrityhomeswi.com/verona/cathedral-point/`
**Built:** 2026-08-19 · Tier 1 (publish-ready per SUBDIVISION-PAGE-BUILDER-README.md Phase 4 + 4b QA)

This page passed Phase 4b QA:
- Placeholder-leak linter: clean (no `[ John`, no `DRAFT`/`Draft —`, no leftover review comments; the one `pending` hit is the intentional Market Data TBD explainer).
- JSON-LD `@graph` parses via `python json.loads` — WebPage, BreadcrumbList, Place, FAQPage.
- Visible FAQ text matches the FAQPage schema entries exactly (verified programmatically).
- Rendered with Playwright/Chromium and visually reviewed. One real bug was found and fixed: the Commute & Proximity table's default row-text color (`var(--text-mid)`, a dark gray meant for a light background) was applied to every row, but only even rows got the cream background — odd rows sat directly on the navy section background with unreadable dark-on-dark text. Fixed by giving odd rows a light/white text color and keeping the cream-background override dark-on-cream for even rows. Confirmed fixed by re-rendering.
- The hero background image and the Homes for Sale featured image did not render in the local screenshot — this is expected: the sandbox has no network access to fetch the external Lofty CDN images from a `file://` context. Both image URLs are the real, confirmed CDN URLs from the research brief, not placeholders, and should render normally once live on the actual domain.

## Open items — Tier 2 punch-list (consolidated, per research brief Section O)

The page ships without these resolved, per the Tier 1/Tier 2 split. All in one list, for John to work through at his own pace:

1. **HOA dues — exact current-year (2026) figure.** Page uses the historical range (~$200–$320/year, varies by association/year) with a pointer to contact DSI Real Estate Group (`hoa@dsirealestate.com`) for the exact current-year dollar amount per association.
2. **Third unidentified CDN photo** (`...5b25951c56304c81.jpeg`) — not used on this page. Confirm what it shows before using it anywhere.
3. **Five unverified author-bio claims** — 115th Fighter Wing/Security Forces, Sun Prairie Fire Department volunteer history, "Top 5% nationally seven consecutive years," MRP designation, ROH EIN 39-3358820. All omitted from this page's author bio per instruction; only the confirmed block (Air Force veteran, WI Realtor®, Broker/Owner, ROH founder, Real Broker LLC) is used. Add back only if/when independently confirmed.
4. **Hero image aspect ratio check** — verify the aerial Memory Garden photo crops acceptably against social platforms' ~1.91:1 preview ratio before/after go-live; not checked in this build.
5. **Fresh SCWMLS pull for current sold-price/median/DOM.** Market Data section currently shows the 2024–2025 resale range ($385,000–$806,100, clustering $500K–$700K) labeled and dated as an existing export, not a live MLS query. Median sale price and median days-on-market are marked TBD pending that fresh pull — do not fill with a public-site estimate.
6. **"Forward Development Group" as master developer** — named in 2 of 4 raw research sources, not corroborated by the other 2. Currently flagged as unconfirmed in the About sidebar rather than stated as fact.

## Not included on this page (by design, per instructions)
- No Dog Parks section — research brief names no specific dog park for Cathedral Point.
- No office street address (no Quinn Drive) anywhere on the page.
- No `streetAddress` in the Place schema.
- No "John's Notes / Insider Notes" section — the research brief supplied no confirmed personal anecdotes from John for this neighborhood, and inventing bracketed placeholder prompts is the exact failure mode Phase 4b was written to catch. Add this section in the Tier 2 pass once John supplies real commentary.

## Internal linking still needed (Phase 5, not done in this pass)
- Verona city hub page (`/verona/`) needs to link down to this new page (Phase 5b).
- Section L (Comparison With Nearby Subdivisions) names Scenic Ridge, Raywood, Gateway, Kettle Creek, Cross Country, Prairie Oaks, Swan Creek — none linked yet since the brief flags Section L as an unpopulated placeholder list, not a researched comparison. Revisit once those pages (if any) exist and a real comparison is written.
