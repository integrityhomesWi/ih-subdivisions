# Village at Autumn Lake — Merged Research Brief

**Merge date:** 2026-08-17
**Legs retrieved:**
- Claude (WebSearch/WebFetch) — retrieved 2026-08-17 — `village-at-autumn-lake-raw-claude.md` + `village-at-autumn-lake-conveniences-claude.md`
- Perplexity — **MISSING.** Neither `village-at-autumn-lake-raw-perplexity.md` nor `village-at-autumn-lake-conveniences.md` exists in `research/`. Per Phase 1a, proceeding with the single available leg rather than blocking; this gap should be logged in the build log and the Perplexity leg re-run before this page is treated as fully sourced.

**Merge method:** Per `docs/SUBDIVISION-PAGE-BUILDER-README.md` Phase 1 union rules. With only one leg available, there is nothing to cross-check for conflicts between engines — every fact below traces to the Claude leg only, tagged **[CL]**. No **[PP]** or **[PP+CL]** tags appear in this version; re-merge and re-tag once the Perplexity leg exists. Internal conflicts *within* the Claude leg (i.e., disagreeing snippets the Claude leg itself found and flagged) are preserved as flagged conflicts below, not silently resolved.

> Sold-price, median-price, and days-on-market figures are not included — those are pending John's SCWMLS export per standing project rule. All prices below are dated builder-list prices, not sold comps.

---

## ⚠️ CRITICAL NAME/LOCATION FLAG — READ FIRST [CL]

Village at Autumn Lake carries a **Madison, WI 53718 mailing address** (City of Madison), not a Sun Prairie address, despite being requested/commonly framed as a Sun Prairie subdivision. It is bordered by **I-39/90 (west), Felland Road (east), and Lien Road (south)**, and is zoned into the **Sun Prairie Area School District** — a Madison-address/Sun Prairie-schools split repeated consistently across the developer (Veridian Homes) and third-party sources. **Do not publish content stating or implying the property address is "Sun Prairie, WI."** Frame it as "Sun Prairie schools, Madison address."

A separate, genuinely-Sun-Prairie Veridian Homes community — **The Reserve**, Sun Prairie WI 53590, west side, ~$598,100 starting price (one source) — must not be conflated with this one. See Section L.

## A. Expert Summary [CL]

Village at Autumn Lake is a Veridian Homes single-family/townhome community on the far east side of the City of Madison, Dane County, built around a man-made lake (reported as both "15-acre" and "16-acre" — unresolved conflict, see below). Mailing address is Madison, WI 53718; school district is Sun Prairie Area School District. Bounded roughly by I-39/90 (west), Felland Road (east), and Lien Road (south). Actively building as of mid-2026 — Veridian's own June 18, 2026 blog post announced new homesites released in "The Reserve & Village at Autumn Lake." Current listed floor plans span roughly 1,482–3,044 sq ft, 3–4 bed / 2–4 bath, with community-wide starting prices reported between $419,900 and $439,900 depending on source/date. Planned/built amenities include ~7 miles of walking trails, open park space, a dog park, a community garden, a playground, and a sledding hill; a Sun Prairie elementary school site was planned along the eastern edge but no source confirms it has opened. "Woods at Autumn Lake" is a newer, more premium enclave within/adjacent to the community, with larger homesites. HOA is managed by DSI Real Estate Group; reported annual dues vary $216–$325 across sources, likely reflecting different lot types and/or years rather than one uniform figure — do not present a single dues number as community-wide.

## B. Verified Quick-Facts Table

| Fact | Value | Confidence / Source note |
|---|---|---|
| Developer/builder | Veridian Homes | High [CL] |
| Mailing address / city | Madison, WI 53718 (City of Madison) | High — unanimous across sources found [CL] |
| School district | Sun Prairie Area School District | High, but a district assignment not a city-of-record fact; verify by address before publishing school claims [CL] |
| Boundaries | I-39/90 (west), Felland Rd (east), Lien Rd (south) | High [CL] |
| Lake size | "15-acre" vs. "16-acre" man-made lake | **Conflict — not resolved.** Flag for GIS/plat verification [CL] |
| Home types | Single-family homes and townhomes; 3–4 bed, 2–4 bath | High [CL] |
| Size range (current listed plans) | ~1,482–3,044 sq ft | Medium — aggregator snippet, not independently cross-checked against builder's own plan pages [CL] |
| Starting price | $419,900–$439,900 (range across sources) | Medium — builder list price, dated Aug 2026 research pass; not sold-price/MLS data [CL] |
| HOA management | DSI Real Estate Group | High [CL] |
| HOA annual dues | $216–$325/year reported across different properties/listings | Low-medium — variation likely reflects lot type and/or year; do not apply one figure to whole neighborhood [CL] |
| Related but distinct community | "The Reserve" by Veridian Homes, Sun Prairie WI 53590 (west side) — different plat/address | High — do not conflate [CL] |
| Related but distinct sub-section | "Woods at Autumn Lake" — newer, larger-homesite enclave within/adjacent to the community | Medium — developer describes as part of the same overall community; treat as a phase, not a separate subdivision [CL] |
| Related but distinct property (not part of subdivision) | "Autumn Lake Apartments," 5607 Summer Shine Dr, Madison — separate rental complex | High — flagged to prevent conflation [CL] |
| Drive time to East Towne Mall | ~3 minutes | Medium — builder marketing copy [CL] |
| Drive time to Dane County Regional Airport | ~9 minutes | Medium — builder marketing copy [CL] |
| Drive time to downtown Sun Prairie | ~11 minutes | Medium — builder marketing copy [CL] |
| Drive time to Hwy 51 | ~4 minutes | Medium — builder marketing copy [CL] |

## C. Development and Phase History [CL]

- Veridian Homes is the developer/builder of record; no other builder name appears associated with the core plat.
- City of Madison Planning Division shows an active record titled "Village at Autumn Lake Replat No. 7" (record LNDSPP-2023-00007) — implies at least seven platting actions/phases. Page content itself could not be fetched (egress blocked this pass); only title/URL retrieved via search. Needs a direct pull from City of Madison Legistar/DPCED for a real phase count and dates.
- Veridian blog post dated **June 18, 2026** confirms new homesites actively releasing in Village at Autumn Lake as of mid-2026 — best-dated confirmation of ongoing activity found.
- An October 2024 Veridian blog post ("October Phase Releases") also references phase releases in this general period, though it was not confirmed whether that post names Village at Autumn Lake specifically or a sibling community. **Flag — needs direct confirmation.**
- "Woods at Autumn Lake" is marketed by Veridian as "the newest section tucked into a serene corner of the Village at Autumn Lake" — current newest phase/enclave, more expansive homesites, more wooded character.
- No source gives a confirmed "project started in [year]" date. **Flag: founding year not independently confirmed — do not state one without verification.**

## D. Location, Streets and Boundaries [CL]

- **Municipality:** City of Madison, Dane County, WI — ZIP 53718 (not Village/City of Sun Prairie).
- **Boundaries:** I-39/90 (west); Felland Road (east); Lien Road (south).
- **Confirmed street:** Autumn Lake Parkway (also "Autumn Lake Pkwy") — the primary named street, confirmed via numerous individual listing addresses.
- **Separate property, same general area:** Autumn Lake Apartments, 5607 Summer Shine Dr, Madison WI 53718 — not part of the for-sale HOA neighborhood.
- No additional internal street names (cul-de-sacs, secondary streets) were independently confirmed. **Flag: full internal street list needs a plat-map or City GIS pull** — cityofmadison.com was egress-blocked this pass.
- **Anchor/landmark:** the 15–16-acre man-made lake at the community's center (acreage unresolved).

## E. Schools [CL]

- **District:** Sun Prairie Area School District — confirmed by every source found, despite the Madison mailing address. Single most distinctive and most easily-misstated fact about this neighborhood.
- **Elementary — CONFLICTING/UNCONFIRMED:** One Veridian planning-map PDF (title only, not fetched) references a "PROPOSED SUN PRAIRIE ELEMENTARY SCHOOL" site planned along the eastern edge — planned, not confirmed built. Separately, search snippets surfaced two different currently-serving elementary school names — **"Meadowview Elementary"** per one source and **"Creekside Elementary"** per another. **Unresolved conflict — do not state either as confirmed assignment.** Use the Sun Prairie Area School District's official address-lookup tool before publishing or advising a buyer.
- **Middle/High:** Not independently confirmed. District operates two high schools (Sun Prairie East, Sun Prairie West) — which serves this address is unconfirmed. **Flag for verification.**
- School attendance boundaries are shifting as the district grows (the "proposed elementary school" reference itself signals active capacity planning) — any specific-address school claim needs the district's current official boundary map.

## F. Homes and Housing Products [CL]

- **Product types:** Single-family detached homes and townhomes (22 "ready to build" plans referenced on one aggregator site).
- **Bed/bath:** 3–4 bedrooms, 2–4 bathrooms.
- **Size range:** ~1,482–3,044 sq ft (aggregator site, not independently cross-checked against Veridian's own plan pages).
- **Named plan example:** "The Atwood" — 2,446 sq ft, 4 bed, 3 bath, single-family; one listed example price $536,300 (single specific listing, not community-wide; date not independently confirmed).
- **Starting price:** $419,900 (one source) vs. $439,900 (another) — likely reflects different points in time or product types rather than a true conflict; date-stamp any price used.
- **Woods at Autumn Lake:** marketed as "more expansive homesites," more wooded setting — implies larger lots/higher price tier, but no specific size/price differential independently confirmed.
- No sold-price or median-price data reported — pending John's SCWMLS pull.

## G. HOA and Restrictions [CL]

- **Management company:** DSI Real Estate Group, Inc. (also manages other Veridian-area HOAs, including Heritage Hills in Waunakee per prior repo research).
- **Dues — CONFLICTING, not one number:** individual listings report $216, $217, $237, $269, and $325/year across different addresses/years — most likely reflects property type (single-family vs. townhome) and/or assessment year, not a single community-wide fee. One listing noted 2025 dues due by January 31, 2025.
- **CC&Rs / specific restrictions:** not independently retrieved this pass — DSI's hosted PDF URL was found but the site was egress-blocked. **Flag: exact CC&R restrictions, architectural review, rental restrictions, fence/exterior rules unconfirmed** — need a direct document pull before advising a buyer.
- **Contact:** DSI Real Estate Group — hoa@dsirealestate.com, (608) 226-3000 (search snippet, not independently re-verified by phone).

## H. Parks, Trails and Amenities [CL]

- **Trails:** marketing copy repeats "7 miles" of walking/hiking trails, described as pet-friendly.
- **Lake:** central man-made lake, 15 or 16 acres depending on source (unresolved conflict).
- **Dog park:** referenced in Veridian's own plans/marketing as planned/included.
- **Playground and sledding hill:** referenced in at least one source as part of the trail/park system "scattered throughout" the neighborhood.
- **Community garden:** referenced in Veridian marketing copy as part of the planned open-space program.
- **Pool: NOT confirmed for the single-family/townhome community.** The pool that appears in search results belongs specifically to Autumn Lake Apartments (5607 Summer Shine Dr) — a separate rental property. **Do not present a pool as a Village at Autumn Lake single-family-home amenity.**
- **Elementary school site:** per Section E, planned along the eastern edge — treat as planned, not a finished amenity, pending confirmation.

## I. Nearby Conveniences with Distances [CL]

**Anchored streets:** Autumn Lake Parkway (primary internal street); bounded by I-39/90 (west), Felland Road (east), Lien Road (south). Mailing address Madison, WI 53718; Sun Prairie Area School District.

**Methodology note:** No direct WebFetch access to business-listing or mapping sites this pass — distances/times below are drawn from WebSearch snippets (largely builder marketing copy) rather than an independently-run mapping tool. **John should spot-check drive times below in Google Maps from an actual Autumn Lake Parkway address before publishing.**

- **Route to downtown Sun Prairie:** ~11 minutes per builder copy (consistent figure). No specific route confirmed — a plausible inferred route runs east on Lien Rd/Felland Rd toward Sun Prairie's western approaches (WI-19 corridor), but this is inference, not confirmed. **Flag: verify actual route/mileage.**
- **Nearest highway on-ramp:** I-39/90 is the immediate western boundary; nearest on-ramp likely the Lien Road or Milwaukee Street/County Hwy AB interchange area, but the specific interchange name/number is not independently confirmed. **Flag for confirmation.** Separately, ~4 minutes to Hwy 51 (US 51) per builder copy.
- **East Towne Mall / East Washington Ave corridor:** ~3 minutes per builder copy — likely reflects the immediate shopping center, not the full East Washington Ave employment corridor; confirm before use.
- **Downtown Madison / State Capitol employment core:** not independently found. Given the neighborhood's position off I-39/90 on Madison's far east side, a reasonable planning estimate is 15–20 minutes via I-39/90 and John Nolen Dr or East Washington Ave — **estimate only, not confirmed, do not publish as-is.**
- **East-side business/tech corridors (American Center, Sprecher Rd area):** not independently confirmed; Felland Rd/I-39/90 position suggests reasonable proximity but no specific drive time found.
- **Dane County Regional Airport (MSN):** ~9 minutes per builder copy — plausible given the airport's position near I-39/90/Hwy 30, but not independently re-verified via mapping tool.
- **Named, currently-operating businesses:** very few specific, individually-named, currently-operating businesses near this exact address were independently confirmed. Search results returned mostly generic city-wide directory pages (Yelp results for "Costco Madison," "Kwik Trip Madison," etc.) rather than confirmation of a specific nearest location.
  - **Grocery:** no specific nearest store confirmed. East Towne Mall area is a reasonable candidate zone to check, but no store name confirmed. **Flag: needs direct verification.**
  - **Gas/convenience:** Kwik Trip confirmed to operate numerous Madison-area locations (having acquired former PDQ locations), but no specific nearest address confirmed. **Flag: needs direct verification.**
  - **Coffee, restaurants, pharmacy/healthcare:** not independently confirmed beyond generic "close to dining" marketing language.
  - **Library:** not confirmed. Sun Prairie Public Library and Madison Public Library's Sequoya or Pinney branches are geographically plausible candidates given the school-district/city split, but none confirmed as nearest — do not name one without verification.
  - **Parks (beyond the neighborhood's own internal system):** no specific named nearby public park independently confirmed.
  - **East Towne Mall:** the one specific, confirmed, currently-operating named destination found — a major regional shopping center on Madison's east side, ~3 minutes away per consistent builder marketing copy.

**Discarded due to name collision or non-confirmation:**
- Autumn Lake Apartments (5607 Summer Shine Dr) — separate rental complex with its own pool, clubhouse, fitness center, dog wash/grooming spa; shares the "Autumn Lake" name but is not this HOA neighborhood. Retained as a flagged distinction, not fully discarded.
- The Reserve (Veridian Homes, Sun Prairie WI 53590) — separate, genuinely-Sun-Prairie community; discarded as a source for this neighborhood's facts but retained in Section L as a legitimate comparison point.
- Generic "Autumn Lake" hits for other US states/cities — not encountered directly this session, but flagged as a standing risk given how common the name is nationally; future passes should keep confirming "Madison, WI 53718" / "Sun Prairie Area School District" in-page before citing a source.
- Yelp/generic Madison-wide business directory results — discarded as too generic to confirm actual proximity to Autumn Lake Parkway.

## J. What Residents Value [CL]

- Not independently confirmed from first-person resident sources this pass — a Nextdoor community page for this neighborhood exists (URL found) but is egress-blocked; WebSearch snippets returned only generic "community discussion, dining and activities" summaries with no specific quoted resident sentiment.
- Marketing copy consistently emphasizes lake views, trail network, and "peaceful, family-friendly" positioning — this is developer framing, not verified resident sentiment, and should be labeled as such if used.
- **Gap — not confident:** this section needs first-person input (Nextdoor, Facebook group, or direct buyer/resident interviews) that this research pass could not access. Left as a gap per Phase 1 rules, not filled with a guess.

## K. Possible Considerations [CL]

- **I-39/90 proximity (western boundary):** a major interstate forming the immediate western edge is worth flagging as a possible noise/traffic consideration for buyers on that side — not independently confirmed as a complaint, but a reasonable, address-relevant consideration.
- **Ongoing construction:** given the June 2026 "new homesites released" post and the "Replat No. 7" record, the neighborhood appears to still be actively building out. Buyers should expect ongoing construction traffic/dust in newer sections (including Woods at Autumn Lake). **Confirm current build-out status/remaining lot count directly with Veridian's sales office before publishing an "almost complete" or "still building" characterization.**
- **School attendance boundary uncertainty:** given the conflicting elementary-school names (Section E) and the planned-but-unconfirmed on-site school, this is a real point of buyer confusion — resolve with the district directly before any address-specific school claim.
- **Madison address / Sun Prairie schools split:** worth calling out proactively in buyer-facing content so there's no surprise about mailing address vs. taxing/voting jurisdiction vs. school district.

## L. Comparison With Nearby Subdivisions [CL]

- **The Reserve (Veridian Homes, Sun Prairie WI 53590):** a genuinely separate, genuinely-Sun-Prairie community by the same builder, west side of Sun Prairie. Reported starting price ~$598,100 (one source) — notably higher than Village at Autumn Lake's ~$419,900–$439,900, suggesting a different price tier/lot size product. **Do not conflate — different plat, address, ZIP, price point.** Both referenced together in Veridian's June 2026 post, likely the source of any confusion.
- **Woods at Autumn Lake:** treated by the developer as a section/phase within the broader community rather than a fully separate subdivision — worth naming distinctly in any lot-size/price-tier comparison.
- **Heritage Hills (Waunakee) and Kilkenny Farms West/Southbridge (Waunakee):** no direct evidence connects these to Village at Autumn Lake; noted only because they share the same builder (Veridian) and/or HOA manager (DSI) pattern seen elsewhere in this repo's prior research — a cross-reference for John's broader content library, not a claim of neighborhood similarity.

## M. Frequently Asked Questions [CL]

- **Is Village at Autumn Lake in Sun Prairie or Madison?** Mailing address is Madison, WI 53718 (City of Madison); zoned into the Sun Prairie Area School District. Two different facts — verify which matters for the buyer's question (municipal services/taxes = Madison; schools = Sun Prairie).
- **What school will my kids attend?** Unconfirmed/conflicting this pass (Section E) — check address-by-address on the district's official attendance-area tool.
- **Is there a pool?** Not confirmed for the for-sale neighborhood. A pool exists at the separate Autumn Lake Apartments rental complex — do not present as a neighborhood-wide amenity.
- **What are the HOA dues?** Reported figures vary ($216–$325/year) likely by lot/property type and year — get the exact current figure from DSI Real Estate Group or the seller's HOA disclosure.
- **Is the neighborhood still under construction?** As of the most recent dated source found (June 2026), yes — new homesites were still being released.

## N. "Only a Local Would Know" Content Ideas [CL]

1. The "Madison address but Sun Prairie schools" split — a genuinely distinctive, explainable fact most out-of-town buyers wouldn't guess; a natural short-form video hook.
2. The difference between Village at Autumn Lake (for-sale homes) and Autumn Lake Apartments (separate rental complex with the pool) — a real point of buyer confusion worth clarifying on camera.
3. The difference between Village at Autumn Lake and The Reserve — same builder, both near Sun Prairie, very different price points.
4. Woods at Autumn Lake as the "premium newer section" within the larger community.
5. I-39/90 forming the literal western property line — practical commute-time content.
6. The planned-but-unconfirmed on-site elementary school — a "here's what's coming" video once confirmed, or a "here's what to ask" caution video now.
7. Drive-time framing already used in builder marketing (3 min to East Towne Mall, 9 min to airport, 11 min to downtown Sun Prairie, 4 min to Hwy 51) — verify each and use as a quick-hit commute reel.
8. The lake itself — man-made, central to design, walking-trail loop around it — good b-roll once acreage is confirmed one way or the other.
9. The "Replat No. 7" City of Madison planning record — evidence of a long, multi-phase build-out.
10. HOA-dues variability by lot/property type — a genuinely useful "ask this specific question" tip for buyers.
11. Multiple Veridian-built, DSI-managed communities across the Madison/Sun Prairie/Waunakee area (this one, The Reserve, Heritage Hills) — a possible cross-sell content series, once each is independently verified.

## O. Missing Information John Should Verify

1. Exact lake acreage (15 vs. 16 acres — direct conflict, unresolved). [CL]
2. Current elementary school assignment — "Meadowview" vs. "Creekside" conflict, plus whether the planned on-site elementary school has actually opened. [CL]
3. Middle school and high school assignment — not found at all this pass. [CL]
4. Full internal street list — only Autumn Lake Parkway confirmed; needs a City of Madison plat map or GIS pull. [CL]
5. Current, single-source HOA dues figure and what it covers (lawn care? snow removal? amenity access?) — get from DSI directly or a current listing's HOA disclosure. [CL]
6. Actual CC&R restrictions (rentals, fences, parking, architectural review) — DSI's PDF exists by URL but wasn't retrievable this pass. [CL]
7. Total number of platted lots/phases to date and remaining inventory — "Replat No. 7" implies significant phasing but no total count found. [CL]
8. Whether the planned elementary school, dog park, community garden, playground, and sledding hill are actually built and open today, versus still-planned. [CL]
9. Confirm the City of Madison record (LNDSPP-2023-00007) directly — only the page title was visible via search, not content. [CL]
10. Direct resident sentiment (Nextdoor, Facebook groups, buyer interviews) — no first-person source access this pass. [CL]
11. **The entire Perplexity leg** — not run or its output files are missing from `research/`. Re-run per Phase 1a before treating this brief as fully union-merged; any facts Perplexity alone would surface are not yet captured here.

## P. Sources (Direct Links) [CL]

- [Village at Autumn Lake, Madison Homes for Rent — Homes.com](https://www.homes.com/madison-wi/village-at-autumn-lake-neighborhood/homes-for-rent/)
- [Village at Autumn Lake in Madison, WI — Veridian Homes (NewHomeSource)](https://www.newhomesource.com/basiccommunity/community-117427/village-at-autumn-lake-madison-wi-53718)
- [Village at Autumn Lake by Veridian Homes in Madison WI — Zillow](https://www.zillow.com/community/village-at-autumn-lake/25562_plid/)
- [Village at Autumn Lake Replat No. 7 — City of Madison DPCED Planning](https://www.cityofmadison.com/dpced/planning/development.cfm?record=LNDSPP-2023-00007)
- [Village at Autumn Lake — Veridian Homes neighborhood page](https://veridianhomes.com/find/neighborhoods/region/madison/village-at-autumn-lake/)
- [Village at Autumn Lake Real Estate — Mad City Dream Homes](https://www.madcitydreamhomes.com/village-at-autumn-lake.php)
- [Autumn Lake Apartments — Apartments.com (separate rental property, not the HOA neighborhood)](https://www.apartments.com/autumn-lake-apartments-madison-wi/dl0srpj/)
- [Village At Autumn Lake, Madison, WI — Stark Company Realtors](https://www.starkhomes.com/s/wi/madison-city/village-at-autumn-lake-subdivision)
- [Village at Autumn Lake, Madison — Nextdoor neighborhood page](https://nextdoor.com/neighborhood/villageatautumnlakewi--madison--wi/)
- [Woods at Autumn Lake — Veridian Homes neighborhood page](https://veridianhomes.com/find/neighborhoods/region/madison/the-woods-at-autumn-lake/)
- [Village at Autumn Lake — DSI Real Estate Group HOA page](https://www.dsirealestate.com/hoa/village-at-autumn-lake/)
- [VILLAGE at AUTUMN LAKE — DSI Real Estate Group PDF](https://www.dsirealestate.com/wp-content/uploads/2021/01/Village-at-Autumn-Lake.pdf)
- [Proposed Sun Prairie Elementary School / Autumn Lake community dog park — Veridian Homes planning PDF](https://files.veridianhomes.com/2cdbe863e568a0730ea99bc594203620-8822villageatautumnlakepm_11194pageweb.pdf)
- [New Homesites Available in The Reserve & Village at Autumn Lake — Veridian Homes blog, June 18, 2026](https://veridianhomes.com/blog/2026/06/18/new-homesites-available-in-the-reserve-village-at-autumn-lake/)
- [The Reserve by Veridian Homes, Sun Prairie, WI — Redfin community page](https://www.redfin.com/WI/Sun-Prairie/The-Reserve/community/23777125)
- [The Reserve by Veridian Homes in Sun Prairie WI — Zillow](https://www.zillow.com/community/reserve/30985244_plid/)
- [Sun Prairie Area School District — School Attendance Areas (official boundary tool)](https://www.sunprairieschools.org/district/enrolling-students/school-attendance-areas)
- [Sun Prairie Area School District Elementary School Attendance Zones — ZipDataMaps](https://www.zipdatamaps.com/schools/wisconsin/district/map-of-sun-prairie-area-school-district-wi-elementary-school-attendance-zones)
- [Sun Prairie School District Boundaries — SCWMLS PDF](https://scwmls.com/pdf/SunPrairie.pdf)
- [Sun Prairie West High School — Wikipedia](https://en.wikipedia.org/wiki/Sun_Prairie_West_High_School)
- [Sun Prairie East High School — Wikipedia](https://en.wikipedia.org/wiki/Sun_Prairie_East_High_School)
- [The Atwood — Village at Autumn Lake — Trulia plan page](https://www.trulia.com/builder-community/Village-At-Autumn-Lake-6000207250/new-home/Plan-The-Atwood/4063484318)
- [October Phase Releases — Veridian Homes blog, October 2024](https://veridianhomes.com/blog/2024/10/01/october-phase-releases-2/)
</content>
