# Subdivision Page System — Claude Code Briefing

Context and task list, carried over from a planning session on August 16, 2026. Read this first before touching anything in the subdivision project.

---

## What this project is

Integrity Homes (John Reuter, Broker/Owner, Waunakee WI) is building a Neighborhood Authority System: one deep, authoritative page per subdivision across Dane County. 126 subdivisions tracked. Goal is to be the definitive local resource — better than Zillow — for buyers, sellers, and residents researching a specific neighborhood.

**Cadence:** one city per week, all subdivisions in that city published the same day. Same-day publishing means within-city interlinking has no dangling-link risk.

**Two-pass model:**
- **Tier 1** — full publish now using AI research + MLS data. Speed and coverage. **A page is "done" at Tier 1 once it clears the Phase 4b QA gate (see `SUBDIVISION-PAGE-BUILDER-README.md`) — not once every open question is personally resolved with John.** Unconfirmed fields (HOA dues, drive times, ambiguous facts) ship as honest "pending"/"not yet routed" badges, not blockers.
- **Tier 2** — Kenzie's human intel (Facebook groups, Nextdoor, HOA newsletters, local news), real photos, John's personal voice, and resolution of each page's Flags/open-items list — layered into the *existing* published page later, at whatever pace, not a gate before Tier 1 ships.

The competitive edge is not secret information — Tier 1 research is all publicly available. The edge is (a) John's proprietary SCWMLS data, (b) completeness nobody else bothers with, (c) Tier 2 hyperlocal detail later.

**2026-08-19 correction:** the Cathedral Point rebuild took over an hour because Tier 2-scale work (real photos, resolving ambiguous facts live, routed drive times, voice-checking Insider Notes) got treated as blocking Tier 1 "done." It also shipped with real defects — leaked bracketed editorial prompts, "Draft — pending" labels visible to buyers, invisible text from a CSS bug — none of which should have passed any QA step. Phase 4b (pre-publish linter + actual visual render check, not just HTML/schema validation) exists specifically to catch these before they reach a live page or a person's live review time. Also confirmed: this environment cannot drive a real browser to Google Maps for routing data (proxy allows simple HTTPS/API calls, not full browser sessions — tested directly, not assumed) — drive times need a routing API key to become fully automated; until then they ship as "not yet routed," which is an acceptable permanent Tier 1 state, not a defect.

---

## Source of truth: Airtable, not spreadsheets

**Base:** Marketing Command Center (`appTtFjtIHkZZYtgY`)

| Table | ID | Contents |
|---|---|---|
| Subdivisions | `tbl4FXwpxRiyaPcOT` | 126 records — status, tier, MLS counts, Semrush data, conflict flags |
| Market Reports | `tblS06Cs9Jzd1sOZE` | One row per city per month, 59 fields of SCWMLS data |
| Price Range Supply | `tblt7I9jJ5ag9BpfU` | Months of supply by price bracket, with confirmed/estimated flags |
| Zip Code Trends | `tbl7PfCqvwrv4Ln1Q` | Per-zip metrics per month |

**`Subdivision_Attack_Plan.xlsx` is deprecated.** Its Page Status column says everything is "Not Started," which is false — that staleness is exactly why it was replaced. Do not read build status from it.

**Write status back to Airtable** as work completes. That's the point of the migration: the tracker stays accurate without someone remembering to update it.

**Files still live in Google Drive** — research briefs, HTML. Airtable holds structured data and links, not documents. Canonical Drive folder: `1vs5sHKyaqkWX6omzWpy8b3dug2zz2Ald`

---

## Status meanings

- **Not Started** — nothing exists
- **Research Done** — research brief exists in Drive, no page built
- **Drafted** — page drafted, not published
- **Needs Rebuild** — ⚠️ research is valid, HTML is outdated. **Do not re-research these.** Rebuild the page from existing research against the current template standard.
- **Published** — live and current

Currently "Needs Rebuild": Kilkenny Farms West, Six Mile Creek, Southbridge, Arboretum Village, Centennial Heights.

---

## Research pipeline

Three legs, same prompt, run for each subdivision:

| Leg | Method | Key |
|---|---|---|
| Perplexity | Sonar API (`sonar-pro`) | `PERPLEXITY_API_KEY` |
| OpenAI | Responses API with `web_search` tool | `OPENAI_API_KEY` |
| Claude | Your own native web search | — |

Both keys are set as user environment variables on this machine.

### Merge rule: union of coverage, NOT consensus voting

Each engine reaches different sources. The point is combined coverage, not agreement.

- **Keep every unique finding.** A fact only one engine found is not weaker — that engine likely reached a source the others didn't.
- **Flag genuine conflicts** (different HOA fee, different plat date, different school assignment) for John. Never resolve silently.
- **Leave gaps marked.** All three saying "not confident" is a real gap for the Tier 2 pass. Do not fill with a guess.
- **Attribute distinctive findings** so a shaky claim can be traced back.

Raw outputs stay in separate files (`<slug>-raw-perplexity.md`, `-raw-openai.md`, `-raw-claude.md`), then merge into `<slug>-research.md`.

### Hard rule on market data

Sold price, median price, days on market, and sales volume come **only** from John's SCWMLS export. Never Redfin, Zillow, Trulia, or any public estimate — those blend in nearby streets and stale data and don't match SCWMLS.

AI research leaves those fields as "pending MLS data from John." Public real estate sites are acceptable only for non-market facts (builder name, floor plan name, HOA management contact).

---

## Page standards

**URL:** `integrityhomeswi.com/[city-lowercase]/[subdivision-slug]/`
Example: `/waunakee/southbridge/`. City lowercase, no county in path, subdivision hyphenated, no punctuation.

**Meta title:** `[Subdivision] [City] WI | Neighborhood Guide | Integrity Homes`

**Meta description:** One sentence — "The complete guide to [Subdivision] — [2-3 distinguishing facts]."

**Template:** Kilkenny Farms West v7 is the reference build, cross-confirmed by Six Mile Creek. **Full static sections, no accordions.** Southbridge uses an older collapsible-accordion pattern — that's legacy, do not replicate it. Mobile responsiveness comes from CSS media queries only.

**Section set** (order varies slightly between builds; treat as a required set, not a rigid sequence): breadcrumb → hero → stats strip → quick answer → photo strip (only if 2+ real photos exist) → about → why people choose it → schools → parks → dining → commute → dog parks → market data → FAQ → market strip → CTA → ROH block → author → explore → footer.

**Images:** if no approved photo exists in the Media Vault, use a gradient/color placeholder with an HTML comment noting asset status. Never a stock photo. Mark the page IMAGE-PENDING in Airtable and swap later — that swap doubles as a content-freshness signal.

**No street address on subdivision pages.** Remove "1025 Quinn Drive Ste 100" from author bio and footer. Also remove any fabricated "anchor address" from Place schema (Southbridge has `1500 Blue Ridge Trail` — an internal routing reference, not a real address). Keep phone, email, "Waunakee-based," city references, Real Broker affiliation, MLS disclaimer.

---

## Schema — reference, don't redefine

The master identity script lives in Lofty's global Script area and defines:
- `https://integrityhomeswi.com/#org` — Organization/RealEstateAgent
- `https://integrityhomeswi.com/#john` — Person
- `https://integrityhomeswi.com/#website` — WebSite

**Subdivision pages reference these by `@id` only.** Never repeat the properties. Every page currently redefines them from scratch, which is why the org name drifted between builds — no single source of truth.

Existing pages have three broken references to fix:
- `#organization` → should be `#org`
- `#johnreuter` → should be `#john`
- `isPartOf: #website` — the master script previously used `#site`, now corrected to `#website`

Correct `@graph` structure is in `subdivision-schema-standard.md`.

---

## GEO / AI-citation requirements

Ranking on Google and getting cited by AI answer engines have diverged — overlap between the two dropped from ~70% to under 20%. Traditional SEO still matters but isn't sufficient.

**Quick-Answer block** — required on every page, immediately after the stats strip. An `<h2>` question ("What is [Subdivision] in [City], Wisconsin?") plus a 60-90 word answer built from a four-slot fact template. This is the passage most likely to be quoted verbatim by an AI, so it carries the strictest accuracy bar. Full spec and worked examples in `subdivision-quick-answer-block.md`.

**Speakable schema** on the quick answer and FAQ selectors.

**Freshness matters** — `dateModified` must actually change when content changes. Quarterly MLS refresh is the highest-leverage recurring task for staying AI-cited.

---

## Interlinking (hub-and-spoke)

City hub pages are the hub. Subdivision pages, market reports, and blogs are spokes.

1. **Link up** — every subdivision page links to its city hub
2. **Link down** — ⚠️ easily missed: when a subdivision page goes live, **edit the city hub to add it.** A one-way link is a dead end, not a cluster.
3. **Link sideways** — to nearby subdivisions, pulled from research Section L (Comparison With Nearby Subdivisions). Vary anchor text.
4. **Link to market reports** — the city's permanent market report URL
5. **Link to blogs** — cross-reference `Integrity_Homes_Content_System_FINAL.xlsx` (239 posts) for city-tagged or subdivision-mentioning content

---

## MLS name matching

Subdivision names in raw MLS exports are messy — misspellings, abbreviations, inconsistent formatting.

- **Auto-consolidate** obvious typos and case differences ("Kilkenny Fams" → "Kilkenny Farms")
- **Never auto-merge** similarly-named but genuinely distinct subdivisions — flag for review

Known conflict pairs (Conflict Flag set in Airtable):
- Kilkenny Farms ≠ Kilkenny Farms West
- Southbridge ≠ Westbridge (shared developer, shared "-bridge" naming, separate HOAs)
- Eagle Trace (Verona) ≠ Crest at Eagle Trace (Middleton)
- Windsor Gardens ≠ Windsor Crossing
- Seminole Forest ≠ Highlands of Seminole
- Wildwood ≠ Wildwood South
- Castle Crest ≠ Castle Creek
- "Cathedral Point" — Drive folder is misspelled "Cathederal Point"; use correct spelling in all output

Use the Semrush-verified name variant as primary. Several subdivisions have competing forms where only one carries search volume — "Six Mile Creek" vs "Sixmile Creek" (entrance sign and golf course use one word, buyers and MLS use two), "Heritage Gardens at Erickson Farms" vs "Heritage Gardens," "Crest at Eagle Trace" vs "Eagle Trace."

---

## Brand rules

- **"Integrity Homes"** — never "Integrity Homes Wisconsin." Legal name "Integrity Homes of Wisconsin" only where legally required (schema `legalName`, footer copyright).
- **No em dashes anywhere.**
- John's cell **608-669-4226** on Integrity Homes content. ROH Foundation **608-492-0515** on ROH content.
- ROH block required on every page. ROH is an **IRS-approved 501(c)(3)**, EIN 39-3358820 — not "pending approval."
- John's title: **Broker/Owner**.

---

## Task list

### ✅ Proven end-to-end 2026-08-16 (system test, not a real build)

Ran the full loop once on **Kilkenny Farms, Waunakee** — chosen specifically because it's a genuinely "Not Started" record AND the exact Kilkenny-Farms/Kilkenny-Farms-West conflict pair this project exists to prevent errors on:

1. Phase 1b archive check — confirmed via live Drive search that no "Kilkenny Farms" (non-West) research or page exists. Passed.
2. Perplexity leg (`research_perplexity.py`) — ran clean, both main + conveniences files.
3. Claude leg — ran as a background agent using the same prompt templates, both main + conveniences files. `WebFetch` still blocked in this environment (snippet-only via `WebSearch`) — a real quality ceiling worth fixing (see below), not a blocker.
4. **Merge step — built and run for the first time.** `research/kilkenny-farms-research.md`. The two legs actually disagreed on the single most load-bearing fact (whether Kilkenny Farms West is a phase of Kilkenny Farms or a separate subdivision) — flagged explicitly per the union rules rather than silently resolved, with the evidence and reasoning laid out for John to confirm.
5. **Airtable status write-back — proven for the first time.** Kilkenny Farms record updated to `Research Done`, Owner `Claude Code`.

**Open finding from this test:** `WebFetch` (full page reads) is blocked by this Claude Code environment's network policy for every external domain, even after John widened "Network access" to "Full" earlier — that setting only cleared enough for direct API calls (Perplexity, this session's Airtable/Drive MCP tools), not general web browsing. The Claude leg is currently limited to `WebSearch` snippets as a result. If this matters enough to fix, it needs a different/broader network policy change than the one already tried — worth revisiting in the environment settings.

### Blocking — before the next REAL build batch

1. ~~Test the research pipeline on one subdivision~~ — done, see above.

2. **Add the Quick-Answer block to the NAS master template.** ✅ Done 2026-08-16 — `templates/kilkenny-farms-west-v8-MASTER-TEMPLATE.html`. Not yet pushed to Drive/Lofty; staged for review.

3. **Add the corrected `@graph` to the NAS master template.** ✅ Done 2026-08-16, same file as above.

### Cleanup — not blocking

4. Apply corrected schema to existing pages (Kilkenny Farms West, Six Mile Creek, Southbridge, Arboretum Village, Centennial Heights)
5. Remove Quinn Drive address from subdivision page bios and footers
6. Remove "anchor address" from Southbridge Place schema
7. Add Quick-Answer blocks to already-published pages
8. Reconcile loose top-level `Page-v1_X.html` files into their subdivision folders
9. Verify what "Eagle Point" is — Drive folder exists, appears on no tracker, city assignment is a guess

### Recurring

10. Quarterly MLS refresh — Market Data section, Quick-Answer price sentence, `dateModified`
11. Quarterly crawler-access check (confirm Lofty isn't blocking AI crawlers)
12. Expand the conflict-pairs list as subdivisions get processed

---

## Companion files from the planning session

- `SUBDIVISION-PAGE-BUILDER-README.md` — full workflow, all phases
- `subdivision-quick-answer-block.md` — Quick-Answer spec
- `subdivision-schema-standard.md` — corrected `@graph`
- `Integrity-Homes-Homepage-Schema-Sheet.md` — homepage blocks and master identity script
- `market-report-consistency-check.md` — pre-publish validation for market reports

---

## One principle worth carrying

Nearly every error found during the planning session was the same shape: **a value stated in two places that disagreed.** The org name drift, the `#site`/`#website` mismatch, the `#johnreuter`/`#john` mismatch, 27-vs-18 pending listings on a live page.

The fix is structural, not vigilance. Read each value once from its source, reference it everywhere from there. A number typed twice is a number that will eventually disagree with itself.
