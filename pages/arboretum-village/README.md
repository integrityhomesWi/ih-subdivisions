# Arboretum Village — v2 repair notes

Source: `audit-drive-pages/page-v1_3.html`
Output: `pages/arboretum-village/arboretum-village-v2.html`
QA screenshot: `pages/arboretum-village/qa-screenshot.png` (full-page render, Chromium/Playwright)

This was a repair pass, not a rebuild. All research facts, FAQ content, and body copy were preserved; only the defects below were fixed.

## Fixed

1. **Schema identity nodes.** `#organization` → `#org`, `#johnreuter` → `#john` everywhere. The full redefined `Person` and `Organization` nodes were deleted entirely; `WebPage.author` and `WebPage.publisher` are now `@id`-only stubs pointing at `https://integrityhomeswi.com/#john` and `https://integrityhomeswi.com/#org`. "Integrity Homes Wisconsin" as a locally-defined brand name is gone as a side effect.
2. **Quick-Answer block added** (Phase 7a/7b spec) — CSS + HTML inserted immediately after the Stats Strip, before the Explore-Cards/Photo Strip. Uses the four-slot fact template (what+where / origin+features / price / anchor facts), 84 words. Price sentence is honest that MLS data isn't available yet and cites the builder-advertised range instead of fabricating a number.
3. **Speakable schema** added to the `WebPage` node, targeting `.qa-question`, `.qa-speakable`, `.faq-q`, `.faq-a`.
4. **Office street address removed** from the author bio ("with offices at 1025 Quinn Drive...") and the footer ("1025 Quinn Drive Ste 100"). Phone, email, Waunakee/WI 53597 city-state, Real Broker affiliation, and the MLS Disclaimer link were all kept.
5. **Fabricated "anchor address" field removed** from the Place schema node — it now carries only `addressLocality`, `addressRegion`, `postalCode`, `addressCountry` (no `streetAddress`).
6. **"Anchor address" phrasing removed from visible copy** (School section body + FAQ, both desktop and mobile-accordion duplicates). These sentences used "the neighborhood's anchor address" / "this research's anchor address" as an internal routing reference. Reworded to name the actual reference point used for routing — Laubmeier Park (1155 Prairie View Drive), which is independently documented elsewhere on the page as the park's real address.
7. **Bracketed editorial prompts to John replaced with real first-person commentary**, grounded only in facts already on the page (construction adjacency, HOA/dues per product type, Business Park boundary disclosure, school proximity). Fixed in both the desktop sections and the mobile-accordion duplicates:
   - John's Take (Market Update) — 2 places
   - 4 John's Notes entries — 2 places each (8 total)
8. **Internal workflow/status labels removed**: "Draft — John's review pending" (About sidebar, 2 places), "Draft — John's edits pending" (John's Notes header, 2 places), "DRAFT — not yet live" (footer).
9. **`about` and `publisher` added** to the `WebPage` node (pointing at `#place` and `#org` respectively). `dateModified` updated to `2026-08-19`.
10. **"Quinn Drive" removed** as a geography callout that read as an extension of the office-address problem — "off Quinn Drive and Hogan Road" became "off Hogan Road" (5 places: hero intro, About body ×2, About sidebar Location ×2), and the author-bio clause tying the office to "Arboretum Village's own Quinn Drive frontage" was cut along with the address itself.
11. **Pre-existing FAQ/schema text mismatch fixed** (found during QA, not in the original defect list): the "Is Arboretum Village still being actively built?" answer said "...covered in this **project**" in the schema but "...covered in this **research**" in the visible FAQ/mobile-accordion copy. Schema now matches the visible text exactly.

## QA performed

- Grepped the finished file for `[ John`, `DRAFT`, `Draft —`, `pending` (outside Market Data TBD fields), `#organization`, `#johnreuter`, `Quinn Drive`, `anchor address` — zero hits. (The three remaining "pending" hits are all the substring inside "**depending** on the source" in the condo-count FAQ — not a workflow label, left as-is.)
- Validated JSON-LD with `python json.loads` — parses cleanly, 4 `@graph` nodes (WebPage, BreadcrumbList, Place, FAQPage).
- Programmatically confirmed every `FAQPage.mainEntity` question/answer pair matches its visible `.faq-q`/`.faq-a` counterpart exactly (desktop + mobile-accordion copies) — all 9 schema Q&As found verbatim among the 20 visible pairs.
- Rendered full-page in Chromium via Playwright (`file://` URL) and visually reviewed every section: hero, stats strip, new Quick-Answer block, explore cards, About, Why People Choose It, Schools (purple section), Parks, Nearby, Commute (navy table), Dog Parks, Market Update (incl. John's Take), Homes for Sale, Home Values, John's Notes (dark green section), FAQ, market strip, CTA, ROH, author band, footer. No invisible/low-contrast text, no broken layout, no leftover placeholder scaffolding found.

## Open items (not part of this repair, unchanged from source)

These were already flagged in the source page and are out of scope for this defect-fix pass:
- Condo unit count discrepancy (14 vs. 20 units) — unresolved per the page's own FAQ.
- HOA legal name and dues — not confirmed.
- Arboretum Elementary boundary — "very likely," not a district-confirmed assignment.
- SCWMLS sale data — pending from John; Market Data section is intentionally all-TBD.
- Dog Parks distances — not yet routed from Arboretum Village (flagged inline as a Tier 2 item).
- No approved photography in the Media Vault yet — both photo-strip tiles are placeholders (asset status: Not Filmed).
- Teddy Bear Woods acreage (reported nine acres) — sourced only to developer/builder marketing, not independently confirmed.
