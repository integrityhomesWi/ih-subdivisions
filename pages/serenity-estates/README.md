# Serenity Estates — Page Build Notes

**Output:** `serenity-estates-v1.html`
**Source research:** `research/serenity-estates-research.md` (merged Perplexity + Claude legs, retrieved 2026-08-16/17; OpenAI leg not run — no API key configured)
**Template scaffold:** `templates/kilkenny-farms-west-v8-MASTER-TEMPLATE.html` (CSS, tokens, section anatomy, schema pattern reused as-is)
**Built:** 2026-08-17

## What's placeholder / pending

- **Hero image:** No approved photo exists in the Media Vault yet. The hero uses a navy CSS gradient (no image URL), flagged with an `<!-- IMAGE-PENDING -->` HTML comment in two places (head og:image note, hero section). `og:image` / `twitter:image` meta tags were omitted entirely rather than pointing at a stock photo.
- **Photo Strip section:** Skipped entirely — the template rule requires 2+ real approved photos to include it, and zero exist for this subdivision.
- **Dog Parks section:** Omitted entirely. The research brief only confirms Token Creek County Park generally (a park, not a dog park) and does not name a specific dog park serving Serenity Estates. Reusing Kilkenny Farms West's Waunakee dog parks (Ripp Park, Yahara Heights) would have been wrong — wrong city, wrong subdivision.
- **Market Data section:** Every field (sale price range, median, average, sales count, active/pending, DOM, list-to-sale ratio, high/low sale, total volume) is `TBD`. No SCWMLS export has been pulled for this subdivision yet. This includes the Sale Price Range card, which in the KFW template carries a real figure — here it stays TBD per the critical rule that builder-quoted pricing cannot substitute for MLS data in the Market Data section specifically (it appears elsewhere, in body copy, clearly labeled "builder-quoted").
- **John's Notes section:** Left as bracketed prompts for John to fill in his own words (lot position on wetland-adjacent lots, the Turn Key Construction builder question, HOA dues/management, and the Serenity Estates vs. The Reserve comparison) — matches the pattern already used in the KFW v8 template for un-filled insider notes.
- **Proximity & Commute table:** Almost entirely unrouted. The research brief itself flags every drive-time figure as a marketing-sourced or unrouted estimate. Only two rows carry any time figure (East Madison ~10 min, Prairie Lakes ~5 min), both explicitly labeled "marketing-quoted, unrouted." The rest of the destinations (Woodman's, downtown Sun Prairie, Highway 51 on-ramp, MSN airport) are shown as "Not routed" rather than inventing a plausible-sounding number.
- **HOA dues, management company, current build-out/remaining lot inventory:** Not in the research brief; not stated anywhere on the page.
- **Turn Key Construction** as a possible third builder is presented as unconfirmed everywhere it appears (Why People Choose It does not claim it; FAQ and John's Notes flag it explicitly).

## Content decisions that weren't purely mechanical

- **Lot size range:** The research brief has an unresolved conflict — Perplexity found ~0.21–0.41 acres, Claude found ~0.222–1.234 acres, and the brief explicitly says not to average or pick one, and not to surface the internal conflict itself on the public page. **I omitted lot size entirely as a standalone claim on the page.** Neither a "starting around a quarter acre" phrasing nor any acreage-per-lot figure appears anywhere in hero copy, stats strip, About section, or FAQ. The only acreage figures used are the plat-wide totals both sources agree on without conflict (35.22 acres total, ~18 acres dedicated open space, both Claude-sourced with high confidence and not disputed by Perplexity). This is more conservative than the brief's suggested "lots starting around a quarter acre" language — I judged that even that hedged framing implies a size claim per-lot that isn't cleanly sourced, and the plat-wide open-space stat is the stronger, better-sourced, more distinctive number anyway.
- **Amanda Avenue:** Not mentioned anywhere as an entrance to Serenity Estates, per the brief's explicit flag that it's more likely associated with the neighboring Reserve development. It does appear once, correctly, as a boundary reference for The Reserve in the FAQ answer distinguishing the two subdivisions.
- **"Serenity Court":** Not used as a confirmed street name anywhere on the page (brief flags it as found in only one land-listing source). The About section and sidebar only list streets confirmed by both research legs or via a specific parcel record: Stonehaven Drive, St. Patrick's Way, Lonnie Court, Lonnie Lane.
- **Metro Market (Ironwood):** Left out of Nearby Conveniences. The address was found by only one research leg (Perplexity) and not corroborated by Claude — treated the same as other single-source, unconfirmed-address items per the "leave it out rather than including a shaky claim" rule, even though the store's general existence was found by both legs.
- **Walmart Supercenter:** Left out — the brief explicitly flags the address as unconfirmed.
- **Schools:** Presented as a district assignment (Sun Prairie Area School District, high confidence) plus an inference-labeled elementary/middle/high chain (Token Springs Elementary, Patrick Marsh Middle, Sun Prairie East), with the inference status stated in the row copy itself, not just a footnote — matches the requirement that the "verify by address" caveat be visible on the page, not only internal metadata. Sun Prairie East vs. West is explicitly called "probable," not stated as fact.
- **Pricing:** Every price figure on the page is labeled "builder-quoted" with the August 2026 date attached, and every instance is paired with a note that sold-price/median/DOM data is pending SCWMLS — including in the Quick-Answer block, About sidebar, Why People Choose It item 08, and FAQ. No figure from the research brief's specific listings ($799,900 / $1,395,000) was used, since those are individual listing prices, not a subdivision-level range, and using them risked implying more precision than the brief supports.
- **Geo coordinates:** The Place schema uses an approximate lat/long (43.203, -89.207) and ZIP 53590 for north Sun Prairie near Token Creek. This is a general map-pin estimate for schema purposes (consistent with how other pages in this project handle Place geo), not a claim sourced from the research brief, and does not function as a street address.

## Facts verified against the JSON-LD

- JSON-LD parses as valid JSON (Python `json.loads` check passed).
- All 9 visible FAQ question/answer pairs match the `FAQPage` schema `mainEntity` entries exactly, word for word (verified programmatically).
- `Organization` and `Person` nodes are not redefined on this page — only referenced by `@id` (`#org`, `#john`), per the corrected schema standard.
- `Place` schema has no `streetAddress` field — locality/region/postal/country only.
- No street address for John/Integrity Homes appears anywhere (footer says "Waunakee-based," no "Quinn Drive" or any office street address).
