# Midvale Heights — Page Build Notes (v1, 2026-08-17)

**File:** `midvale-heights-v1.html`
**URL slug:** `https://integrityhomeswi.com/madison/midvale-heights/`
**Source:** `research/midvale-heights-research.md` (Claude leg only — Perplexity leg failed/missing; the entire brief is explicitly flagged as provisional).

This page is thinner than Kilkenny Farms West / Southbridge on purpose. The research brief itself is single-source and carries an unusually long list of "not confirmed" flags, so several sections were written as honest placeholders rather than filled with plausible-sounding invented detail.

## Non-mechanical content decisions

- **No numeric [PP]/[CL] conflict to resolve.** The brief has only a Claude leg — Perplexity never ran — so there was no cross-engine numeric conflict to average/pick/omit. Every fact is single-source `[CL]` by necessity. I did not surface the internal `[CL]` tags on the public page; I translated "single-source, not corroborated" into plain-English hedges instead (e.g., "one source describes it as..." / "reported").
- **Land area (857 acres):** stated everywhere with an explicit single-source hedge (stats-strip footnote, About section, love-grid item, FAQ answer) rather than as a flat fact.
- **Quick-Answer sentence 4 (anchor fact):** the four-slot template calls for "a specific distance to a real named place." No confirmed distance exists anywhere in the brief (Section I is an admitted total gap). Rather than invent a plausible mileage figure, I substituted the one genuinely confirmed anchor fact available — adjacency to, and joint city planning with, the Westmorland neighborhood — plus the MMSD inference. This is a deliberate deviation from the letter of the four-slot template in service of the "never put unverified data here" rule, which takes priority.
- **Schools:** no specific elementary/middle/high school is named anywhere on the page. Only "Madison Metropolitan School District, by strong geographic inference" is used, with a boundary-verification disclaimer, per the brief's explicit caveat and the Kenzie SOP's verify-don't-guess rule. The standard 4-box school-stat strip (ranking, ratio, graduation rate) used on other pages was omitted entirely — no such numbers exist in the brief.
- **Parks & Recreation and Dining & Shopping sections:** the brief flags these as complete research gaps (Sections H and I), explicitly warning that attributing a neighboring area's park (e.g., Westmorland Park, Hoyt Park) to Midvale Heights would repeat the Kilkenny/Southbridge-style conflation this project exists to prevent. Both sections were written as honest "research pending" call-outs rather than populated with a fabricated love-grid/dining-grid/park-row list. No dog park is named in the brief, so the Dog Parks section was omitted entirely per the task instructions.
- **Commute & Proximity:** no confirmed distance or drive-time to any destination exists in the brief. The usual proximity data table was replaced with two hedged paragraphs rather than a table full of "TBD" cells for every row, since a real table implies a level of anchoring the research doesn't support yet.
- **"Why People Choose It":** reduced from the usual 8-item grid to 5 items — only the number of points that are actually traceable to something in the brief (build era, reported acreage, community association longevity, general location, and the WSJ resident-sentiment headline). Padding to 8 would have required inventing generic appeal language, which the brief and project rules both explicitly prohibit.
- **Market Data section:** fully TBD, including the Sale Price Range card (Kilkenny Farms West's version has a real builder-quoted range there; Midvale Heights has no price data of any kind yet, confirmed or builder-quoted, so every card reads TBD). John's Take copy explains why rather than pretending analysis has happened.
- **Geo coordinates in schema:** the research brief does not supply a lat/long or ZIP code for Midvale Heights, and Section D explicitly says boundary streets aren't confirmed. I used an approximate near-west-side Madison coordinate pair (43.061, -89.451) for the `GeoCoordinates` schema node — this is a rough, unconfirmed geocode for structured-data purposes only, not a claim exposed to page readers. `postalCode` was omitted from the Place schema entirely rather than guessed. **Flag for John/Kenzie:** replace with a verified coordinate and ZIP once the boundary is confirmed.
- **John's Notes section:** left as bracketed placeholder questions (dated 2026-08-17) exactly like the Kilkenny Farms West template's own pattern for un-filled local intel — no invented personal anecdotes or quotes attributed to John.
- **ROH section:** removed the KFW page's specific "X miles from Truax Field" claim since no distance is confirmed for this neighborhood; kept only the standing brand-level ROH facts (501(c)(3) status, average savings figure) which are established elsewhere in the repo, not sourced from this neighborhood's research brief.
- **Author bio / footer:** no street address anywhere (per the standing subdivision-page address rule) — removed "1025 Quinn Drive" and "in the village" language entirely, including from the author bio bullet that names John's Waunakee base.

## Placeholder / pending items (tracked for follow-up)

- 🖼️ **IMAGE-PENDING** — no approved photo exists for Midvale Heights. Hero uses a navy CSS gradient placeholder (no Photo Strip section, per instructions). Swap in a real photo once sourced/approved and bump `dateModified`.
- 📊 **Market Data — fully pending.** No SCWMLS export has been pulled for this neighborhood yet. Every card in the Market Update block reads TBD.
- 🏫 **Schools — pending exact assignments.** MMSD is a strong inference only; no specific elementary/middle/high school is confirmed.
- 🌿 **Parks/Amenities — pending.** No specific park, trail, or amenity name for Midvale Heights was confirmed in the current research pass.
- 🍽️ **Conveniences — pending.** No named grocery/coffee/restaurant/pharmacy/gas business confirmed; boundary streets need to be confirmed first so a conveniences search can be properly anchored.
- 🚗 **Commute/Proximity — pending.** No confirmed distance or drive time to downtown Madison, MSN airport, or any employer.
- 🗺️ **Boundary streets — pending.** Section D of the brief has no confirmed N/S/E/W bounding streets; several downstream sections (conveniences, commute) are blocked on this.
- 🏛️ **HOA dues/authority — pending.** Community Association confirmed to exist (founded 1954) but dues and architectural-review authority are unconfirmed; do not assume either.
- 📍 **Geo coordinates / ZIP — approximate/unconfirmed**, see note above.
- 🔁 **Perplexity leg — never run.** The whole brief should be re-merged once that leg completes; this page should be revisited as a Tier 2 enrichment pass once it does, not just a data refresh.

## Interlinking (Phase 5) — not yet done

This page links up to `https://integrityhomeswi.com/madison/` (city hub) and out to the Madison market report and MMSD site, but per Phase 5b the **Madison city hub page itself has not been edited** to link back down to this new page — that's a manual follow-up step. No nearby-subdivision (Section L) links were added since none of the comparison neighborhoods named in the brief (Westmorland, Shorewood Hills, Nakoma, Dudgeon-Monroe, University Heights, Sunset Village) currently have a published Integrity Homes subdivision page to link to.

## Validation

- JSON-LD `@graph` validated with `python3 -c "import json; json.loads(...)"` — parses cleanly, 4 graph nodes (WebPage, BreadcrumbList, Place, FAQPage) plus `#john`/`#org` `@id`-only references, no redefinition.
- All 5 visible FAQ Q&A pairs verified to match the FAQPage schema entries word-for-word (scripted diff, 5/5 match).
- No "Quinn Drive" string anywhere in the file.
- No `streetAddress` field anywhere in the file (Place schema uses locality/region/country only).
- No Redfin/Zillow/Trulia-sourced pricing data; the only dollar figure on the page is the standing brand-level ROH average-savings stat, not neighborhood sold-price data.
