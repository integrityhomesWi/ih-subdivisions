# Royal Oaks (Sun Prairie, WI) — Build Notes

**File:** `royal-oaks-v1.html`
**Source of truth used:** `research/royal-oaks-research.md` only. No outside knowledge was used.
**Status:** Tier 1 publish-ready build, JSON-LD validated with `python -m json.loads`.

## Why this page reads more hedged than Kilkenny Farms West

The research brief for Royal Oaks is **single-source** — the Perplexity leg never
ran (files missing), so every fact in the brief carries a `[CL]` (Claude-only)
tag and is explicitly flagged as "not cross-engine-verified." That single-source
status, plus the neighborhood itself being an informal, decades-old area name
rather than a platted/HOA-governed subdivision, means several standard
sections have less certainty than a page like Kilkenny Farms West. This was
treated as a content constraint, not something to paper over — see the
hedging choices below.

## Placeholder / pending items

- **Hero image:** No approved photo exists for Royal Oaks. The hero uses a
  navy CSS gradient (`linear-gradient(135deg, var(--navy-dark)...)`) in place
  of a background photo, marked `IMAGE-PENDING` in an HTML comment. `og:image`
  / `twitter:image` were omitted from `<head>` rather than pointed at a stock
  or placeholder image.
- **Photo Strip section:** Skipped entirely, per the rule that it only
  appears when 2+ real approved photos exist.
- **Dog Parks section:** Skipped entirely. The research brief names no
  specific dog park as near Royal Oaks (unlike Kilkenny Farms West, which has
  two confirmed nearby options) — inventing one would violate the "no
  invented amenities" rule, so the section was omitted rather than padded.
- **Market Data section:** Fully TBD, matching the template exactly.
  Reporting period reads "Pending SCWMLS Pull" instead of a dated trailing-12
  window, since John has not yet supplied an SCWMLS export for this
  neighborhood. No Redfin/Zillow/Trulia-derived figure was substituted
  anywhere on the page (see below).
- **John's Notes (Insider Notes) section:** Left as bracketed prompts for
  John, same pattern as the master template's own unfinished observations —
  no Phase 1 Part 3 (Facebook/Nextdoor/HOA-newsletter) human-intel pass was
  run for this build, so no personal anecdote or resident quote was invented
  to fill the section.
- **School district stat strip (ranking, student-teacher ratio, graduation
  rate):** Omitted from the Schools section. The brief has no SPASD-wide
  stats confirmed for Royal Oaks (unlike Waunakee's #7/#1/13:1/95.9% block on
  the KFW page) — the README explicitly makes this box optional and
  conditional on confirmed data, so it was left out rather than filled with
  invented or borrowed numbers.
- **Sun Prairie city hub (`/sun-prairie/`) and Sun Prairie Market Report
  (`/market-reports/sun-prairie-wisconsin/`) links:** These pages were
  assumed to exist per the standard URL pattern (mirroring the Waunakee
  equivalents used on Kilkenny Farms West) but their existence was **not**
  independently verified in this session. Flag for Phase 5b: confirm these
  URLs resolve, and if `/sun-prairie/` exists, add Royal Oaks to its
  neighborhood directory (link-down requirement).
- **Restaurants:** No restaurant names were confirmed as specifically near
  Royal Oaks' boundary streets in the brief (Section I explicitly flags this
  as a gap) — no dining-card content was invented for it; the Dining &
  Conveniences info-box notes the gap directly and points to the (unverified)
  Sun Prairie city guide for the citywide picture instead.
- **Target (Sun Prairie):** Named in the brief but its address was not
  independently confirmed — left out of the Conveniences section per the
  "every named business needs a real address" rule.
- **What's Brew'n Cafe, Beans 'n Cream, Jinx Coffee, Windsor Breads,
  MOKA:** All mentioned in the brief as Sun Prairie coffee options but none
  had a confirmed current address — left out for the same reason. Only Roots
  Coffeehouse (804 Liberty Blvd, confirmed address) made the page.

## Non-mechanical content decisions

- **Kilkenny/Royal Oaks-style "conflict" handling:** There is no internal
  `[PP]`/`[CL]` cross-engine conflict in this brief to reconcile (Perplexity
  never ran, so there's nothing to average or choose between) — the brief's
  actual open questions are single-source uncertainty flags, not two
  disagreeing sources. Per the task's instruction to never surface internal
  conflict-tracking notation on the public page, none of the `[CL]` tags or
  "Gap" language from the brief appear verbatim on the page; they were
  translated into plain hedged English instead (e.g. "not confirmed," "verify
  by address," "pending a fresh SCWMLS pull").
- **High school assignment:** The brief explicitly could not confirm whether
  Royal Oaks feeds Sun Prairie East or Sun Prairie West post-2022 split. The
  page states both named schools with addresses, states plainly that the
  assignment is unconfirmed, and tells the reader to check
  sunprairieschools.org by address — it does not guess or default to either
  school. This is called out in both the visible Schools section and its own
  dedicated FAQ entry (matched word-for-word in the FAQPage schema).
- **HOA status:** The brief could not confirm whether an HOA exists. The page
  states plainly "not confirmed either way," explains why that's plausible
  (established, informally-named neighborhood, not a single developer-platted
  subdivision), and recommends the same verification path the brief
  recommends (title work / current listing agent) — it does not assert
  "no HOA" as settled fact.
- **Boundary streets (Windsor St / Colorado Ave / Broadway Dr / Thompson
  Rd):** The brief flags these as single-source and not GIS-verified. Every
  place these streets are used on the page (About section, Dining section
  proximity notes) is phrased as "commonly cited" / "not yet GIS-verified,"
  not as a confirmed legal boundary.
- **Population (~6,520) and aggregator "median home price" (~$412,450):**
  Both are explicitly flagged in the brief as low-confidence /
  methodology-unclear or pending-MLS. Per the no-sold-price/no-median-price
  rule, the price figure was never a candidate for inclusion anywhere. The
  population figure was also omitted entirely rather than included with a
  hedge — it wasn't load-bearing for any section and the brief itself flags
  its methodology as unclear, so it didn't clear the bar for "worth hedging
  and keeping" versus "just leave out."
- **"Only open-concept school in SPASD" claim (Royal Oaks Elementary):**
  Kept, but explicitly flagged on-page as needing confirmation of current
  building configuration before repeating it publicly, per the brief's own
  caveat that renovations can change this.
- **Wyndham Hills / Vandenburg comparison:** Wyndham Hills is referenced only
  in a John's Notes prompt (not yet John's actual words) rather than built
  out into a full comparison-table section (Phase 7d), since the brief's
  Wyndham Hills detail, while reasonably solid, wasn't matched against a
  second source either, and a full side-by-side table felt like it would
  overstate the confidence level of a single-source brief. Vandenburg is not
  mentioned on the page at all — the brief itself says it "was not
  independently researched" beyond a directional mention, so there wasn't
  enough to say anything accurate about it.
- **Geo meta tags (`geo.position`, `ICBM`):** Set to Sun Prairie **city-level**
  public coordinates (43.1836, -89.2137), not a Royal-Oaks-specific position —
  the brief never supplied subdivision-level coordinates, and inventing
  precise lat/long for the neighborhood itself would have been exactly the
  kind of fabricated precision the brief warns against. This is called out in
  an HTML comment directly above the meta tags. For the same reason, no `geo`
  field was added to the Place JSON-LD node at all.
- **No street address for John/Integrity Homes anywhere:** Confirmed absent
  from the author bio, footer, and Place schema (the Place schema only has
  locality/region/postal/country, per the standard). Verified by grep for
  "Quinn" across the final file — zero matches.

## Airtable

Record `recBXACIEUzrkm3Di` in base `appTtFjtIHkZZYtgY` / table
`tbl4FXwpxRiyaPcOT` updated: `fldmsKM6bv2QlqW15` → "Drafted",
`fldyHHnYkU6xuyJQ1` → "Claude Code".
