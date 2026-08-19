# Bishops Bay — Repair Job Notes

Source: `audit-drive-pages/bishops-bay-page.html`
Fixed output: `pages/bishops-bay/bishops-bay-v2.html`
QA screenshot: `pages/bishops-bay/qa-screenshot.png` (full-page, Chromium, file:// render)

## What was fixed

1. **Schema identity nodes.** Deleted the fully redefined `Person` (`#johnreuter`) and `Organization` (`#organization`) nodes from the `@graph` entirely. `WebPage.author` now points to `{ "@id": "https://integrityhomeswi.com/#john" }` and the new `WebPage.publisher` points to `{ "@id": "https://integrityhomeswi.com/#org" }` — both `@id`-only stubs, no redefinition. This also removed the only place "Integrity Homes Wisconsin" appeared as a primary Organization name — confirmed gone.
2. **Quick-Answer block added** (Phase 7a/7b spec): CSS block added to `<style>`, HTML inserted immediately after the Stats Strip and before the Explore Card Grid / Photo Strip. Question: "What is Bishops Bay in Middleton, Wisconsin?" Answer is 90 words, four-slot fact template (what/where → origin/features → price caveat → schools/anchor distance). Note: the price slot could not cite a real SCWMLS number because none has been supplied for this subdivision yet, so it states that plainly and directs to John rather than substituting a builder or public-site estimate.
3. **`speakable`** added to the WebPage node, targeting `.qa-question`, `.qa-speakable`, `.faq-q`, `.faq-a`.
4. **Office street address removed.** "1025 Quinn Drive Ste 100" deleted from both the author bio and the footer. Kept: phone, email, "Waunakee, WI" city reference, Real Broker LLC affiliation + broker name, and the MLS Disclaimer link.
5. **Anchor address in Place schema** — checked; the Place node never had a `streetAddress` field in this file (locality/region/postal/country only). No change needed, confirmed compliant.
6. **Bracketed editorial prompts to John removed/rewritten**, in both the desktop `#johns-notes` section and the mobile-accordion duplicate (`#mob-johns-notes`):
   - Golf club membership optionality → rewritten in John's voice, grounded in the page's own HOA/club-separation facts.
   - Middleton/Westport jurisdiction split → rewritten, grounded in the page's tax/permitting and Reserve Hill boundary facts.
   - Reserve Hill/Watermark/Town Center still under construction → rewritten, grounded in the page's own build-status facts.
   - HOA obligations differing by neighborhood → rewritten, grounded in the page's HOA/sub-association facts.
   - A fifth bracketed prompt was found in the Market Update "John's Take" block (desktop + mobile), asking John to fill in commentary once he pulls the SCWMLS export. Since no sold data exists yet to ground a real quote in, and inventing one would fabricate market commentary, that block was **removed entirely** (bracket + prompt + label) rather than papered over — consistent with the "remove if you can't confidently write something grounded" instruction.
7. **Workflow status labels removed from visible copy**: "Draft — John's edits pending" (desktop + mobile John's Notes header) and "DRAFT — not yet live" (footer copyright line). "Last updated: August 2026" was kept.
8. **WebPage node**: added `about` (→ `#place`) and `publisher` (→ `#org`); `dateModified` updated to `2026-08-19`.

## QA performed (Phase 4b)

- Grep for `[ John`, `DRAFT`, `Draft —`, `pending`, `#organization`, `#johnreuter`, `Quinn Drive`, `anchor address` — all clean. Remaining "pending"/"TBD" hits are confined to the intentional Market Data TBD block, which is expected until John supplies the SCWMLS export.
- JSON-LD parsed successfully with `python json.loads` — 4 `@graph` nodes remain (WebPage, BreadcrumbList, Place, FAQPage), Person/Organization confirmed removed.
- Rendered full-page screenshot via Playwright/Chromium at `file://`. Reviewed every section, including the dark John's Notes panel (`.section-john`), the navy Schools/Commute sections, and the purple Schools section — no invisible-text-on-dark-background issues found anywhere (the Cathedral Point/Heritage Hills pattern was specifically checked for and not present).
- Found and fixed an **additional, previously unflagged defect**: 6 of 8 FAQ answers had drifted between the visible accordion text and the FAQPage schema (minor wording differences — e.g. "confirm your address with the WCSD Registrar" vs. the visible "ask your agent to check the district's boundary tool," and a duplicated subdivision name in the HOA question). Rewrote the schema's 8 Q/A pairs to match the visible desktop/mobile FAQ text byte-for-byte; verified programmatically (0 mismatches, 8/8 matched).

## Remaining open items (not fixed, out of scope for this repair pass or requiring John's input)

- **Market Update section is still all TBD.** No SCWMLS export has been supplied for Bishops Bay; the reporting-period label, all 12 stat cards, and the "John's Take" narrative all depend on that data. This is an intentional placeholder, not a defect, but it's the most visible gap on the page.
- **No approved Bishops Bay photography.** Both photo-strip tiles are still placeholders (confirmed "Not Filmed" status in the Media Vault as of this build).
- **Elementary school assignment** for Bishops Bay is still unconfirmed to a specific building (WCSD's boundary tool couldn't be automated) — flagged in-page as a call-before-you-offer item, not resolved here.
- **Park build-out status** (the ~191 acres of planned parks/open space, Woodland Adventure Park) is still marked as needing field verification — not resolved here, per the existing FLAG convention.
- **Dog park section** has no mobile-accordion counterpart, carried over intentionally from the master template per the existing in-file note; not something this repair pass should unilaterally "fix."
