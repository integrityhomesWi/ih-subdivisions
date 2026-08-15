# IH_Subdivisions

Full code export of the Integrity Homes **Subdivisions** project — the Waunakee
short-form video package (Kilkenny Farms West & Southbridge), the Waunakee
driving-tour transcripts, the Gemini transcription script, and the complete
Integrity Homes / Reward Our Heroes skill library.

Everything here is plain text and version-controllable. Nothing depends on a
Claude Project, a chat history, or an uploaded knowledge base.

Exported: 2026-08-15
Source: `C:\Users\admin\OneDrive\Documents\Claude\Projects\Subdivisions` + synced account skills

---

## What's in here

```
IH_Subdivisions/
├── README.md                  ← you are here
├── CLAUDE.md                  ← project context Claude Code reads automatically
├── MANIFEST.json              ← machine-readable file index with provenance
├── .gitignore
│
├── content/                   ← THE SOURCE OF TRUTH (plain markdown)
│   ├── cut-sheets/            8 editor cut sheets for the six Waunakee shorts
│   ├── planning/              clip map, calendar revision, handoff plans
│   └── transcripts/           14 Gemini transcripts of raw field video
│
├── scripts/
│   └── transcribe_videos.py   batch video → timestamped transcript (Gemini API)
│
├── skills/                    18 custom Integrity Homes / ROH skills, verbatim
│
└── originals/                 the untouched .docx / .pdf files the markdown came from
```

### content/cut-sheets/

Editor instructions for building six vertical shorts from footage shot
**2026-06-16** in two Waunakee neighborhoods. No re-recording required — every
clip named is a real file in the Google Drive footage folder.

| File | Short |
|---|---|
| `READ_ME_FIRST.md` | Orientation for an editor who doesn't know Waunakee |
| `00_MASTER_...` | Clip library, local cheat sheet, short order, thumbnails |
| `01_Kilkenny_Farms_West_vs_Southbridge...` | Which one is actually you? |
| `02_If_I_Were_Building_in_Kilkenny_West...` | John's personal buyer advice |
| `03_Dont_Assume_the_Pool_in_Southbridge...` | Pool access depends on section |
| `04_Ranking_Waunakees_Parks...` | Settlers vs Tierney vs Kilkenny park |
| `05_More_Than_a_Garage_Door...` | Southbridge community feel |
| `06_Southbridge_Isnt_One_Neighborhood...` | Southbridge is an umbrella |

**Known flags** (carried over from the 2026-06-28 correction pass):

- Only **one** Dunwoody clip exists. Short 01 was written for two; both entries
  now point to the same real file. Use a second establishing shot for variety.
- There is **no** `Park-Pavilion-Amenity-Close_Horizontal` clip. A real
  Southbridge pool clip is substituted wherever it was called for.
- Shorts 05 and 06: confirm which Southbridge on-camera file actually contains
  the spoken line — several filenames look nearly identical.

### content/planning/

- `CORRECTED_Clip_Map_Real_Drive_Filenames.md` — per-short clip-by-clip map,
  verified against Drive on 2026-06-28.
- `Calendar_Revision_Summary_2026-06-28.md` — the ClickUp Social Distribution
  Calendar fix (91 market tasks relabeled so Dane County leads the month, per
  the `v1.4 Market Rotation` tab of the OPERATING_SYSTEM workbook).
- `Kilkenny_vs_Southbridge_Short_1_Handoff.md` — handoff for short 01.
- `Marketing_Video_Handoff_Plan.txt` — text extraction of the handoff PDF
  (original PDF preserved in `originals/planning/`).

### content/transcripts/

14 transcripts produced by `scripts/transcribe_videos.py`. Timestamped every
~15 seconds. `IMG_0766.md` is the longest (~6:55 Six Mile / HeyDay driving
tour). Several are near-empty — those clips had little or no speech.

### skills/

The 18 custom skills, copied verbatim with their reference files:

`blog-create` · `blog-post-writer` · `blog-seo-packager` · `brand-style-guide` ·
`email-newsletter-writer` · `instagram-caption-writer` · `integrity-blog-pipeline` ·
`listing-photo-captioner` · `listing-remarks-writer` · `lofty-blog-html-builder` ·
`market-report-page` · `mls-data-analyzer` · `price-reduction-angle-generator` ·
`reel-script-writer` · `roh-content-writer` · `roh-video-distribution` ·
`transaction-coordinator` · `transaction-email-templates`

Anthropic's built-in skills (`docx`, `xlsx`, `pptx`, `pdf`, `skill-creator`,
`morning`) are deliberately **excluded** — they ship with Claude Code and would
only add ~4 MB of noise and drift.

---

## Using this with Claude Code

```bash
cd IH_Subdivisions
git init && git add -A && git commit -m "Initial export from Claude Project"
claude
```

`CLAUDE.md` loads automatically, so Claude Code starts with the project context
without you pasting anything.

To make the skills active in Claude Code, symlink or copy them:

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)/skills/"* ~/.claude/skills/     # macOS/Linux
```

On Windows (PowerShell, as admin):

```powershell
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\blog-create" -Target "$PWD\skills\blog-create"
```

Or just `xcopy /E /I skills %USERPROFILE%\.claude\skills`.

### Running the transcriber

```bash
pip install google-genai
export GEMINI_API_KEY="..."          # PowerShell: $env:GEMINI_API_KEY="..."
python scripts/transcribe_videos.py --input-dir /path/to/videos --output-dir content/transcripts
```

Re-runs are safe — it skips any video whose `.md` already exists.

---

## What is *not* in here

These are referenced by the content but live elsewhere. Nothing in this repo
breaks without them, but you'll want the links handy:

- **Raw video footage** — Google Drive footage folder. Too large for git;
  cut sheets reference clips by filename only.
- **Integrity_Homes_OPERATING_SYSTEM workbook** — the `v1.4 Market Rotation`
  tab is the governing source for the content calendar.
- **ClickUp** — IHWI Content System → 01 Content Production → Social
  Distribution Calendar.
- **Image Vault** (Google Sheet) and **Lofty CMS** — used by the blog skills.

Consider adding a `.env.example` and a `links.md` if you want those pointers
tracked in the repo too.
