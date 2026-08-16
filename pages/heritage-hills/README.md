# Heritage Hills — Schema Cleanup Pass

`heritage-hills-v3-SCHEMA-CLEANED.html` — pulled from the Drive archive
(`heritage-hills-page-v2.html`, published 2026-08-04) and brought up to the
corrected schema standard from `docs/subdivision-schema-standard.md` and
`docs/subdivision-quick-answer-block.md`. This is a cleanup pass on an
already-researched, already-drafted page — no re-research was done, per
Phase 1b (the existing brief's content, including the quarry disclosure,
Phase 8/9 status, and HOA dues, is real and was left untouched).

## What changed

1. **Schema `@graph`:**
   - `author` → `#john` (was `#johnreuter`, doesn't resolve)
   - `publisher` added, referencing `#org`
   - Full Person and Organization nodes deleted — both now `@id`-only,
     inheriting from the (now-corrected, per John) homepage master script
   - Added `about` (ties WebPage to the Place node) and `speakable`
   - `dateModified` bumped to 2026-08-16
2. **Quick-Answer block added** (was entirely absent) — CSS + HTML per spec,
   inserted after the stats strip.
3. **Quinn Drive address removed** from both the author bio and the footer,
   per the subdivision-page address rule.

## What's intentionally left alone / flagged, not fixed

- **Quick-Answer price sentence has no dollar figure.** SCWMLS data for
  Heritage Hills hasn't been supplied yet — the sentence honestly says so
  and points to John's phone number instead of a guessed range. There's an
  HTML comment at that spot flagging it as the first thing to update once
  MLS data lands (this is also the quarterly-refresh trigger going forward).
- **Everything else on the page** (FAQ content, stats, body copy) is
  untouched — it was already good, sourced research (quarry disclosure with
  a specific Village Board hearing date, $240.65/year HOA dues, Phase 8/9
  status). Confirmed this is meaningfully better and more specific than the
  Claude-leg/OpenAI-leg research run earlier in this session, which is why
  Phase 1b (check the archive first) matters.

## Not done

Same caveat as the master template: this file is not pushed back to Drive
or Lofty. It's here for review before anything goes live.
