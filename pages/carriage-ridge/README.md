# Carriage Ridge — Build Notes (Tier 1, v1)

Built 2026-08-20. Source of research, decisions made, and everything still open for
John/Kenzie to resolve in Tier 2.

## Research source — Phase 1b found existing work, no fresh research was run

Per the mandatory Phase 1b check, Google Drive was searched first (canonical archive
folder `1vs5sHKyaqkWX6omzWpy8b3dug2zz2Ald` and beyond) before any new research began.

Found: **`ResearchBrief.md`** for Carriage Ridge, Google Doc id
`1gEGKi2mFIi8MY05xvcg7a5HbCylffGLBq9mhv1OP7LQ`, prepared 2026-08-07 by a prior Claude
desk-research pass per the Kenzie SOP v2 workflow. It lives in a Drive folder that
isn't the direct `carriage-ridge/` subfolder of the canonical archive (it turned up
under a different parent id, `0ANYtjtT9QNqjUk9PVA` — worth Kenzie filing it into the
proper `subdivisions/carriage-ridge/` folder as cleanup) but it is unambiguously the
Carriage Ridge Tier 1 research brief: full A–Q sections, sources, and a review table.

No `Flags.md`, `CMS.md`, or `Page-v1.html` was found anywhere in Drive for Carriage
Ridge — confirmed via targeted search (`fullText contains 'Carriage Ridge'` and
title-filtered searches against the canonical folder). This matches the Airtable
status ("Research Done," no page yet) — this v1 build is the first page draft.

**This page was built entirely from that existing brief.** No new web research was
run, consistent with the instruction to exhaust Drive before doing fresh Phase 1 work.

## Key facts used, and why they're stated the way they are

- **Jurisdiction:** Carriage Ridge carries a Waunakee, WI 53597 mailing address but is
  verified via Dane County's own Access Dane parcel records to sit in the **Town of
  Westport**, not the Village of Waunakee. The page states this plainly and repeatedly
  (hero eyebrow, stats strip, About section, FAQ) rather than letting the mailing
  address imply village membership — this is the single most important framing fact
  in the brief, flagged the same way Bishops Bay's split-jurisdiction fact was handled
  elsewhere in this project.
- **"Bring your own builder" model:** genuinely different from every other subdivision
  built in this project so far — no single production builder, buyers purchase a
  platted lot and choose their own builder. Led with this as the hero badge.
- **Assessed values, not sold prices:** the brief's two Dane County assessment
  examples ($1,930,400 and $1,137,500, 2026 records) are real public data but are
  **not** MLS sold prices. They're presented in the stats strip, About sidebar, and
  Market Data section with explicit "county assessment record, not an MLS sold price"
  language every time they appear, per the standing rule against substituting any
  non-SCWMLS number for market data.
- **No routed drive times:** the brief discloses a tool malfunction (stale/cached
  geocoding results from an unrelated subdivision) that blocked all routing for this
  subdivision. Every distance/drive-time cell in the Proximity & Commute table and
  the Dog Parks section is labeled "Not yet routed" rather than estimated or
  reused from a different subdivision's numbers.
- **Peaceful Valley Park / Blue Ridge Park proximity claim — deliberately NOT
  repeated:** the developer's own site claims walking-distance proximity to these two
  parks, but the brief cross-references this project's own Southbridge research and
  finds both parks are actually in Southbridge, several miles away. This page states
  that discrepancy explicitly in the Nearby Conveniences section instead of repeating
  the developer's claim.
- **Elementary school assignment left unresolved on purpose:** the brief explicitly
  declined to force an elimination-based guess given how far outside the village core
  this location sits. The page follows that same discipline — K–4 row says "Not Yet
  Confirmed" with a call-the-registrar instruction, rather than guessing Heritage,
  Arboretum, or Prairie.
- **No pool/clubhouse:** stated as a genuine, disclosed amenity gap (in the Parks
  section as an info-box, and in the FAQ) rather than glossed over, matching every
  other comparable subdivision's amenity write-up in this project.
- **Equestrian stable ownership:** Carriage Ridge Stables LLC is called out explicitly
  as an independently owned business, not an HOA amenity, everywhere it's mentioned
  (Why People Choose It, Parks section, FAQ) — the brief was emphatic that conflating
  the two would be a real accuracy problem.
- **Geo coordinates omitted from the Place schema** — no verified lat/long exists for
  Carriage Ridge (the brief's own geocoding attempts failed). Precedent for omitting
  `geo` entirely rather than guessing comes from `pages/bishops-bay/bishops-bay-v2.html`,
  which also omits it.
- **Comparison/nearby subdivision links:** the brief's Section L names Bishops Bay,
  Southbridge, and Heritage Hills as comparables — all three already have published
  pages in this repo (`pages/bishops-bay/`, `pages/southbridge/`, `pages/heritage-hills/`),
  so the market strip links directly to them rather than logging a cross-city
  placeholder.

## Template / design source

Built from the Six Mile Creek template
(`pages/six-mile-creek/six-mile-creek-original.html`) rather than Kilkenny Farms West,
because Six Mile Creek's simpler structure (no photo strip, no purple schools
section, no forced ranking stats) fit a subdivision with no approved photos and no
verified district-ranking numbers better than force-fitting KFW's fuller sections.
Section-set coverage still matches the README's required list (hero, stats strip,
quick-answer, about, why-people-love-it, schools, parks, market data, proximity,
dining, dog parks, FAQ, market strip, CTA, ROH, author, explore, footer) — the photo
strip is the only section genuinely skipped, per the "skip rather than fill with
placeholders" rule, and is documented as `IMAGE-PENDING` in an HTML comment at the
top of the file.

## Phase 4b QA — results

- `grep -c "#johnreuter"` → **0**
- `grep -c '"#organization"'` → **0**
- `grep -ci "quinn drive"` → **0**
- `grep -c "DRAFT"` → **0**
- `grep -c "\[ John"` (or any bracketed editorial prompt) → **0**
- `author` → `{ "@id": "https://integrityhomeswi.com/#john" }` only
- `publisher` → `{ "@id": "https://integrityhomeswi.com/#org" }` only — no full
  Person/Organization node defined anywhere on the page
- JSON-LD parsed successfully with `python3 json.loads` — 4 `@graph` nodes (WebPage,
  BreadcrumbList, Place, FAQPage)
- Speakable schema present on the WebPage node, targeting `.qa-question`,
  `.qa-speakable`, `.faq-a`
- Rendered full-page with Playwright/Chromium and reviewed every section as
  cropped screenshots. **Found and fixed one real bug:** the Market Data section's
  closing disclaimer paragraph was styled `color: rgba(255,255,255,0.55)` (a leftover
  from copying a navy-background pattern) sitting on the `.market-box`'s cream
  background — nearly invisible white-on-cream text. Fixed to `var(--text-muted)` and
  re-rendered to confirm it's now legible. `qa-screenshot.png` in this folder is the
  **post-fix** render.
- No `1025 Quinn Drive` or any office street address anywhere on the page (author
  bio or footer) — confirmed by the Quinn Drive grep above returning zero.

## Open items for John / Kenzie (Tier 2) — everything the research brief flagged as unresolved

1. **Developer/platting company name** — not identified anywhere in the brief. Call
   carriageridgedevelopment.com's own number, (608) 535-4333, or visit
   `/contact-us/` in a real browser (blocked to the research tool).
2. Read the two Waunakee Tribune / hngnews.com articles directly (both were
   rate-limited during research) — likely contain the developer name, acreage, and
   vote dates for the "68-lot addition."
3. **HOA dues, management, and covenant/architectural-control terms** — the HOA's own
   site (carriageridgehoa.com) exists but its detail subpages 404'd for the research
   tool (likely JS-driven navigation). Not published on the page until confirmed.
4. **Specific elementary school assignment** — call WCSD Registrar, (608) 849-2000,
   with a real Carriage Ridge address (e.g., 5769 Derby Downs Dr).
5. **Full routed drive-time table** — re-run geocoding/routing from a confirmed
   Carriage Ridge address once the earlier tool malfunction is resolved. This
   directly feeds the Proximity & Commute table and the Quick-Answer's anchor
   distance, both currently qualitative/unrouted.
6. **"Carriage Ridge Neighborhood Park"** — referenced by name on a third-party
   recreation directory (recplanet.com) but never independently confirmed. Field-visit
   or call to confirm address, acreage, and ownership (HOA vs. Town of Westport).
7. **Total lot/acreage reconciliation** — one source says 80 acres/132 lots, the
   developer's own site claims 200 acres. Not resolved; not stated on the page.
8. **Carriage Ridge Stables LLC's actual relationship to residents** — confirm
   whether boarding/riding access is genuinely available to any resident and at
   what cost.
9. **Wisconsin DFI entity confirmation** for the HOA and/or development company.
10. **Possible undiscovered third addition** — only two are confirmed (First
    Addition, 2nd Addn); the "68-lot addition" headline's date is unconfirmed.
11. **Photography/video** — no approved image exists for Carriage Ridge in any
    source checked. Hero uses a navy gradient placeholder, flagged `IMAGE-PENDING`
    in an HTML comment. Needs a field visit to shoot ponds, trails, and stable
    access per the brief's own Tier 2 list.
12. **Town of Westport incorporation status** — the Town petitioned the Wisconsin
    Incorporation Review Board in July 2025 to become its own village. If that
    resolves during this project's active life, the jurisdiction language on this
    page (and possibly the URL's `/waunakee/` prefix itself) may need revisiting.
13. **MLS export** — every Market Data field is pending John's SCWMLS pull. When
    supplied, cross-check against both recorded additions ("Carriage Ridge, First
    Addition To" and "Carriage Ridge, 2nd Addn") and report lot sales separately
    from completed-home sales, since this is an active custom-lot community.

## Interlinking done / still needed

- **Up:** links to `/waunakee/` city hub (breadcrumb, market strip, explore band) — done.
- **Down:** the Waunakee city hub page itself still needs to be edited to add
  Carriage Ridge to its neighborhood directory (Phase 5b) — **not done as part of
  this build**, flagging per the mandatory step; this repo doesn't currently contain
  the Waunakee hub page file to edit directly.
- **Sideways:** linked to Bishops Bay, Southbridge, and Heritage Hills (all three
  already published in this repo) in the market strip — done.
- **Market report:** linked to `/market-reports/waunakee-wisconsin/` — done.
- **Blog cross-linking (Phase 5e):** not attempted this pass — no blog content
  inventory was available in this session.

## Not committed to git

Per instructions, files were left in place (`carriage-ridge-v1.html`, this
`README.md`, `qa-screenshot.png`) without a git commit — John will verify and commit.
