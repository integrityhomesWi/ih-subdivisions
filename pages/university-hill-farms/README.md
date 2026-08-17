# University Hill Farms (Madison) — Page Build Notes

**File:** `university-hill-farms-v1.html`
**Source of facts:** `research/university-hill-farms-research.md` only (Claude leg — Perplexity leg missing/failed for this subdivision, per the brief's own header note).
**JSON-LD:** validated with `python3 -c "json.loads(...)"` — parses clean, 4 `@graph` nodes (WebPage, BreadcrumbList, Place, FAQPage), `author`/`publisher` referenced as `#john`/`#org` @id-only stubs, no redefinition.

## Placeholders / pending items

- **IMAGE-PENDING** — no approved photo exists. Hero uses a navy CSS gradient (`linear-gradient(160deg, var(--navy), var(--navy-dark))`) with an HTML comment flagging it. Photo Strip section is omitted entirely (not filled with placeholders), per rule.
- **Market Data section** — fully TBD, including the "Sale Price Range" card (unlike Kilkenny Farms West, this is a resale-only neighborhood with no builder pricing to fall back on, so every market-stats card is TBD, not just the derived ones). Marked "Pending MLS Data from John."
- **John's Notes (Insider Notes)** — left as bracketed prompts for John, retargeted to the brief's actual open questions: current association dues ($10 vs. $20 conflict), the Frank Lloyd Wright house's address, how much the Madison Yards construction is disrupting daily life, and how Hill Farms compares to Westmorland/Nakoma/Regent (brief explicitly says no comparison data was pulled).
- **Dog Parks section — omitted entirely.** The brief names no dog park confirmed near this subdivision (unlike Kilkenny Farms West's Ripp Park / Yahara Heights), so the section anatomy item was dropped rather than padded.
- **Pharmacy / named restaurant tenants** — the brief found no confirmed pharmacy or individually-named Hilldale restaurant/coffee tenants, so none are named on the page; the Dining & Shopping info-box says so explicitly and points to `hilldale.com/directory` instead.
- **Capitol Petrol Mart** (6702 Mineral Point Rd) — the brief flagged this single-source gas station as needing verification that it's still operating. Left out of the page entirely rather than published unconfirmed.

## Non-mechanical content decisions

- **The dues conflict ($10 vs. $20/household) and the acreage conflict (600 vs. 487 acres) are internal single-leg conflicts, not the `[PP]`/`[CL]` cross-engine conflicts the build rules are primarily written for** (there is no Perplexity leg to conflict with — the brief is explicit about this). Per the "no averaging, no silent pick" rule, I treated these the same way: the dues conflict is stated as a range with both figures given and a link to verify (not averaged to "$15," not silently resolved to one number) in the About sidebar, the Why-People-Choose-It grid is silent on the exact number, and the FAQ/schema answer states both figures. The acreage conflict (600 ac. Wikipedia vs. 487 ac. aggregator) has **no safe overlap and isn't load-bearing for the page's argument**, so I omitted the acreage claim entirely rather than publish either figure or a range.
- **No FAQ/body text names the Frank Lloyd Wright house's address** — the brief is explicit that the address wasn't confirmed. The page acknowledges the house exists (multiple sources) but treats the address as an open question in both the FAQ and John's Notes.
- **Niche school rankings omitted** — the brief flags these (Van Hise #10, Hamilton #5, West High #3, all "A") as a single-source aggregator claim "not independently corroborated." Rather than present them in a stat-box grid (which visually implies the same certainty as Kilkenny Farms West's officially-sourced #7/#1/13:1/95.9% district stats), I dropped the numeric ranking claims from the Schools section entirely and kept only the confirmed district/school-name facts.
- **Madison Yards at Hill Farms build-out** — the page states only what the brief calls confirmed-open (the state office tower, the Whole Foods) and explicitly flags the larger proposed retail/hotel/housing scope as an earlier master-plan projection, per the brief's own caveat.
- **Stats strip** uses "1950s," "2015," "MMSD," and "~3–4 mi to Capitol Square (est.)" instead of a price-range/build-era pair like Kilkenny Farms West — there's no builder price or build-era range to quote for a resale-only 70-year-old neighborhood, so the four most distinctive *confirmed* facts were substituted instead of forcing the template's original stat categories.
- **Quick-Answer block** hedges the price sentence honestly instead of quoting a number: "It's resale-only, with no active builder and no published price range — MLS-sourced sold-price data is pending" — this replaces the four-slot template's usual sourced price range, since none exists yet for this subdivision, per the brief's explicit "no sold data" instruction. 85 words, within the 60–90 target.
- **Author bio and footer** — no office street address anywhere (no "Quinn Drive"), per the standing subdivision-page address rule. Footer keeps phone, email, "Waunakee-based," Real Broker affiliation, and MLS disclaimer link only.
- **Comparison-with-nearby-subdivisions (research Section L)** — the brief says this is out of scope for a single-leg pass with no comparison data pulled. No comparison table/section was added to the page; John's Notes Observation 4 flags it as an open question for him to answer from firsthand knowledge instead.

## Follow-ups for a later pass

- Re-run/merge the Perplexity leg for this subdivision once that API key works — this brief is single-leg coverage.
- Once John supplies an SCWMLS export for University Hill Farms, fill in the Market Data section and John's Take, then bump `dateModified`.
- Once a real photo is approved, replace the hero gradient placeholder and photo-strip omission, and bump `dateModified` (freshness trigger per Phase 7c).
- City hub page `/madison/` needs to be updated to link down to this new page (Phase 5b) — not done as part of this build.
