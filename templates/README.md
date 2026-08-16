# NAS Master Template

`kilkenny-farms-west-v8-MASTER-TEMPLATE.html` — the corrected reference build.

Source: pulled from Google Drive (`kilkenny-farms-west-v7 (1).html`, canonical
archive folder), then updated per the two "blocking" items in
`docs/CLAUDE-CODE-BRIEFING.md`:

1. **Quick-Answer block added** — CSS + HTML, inserted immediately after the
   stats strip, per `docs/subdivision-quick-answer-block.md`. Uses the
   worked Kilkenny Farms West example verbatim from that spec.
2. **Corrected `@graph` schema** — per `docs/subdivision-schema-standard.md`:
   - `author` now references `#john` (was `#johnreuter`, which doesn't
     resolve against the master identity script)
   - `publisher` added, referencing `#org`
   - The full Person and Organization nodes are no longer redefined on the
     page — both are `@id`-only references now, so they'll inherit
     whatever's correct on the homepage once that's fixed there
   - Added `about` (ties WebPage to the Place node) and `speakable`
     (targets `.qa-question`, `.qa-speakable`, `.faq-q`, `.faq-a`)
   - `dateModified` bumped to reflect this edit

**Not done here, and still blocking per the briefing:** the homepage's own
master identity script (Lofty global Script area) still needs the `#org`
name/alternateName fix and the ROH nonprofit-status text fix. Until that's
live, `#org` and `#john` references from this template resolve to whatever
the homepage currently says — which the briefing documents as still wrong
(`"Integrity Homes Wisconsin"`, `"Nonprofit status pending IRS approval"`).
That's a Lofty CMS edit, not something fixable from a static HTML file.

**Not pushed back to Drive/Lofty.** This lives in the repo for review first —
uploading it as the new source of truth for the NAS template, or applying it
to the live Kilkenny Farms West page, is a separate, deliberate step once
John confirms the changes look right.

## Still needed for other pages

Every other subdivision page (Six Mile Creek, Southbridge, Arboretum
Village, Centennial Heights, Heritage Hills v2, etc.) still has the old
schema pattern and needs the same cleanup pass — see the checklist in
`docs/subdivision-schema-standard.md`.
