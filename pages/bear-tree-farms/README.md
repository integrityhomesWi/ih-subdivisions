# Bear Tree Farms — Page Build Notes (v1, 2026-08-17)

Source file: `pages/bear-tree-farms/bear-tree-farms-v1.html`
Research source: `research/bear-tree-farms-research.md` (Claude-leg-only merge; Perplexity leg missing — see that file's header)

## Status: Tier 1 draft, publish-ready with placeholders below unresolved

## The single biggest content decision: DeForest vs. Village of Windsor

The research brief is explicit and repeated on this point: Bear Tree Farms carries a DeForest, WI 53532 **mailing address** and is marketed by builders/portals as "DeForest, WI," but it is physically platted and governed by the **Village of Windsor** — a different municipality with its own government, ordinances, and (likely) tax rate. This is flagged in the brief as "worth clarifying explicitly with any buyer" and as a top-tier "only a local would know" hook.

Given the task's explicit URL slug (`/deforest/bear-tree-farms/`), meta title ("Bear Tree Farms DeForest WI"), and breadcrumb (Home → DeForest → Bear Tree Farms), the page keeps the DeForest URL/breadcrumb/mailing-address convention (this matches how the subdivision is actually marketed and searched for), but states the Windsor governance fact plainly and repeatedly in the hero eyebrow, hero tags, stats strip, Quick-Answer block, About section, Why-People-Choose-It grid, and the first FAQ. Nothing on the page states or implies Bear Tree Farms is legally within DeForest — that would be factually wrong per the brief.

The Place schema's `addressLocality` is set to "DeForest" (the confirmed mailing-address convention), while the Place `description` states the actual Windsor governance explicitly. This mirrors real-world practice (mailing city ≠ municipality) but is worth a second look from John before this goes live, given how central the distinction is to the brief's "possible considerations."

## How the one open numeric conflict was handled

Section C of the brief flags an **unresolved conflict**: one builder-marketing source claims construction began around 2016 ("close to 10 years"), which conflicts with the 2018 plat-recording date found in Windsor's own resolution titles. Per the task rule (don't average or pick one silently), the page **omits any single "development began in [year]" claim**. Instead, every reference to development history on the page cites only what both the brief's confirmed-via-resolution-titles data supports: "documented phases from Phase 2 through Phase 8, per Village of Windsor board records dated 2020–2025." This sidesteps the 2016-vs-2018 conflict entirely rather than surfacing it publicly or guessing.

## No sold-price / median-price / DOM data anywhere

The Market Data section is fully TBD, matching the master template's TBD pattern exactly (all 12 stat cards, "John's Take" honestly describing the gap). The Quick-Answer price sentence is explicitly hedged ("Current sale prices are pending MLS confirmation") per the four-slot template's own instruction to never substitute a public-site estimate here.

The brief's single builder-price data point (~$590K, tied to Tim O'Brien Homes) is explicitly marked in the brief as "stale/unverifiable — treat as unverified, not a current price... do not use." Per that instruction, **this figure does not appear anywhere on the page**, including in body copy, even hedged/dated as "builder-quoted" — the brief itself says not to use it, so the "builder-quoted, dated" allowance in the task instructions wasn't exercised (there was no reliable builder-quoted figure in the brief to use).

## Address rules followed

- No street address for John/Integrity Homes anywhere. Author band and footer say "Dane County-based" / "Serving Dane County, Wisconsin" instead of an office address (no Quinn Drive reference — confirmed by grep).
- No `streetAddress` field in the Place schema (confirmed by grep) — locality/region/postal/country only.
- Every named business with an address (Woodman's Food Market, both Kwik Trip locations, DeForest Area Public Library, Windsor Elementary School) uses the exact address given in the brief. Businesses without a confirmed address in the brief — Door Creek Church, Paradise Paws Doggie Day Care, Yahara River Learning Center — are mentioned narratively as part of the development's on-site commercial node (matching how the brief itself describes them: within/adjacent to the development, no street address given) rather than presented as address-carrying "Nearby Conveniences" cards. Restaurants, a standalone coffee shop, and pharmacy/healthcare were explicitly flagged "not independently confirmed with named businesses" in the brief, so none are named on the page — the Nearby Conveniences section says so directly instead of inventing or guessing at a business name.

## Dog Parks section: omitted

Per task instructions, only include a Dog Parks section if the brief names a specific dog park actually near the subdivision. The brief names no dog park near Bear Tree Farms — only Paradise Paws Doggie Day Care, which is a commercial daycare business, not a public off-leash park. The Parks section explicitly notes this ("a dog-care convenience, not a public off-leash dog park... this guide doesn't include a Dog Parks section") rather than silently dropping the topic, so it reads as a deliberate omission rather than a gap.

## Photo Strip: skipped, hero uses navy gradient placeholder

No approved photo exists for Bear Tree Farms yet (Phase 3 — IMAGE-PENDING). The hero section uses a navy gradient background (`linear-gradient` over the same design tokens) with an `IMAGE-PENDING` HTML comment, per instructions. The Photo Strip section is skipped entirely rather than filled with placeholders. `og:image` / `twitter:image` meta tags are also omitted rather than pointed at a stock or invented photo — this deviates from the master template (which has real photo URLs in those tags) but was necessary given no real photo exists; there's an HTML comment in the `<head>` flagging this for a follow-up once an approved photo lands in the Image Vault.

## Other placeholders / pending items

- **HOA annual fee**: not stated anywhere on the page (only "Yes, an HOA exists — fee not confidently verified") per the brief's explicit "do not quote without confirming" flag.
- **Geo coordinates** in the Place schema (`43.2043, -89.3361`) are an unsurveyed estimate for the Windsor Road / Pederson Crossing Blvd / US-51 area — the brief did not supply verified lat/long, and no plat map was pulled. Flag for a follow-up with an actual coordinate lookup before this is treated as final.
- **Homes-for-sale / market-report / school-district-guide URLs** (`/homes-for-sale/deforest-wisconsin/`, `/market-reports/deforest-wisconsin/`) follow the site's existing naming convention (seen on the Waunakee equivalents) but were not verified to exist yet — flag for Phase 5 interlinking cleanup once the DeForest city hub batch is built.
- **City hub link-down (Phase 5b)**: this page links up to `https://integrityhomeswi.com/deforest/`, but that DeForest city hub page needs to be manually updated to link back down to this new subdivision page — not done as part of this build.
- **John's Notes section**: left as bracketed placeholder questions (matching the master template's own draft convention) — no fabricated "insider" observations were written in John's voice, since none were available in the brief or from John directly.
- **"Fox Hill Estates"** relationship to Bear Tree Farms is unresolved per the brief ("needs verification") and is intentionally not mentioned anywhere on the page.
- **Perplexity research leg**: missing entirely (see the brief's own header). This page should be revisited once that leg is run and merged, per the brief's own recommendation not to treat this subdivision as Tier-1-complete until then.

## Validation performed

- JSON-LD `@graph` parses cleanly via `python3 -c "json.loads(...)"` (4 nodes: WebPage, BreadcrumbList, Place, FAQPage).
- FAQ schema text (`mainEntity`) programmatically diffed against the visible desktop FAQ section — exact match, all 7 Q&A pairs.
- Grep-confirmed: no "Quinn" string, no `streetAddress` field, no "$590K" or Redfin/Zillow-sourced price figures anywhere (the only "Zillow" mentions are generic marketing phrasing — "homes that haven't hit Zillow yet," "What You Won't Find on Zillow" — not sourced price data).
- Quick-Answer block word count: 86 words (within the required 60–90 range).

## Schema pattern

Follows the corrected `@id`-only stub pattern exactly: `author` references `https://integrityhomeswi.com/#john`, `publisher` references `https://integrityhomeswi.com/#org` — no Person or Organization node is redefined on this page.
