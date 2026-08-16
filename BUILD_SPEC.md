# Subdivision Pipeline — Build Spec for Local Claude Code

This is the handoff doc. Build/execution work moves to Claude Code running
locally at `C:\Users\admin\Documents\ih-subdivisions` (real filesystem access,
no file-download round-trips, can run/see errors/fix in a loop). This repo's
cloud session (`claude/ih-subdivisions-zi5j95`) stays the design/spec/decision
space — read `PIPELINE_STATUS.md` first for what's already built and tested.

**To start:** open Claude Code in that folder, `git pull`, paste this file's
contents (or just say "read BUILD_SPEC.md and start on the Claude leg") and go.

---

## Architecture recap

```
Perplexity leg  ──┐
Claude leg      ──┼──► merge/union step ──► subdivision page (HTML)
ChatGPT leg     ──┘        (per subdivision)
   (optional/future)
```

Each leg researches the same subdivision independently and writes its own
file, so a questionable claim can always be traced to which leg introduced
it. The merge step reconciles them — it does not re-research.

**Status:** Perplexity leg is built, tested (Heritage Hills), and works.
Everything below this line is unbuilt as of 2026-08-16.

---

## 1. Claude leg

**Goal:** same research depth as the Perplexity leg, using Claude Code's own
`WebSearch`/`WebFetch` instead of the Perplexity API — a second, independent
pass so systematic gaps in one search engine's index don't become blind spots
in the final brief.

**Reuse, don't reinvent the prompt.** `research_perplexity.py`'s
`PROMPT_TEMPLATE` and `CONVENIENCES_PROMPT_TEMPLATE` constants are
API-agnostic research instructions — they don't mention Perplexity anywhere
except the file's own docstring/output naming. Reuse them verbatim as the
brief Claude Code answers via its own tools, so the two legs are actually
comparable (same 16 sections, same "verify don't guess," same MLS/Redfin
exclusions, same name-collision discipline).

**Build:**
- A script or slash-command-style workflow that, given `Subdivision` + `City`:
  1. Runs the equivalent of the main brief (sections A–P) via `WebSearch`/`WebFetch`.
  2. Runs the equivalent of the conveniences leg, anchored to the streets
     confirmed in step 1 — same auto-chaining behavior as the Perplexity
     script already does (see `extract_streets_context()` in
     `research_perplexity.py` for the pattern — section D extraction via
     regex on the markdown headers).
  3. Writes `research/<slug>-raw-claude.md` and `research/<slug>-conveniences-claude.md`,
     matching the Perplexity leg's file-header format (model/date/tokens-if-knowable,
     "not a finished brief" merge note) so downstream tooling can treat all
     legs uniformly.
- Batch-capable the same way: read `waunakee_batch.txt` (or whatever the
  current target list file is), loop unattended.

**Open question to resolve in Claude Code, not here:** does per-subdivision
web search burn meaningful budget/time at 50x scale? Decide whether to run
this leg for every subdivision or only ones where the Perplexity leg came
back thin/single-sourced (see Heritage Hills' single-source caveat in
`PIPELINE_STATUS.md`) — that's a real cost/thoroughness tradeoff worth
surfacing to John rather than deciding silently.

---

## 2. ChatGPT/OpenAI leg

**Status: in progress as of 2026-08-16** — John is setting up the OpenAI API
now. Same reusable prompt templates apply (`PROMPT_TEMPLATE` /
`CONVENIENCES_PROMPT_TEMPLATE` from `research_perplexity.py`, verbatim).

Build a `research_openai.py` mirroring `research_perplexity.py`'s shape as
closely as possible — same CLI surface (`subdivision city`, `--batch FILE`,
auto-chained conveniences leg via the same `extract_streets_context()`
pattern, same file-header format), swapping only the API call
(`https://api.openai.com/v1/chat/completions` or the Responses API,
whichever John's key/tier supports — check current OpenAI API docs, this
repo's script was written against Perplexity's schema and needs adapting,
not copy-pasting).

Env var convention to match: `OPENAI_API_KEY`.
File convention: `research/<slug>-raw-chatgpt.md` / `research/<slug>-conveniences-chatgpt.md`.

Don't block the rest of the pipeline on this finishing — design the merge
step (below) to work with 2 legs present now and gracefully pick up a 3rd
once this lands.

---

## 3. Merge / union step

**Input:** all available leg files for one subdivision (2 today, 3 once
ChatGPT leg exists). **Output:** one `research/<slug>-merged.md`.

**Rules (from the original prompt's own "union rules" language, made
concrete):**

1. Walk section-by-section (A through P — same structure all legs already share).
2. **Same fact, multiple legs agree** → keep once, note it's cross-confirmed
   (this is a genuine confidence signal — surface it, don't just discard the
   duplication silently).
3. **Same fact, legs disagree** (e.g. different HOA due amounts, different
   street lists) → do NOT silently pick one. Show both, cite both sources,
   flag as a conflict John needs to resolve. This mirrors the "identify
   conflicting information instead of choosing one version silently" rule
   already baked into the research prompt itself.
4. **Fact appears in only one leg** → keep it, but carry forward a
   single-source flag *especially* when that one source is developer/builder
   marketing (this is exactly the Heritage Hills conveniences caveat —
   don't lose that signal in the merge).
5. **"Not confident" / "pending MLS data from John" labels never get
   stripped or silently resolved during merge.** If one leg guessed where
   another correctly flagged uncertainty, the flag wins — never the guess.
6. Preserve every leg's Sources section in the merged output (don't
   deduplicate away a URL just because two legs both cite it — that's useful
   corroboration info).
7. Re-run (or manually re-check) the name-collision guard across the merged
   set — a collision one leg caught and discarded should stay discarded, not
   quietly reappear via another leg that didn't have the same guard.

**Build this as a script, not a one-off manual pass** — at 50 subdivisions
manual merging doesn't scale and reintroduces exactly the babysitting problem
this whole restructuring is trying to kill.

---

## 4. Consistency / schema checks

Before a merged brief is allowed to feed the page builder, it should pass:

- [ ] All sections A–P present (a leg failing entirely shouldn't silently
      produce a thin merged file with no indication a leg is missing).
- [ ] No sold-price / median-price / days-on-market figures present unless
      explicitly sourced from an SCWMLS export John supplied — everything
      else must read "pending MLS data from John."
- [ ] HOA dues either sourced with a citation or explicitly flagged
      not-confirmed — never a bare number with no source.
- [ ] School assignments carry the "verify at address level" caveat — never
      stated as guaranteed.
- [ ] Every named business/street/date has at least one citation.
- [ ] Name-collision "Discarded" section present and reviewed (not just
      generated and ignored).
- [ ] At least one fact in each major section is NOT sourced solely to
      developer/builder marketing — if it is, that's a flag for John to
      spend 10 minutes verifying before publish, not a silent pass.

This can be a script (grep for the required headers/flags, fail loud if
missing) or a checklist Claude Code walks through per subdivision — script
preferred once the pattern is proven on a few by hand.

---

## 5. Page template

**Does not exist yet.** Closest existing pattern in this repo:
`skills/market-report-page/SKILL.md` — Lofty CMS-ready HTML, inline CSS,
JSON-LD schema, speakable classes, sticky CTA bar. That skill is built for
city-level *market data* pages that overwrite monthly; a subdivision page is
evergreen neighborhood content, not a monthly data refresh, so don't just
copy it — adapt the *conventions* (Lofty compatibility, schema markup,
mobile-first CTA) to a neighborhood-guide structure.

**Suggested section mapping** (merged-brief section → public page section —
confirm with John before building, this is a proposal not a decision):

| Merged brief section | Goes on public page? |
|---|---|
| A. Expert Summary | Yes — intro |
| B. Quick-Facts Table | Yes — condensed |
| C. Development/Phase History | Yes — shortened |
| D. Location/Streets/Boundaries | Yes — with map |
| E. Schools | Yes, with "verify at address level" caveat kept visible |
| F. Housing Products | Yes |
| G. HOA/Restrictions | Yes — high buyer-relevance |
| H. Parks/Trails/Amenities | Yes |
| I. Nearby Conveniences | Yes — this is the section we just fixed |
| J. What Residents Value | Yes |
| K. Possible Considerations | Yes — credibility, not spin |
| L. Comparison With Nearby Subdivisions | Maybe — could be its own linked page |
| M. FAQs | Yes — also feeds schema markup |
| N. "Only a Local Would Know" | Content-idea backlog, not page copy directly |
| O. Missing Info John Should Verify | **No — internal only, never publish** |
| P. Sources | Maybe footnoted, maybe omitted from public page but kept in source file |

---

## Open decisions still needed from John (don't guess these in Claude Code)

1. Research-only pipeline, or full research → merge → published-page pipeline?
   (Asked, not yet answered as of this doc's last update.)
2. The actual target list of ~50 subdivisions + cities.
3. Run the Claude leg for every subdivision, or only where Perplexity's
   single-source risk shows up?
4. Confirm/adjust the page-section mapping table above before any HTML gets built.

## File/naming conventions (keep consistent across all legs + merge)

```
research/<slug>-raw-perplexity.md
research/<slug>-conveniences.md              (Perplexity leg's conveniences — existing name, unchanged)
research/<slug>-raw-claude.md
research/<slug>-conveniences-claude.md
research/<slug>-raw-chatgpt.md               (once built)
research/<slug>-conveniences-chatgpt.md      (once built)
research/<slug>-merged.md
```

`slug` = same `slugify()` function already in `research_perplexity.py`
(lowercase, hyphenated, apostrophes dropped) — reuse it, don't reimplement.
