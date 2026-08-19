# Centennial Heights — Repair Log (v1_4 → v2)

Source: `audit-drive-pages/page-v1_4.html`
Output: `pages/centennial-heights/centennial-heights-v2.html`

This was a repair job, not a rebuild. All existing research facts, FAQ content, and body copy were preserved; only the eight identified defects were fixed.

## Fixed

1. **Schema `@id` references** — `#organization` → `#org`, `#johnreuter` → `#john` everywhere they appeared. The full redefined `Person` and `Organization` nodes were deleted entirely and replaced with `@id`-only stubs (`author`: `{"@id": ".../#john"}`, `publisher`: `{"@id": ".../#org"}`).
2. **"Integrity Homes Wisconsin" as primary Organization name** — resolved automatically by step 1; confirmed gone (the Organization node no longer exists on this page).
3. **Quick-Answer block** — added per `subdivision-quick-answer-block.md`: CSS block (`.quick-answer`, `.qa-question`, etc.) added to `<style>`, HTML inserted after the Stats Strip and before the Explore Cards / Photo Strip, using the four-slot fact template (86 words). `speakable` added to the WebPage node targeting `.qa-question`, `.qa-speakable`, `.faq-q`, `.faq-a`.
4. **Office street address** — "1025 Quinn Drive Ste 100" removed from both the author bio ("John Reuter is a Waunakee-based Broker/Owner...") and the footer. Phone, email, "Waunakee, WI 53597" locality, Real Broker LLC affiliation, and the MLS Disclaimer link were all kept.
5. **Fabricated "anchor address"** — `"streetAddress": "808 Centennial Pkwy (anchor address)"` removed entirely from the Place node's `address`. Locality/region/postal/country retained. (Note: 808 Centennial Pkwy still appears once in visible body copy as an *example* address to give the WCSD Registrar — that's legitimate example text, not a schema field, and was left alone.)
6. **Bracketed editorial prompts to John** — all 5 instances (the "John's Take" market paragraph + 4 "John's Notes" observations), each duplicated once for desktop and once for the mobile-accordion copy (10 total edits), were rewritten as real, grounded first-person commentary in John's voice, using only facts already established elsewhere on the page (no active HOA / recorded covenants, gradual multi-decade build-out and renovation variance, the 2024 Centennial Park playscape, and the small 1109–1111 Centennial Pkwy condo unit). None of the new copy invents a price, a statistic, or a fact not already on the page.
7. **Internal workflow status labels** — removed from all 5 locations: the "Published" sidebar fact ("Draft — John's review pending," desktop + mobile), the John's Notes byline ("Draft — John's edits pending," desktop + mobile), and the footer ("DRAFT — not yet live").
8. **WebPage schema additions** — `about` now points to the Place node (`#place`), `publisher` now points to `#org`, `speakable` added. `dateModified` updated from `2026-08-07` to `2026-08-19`.

## Phase 4b QA — results

1. **Placeholder-leak grep** — clean. No hits for `[ John`, `DRAFT`, `Draft —`, `#organization`, `#johnreuter`, `Quinn Drive`, or `anchor address`. Remaining `pending` hits (7) are all intentional, honest disclosures — routed drive-time data and MLS sale figures — not workflow labels.
2. **JSON-LD validation** — parses cleanly with `python json.loads`. Graph: `WebPage`, `BreadcrumbList`, `Place`, `FAQPage` (4 nodes, Person/Organization correctly absent). Place `address` confirmed to contain only locality/region/postal/country.
3. **Visual render** — full-page Chromium screenshot saved to `pages/centennial-heights/qa-screenshot.png` and reviewed in 10 cropped sections end to end (hero → Quick-Answer → about → love grid → schools (purple) → parks → nearby → commute (navy) → dog parks → market → home values → John's Notes (dark green) → FAQ → CTA → ROH (navy-dark) → author → footer). No invisible/low-contrast text found on any background (navy, purple, dark-green, navy-dark, cream all check out), no broken layout, no leftover placeholder brackets visible anywhere.
4. **FAQ schema vs. visible text** — programmatically compared all 10 FAQ Q/A pairs in the JSON-LD against both the desktop and mobile-accordion visible copy (20 visible instances total). All match exactly.

## Open items for John (Tier 2 / async, not blocking)

- **Developer/HOA confirmation** — no developer, builder, or HOA has been confirmed for Centennial Heights; page says so honestly. Pull the "Centennial Heights Combined" plat from the Village to settle this.
- **Elementary school assignment** — Prairie Elementary is presented as "likely, by elimination," not a confirmed WCSD attendance-boundary lookup. Confirm with the WCSD Registrar, (608) 849-2000.
- **HOA covenants** — confirm via Dane County's Register of Deeds whether recorded covenants exist even without an active dues-collecting association.
- **Routed drive times** — the Commute table and several proximity claims are marked "Pending" due to a disclosed tool malfunction (Census geocoder / OSRM) during this research pass. Needs a follow-up pass once routing tools are working.
- **MLS market data** — the entire Market Update block is TBD, pending a SCWMLS export for Centennial Heights from John. This also feeds the Quick-Answer block's price sentence, which currently states the data is pending rather than fabricating a number.
- **Photography** — no approved Centennial Heights photography exists in the Media Vault yet (asset status: Not Filmed). Both photo-strip tiles are still placeholders.
- **John's Notes / John's Take copy** — the four insider-notes observations and the market "John's Take" quote were drafted in John's voice grounded in confirmed page facts, per the repair-job instructions. John should review and adjust wording/tone before this ships, since these are attributed quotes.
