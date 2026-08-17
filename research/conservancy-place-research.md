# Conservancy Place — DeForest, WI — Merged Research Brief

**Merge date:** 2026-08-17
**Claude leg (raw + conveniences) retrieved:** 2026-08-17
**Perplexity leg (raw + conveniences):** **MISSING — files not found.** `conservancy-place-raw-perplexity.md` and `conservancy-place-conveniences.md` do not exist in `research/`. This merge is single-source (Claude leg only). Per Phase 1a rule ("if one engine fails or times out, proceed with the other[s] and note the gap"), this brief proceeds on Claude only — **the union-of-coverage benefit does not apply here since there is only one leg to union.** Re-run the Perplexity leg and re-merge before treating this as complete; until then, every fact below carries single-source risk that a second leg might have caught (a conflict Perplexity would have surfaced, a fact only Perplexity's sources reached, etc.).

**Source tagging:** every fact below is tagged **[CL]** (Claude leg). No **[PP]** or **[PP+CL]** tags appear in this version because there is no Perplexity data to merge. When the Perplexity leg is run, re-tag accordingly and add any **[PP]**-only findings and flag any genuine **[PP] vs [CL] conflicts**.

**Underlying caveat carried over from the raw file:** most primary sites (Redfin, Zillow, Movoto, neighborhoods.com, joshlavik.com, starkhomes.com, conservancyplace.com, madcitydreamhomes.com) returned `EGRESS_BLOCKED` when fetched directly — the Claude leg relied on WebSearch snippet text, not full-page verification. Nothing here should be treated as final without a second source.

---

## A. Expert Summary

Conservancy Place is a large (~640–650 acre — see conflict note in Section B) [CL], master-planned mixed-use community in the Village of DeForest, Dane County, WI, developed by Park Towne Development Corp. [CL] It runs along roughly 3.5 miles of the Yahara River / Upper Yahara River Environmental Corridor [CL]. It is **not** a single small subdivision — it's an umbrella development containing multiple named neighborhoods/plats (Woods Glen, The Knolls, Hawthorn Point, Rivers Turn, plus commercial/mixed-use components called Innovation Springs and The Promenade) [CL]. Housing type varies by sub-neighborhood: single-family detached homes in some plats, condos/townhomes in others (e.g., "The Meadows at Conservancy Place" by Veridian Homes) [CL]. Building started in 2003 and construction is described as ongoing as of the most recent listings found [CL]. This is structurally analogous to the Southbridge situation flagged in this repo's CLAUDE.md — Conservancy Place is an umbrella name, and it is **not confident** all sub-neighborhoods share the same HOA, price point, or amenities [CL]. Treat every fact below as needing confirmation against the specific street/plat before use in a cut sheet or client conversation.

## B. Verified Quick-Facts Table

| Fact | Value | Confidence | Source |
|---|---|---|---|
| Municipality | Village of DeForest, Dane County, WI | High | [CL] |
| Developer | Park Towne Development Corp. (Madison, WI; principals historically Gerald Ring, Gerard Dohm, John DeBeck) | Medium — from search snippets, not primary site fetch | [CL] |
| Development size | "650-acre community" (one source) vs. "640-acre" (another source) | **CONFLICT (within Claude leg's own sources) — not resolved.** Do not state a single acreage without checking conservancyplace.com directly | [CL] |
| River frontage | ~3.5 miles along the Yahara River / Upper Yahara River Environmental Corridor | Medium | [CL] |
| Construction start | 2003 | Medium | [CL] |
| Construction status | Still actively building as of most recent listings (e.g., Meadows at Conservancy Place quick-move-in homes) | Medium | [CL] |
| Named sub-neighborhoods/plats | Woods Glen, The Knolls, Hawthorn Point, Rivers Turn (residential); Innovation Springs (office/research); The Promenade (retail/residential/office) | Medium — one source said "six neighborhoods" including Promenade, another said "five separate plats" excluding Promenade — **CONFLICT (within Claude leg), not resolved** | [CL] |
| Condo component | "The Meadows at Conservancy Place" by Veridian Homes — 3–4 bed, 3 bath, 1,482–2,416 sq ft, homes advertised "starting at $336,500" | Medium; builder asking/starting price, dated to whenever that listing snapshot was crawled — time-sensitive | [CL] |
| Primary internal street | Conservancy Plaza (aka "Conservancy Plz") | High — confirmed via multiple MLS/listing sources showing addresses (6542, 6701, 6706, 6717, 6803 Conservancy Plaza) | [CL] |
| Other internal streets (unverified) | Stonecrop Way, Bluestem Trail, Larkspur Lane, Yellowwood Lane, Woods Glen Court | Low–Medium — Yellowwood Lane confirmed (park address); others from a single AI-generated search summary, need independent confirmation | [CL] |
| Village park in the development | Conservancy Commons Park, 6822 Yellowwood Lane, DeForest WI 53532 | High — confirmed via deforestwi.gov facility page | [CL] |
| School district | DeForest Area School District | High | [CL] |
| Sold prices / median price / DOM | **Not researched — pending MLS data from John** (rule: no Redfin/Zillow/Trulia sold-price stats) | N/A | N/A |

## C. Development and Phase History

- Park Towne Development Corp. has developed real estate in south-central Wisconsin for 40+ years, beginning with the Parkwood Hills neighborhood on Madison's west side in the 1960s — from a search snippet, not independently verified against parktowne.com directly (fetch blocked). [CL]
- Conservancy Place construction reportedly began in 2003, sited along the Yahara River corridor. [CL]
- Multiple named phases/plats exist: **Woods Glen**, **The Knolls**, **Hawthorn Point**, **Rivers Turn** are residential; **Innovation Springs** is office/research; **The Promenade** is retail/residential/office (mixed-use, possibly not yet built out — treat as *planned* unless confirmed built). [CL]
- A "Rivers Turn at Conservancy Place Final Development Plan" PDF (dated June 2017, adopted) exists on the Village of DeForest's file server — suggests Rivers Turn was still in active platting/approval as of 2017, a **later phase** than the original 2003 build-out. Verify exact phase timeline. [CL]
- **FLAG:** conflicting acreage (640 vs. 650) and conflicting neighborhood count (five plats vs. six including Promenade) — not resolved. John should check conservancyplace.com's "About Us" page directly (blocked from this leg) or the Village of DeForest planning department. [CL]
- Condo/townhome product "The Meadows at Conservancy Place" is built by **Veridian Homes**, a different builder than Park Towne itself appears to build directly — suggests Park Towne functions as master developer/land developer, with production builders (Veridian and possibly others) building out individual plats. Not confident this is the only builder active. [CL]

## D. Location, Streets, and Boundaries

- Confirmed street: **Conservancy Plaza** (also written "Conservancy Plz") — spine street, house numbers observed in the 6500s–6800s range (6542, 6701, 6706, 6717, 6803 Conservancy Plaza). [CL]
- Confirmed street: **Yellowwood Lane** — home to Conservancy Commons Park at 6822 Yellowwood Lane. [CL]
- Confirmed street: **Woods Glen Court** — within the Woods Glen plat (e.g., 822 Woods Glen Court, DeForest WI 53532). [CL]
- Unconfirmed/low-confidence streets from a single AI search summary only (Stonecrop Way, Bluestem Trail, Larkspur Lane) — **do not use in a cut sheet without independent confirmation**, per repo rule against inventing/assuming facts. [CL]
- Overall development is sited along the Yahara River / Upper Yahara River Environmental Corridor within Village of DeForest limits, Dane County. Zip: 53532. [CL]
- **Not confident** on exact outer boundary streets — not found in this pass. Verify with a plat map or Village of DeForest GIS. [CL]

## E. Schools

- District: **DeForest Area School District** (deforest.k12.wi.us) — confirmed, high confidence. [CL]
- District elementary schools: **Eagle Point Elementary** (206 N Johnson St, DeForest WI), **Windsor Elementary**, and **Yahara Elementary** (234 N Lexington Pkwy, DeForest WI). [CL]
- One older marketing source states Conservancy Place residents are assigned to **Yahara Elementary**, DeForest Area Middle School, and DeForest Area High School, "only 10 minutes" from the community. [CL]
- **CAUTION — verify-by-address required.** DeForest Area SD has three elementary schools, and boundaries commonly split even within one subdivision, especially one this large (640+ acres, multiple plats). The Yahara Elementary assignment is from a single marketing source and should **not** be presented as guaranteed for every address — a home near Rivers Turn (platted 2017) could plausibly be zoned differently than a home in the original Woods Glen/Knolls sections. Verify per-address against the district's official boundary map before telling any client which elementary school they'll attend. [CL]
- Middle school: DeForest Area Middle School (district has only one — low-risk). High school: DeForest Area High School (same, only one HS — low-risk). [CL]

## F. Homes and Housing Products (no sold-price stats)

- Housing mix varies by plat: single-family detached is the primary product in Woods Glen, The Knolls, Hawthorn Point, and Rivers Turn; condos/townhomes are found in "The Meadows at Conservancy Place" (Veridian Homes). [CL]
- The Meadows at Conservancy Place (Veridian Homes): 3–4 bed, 3 bath, 1,482–2,416 sq ft; builder-advertised starting price ~$336,500 as of the source snapshot (undated precisely — reconfirm before quoting). [CL]
- General description across sources: "variety of housing options, including single-family homes and condominiums in various architectural styles." [CL]
- No sold-price, median-price, or days-on-market data included per instructions — pending MLS pull from John.
- Not confident on total unit count, lot sizes, or full builder roster (only Veridian confirmed). [CL]

## G. HOA and Restrictions

- **Not confident on a development-wide HOA fee.** Multiple sub-communities referenced (e.g., "The Meadows at Conservancy Place" condo association, managed per a DSI Real Estate CC&R/HOA management page) strongly suggest **HOA structure and fees differ by plat/product type** — consistent with this repo's warning not to apply one section's HOA fee to a whole neighborhood. [CL]
- No specific dollar HOA fee amount confirmed for any plat in this pass. [CL]
- Park Towne's general contact info (for HOA/CC&R inquiries) found via a business directory listing: 402 Gammon Place, Suite 300, Madison, WI 53719, (608) 833-9044 — **not independently verified as current**, single business-directory snippet. [CL]
- CC&Rs for The Meadows at Conservancy Place are referenced as managed via dsirealestate.com — suggests at least the condo section has a formal HOA/management company. Single-family plats' HOA status not confirmed either way. [CL]
- **John should verify:** one master HOA plus sub-associations, or fully separate HOAs per plat — and pull actual current fee amounts.

## H. Parks, Trails, and Amenities

- **Conservancy Commons Park** — confirmed Village of DeForest public park at 6822 Yellowwood Lane. Amenities per the Village's facility page: ADA-accessible areas, bike trail, football field, pavilion, picnic areas/shelters, restrooms, splash pad, tables, trails, water facilities. Open 7:00 AM–10:00 PM daily; splash pad hours 10:00 AM–8:00 PM (seasonal). Contact: Greg Hall, 608-846-6751. [CL]
- **Note:** one search result title read "Conservancy Commons Park — Closed for 2026" and another referenced a "Park Improvement Concepts – Next Steps Announced" village newsflash, plus mention of a splash-pad/layout refresh being planned. Do **not** tell a client the splash pad is definitely open without checking the current Village of DeForest facilities page. [CL]
- Yahara River corridor: biking, hiking, paddling access described as a development amenity. [CL]
- Small parks/green spaces described generally ("array of small parks and green spaces") but not itemized by name beyond Conservancy Commons Park. [CL]
- **Do not present a pool or clubhouse as a completed amenity** — no source in this leg confirmed a private pool/clubhouse for Conservancy Place; the "DeForest Area School District pool" reference is a *school district* facility (Performing Arts Center/pool complex), not a subdivision amenity — do not conflate. [CL]

## I. Nearby Conveniences with Distances (named businesses only)

*(Merged in from `conservancy-place-conveniences-claude.md`; no Perplexity conveniences file exists to merge against.)*

**Anchored streets:** Conservancy Plaza (spine street, ~6500s–6800s), Yellowwood Lane (park at 6822), Woods Glen Court. All distances below are estimated from the Conservancy Place development generally (zip 53532) rather than a single confirmed address, since most primary listing/business sites could not be fetched directly — treat as approximate until confirmed with a mapping tool from the actual anchor address. [CL]

- **Grocery — not confidently confirmed.** "Festival Foods" and "Piggly Wiggly" referenced generally for DeForest, but no verified in-DeForest street address found for either (closest confirmed Piggly Wiggly was in Waunakee, not DeForest). Verify current DeForest grocery options before publishing. [CL]
- **Gas/Convenience:** Kwik Trip — 4848 Co Rd V, DeForest, WI 53532, (608) 842-3446, open 24 hours (medium confidence, truck-stop directory aggregator, not Kwik Trip's own site). A second possible Kwik Trip/travel center at 7372 N Towne Rd (US-51) — not cross-verified as distinct from the above; confirm before use. [CL]
- **Coffee — not found** with a confirmed named business and address. Do not guess. [CL]
- **Pharmacy/Healthcare:** Walgreens Pharmacy — 807 S Main St, DeForest, WI 53532, (608) 846-3671 (medium-high confidence, multiple consistent sources). CVS referenced in nearby communities (e.g., Sun Prairie) but **not confirmed in DeForest itself** — do not state a DeForest CVS exists. De Forest Clinic (Dr. Scott Miller, MD) — 815 S Main St, DeForest, WI 53532, (608) 846-4787, walk-in/urgent-care-style primary care (medium confidence). No confirmed hospital within DeForest itself — nearest almost certainly Madison (UW Health/SSM Health/UnityPoint Health–Meriter), but **not verified** in this pass. [CL]
- **Library:** DeForest Area Public Library — 203 Library Street, DeForest, WI 53532 (South Central Library System). High confidence. [CL]
- **Parks/Recreation:** Conservancy Commons Park, 6822 Yellowwood Lane — inside the development itself (see Section H). [CL]
- **Schools (distance purposes only):** Yahara Elementary — 234 N Lexington Pkwy; Eagle Point Elementary — 206 N Johnson St; Windsor Elementary — location not confirmed. Do not assign a specific elementary school to a specific address without checking the district's boundary map (see Section E). [CL]
- **Route to downtown DeForest:** marketing copy consistently ~10 minutes. Not independently verified with a live drive-time tool; date of original marketing copy unknown, resurfaced 2026-08-17. [CL]
- **Nearest highway on-ramp:** DeForest sits directly at the I-39/90/94 & US-51 interchange (Exit 132), a six-ramp parclo interchange just north of Dane County Regional Airport — nearest interstate access for the Village generally, including Conservancy Place. Exact drive time from the Conservancy Plaza/Yellowwood Lane anchor streets to the on-ramp not independently measured — estimate a few minutes given DeForest's compact footprint, confirm before publishing a specific number. [CL]
- **Drive time to Madison employment centers:** marketing copy states ~30 minutes to downtown Madison via interstate — a developer/marketing estimate, not independently verified. Will vary significantly by time of day (isthmus congestion at rush hour) and destination (downtown/Capitol Square vs. West Towne/university area vs. American Center/east side, notably closer than downtown). Re-verify with a live mapping tool for the specific employment center. [CL]
- **Drive time to Dane County Regional Airport (MSN):** one source says ~10 minutes south of DeForest; another frames airport-to-downtown-Madison as 20–25 minutes — **these measure different legs, do not conflate.** From Conservancy Place specifically, expect roughly 10–15 minutes via I-39/90/94, but not independently measured from the actual anchor address. Confirm before publishing a specific number. [CL]

## J. What Residents Value

Based on marketing language and repeated themes across sources (not resident-sourced — directional only, not verified sentiment): [CL]
- River/nature access — biking, hiking, paddling along the Yahara River corridor.
- "Rolling terrain and expansive permanent open space" — a stated differentiator from flatter subdivisions.
- Mixed housing choice within one large development (single-family vs. condo/townhome) without leaving the "neighborhood."
- Proximity to downtown DeForest and quick interstate access to Madison.
- School district reputation (DeForest Area School District) — not independently verified sentiment, but commonly cited by Dane County exurban buyers generally.

## K. Possible Considerations

- **Size and complexity:** because Conservancy Place is a large, multi-plat, mixed-use master development (not a single small subdivision), buyers should not assume amenities, HOA fees, or even school assignment are uniform across the whole development — the single biggest "don't conflate" risk here, structurally similar to the Southbridge situation flagged in CLAUDE.md. [CL]
- **Ongoing construction:** building described as still active as of the most recent listings found — potential for continued construction noise/traffic in newer phases (e.g., Rivers Turn, platted as recently as 2017) even as older phases (Woods Glen, The Knolls) are fully built out. [CL]
- **Mixed-use proximity:** Innovation Springs (office/research) and The Promenade (retail/office/residential) mean some residential areas may be closer to commercial/office development than a purely residential subdivision — could be a plus (walkability) or a minus (traffic/noise) depending on exact lot location. [CL]
- **Park status uncertainty:** Conservancy Commons Park shows signs of renovation/seasonal-closure messaging for 2026 — verify current status before promising splash pad access. [CL]
- School boundary uncertainty flagged in Section E. [CL]

## L. Comparison With Nearby Subdivisions

Not deeply researched in this pass (out of scope beyond a brief flag) — DeForest has other named subdivisions/developments (e.g., areas off Vinburn Road, Sandhill, etc.) that were not investigated. **Do not assume any comparison points without separate research** — none is offered here to avoid guessing. Request a dedicated comparison pass if needed. [CL]

## M. Frequently Asked Questions

*(Compiled from what the research surfaced as likely buyer questions — answers only given where sourced; otherwise marked unconfirmed.)* [CL]

1. **Is Conservancy Place one subdivision or several?** It's a large master-planned development containing several named plats (Woods Glen, The Knolls, Hawthorn Point, Rivers Turn) plus mixed-use components. Not a single uniform subdivision.
2. **What school will my kids attend?** DeForest Area School District for certain; specific elementary (Eagle Point, Windsor, or Yahara) depends on exact address — verify, don't assume Yahara for every address.
3. **Is there an HOA?** At least the condo section (The Meadows) has a homeowners/condo association; single-family plat HOA status and fees not confirmed — verify per plat.
4. **Is there a pool or clubhouse?** Not confirmed. Do not promise one.
5. **What park serves the neighborhood?** Conservancy Commons Park (6822 Yellowwood Lane) — verify current 2026 operating status before citing splash pad hours.
6. **How far to Madison?** Roughly 30 minutes via interstate per marketing copy — not independently verified with a live drive-time tool.
7. **How far to downtown DeForest?** Roughly 10 minutes per marketing copy.
8. **Who is the developer?** Park Towne Development Corp.
9. **When was it built?** Construction started 2003; still ongoing in newer phases as of the most recent listings surfaced.
10. **Are there condos as well as single-family homes?** Yes — The Meadows at Conservancy Place (Veridian Homes) is a condo/townhome product within the larger development.

## N. "Only a Local Would Know" Content Ideas (10+)

1. The distinction between Conservancy Place's several named plats (Woods Glen vs. The Knolls vs. Hawthorn Point vs. Rivers Turn) — most out-of-town buyers won't realize it's not one subdivision. [CL]
2. Which specific elementary school (Eagle Point, Windsor, or Yahara) actually serves which street — a genuinely useful, locally-verified data point once confirmed. [CL]
3. The Yahara River paddling/biking access point(s) specific to Conservancy Place — exact trailhead location. [CL]
4. Current (2026) status of Conservancy Commons Park's splash pad renovation — whether it's open, and the new layout once finalized. [CL]
5. Which builder(s) are actively building in which plat right now (Veridian confirmed for Meadows; others unconfirmed) — useful for new-construction buyers. [CL]
6. Whether Rivers Turn (platted 2017) has different lot sizes/pricing than the original 2003-era Woods Glen/Knolls sections. [CL]
7. The Innovation Springs office/research component — what's actually been built there vs. still planned, and whether it affects any residential streets' character. [CL]
8. The Promenade mixed-use component — same question: built or still planned? [CL]
9. Practical rush-hour drive time from Conservancy Place to the I-39/90/94 & US-51 interchange vs. marketing-copy "30 minutes to Madison." [CL]
10. Which churches, if any, are actually within walking distance (marketing copy says "churches ... a stone's throw" — name them). [CL]
11. Whether HOA dues differ meaningfully between the condo section and single-family sections — a real financial planning detail for buyers. [CL]
12. History angle: Park Towne's 40+ year local track record starting with Parkwood Hills — a "why this developer" trust point for content. [CL]

## O. Missing Information John Should Verify

- **Run the missing Perplexity leg** (`conservancy-place-raw-perplexity.md`, `conservancy-place-conveniences.md`) and re-merge — this brief is currently single-source.
- Exact, current acreage (650 vs. 640 — conflicting sources within the Claude leg alone).
- Exact count and full list of named plats/neighborhoods (5 vs. 6 — conflicting sources), and whether Innovation Springs / The Promenade are built, under construction, or still only planned.
- Full, complete street list for the development (only Conservancy Plaza, Yellowwood Lane, and Woods Glen Court confirmed).
- Whether there is a master HOA plus sub-associations, or fully separate HOAs — and current fee amounts for each.
- Elementary school boundary lines within the development — confirm per street/plat, do not assume uniform Yahara Elementary assignment.
- Current (2026) status/hours of Conservancy Commons Park, given renovation signals in search results.
- Whether a pool, clubhouse, or other private resident amenity exists anywhere in the development (none confirmed; likely does not exist, but not 100% ruled out).
- Sold-price, median-price, and days-on-market data — pull from MLS.
- Builder roster beyond Veridian Homes.
- Current Park Towne Development Corp. contact info (address/phone found via a single business-directory snippet only; parktowne.com and conservancyplace.com could not be fetched directly).
- Grocery, coffee shop, and named-church options in DeForest — none confidently confirmed in Section I.
- Confirm the second possible Kwik Trip location (7372 N Towne Rd) is distinct from the Co Rd V location, not a duplicate listing.

## P. Sources with Direct Links

*(All from the Claude leg — no Perplexity source list exists to merge.)*

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
- Redfin, Zillow, Trulia, Movoto listing pages seen in search results for street/address confirmation only (e.g., confirming "Conservancy Plaza" as a real street) — **not used for any sold-price, median-price, or DOM statistic**, per instructions.

---

**Discarded due to name collision:**
- No businesses/places discarded for a Conservancy Place / DeForest, WI collision specifically. Note for the record: "Conservancy Place" is a generic-sounding real-estate name pattern likely reused in other US metros; no cross-state/cross-metro results were mistakenly included — all retained sources explicitly referenced DeForest, WI 53532, Dane County, and/or the Village of DeForest.
- "Charleston Parks Conservancy" (Charleston, SC) surfaced twice due to the word "Conservancy" — correctly excluded (different state, different entity type — nonprofit parks org, not a residential subdivision).
- A "Conservatory HOA" result (note: **Conservatory**, not **Conservancy**) surfaced once during HOA research — correctly excluded as a different-named entity.
