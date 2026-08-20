# Project context — IH_Subdivisions

Read this before working in this repo.

## Who / what

John Reuter, Integrity Homes (integrityhomeswi.com), Dane County, Wisconsin.
Also runs the Reward Our Heroes Foundation (rewardourheroes.com).

This repo is the **Subdivisions** project: a short-form video package for two
Waunakee neighborhoods, plus the transcript pipeline and the full skill library
that produces Integrity Homes content.

## The two neighborhoods — do not conflate them

This is the single most important fact in the repo, and it is easy to get wrong:

- **Kilkenny Farms West** — a newer, separate Waunakee subdivision. Active
  construction, open lots, buyer choice of floor plan and lot, rural views,
  school/trail access.
- **Southbridge** — an established Waunakee area that is an *umbrella* over
  multiple sections. Mature trees, parks, pools, community feel.
- **"Kilkenny section of Southbridge"** — a section *within* Southbridge.
  **Not** the same thing as Kilkenny Farms West. Mixing these two up is the
  error the cut sheets exist to prevent.

Pool access in Southbridge depends on the section/address. Never state pool
access as a blanket Southbridge amenity.

## Ground rules

1. **`content/` is the source of truth.** `originals/` is the archived .docx and
   .pdf the markdown was converted from — reference it, don't edit it.
2. **Clip filenames are literal.** Every clip named in a cut sheet is a real
   file in the Google Drive footage folder. Do not invent, guess, or "fix" a
   filename. Kilkenny clips are prefixed `2026-06-16_Kilkenny-Farms-West...`;
   Southbridge clips are prefixed `2026-06-XX_Southbridge...`. Two naming
   styles, same folder — that's expected.
3. **Respect the correction flags.** Cut sheets were verified against Drive on
   2026-06-28. Any line marked `FLAG` is unresolved; see README for the three
   open ones. Don't silently resolve a flag.
4. **No re-record.** The whole package is built to use existing footage only.
5. **Brand voice** lives in `skills/brand-style-guide/`. Apply it to anything
   client-facing.
6. **Schema identity IDs are settled.** Every page crediting John or Integrity
   Homes references `#john` / `#org` by `@id` only — never redefines a full
   Person/Organization node. See `docs/HOMEPAGE-IDENTITY-IDS.md` before ever
   questioning this again; Drive docs on this topic can be stale.

## Skills

`skills/` holds 18 custom skills, verbatim. They are the real behavior spec for
Integrity Homes content — treat them as source, not documentation. Notable
routing rules baked into them:

- Ad-hoc blog → `blog-create` (orchestrates writer → SEO packager → HTML builder)
- Scheduled weekly market/pillar content → `integrity-blog-pipeline`
- Anything for rewardourheroes.com → `roh-content-writer`, never `blog-post-writer`
- Monthly per-city market page → `market-report-page` (one permanent URL per
  city, overwritten monthly; six cities: Madison, Sun Prairie, DeForest,
  Verona, Waunakee, Middleton)

## External dependencies (not in this repo)

| Thing | Where | Used by |
|---|---|---|
| Raw video footage | Google Drive footage folder | all cut sheets |
| Integrity_Homes_OPERATING_SYSTEM workbook | Google Sheets, `v1.4 Market Rotation` tab | blog pipeline, calendar |
| Social Distribution Calendar | ClickUp → IHWI Content System → 01 Content Production | calendar revision |
| Image Vault | Google Sheet | blog SEO packager |
| Lofty CMS | lofty.com | blog HTML builder |
| `GEMINI_API_KEY` | env var | `scripts/transcribe_videos.py` |

## Conventions

- Dates in filenames and content: `YYYY-MM-DD`.
- Transcripts are named after the source video stem (`IMG_0766.md`) and start
  with `# Transcript: <original filename>`.
- Timestamps in transcripts: `[mm:ss]`, roughly every 15s and at speaker changes.
- Never commit API keys, client PII, or raw video.
