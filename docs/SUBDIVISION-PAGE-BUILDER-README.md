# Subdivision Page Builder — Claude Code Operating Instructions

## Purpose
This is the operating guide for building Neighborhood Authority System (NAS) subdivision pages for Integrity Homes autonomously. When told to "build the [Subdivision Name] page" (or given a batch of subdivisions), follow this workflow end to end.

Source of truth for the subdivision list: `Subdivision_Attack_Plan.xlsx` (Google Drive). Filter to `Page Status = Not Started` and work by Tier, then by Rank within tier, unless a specific subdivision is named.

**Note:** superseded by `CLAUDE-CODE-BRIEFING.md` — the actual source of truth is now the Airtable "Marketing Command Center" base, not this xlsx. Kept here for the full phase-by-phase workflow detail, which is still current.

---

## Phase 0 — Batch Discipline
- Work **one city at a time**, roughly one city per week (or faster once the workflow is proven).
- All subdivisions within a city are built and published on the same day. This means within-city interlinking (Phase 5c, 5b) is safe to do immediately — no 404 risk, since every page a same-city page links to already exists by the time it goes live.
- After each city's batch, stop and report per Phase 6.

---

## Phase 1 — Research (Kenzie SOP v2 — investigative research, not persona roleplay)

**Note:** This replaces an earlier "you live in the neighborhood" persona-prompt version. That framing invited fabricated-sounding local color. The current version treats this as investigative research: verify everything, mark what can't be verified, never invent a personal anecdote.

### Part 1: Deep Research (AI-assisted)
Run the prompt below through **Claude, ChatGPT, and Perplexity** (API preferred over browser — see Phase 1a).

**Why three sources:** each engine reaches different sources and surfaces different findings — Perplexity tends to pull the strongest results, ChatGPT surfaces things Perplexity misses, and so on. The goal is **union of coverage, not consensus voting.** Merge everything each engine found into one brief; a fact appearing in only one source isn't weaker, it's usually just that engine reaching a source the others didn't.

**Merge rules:**
- Combine all unique findings from all three into one brief. Don't discard something because only one engine found it.
- Where sources **conflict** on the same fact (different HOA fee, different plat date, different school assignment), flag it for John rather than picking one silently.
- Where all three say "not confident," note it as a gap for Tier 2 / Kenzie's human-intel pass — don't fill it with a guess.
- Note which engine produced each distinctive finding, so a questionable claim can be traced back.

```
You are helping Wisconsin real estate agent John Reuter build the most complete and useful online neighborhood guide for:

SUBDIVISION: [SUBDIVISION NAME]
CITY: [CITY], Wisconsin

The goal is to establish John as the genuine neighborhood expert. This is not a generic subdivision description, sales pitch, or rewritten builder page. Research the neighborhood deeply enough to answer the questions that current residents, prospective buyers, sellers, and relocating families would actually ask.

RESEARCH REQUIREMENTS

Research before writing. Use multiple sources, prioritizing:
1. Municipal plats, planning documents, meeting packets and park plans
2. Recorded covenants, HOA documents and management information
3. Official school-district attendance maps
4. Builder and developer documents
5. Municipal park, trail and development maps
6. Current maps and local business information
7. Reputable local reporting and neighborhood sources

Do not rely primarily on the developer's marketing language.

Do NOT use Redfin, Zillow, Trulia, or similar consumer real-estate sites as a source for sold-price data, median/average sale price, or days-on-market figures. Those numbers come from John's own MLS (SCWMLS) export, which is supplied separately — leave those fields marked "pending MLS data from John" rather than substituting a public-site estimate. Public real estate sites may be used only for non-market facts (e.g., confirming a builder name, a floor plan name, or an HOA management contact).

VERIFY, DO NOT GUESS

For every important fact:
* Confirm it through a reliable source whenever possible.
* Distinguish verified facts from reasonable conclusions.
* Say "not confident" when information cannot be reliably confirmed.
* Identify conflicting information instead of choosing one version silently.
* Do not present proposed amenities as completed amenities.
* Do not apply an HOA fee from one housing section to the entire neighborhood.
* Do not guarantee school assignments without checking the official attendance boundary.
* Date all prices, fees, development plans and other information that may change.
* Do not claim to live in the neighborhood or invent personal experiences.

DEPTH REQUIRED

Research and report on all of the following:

1. DEVELOPMENT HISTORY — original developer/builders; when planning/infrastructure/construction began; development phases and additions with dates; which phases are complete/active/approved/proposed; expected future expansion; original land use if documented.

2. EXACT LOCATION AND BOUNDARIES — what part of the city/village; exact roads, cross streets, physical boundaries; every confirmed street within the subdivision; major entrances/connections; whether phases have different access points; relationship to downtown and neighboring subdivisions; note uncertain boundaries due to active expansion.

3. SCHOOL ASSIGNMENTS — school district; assigned elementary/intermediate/middle/high schools; verify using addresses from different sections; note any attendance boundary crossings; grades served and approximate distance; advise address-level verification.

4. HOUSING PRODUCT TYPES (no sold-price stats — see note below) — break into single-family, cottage-style, twin/duplex/townhome/condo, apartments/senior housing, custom vs. production. For each: architectural styles, typical year built, typical sq ft, bed/bath ranges, lot-size range, garage configs, common builder floor plans, current new-construction starting prices (builder-quoted, dated). Do NOT report median/average sold price or days-on-market — mark those "pending MLS data from John" for every housing type. Do not substitute builder starting prices for actual sold data.

5. HOA, COVENANTS AND COSTS — HOA's full legal name; management company/contact; which properties fall under which association; current dues (dated by year); what dues include; separate fees for twin homes/condos if applicable; architectural-control requirements; restrictions on fences, sheds, rentals, parking, landscaping, pets, exterior changes; known special assessments or developer-controlled period. Show separately by housing type if fees/rules differ.

6. AMENITIES AND OPEN SPACE — divide into completed/available now, under construction, approved but not completed, proposed/uncertain. Cover parks, playgrounds, trails/sidewalks, conservancy/natural areas, ponds/stormwater, athletic facilities, dog parks, pools, clubhouses, gathering spaces, municipal trail connections, nearby public parks. Note ownership/maintenance of major amenities when known.

7. NEARBY CONVENIENCES — realistic driving/walking times to grocery, coffee, restaurants, gas, pharmacy/healthcare, library, schools, parks, downtown, major highways, Madison employment centers, Dane County Regional Airport. Name specific businesses — never "shopping and dining are nearby."

8. RESIDENT-LEVEL KNOWLEDGE — walking routes/trail connections, traffic patterns and primary exits, ongoing construction, snow-removal/private-maintenance arrangements, community events, noise/traffic considerations, access to schools/parks, postal address vs. municipal jurisdiction, trash/recycling/municipal services, questions residents commonly ask, details useful when selling in the subdivision.

9. BENEFITS AND POSSIBLE DRAWBACKS — what residents are likely to value, with specific evidence, not promotional adjectives. Also legitimate considerations: active construction, smaller lots, HOA restrictions, limited private amenities, traffic, distance from services, future development uncertainty, differing fee structures. Keep factual and fair — credibility, not "everything is perfect."

10. COMPARISON WITH NEARBY SUBDIVISIONS — compare against 3–5 most relevant nearby subdivisions on location, home age, price range (builder-quoted only, dated), lot sizes, housing variety, HOA structure, parks/pools/trails, downtown proximity, schools, buyer fit. Identify 2–3 genuinely distinctive qualities — avoid vague claims like "strong sense of community" unless supported.

REQUIRED OUTPUT — organize into these sections:
A. Expert Summary
B. Verified Quick-Facts Table
C. Development and Phase History
D. Location, Streets and Boundaries
E. Schools
F. Homes and Housing Products (builder prices only — sold data marked "pending MLS data from John")
G. HOA and Restrictions
H. Parks, Trails and Amenities
I. Nearby Conveniences with Distances
J. What Residents Value
K. Possible Considerations
L. Comparison With Nearby Subdivisions
M. Frequently Asked Questions
N. "Only a Local Would Know" Content Ideas (at least 10 specific questions/observations to investigate in person, use in videos, or ask residents about)
O. Missing Information John Should Verify (every MLS/sold-data field left pending)
P. Sources with direct links

QUALITY CHECK BEFORE ANSWERING — confirm that:
* The answer couldn't simply have the subdivision name swapped for another neighborhood's.
* It contains specific streets, dates, schools, housing data, fees, destinations.
* Completed vs. proposed amenities are separated.
* Different housing products/fee structures are separated.
* No sold-price/median-price/days-on-market figures came from Redfin/Zillow/Trulia — marked pending MLS data instead.
* Claims are supported by direct sources.
* Unknown information is labeled "not confident."
* The result helps John answer follow-up questions rather than merely advertise the neighborhood.

If public information is insufficient, don't pad with generic language — give verified findings plus a precise list of records/people/field observations needed to finish the file.
```

After running all three sources: paste outputs into one doc, highlight disagreements, flag any "not confident" gaps rather than filling them with a guess.

### Part 2: MLS Market Data (from John — never from public sites)
Median/average sold price, days on market, list-to-sale ratio, sales volume, active/pending counts **never** come from Redfin, Zillow, Trulia, or any public consumer real estate site — those numbers don't match SCWMLS and are frequently wrong for a specific subdivision (they blend in nearby streets or stale data).
- John pulls the raw SCWMLS export/report for the subdivision and supplies it directly.
- Claude's job is to analyze/summarize that export once provided — not source the numbers independently.
- Until John supplies it, every "pending MLS data from John" field from Part 1 stays pending. Do not fill with a public-site estimate as a placeholder.

### Part 3: Human/Local Intel (AI can't do this part)
This is what makes the page actually better than Zillow — current, hyperlocal, only-a-resident-would-know detail:
- Facebook groups — search "[Subdivision name] [City]" or "[Subdivision name] neighbors"
- Nextdoor — same idea
- HOA meeting notes/newsletters — assessment changes, new amenities, disputes
- Recent local news — subdivision name + city in Google News, last 6–12 months
- Google/local business reviews mentioning the neighborhood
- Anything seasonal/timely — construction, new stores, upcoming events

Section N ("Only a Local Would Know") from Part 1 is a good starting checklist of things to go verify here — those are AI-generated leads to chase down, not confirmed intel on their own.

**Bar for "good" local intel:** not "has parks and trails" (generic), but "residents in the Facebook group have been discussing the new stop sign going in this fall after traffic complaints" — specific, current, sourced.

### Output per subdivision
One research file per subdivision with three clearly labeled sections — **Deep Research** (Part 1, MLS fields marked pending), **MLS Market Data** (Part 2, once supplied), **Local Intel** (Part 3, each item sourced, e.g. "per [Subdivision] Facebook group, July 2026"). Save as `research/[slug]-research.md`. These are raw briefs, not publish-ready copy — don't publish directly from this file.

If a Research-Brief.md already exists for this subdivision (see Phase 1b), read and use it — don't rerun research from scratch.

### Phase 1a — Research engine setup

All three legs are automated. Claude Code runs the same research prompt through each, then merges per the union rules above.

| Engine | Method | Status |
|---|---|---|
| **Claude** | Claude Code's native web search | Already enabled — no setup needed |
| **Perplexity** | Perplexity Sonar API | API key required. ~$0.30–$1.30 per subdivision |
| **ChatGPT** | OpenAI API | API key required |

- Perplexity API key: `[ADD ENV VAR NAME ONCE SET UP]`
- OpenAI API key: `[ADD ENV VAR NAME ONCE SET UP]`

**Setup notes:**
- Store keys as environment variables, not hardcoded in the README or any script that could end up in a repo.
- Run the three legs in parallel rather than sequentially — cuts wall-clock time per subdivision meaningfully across a full city batch.
- Log each engine's raw output separately before merging (e.g. `research/[slug]-raw-perplexity.md`, `-claude.md`, `-chatgpt.md`), then produce the merged brief. Keeping raws makes it possible to trace a questionable claim back to its source without re-running.
- If one engine fails or times out, proceed with the other two and note the gap in the build log — don't block the whole batch on one API hiccup.

### Phase 1b — Check the existing archive FIRST, before running new research
Substantial research already exists in the Google Drive Subdivision Attack Plan folder — this is the **canonical source of truth**, checked live via Drive access, not a local zip/dump copy:

**Canonical folder:** `Subdivision Attack Plan` (Google Drive)
**Folder ID:** `1vs5sHKyaqkWX6omzWpy8b3dug2zz2Ald`
**Link:** https://drive.google.com/drive/folders/1vs5sHKyaqkWX6omzWpy8b3dug2zz2Ald

Do not work from a local zip export of the old Claude Project — that's a stale, likely-duplicate snapshot. Read this Drive folder directly and treat it as current. Before starting fresh research on any subdivision, check for an existing folder or loose file here:

```
subdivisions/
  kilkenny-farms-west/Page-v7.html          (already fully built — reference standard)
  carriage-ridge/Flags.md, CMS.md, Page-v1.html, Research-Brief.md
  centennial-heights/...   (also has a loose Page-v1_4.html at Drive top level — reconcile which is current)
  arboretum-village/...    (also has a loose Page-v1_3.html at Drive top level — reconcile which is current)
  southbridge/...          (also has a loose Page-v1_2.html at Drive top level — reconcile which is current)
  savannah-village/...
  golden-ponds/...
  westbridge/...
  bishops-bay/...
  heritage-hills/...
  eagle-point/...          (found in Drive, not yet cross-checked against Project)
  cathedral-point/...      (Drive folder is misspelled "Cathederal Point" — fix on sight, don't propagate the typo into the slug)
  smiths-crossing/...      (found in Drive, not yet cross-checked against Project)
  savannah-brooks/...      (found in Drive, not yet cross-checked against Project)
  Workflow/  (checklists, work order, quick-start guide, research prompts, brief template — canonical SOP source)
  claude/Session-Log.md
Subdivision_Attack_Plan.xlsx
```

- If a `Research-Brief.md` exists for the subdivision, use it as the Phase 1 output — do not rerun research.
- If a `Flags.md` exists, read it first — it likely notes name-conflict issues, data gaps, or things to double check.
- If a `Page-v1.html` (or numbered variant like `Page-v1_2.html`) exists, treat the subdivision as already drafted — Phase 4 becomes a refinement/QA pass against the Kilkenny Farms West v7 standard, not a fresh build. **Note:** several subdivisions currently have their draft HTML sitting loose at the top level of the Drive folder rather than filed inside their own subdivision folder — reconcile and file these properly as part of cleanup, don't duplicate work by treating a loose top-level file and a folder file as two different drafts.
- **Note:** `Subdivision_Attack_Plan.xlsx` on Google Drive currently shows all subdivisions as "Not Started" — this is stale. The archive (Project + Drive folder) is the accurate source of what's actually done. Update the tracker's Page Status column to match reality once confirmed.

---

## Phase 2 — MLS Market Data Pull
- Source: SCWMLS export only (per standing rule — no external data like Zillow/Redfin estimates).
- Filter the MLS spreadsheet to the target subdivision.
- **Fuzzy matching required** — subdivision names in raw MLS exports are frequently misspelled, abbreviated, or inconsistently formatted (e.g., "Kilkenny Fams" vs "Kilkenny Farms").
- **Known conflict pairs — do NOT auto-merge, always flag for human review:**
  - Kilkenny Farms ≠ Kilkenny Farms West (two distinct subdivisions, easily confused)
  - Southbridge ≠ Westbridge (shared "-bridge" naming and shared developer, but separate non-adjacent subdivisions with separate HOAs — confirmed via existing page FAQ)
  - "Cathedral Point" — Drive folder name is misspelled "Cathederal Point"; treat as the same subdivision, correct spelling in all new output
  - [ADD OTHER KNOWN CONFLICT PAIRS AS DISCOVERED]
- Rule of thumb: obvious typos/case differences (e.g., "HEritage Hills" vs "Heritage Hills") → auto-consolidate. Genuinely different-but-similar names → flag, do not guess.
- Pull: sold price (median + range), days on market, # of sales trailing 12 months, active inventory if any.

---

## Phase 3 — Image / Asset Check
- Search Google Drive Image Vault + Lofty CDN for existing approved images for this subdivision.
- **If no image exists:** use the generic city-level placeholder image (per city — Waunakee, Sun Prairie, DeForest, Verona, Madison, Middleton) and flag the page in the build log as `IMAGE-PENDING`.
- Do not block page publication waiting on an image. Swapping the placeholder later is a deliberate freshness signal for Google re-crawl — treat it as a scheduled follow-up task, not a blocker.

---

## Phase 4 — Page Build
- Use the NAS master template (Kilkenny Farms West v7 is the reference build).
- **URL slug standard (confirmed from live pages — Southbridge, Arboretum Village, Centennial Heights):**
  `integrityhomeswi.com/[city-lowercase]/[subdivision-slug]/`
  Example: `integrityhomeswi.com/waunakee/southbridge/`, `integrityhomeswi.com/waunakee/arboretum-village/`
  City is lowercase, no county in the path. Subdivision name is lowercase, hyphenated, no punctuation.

- **Meta title format (confirmed):** `[Subdivision] [City] WI | Neighborhood Guide | Integrity Homes`
  Example: `Southbridge Waunakee WI | Neighborhood Guide | Integrity Homes`

- **Meta description format (confirmed):** One sentence — `The complete guide to [Subdivision] — [2–3 distinguishing facts specific to this subdivision, not generic].`
  Example: "The complete guide to Southbridge — a six-addition Waunakee neighborhood with the shortest routed drive to downtown found in this project, a fully-verified pool fee schedule, four confirmed parks, and three separate HOAs buyers need to understand."

- **⚠️ Brand name flag:** older page schema (Kilkenny Farms West, Southbridge) uses `"Integrity Homes Wisconsin"` as the Organization name — conflicts with the standing brand rule.

- **⚠️ CRITICAL — `@id` mismatch found (this would break the reference-stub fix if not caught):** the actual homepage schema defines the Organization at `"@id": "https://integrityhomeswi.com/#org"` — not `#organization` as subdivision pages currently reference. These are different fragment identifiers to a schema parser; a subdivision page referencing `#organization` points at nothing. **Use `#org` everywhere, matching the homepage** — this applies to the stub pattern below and to fixing any already-published pages using `#organization`.

- **⚠️ The homepage's own Organization node currently violates the brand rule** — its primary `name` is `"Integrity Homes of Wisconsin"` (should be `"Integrity Homes"`, with the full name only as `legalName`), and its `alternateName` array includes `"Integrity Homes Wisconsin"` — the specific variant the brand rule bans. **Fix this at the source (homepage) first** — subdivision pages referencing it by `@id` will inherit whatever the homepage says, so fixing subdivision pages alone accomplishes nothing.

- **⚠️ John's jobTitle is inconsistent across the site:** homepage schema says `"Broker Associate & Team Leader"`; subdivision pages say `"Broker/Owner, Military Relocation Professional"`. Per standing info, "Broker/Owner" is correct — the homepage title appears outdated. Fix at the source (homepage Person node) in the same cleanup pass.

- **⚠️ Possible duplicate content block:** two versions of a "Giving Back" mission-split section + schema were found on the homepage — an older and a newer iteration of the same feature, not two complementary halves of one split block (Lofty's code-block character limit is why the homepage schema is split across multiple `<script>` tags at all, but these two "Block 2" versions overlap rather than complete each other). Confirm on the live page that only one "Giving Back to Those Who Serve" section actually renders — if both are live, remove the older one and keep the version with the fuller schema (address, geo, GeoCircle areaServed, memberOf including SCWMLS, knowsAbout, 3-item award list).

- **⚠️ Two separate address rules for subdivision pages:**

  **1. No "anchor address" in Place schema.** Southbridge's Place schema includes a fabricated `streetAddress` — `"1500 Blue Ridge Trail (anchor address)"` — used only internally to calculate routing distances for the Proximity table, not a real public-facing address. Kilkenny Farms West and Six Mile Creek correctly omit it (Place schema only has locality/region/postal/country). Follow KFW/Six Mile Creek: no street address in Place schema.

  **2. No office street address in the footer or author bio.** Do NOT include "1025 Quinn Drive Ste 100" (or any office street address) on subdivision pages. Current KFW and Six Mile Creek builds have it in both the author bio ("offices at 1025 Quinn Drive — in the village") and the page footer — remove it going forward and strip it from existing pages in the cleanup pass.

  Keep instead: phone (608-669-4226), email, "Waunakee-based," city/region references, Real Broker affiliation line, MLS disclaimer link. Those carry the local-relevance signal without pinning a street address.

  **Status note:** whether a replacement office address exists is TBD. This rule is scoped to subdivision pages only for now — the master identity schema, homepage, blogs, and city hub pages are unchanged and still carry the Quinn Drive address. Revisit site-wide once the address situation is settled, and check with Real Broker (Dan Dyslin) on any brokerage advertising requirements for displaying a physical address before removing it more broadly.

### HTML page anatomy (corrected — based on Kilkenny Farms West v7, the designated reference build, cross-checked against Six Mile Creek)

**⚠️ Correction:** an earlier version of this doc documented Southbridge's structure, which uses an older collapsible-accordion pattern (`<details>`/`<summary>`, `section-collapse`). That's a **legacy/older template variant — do not replicate it.** The actual current standard, confirmed from Kilkenny Farms West v7 (the explicitly designated reference build) and matched by Six Mile Creek, uses **full static sections with no collapsing/accordion behavior at all.** Mobile responsiveness comes entirely from CSS media queries, not JS show/hide.

**Head:**
- Standard meta (charset, viewport, title, description, robots, canonical, OG tags, Twitter card)
- `og:image` / `twitter:image` pointing to a real approved CDN photo when one exists
- Geo meta tags: `geo.region` (US-WI), `geo.placename`, `geo.position`, `ICBM` — present in the most recent build (Six Mile Creek); standardize this into every new page
- Single `@graph` JSON-LD: WebPage, BreadcrumbList, Place, Person (John), Organization, FAQPage

- **Organization schema — corrected format, defined ONCE on the homepage (correcting the `@id` and `name` issues found above):**
  ```json
  {
    "@type": ["Organization", "RealEstateAgent"],
    "@id": "https://integrityhomeswi.com/#org",
    "name": "Integrity Homes",
    "legalName": "Integrity Homes of Wisconsin",
    "alternateName": ["IntegrityHomesWI"],
    "url": "https://integrityhomeswi.com/",
    "telephone": "+1-608-669-4226",
    "logo": "[homepage logo URL]",
    "founder": { "@id": "https://integrityhomeswi.com/#john" }
  }
  ```
  **On subdivision pages, don't repeat this — reference it by `@id` only:**
  ```json
  { "@id": "https://integrityhomeswi.com/#org" }
  ```
  **⚠️ Do not treat `#org`/`#john` as final without one more check.** Across this conversation, the Person node id alone has been documented three different ways (`#johnreuter`, then corrected to `#john` per a "Part B" revision note referencing a "Part A master identity"). The homepage schema appears to be actively mid-revision across multiple Lofty code blocks. Before Claude Code hardcodes any `@id` value into the stub pattern or touches existing pages, pull the actual current live "Part A" content directly (view-source or Lofty's code editor) to confirm the ids are stable, rather than trusting any single version documented here.

  Same pattern applies to the Person node — full definition once on the homepage, `@id`-only stub everywhere else. Note the homepage's fuller Organization node also carries valuable structured data subdivision pages don't currently reference at all — geo coordinates, areaServed, memberOf (NAR, WRA, SCWMLS), knowsAbout, award list. Fixing the source once means every subdivision page inherits all of that automatically — a genuine entity-clarity upgrade for GEO (Phase 7), not just a name fix.

- **🚨 HIGH PRIORITY — ROH nonprofit status text is wrong on the live homepage, confirmed:** the Reward Our Heroes Organization/NGO schema description currently reads "Nonprofit status pending IRS approval" — confirmed incorrect. ROH is an IRS-approved 501(c)(3) (EIN 39-3358820). This is a factual-accuracy issue, not just an SEO/schema-consistency one — fix this before any of the lower-priority schema cleanup items below. Check whether the same outdated "pending" language exists anywhere else on integrityhomeswi.com or rewardourheroes.com, given the ongoing ROH compliance work already underway on that site.


**Body, in order (core section set — exact sequencing has some observed variation between builds, see note below):**
1. Breadcrumb
2. Hero — badge (e.g. "🏆 2026 MABA Parade of Homes" or "Established Waunakee Neighborhood"), eyebrow, H1, intro paragraph, hero-tags (icon + short label chips), CTA buttons (View Homes for Sale / Call John). Background is a real approved photo (`background-image` + gradient overlay) when one exists; use a navy gradient placeholder with an HTML comment noting asset status ("Not Filmed") when it doesn't — do not invent a stock photo.
3. Stats strip — 4 stat boxes (navy background, gold numbers), e.g. distance to airport, distance to downtown, home price range, build era. Pick the 4 most relevant/distinctive facts for that subdivision, not a fixed formula.
4. Photo strip (**conditional** — only include if 2+ real approved photos exist beyond the hero image; Kilkenny Farms West has this, Six Mile Creek does not, since Six Mile Creek only had the one hero photo available). Skip this section entirely rather than filling it with placeholders.
5. `About the Neighborhood` — editorial two-column layout: main body copy (2fr) + sidebar fact boxes (1fr: Developer/Location, Location, [a distinguishing fact like "2026 Distinction" or "Neighborhood Feel"], Price Range or Recent Sold Range, Published/Updated date). Include one pull-quote styled as an italic blockquote.
6. `Why People Choose It` — 8-item numbered grid (01–08), evidence-based points pulling from research section J, not promotional adjectives.
7. `Schools` — school-list rows by grade band (K–4, 5–6, 7–8, 9–12) with school name + trail/distance detail. Include a 4-box district stat strip (ranking, ratio, graduation rate, etc.) when that data is confirmed and available — Kilkenny Farms West uses a distinctive purple section treatment here, which is optional styling, not a hard requirement. Always end with a "verify by address" boundary disclaimer, per Kenzie SOP verification rules.
8. `Parks & Recreation` — icon + title + description rows, most distinctive/closest amenities first.
9. `Dining & Shopping` / `Nearby Conveniences` — 3-column card grid naming specific businesses (never "shopping and dining are nearby"), plus a closing info-box summarizing the downtown/big-box picture with a link to the city guide.
10. `Proximity & Commute` — data table: destination, distance, drive time, notes. Include a routing-check caveat line.
11. `Dog Parks` — icon + title + description cards, closest first, permit info included.
12. `Market Data` — market-box: SCWMLS-sourced figures only (never Redfin/Zillow/Trulia — see Phase 1/2), with a link to the city's Market Report page. **Note:** this section's position varies between builds — Kilkenny Farms West places it after Dog Parks, Six Mile Creek places it earlier (before Commute). Either position is acceptable; just don't drop the section.
13. `FAQ` — pulls from research section M, matches the FAQPage schema entries in the head exactly.
14. Market strip — pill-style link bar (city guide, other neighborhoods, market reports, school district guide) — this is Phase 5's internal linking surface.
15. CTA band
16. ROH section (required on every page per brand standard)
17. Author band (John's bio — MRP, Ramsey Trusted, Top 5%, veteran background)
18. Explore band ("← View All [City] Neighborhoods")
19. Footer (Integrity Homes, address, phone, MLS disclaimer link, ROH link, copyright)

**Section-set consistency, not rigid ordering:** treat items 5–13 as a required *set* of sections rather than a fixed sequence — build all of them, but don't block on getting the exact order identical to any one prior page.

**Placeholder discipline:** if a hero/photo asset or specific data point isn't confirmed, say so plainly (in copy and/or an HTML comment) rather than guessing or inventing something that looks confirmed. This matches the Kenzie SOP's "verify, don't guess" rule and makes IMAGE-PENDING pages (Phase 3) easy to find and finish later.

### Tier System (two-pass, not a blocker)
- **Tier 1 (this build):** Full publish-ready page using Phase 1–4 above. Goal is speed and full coverage across the priority list.
- **Tier 2 (later enrichment pass):** Kenzie's deeper "secrets of the area" research layered into the *existing* published page. This is an update, not a rebuild — do not regenerate the whole page from scratch.

---

## Phase 5 — Interlinking & Cluster Architecture

The goal is not "add a few links" — it's making every subdivision page a connected node in the existing content system, not an island. Model: **city hub pages are the hub, everything else is a spoke.**

```
                    City Hub Page (e.g. /waunakee/)
                    /        |         \
        Market Report      Subdivision      Blog Posts
        Page (city)         Pages           (city-tagged)
                              |
                    Nearby Subdivision Pages
                    (from research section L)
```

### 5a. Link UP — subdivision page → city hub (required, every page)
Every subdivision page links to its city hub page (e.g. Southbridge → `/waunakee/`) in the intro/breadcrumb area and again in a closing "Continue Exploring" section. This already exists in the template — keep it.

### 5b. Link DOWN — city hub → subdivision page (required, and easy to forget)
This is the one that gets missed: when a new subdivision page goes live, **the city hub page must be updated too**, adding that subdivision to its neighborhood list/directory. A subdivision page that links up to a hub that doesn't link back down is a dead end for Google, not a cluster. Add this as a mandatory step, not optional: after publishing a subdivision page, edit the corresponding city hub page to add it.

### 5c. Link SIDEWAYS — subdivision ↔ nearby subdivisions
The research brief's **Section L (Comparison With Nearby Subdivisions)** already names 3–5 relevant nearby subdivisions — use that list directly:
- If a named comparison subdivision already has a published page, link to it with natural anchor text (not just the raw subdivision name every time — vary it: "nearby Westbridge," "the neighboring Southbridge community," etc.)
- If it doesn't have a page yet, note it as a linking placeholder to fill in once that page goes live (track in the build log so it gets picked up on a later pass, not forgotten)
- Known conflict/comparison pairs already discovered belong here too — e.g. the Southbridge/Westbridge FAQ distinction is itself good internal-link content ("often confused with Westbridge — here's the difference")

### 5d. Link to Market Report pages
Every subdivision page links to its city's Market Report page (from the `market-report-page` skill — one permanent URL per city) for current pricing/trend context, since the subdivision page itself only carries "pending MLS data" or builder-quoted prices, not live market stats.

### 5e. Link to/from relevant blog posts
Cross-reference `Integrity_Homes_Content_System_FINAL.xlsx` (239 posts, Blog Master tab) for posts tagged with this city or mentioning this subdivision by name.
- Link the subdivision page OUT to 2–4 relevant existing posts (buyer guides, market updates, "living in [city]" content)
- Where feasible, also add a link back INTO the subdivision page from those blog posts — this is a manual/flagged follow-up if Claude Code can't edit already-published blog HTML directly, but should be logged as a to-do, not skipped silently
- New blogs written after a subdivision page exists should link to it going forward — add "check for a matching subdivision page and link to it" as a standing step in the blog-seo-packager / blog-create workflows

### 5f. Anchor text rule
Don't repeat the exact same anchor text ("Southbridge") every time a page is linked to from elsewhere — vary it naturally ("this Waunakee neighborhood," "the Southbridge community," "nearby Southbridge") to avoid over-optimized, spammy-looking link patterns.

### 5g. Track it (cross-city only)
Within a city's same-day batch, no placeholder tracking is needed — every subdivision page linked to already exists by publish time. The only case still worth logging: a nearby-subdivision comparison (Section L) that names a subdivision in a **different city** not yet built. Log those in a running `Internal-Link-Map.md` (or a tab on the Attack Plan tracker) so they get filled in once that other city's batch runs — otherwise skip the tracking overhead entirely.

---

## Phase 6 — Reporting
After each batch, report back:
- ✅ Pages completed (with URLs)
- 🚩 Name conflicts flagged for review
- 🖼️ Pages marked `IMAGE-PENDING`
- ❓ MLS match issues that need manual resolution
- 🔗 Internal links added (city hub, nearby subdivisions, blog posts)
- ⏳ Cross-city placeholder links only (nearby subdivision comparison names a subdivision in a city not yet built — flag for later fill-in once that city's batch runs)
- 📝 City hub pages that need manual updating to link back down to new subdivision pages (Phase 5b)

---

## Phase 7 — Authority, GEO & AI-Citation Optimization

Traditional SEO and AI-citation optimization (GEO) increasingly diverge — ranking #1 on Google no longer guarantees an AI Overview/ChatGPT/Perplexity citation. What's already strong in the current template (specific stats, structured @graph schema, sourced FAQ) stays. Add the following:

### 7a. Quick-Answer block (new, required)
Add a short block immediately after the hero/stats strip — 40–60 words, definition-first, answering "what is [Subdivision] and where is it" directly and completely with no narrative wind-up. This is the passage most likely to get lifted whole into an AI answer. Style it visually distinct (e.g., a bordered callout) so it also serves human skimmers. Draft from research section A (Expert Summary), tightened to a single citable paragraph.

### 7b. Speakable schema on Quick-Answer + FAQ
Brand standard already requires "speakable selectors" on Integrity Homes blogs — extend the same `SpeakableSpecification` schema markup to the subdivision page's Quick-Answer block and FAQ section. Not yet present in the current subdivision template; add it as a standard schema node in Phase 4's `@graph`.

### 7c. Freshness policy (ties into the existing Tier 1/Tier 2 system)
`dateModified` in the schema must actually change when the page is meaningfully updated — right now it's set once at publish and never revisited. Treat these as required freshness triggers, each updating `dateModified`:
- Image swap (Phase 3, once a placeholder gets replaced)
- Tier 2 enrichment pass (Phase 4's two-pass system)
- Quarterly MLS data refresh — add this as a new standing task, not previously tracked: revisit each published subdivision page roughly every 3 months to refresh sold-price ranges and days-on-market figures from a fresh SCWMLS pull. This is the single highest-leverage recurring task for staying AI-cited over time.

### 7d. Comparison table for nearby-subdivision data
Research section L (Comparison With Nearby Subdivisions) currently feeds prose and the love-grid — add a small side-by-side comparison table (price range, lot size, HOA, schools, distance to downtown) for 2–3 of the closest comparable subdivisions. Structured comparison tables are a specifically favorable format for AI citation, beyond just being useful to a human buyer.

### 7e. External validation (separate workstream, not a page-build task)
Third-party citations of the page — not just the page's own content — are an increasingly important trust signal AI systems weigh, on top of what the page itself says. Two low-effort angles worth pursuing separately from the build pipeline:
- When a subdivision's HOA has its own website/newsletter, ask (or have Kenzie ask during Phase 1 Part 3 human-intel research) whether they'll link to the Integrity Homes neighborhood guide as a resident resource
- Local news/Chamber/community org mentions of a subdivision are worth a light outreach pass once a page is live, since third-party links function as external validation in a way on-page content can't replicate on its own

### 7f. Periodic crawler-access check
Confirm periodically (not per-page) that Lofty's bot filtering isn't inadvertently blocking AI crawlers — this was already checked and confirmed fine as of a prior conversation, but Lofty or Cloudflare-style platforms have been known to change default crawler-blocking behavior, so a periodic spot-check (e.g., quarterly, alongside the MLS refresh) is worth keeping on the calendar rather than assuming it stays fixed.

## Open Items

### ✅ Resolved this session
- [x] Research prompt — Kenzie workflow v2 (3-part: Deep Research / MLS Data / Local Intel)
- [x] Merge logic — union of coverage, not consensus voting
- [x] All three research engines automated (Claude native + Perplexity API + OpenAI API)
- [x] URL slug convention — locked, confirmed from live pages
- [x] Meta title/description format — locked, confirmed from live pages
- [x] Canonical archive location — Google Drive folder `1vs5sHKyaqkWX6omzWpy8b3dug2zz2Ald`
- [x] Master identity schema corrected — `#org` name/alternateName fixed, `#website` id fixed (was `#site`, which subdivision pages referenced but didn't exist), address + geo + areaServed consolidated into the master node
- [x] Homepage mission block corrected — jobTitle, brand name, ROH nonprofit status
- [x] Confirmed no duplicate "Giving Back" section on the live homepage
- [x] Quick-Answer block + Speakable schema designed → `subdivision-quick-answer-block.md`
- [x] Subdivision `@graph` standard with `@id`-only stubs → `subdivision-schema-standard.md`
- [x] Page anatomy corrected — static sections (KFW v7 / Six Mile Creek), NOT Southbridge's legacy accordion pattern
- [x] Cadence + cluster architecture — one city per week, same-day publish, hub-and-spoke interlinking

### 🔴 Blocking — do before the next build batch
- [ ] Set up Perplexity Sonar API key (env var)
- [ ] Set up OpenAI API key (env var)
- [ ] Roll the Quick-Answer block + Speakable schema into the NAS master template
- [ ] Roll the corrected `@graph` (`@id`-only stubs) into the NAS master template
- [ ] Update `Subdivision_Attack_Plan.xlsx` Page Status column — currently shows everything "Not Started," which is stale and will cause duplicate work

### 🟡 Cleanup on existing pages (not blocking new builds)
- [ ] Apply the corrected `@graph` to: Kilkenny Farms West, Six Mile Creek, Southbridge, Arboretum Village, Centennial Heights (+ any others in the archive)
- [ ] Remove "anchor address" `streetAddress` from Place schema (Southbridge confirmed)
- [ ] Remove "1025 Quinn Drive Ste 100" from author bio + footer on subdivision pages (KFW + Six Mile Creek confirmed)
- [ ] Add Quick-Answer block to already-published pages
- [ ] Reconcile loose top-level `Page-v1_X.html` files (Southbridge, Arboretum Village, Centennial Heights) into their proper subdivision folders

### 🔵 Recurring / ongoing
- [ ] Quarterly MLS refresh — update Market Data section AND the Quick-Answer price sentence, bump `dateModified` (Phase 7c)
- [ ] Quarterly crawler-access spot-check (Phase 7f)
- [ ] Expand the known name-conflict pairs list as more subdivisions are processed
- [ ] External validation outreach — HOA sites, local news, Chamber (Phase 7e)

### ⚪ Out of scope here — tracked elsewhere
- [ ] Site-wide address decision (new office vs. no public street address) + check Real Broker advertising requirements
- [ ] Footer text site-wide: "Integrity Homes of Wisconsin is Powered by Real Broker, LLC" — global Lofty element, not a subdivision-page issue
- [ ] Trim Block B homepage schema — geo/areaServed/knowsAbout/memberOf now duplicated in the master node
