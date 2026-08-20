# Subdivision Page Schema — Corrected `@graph` Standard

The subdivision page schema, corrected to reference the master identity nodes by `@id` instead of redefining them. Use this structure on every new build and when cleaning up existing pages.

> **The `#john`/`#org` IDs below are settled — see `docs/HOMEPAGE-IDENTITY-IDS.md` for the verification trail before ever second-guessing this again.**

**What changed and why:**

| Issue | Before | After |
|---|---|---|
| Organization node | Full node redefined on every page (`#organization`), properties drifting between builds | `@id`-only reference to `#org` |
| Person node | Full node redefined on every page (`#johnreuter` — an id that doesn't exist in the master script) | `@id`-only reference to `#john` |
| `isPartOf` | Pointed to `#website`, which didn't exist (master script used `#site`) | Points to `#website` — master script corrected to match |
| Place `address` | Some pages had a fabricated `streetAddress` ("anchor address") | Locality/region/postal/country only, no street address |
| Speakable | Absent | Added to the WebPage node |

The net effect: the Organization's full property set — address, geo, areaServed, knowsAbout, memberOf (NAR, WRA, SCWMLS), awards, sameAs links, subOrganization links to Reward Our Heroes and The Veteran Realtor Podcast — all now inherit automatically from one source. Fix it once on the homepage, every subdivision page reflects it.

---

## The corrected `@graph` (worked example: Kilkenny Farms West)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/#webpage",
      "url": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/",
      "name": "Kilkenny Farms West Waunakee WI | Neighborhood Guide | Integrity Homes",
      "description": "The complete guide to Kilkenny Farms West in Waunakee, Wisconsin — schools, parks, saltwater pool, trails, dining, commute times, and what buyers need to know.",
      "inLanguage": "en-US",
      "isPartOf": { "@id": "https://integrityhomeswi.com/#website" },
      "breadcrumb": { "@id": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/#breadcrumb" },
      "about": { "@id": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/#place" },
      "datePublished": "2026-04-25",
      "dateModified": "2026-08-16",
      "author": { "@id": "https://integrityhomeswi.com/#john" },
      "publisher": { "@id": "https://integrityhomeswi.com/#org" },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": [".qa-question", ".qa-speakable", ".faq-q", ".faq-a"]
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://integrityhomeswi.com/" },
        { "@type": "ListItem", "position": 2, "name": "Waunakee", "item": "https://integrityhomeswi.com/waunakee/" },
        { "@type": "ListItem", "position": 3, "name": "Kilkenny Farms West", "item": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/" }
      ]
    },
    {
      "@type": "Place",
      "@id": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/#place",
      "name": "Kilkenny Farms West",
      "description": "A newer residential neighborhood in the southern corridor of Waunakee, Dane County, Wisconsin. Saltwater pool, trail system, beer garden shelter, and walkable access to downtown Waunakee.",
      "geo": { "@type": "GeoCoordinates", "latitude": 43.178, "longitude": -89.455 },
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Waunakee",
        "addressRegion": "WI",
        "postalCode": "53597",
        "addressCountry": "US"
      },
      "containedInPlace": {
        "@type": "City",
        "name": "Waunakee",
        "containedInPlace": { "@type": "AdministrativeArea", "name": "Dane County, Wisconsin" }
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://integrityhomeswi.com/waunakee/kilkenny-farms-west/#faq",
      "mainEntity": [
        { "@type": "Question", "name": "[Question text — must match the visible FAQ on the page exactly]", "acceptedAnswer": { "@type": "Answer", "text": "[Answer text — must match the visible FAQ answer]" } }
      ]
    }
  ]
}
</script>
```

---

## Template pattern

Replace the bracketed values. Everything else stays byte-identical across pages.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://integrityhomeswi.com/[city]/[slug]/#webpage",
      "url": "https://integrityhomeswi.com/[city]/[slug]/",
      "name": "[Subdivision] [City] WI | Neighborhood Guide | Integrity Homes",
      "description": "[Meta description — 1 sentence, 2-3 distinguishing facts]",
      "inLanguage": "en-US",
      "isPartOf": { "@id": "https://integrityhomeswi.com/#website" },
      "breadcrumb": { "@id": "https://integrityhomeswi.com/[city]/[slug]/#breadcrumb" },
      "about": { "@id": "https://integrityhomeswi.com/[city]/[slug]/#place" },
      "datePublished": "[YYYY-MM-DD]",
      "dateModified": "[YYYY-MM-DD]",
      "author": { "@id": "https://integrityhomeswi.com/#john" },
      "publisher": { "@id": "https://integrityhomeswi.com/#org" },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": [".qa-question", ".qa-speakable", ".faq-q", ".faq-a"]
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://integrityhomeswi.com/[city]/[slug]/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://integrityhomeswi.com/" },
        { "@type": "ListItem", "position": 2, "name": "[City]", "item": "https://integrityhomeswi.com/[city]/" },
        { "@type": "ListItem", "position": 3, "name": "[Subdivision]", "item": "https://integrityhomeswi.com/[city]/[slug]/" }
      ]
    },
    {
      "@type": "Place",
      "@id": "https://integrityhomeswi.com/[city]/[slug]/#place",
      "name": "[Subdivision]",
      "description": "[1-2 sentences — character, location within city, defining features]",
      "geo": { "@type": "GeoCoordinates", "latitude": [lat], "longitude": [lng] },
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "[City]",
        "addressRegion": "WI",
        "postalCode": "[ZIP]",
        "addressCountry": "US"
      },
      "containedInPlace": {
        "@type": "City",
        "name": "[City]",
        "containedInPlace": { "@type": "AdministrativeArea", "name": "Dane County, Wisconsin" }
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://integrityhomeswi.com/[city]/[slug]/#faq",
      "mainEntity": [ /* Questions — must match visible FAQ text exactly */ ]
    }
  ]
}
</script>
```

---

## Rules

1. **Never redefine Organization or Person on a subdivision page.** Reference `#org` and `#john` by `@id` only. If a property needs changing (phone, address, award, jobTitle), it changes once on the homepage and propagates everywhere.

2. **No `streetAddress` in the Place node.** Locality, region, postal code, country only. No "anchor address" — that was an internal routing reference, not a public address.

3. **FAQ schema must match visible page text exactly.** Schema markup that doesn't correspond to on-page content is a structured-data violation, and mismatches between the two are a real risk when the page and schema get edited at different times.

4. **`dateModified` must actually change** when the page is meaningfully updated — image swap, Tier 2 enrichment, quarterly MLS refresh. A `dateModified` frozen at publish date undercuts the freshness signal (Phase 7c).

5. **Added `about` and `publisher`** — neither was on the prior pages. `about` explicitly ties the WebPage to the Place it describes, and `publisher` connects the page to the organization. Both are entity-clarity signals that cost nothing to include.

---

## Cleanup checklist for existing pages

Per page:
- [ ] Delete the full Organization node, replace with `{ "@id": "https://integrityhomeswi.com/#org" }` where referenced
- [ ] Delete the full Person node, replace `author` with `{ "@id": "https://integrityhomeswi.com/#john" }`
- [ ] Change `isPartOf` target to `#website`
- [ ] Remove `streetAddress` from the Place node if present (Southbridge confirmed)
- [ ] Add `about`, `publisher`, and `speakable` to the WebPage node
- [ ] Update `dateModified`
- [ ] Remove "1025 Quinn Drive Ste 100" from the visible author bio and footer (separate from schema — see README)

Known pages needing this: Kilkenny Farms West, Six Mile Creek, Southbridge, Arboretum Village, Centennial Heights, plus any others in the Drive archive.
