# Ardent Glen — Verona, WI — Build Notes

**File:** `ardent-glen-v1.html`
**Source:** `research/ardent-glen-research.md` (Claude-only leg; Perplexity leg missing — see below)
**Built:** 2026-08-17

## Status: Tier 1 publish-ready, with real gaps flagged on-page

## Placeholders / pending items

- **IMAGE-PENDING.** No approved Ardent Glen photo exists. The hero uses a navy CSS gradient placeholder (matches the template's design tokens), flagged with an HTML comment in the `<section class="hero">` block. The Photo Strip section is skipped entirely per instructions, not filled with a placeholder image.
- **Market Data section is fully TBD.** Every stat card (median price, avg price, DOM, list-to-sale ratio, etc.) reads `TBD`, "Reporting Period: Pending SCWMLS Pull." No sold-price, median-price, or DOM figures appear anywhere on the page. Builder-quoted pricing is mentioned only in body copy (About sidebar, Quick Answer, John's Take), always dated August 2026 and labeled as pending/builder-quoted — never presented as a settled number.
- **Dog Parks section omitted.** The research brief names Badger Prairie County Park as having a dog park, but explicitly flags that its distance from Ardent Glen "has not been independently verified" and is only "cited in builder marketing." That's short of "a specific dog park actually near this subdivision" with confirmed proximity, so per instructions the dedicated Dog Parks section was left out. Badger Prairie is still mentioned, hedged, inside Parks & Recreation.
- **Schools section has no confirmed per-school assignment.** The brief explicitly states the specific VASD elementary/middle/high school for Ardent Glen addresses was not confirmed. Rather than naming a school, each grade-band row says "Not Yet Confirmed" and lists the district's building options generically, with a hard verify-by-address disclaimer (VASD boundary tool + Registration Office contact) — matching the Kenzie SOP rule against guaranteeing school assignments.
- **Dining & Shopping is thin by design.** Only Kwik Trip (2145 County Rd PB, Verona) has a confirmed street address in the brief. Festival Foods, Caffe Depot, and downtown Verona restaurants (Gus's Diner, Paddy Mac's, Riley Tavern) are named in the brief but without confirmed addresses/distances, so they're mentioned only in a hedged info-box, not given their own business cards, per the "every named business needs a real address" rule.
- **HOA fee treated as unverified.** The ~$32/month figure appears only with its Homes.com-aggregator caveat, both in the FAQ/schema and in John's Notes prompts — never stated as a settled fact.
- **John's Notes section is all bracketed prompts** — no fabricated insider quotes. Topics: current phase/lot status, HOA fee verification, the Ardent Glen/Whispering Coves distinction, and the single-family vs. twin-home decision.
- **Geo coordinates are an estimate**, not sourced from the research brief (which had no lat/long). Flagged with an HTML comment above the JSON-LD script. Approximate location for the McKee Road / Shady Oak Lane corridor on Verona's west side.
- **Perplexity research leg never ran** for this subdivision — the brief is Claude-only. Per Phase 1 rules this should be re-run and re-merged; nothing on this page should be treated as cross-verified across two engines yet.

## Non-mechanical content decisions

- **Home size range conflict — handled by omission.** The research brief flags an unresolved conflict *within the single available leg* itself: Veridian's own page says "1,500–2,500 finished sq ft," a third-party aggregator says "1,480–3,459 sq ft." Per the critical rules, this wasn't averaged or arbitrarily picked — home square footage doesn't appear anywhere on the public page at all. No safe overlap existed to state (the ranges only partially overlap and the brief itself says the discrepancy may reflect different product types or plan-set vintages), so the safest honest choice was to leave the claim out entirely rather than surface the source conflict to a public-facing reader.
- **Whispering Coves distinction promoted to its own FAQ.** The brief explicitly parallels this to the Kilkenny Farms West / Kilkenny Farms confusion this content system already guards against, so it got the same treatment: a dedicated "Is Ardent Glen the same as Whispering Coves?" FAQ (in both visible copy and FAQPage schema).
- **"Why People Choose It" reframed as hedged, not resident-sourced.** Section J of the brief is explicit that these are inferred appeal points, not survey data. The section lead line says so directly, and no fabricated resident quote or sentiment appears anywhere on the page (unlike the Kilkenny Farms West template, which this page otherwise mirrors structurally).
- **All commute/distance figures carry an "estimate, not GPS-measured" caveat** in the table and its footer note, mirroring the brief's own repeated caution that Section I's distances are estimated, not independently measured.
- **Author bio trimmed for accuracy.** The Kilkenny Farms West template's bio references "1025 Quinn Drive — in the village" and specific Waunakee/Kilkenny builder relationships; both were removed/adjusted here — no street address anywhere (per the standing subdivision-page address rule), and the builder-relationship line was narrowed to Veridian Homes only (the brief doesn't establish a relationship with Acker Builder for this neighborhood).
- **ROH section's Truax Field distance line was dropped** rather than reused from the KFW template, since the brief has no confirmed Ardent Glen-to-Truax-Field distance.

## Not yet done (flagged for follow-up, per Phase 5/6)

- City hub page `/verona/` needs to link back down to this page (Phase 5b) — not actioned as part of this build.
- Sideways links to Whispering Coves and Hawks Landing (Section L comparisons) are name-only for now — neither has a published Integrity Homes page yet, so no link target exists. Track for a later interlinking pass once/if those pages are built.
- Quarterly SCWMLS pull needed to populate the Market Data section and the Quick Answer price sentence (Phase 7c).
