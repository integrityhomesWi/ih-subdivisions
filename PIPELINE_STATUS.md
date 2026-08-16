# Subdivision Page Pipeline — Status

Tracking doc for the new subdivision-research-and-page pipeline (separate from
the existing Kilkenny Farms West / Southbridge video package this repo
started with). Started 2026-08-16, kicked off by a request to build a
subdivision page for Arboretum Village.

## Goal

For each subdivision (Waunakee first, more cities to follow — target ~50
subdivisions total), produce a researched, sourced, publish-ready neighborhood
page establishing John as the genuine local expert. Explicitly not generic
subdivision copy or rewritten builder marketing.

## Pipeline design (three research legs → merge → page)

1. **Perplexity leg** — `research_perplexity.py`. ✅ **Built and working.**
2. **Claude leg** — Claude Code's native web search, per-subdivision. ⛔ **Not built.** No script/process exists yet; referenced in `research_perplexity.py`'s docstring as a future companion leg only.
3. **ChatGPT/OpenAI leg** — ⛔ **Not built.** No API key configured, no script.
4. **Merge/union step** — reconcile all three legs into one final brief per the "union rules" (keep all unique findings, flag only genuine conflicts). ⛔ **Not built.**
5. **Page template/HTML builder** — subdivision-page equivalent of the existing `skills/market-report-page/` skill (which only covers city-level market reports, not neighborhoods). ⛔ **Does not exist.**

**Bottom line: only step 1 of 5 is done.** Research briefs are raw material
right now, not publishable pages.

## What's working — `research_perplexity.py`

- Runs the Kenzie SOP v2 deep-research prompt against Perplexity's Sonar API.
- **Auto-chains two legs per subdivision in one command:**
  1. Full 16-section brief (development history, location/streets, schools,
     housing types, HOA, amenities, comparisons, FAQs, sources, etc.)
  2. A second, narrow **conveniences leg**, auto-anchored to the streets the
     first pass just confirmed (extracted from section D automatically — no
     manual copy-paste between commands). Explicitly guards against
     name-collision errors (e.g. a same-named subdivision/apartment complex in
     a different city) — required reading given this repo's whole reason for
     existing is the Kilkenny Farms West vs. Southbridge mixup.
- Outputs to `research/<slug>-raw-perplexity.md` and `research/<slug>-conveniences.md`.
- Batch mode: `python research_perplexity.py --batch waunakee_batch.txt` runs
  an arbitrary list of `Subdivision|City` pairs unattended.
- Sold-price/DOM data is explicitly kept out of scope — always flagged
  "pending MLS data from John," never pulled from Redfin/Zillow/Trulia.

### Quality check — Heritage Hills, Waunakee (test subdivision #1)

Ran full pipeline test 2026-08-16. Verdict: **good enough to scale, with one
caveat.**

- Strong: real named streets tied to actual plat/parcel records, real HOA
  detail (recording date, specific covenant rules) with direct source links,
  disciplined about marking things "not confident" instead of guessing,
  17 cited sources.
- First-pass weakness (now fixed): section I (nearby conveniences) came back
  vague/hedged in the big 10-part prompt. The narrower, streets-anchored
  conveniences leg fixed this — got real named businesses with addresses
  (confirmed correct by John) and caught/discarded a genuine name-collision
  result (a same-named "Heritage Hills" apartment complex in Madison).
- **Open caveat:** most named conveniences traced back to a single source —
  the builder's (Veridian Homes) own marketing page — which the prompt
  explicitly says not to rely on primarily. John spot-checked a few
  restaurant names and confirmed they're accurate, but this is a
  single-source risk worth remembering when running this at scale without
  a human reviewing every output.

## Environment / access notes

- This Claude Code environment's network access was **"Trusted" (blocked
  Perplexity) → changed to "Full" by John on 2026-08-16.** Confirmed working
  (401 auth-required response instead of a 403 proxy block) — Claude can now
  call the Perplexity API directly from this environment instead of routing
  every command through John's local PowerShell.
- `PERPLEXITY_API_KEY` — John has an active key with $50 credit balance.
  Not stored in the repo or environment variables (secrets don't belong in
  the environment's env-var block, which is visible to anyone using the
  environment). Provided per-session as needed.

## Next steps (not yet started)

1. Decide: is "the pipeline" scoped to research only, or research → merge →
   published page? (Asked John 2026-08-16, awaiting answer.)
2. If full pipeline: build the Claude leg, the ChatGPT leg, the merge/union
   logic, and a subdivision-page HTML template before running unattended at
   scale.
3. Get the actual target list of ~50 subdivisions (only 3 Waunakee test
   subdivisions + a handful of commented-out placeholders exist in
   `waunakee_batch.txt` today — nowhere near the full target list).
4. Re-test the conveniences leg's single-source issue on a subdivision with
   less builder-marketing coverage, to see if the pattern holds or if
   Heritage Hills was a best-case (Veridian happens to publish an unusually
   detailed neighborhood page).
