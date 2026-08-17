# Middleton Hills — Middleton, WI — Merged Research Brief

**Merge date:** 2026-08-17

**Leg retrieval dates:**
- Claude leg (raw + conveniences): retrieved 2026-08-17
- Perplexity leg: **MISSING** — `research/middleton-hills-raw-perplexity.md` and
  `research/middleton-hills-conveniences.md` were not found in the repo. This
  merge proceeds on the Claude leg only, per the README's "if one engine
  fails, proceed with the others and note the gap" rule. **This brief has not
  been cross-checked against a second engine — treat it as single-source
  until the Perplexity leg is run and merged in.**

**Tagging key:** `[CL]` = Claude leg only (the only leg available this pass).
No `[PP]` or `[PP+CL]` tags appear anywhere in this document because the
Perplexity leg does not exist yet — this is not a merge decision, it's a
missing input. Re-tag on the next pass once Perplexity data exists.

> Note: this brief also inherits several **internal** conflicts that surfaced
> within the single Claude leg itself (two sources the Claude leg pulled from
> disagreed with each other). These are flagged below exactly as the union
> rules require for cross-engine conflicts — not silently resolved — even
> though both sides trace back to the same engine.

---

## A. Expert Summary [CL]

Middleton Hills is a ~400–428-unit master-planned New Urbanist neighborhood in
the City of Middleton, WI, roughly one mile north of downtown Middleton and
about 8 miles from the Wisconsin State Capitol in Madison. It was designed in
1993 by DPZ (Andres Duany and Elizabeth Plater-Zyberk), the firm credited with
founding the New Urbanism movement, and is widely cited as the first New
Urbanist community built in Wisconsin. It has a walkable interconnected street
grid, narrow tree-lined streets, alley-loaded garages, front porches, small
lots, a mix of single-family homes, townhouses, apartments, and live/work
units, and a pedestrian-oriented commercial center along Frank Lloyd Wright
Avenue. Homes commonly reflect Prairie and Craftsman styles as a nod to Frank
Lloyd Wright, who was Wisconsin-based. This is a **single, distinct
neighborhood** — not to be confused with any other "Middleton Hills" outside
Wisconsin, and not to be confused with other Middleton, WI subdivisions such
as Rolling Hills or Parkside Heights.

## B. Verified Quick-Facts Table

| Fact | Value | Confidence / Source |
|---|---|---|
| City | Middleton, WI (Dane County) | Confirmed, multiple sources [CL] |
| Designer/master planner | DPZ (Andres Duany & Elizabeth Plater-Zyberk), 1993 plan | Confirmed, ULI case study snippet, mikezenz blog [CL] |
| Approx. residential units | ~400 (per HOA-adjacent source) to 428 (per ULI case study) | **CONFLICT (internal to CL leg, not reconciled)** — likely different count-dates/phases [CL] |
| Commercial space | ~102,800 sq ft | ULI case study snippet only — not independently confirmed [CL] |
| Distance to downtown Middleton | ~1 mile north | Homes.com summary — not confident on exact figure [CL] |
| Distance to Madison Capitol | ~8 miles | dsirealestate.com / homes.com summaries [CL] |
| Drive time to Downtown Madison | ~20 min via University Ave (one source); ~10 min via Hwy 14 (separate source, for "western Middleton" generally, not Middleton Hills specifically) | **CONFLICT (internal to CL leg) — flag, do not merge silently** [CL] |
| School district | Middleton-Cross Plains Area School District (MCPASD) | Confirmed [CL] |
| HOA / neighborhood association | Middleton Hills Neighborhood Association; managed by DSI Real Estate Group, LLC; Architectural Review Committee (MHARC) | Confirmed via page titles/URLs only — dues/covenant text not fetched (egress-blocked) [CL] |
| Signature streets | Frank Lloyd Wright Ave (commercial spine + homes), Century Ave (commercial frontage) | Confirmed via multiple listing sources [CL] |
| Home era | Most built after 2000 | dsirealestate/homes.com summary [CL] |
| Typical home size | 3,000–4,000 finished sq ft, 3–5 bedrooms, Prairie/Craftsman style | Multiple sources, consistent [CL] |

**Gap:** no Perplexity leg to cross-check any of the above against — every row
above rests on Claude's search coverage alone.

## C. Development and Phase History [CL]

- 1993: Master plan designed by DPZ (Duany Plater-Zyberk & Company) for a site
  north of downtown Middleton. Site plan described as shaped like "a wide
  question mark," running north–south.
- Development proceeded gradually over subsequent years/decades ("has since
  then slowly developed" per search-summary text); one source states
  development "began in the late 1990s."
- Design intent: interconnected street grid (breaking from cul-de-sac
  suburban norms), narrow streets, alleys for garage access, small yards,
  relatively high density for a suburban setting, a walkable town-center-style
  commercial core.
- Notability: cited as the first New Urbanist community in Wisconsin; has
  drawn planners, developers, and city staff from around the world to study
  it (per ULI/search-summary text).
- **Not confident** on: exact phase boundaries/names, exact build-out
  completion date, or a verified final unit count (see the 400 vs. 428
  discrepancy in Section B — a genuine internal conflict, left unresolved).
  John should verify phase history against the City of Middleton planning
  department or the neighborhood association directly — the official history
  page (middletonhills.org/history.php) could not be fetched (egress-blocked);
  only search-snippet-level detail was available.

## D. Location / Streets and Boundaries [CL]

Confirmed streets associated with Middleton Hills addresses/commercial center:
- **Frank Lloyd Wright Avenue** — the neighborhood's commercial and mixed-use
  spine; confirmed addresses include 6712, 6741, 6754, 6767, 6846, 6934 Frank
  Lloyd Wright Ave, Middleton, WI 53562 (residential, live/work, and
  restaurant listings).
- **Century Avenue** — commercial frontage along the development's base per
  the ULI case-study summary; a Kwik Trip gas station sits on Century Ave —
  **CONFLICT (internal to CL leg):** two different addresses appeared, 7508
  Century Ave (GasBuddy) and 6519 Century Ave (Yelp), for what may be the same
  or different stations — not reconciled, flagged rather than guessed.
- **University Avenue** — cited as the commute route toward downtown Madison.
- **Bear Claw Way** — appears in an apartment-community listing (Paragon
  Place) tied to a Middleton, WI 53562 address; relationship to the core
  Middleton Hills subdivision boundary is **not confirmed** — flag for
  verification.

**Gap:** a precise, sourced boundary description (i.e., "bounded by X to the
north, Y to the south," etc.) or a full street list was not found. Streets
like "North Street," "Blue Bell Drive," and "Deer Trail" were considered based
on general Middleton-area naming patterns but could not be confirmed as inside
Middleton Hills — deliberately excluded rather than guessed. John should pull
the City of Middleton GIS/plat map or the neighborhood association's own
boundary map to lock this section down.

## E. Schools [CL]

- **District:** Middleton-Cross Plains Area School District (MCPASD),
  confirmed.
- District has 7 elementary schools: Elm Lawn, Park, Pope Farm, Northside,
  Sauk Trail, Sunset Ridge, West Middleton; 2 middle schools (incl. Kromrey
  Middle School); 1 high school (Middleton High School) + 1 alternative senior
  high.
- **Likely elementary assignment:** Northside Elementary School, 3620 High Rd,
  Middleton, WI — noted as the elementary school nearest to Kromrey Middle
  School (0.6 mi) and geographically closest to the Middleton Hills area.
  **This is a proximity inference, NOT a verified attendance-zone
  assignment.** Elm Lawn Elementary was also surfaced as a candidate with no
  boundary confirmation either way.
- **Middle school:** Kromrey Middle School is geographically closest;
  feeder-pattern (which elementary schools feed Kromrey vs. the district's
  other middle school) was **not confirmed**.
- **High school:** Middleton High School (single comprehensive high school
  serving the district, per Wikipedia summary) — likely the assignment for
  all MCPASD residential addresses, but not verified address-by-address.
- **VERIFY-BY-ADDRESS CAVEAT (required):** MCPASD draws attendance boundaries
  by exact street address and boundaries can be redrawn between school years.
  Nothing in this section should be presented to a buyer as guaranteed. John
  should confirm current-year assignment via MCPASD's boundary lookup tool
  (mcpasd.k12.wi.us) or by calling the district office at (608) 829-9000 for
  the specific address in question before publishing any client-facing claim.

## F. Homes and Housing Products [CL]

- Mix of product types: detached single-family homes, townhouses, condos/
  apartments, and live/work units (residential over ground-floor commercial),
  concentrated near the Frank Lloyd Wright Ave commercial core.
- Typical single-family home: 3,000–4,000 finished sq ft, 3–5 bedrooms,
  Prairie- and Craftsman-style architecture, most built after 2000.
- Lots are notably small/narrow by suburban standards, with garages
  alley-loaded off rear lanes rather than fronting the street — a defining
  New Urbanist design feature here.
- A high-end current listing example (architectural/product-type reference
  only, NOT a market statistic): 6934 Frank Lloyd Wright Ave — 5 bed / 4.5
  bath / 3,903 sq ft, listed asking price $1,299,900 per a late-2026 Redfin
  listing snippet. **One individual asking-price data point, not a market
  average — do not extrapolate.**
- Per house rules: **no sold-price, median-price, or days-on-market
  statistics are reported here — pending MLS data from John.**

## G. HOA and Restrictions [CL]

- **Association:** Middleton Hills Neighborhood Association.
- **Management company:** DSI Real Estate Group, LLC (confirmed via page
  titles/URLs: "Middleton Hills Neighborhood – DSI Real Estate Group, Inc.,"
  including sub-pages for "Covenants & Bylaws" and an "Architectural Review
  Committee (MHARC)").
- Private alleys within the neighborhood are technically private
  rights-of-way and are HOA-maintained (per search-summary text referencing
  winter-clearing obligations).
- There is a documented Architectural Review Committee (MHARC) — implies
  design-review requirements for exterior changes, consistent with a
  New-Urbanist-planned community.
- **Gap — not confirmed:** exact annual dues amount, what dues cover, rental
  restrictions, or full covenant text. The DSI Real Estate Group pages and the
  neighborhood association's own site (middletonhills.org) were both blocked
  by network egress rules and could not be fetched directly — only page
  titles/URLs were visible via search. **Do not quote a dues figure to a
  client without John independently pulling it from DSI Real Estate Group or
  the HOA's resale disclosure documents.**
- A separate domain, middletonhoa.org, surfaced in search results but could
  not be confirmed as affiliated with Middleton Hills, WI specifically (may
  relate to a different "Middleton" HOA, e.g., in Tennessee) — **discarded,
  not used.**

## H. Parks, Trails, and Amenities [CL]

- **Middleton Hills Park** (main park): playground, basketball court,
  volleyball courts, soccer field, picnic tables, and a wood-plank boardwalk
  for nature viewing. No dedicated parking lot; on-street parking only near
  the main entrance.
- **Middleton Hills Neighborhood Park–North**: a 4.8-acre park on the north
  side of the neighborhood with a playground (ages 5–12) including a spider
  net climbing structure, a sandbox with two sand diggers, a
  baseball/softball field with bleachers, an open-air shelter, and a winter
  sledding hill.
- Sidewalks throughout, consistent with the neighborhood's walkable design
  intent.
- **No pool found** associated with either park — do not claim pool access
  for Middleton Hills without further verification.
- Pope Farm Conservancy is a well-known nearby Middleton landmark/park but was
  **not confirmed** as part of or adjacent to Middleton Hills itself — treat
  as a general-area amenity, not a Middleton Hills amenity, until proximity is
  verified.

## I. Nearby Conveniences with Distances [CL]

**Anchored streets:** Frank Lloyd Wright Avenue (neighborhood commercial
spine) and Century Avenue (commercial frontage), with University Avenue as
the primary commute corridor toward downtown Madison. All distances below are
estimated from this anchor point and are approximate — not measured
address-to-address from a specific home — until John pins an exact street
address.

**Grocery**
- Metcalfe's Market — could not confirm a Middleton, WI store location;
  confirmed locations found were in Madison (Hilldale) and Wauwatosa. **Not
  confident** a standalone Middleton Hills-area location exists.
- Trader Joe's — referenced near "Greenway Station" / 8401 Greenway Blvd,
  Middleton, WI 53562, but Greenway Station's own tenant list did not confirm
  Trader Joe's as a tenant in the snippets retrieved. **Flag: address needs
  confirmation before use.**
- Hy-Vee and Woodman's Food Market referenced generally as Middleton-area
  grocery options, without specific confirmed addresses.
- **Action item:** none of the above grocery addresses were independently
  verified against a live store locator (multiple retailer domains were
  egress-blocked). Confirm current addresses and distance before publishing.

**Gas**
- Kwik Trip — Century Ave, Middleton, WI 53562. **CONFLICT (internal to CL
  leg):** 7508 Century Ave (GasBuddy) vs. 6519 Century Ave (Yelp) — not
  reconciled; needs confirmation before publishing.

**Coffee**
- No coffee shop confirmed inside the Middleton Hills commercial center
  itself.
- General Middleton-area options surfaced (not confirmed as Middleton
  Hills-proximate): Grace Coffee Co. (1824 Parmenter St), Vitruvius Coffee and
  Tea (7429 Elmwood Ave), Burman Coffee Traders (2140 W Greenview Dr #2).
  Distances from Middleton Hills not verified.

**Restaurants**
- **Pasqual's Cantina** — 6712 Frank Lloyd Wright Ave #102, Middleton, WI
  53562. **Confirmed inside the Middleton Hills commercial center itself**
  (multiple sources explicitly place it in "Middleton Hills Commercial
  Center"). Tex-Mex/Southwestern; a genuine walkable, on-site amenity for
  residents.
- No other sit-down restaurants inside the neighborhood core were confirmed;
  additional dining along Century Ave / University Ave is likely but not
  individually verified.

**Pharmacy / Healthcare**
- **CVS Pharmacy** — 6210 Century Ave, Middleton, WI 53562. Confirmed
  address, includes drive-thru pharmacy.
- **UW Health / Junction Road Medical Center** — referenced as serving the
  Middleton area; distance from Middleton Hills **not verified.**
- Walgreens referenced generally as present in Middleton; no confirmed
  address retrieved.

**Library**
- **Middleton Public Library** — 7425 Hubbard Ave, Middleton, WI 53562,
  (608) 831-5564. Confirmed address; South Central Library System. Distance
  from Middleton Hills not precisely measured but consistent with the ~1 mile
  downtown-proximity figure.

**Parks / Schools (cross-ref Sections H/E)**
- Middleton Hills Park and Middleton Hills Neighborhood Park–North are inside
  the neighborhood itself; no street address confirmed for either, access via
  internal streets, on-street parking only.
- Northside Elementary — 3620 High Rd; plausible nearest school, attendance
  zone unconfirmed. Kromrey Middle School — closest middle school (0.6 mi
  from Northside), feeder pattern unconfirmed. Middleton High School — likely
  sole MCPASD high school, not boundary-verified.

**Route to Downtown Middleton**
- Consistently described as roughly **1 mile north of downtown Middleton** —
  a likely sub-5-minute drive, though no source gave an exact minutes figure.
  **Not confident** on an exact drive time.

**Nearest Highway On-Ramp**
- Century Avenue and University Avenue both connect toward US Highway 12/14
  (Middleton's main highway corridor). **Exact on-ramp location and distance
  not independently verified** — flag for a live-map check.

**Drive Time to Madison Employment Centers**
- Downtown Madison: **CONFLICT (internal to CL leg)** — ~20 min via
  University Avenue (one source, specific to Middleton Hills) vs. ~10 min via
  Highway 14 (separate source, for "western Middleton neighborhoods"
  generally, not confirmed specific to Middleton Hills). Do not present
  either as settled; recommend a live-map spot-check from a specific address
  at a normal commute hour.
- UW-Madison campus / West Madison employment corridors (e.g., University
  Research Park): not independently researched — gap.

**Dane County Regional Airport (MSN)**
- General Middleton-to-MSN driving distance found: **~12 miles, ~22 minutes**
  (Travelmath), but this is a **Middleton-wide estimate, not measured from
  Middleton Hills specifically.** Plausibly similar or slightly longer given
  the ~1-mile-north position — not independently confirmed.

**Discarded due to name collision or unconfirmed affiliation**
- middletonhoa.org — could not be confirmed as affiliated with Middleton
  Hills, WI (search context suggests a differently-named "Middleton" HOA
  elsewhere, e.g., Nashville, TN). Discarded.
- Rolling Hills HOA, Middleton, WI — real but a separate subdivision/HOA, not
  Middleton Hills. Flagged only to prevent conflation.
- Parkside Heights, Middleton, WI — another distinct Middleton neighborhood;
  not used as a source for any Middleton Hills fact.
- "Cafe Continental" / "Icon Nightclub" — searched for as possible commercial
  tenants on a general assumption; no evidence either exists in Middleton, WI
  at all. Fully discarded.
- Middleton, MA and other out-of-state "Middleton" listings — excluded from
  all findings due to shared place-name.

## J. What Residents Value [CL]

Based on the design intent and repeatedly-cited features across sources — not
resident-survey data. **Not confident this reflects actual resident
sentiment**, only inferred from what the development is built and marketed
around:
- Walkability — sidewalks throughout, interconnected grid, short walk to a
  commercial center with restaurants and shops.
- Traditional/architectural character — Prairie and Craftsman styles, front
  porches, a "small town" aesthetic distinct from typical cul-de-sac
  subdivisions.
- Proximity to downtown Middleton and a relatively short commute to downtown
  Madison.
- Parks and green space within walking distance (two dedicated neighborhood
  parks).
- The novelty/prestige of living in a nationally studied planning example —
  anecdotally, planners and city officials visit to study the neighborhood,
  which residents may take some pride in, but this is inference, not a
  sourced resident quote.

## K. Possible Considerations [CL]

- Small lots and alley-loaded garages mean less private yard space than a
  typical suburban subdivision — worth flagging for buyers who want a large
  yard.
- No confirmed on-site pool; parking is limited at the main park (no
  dedicated lot).
- HOA architectural review (MHARC) implies exterior modification approval
  requirements — buyers who want full design freedom should be told to review
  covenants before purchase.
- Two conflicting unit-count figures (400 vs. 428) and two conflicting
  commute-time figures suggest some published sources may be dated or drawn
  from different original documents (e.g., an original ULI case study vs.
  current realtor copy) — treat marketing copy about this neighborhood
  cautiously and verify current figures before reusing them.
- Dues amount unverified — could be a material cost consideration for buyers;
  must be confirmed before quoting.

## L. Comparison With Nearby Subdivisions [CL]

- **Rolling Hills (Middleton, WI):** A separate, distinctly named HOA
  community. Not the same neighborhood as Middleton Hills — flagged
  explicitly so the two are not conflated in any client-facing copy.
- **Parkside Heights (Middleton, WI):** Another distinct Middleton
  neighborhood referenced in search results (homes.com local guide) — not
  further researched; noted only to avoid confusion.
- General positioning: Middleton Hills is distinguished from typical Dane
  County subdivisions (including Integrity Homes' own Kilkenny Farms West /
  Southbridge product) by its New Urbanist design pedigree, walkable
  commercial core, and older/denser lot pattern versus new-construction,
  larger-lot subdivisions. A true builder-by-builder or price-band comparison
  was **not performed** — flagged as a gap.

## M. Frequently Asked Questions [CL]

- **Is Middleton Hills in the City of Middleton or the Town of Middleton?**
  City of Middleton, per multiple sources. (Town of Middleton is a distinct,
  separate municipality nearby — do not conflate.)
- **Who designed Middleton Hills?** DPZ (Andres Duany and Elizabeth
  Plater-Zyberk), 1993 master plan.
- **Is there an HOA?** Yes — Middleton Hills Neighborhood Association,
  managed by DSI Real Estate Group, LLC, with an Architectural Review
  Committee (MHARC). Dues amount not verified.
- **What school district?** Middleton-Cross Plains Area School District.
  Specific school assignment must be verified by address.
- **Is there a pool?** Not confirmed. Do not promise one.
- **How far to downtown Madison?** Sources conflict (10–20 minutes depending
  on route/source) — verify current drive time before quoting to a client.

## N. "Only a Local Would Know" Content Ideas [CL]

1. Middleton Hills is Wisconsin's first true New Urbanist neighborhood — a
   talking point most buyers touring newer Dane County subdivisions have
   never heard, and a natural comparison/contrast video against Kilkenny
   Farms West or Southbridge's more conventional layouts.
2. The garages are almost all alley-loaded — a "spot the garage" walk-and-talk
   clip could be a fun visual hook (verify on-site before filming).
3. The commercial center along Frank Lloyd Wright Ave (Pasqual's Cantina,
   live/work units) means residents can walk to a sit-down restaurant — a
   strong "day in the life" B-roll opportunity.
4. Two distinct neighborhood parks (main park with boardwalk vs. the
   4.8-acre North park with a sledding hill) — worth a "which park is right
   for your family" comparison, but confirm current equipment/condition
   on-site before publishing specifics.
5. Homes here nod to Frank Lloyd Wright's Prairie style — a natural tie-in
   given Wright's own Wisconsin roots (Taliesin is in the Madison area), good
   for an architecture-focused short.
6. Because the street grid is unusually interconnected for a subdivision,
   local wayfinding/GPS quirks (cut-throughs, one-ways, etc.) could be worth
   asking a resident about on camera — verify locally, not from search data.
7. City planners and developers from other cities and countries have
   reportedly toured Middleton Hills to study it — a genuinely unusual
   credibility point, but confirm with the neighborhood association before
   stating as fact on camera.
8. The mixed-unit-type model (single-family + townhomes + apartments +
   live/work in one walkable neighborhood) is unusual for the area and could
   anchor an "affordability ladder in one neighborhood" content angle —
   verify current unit-type availability before filming.
9. Because it's ~1 mile from downtown Middleton, a "walk score" or "bike to
   downtown" themed reel is plausible — verify actual walk/bike time on-site.
10. The HOA's Architectural Review Committee (MHARC) is a genuine
    differentiator vs. many Dane County subdivisions with lighter-touch HOAs
    — good material for a "know before you buy" educational post, once
    dues/covenant specifics are confirmed.
11. Kwik Trip and CVS both sit close by on Century Ave — a quick "everyday
    errands" convenience map graphic could resonate, once the correct Kwik
    Trip address is confirmed (two different addresses surfaced).
12. The "question mark" shaped site plan (per the original ULI case study
    language) is a fun bit of design trivia for a script, pending
    confirmation from a primary planning document.

## O. Missing Information John Should Verify

- **Run the Perplexity leg** — this brief is currently single-source
  (Claude only); no cross-engine merge has happened yet.
- Exact, current HOA annual dues amount and what they cover.
- Full covenant/restriction text (rental restrictions, exterior-modification
  rules, etc.) from DSI Real Estate Group or the resale disclosure packet.
- Confirmed elementary/middle school attendance-zone assignment by specific
  street address (Northside Elementary is a plausible-but-unverified
  candidate).
- A reconciled, sourced neighborhood boundary description and full street
  list (only Frank Lloyd Wright Ave and Century Ave frontage are solidly
  confirmed; Bear Claw Way's relationship to the core subdivision is
  unclear).
- Reconciliation of the 400-unit vs. 428-unit figures, and of the two
  conflicting drive-time-to-Madison figures (both internal conflicts within
  the Claude leg, unresolved).
- Confirmation of whether Middleton Hills has any pool access at all (none
  found).
- Current phase/build-out status — is the neighborhood still adding units, or
  fully built out?
- The correct current Kwik Trip address on Century Ave (7508 vs. 6519).
- Whether middletonhoa.org has any legitimate connection to this
  neighborhood (current read: likely unrelated/different-state HOA, discarded
  — worth a five-minute confirmation).
- Trader Joe's / Greenway Station tenancy — unconfirmed, flagged in Section I.
- Metcalfe's Market — no confirmed Middleton Hills-area location found.

## P. Sources (with direct links)

- [Middleton Hills (ULI Case Study PDF)](https://casestudies.uli.org/wp-content/uploads/2015/12/C039017.pdf) — page itself egress-blocked; used via search-result summary only.
- [A trip to Middleton Hills – An example of new urbanism (blog)](https://mikezenz.wordpress.com/2009/05/29/a-trip-to-middleton-hills-an-example-of-new-urbanism/)
- [New Developments and New Urbanism: The Middleton Hills Case Study](http://data.quaytest.net/APAPROCEEDINGS/PRCDS01/GRAMILL/gramill.htm)
- [Middleton Hills, Middleton WI Real Estate — Lake & City Homes](https://www.lakeandcityhomes.com/middleton-hills-middleton-wisconsin-real-estate.php) — egress-blocked, search snippet only.
- [Middleton Hills Neighborhood Association — official site](https://www.middletonhills.org/history.php) — egress-blocked, could not fetch full history page.
- [Middleton Hills Neighborhood – DSI Real Estate Group, Inc.](https://www.dsirealestate.com/hoa/middleton-hills/) — egress-blocked, page titles/URLs used only.
- [Middleton Hills, Middleton Homes for Sale with No HOA Fee — Homes.com](https://www.homes.com/middleton-wi/middleton-hills-neighborhood/no-hoa/)
- [About Middleton Hills — Homes.com local guide](https://www.homes.com/local-guide/middleton-wi/middleton-hills-neighborhood/) — egress-blocked, search snippet only.
- [Middleton Hills recently sold — Redfin](https://www.redfin.com/neighborhood/466930/WI/Middleton/Middleton-Hills/recently-sold) — NOT used for pricing per house rules; listed only as a boundary-map reference source.
- [Middleton-Cross Plains School District — Wikipedia](https://en.wikipedia.org/wiki/Middleton-Cross_Plains_School_District)
- [Middleton-Cross Plains Area School District — Our Schools](https://www.mcpasd.k12.wi.us/page/schools) — egress-blocked, search snippet only.
- [Northside Elementary School — GreatSchools](https://www.greatschools.org/wisconsin/middleton/1017-Northside-Elementary-School/)
- [Kromrey Middle School — SchoolDigger](https://www.schooldigger.com/go/WI/schools/0951001104/school.aspx)
- [6934 Frank Lloyd Wright Ave, Middleton, WI 53562 — Redfin listing](https://www.redfin.com/WI/Middleton/6934-Frank-Lloyd-Wright-Ave-53562/home/89970414) — single asking-price data point only, not a market statistic.
- [Pasqual's Cantina — Middleton (Toast ordering page)](https://order.toasttab.com/online/pasquals-cantina-middleton-1)
- [Pasqual's Cantina — Yelp](https://www.yelp.com/biz/pasquals-cantina-middleton)
- [Kwik Trip — 7508 Century Ave — GasBuddy](https://www.gasbuddy.com/station/12962)
- [CVS Pharmacy — 6210 Century Ave, Middleton, WI](https://www.cvs.com/store-locator/middleton-wi-pharmacies/6210-century-ave-middleton-wi-53562/storeid=5584)
- [Middleton Hills Park, North — Wanderlog](https://wanderlog.com/place/details/12745602/middleton-hills-neighborhood-park-north)
- [Middleton Hills Park — Wanderlog](https://wanderlog.com/place/details/1218231/middleton-hills-park)

**Perplexity leg sources:** none — leg not run / files not found this pass.
