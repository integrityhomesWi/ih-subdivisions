# Castle Crest — Build Notes (Tier 1, fresh build)

**Status:** Tier 1 complete, published-ready pending John's review. Airtable record `recn5jl9xzMICL2wS` (base `appTtFjtIHkZZYtgY`, table `tbl4FXwpxRiyaPcOT`) showed `Page Status = Not Started` and no existing research — this was a genuine from-scratch build, not a refinement pass.

**File:** `castle-crest-v1.html`
**Screenshot:** `qa-screenshot.png` (full-page render, Playwright/Chromium)
**Target URL:** `https://integrityhomeswi.com/waunakee/castle-crest/`

---

## Phase 1b — archive check (done first, per SOP)

- Searched Google Drive for "Castle Crest" (fullText + title). No `Research-Brief.md`, no `Page-v1.html`, no dedicated subdivision folder exists anywhere in Drive for Castle Crest.
- The only Drive hits were: (1) the `Subdivision_Attack_Plan.xlsx` tracker rows, (2) Kenzie's `KenzieWorkOrder.md`, which lists Castle Crest as subdivision #10 in the Waunakee queue (not yet worked), and (3) a stray mention of "Castle Crest" as a stock-photo suggestion inside an unrelated October 2025 market-update carousel doc — not research, not usable as a source.
- Conclusion confirmed: no prior research exists. Proceeded to full fresh Phase 1 web research as instructed.

## Airtable flag — critical, carried into the page

The Airtable record for Castle Crest carries this note verbatim: **"Note: 'Castle Creek' is a separate subdivision in the MLS data — do not confuse."**

Web research confirmed this is a real, easy-to-make mistake — Castle Creek is a genuinely different Waunakee neighborhood (near Bolz Conservancy Park and Sixmile Creek, closer to the Six Mile Creek/Westport side of the village, ~915 residents per Nextdoor/Census data cited on realty sites) from Castle Crest (bordered by Knightsbridge Road/South Street/Winston Way, adjacent to downtown). **This is now a documented name-conflict pair**, same category as Kilkenny Farms/Kilkenny Farms West and Southbridge/Westbridge. The page addresses it directly with a dedicated FAQ entry and an "About" sidebar callout ("Not to Be Confused With"). Recommend adding this pair to the known-conflicts list in `docs/SUBDIVISION-PAGE-BUILDER-README.md` Phase 2.

## Research sources (Phase 1, web search — no Perplexity/ChatGPT legs run; those API keys are not yet configured per the README's own Phase 1a status table, so this build used Claude's native web search only, consistent with "if one engine fails or times out, proceed with the others")

- neighborhoods.com, homes.com, joshlavik.com, madcitydreamhomes.com, starkhomes.com — consistent, independently-corroborated description of Castle Crest's boundaries (Knightsbridge Rd / South St / Winston Way), build era (1970s–early 1980s), and walkability to schools/library. Multiple independent real-estate sites repeating the same specific boundary description gives reasonable confidence in that fact even though none of them are a primary municipal source.
- hngnews.com (Waunakee Tribune) — "Stink pond evolves into park site" — sourced the Waunakee Rotary Walk history (2008 completion, Rotary-funded path, bridge donated by Endres Manufacturing, later lighting/pier additions).
- waunakee.gov — Waunakee Public Library address (201 N Madison St), Village Hall address (500 W Main St).
- waunakee.k12.wi.us / hometownlocator.com / zipdatamaps.com — confirmed the district's three elementary schools and their addresses (Prairie Elementary 700 N Madison St, Heritage Elementary 6271 Woodland Dr, Arboretum Elementary 1350 Arboretum Dr). Could **not** find an official parcel-level attendance-boundary confirmation for Castle Crest specifically — this is flagged as an open item below, not guessed.
- HOA search (BBB, hoa-community.com, general web search) — found no HOA registered under "Castle Crest" in Waunakee. Treated as "no HOA found," not "confirmed no HOA" — a real distinction, stated as such on the page.
- Google Drive `Subdivision_Attack_Plan.xlsx` — 12 MLS records logged for Castle Crest as of the July 31, 2026 pull (a count only, no pricing) — used only as a citation for sales-volume context in the Market Data section, not as a pricing source.

## What was deliberately NOT used

- Zillow/Redfin/Movoto/homes.com "median listing price" figures (e.g. a March 2024 Zillow-sourced $286K figure surfaced during research) — **excluded per standing project rule.** All pricing fields are marked "pending MLS data from John" instead. This is the single most important rule this build had to hold the line on, since Castle Crest is exactly the kind of thin/no-prior-research subdivision where it would be tempting to backfill with a public-site number.
- Any drive-time/routing figure I could not verify through a live routing tool (not available in this build environment) — marked "not yet routed" consistently, per Phase 4b rule 5, rather than estimated from general Waunakee geography.

## Design/build decisions

- Used Six Mile Creek's structure/CSS as the primary template (established-neighborhood tone, no purple schools treatment, no photo strip) rather than Kilkenny Farms West's (new-construction tone) — Castle Crest is an older, established neighborhood, closer in character to Six Mile Creek.
- No hero photo: searched both Google Drive and this repo for any Castle Crest image — none found. Used the navy gradient placeholder pattern from the anatomy doc with an HTML comment noting the asset status, per Phase 3/4b rules (checked, not assumed).
- Added a **Comparison table** (Phase 7d) against Castle Creek (flagging it unresearched, not conflating data), Six Mile Creek, and Kilkenny Farms West — using only already-published, sourced SCWMLS figures from those two live pages, never inventing a number for Castle Crest itself.
- Quick-Answer block follows the exact 4-slot template (what+where / origin+features / price+source / schools+anchor distance), speakable schema wired to `.qa-question`/`.qa-speakable`/`.faq-q`/`.faq-a`.
- Schema: `author`/`publisher` are `@id`-only stubs to `#john`/`#org`. No full Person/Organization node anywhere on the page. No `streetAddress` in the Place node. No office street address anywhere in the author bio or footer.

## Phase 4b QA results

- `grep -c "#johnreuter"` → **0**
- `grep -c "#organization"` → **0**
- `grep -c "Quinn Drive"` → **0**
- `grep -c "DRAFT"` → **0**
- Bracketed editorial prompts (`[ John`, `[XXX]`-style scaffolding) → **0** matches
- `pending` appears only inside the intentional Market Data / pricing-TBD copy (Quick-Answer sentence, About sidebar, Market Data section, comparison table, FAQ) — every instance reviewed manually, none are stray template scaffolding.
- JSON-LD: parsed successfully with `python3 json.loads()` — 4 `@graph` nodes (WebPage, BreadcrumbList, Place, FAQPage), all `@id`s correctly namespaced under `https://integrityhomeswi.com/waunakee/castle-crest/`.
- Visual render: full-page Playwright/Chromium screenshot (`qa-screenshot.png`, 1400×12069px) reviewed in 8 vertical slices. No invisible/low-contrast text found (including the navy Market Data section on navy background, dog-park cards, and comparison table's highlighted "current row" — all checked specifically since these are the pattern that broke on a prior build). No broken images (none used). Mobile breakpoints inherited unchanged from the Six Mile Creek reference CSS.

---

## Open items — consolidated in one place per Phase 4b rule 4

These are genuine gaps from a from-scratch build with no prior research file. None of them block Tier 1 publish; they're the Tier 2 worklist.

1. **MLS pricing — the big one.** Every Market Data field (sold price range, median/average, DOM, list-to-sale ratio) and the Quick-Answer price sentence need a real SCWMLS export for "Castle Crest," fuzzy-matched carefully against "Castle Creek" (do not merge). 12 MLS records were logged in the Attack Plan tracker as of July 2026 — small sample, worth pulling directly.
2. **School attendance boundary — not independently verified.** The page infers Prairie Elementary as the likely K–4 assignment based on Castle Crest's central location, but this is a reasoned guess from geography, not a boundary-map confirmation. Needs an actual check against `waunakee.k12.wi.us`'s attendance map (or Kenzie's human-intel pass) before this is stated as fact rather than "likely."
3. **HOA status — "no HOA found" is not the same as "confirmed no HOA."** Worth a quick title-company or county-recorder check to close this out definitively, especially since some individual lots in older subdivisions can carry legacy covenants even without an active association.
4. **All drive-time/distance figures beyond "walking distance to downtown/library"** — Downtown Madison, MSN airport, UW Health, Epic Systems, and both dog parks are marked "not yet routed." This environment has no live map-routing access (documented limitation, see `SUBDIVISION-PAGE-BUILDER-README.md` Phase 4b rule 5). Needs a routing pass once a routing API/key is wired in, or a manual check.
5. **No approved photo exists for Castle Crest** in Drive or the Media Vault as of this build (2026-08-20) — confirmed via search, not assumed. Page ships with the navy gradient placeholder per standard. Flagging as `IMAGE-PENDING` for Phase 3 follow-up — swapping this is also a scheduled freshness-signal opportunity (bump `dateModified` when it happens).
6. **Castle Creek comparison row is intentionally thin** — I did not research Castle Creek in depth for this build (out of scope; Castle Crest was the assignment). The comparison table and FAQ note enough to prevent confusion but don't claim anything about Castle Creek's pricing, HOA, or schools. If/when Castle Creek gets its own Tier 1 build, this page's comparison row and FAQ should be revisited to link to it.
7. **Perplexity/ChatGPT research legs not run** — those API keys are not yet configured per the builder README's own open-items list. This build relied on Claude's native web search only (the one leg confirmed "already enabled" in Phase 1a). Once the other two keys exist, Castle Crest is a reasonable candidate for a supplemental research pass to catch anything the single-engine search missed (per the union-of-coverage merge philosophy).

## Phase 5 — interlinking status

- 5a (link up to city hub): done — breadcrumb + market-strip link to `/waunakee/`.
- 5b (link down from city hub): **not done** — the Waunakee city hub page is outside this repo/task scope. Flagging per SOP: **the Waunakee hub page needs a manual edit to add Castle Crest to its neighborhood directory** once this page is live.
- 5c (sideways links): linked to Six Mile Creek and Kilkenny Farms West (both live, both in Waunakee, both same-day-available). Castle Creek is named but not linked (no page exists yet).
- 5d (market report link): done — links to `/market-reports/waunakee-wisconsin/`.
- 5e (blog cross-links): not attempted — out of scope for this single-page build; flagging as a to-do for whoever runs the next blog-seo-packager pass on Waunakee content.
