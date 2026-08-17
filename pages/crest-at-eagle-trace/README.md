# Crest at Eagle Trace — Page Build Notes (v1)

**File:** `crest-at-eagle-trace-v1.html`
**URL:** https://integrityhomeswi.com/middleton/crest-at-eagle-trace/
**Published / Modified:** 2026-08-17
**Source:** `research/crest-at-eagle-trace-research.md` (Claude leg only — Perplexity leg missing/failed for this subdivision; brief is single-source despite being labeled "merged")

## Status: Tier 1 draft, several open items before this is fully client-ready

This page follows the KFW v8 master template exactly (CSS, design tokens, section anatomy, `#john`/`#org` `@id`-only schema stubs). It is intentionally thinner and more hedged than Kilkenny Farms West or Southbridge because the underlying research brief is thinner — single-source, several sections explicitly marked "not confident" or blocked by network egress.

## JSON-LD

Validated with `python3 -c "json.loads(...)"` — parses cleanly. `@graph` contains WebPage, BreadcrumbList, Place, FAQPage. Person (`#john`) and Organization (`#org`) are referenced by `@id` only, never redefined, per the corrected schema standard. All 8 visible FAQ Q&A pairs were diffed programmatically against the FAQPage schema — zero mismatches.

## How the price conflict was handled

The research brief flags an **internal, unresolved conflict** in Section B/K/L: one snippet cites "$410K–$500K" for the Crest Collection, another cites "$626,300–$635,000+" that may actually belong to the *parent* Eagle Trace collection, not Crest. Per the task instructions, this conflict is **not surfaced publicly** and **not averaged/picked**:

- The only price stated anywhere on the page is the single **builder-quoted Astor Twin Home starting price ($409,900, 2bd/2.5ba, 1,403 sq ft)**, sourced from one search snippet dated August 2026, explicitly labeled "builder-quoted" and "not a sold price."
- No "price range" is claimed for the community as a whole.
- The Market Data section is **fully TBD** — including the Sale Price Range card, which stays TBD rather than substituting the builder-quoted figure (per the "no sold-price/median/DOM anywhere" rule).
- The $626K–$635K figure appears **only once**, inside John's private-sounding "Market Update" commentary block, framed explicitly as "I have not reconciled this with Crest's own pricing" — i.e., visible as an open item for John, not presented to buyers as a fact. This is the closest the page gets to surfacing the conflict, and it's framed as an internal to-do, not a public claim.
- The Quick-Answer block's price sentence uses only the single hedged Astor Twin Home figure with "current pricing unconfirmed" language, per the four-slot template's requirement that Sentence 3 never carry an unverified number as settled fact.

## Placeholder / pending items

- **Hero image:** No approved photo exists. Hero uses a navy gradient background (`linear-gradient(135deg, var(--navy) 0%, var(--navy-dark) 100%)`) with an `<!-- IMAGE-PENDING -->` HTML comment. **Photo Strip section is omitted entirely** (not filled with placeholders), per Phase 3/4 rules.
- **Dog Parks section:** Omitted entirely. The research brief names no specific dog park near this subdivision — nothing to include.
- **HOA:** Not confirmed either way (fee, management company, CC&Rs). Stated as an open item in the About section, sidebar, John's Notes, and FAQ — never assumed or invented.
- **School boundary assignment:** MCPASD is confirmed at the district level only. Pope Farm Elementary, Glacier Creek Middle School, and Middleton High School are listed explicitly as "nearest by proximity / district structure," **not** as confirmed boundary-assigned schools. A mandatory verify-by-address disclaimer is included in the Schools section, matching Kenzie SOP requirements.
- **Streets:** Only Mosaic Way is confirmed inside the Crest at Eagle Trace boundary. Tabby Turn Drive and the White Fox Lane sales-office address are flagged in-page as unconfirmed — the brief could not determine which subdivision brand (Crest vs. parent Eagle Trace) they actually belong to.
- **Nearby conveniences:** Only one business is named with a real, confirmed address — Middleton Farmers Cooperative (Cenex), 1755 Pleasantview Road. Metcalfe's Market and Kelleys Market/Middleton Mobil were explicitly excluded from the business-card grid because the brief could not confirm an exact address for either — they're mentioned only in an honesty info-box, not presented as verified nearby options. No grocery/coffee/restaurant/pharmacy/healthcare/library option could be confirmed for this specific corner of Middleton.
- **Golf course(s):** Builder marketing references "gorgeous parks and golf courses" nearby but names none — page explicitly declines to guess a course name.
- **Neighborhood-internal amenities** (pool/clubhouse/playground within the plat): neither confirmed nor denied in the brief — page states this honestly in an info-box rather than listing invented amenity rows.
- **Market Data section:** 100% TBD, exactly matching the master template's TBD pattern — this is a brand-new community with no SCWMLS sold-comp history yet, on top of the standing "MLS data comes from John, never from public sites" rule.
- **Distances/drive times:** All commute-table and stats-strip figures the brief could produce were explicitly unrouted estimates (mapping tools were blocked during research). The Proximity & Commute table labels every row "(est.)" and carries a stronger-than-usual disclaimer paragraph stating these are not routed/measured output.
- **Geo coordinates:** Place schema uses an approximate lat/long (43.099, -89.542) for Middleton's far-west Old Sauk Rd/Schewe Rd corridor — general public geography for schema purposes, not a brief-sourced fact, consistent with how the KFW template handled its own approximate Waunakee coordinates.

## Rule compliance checklist

- [x] No street address for John/Integrity Homes anywhere (no Quinn Drive) — confirmed via grep, none present.
- [x] No `streetAddress` field in Place schema — confirmed via grep, none present.
- [x] No sold-price/median-price/DOM figures anywhere; Market Data section fully TBD.
- [x] Dog Parks section omitted (no specific park named in the brief).
- [x] Photo Strip section omitted; navy gradient placeholder with IMAGE-PENDING comment used instead.
- [x] Every named business (Middleton Farmers Cooperative) has a real, brief-confirmed address; unconfirmed businesses excluded from cards.
- [x] `#john` / `#org` referenced by `@id` only, never redefined.
- [x] FAQ visible copy and FAQPage schema match word-for-word (programmatically verified).
- [x] Quick-Answer block: 90 words, four-slot template, price sentence honestly hedged.
- [x] Collision with the separate 53593 "Eagle Trace" (Verona area) called out explicitly in About copy, love-grid, and two FAQ entries — this is the single most important disambiguation on the page, mirroring the Kilkenny Farms West / Kilkenny section-of-Southbridge pattern this repo already guards against.

## Next steps for John (mirrors research brief Section O)

1. Confirm current live pricing for both Crest Collection and parent Eagle Trace directly with Veridian's sales office; resolve the $410K–$500K vs. $626K–$635K conflict.
2. Get HOA fee, management company, and CC&R info from Veridian.
3. Confirm exact plat boundary — is Tabby Turn Dr / White Fox Ln inside Crest or the parent Eagle Trace?
4. Run MCPASD's official boundary lookup tool for a Mosaic Way address to confirm actual assigned schools.
5. Name the golf course(s) referenced in builder marketing, if any.
6. Get a real SCWMLS pull once enough closed sales exist to report Market Data.
7. Confirm named grocery/coffee/restaurant/pharmacy/healthcare/library options for the Old Sauk/Schewe corner of Middleton.
8. Route actual drive times (Beltline on-ramp, downtown Middleton, MSN airport, Madison employment centers) — Proximity table is currently unrouted estimates only.
9. Re-run the Perplexity leg of research and re-merge the brief — this page was built from Claude-only, single-source research.
10. Once a Media Vault-approved photo exists, replace the navy gradient hero, add a Photo Strip section, and bump `dateModified`.

## Airtable

Record `recgayYi33H7LUSeQ` in base `appTtFjtIHkZZYtgY` / table `tbl4FXwpxRiyaPcOT` updated: status → "Drafted", drafted-by → "Claude Code".
