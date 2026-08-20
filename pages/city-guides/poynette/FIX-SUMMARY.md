# Poynette page — schema fix summary

**Page:** integrityhomeswi.com/poynette/
**Fixed:** 2026-08-19
**File:** `poynette.html` in this folder (corrected version, ready to paste into the Lofty CMS source)

## What was wrong

The page's JSON-LD (`<script type="application/ld+json">` in the `<head>`) redefined
John Reuter and Integrity Homes as full `Person`/`Organization` nodes, using IDs that
don't exist anywhere else on the site:

- `https://integrityhomeswi.com/#johnreuter` (Person)
- `https://integrityhomeswi.com/#organization` (Organization)

These don't match the IDs the homepage actually defines (`#john` and `#org`). Since
nothing else on the site links to `#johnreuter`/`#organization`, those nodes were
islands — search engines and AI answer engines can't connect this page's author/publisher
back to the homepage's actual John Reuter / Integrity Homes identity.

It also meant John's bio facts (phone, jobTitle, awards, `sameAs` links) were typed out
fresh on this page instead of inheriting from the one place they're maintained — so any
future update to his bio on the homepage would silently NOT apply here, and the two
would drift out of sync over time.

## What changed

In the `Article` node (`#article`), replaced:

```json
"author": {
  "@type": "Person",
  "@id": "https://integrityhomeswi.com/#johnreuter",
  "name": "John Reuter",
  "jobTitle": "Broker/Owner",
  "worksFor": { "@type": "Organization", "@id": "https://integrityhomeswi.com/#organization" },
  "sameAs": [ ... ],
  "knowsAbout": [ ... ]
},
"publisher": {
  "@type": "Organization",
  "@id": "https://integrityhomeswi.com/#organization",
  "name": "Integrity Homes",
  "url": "https://integrityhomeswi.com/",
  "logo": { "@type": "ImageObject", "url": "https://integrityhomeswi.com/logo.png" }
},
```

with:

```json
"author": { "@id": "https://integrityhomeswi.com/#john" },
"publisher": { "@id": "https://integrityhomeswi.com/#org" },
```

Nothing else on the page changed — no visible copy, no other schema nodes, no CSS.
`WebPage`, `BreadcrumbList`, `Place`, and `FAQPage` were already correct and untouched.

## How to apply it to the live page

1. Open the Poynette page in Lofty CMS.
2. Find the `<script type="application/ld+json">` block in the page head/custom code.
3. Replace the `author` and `publisher` objects inside the `Article` node exactly as
   shown above (delete the full nested `Person`/`Organization` objects, replace with
   the two one-line `@id` stubs).
4. Save/publish, then re-validate with Google's Rich Results Test or Schema.org
   validator to confirm the `@graph` resolves cleanly.

## Standing rule (already documented in this repo)

Every page that credits John or Integrity Homes — subdivision pages, city guides,
blog posts, anything — should reference `#john` and `#org` by `@id` only, never
redefine them. See `docs/subdivision-schema-standard.md` for the full standard; it
applies here even though Poynette isn't a subdivision page. If a future page shows
this same `#johnreuter`/`#organization` pattern, it has the identical bug and the
identical fix.
