# Golden Ponds — Repair Notes (page-v1.html → golden-ponds-v2.html)

Source: `/home/user/ih-subdivisions/audit-drive-pages/page-v1.html`
Output: `/home/user/ih-subdivisions/pages/golden-ponds/golden-ponds-v2.html`

This was a repair job on an already-built page — all existing research facts, FAQ content, and body copy were preserved. Only the identified defects were touched.

## What was fixed

1. **Schema identity nodes.** `#organization` → `#org`, `#johnreuter` → `#john` everywhere they appeared. The full redefined `Person` and `Organization` nodes were deleted from the `@graph` entirely. `author` on the WebPage node now points to `{ "@id": "https://integrityhomeswi.com/#john" }`; a new `publisher` property points to `{ "@id": "https://integrityhomeswi.com/#org" }`. The `@graph` now has exactly four nodes (WebPage, BreadcrumbList, Place, FAQPage), matching the corrected standard.
2. **"Integrity Homes Wisconsin" as primary Organization name** — gone automatically now that Organization is an `@id`-only reference instead of a redefined node.
3. **Quick-Answer block added.** New CSS block (`.quick-answer`, `.qa-question`, etc.) added to `<style>`, and the HTML block inserted immediately after the Stats Strip / before the Explore Card Grid + Photo Strip. Question: "What is Golden Ponds in Waunakee, Wisconsin?" Answer follows the four-slot fact template (what/where, origin + named amenities, sourced price status, school district + anchor distance), 90 words. `speakable` added to the WebPage schema node targeting `.qa-question`, `.qa-speakable`, `.faq-q`, `.faq-a`.
4. **Office street address removed.** "1025 Quinn Drive" removed from both the author bio ("John Reuter is a Waunakee-based Broker/Owner...") and the footer. Phone, email, "Waunakee, WI," Real Broker, LLC affiliation, and the MLS Disclaimer link were all kept.
5. **Fabricated "anchor address" removed from schema.** The Place node's `address` object no longer has a `streetAddress` field — locality/region/postal/country only. (Note: the visible body copy's use of "905 Travis Larson Court" as a real routing-reference address for the Nearby Conveniences / Commute sections was left in place — that's a legitimate real address used for distance calculations, not the fabricated schema field, and isn't the defect that was flagged.)
6. **Bracketed editorial prompts replaced with real first-person copy**, grounded in facts already established elsewhere on the page (Westbridge/Golden Ponds confusion, developer-controlled HOA status, unconfirmed park completion, new-build-vs-resale tradeoffs, and the pending-MLS-export "John's Take" note). Fixed in all four locations: desktop John's Notes section, the mobile-accordion duplicate of John's Notes, the desktop Market Update "John's Take," and its mobile-accordion duplicate.
7. **Draft/workflow status labels removed** from: the About sidebar "Published" fact ("Draft — John's review pending" → just "August 2026"), the John's Notes "Last updated" line ("Draft — John's edits pending" removed), and the footer copyright line ("DRAFT — not yet live" removed). The Market Update section's "Pending MLS data from John" / "TBD" fields were intentionally left as-is — those are the legitimate Market Data TBD placeholders, not workflow labels.
8. **`about` and `publisher` added to the WebPage node**, plus `dateModified` updated to `2026-08-19`.

## Phase 4b QA — results

1. **Placeholder-leak grep** — clean. No hits for `[ John`, `DRAFT`, `Draft —`, `#organization`, `#johnreuter`, `Quinn Drive`, or `anchor address`. The only `pending` hits remaining are legitimate content ("developer-claimed pending field or Village confirmation" — describing the park's confirmation status, not a workflow label) in the FAQ, matched identically in both visible copy and schema.
2. **JSON-LD validation** — parses cleanly via `python3 json.loads`. `@graph` contains exactly `WebPage`, `BreadcrumbList`, `Place`, `FAQPage`.
3. **Visual render** — full-page Chromium screenshot saved to `qa-screenshot.png` in this folder (1400×16080px). Reviewed in 8 chunks: hero, Quick-Answer block, About section, love-grid, purple Schools section, Parks/Nearby (cream), navy Commute table, dark-green John's Notes section, cream Market/Home Values, navy CTA, near-black ROH band, and the footer. No invisible-text-on-dark-background issues found — every dark section (navy hero, purple schools, navy commute, dark-green John's Notes, near-black ROH/footer) pairs light text correctly against its background.
4. **FAQ schema vs. visible text** — programmatically diffed. All 12 FAQ Q&A pairs match byte-for-byte between the FAQPage schema and both visible copies (desktop `#faq` section and the mobile-accordion `#mob-faq` duplicate).

## Remaining open items (not blockers — Tier 2 enrichment list)

- **No approved Golden Ponds photography exists yet** (asset status: Not Filmed per existing page comments). Both photo-strip tiles are still placeholders pending a Media Vault shoot.
- **Elementary school assignment unconfirmed** — WCSD has no public address-lookup tool; page correctly flags this as call-to-confirm rather than guessing.
- **HOA dues not confirmed for 2026** — only the 2022 recording-time ceiling ($250/lot max) is documented.
- **Park completion (shelter/playground/pickleball) not independently confirmed by the Village** — currently developer-marketed only, flagged as such on the page.
- **Westbridge Neighborhood Pool membership pricing not found** this research pass.
- **Golden Ponds-specific dog park distances not yet routed** (routing was done from a Golden Ponds anchor for other destinations, but not for the two named county dog parks).
- **Market Data section is fully TBD** — no SCWMLS export has been pulled yet for Golden Ponds. This is the single highest-priority follow-up once John supplies the export, per the standing quarterly-refresh policy.
- **City hub page linking-down (Phase 5b)** — confirm `/waunakee/` neighborhood directory has been updated to list Golden Ponds; not verified as part of this repair pass since it's outside this file.
