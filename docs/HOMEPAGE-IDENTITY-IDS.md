# Homepage Identity IDs — Standing Rule

**Status: SETTLED. Do not re-open without new evidence from the live site itself.**

This question came up more than once in the same session and wasted real time each
time. This doc exists so it never has to be re-litigated from scratch again.

## The answer

Every page that credits John Reuter or Integrity Homes — subdivision pages, city
guides, blog posts, anything — references the homepage's identity nodes by `@id`
only. Never redefine a full `Person` or `Organization` node on a content page.

```json
"author": { "@id": "https://integrityhomeswi.com/#john" },
"publisher": { "@id": "https://integrityhomeswi.com/#org" }
```

| Node | Correct `@id` | Wrong / stale `@id` |
|---|---|---|
| Person (John Reuter) | `#john` | ~~`#johnreuter`~~ |
| Organization (Integrity Homes) | `#org` | ~~`#organization`~~ |

That's it. Both nodes are defined once, in full, on the homepage itself (in the
Lofty CMS script area). Every other page just points at them.

## How this was verified (2026-08-20)

This was checked against the **actual live Lofty homepage source**, pasted directly
into chat by John — not a Drive doc, not a repo doc, not an inference. Two things
confirmed it:

1. The homepage's middle-section code block, which literally states in its own
   change-log comment: `✅ @id values unchanged from your Part A-matching version
   (#org, #john, rewardourheroes.com/#org)`.
2. The actual JSON-LD in that same paste: `"founder":{"@id":"https://integrityhomeswi.com/#john"}`.

Both the hero/identity block (Part A) and the mission/impact block (Part B) agree:
`#john` and `#org`.

## Why this got confused in the first place

A **stale Drive doc** ("Home Page Schema," last modified January 2026, well before
the `#john`/`#org` correction was made on the live site) still shows the old
`#johnreuter`/`#organization` pattern. That doc predates the fix and was never
updated after. A newer Poynette page draft (`poynette-v1_3.html`) was apparently
built referencing that same stale doc, which is why it also shipped with
`#johnreuter`/`#organization` despite being created in August.

**The lesson:** Drive docs can go stale silently. If this question ever comes up
again, the only source that settles it is the actual live Lofty homepage script —
not a Drive doc, not this repo's own docs, not a page that "looks like" it should
be a reference. Ask John to paste the current homepage `<script type="application/
ld+json">` block directly, or view-source the live site, before touching any
identity ID.

## Checklist for any new or fixed page

- [ ] `author` is `{ "@id": "https://integrityhomeswi.com/#john" }` — nothing else
- [ ] `publisher` is `{ "@id": "https://integrityhomeswi.com/#org" }` — nothing else
- [ ] No full `Person` or `Organization` node defined anywhere on the page
- [ ] No `worksFor`, `jobTitle`, `sameAs`, `telephone`, etc. duplicated from the
      homepage's Person/Organization nodes — those live on the homepage only
- [ ] Grep the file for `#johnreuter` and `#organization` — both should return zero
      hits before calling a page done

## Related docs

- `docs/subdivision-schema-standard.md` — the full corrected `@graph` structure
  this rule is part of (Place, BreadcrumbList, FAQPage, speakable, etc.)
- `docs/SUBDIVISION-PAGE-BUILDER-README.md` — Phase 4b QA process, which should
  include the grep check above on every page before it ships
