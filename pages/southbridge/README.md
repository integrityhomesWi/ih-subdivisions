# Southbridge Page — Repair Notes (v2)

Source: `audit-drive-pages/page-v1_2.html`
Output: `pages/southbridge/southbridge-v2.html`
QA screenshot: `pages/southbridge/qa-screenshot.png` (full-page, 1440×15037, Chromium/Playwright)

This was a repair job on an already-built page. The legacy `<details>`/`<summary>`
collapsible-accordion pattern (desktop `.section-collapse` + mobile
`.mob-accordion-item`) was left alone per instructions — not converted to the
newer static-section template.

## Fixed

1. **Schema identity nodes.** `#organization` → `#org`, `#johnreuter` → `#john`
   everywhere. Deleted the full redefined `Person` and `Organization` nodes
   from the page's `@graph` entirely; `author` and `publisher` now reference
   the master identity nodes by `@id` only. Graph is now four nodes —
   `WebPage`, `BreadcrumbList`, `Place`, `FAQPage` — matching the corrected
   standard's worked example exactly.
2. **Brand name "Integrity Homes Wisconsin."** Gone automatically — it only
   existed inside the deleted Organization node.
3. **Quick-Answer block.** Added per
   `docs/subdivision-quick-answer-block.md`: CSS block inserted into
   `<style>`, HTML inserted after the Stats Strip and before the Explore
   Cards / Photo Strip. Four-slot fact template, 90 words, question as `<h2
   class="qa-question">`, answer as `<p class="qa-speakable">`. Added
   `speakable` (`SpeakableSpecification`, targeting `.qa-question`,
   `.qa-speakable`, `.faq-q`, `.faq-a`) to the `WebPage` node.
4. **Office street address removed.** "1025 Quinn Drive Ste 100" deleted from
   both the author bio paragraph and the footer. Footer now reads
   "Waunakee, WI · phone · email"; phone, email, Waunakee-based framing,
   Real Broker LLC affiliation, and the MLS Disclaimer link are all still
   present.
5. **Fabricated "anchor address" removed.** `streetAddress: "1500 Blue Ridge
   Trail (anchor address)"` deleted from the `Place` node — it now carries
   only locality/region/postal/country. Also swept the visible body copy and
   FAQ text (both the mobile and desktop duplicate sections) for the same
   "anchor address" / "anchored at 1500 Blue Ridge Trail" phrasing, since the
   Phase 4b grep check screens for the literal string "anchor address"
   anywhere in the file, not just in schema. Replaced with neutral phrasing
   ("from within the neighborhood," "from within Southbridge") that keeps the
   verified 6-minute/2.4-mile drive-time fact intact.
6. **Bracketed editorial prompts to John** — five distinct prompts, each
   appearing twice (mobile-accordion copy + desktop section copy, 10 lines
   total): the John's Take market block, and four John's Notes
   observations (multi-HOA confusion, pool fee sticker shock, Kilkenny/Kilkenny
   Farms mix-ups at showings, and the drive-time comparison to Heritage Hills
   /Golden Ponds). All rewritten as real first-person commentary in John's
   voice, grounded only in facts already established on the page (the $50/
   $100-per-lot HOA figures, the $1,000 pool initiation fee, the confirmed
   6-minute drive time, the Kilkenny/Kilkenny Farms distinction). No new
   claims or numbers were introduced.
7. **"Draft — pending" labels removed.** "Draft — John's review pending"
   (sidebar Published fact) and "Draft — John's edits pending" (John's Notes
   updated line) removed, both instances (mobile + desktop). Footer
   "DRAFT — not yet live" removed. Left the intentional Market Data `TBD`
   fields and "Pending MLS data from John" market-stats labels alone — those
   are the explicitly exempted, real workflow state (MLS export not yet
   supplied), not stray internal notes.
8. **`about` and `publisher` added to WebPage node**; `dateModified` updated
   to `2026-08-19`.

## Phase 4b QA — results

1. **Grep sweep** for `[ John`, `DRAFT`, `Draft —`, `pending` (outside Market
   Data TBD), `#organization`, `#johnreuter`, `Quinn Drive`, `anchor
   address` — zero hits after fixes. Remaining `pending`/`TBD` matches are
   all in the Market Data block and are intentional.
2. **JSON-LD** parses cleanly with `python json.loads` — 4 graph nodes,
   `author`/`publisher` resolve to `#john`/`#org`, `about` resolves to the
   `#place` node, `speakable` present, `dateModified` = `2026-08-19`.
3. **Playwright screenshot** (Chromium, 1440px viewport, full page) reviewed
   in full. No contrast bugs — the dark sections (navy hero, navy stats
   strip, purple schools section, dark-green John's Notes section) all render
   their light/gold text correctly against their backgrounds. No
   invisible-text-on-dark-background issue like Cathedral Point/Heritage
   Hills.
4. **FAQ text vs. schema.** Found and fixed a pre-existing mismatch (not in
   the original defect list, caught by this QA step): the FAQPage schema
   text for the HOA, pool, and parks questions was shorter than the visible
   FAQ answers (missing the "ask which association governs your address"
   line, the detailed pool-fee-schedule parenthetical, and the individual
   park street addresses). Schema text was updated to match the visible copy
   exactly — verified programmatically against both the mobile-accordion and
   desktop FAQ instances (20 visible Q/A pairs total, matching the 10 schema
   entries).

## Open items

- **No approved Southbridge photography** — both hero and the two Photo Strip
  tiles remain gradient/placeholder. Flagged in-page as "needs shoot — not
  yet in Media Vault." Not a defect in scope for this pass.
- **Market Data section is genuinely TBD** — SCWMLS export has not been
  supplied yet. All twelve `ms-card` stats are placeholder `TBD`, and the
  Quick-Answer block's price sentence notes data is "being compiled" rather
  than citing a number, per the no-fabrication rule. Needs the quarterly
  MLS refresh once John supplies the export (Phase 7c).
- **Three open FLAG items** referenced in the repo README (per CLAUDE.md)
  were not re-verified in this pass — this was a schema/defect repair job,
  not a fact-verification pass. Still open in the page: (a) elementary school
  assignment for Southbridge addresses, (b) exact pool water-feature list,
  (c) Tierney Park acreage (12.7 vs. 21.4, disputed) and Bolz Conservancy
  acreage (10–13 vs. ~15, disputed).
