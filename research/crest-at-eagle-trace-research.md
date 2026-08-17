# Crest at Eagle Trace — Middleton, WI — Merged Research Brief

**Merge date:** 2026-08-17
**Claude leg retrieval date:** 2026-08-17 (source: `crest-at-eagle-trace-raw-claude.md` + `crest-at-eagle-trace-conveniences-claude.md`)
**Perplexity leg:** **MISSING / FAILED** — `crest-at-eagle-trace-raw-perplexity.md` and `crest-at-eagle-trace-conveniences.md` do not exist in `research/`. Per Phase 1a rule ("if one engine fails or times out, proceed with the other two and note the gap"), this merge proceeds on the Claude leg alone. **No union/conflict-check against Perplexity has occurred — every fact below is single-source (Claude) despite this being labeled a "merged" brief.** Re-run this merge once the Perplexity leg exists; do not treat this file as final until then.

**Tagging key:** `[CL]` = from Claude leg only. (No `[PP]` or `[PP+CL]` tags appear in this version — there is no Perplexity data to cross-reference. Once the Perplexity leg is supplied, re-merge and add those tags/conflict flags.)

**Note on source reliability (carried from raw file):** Many builder/aggregator domains (veridianhomes.com, Zillow, Trulia, Homes.com, exprealty.com, starkhomes.com, housesthatshine.com, livabl.com, mcpasd.k12.wi.us, Facebook) were blocked by the Claude leg's network egress proxy this session and could only be triangulated via search-result snippets, not full page fetches. Anything sourced only from a snippet (not a fetched page) is marked accordingly below, same as in the raw file.

---

## A. Expert Summary

Crest at Eagle Trace is an **active, currently-selling new-construction neighborhood in Middleton, WI 53562** [CL], built by **Veridian Homes** [CL]. It is the "**Crest Collection**" — a distinct, more attainably-priced product line (smaller twin homes / attached homes and simplified single-family plans) sited within or immediately adjacent to Veridian's larger **Eagle Trace** master community [CL]. Both communities sit on former farmland a short distance from **Pope Farm Conservancy**, off the Old Sauk Road / Schewe Road corridor on Middleton's far west side [CL]. Marketing copy references "three heirloom oaks planted by three Schewe sisters" as a heritage nod on the site [CL]. **Not confident** on exact plat boundaries between "Eagle Trace" and "Crest at Eagle Trace" [CL] — see Sections D and O.

## B. Verified Quick-Facts Table

| Field | Value | Confidence | Source |
|---|---|---|---|
| Subdivision name | Crest at Eagle Trace | Confirmed | [CL], search results Aug 2026 |
| City/Zip | Middleton, WI 53562 | Confirmed (multiple listings) | [CL] |
| Builder/Developer | Veridian Homes | Confirmed | [CL] |
| Parent community | Eagle Trace (Crest Collection is a sub-line within it) | Confident but not fully verified | [CL] |
| Confirmed street | Mosaic Way (10114, 10116, 10120, 10122 Mosaic Way) | Confirmed — eXp Realty listing URL nests it under `/crest-at-eagle-trace/` | [CL] |
| Product type | Twin homes ("The Astor Twin Home") and single-family plans ("The Chelsea") | Confirmed plan names exist | [CL] |
| Starting price (Astor Twin Home) | $409,900, 2 bed / 2.5 bath, 1,403 sq ft | Confirmed from search snippet, NOT a fetched page | [CL] |
| Price range cited for community | "$410K–$500K" in some snippets; a separate snippet cites "starting around $635,000" / "now selling from $626,300" for what may be the broader (non-Crest) Eagle Trace collection | **INTERNAL CONFLICT within the Claude leg itself — flagged, not resolved** | [CL] |
| Nearby landmark | Pope Farm Conservancy (Town of Middleton, 105+ acres) | Confirmed | [CL] |
| Nearby elementary | Pope Farm Elementary, 816 Schewe Rd, Middleton WI 53562 | Confirmed address; NOT confirmed as boundary-assigned school | [CL] |
| School district | Middleton-Cross Plains Area School District (MCPASD) | Confirmed | [CL] |
| Sold-price / DOM stats | **Not pulled** — pending MLS data from John | n/a | n/a |

## C. Development and Phase History

- Veridian Homes markets **Eagle Trace** and **Crest at Eagle Trace** as two related but separately-branded neighborhood pages on its own site (both under `veridianhomes.com/find/neighborhoods/region/madison/`), strongly suggesting Crest at Eagle Trace is a phase/product-collection carved out of (or adjacent to) the larger Eagle Trace development, sharing a sales/model address. [CL]
- Move-in-ready listing codes seen in search results ("5CET," "19CET," "21CET," "40CET," "1ET") appear to be Veridian's internal lot/plan numbering — "CET" plausibly Crest [at] Eagle Trace, "ET" Eagle Trace. **Not confident** — inference from naming pattern, not a confirmed source statement. [CL]
- A Veridian Facebook post title captured in search results reads "Welcome to Crest at Eagle Trace!! Our newest Middleton neighborhood..." — indicating Crest at Eagle Trace is the **newer** of the two brands. Exact launch/plat date not found — flag for John. [CL]
- No plat map, phase count, or total lot count was retrievable — primary sources (veridianhomes.com, plat/GIS pages) were blocked at the network level. [CL]

## D. Location, Streets, and Boundaries

**Confirmed street inside Crest at Eagle Trace:** **Mosaic Way** (10114–10122+ Mosaic Way, Middleton, WI 53562), explicitly nested under the `/crest-at-eagle-trace/` path on an eXp Realty listing. [CL]

**Likely-related but NOT fully confirmed to be inside Crest specifically:**
- **Tabby Turn Drive** (613, 616, 632 Tabby Turn Dr, Middleton WI 53562) — appeared in Eagle Trace search results, zip matches, but not explicitly tied to the "Crest" sub-brand. [CL]
- **White Fox Lane** (sales-office/model address, "10129 White Fox Lane") — appears in listings for BOTH "Eagle Trace" (cited with zip 53593 in one snippet) and "Crest at Eagle Trace" (cited with zip 53562 in another) at the same house number. Almost certainly one physical location/model complex with inconsistent aggregator zip data, but which subdivision boundary it falls inside could NOT be verified. **FLAG for John: verify via city/county GIS or Veridian directly.** [CL]

**Confirmed general location:** Town/City of Middleton's far west side, off the **Old Sauk Road / Schewe Road** corridor, near **Pope Farm Conservancy**, roughly 2 miles west of the Beltline (Hwy 12/18) along Old Sauk Rd. Pope Farm Conservancy's own address (7440 W Old Sauk Rd) is technically listed under Verona WI 53593, illustrating how tightly this zip/city-line area is split; Pope Farm Elementary itself (816 Schewe Rd) carries a 53562 Middleton address. This zip/municipal-line ambiguity is a genuine local quirk, not a research error. [CL]

**COLLISION FINDING (important — do not merge into Crest at Eagle Trace facts):** A separate "Eagle Trace" neighborhood by the same builder (Veridian Homes) exists with streets **Hollow Aspen Lane, Rustic Rise Way, and Windy Willow Road**, all zip **53593**, Madison/Verona-area addressing — NOT the 53562 Crest at Eagle Trace streets above. These three streets are logged as a discard for this Middleton profile (see conveniences file). Do not use them as Crest at Eagle Trace streets. [CL]

## E. Schools

- **District:** Middleton-Cross Plains Area School District (MCPASD) — confirmed, covers this part of the Town/City of Middleton. [CL]
- **Nearest elementary by proximity:** Pope Farm Elementary, 816 Schewe Rd, Middleton, WI 53562 — geographically close, same road as landmark references. [CL]
- **Nearest middle school by district structure:** Glacier Creek Middle School, 2800 Military Rd, Cross Plains, WI 53528. [CL]
- **High school:** Middleton High School (district's comprehensive high school). [CL]
- **VERIFY-BY-ADDRESS CAVEAT (mandatory):** None of the above is confirmed as the *boundary-assigned* school for Crest at Eagle Trace specifically. MCPASD's official Boundaries & Maps page (mcpasd.k12.wi.us/page/boundaries-maps) was blocked by network egress and could not be checked directly. **John must verify exact school assignment via the district's boundary lookup tool or by calling the district office before publishing anything school-specific.** [CL]

## F. Homes and Housing Products (no sold-price stats)

- **Crest Collection** product line: described by the builder as "attainably priced homes... thoughtfully crafted with the same comfort and style as [Veridian's] most loved plans, refined with smarter layouts and simplified construction," marketed as energy-efficient. [CL]
- Named plans confirmed to exist (plan names only, not current availability):
  - **The Astor Twin Home** — 2 bed / 2.5 bath, 1,403 sq ft, attached duplex-style. Starting price $409,900 per search snippet dated Aug 2026 — not independently verified against a live builder page; treat as list-price-at-time-of-snippet, not current. [CL]
  - **The Chelsea** — single-family plan; builder page exists but content not retrievable this session (blocked). [CL]
- Move-in-ready inventory homes referenced under lot codes (5CET, 19CET, 21CET, 40CET) — sq ft/bed/bath not retrieved for all. [CL]
- One specific point-in-time listing: **10116 Mosaic Way** — 3 bed / 2 bath, 1,528 sq ft, single-family, move-in ready target 7/20/26 (eXp Realty snippet) — a listing snapshot, not a standing neighborhood fact. [CL]
- Per instructions, **no sold-price, median-price, or days-on-market statistics reported** — all marked **pending MLS data from John**.

## G. HOA and Restrictions

**Not confirmed.** No HOA fee amount, HOA management company name, or CC&R document was retrievable (the builder's own neighborhood page, which would normally list HOA details, was blocked). Given this is a Veridian planned community with shared entry features (heirloom oak grouping, likely shared landscaping/monument signage), an HOA is likely to exist, but **this is an inference, not a verified fact — do not publish an HOA fee without confirming directly with Veridian Homes or the plat's CC&Rs.** Per project rules, no fee figure from any Southbridge/Kilkenny-type context should ever be applied here. [CL]

## H. Parks, Trails, and Amenities

- **Pope Farm Conservancy** — standout nearby amenity: 105+ acre Town of Middleton-owned natural area with walking trails, prairie/wildflower plantings, 40+ interpretive signs, and seasonal events (sunflower/sunrise viewing is a known regional draw, though not independently re-confirmed this session). Confirmed as adjacent/nearby, not confirmed as literally bordering every Crest at Eagle Trace lot. [CL]
- Marketing copy references being "surrounded by gorgeous parks and golf courses" — **generic builder language, not itemized**. No specific golf course name confirmed. **Flag for John** to confirm which golf course(s) (candidates along the Hwy 12 corridor, not confirmed by name — do not guess). [CL]
- No neighborhood-internal amenities (pool, clubhouse, playground within the plat) were confirmed or denied — absence of evidence, not evidence of absence. **Flag for John to verify with Veridian.** [CL]

## I. Nearby Conveniences with Distances

*(Merged from `crest-at-eagle-trace-conveniences-claude.md`. All distances below are approximate, road-network estimates from general known geography of this corridor — mapping tools were blocked this session, not a routed/measured output. Verify with an actual map before publishing.)*

**Grocery** — **Metcalfe's Market** confirmed as an operating Middleton-area grocer (Chamber of Commerce member listing), but exact Middleton street address not confirmed this session (only a Madison location at 726 N Midvale Blvd independently verified). **Not confident** this is the closest grocery option — flag for John to confirm nearest full grocery store. [CL]

**Gas / Convenience** — **Middleton Farmers Cooperative (Cenex)**, 1755 Pleasantview Road, Middleton, WI — confirmed operating; distance not independently measured. **Kelleys Market / Middleton Mobil** — "just off Highway 14 on the way to Cross Plains," fuel plus grocery/hot food; confirmed operating, exact address/distance not verified. [CL]

**Coffee / Restaurants / Pharmacy / Healthcare / Library** — **Not confirmed this session.** No specific named, currently-operating business could be verified for this corner of Middleton (Old Sauk/Schewe). **Gap — flag for John** to fill in rather than publish a guessed business name. [CL]

**Parks / Trails** — Pope Farm Conservancy (see Section H); address on file 7440 W Old Sauk Rd, listed under Verona WI 53593 despite being a Town of Middleton facility (same municipal-line ambiguity noted in Section D). Distance not precisely measured; plausibly walkable or a very short drive — **John should confirm actual walkability/distance.** [CL]

**Schools (proximity only — see Section E for boundary caveat)** — Pope Farm Elementary (816 Schewe Rd); Glacier Creek Middle School (2800 Military Rd, Cross Plains); Middleton High School (address not re-verified). [CL]

**Route to Downtown Middleton** — Not independently routed (mapping tool blocked). Downtown (University Ave/Parmenter St core) generally reached by heading east on Old Sauk Road toward the Beltline (Hwy 12/18), then into central Middleton — estimated single-digit-mile drive; **John should confirm actual route/time.** [CL]

**Nearest Highway On-Ramp** — Beltline (US Hwy 12/18) very likely nearest, reachable via Old Sauk Road, roughly the same ~2-mile range cited for Pope Farm Conservancy's own address. Not independently measured — estimate pending map verification. [CL]

**Drive Time to Madison Employment Centers** — Not independently verified. Rough unverified estimate 20–30 minutes depending on destination/traffic, based on the ~2-mile Old Sauk Road distance to the Beltline. **Estimate only.** [CL]

**Drive Time to Dane County Regional Airport (MSN)** — General search results put Middleton overall at roughly 12.2 miles / ~22–25 minutes from MSN under normal traffic. This far-west pocket (near Pope Farm Conservancy) is farther from the airport than central Middleton, so actual drive time from Crest at Eagle Trace is likely **somewhat longer than 22–25 minutes** — not independently measured, flag for John. [CL]

## J. What Residents Value

Not sourced from resident-generated content (no NextDoor, local FB group, or resident review threads were retrievable this session). Based only on builder marketing framing, prospective buyers appear to be sold on: proximity to Pope Farm Conservancy and its trails, a "farmland heritage" identity (heirloom oak trees, historic Middleton farmland site), and — for the Crest Collection specifically — **more attainable pricing** than Veridian's standard single-family Eagle Trace product, i.e., an entry point for buyers who want the area but not the $600K+ price point. **This entire section is builder-marketing-derived inference, not verified resident sentiment.** Recommend John supplement with actual resident/agent-network input before client-facing use. [CL]

## K. Possible Considerations

- **Active construction zone** — as a currently-selling new-construction community, expect ongoing building activity, construction traffic, and an evolving streetscape near-term; how many phases remain unbuilt is not confirmed. [CL]
- **Price-point conflict unresolved** (see Section B) — if the $600K+ figures actually belong to the parent Eagle Trace collection and not Crest, Crest genuinely undercuts it significantly; if the figures were miscategorized in search snippets, the real spread could be narrower. Needs resolving before quoting any price range to a client. [CL]
- **Zip/municipal boundary complexity** in this specific pocket of Middleton (53562/53593, Middleton/Verona-adjacent) could affect municipal services, some school assignments, and potentially property tax jurisdiction. Flag for John. [CL]
- **HOA unknown** — buyers will ask; John needs the fee/CC&R answer before this converts to client-ready content. [CL]

## L. Comparison With Nearby Subdivisions

- **Eagle Trace (parent/main collection, same builder, same immediate area):** Larger, pricier single-family homes (cited starting ~$626,300–$635,000 in snippets) vs. Crest's more compact/attached product starting ~$409,900. Same builder, same general Pope Farm Conservancy-adjacent location — genuinely easy to conflate with Crest at Eagle Trace; be precise about which collection a listing belongs to. [CL]
- **Eagle Trace, Verona/far-west-Madison area (DIFFERENT, unrelated development, also by Veridian Homes, zip 53593, streets Hollow Aspen Lane / Rustic Rise Way / Windy Willow Road):** The collision case flagged in the task brief. **Do not confuse with Crest at Eagle Trace, Middleton 53562.** Same builder, similar name, likely different municipality/school district (not independently confirmed which district serves that Verona-area Eagle Trace — out of scope here). [CL]
- No comparison data gathered for Kilkenny Farms West or Southbridge — different city (Waunakee, not Middleton) and a different project entirely; noted only to reaffirm no cross-contamination with the separate Waunakee subdivisions work in this repo. [CL]

## M. Frequently Asked Questions

1. **Is Crest at Eagle Trace the same as Eagle Trace?** No — Crest at Eagle Trace ("the Crest Collection") is a distinct, more attainably-priced product line by the same builder (Veridian Homes), in the same immediate Middleton location, but marketed and priced separately from the main Eagle Trace single-family collection. [CL]
2. **Is this the same as the "Eagle Trace" near Verona?** No. There is a separate, unrelated-by-plat "Eagle Trace" development (also Veridian Homes) with streets Hollow Aspen Lane, Rustic Rise Way, and Windy Willow Road, zip 53593, in the Verona/far-west-Madison area. Do not conflate. [CL]
3. **What school district?** Middleton-Cross Plains Area School District — confirmed at the district level; specific school assignment not yet boundary-verified (see Section E). [CL]
4. **Is there an HOA?** Not confirmed either way this session — verify directly with Veridian Homes before answering a client. [CL]
5. **What's nearby?** Pope Farm Conservancy is the standout confirmed amenity; see Section I for named businesses (several categories remain unconfirmed gaps). [CL]

## N. "Only a Local Would Know" Content Ideas (11)

*(Content angles for John to verify and personalize — not verified local color, since no resident-level sourcing was available this session.)*

1. The "three heirloom oaks planted by three Schewe sisters" story on-site — a literal, name-checkable piece of the land's farm history that could anchor a video or blog intro (verify exact location/visibility from the street before filming). [CL]
2. The Pope Farm Conservancy sunflower/prairie bloom season is a known regional seasonal draw in this part of Middleton — confirm current-year bloom timing before promising it in content. [CL]
3. The Schewe Road name itself ties directly to the farm family referenced in the oak story — a "why is it called that" angle. [CL]
4. The Crest Collection vs. Eagle Trace price-point split is itself a locally-useful selling point/FAQ ("get into this pocket of Middleton starting in the $400s") — confirm current live price range with Veridian before using publicly given the conflict flagged above. [CL]
5. The Middleton/Verona zip-line ambiguity in this micro-area (53562 vs 53593 addresses within a stone's throw of each other) is hyper-local nuance that separates a real local agent from a generic listing site — worth a short "did you know" content beat once verified. [CL]
6. Twin-home/attached product in the Crest Collection may appeal specifically to downsizers or first-time buyers wanting new construction without full single-family maintenance — confirm actual buyer profile with Veridian's sales team. [CL]
7. Proximity to golf courses is claimed in builder marketing but unnamed — running this down (which course, how far) turns generic copy into a specific, checkable local fact. [CL]
8. Whether Pope Farm Elementary is the actual boundary school is exactly the kind of "everyone assumes X" trap worth mythbusting on video once confirmed either way. [CL]
9. Construction-phase status (which streets/lots are built vs. still under construction as of a given content date) is fast-changing, hyper-local, and worth refreshing before every content push. [CL]
10. The "CET" lot-numbering pattern (5CET, 19CET, etc.) suggests Veridian tracks Crest at Eagle Trace as its own numbered phase — confirming the actual phase count/timeline with Veridian's sales office would make a genuinely differentiated "state of the neighborhood" update. [CL]
11. Model home / sales office location and hours (White Fox Lane address, pending boundary confirmation) is useful, evergreen, checkable content once verified live. [CL]

## O. Missing Information John Should Verify

1. **Resolve the price-range conflict**: is $410K–$500K the accurate current Crest Collection range, and is $626K–$635K+ the *separate* main Eagle Trace collection range? Confirm directly with Veridian Homes sales office.
2. **HOA fee, HOA management company, and CC&R restrictions** — not found this session.
3. **Exact plat boundary** between Eagle Trace and Crest at Eagle Trace — which streets belong to which brand (Mosaic Way confirmed Crest; Tabby Turn Dr and White Fox Lane unconfirmed).
4. **School boundary verification** via MCPASD's official boundary lookup tool (mcpasd.k12.wi.us/page/boundaries-maps) — blocked this session.
5. **Named golf course(s)** referenced in builder marketing — not identified.
6. **Current construction/phase status** — how many lots built, under construction, or still platted-but-unbuilt.
7. **Sold-price, median-price, and days-on-market data** — intentionally not pulled per instructions; needs MLS data from John.
8. **Model home / sales office hours and exact confirmed address** (White Fox Lane number, correct zip).
9. **Whether the neighborhood has sidewalks, streetlighting, or any completed (not just planned) internal amenities.**
10. Direct confirmation that Pope Farm Conservancy's main trailhead/parking is genuinely walkable from the subdivision vs. a short drive.
11. **Named grocery, coffee, restaurant, pharmacy, healthcare, and library options** closest to the Old Sauk/Schewe corridor — all gaps this session (Section I).
12. **Routed distances/drive times** (downtown Middleton, Beltline on-ramp, Madison employment centers, MSN airport) — all estimates pending an actual map check this session.
13. **PERPLEXITY LEG ITSELF** — the entire Perplexity research pass (`crest-at-eagle-trace-raw-perplexity.md`, `crest-at-eagle-trace-conveniences.md`) is missing. Re-run it and re-merge; treat every fact in this file as single-source until then.

## P. Sources with Direct Links

- [Crest at Eagle Trace by Veridian Homes in Middleton WI | Zillow](https://www.zillow.com/community/crest-at-eagle-trace/31431731_plid/) — snippet only, page fetch blocked; general description/pricing/address snippet only, NOT sold-price data.
- [Crest at Eagle Trace, Middleton, WI 53562 | Trulia](https://www.trulia.com/builder-community/crest-at-eagle-trace--31431731) — snippet only, page fetch blocked; not used for sold-price data.
- [Eagle Trace - Crest Collection in Middleton, WI by Veridian Homes | Homes.com](https://www.homes.com/new-homes/community/eagle-trace-crest-collection/rjhxslgeynhv0/) — snippet only, page fetch blocked.
- [Middleton, Crest At Eagle Trace, WI Real Estate & Homes for Sale | eXp Realty](https://www.exprealty.com/middleton-wi-real-estate/crest-at-eagle-trace) — snippet only, page fetch blocked.
- [10116 Mosaic Way, For Sale in Middleton | eXp Realty](https://www.exprealty.com/middleton-wi-real-estate/crest-at-eagle-trace/10116-mosaic-way) — key source confirming Mosaic Way's Crest at Eagle Trace nesting; snippet only.
- [Crest At Eagle Trace Real Estate & Homes for Sale in Middleton, WI | housesthatshine.com](https://www.housesthatshine.com/results-gallery/?hood=8599769) — snippet only, page fetch blocked.
- [Crest at Eagle Trace | Neighborhoods | Veridian Homes](https://veridianhomes.com/find/neighborhoods/region/madison/crest-at-eagle-trace/) — primary builder source, **fetch blocked** — flagged for John to check directly.
- [Eagle Trace | Neighborhoods | Veridian Homes](https://veridianhomes.com/find/neighborhoods/region/madison/eagle-trace/) — primary builder source, **fetch blocked**.
- [Middleton WI Residential Properties | Stark Company Realtors](https://www.starkhomes.com/s/wi/middleton-city/crest-at-eagle-trace-subdivision) — snippet only, page fetch blocked.
- [Pope Farm Conservancy - South (105.3 acres) | Town of Middleton](https://town.middleton.wi.us/index.asp?SEC=CA102B3D-5C8E-4FEC-8A29-0C90F2908CC0&DE=EA815CED-3887-476A-9D24-7D0C5B14EA19) — reachable in search snippet, confirms conservancy acreage/ownership.
- [Friends of Pope Farm Conservancy](https://www.popefarmconservancy.org/) — snippet only.
- [Middleton-Cross Plains Area School District | Boundaries & Maps](https://www.mcpasd.k12.wi.us/page/boundaries-maps) — **fetch blocked**, authoritative source John should check directly.
- [Middleton-Cross Plains School District | Wikipedia](https://en.wikipedia.org/wiki/Middleton-Cross_Plains_School_District) — general district background, snippet only.
- [613 Tabby Turn Drive, Middleton, WI 53562 | Redfin](https://www.redfin.com/WI/Middleton/613-Tabby-Turn-DR-53562/home/198838875) — used only to confirm street/zip existence, NOT price data.
- [9907 White Fox Ln, Middleton, WI 53562 | Coldwell Banker](https://www.coldwellbankerhomes.com/chicago-milwaukee/9907-white-fox-ln/pid_66197285/) — used only to confirm street/zip existence, NOT price data.
- [Eagle Trace by Veridian Homes, Middleton, WI, 53593 | Redfin](https://www.redfin.com/WI/Middleton/Eagle-Trace/community/26120) — snippet only; contributes to the zip-ambiguity flag in Section D.
- [Lot #8 Rustic Rise Way, Middleton, WI 53593 | Homes.com](https://www.homes.com/property/lot-8-rustic-rise-way-middleton-wi/vhwg93zzn1qcr/) — used to identify the Hollow Aspen/Rustic Rise/Windy Willow street cluster as belonging to a DIFFERENT, 53593-addressed Eagle Trace.
- [602 Windy Willow Rd, Middleton, WI 53593 | Trulia](https://www.trulia.com/p/wi/middleton/602-windy-willow-rd-middleton-wi-53593--2452022447) — same collision-cluster confirmation, snippet only, NOT used for its cited sold-price.

*(All sources above from the Claude leg. No Perplexity sources exist to add — see header.)*
