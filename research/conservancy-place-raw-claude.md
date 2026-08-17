# Conservancy Place — DeForest, WI

**Research leg:** Claude (WebSearch/WebFetch)
**Retrieved:** 2026-08-17

**Note:** This is raw single-source (Claude-leg) output, produced primarily from search-result snippets — most primary real estate sites (Redfin, Zillow, Movoto, neighborhoods.com, joshlavik.com, starkhomes.com, conservancyplace.com, madcitydreamhomes.com) returned `EGRESS_BLOCKED` when fetched directly, so claims below rely on WebSearch snippet text, not full-page verification. This file is meant to be merged with the Perplexity leg and cross-checked before anything goes client-facing. Do not treat any figure here as final without a second source.

---

## A. Expert Summary

Conservancy Place is a large (~640–650 acre — see conflict note in Section B), master-planned mixed-use community in the Village of DeForest, Dane County, WI, developed by Park Towne Development Corp. It runs along roughly 3.5 miles of the Yahara River / Upper Yahara River Environmental Corridor. It is NOT a single small subdivision — it's an umbrella development containing multiple named neighborhoods/plats (Woods Glen, The Knolls, Hawthorn Point, Rivers Turn, plus commercial/mixed-use components called Innovation Springs and The Promenade). Housing type varies by sub-neighborhood: single-family detached homes in some plats, condos/townhomes in others (e.g., "The Meadows at Conservancy Place" by Veridian Homes). Building started in 2003 and construction is described as ongoing as of the most recent listings found. This is analogous to the Southbridge situation flagged in this repo's CLAUDE.md — Conservancy Place is an umbrella name, not confident all sub-neighborhoods share the same HOA, price point, or amenities. Treat every fact below as needing to be confirmed against the specific street/plat before use in a cut sheet or client conversation.

## B. Verified Quick-Facts Table

| Fact | Value | Confidence | Source date |
|---|---|---|---|
| Municipality | Village of DeForest, Dane County, WI | High | retrieved 2026-08-17 |
| Developer | Park Towne Development Corp. (Madison, WI; principals historically Gerald Ring, Gerard Dohm, John DeBeck) | Medium — from search snippets, not primary site fetch | retrieved 2026-08-17 |
| Development size | "650-acre community" (one source) vs. "640-acre" (another source) | **CONFLICT — not resolved.** Do not state a single acreage without checking conservancyplace.com directly | retrieved 2026-08-17 |
| River frontage | ~3.5 miles along the Yahara River / Upper Yahara River Environmental Corridor | Medium | retrieved 2026-08-17 |
| Construction start | 2003 | Medium | retrieved 2026-08-17 |
| Construction status | Still actively building as of most recent listings (e.g., Meadows at Conservancy Place quick-move-in homes) | Medium | retrieved 2026-08-17 |
| Named sub-neighborhoods/plats | Woods Glen, The Knolls, Hawthorn Point, Rivers Turn (residential); Innovation Springs (office/research); The Promenade (retail/residential/office) | Medium — one source said "six neighborhoods" including Promenade, another said "five separate plats" excluding Promenade — **CONFLICT, not resolved** | retrieved 2026-08-17 |
| Condo component | "The Meadows at Conservancy Place" by Veridian Homes — 3-4 bed, 3 bath, 1,482–2,416 sq ft, homes advertised "starting at $336,500" | Medium; price is a builder asking/starting price, dated to whenever that listing snapshot was crawled (not verified live) — **not a sold-price stat, but still flag as time-sensitive** | retrieved 2026-08-17 |
| Primary internal street | Conservancy Plaza (aka "Conservancy Plz") | High — confirmed via multiple MLS/listing sources showing addresses (6542, 6701, 6706, 6717, 6803 Conservancy Plaza) | retrieved 2026-08-17 |
| Other internal streets (unverified) | Stonecrop Way, Bluestem Trail, Larkspur Lane, Yellowwood Lane, Woods Glen Court | Low-Medium — Yellowwood Lane confirmed (park address); others from a single AI-generated search summary, need independent confirmation | retrieved 2026-08-17 |
| Village park in the development | Conservancy Commons Park, 6822 Yellowwood Lane, DeForest WI 53532 | High — confirmed via deforestwi.gov facility page | retrieved 2026-08-17 |
| School district | DeForest Area School District | High | retrieved 2026-08-17 |
| Sold prices / median price / DOM | **Not researched — pending MLS data from John** (rule: no Redfin/Zillow/Trulia sold-price stats) | N/A | N/A |

## C. Development and Phase History

- Park Towne Development Corp. has developed real estate in south-central Wisconsin for 40+ years, beginning with the Parkwood Hills neighborhood on Madison's west side in the 1960s (per a Park Towne company-history search snippet — not independently verified against parktowne.com directly, as fetch was blocked).
- Conservancy Place construction reportedly began in 2003, sited along the Yahara River corridor.
- Multiple named phases/plats exist within the overall development: **Woods Glen**, **The Knolls**, **Hawthorn Point**, **Rivers Turn** are residential; **Innovation Springs** is described as office/research; **The Promenade** is described as retail/residential/office (mixed-use, possibly not yet built out — treat as a *planned* component unless confirmed built).
- A "Rivers Turn at Conservancy Place Final Development Plan" PDF (dated June 2017, adopted) exists on the Village of DeForest's engagement file server — this suggests Rivers Turn was still in active platting/approval as of 2017, i.e., a **later phase** than the original 2003 build-out. This should be verified for exact phase timeline.
- **FLAG:** conflicting acreage (640 vs. 650) and conflicting neighborhood count (five plats vs. six neighborhoods including Promenade) — not resolved in this pass. John should check conservancyplace.com's "About Us" page directly (blocked from this research leg) or the Village of DeForest planning department.
- Condo/townhome product "The Meadows at Conservancy Place" is built by **Veridian Homes**, a different builder than Park Towne itself appears to build directly — suggests Park Towne functions as master developer/land developer, with production builders (Veridian and possibly others) building out individual plats. Not confident this is the only builder active in the development.

## D. Location, Streets, and Boundaries

- Confirmed street: **Conservancy Plaza** (also written "Conservancy Plz" in postal/MLS systems) — the spine street, with house numbers observed in the 6500s–6800s range (6542, 6701, 6706, 6717, 6803 Conservancy Plaza).
- Confirmed street: **Yellowwood Lane** — home to Conservancy Commons Park at 6822 Yellowwood Lane.
- Confirmed street: **Woods Glen Court** — within the Woods Glen plat (e.g., 822 Woods Glen Court, DeForest WI 53532).
- Unconfirmed/low-confidence streets surfaced in one AI search summary only (Stonecrop Way, Bluestem Trail, Larkspur Lane) — **do not use these in a cut sheet without independent confirmation**, per repo rule against inventing/assuming filenames or facts.
- Overall development is sited along the Yahara River / Upper Yahara River Environmental Corridor within Village of DeForest limits, Dane County.
- Zip code: 53532 (DeForest).
- **Not confident** on exact outer boundary streets (what borders the development on each side) — not found in this pass. John should verify with a plat map or the Village of DeForest GIS.

## E. Schools

- District: **DeForest Area School District** (deforest.k12.wi.us) — confirmed, high confidence.
- District elementary schools: **Eagle Point Elementary** (206 N Johnson St, DeForest WI), **Windsor Elementary**, and **Yahara Elementary** (234 N Lexington Pkwy, DeForest WI).
- One older marketing source states Conservancy Place residents are assigned to **Yahara Elementary**, DeForest Area Middle School, and DeForest Area High School, "only 10 minutes" from the community.
- **CAUTION — verify-by-address required.** DeForest Area School District has three elementary schools (Eagle Point, Windsor, Yahara), and elementary boundaries commonly split even within one subdivision, especially one as large as Conservancy Place (640+ acres, multiple plats). The Yahara Elementary assignment above is from a single marketing source and should NOT be presented as guaranteed for every address in Conservancy Place — a homebuyer on the far side of the development (e.g., near Rivers Turn, platted 2017) could plausibly be zoned differently than a home in the original Woods Glen/Knolls sections. **John should verify per-address using the district's official boundary map before telling any client which elementary school they'll attend.**
- Middle school: DeForest Area Middle School (unconfirmed exact assignment, but district only has one middle school district-wide, so this is low-risk).
- High school: DeForest Area High School (same — only one HS in the district, low-risk).

## F. Homes and Housing Products (no sold-price stats)

- Housing mix varies by plat: single-family detached homes are the primary product in Woods Glen, The Knolls, Hawthorn Point, and Rivers Turn; condominiums/townhomes are found in "The Meadows at Conservancy Place" (built by Veridian Homes).
- The Meadows at Conservancy Place (Veridian Homes) product specs found: 3–4 bed, 3 bath, 1,482–2,416 sq ft floor plans; builder-advertised starting price around $336,500 as of the source snapshot (undated precisely — flag as time-sensitive, reconfirm before quoting).
- General description across sources: "variety of housing options, including single-family homes and condominiums in various architectural styles."
- **No sold-price, median-price, or days-on-market data included per instructions** — that data is pending MLS pull from John, and Redfin/Zillow/Trulia were explicitly excluded as sources for those figures.
- Not confident on total unit count, lot sizes, or the full builder roster (only Veridian Homes confirmed; Park Towne itself and/or other builders may also be active — not verified).

## G. HOA and Restrictions

- **Not confident on a development-wide HOA fee.** Multiple sub-communities were referenced (e.g., "The Meadows at Conservancy Place" condo association, managed per a DSI Real Estate CC&R/HOA management page), which strongly suggests **HOA structure and fees differ by plat/product type** (condo vs. single-family) — consistent with this repo's explicit warning not to apply one section's HOA fee to a whole neighborhood.
- No specific dollar HOA fee amount was confirmed in this pass for any plat.
- Park Towne's general contact info (for HOA/CC&R inquiries) found via a business directory listing: 402 Gammon Place, Suite 300, Madison, WI 53719, (608) 833-9044 — **not independently verified as current**, sourced from a single business directory search snippet.
- CC&Rs for The Meadows at Conservancy Place are referenced as managed via a property-management portal (dsirealestate.com) — suggests at least the condo section has a formal HOA/management company. Single-family plats' HOA status not confirmed either way.
- **John should verify:** whether there is one master HOA for the whole Conservancy Place development plus sub-associations per plat, or fully separate HOAs per plat, and pull actual current fee amounts.

## H. Parks, Trails, and Amenities

- **Conservancy Commons Park** — confirmed Village of DeForest public park at 6822 Yellowwood Lane, DeForest, WI 53532. Amenities per the Village's facility page: ADA-accessible areas, bike trail, football field, pavilion, picnic areas/shelters, restrooms, splash pad, tables, trails, water facilities. Open 7:00 AM–10:00 PM daily; splash pad hours 10:00 AM–8:00 PM (seasonal). Contact listed: Greg Hall, 608-846-6751.
- **Note:** one search result title read "Conservancy Commons Park — Closed for 2026" and another referenced a "Park Improvement Concepts – Next Steps Announced" village newsflash, plus mention of a splash-pad/layout refresh being planned. This suggests the park may be under renovation or have seasonal closures in 2026 — **do not tell a client the splash pad is definitely open without checking the current Village of DeForest facilities page**, since this park is described elsewhere as still being developed/refreshed by the Village.
- Yahara River corridor: biking, hiking, and paddling access described as a development amenity (river frontage, trail connections).
- Small parks/green spaces are described generally ("array of small parks and green spaces") but not itemized by name beyond Conservancy Commons Park.
- **Do not present a pool or clubhouse as a completed Conservancy Place amenity** — no source in this pass confirmed a private pool/clubhouse for Conservancy Place; district-level references to "DeForest Area School District pool" are a *school district* facility (Performing Arts Center / pool complex), not a subdivision amenity, and should not be conflated.

## I. Nearby Conveniences with Distances (named businesses only)

See Part 2 file (`conservancy-place-conveniences-claude.md`) for full detail. Brief summary: retail outlets, churches, and restaurants are described generically as "just a stone's throw" from the neighborhood; downtown DeForest is described as roughly 10 minutes from the community; downtown Madison roughly 30 minutes via the interstate.

## J. What Residents Value

Based on marketing language and repeated themes across sources (not resident-sourced, so treat as directional only, not verified sentiment):
- River/nature access — biking, hiking, paddling along the Yahara River corridor.
- "Rolling terrain and expansive permanent open space" — a stated differentiator from flatter subdivisions.
- Mixed housing choice within one large development (single-family vs. condo/townhome) without leaving the "neighborhood."
- Proximity to downtown DeForest and quick interstate access to Madison.
- School district reputation (DeForest Area School District) — not independently verified sentiment, but commonly cited by Dane County exurban buyers generally.

## K. Possible Considerations

- **Size and complexity**: because Conservancy Place is a large, multi-plat, mixed-use master development (not a single small subdivision), buyers should not assume amenities, HOA fees, or even school assignment are uniform across the whole development — this is the single biggest "don't conflate" risk here, structurally similar to the Southbridge situation flagged in CLAUDE.md.
- **Ongoing construction**: sources describe building as still active as of the most recent listings found — potential for continued construction noise/traffic in newer phases (e.g., Rivers Turn, platted as recently as 2017) even as older phases (Woods Glen, The Knolls) are fully built out.
- **Mixed-use proximity**: Innovation Springs (office/research) and The Promenade (retail/office/residential) components mean some residential areas may be closer to commercial/office development than a purely residential subdivision — could be a plus (walkability) or a minus (traffic/noise) depending on exact lot location.
- **Park status uncertainty**: Conservancy Commons Park shows signs of renovation/seasonal-closure messaging for 2026 — verify current status before promising splash pad access.
- School boundary uncertainty flagged in Section E.

## L. Comparison With Nearby Subdivisions

Not deeply researched in this pass (out of scope beyond a brief comparison note) — but worth flagging: DeForest has other named subdivisions/developments (e.g., areas off Vinburn Road, Sandhill, etc.) that were not investigated here. **Do not assume any comparison points without separate research** — none is offered here to avoid guessing. John should request a dedicated comparison pass if needed.

## M. Frequently Asked Questions

*(Compiled from what the research surfaced as likely buyer questions — answers only given where sourced; otherwise marked unconfirmed.)*

1. **Is Conservancy Place one subdivision or several?** It's a large master-planned development containing several named plats (Woods Glen, The Knolls, Hawthorn Point, Rivers Turn) plus mixed-use components. Not a single uniform subdivision.
2. **What school will my kids attend?** DeForest Area School District for certain; specific elementary (Eagle Point, Windsor, or Yahara) depends on exact address — verify, don't assume Yahara for every address.
3. **Is there an HOA?** At least the condo section (The Meadows) has a homeowners/condo association; single-family plat HOA status and fees not confirmed — verify per plat.
4. **Is there a pool or clubhouse?** Not confirmed. Do not promise one.
5. **What park serves the neighborhood?** Conservancy Commons Park (6822 Yellowwood Lane) — verify current 2026 operating status before citing splash pad hours.
6. **How far to Madison?** Roughly 30 minutes via interstate per marketing copy — not independently verified with a live drive-time tool in this pass.
7. **How far to downtown DeForest?** Roughly 10 minutes per marketing copy.
8. **Who is the developer?** Park Towne Development Corp.
9. **When was it built?** Construction started 2003; still ongoing in newer phases as of the most recent listings surfaced.
10. **Are there condos as well as single-family homes?** Yes — The Meadows at Conservancy Place (Veridian Homes) is a condo/townhome product within the larger development.

## N. "Only a Local Would Know" Content Ideas (10+)

1. The distinction between Conservancy Place's several named plats (Woods Glen vs. The Knolls vs. Hawthorn Point vs. Rivers Turn) — most out-of-town buyers won't realize it's not one subdivision.
2. Which specific elementary school (Eagle Point, Windsor, or Yahara) actually serves which street — a genuinely useful, locally-verified data point once John confirms it.
3. The Yahara River paddling/biking access point(s) specific to Conservancy Place — exact trailhead location.
4. Current (2026) status of Conservancy Commons Park's splash pad renovation — whether it's open, and the new layout once finalized.
5. Which builder(s) are actively building in which plat right now (Veridian confirmed for Meadows; others unconfirmed) — useful for buyers wanting new construction.
6. Whether Rivers Turn (platted 2017) has different lot sizes/pricing than the original 2003-era Woods Glen/Knolls sections.
7. The Innovation Springs office/research component — what's actually been built there vs. still planned, and whether it affects any residential streets' character.
8. The Promenade mixed-use component — same question: built or still planned?
9. Practical rush-hour drive time from Conservancy Place to the I-39/90/94 & US-51 interchange vs. marketing-copy "30 minutes to Madison."
10. Which churches, if any, are actually within walking distance (marketing copy says "churches ... a stone's throw" — name them).
11. Whether HOA dues differ meaningfully between the condo section and single-family sections — a real financial planning detail for buyers.
12. History angle: Park Towne's 40+ year local track record starting with Parkwood Hills — a "why this developer" trust point for content.

## O. Missing Information John Should Verify

- Exact, current acreage (650 vs. 640 — conflicting sources).
- Exact count and full list of named plats/neighborhoods (5 vs. 6 — conflicting sources), and whether Innovation Springs / The Promenade are built, under construction, or still only planned.
- Full, complete street list for the development (only Conservancy Plaza, Yellowwood Lane, and Woods Glen Court are confirmed here).
- Whether there is a master HOA plus sub-associations, or fully separate HOAs — and current fee amounts for each.
- Elementary school boundary lines within the development — confirm per street/plat, do not assume uniform Yahara Elementary assignment.
- Current (2026) status/hours of Conservancy Commons Park, given renovation signals in search results.
- Whether a pool, clubhouse, or other private resident amenity exists anywhere in the development (none confirmed; likely does not exist, but not 100% ruled out).
- Sold-price, median-price, and days-on-market data — intentionally excluded here; pull from MLS.
- Builder roster beyond Veridian Homes.
- Current Park Towne Development Corp. contact info (address/phone found via a single business-directory snippet, not verified against a primary source since parktowne.com and conservancyplace.com could not be fetched directly in this pass).

## P. Sources with Direct Links

- [Conservancy Place - A Park Towne Development | Facebook](https://www.facebook.com/ConservancyPlace/)
- [Conservancy Place | Building Community, Respecting Nature (conservancyplace.com)](https://conservancyplace.com/) — could not be fetched directly (egress blocked); relied on search snippets only
- [Conservancy Place | About Us](https://conservancyplace.com/about-us/) — same limitation
- [Park Towne | Residential Property](https://parktowne.com/residential-property/) — could not be fetched directly
- [Park Towne | Rivers Turn](https://parktowne.com/commercial-property-2-2/rivers-turn-deforest-wi/)
- [Conservancy Place Site Development – Vierbicher](https://www.vierbicher.com/portfolio/conservancy-place-site-development/)
- [Conservancy Place - A Park Towne Development (DeForest Area Chamber business directory)](https://business.deforestarea.com/list/member/conservancy-place-a-park-towne-development-105) — could not be fetched directly
- [neighborhoods.com — Conservancy Place, DeForest, WI](https://www.neighborhoods.com/conservancy-place-deforest-wi) — could not be fetched directly
- [madcitydreamhomes.com — Conservancy Place](https://www.madcitydreamhomes.com/conservancy-place.php) — could not be fetched directly
- [Movoto — Conservancy Place, DeForest](https://www.movoto.com/deforest-wi/conservancy-place/)
- [Movoto — Woods Glen at Conservancy Place](https://www.movoto.com/deforest-wi/woods-glen-at-conservancy-place/)
- [Stark Company Realtors — Conservancy Place subdivision](https://www.starkhomes.com/s/wi/deforest-city/conservancy-place-subdivision) — could not be fetched directly
- [joshlavik.com — Conservancy Place homes](https://www.joshlavik.com/deforest/conservancy-place/) — could not be fetched directly
- [Rivers Turn at Conservancy Place Final Development Plan (PDF, Village of DeForest, adopted June 2017)](https://hdp-us-prod-app-deforest-engage-files.s3.us-west-2.amazonaws.com/3017/0992/8954/Rivers_Turn_FDP_June_2017_adopted_-_compressed.pdf)
- [Mapcarta — The Knolls at Conservancy Place](https://mapcarta.com/N5302784040)
- [The Meadows at Conservancy Place — Trulia builder community listing](https://www.trulia.com/builder-community/The-Meadows-At-Conservancy-Place-6000246140)
- [The Meadows at Conservancy Place — NewHomeSource (Veridian Homes)](https://www.newhomesource.com/community/wi/deforest/the-meadows-at-conservancy-place-by-veridian-homes/128517)
- [DSI Real Estate — The Meadows at Conservancy Place CC&Rs/HOA management](https://www.dsirealestate.com/condo-hoa/acc/neighborhoods-ccrs/b2ef88b68f2c00161896acc364719388-8948meadowsatconservancyplacepm_1220web/)
- [Conservancy Commons Park — Village of DeForest facility page](https://www.deforestwi.gov/facilities/facility/details/Conservancy-Commons-Park-1)
- [Conservancy Commons Park — CivicPlus mirror](https://wi-deforest.civicplus.com/Facilities/Facility/Details/Conservancy-Commons-Park-1)
- [Park Improvement Concepts – Next Steps Announced (Village of DeForest newsflash)](https://www.deforestwi.gov/m/newsflash/Home/Detail/64)
- [DeForest Area School District — official site](https://www.deforest.k12.wi.us/)
- [DeForest Area School District — Yahara Elementary](https://www.deforest.k12.wi.us/schools/yahara/)
- [DeForest Area School District — Eagle Point Elementary](https://www.deforest.k12.wi.us/schools/eagle-point/about/)
- [DeForest Area School District — Wikipedia](https://en.wikipedia.org/wiki/DeForest_Area_School_District)
- [ZipDataMaps — DeForest Area SD Elementary School Attendance Zones map](https://www.zipdatamaps.com/schools/wisconsin/district/map-of-deforest-area-school-district-wi-elementary-school-attendance-zones)
- [Village of DeForest — Market Access page](https://www.vi.deforest.wi.us/217/Market-Access)
- [Village of DeForest — Life in DeForest](https://www.vi.deforest.wi.us/216/Life-in-DeForest)
- Redfin, Zillow, Trulia, Movoto listing pages were seen in search results for street/address confirmation only (e.g., confirming "Conservancy Plaza" as a real street) — **not used for any sold-price, median-price, or DOM statistic**, per instructions.

---

**Discarded due to name collision:** none in the main brief — see Part 2 file for the dedicated discard log.
