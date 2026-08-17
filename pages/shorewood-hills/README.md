# Shorewood Hills — Build Notes (v1)

**File:** `shorewood-hills-v1.html`
**URL slug:** `https://integrityhomeswi.com/madison/shorewood-hills/`
**Published/Modified:** 2026-08-17
**Source:** `research/shorewood-hills-research.md` (Perplexity + Claude legs; ChatGPT leg missing, noted in the brief itself)

## Status: Tier 1 draft, publish-ready pending the items below

## Placeholders / pending items

- **IMAGE-PENDING.** No approved photo exists for Shorewood Hills. The hero uses a navy CSS gradient placeholder (no `background-image`, no invented stock photo), flagged with an HTML comment. No `og:image`/`twitter:image` tags were added for the same reason. Photo Strip section is omitted entirely per the build rules (skip rather than fill with placeholders).
- **Market Data section is fully TBD** — no sold price, median price, average price, DOM, or sales-volume figures anywhere on the page, matching the standing MLS rule. "John's Take" in that section explicitly says the numbers are pending a proper SCWMLS pull and that the ~$1.35M third-party aggregator figure in the research brief is not being used.
- **John's Notes section** is four bracketed placeholder prompts (`[ John — ... ]`), same convention as the KFW v8 template, since no actual quotes from John exist yet for this village.
- **Middle/high school assignment (Hamilton Middle / Wright lottery / Madison West High)** is presented as "reported," sourced to only one research leg, with an explicit instruction (in the Schools section, the FAQ, and a John's Notes prompt) to verify against MMSD's official attendance map before it's treated as fact for any specific address.
- **STR (short-term rental) ordinance status** — the 2023 proposal (primary-residence-only, 180-night cap) is presented as still "proposed," not adopted, per the research brief's own caveat. Flagged again as a John's Notes item to check current status.
- **Blackhawk Country Club access for residents** — presented as unconfirmed (private club, membership/access policy for village residents not verified).
- **Frautschi Point** is explicitly called out as a UW–Madison asset adjacent to the village, *not* a village park — a "commonly confused amenity" caution, directly parallel to this repo's Southbridge pool-access caution.

## Non-mechanical content decisions

1. **Population figure — omitted entirely.** The research brief flags a genuine, unresolved numeric conflict between two population estimates (2,277 people / 950 households / 625 families per the 2020 Census, vs. 2,067 people / median age 38.6 from a different, uncorroborated source) and explicitly says "do not average or pick one silently." Since there's no safe overlap between the two figures and no way to tell which year/source each represents without John's input, the page omits a population number entirely rather than averaging or guessing. It uses the uncontested, non-conflicting **660 total housing units (2020 Census)** figure instead, wherever a "how big is this village" fact was needed (stats strip, sidebar, love-grid, homes-for-sale copy).
2. **[PP]/[CL] conflict-tracking tags never appear on the public page.** All internal-only leg-attribution tags from the research brief were stripped; where the brief flags something as single-source or unconfirmed, the page instead uses plain-language hedges ("reported," "not independently confirmed," "verify before relying on this").
3. **Middle/high school assignment hedged, not stated as fact.** Because the Hamilton/Wright/West assignment was sourced to only one research leg and the second leg explicitly could not confirm it, the page presents it as "reported" rather than confirmed, in three places (Schools section stat block avoided any hard numeric school-ranking claims since none exist for this village; the school-row copy; and the FAQ), each carrying a verify-with-MMSD instruction.
4. **No builder-quoted pricing used anywhere**, including body copy. Unlike a typical Integrity Homes subdivision, Shorewood Hills has no builder or developer selling new tract product — it's a century-old, built-out village where new homes only happen via custom teardown/rebuild. The one dollar figure that exists in the research brief (~$1.35M trailing-12-month median from a third-party aggregator) is explicitly flagged in the brief as non-authoritative and was excluded from the page entirely, per the standing "no sold-price/median-price/DOM figures anywhere outside a dated builder-quoted mention" rule — and there is no builder-quoted figure to use instead.
5. **Dog Parks section omitted.** The research brief names no specific dog park near Shorewood Hills (Ripp Park and Yahara Heights are Waunakee-area facilities from the Kilkenny Farms West brief, not from this brief) — per the build instructions, the section is skipped rather than filled with unrelated or invented content.
6. **Businesses included are limited to those with a real, brief-sourced address.** Whole Foods (3313 University Ave), Metro Market/Pick 'n Save (3650 University Ave), Ancora Coffee Roasters (2871 University Ave), UW Health Clinic (2880 University Ave), and UW Health University Hospital (600 Highland Ave) all made the page. Gas stations, specific Hilldale tenants, Trader Joe's, Walgreens, and any library branch were left out — the brief either declined to name them, flagged their addresses as unconfirmed, or (Trader Joe's) explicitly warned against implying proximity that doesn't exist.
7. **Distance/drive-time figures carry explicit hedge language** where the brief itself labels them inferred or single-source (downtown Madison ~3–4 mi/10–15 min; airport ~8.6–11 mi/20–30 min) rather than presenting them as GPS-confirmed facts.
8. **Geo coordinates in the Place schema (43.078, -89.437)** are an approximate public-map estimate for the village centroid, not sourced from the research brief (the brief explicitly flags the exact legal boundary/plat map as unconfirmed and recommends pulling it from shorewoodhillswi.gov). These coordinates are for schema/mapping purposes only, are not displayed as page copy, and should be verified/replaced once John or Kenzie pulls the official village boundary map.
9. **No street address for John/Integrity Homes anywhere** — author bio and footer omit "1025 Quinn Drive," consistent with the subdivision-page address rule; only phone, email, and Real Broker affiliation are shown. The Place schema carries no `streetAddress` field (locality/region/postal/country only).

## Interlinking / Phase 5 follow-ups (not yet done — flagging per Phase 6)

- **Link DOWN (5b):** The Madison city hub page (`/madison/`) needs to be updated to list Shorewood Hills in its neighborhood directory. Not yet done — this file only builds the subdivision page itself.
- **Link SIDEWAYS (5c):** Section L of the research brief names Nakoma, Dudgeon-Monroe, University Heights, and Sunset Village as comparison neighborhoods. None are confirmed to have published Integrity Homes pages yet — track as placeholders for a later cross-link pass once/if those pages exist.
- **Link to Market Report (5d):** Page links to `https://integrityhomeswi.com/market-reports/madison-wisconsin/` — confirm this URL is live/correct before publish.
- **Blog cross-links (5e):** Not run this pass — would need the Blog Master tab cross-reference.

## Facts intentionally left out of the page

Population count (see #1 above); any sold/median/average price or DOM figure; specific gas stations; unconfirmed condo communities ("The Cove," "Marshall Court" — single-source, boundary-within-village not confirmed); Walk Score/Bike Score numbers (flagged single-source in the brief); village property tax rate (not documented by either research leg); full text of historic deed covenants (not documented); current adopted/proposed status of the STR ordinance (left as "reported proposed, verify current status").
