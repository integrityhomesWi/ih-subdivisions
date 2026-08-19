# Westbridge Page — Repair Notes

Source: `audit-drive-pages/westbridge-page.html`
Fixed output: `pages/westbridge/westbridge-v2.html`
QA screenshot: `pages/westbridge/qa-screenshot.png` (full-page, Playwright/Chromium, 1400x900 viewport)

This was a repair job on an already-built page — all existing research facts, FAQ content, and body copy were preserved. Only the identified defects were fixed.

## What was fixed

1. **Schema identity references** — `#organization` → `#org`, `#johnreuter` → `#john` everywhere. The full redefined `Person` and `Organization` nodes were deleted from the `@graph` entirely; `author` now points to `{ "@id": "https://integrityhomeswi.com/#john" }` and `publisher` to `{ "@id": "https://integrityhomeswi.com/#org" }`, both `@id`-only stubs per the schema standard.
2. **"Integrity Homes Wisconsin" as primary Organization name** — resolved automatically by #1; the full Organization node (and its `name` property) no longer exists on this page.
3. **Quick-Answer block added** — new CSS block + HTML inserted immediately after the Stats Strip (60–90 words, four-slot fact template: what/where, origin + named amenities, price status, anchor facts). Added in two places to match the page's existing mobile-accordion/desktop duplicate structure: once inside `mobile-accordion-wrap` (mobile-visible) and once after the real `.stats-strip` (desktop-visible, hidden on mobile via `#quick-answer-desktop { display: none; }` in the existing mobile media query, so it doesn't duplicate visible text on small screens). `speakable` schema added to the WebPage node targeting `.qa-question`, `.qa-speakable`, `.faq-q`, `.faq-a`.
   - Note: no confirmed SCWMLS sold-price data exists for Westbridge yet (Market Data section is still all `TBD`), so the price sentence honestly states that status and directs to John rather than fabricating a number — consistent with the page's own existing "pending MLS data" handling elsewhere.
4. **Office street address removed** — "1025 Quinn Drive Ste 100" removed from both the author bio and the footer. Phone, email, Waunakee-based description, Real Broker LLC affiliation, and the MLS Disclaimer link are all preserved.
5. **Fabricated "anchor address" removed** — `streetAddress: "722 Westbridge Trail (anchor address)"` deleted from the Place node entirely. Locality/region/postal/country retained.
6. **Bracketed editorial prompts replaced** — all 5 unique `[ John — ... ]` placeholders (the Market Update "John's Take" note, plus 4 "John's Notes" observations) were rewritten as real first-person commentary in John's voice, grounded in facts already established elsewhere on the page (Southbridge/Westbridge confusion, original HOA's homeowner-controlled governance, original-plat-vs-Golden-Ponds buyer tradeoffs, saltwater pool membership uptake). Fixed in both the desktop section and the mobile-accordion duplicate (identical text in both places in the source, so both were caught).
7. **Draft/workflow status labels removed** — "Draft — John's review pending" (About sidebar, ×2), "Draft — John's edits pending" (John's Notes "Last updated" line, ×2), and "Draft — Published August 2026 · Not yet live" (footer) all removed. Remaining `TBD` values in the Market Data section were left in place — those are intentional, labeled data-pending fields, not workflow status.
8. **WebPage node enrichment** — added `about` (→ the Place node) and `publisher` (→ `#org`); both were absent before. `dateModified` updated to `2026-08-19`.

## Additional fix found during Phase 4b QA (not in the original defect list)

- **FAQ schema/visible-text mismatches, 2 instances**, both on the "What school district serves Westbridge?" and "What are Westbridge's HOA dues?" answers:
  - The schema text for the school-district answer was missing the phone number `(608) 849-2000 ext. 8470` that appears in the visible FAQ answer.
  - The schema text for the HOA-dues answer used "that is" where the visible answer uses "that's."
  - Both were fixed by updating the schema text to match the visible copy exactly (visible copy treated as source of truth, since it's what a human reader — and the two duplicate on-page instances — actually say). Confirmed via a script that diffed all 10 schema `Question`/`Answer` pairs against every visible `.faq-q`/`.faq-a` pair on the page: zero mismatches remain.

## Phase 4b QA — mandatory checks, all passed

1. **Placeholder-leak grep** — searched the finished file for `[ John`, `DRAFT`, `Draft —`, `pending` (outside Market Data TBD fields), `#organization`, `#johnreuter`, `Quinn Drive`, `anchor address`. Zero hits.
2. **JSON-LD validation** — parsed with Python `json.loads()`. Valid. `@graph` contains exactly `WebPage`, `BreadcrumbList`, `Place`, `FAQPage` (no orphaned Person/Organization nodes).
3. **Visual render** — rendered via Playwright + Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) at a 1400×900 viewport, full-page screenshot saved to `qa-screenshot.png`. Reviewed in full: hero, stats strip, new Quick-Answer block, About section, Why-People-Choose-It grid, Market Update / John's Take, Home Values, John's Notes (dark green section), CTA/ROH bands, author bio, and footer. No invisible-text-on-dark-background issues (the Cathedral Point/Heritage Hills failure pattern) — every dark section (navy, purple, dark green) renders its text in visible cream/white/gold tones. No broken layout.
   - Note: Google Fonts (`fonts.googleapis.com`) could not be reached in this sandboxed environment during rendering, so the screenshot uses fallback system fonts instead of Cormorant Garamond/Jost. This is a rendering-environment limitation, not a defect in the page — the font `<link>` tags are unchanged and will load normally in production.
4. **FAQ text match** — confirmed programmatically (see "Additional fix" above); all 10 FAQ questions/answers now match byte-for-byte between the visible page (both desktop and mobile-accordion copies) and the FAQPage schema.

## Open items for John (Tier 2)

None blocking Tier 1 publish. Carried over from the existing page, unchanged by this repair pass:
- No approved Westbridge photography exists yet in the Media Vault (hero and both photo-strip tiles remain placeholders).
- SCWMLS sold-price data has not been pulled — Market Data section is all `TBD`, and the new Quick-Answer block's price sentence reflects that honestly rather than guessing.
- Original Westbridge Neighborhood Association's current HOA dues were not found in any public source (noted in the FAQ).
- Westbridge elementary school assignment (of Waunakee CSD's three elementary schools) has not been confirmed to a specific building.
