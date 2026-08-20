# Kilkenny Farms — Build Notes (v1, 2026-08-20)

## Naming — read this first

**Kilkenny Farms** is the original/older Waunakee neighborhood, developed starting
in 2014. **Kilkenny Farms West** (`pages/kilkenny-farms-west/`) is a newer, separate
phase immediately adjacent to it, currently under active construction. They share a
developer, a name, and a pool amenity — which is exactly why they get conflated.
This page is about the base **Kilkenny Farms** only. Do not merge content from the
two guides.

## Research source

**No existing Drive research brief was found for Kilkenny Farms (base name).**
Checked before doing any fresh research, per Phase 1b:

- Airtable record `recUtrbT1Lxgq0Kng` (base `appTtFjtIHkZZYtgY`, table
  `tbl4FXwpxRiyaPcOT`) — Status = "Research Done," Tier 1, 39 MLS records / 70
  search vol/mo. The "Research Done" status appears to refer to the *tracker
  entry itself* being researched (name, tier, MLS/SEO numbers), not a subdivision
  content brief — no such brief exists.
- Searched the canonical Drive folder (`Subdivision Attack Plan`,
  `1vs5sHKyaqkWX6omzWpy8b3dug2zz2Ald`) for a Kilkenny Farms research brief, page
  draft, or Flags doc. None exists. The Kenzie Work Order
  (`KenzieWorkOrder.md`) lists "Kilkenny Farms" as item #2 on the Waunakee
  research queue with an empty Status column — i.e., not yet started.
  `SubdivisionBriefTEMPLATE.md` exists but no filled `Brief-Kilkenny-Farms-Waunakee.md`
  was ever saved.
- Searched Drive broadly for any Kilkenny Farms (non-West) content — found only
  Kilkenny Farms West assets (footage, editing-trial folders, photos), a
  `Subdivision_Attack_Plan (3).xlsx` tracker row, and Kilkenny Farms Park's public
  city facility page (via web search, not Drive).

**Conclusion: nothing subdivision-specific existed beyond the tracker row**, so
this build used fresh Phase 1 web research (public sources only — builder/developer
sites, the Waunakee city parks page, and MLS-listing aggregator sites for
non-price facts like streets and HOA range) rather than an existing brief.

### Fresh research — sources consulted
- `dontierney.com/neighborhoods/kilkenny-farms` (developer site, listed in search
  results — direct fetch was blocked by the network egress proxy, so only search
  snippets were used, not the full page)
- `cchofwaunakee.com/kilkenny-farms-subdivision/`, `madcitydreamhomes.com`,
  `neighborhoods.com`, `remax.com`, `stark­homes.com` — search snippets only
  (same egress block)
- `waunakee.gov` — Kilkenny Farms Park facility page (address, acreage, amenities)
- WebSearch aggregation for streets (Ireland Drive, Water Wheel Drive), schools,
  and HOA range

**Note on source quality:** because direct WebFetch to these sites was blocked
by the environment's egress proxy, all facts below are sourced from WebSearch
result *snippets*, not full page reads. Facts that appeared consistently across
multiple independent snippets (2014 origin, Irish-immigrant land history, Ireland
Drive/Water Wheel Drive streets, Kilkenny Farms Park details) are treated as
reasonably solid. Anything that only appeared once, or that reads like a page
category rather than a real data point, was left out or explicitly flagged below.

## What's on the page vs. what's still open

**Solid / used directly:**
- Origin year (2014), developer (Livable Communities by Don Tierney), Irish-1848
  land history — matches Kilkenny Farms West's own page copy for the shared
  heritage story
- Streets: Ireland Drive, Water Wheel Drive (confirmed via MLS listing URLs)
- Kilkenny Farms Park: 1021 Water Wheel Drive, 5.42 acres, playground (zip line,
  rope climbing structure, sand toys), park shelter, restrooms, tennis/basketball
  courts, 6 pickleball courts — confirmed via waunakee.gov
- The neighborhood's own saltwater pool complex — confirmed indirectly via the
  live Kilkenny Farms West page, which describes it as "the saltwater pool
  complex in the adjacent Kilkenny Farms neighborhood"
- Schools: same Waunakee Community School District chain as Kilkenny Farms West
  (Heritage Elementary → Waunakee Intermediate → Waunakee Middle → Waunakee
  Community High) — used as "expected" per the Woodland Drive-area location,
  **not asserted as independently confirmed for Kilkenny Farms specifically**.
  Every school reference on the page carries a verify-by-address caveat.

**Explicitly left pending — flagged for John / Tier 2:**
1. **MLS/sold-price data** — no SCWMLS export was supplied for this build. Every
   price field on the page reads "Pending SCWMLS Pull." Do not substitute the
   `$197/mo HOA` or "$600K–$1.375M" figures that appeared in public aggregator
   search snippets — those are unverified public-site numbers, exactly the kind
   this project's rules prohibit using for market data.
2. **HOA name, exact dues, and covenant details** — not confirmed to any specific
   figure. Deliberately omitted from the page rather than guessing (one snippet
   said "median HOA $197/month" for Waunakee land listings generally, not
   Kilkenny Farms specifically — too weak to publish).
3. **Drive times** — every row in the Proximity & Commute table shows "Not yet
   routed," per the standing environment limitation (Google Maps routing isn't
   reachable here). Distances are rough estimates based on the neighborhood's
   general location adjacent to Kilkenny Farms West, not independently measured
   for Kilkenny Farms specifically.
4. **School attendance boundary** — assumed identical to Kilkenny Farms West's
   confirmed boundary because of shared geography, but not verified against the
   district's official attendance map for Kilkenny Farms addresses specifically.
   Flagged in both the Schools section and the FAQ.
5. **Hero/photo image** — no approved Kilkenny Farms (base, non-West) photo was
   found in Drive as of 2026-08-20 (searched Image Vault/Media Vault folder and
   general Drive full-text search — actually checked, not assumed). Page ships
   with a navy gradient placeholder and an HTML comment marking it IMAGE-PENDING.
   Swap for a real photo when available and bump `dateModified`.
6. **Exact current build-out status** — described as "largely built out" based on
   a "Kilkenny Farms-archived" listing on newhomesource.com (search snippet only,
   not confirmed by direct fetch) plus the 2014 origin date. Reasonable inference,
   not independently verified.
7. **Comparison table (Southbridge, Westbridge, Heritage Hills) price ranges** —
   intentionally left out of the comparison table rather than pulled from those
   pages' own (also-pending) Market Data sections.

## Phase 4b QA — results

- `grep -c "#johnreuter"` → **0**
- `grep -c "#organization"` → **0**
- `grep -ci "quinn drive"` → **0**
- `grep -c "DRAFT"` → **0**
- `grep -c "\[ John"` (bracketed editorial prompt) → **0**
- `grep -c "1025"` → **0**
- `grep -ci "todo"` → **0**
- `grep -c "\[SUBDIVISION"` (unfilled template token) → **0**
- JSON-LD: parsed successfully with `python3 json.loads` — 4 `@graph` nodes
  (WebPage, BreadcrumbList, Place, FAQPage), all using `#john`/`#org` `@id`-only
  stubs, no full Person/Organization node redefined on the page.
- Rendered full-page with Playwright (Chromium at
  `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`), screenshot saved as
  `qa-screenshot.png` (1400×12515). Reviewed in 8 chunks, including the purple
  Schools section and both navy/dark sections (Proximity table, CTA band, ROH
  section, footer) — no invisible or low-contrast text found, no broken images
  (none embedded — page has no photo strip since no real photos exist yet),
  layout holds together.

## Internal linking done this build
- Links up to `/waunakee/` city hub (breadcrumb, market strip, explore band)
- Links sideways to `/waunakee/kilkenny-farms-west/`, `/waunakee/southbridge/`,
  `/waunakee/westbridge/`, `/waunakee/heritage-hills/` — all already published
  pages in this repo, referenced in the About section, market strip, and the new
  comparison table
- Links to `/market-reports/waunakee-wisconsin/` and the school district guide

**Not yet done (flagged per Phase 5b):** the Waunakee city hub page itself needs
a manual edit to add Kilkenny Farms to its neighborhood directory — this page
build did not touch the hub page. Kilkenny Farms West's own page also does not
yet link back to this new Kilkenny Farms page — consider adding that cross-link
in a follow-up pass since the two are so frequently confused.

## Files
- `kilkenny-farms-v1.html` — the finished page
- `qa-screenshot.png` — full-page render used for the Phase 4b visual QA pass
- This README
