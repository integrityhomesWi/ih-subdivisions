# Savannah Village — Page Repair (v1_1 → v2)

Source: `audit-drive-pages/page-v1_1.html`
Fixed: `pages/savannah-village/savannah-village-v2.html`
QA screenshot: `pages/savannah-village/qa-screenshot.png` (full-page, 1400px viewport)

## What was fixed

1. **Schema identity IDs.** `#organization` → `#org`, `#johnreuter` → `#john` throughout the JSON-LD `@graph`. The full redefined `Person` and `Organization` nodes were deleted entirely (no stub nodes left in the graph either — per the schema-standard doc, references now point directly via `{"@id": "https://integrityhomeswi.com/#john"}` / `#org"}` at the point of use: `author` and the new `publisher` field on the WebPage node).
2. **"Integrity Homes Wisconsin" as primary Organization name** — resolved automatically by (1); confirmed gone from the JSON-LD.
3. **Quick-Answer block added** — CSS block (`.quick-answer`, `.qa-question`, `.qa-speakable`) inserted into `<style>`, and the HTML block inserted immediately after the Stats Strip, before the Explore-Cards/Photo Strip. 90-word four-slot answer (what/where, origin+named features, price status, anchor facts — school district + routed distance to Madison). `speakable` (`SpeakableSpecification`, targeting `.qa-question`, `.qa-speakable`, `.faq-q`, `.faq-a`) added to the WebPage node.
4. **Office street address removed.** "1025 Quinn Drive" deleted from both the author bio paragraph and the footer. Kept: phone, email, "Waunakee-based," "Affiliated with Real Broker, LLC · Broker: Dan Dyslin," and the MLS Disclaimer link. Added an explicit MLS-disclaimer link sentence to the author bio to keep that section useful without the address.
5. **Fabricated "anchor address" removed** from the Place node — `streetAddress: "1314 Hanover Court (anchor address)"` deleted entirely; Place now carries only locality/region/postal/country.
6. **Bracketed editorial prompts replaced with real first-person copy** in John's voice, grounded in facts already established on the page (five named additions, no confirmed covenant HOA vs. the documented pool nonprofit, the Six Mile Solar litigation timeline, and the Golden Ponds comparison already used elsewhere on the page). Five instances fixed, each in both the desktop and the mobile-accordion-duplicate copy of the section (10 total edits): the "John's Take" market-data paragraph, and all four "John's Notes" observation paragraphs.
7. **Internal workflow status labels removed**: "Draft — John's review pending" (About sidebar "Published" fact, both copies), "Draft — John's edits pending" (John's Notes "Last updated" line, both copies), and "DRAFT — not yet live" (footer copyright line). Replaced with real publish/update dates where a date line existed.
8. **WebPage node**: added `about` (→ `#place`), `publisher` (→ `#org`), and `speakable` (see #3). `dateModified` updated to `2026-08-19`.

## Phase 4b QA — results

- **Placeholder-leak grep** (`[ John`, `DRAFT`, `Draft —`, `pending` outside Market Data TBD, `#organization`, `#johnreuter`, `Quinn Drive`, `anchor address`): clean. The only remaining `pending` hits are legitimate content — the Six Mile Solar litigation status and the Market Data "pending MLS data" TBD fields, not workflow labels.
- **JSON-LD**: parses cleanly with `json.loads` (`WebPage`, `BreadcrumbList`, `Place`, `FAQPage` nodes, no orphaned stub nodes).
- **FAQ schema vs. visible text**: programmatically diffed all 20 visible FAQ entries (10 questions × desktop + mobile-accordion copies) against the `FAQPage` schema — 0 mismatches. (Found and fixed two pre-existing curly-vs-straight-quote mismatches in the "~15 minutes to Madison" and "Hanover Park" FAQ answers while checking this.)
- **Visual render**: full-page Chromium screenshot reviewed in segments. Hero, stats strip, new Quick-Answer block, About/sidebar, Schools (purple section), Parks, Market Data, John's Notes (dark green section), FAQ accordion, CTA/ROH bands, author band, and footer all checked for contrast — no invisible-text-on-dark-background issues found (the John's Notes dark-green section and purple Schools section, the two highest-risk spots for that bug pattern per the README note, both render with clearly legible light text).

## Remaining open items (not in scope for this repair pass — carried over from the original research)

- No approved Savannah Village photography in the Media Vault — hero uses a navy gradient placeholder and the Photo Strip shows two labeled placeholder tiles ("needs shoot — not yet in Media Vault").
- Market Data section is genuinely TBD — no SCWMLS export has been pulled for Savannah Village yet. All 12 stat cards show "TBD" and John's Take note now explains this honestly rather than via a workflow bracket.
- Savannah Park's exact street address is unresolved (two conflicting sources: 1202 Bluebird Trail vs. 1202 Arboretum Drive).
- "Hanover Park" (tennis/ball-field facility) is unverified — no independent source found.
- No standalone covenant-enforcement HOA has been confirmed to exist separately from the pool association.
- Dog Parks section flags that Ripp Park / Yahara Heights (referenced elsewhere in this project) haven't been routed specifically from Savannah Village and a closer option may exist — flagged as a Tier 2 item in the page copy itself.
- City hub page (`/waunakee/`) still needs to be updated to link down to this page (Phase 5b) — not done as part of this repair.
