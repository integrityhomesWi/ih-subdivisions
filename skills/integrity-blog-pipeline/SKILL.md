---
name: integrity-blog-pipeline
description: "End-to-end weekly blog automation for Integrity Homes. Reads the OPERATING_SYSTEM workbook (Strategic Overview, Daily Blog Spine, Blog Distribution), pulls the weekly topic from the Daily Blog Spine, researches current market data, writes the blog using Blog Post Writer, formats it to gold-standard HTML using Lofty Blog HTML Builder, selects an approved image from the Image Vault, generates a Lofty metadata sheet for the CMS, and produces the full distribution package (GBP from approved templates + v1.1 patch, Reels script, IG/FB captions, Nextdoor, Reddit, YouTube Short, optional carousel). Use when John asks to create a blog, write a weekly blog, publish a blog, do blog content, run the blog pipeline, or anything related to blog creation and Lofty publishing for integrityhomeswi.com. Also trigger when John mentions Lofty blog, market report blog, Living in guide, lifestyle guide, blog distribution, Lofty metadata, weekly content pipeline, or content automation."
---

# Integrity Homes Weekly Blog Pipeline (v6)

End-to-end weekly blog workflow — from topic to published Lofty draft to full distribution package. Chains existing skills in the Integrity Homes content system and reads the OPERATING_SYSTEM workbook for distribution tier, authority tag, and brand separation rules.

## Reference docs — read these first via Google Drive MCP

Before writing anything, read these files from the `0 - Skills & Systems` folder (Drive folder ID: `1Fq1IupOP6qGyHyOtmEor_BZJ0rEVmTQe`):

| File | Drive ID | What it covers |
|---|---|---|
| `brand-voice.md` | `1gGEYNpOvpkS8_98RdeQGcPXp4BywBgRb` | Voice rules, banned phrases, phones, colors, brand separation, Fair Housing |
| `blog-structure.md` | `1WiVoWeN0fMNgaBNWaEQ-lKDZulsg-UNk` | Scoring formula, metadata bundle, blog week vs video week counter rules, confirm-Drive-folder rule |

These are the single source of truth for voice and scoring. If anything below conflicts, the reference docs win.

---

## What's new in v6 (2026-05-28 patch)

- **Drive IDs patched.** The two canonical workbooks are now the only Drive sources:
  - `Integrity_Homes_OPERATING_SYSTEM_2026-05-26.xlsx` — file ID `113NVFTaJ6e1GUILrKeySxA0eTWg1_LNw`. Holds Strategic Overview, Daily Blog Spine (replaces the standalone 12-week plan), Blog Distribution, Asset Library, GBP/Carousel indexes, ROH Moments, Weekly Audit.
  - `Integrity_Homes_MASTER_2026-05-26.xlsx` — file ID `1Ir1WDR_IjjRWNRmRGNvVhCyqV2PAXVVd`. The 30-tab warehouse — Blog Master, Site Pages, Content Strategy, Video Library, Semrush, Changelog.
- **Retired references stripped:** old Master Content Operating System (`117n4878IzWNeTJsaWW1W4osTyLNsovV-`), old Content System FINAL (`16f3_lyxVGhxunHeSw5i4-_sgPRe9FhEO`), standalone `IWHI_12_Week_Plan.xlsx` (`12MeQJDdi_cjJUaDJEFZeXGaR-NV9cUcM`), "Updated Documents" folder (`1XkAG-Mik0oQfu66Av67NhiHx191tBprO`), and "Market Updates" folder (`1FKR1nqX2rCAszpqWYyM7FKxUNT-1rrP6`) — all confirmed 404 in Drive and removed from this skill.
- **Skill invocation fixed.** Step 6.0 no longer references the unresolvable `/mnt/skills/user/...` paths. Skills are now invoked by name (`lofty-blog-html-builder`, `brand-style-guide`), which is environment-portable.
- **Monthly market PDFs:** new home is `/1 - Integrity Homes/4 - Content/6 - Market Reports/{YYYY-MM}/{city}/`. Folder convention is undecided (City/{YearMonth}.pdf vs. Year/Month/{City}.pdf) — Step 3a handles both and flags if the file can't be located.

## What's new in v5

- **Hard read-skills requirement before HTML generation** (Step 6): Lofty Blog HTML Builder and Brand Style Guide MUST be invoked fresh on every run. No HTML may be generated from memory or interpretation.
- **Quality grep rebuilt to match the actual gold standard** (Step 7): validates the four exact speakable class names, single `@graph` JSON-LD with seven entities, `<details>` FAQ accordion, canonical link, OG and Twitter Card meta, all required CSS variables, brand fonts loaded.
- **Naming convention corrected**: "Integrity Homes" is the brand name in all visible copy. "Integrity Homes of Wisconsin" is the legal name and appears ONLY in JSON-LD `legalName` field or legally required disclosures. "Integrity Homes Wisconsin" (no "of") is forbidden everywhere. This is the wrong form Google and AI sometimes invent.
- **Brand consistency enforced**: Brand Style Guide is the single source of truth for colors (`#002850` navy / `#C9A84C` gold), fonts (Playfair Display + Source Sans 3), and naming.
- **Image Vault rebuilt (2026-05-28)** — new all-brands, all-media catalog at file ID `1-7adErt886OpAjwBQB7APudowaLBQX8e6GwER32GJK0`. Single Master tab + 15 auto-populated view tabs (Brand, City, Hero Profession). Step 8 updated accordingly. Old vault `1AjrZWvFRfcHQSjMd3rUQqIM83FD0Laqp` retired.

## What's new in v4

- Reads the framework workbook at the start to get rules (Strategic Overview, Daily Blog Spine, Blog Distribution tab) before writing
- GBP distribution copy is pulled from `GBP_Copy_Templates.docx` and the v1.1 patch is applied automatically (no more generating GBP from scratch). NOTE: as of v6, the clean GBP template bank is still being drafted; Step 10 falls back to generating from structure when templates are unavailable.
- Carousel asset added as a conditional output (when distribution tier calls for it), referencing `Carousel_Design_System.html` for design tokens. NOTE: as of v6, the Carousel Design System html does not yet exist; Step 10 falls back to the reproduced tokens.
- Hard ROH brand separation enforced (no 608-492-0515 on IH content; IH→ROH co-mention only, never reverse)
- Final status report includes Human/AI authority tag (HUMAN-REQUIRED / HUMAN-PREFERRED / HYBRID / AI-OK) for the weekly audit

---

## Voice & Brand

Read `brand-voice.md` (Drive ID: `1gGEYNpOvpkS8_98RdeQGcPXp4BywBgRb`) for the full voice, tone, naming, punctuation, emoji, and brand separation rules. Apply them across every step and every output of this pipeline.

Quick reference for pipeline use:
- **Brand name in visible copy:** "Integrity Homes" only. Legal name "Integrity Homes of Wisconsin" = JSON-LD `legalName` field only. "Integrity Homes Wisconsin" (no "of") is forbidden everywhere.
- **No em dashes.** Use periods, commas, or parentheses.
- **No emojis** in any output unless explicitly requested.
- **ROH brand separation:** Never use ROH phone (608-492-0515) on IH content. IH→ROH co-mention only, never reverse.

## Prerequisites — Existing Skills Required

- **brand-voice.md** (Drive): Voice, tone, colors, banned phrases, compliance rules. Read first — do not rely on memory.
- **brand-style-guide** (skill): Typography, web functional colors, authority signals, CTA defaults.
- **mls-data-analyzer**: For interpreting any uploaded market data.
- **blog-post-writer**: Writes the blog content.
- **lofty-blog-html-builder**: Converts blog content to gold-standard HTML.

If any skill isn't installed, read the corresponding files and follow inline.

---

## Pipeline Steps

Execute in order. Each step depends on the previous.

---

### Step 0: Read the OPERATING_SYSTEM Workbook

**Source:** Google Sheets file ID `113NVFTaJ6e1GUILrKeySxA0eTWg1_LNw`
**File:** `Integrity_Homes_OPERATING_SYSTEM_2026-05-26.xlsx`

Read this once at the start of every pipeline run. It is the framework everything else operates within.

**Tabs to load (in order of importance for the blog pipeline):**

1. **Strategic Overview** — the 4-level Human/AI authority tagging rules, format mix, ROH brand separation rules, sustainability check
2. **Daily Blog Spine** — maps blog day (Mon-Sat) → blog type → default distribution level → authority tag. ALSO holds the rolling weekly topic schedule (replaces the retired standalone 12-week plan).
3. **Blog Distribution** — the A/B/C tagging matrix that determines social treatment per blog type
4. **Asset Library** — repurposing recipes per blog type (which assets to produce from a Listicle vs. Hyper-Local vs. Case Study, etc.)
5. **GBP Copy Bank Index** — pointer to the (in-progress) `GBP_Copy_Templates.docx` used in Step 10
6. **Carousel Inventory** — pointer to the (in-progress) `Carousel_Design_System.html` used in Step 10 if carousel is called for

**How to access:** Use `read_file_content` on file ID `113NVFTaJ6e1GUILrKeySxA0eTWg1_LNw`. The whole workbook returns as text; pull the tab content needed at each downstream step.

**What to remember from this read:**

- The **Daily Blog Spine** tells you, given the day of the week, what default distribution tier (A/B/C) and authority tag (HUMAN-REQUIRED / HUMAN-PREFERRED / HYBRID / AI-OK) apply. Defaults below — override only if a specific row in the spine explicitly tags differently.

  | Day | Blog Type | Default Tier | Authority Tag |
  |-----|-----------|-------------|---------------|
  | Mon | Listicle | C | AI-OK |
  | Tue | Buyer/Seller Education | B | HUMAN-PREFERRED |
  | Wed | Listicle (often local) | C | AI-OK (B if tied to featured market) |
  | Thu | Hyper-Local Insight | A | HUMAN-REQUIRED |
  | Fri | Listicle (weekend prep) | C | AI-OK |
  | Sat | Case Study | A | HUMAN-REQUIRED |

- The **ROH Brand Separation Rules** — load these now and apply throughout the run:
  - Never use ROH phone (608-492-0515) on Integrity Homes content
  - ROH content uses Foundation address (1025 Quinn Drive Ste 100) and EIN 39-3358820
  - Co-mention from IH → ROH only. Never the reverse.
  - CNN/HNG/AF.mil placement rules apply per existing standards

These are checked again in Step 7 quality review.

---

### Step 1: Pull the Weekly Blog Topic

**Primary source:** the **Daily Blog Spine** tab in the OPERATING_SYSTEM workbook (file ID `113NVFTaJ6e1GUILrKeySxA0eTWg1_LNw`, already loaded in Step 0).

This is the rolling content schedule. Read the current week's row for topic, working title, city, content type, distribution tier (Tier A/B/C), and post location.

**How to access:**
- Already in memory from Step 0. Re-read the Daily Blog Spine tab specifically and locate the row for today's date / current week.
- Or open via Claude in Chrome at `https://docs.google.com/spreadsheets/d/113NVFTaJ6e1GUILrKeySxA0eTWg1_LNw`

**What to extract for this week:**
- Day of week + week number
- Content Type (Listicle / Buyer-Seller Education / Hyper-Local Insight / Case Study)
- Topic / Working Title
- City / Area
- Market Tier (A/B/C)
- Primary Post Location

**If the working title is blank** (some Thursday Hyper-Local and Saturday Case Study rows are intentionally left open), ask John for the angle before continuing.

**Note:** The Market Rotation logic is for the *monthly market update* schedule (Nerd Pages, Pillar Blogs, Overview Hubs), not for this weekly pipeline. Don't cross-check it here.

**Output of this step:** Topic, target market area, blog role (= Content Type), distribution tier, day of week, and any notes. Also derive the authority tag from the Daily Blog Spine table in Step 0.

---

### Step 2: Pull Internal Linking Data

**Source:** `Integrity_Homes_MASTER_2026-05-26.xlsx` — file ID `1Ir1WDR_IjjRWNRmRGNvVhCyqV2PAXVVd`

The warehouse. Tracks all existing blogs, pages, URLs, and internal linking strategy in dedicated tabs. Determines which hyperlinks weave into the blog body and sidebar.

**How to access:**
- `read_file_content` on file ID `1Ir1WDR_IjjRWNRmRGNvVhCyqV2PAXVVd`
- Or via Claude in Chrome at `https://docs.google.com/spreadsheets/d/1Ir1WDR_IjjRWNRmRGNvVhCyqV2PAXVVd`

**Tabs that matter for this step:**
- **Blog Master** — every published blog URL + title + topic tags
- **Site Pages** — every market report page, guide, landing page
- **Content Strategy** — internal linking notes and category groupings

**Extract:**
- All existing blog post URLs and titles
- All page URLs (market reports, guides, landing pages)
- Internal linking notes / categories
- Which content is most relevant to the current blog topic

Keep available for Step 5 (cross-referencing) and Step 6 (sidebar links).

---

### Step 3: Research Current Market Data

**Data source priority (use in order; fall through only when prior is unavailable):**

1. **Market Reports folder** in Google Drive (raw monthly PDF reports — primary)
2. **Most recent monthly Nerd Page** for the city (interpreted/published statistics)
3. **John-provided MLS data** uploaded directly in conversation
4. **External sources** (SCWMLS, Redfin, Realtor.com, Freddie Mac, NAR) for macro data only

---

#### 3a. Market Reports Folder (Primary)

**Location:** `/1 - Integrity Homes/4 - Content/6 - Market Reports/` in John's Google Drive.

The legacy "Market Updates" folder (ID `1FKR1nqX2rCAszpqWYyM7FKxUNT-1rrP6`) has been retired. Files now live under the new content tree. The exact intra-folder cadence is still being finalized — two patterns may appear:

- **Year-Month pattern:** `6 - Market Reports/{YYYY-MM}/{city}/{city}-{YYYY-MM}.pdf`
- **City-first pattern:** `6 - Market Reports/{city}/{YYYY-MM}.pdf`

Try both before falling through.

**7 PDFs per month expected** (6 cities + Dane County rollup):
- Dane County (rollup)
- Madison
- Sun Prairie
- DeForest
- Verona
- Waunakee
- Middleton

**Filename matching — be flexible:**
1. Case-insensitive (`madison` = `Madison` = `MADISON`)
2. Punctuation-flexible (`Sun Prairie` = `Sun-Prairie` = `SunPrairie`)
3. Spelling-flexible for known variants (`DeForest` = `Deforest`)
4. Year/month-flexible (`2026-05`, `May-2026`, `May2026`, `05-2026` all = May 2026)

**Algorithm:**
1. Locate the month folder using either pattern above
2. For each PDF, normalize filename to lowercase + strip punctuation, check if it contains the target city name (also normalized)
3. If exactly one match, use it
4. If multiple, prefer the one also containing month + year string
5. If zero matches, fall through to Nerd Page (Step 3b) and flag the gap

**City normalization:** Madison → `madison`; Sun Prairie → `sunprairie`/`sun-prairie`; DeForest → `deforest`; Verona → `verona`; Waunakee → `waunakee`; Middleton → `middleton`; Dane County → `danecounty`/`dane-county`.

**How to find the file:**
1. Determine the data month. Convention: blogs published in May 2026 reference April 2026 sold data (last full closed month).
2. Use `google_drive_search` with `title contains` queries to locate the city PDF under `/4 - Content/6 - Market Reports/`.
3. Pull the city PDF — and also the Dane County rollup PDF if the blog needs county-wide context.

**How to read:**
- All PDFs. Use the `pdf` skill or `web_fetch`.
- Each contains: median sold price, average DOM, active inventory, list-to-sale ratio, new listings, closed sales, charts.
- Extract only what's relevant to the blog topic. Don't dump the whole PDF.

**Why primary:** these are the source documents the Nerd Page is built from. Working from them gives you the same numbers plus subdivision-level and price-bracket cuts that may not appear on the published Nerd Page.

---

#### 3b. Nerd Page (Secondary)

**URL pattern:** `https://integrityhomeswi.com/[city-slug]-wisconsin/[month-year]/`

Examples: `madison-wisconsin/may-2026/`, `sun-prairie-wisconsin/may-2026/`, `deforest-wisconsin/may-2026/`, `verona-wisconsin/may-2026/`, `waunakee-wisconsin/may-2026/`, `middleton-wisconsin/may-2026/`.

**Slugs:** `madison`, `sun-prairie`, `deforest`, `verona`, `waunakee`, `middleton`.

**Month-year:** lowercase, hyphenated to year (`may-2026`). Report month is one ahead of data month (May 2026 page = April 2026 sold data). If current-month Nerd Page returns 404, fall back to previous month and flag.

**When to use:** Market Reports folder unreachable, or you need a published interpretation, or you need a clean canonical link target.

**The current-month Nerd Page is also a mandatory internal link in every blog with community statistics**, regardless of where the raw data came from.

---

#### 3c. John-Provided MLS Data

If John uploads MLS data directly, treat as authoritative for that dataset. Use the `mls-data-analyzer` skill.

---

#### 3d. External Sources

External only for: macro data (national rates, Freddie Mac PMMS, NAR), cross-city comparisons, breaking news, context beyond Dane County.

Never use external for community-level statistics.

---

#### 3e. Citation & Linking Rules

- Every community-level statistic must be traceable: Market Reports → Nerd Page → John-provided → cited external
- Current month's Nerd Page must be linked when community statistics appear
- Use "approximately" or "about" for numbers that may shift week-to-week
- Never fabricate
- For Dane County market guides, prioritize internal data over external

Also check `https://integrityhomeswi.com/market-reports/` for Market Overview Hub pages — link to the relevant one.

---

### Step 4: Write the Blog Content

**Invoke: `blog-post-writer` skill.**

Feed:
1. Blog type (= Content Type from Step 1)
2. Market area (from Step 1)
3. Target audience (from Step 1, or ask)
4. Keywords (derive from topic + location)
5. Data (from Step 3)
6. CTA (default: "Call or text me at 608-669-4226" or context-appropriate)

Follow Blog Post Writer's full structure: snippet answer → hook intro → body with H2/H3 → FAQ (4-6 Qs for schema) → Reward Our Heroes footer → CTA.

**Apply `brand-voice.md` rules (read from Drive — do not rely on memory):**
- Voice: laid-back, knowledgeable, data-driven, relatable, not salesy
- Avoid all banned phrases listed in brand-voice.md
- Include: specific neighborhood names, data points, John's authority signals where appropriate
- Fair Housing: no school ratings, no demographics

**ROH Footer (the Reward Our Heroes section in every IH blog):**
- IH → ROH co-mention is allowed. Mention ROH the Foundation, link to rewardourheroes.com.
- Do NOT include the ROH phone (608-492-0515) anywhere on the IH blog.
- Use the IH phone (608-669-4226) and IH address (1025 Quinn Drive Ste 100, Waunakee, WI 53597) on the IH blog.

**Output:** complete blog content in markdown with suggested meta title and description.

---

### Step 4B: Special Case — "Living in [Area]" Lifestyle Guides

**Trigger if any of the following:**
- Blog role from Step 1 is "Lifestyle Guide"
- Working title starts with "Living in"
- Topic is framed as a community/area overview rather than market or transaction

**Override the standard structure with this 8-section framework.**

**H1 pattern:** "Living in [Area Name], WI: What It's Actually Like in 2026"

**Sections** (each as `.spot-card` or `.card`):
1. **The Vibe** — community feel, who lives here, daily life
2. **Schools** — district name, key schools (no ratings — Fair Housing)
3. **Commute & Location** — drive times to Madison, Epic Systems, UW campus, Dane County Regional Airport
4. **Parks, Trails & Outdoor** — specific named places
5. **Coffee, Dining & Local Spots** — 3-5 named places
6. **Housing & What You Get** — typical price range, home styles, lot sizes (current MLS)
7. **Who Loves It Here** — 3-4 buyer personas
8. **Fit Test: Whether [Area] Fits You** — connects lifestyle to housing decision

**Mandatory MLS pull:** every Living-in guide cites the most recent monthly Nerd Page for the city. Pull median sold price, average DOM, active inventory. Cite Nerd Page inline. Link to both the Nerd Page and the city's Market Overview Hub.

**Mandatory internal links:**
- Most recent monthly Nerd Page for that city
- City's Market Overview Hub
- At least 2 related neighborhood/lifestyle blogs

---

### Step 5: Cross-Reference Internal Links

Using Step 2 data:

1. **Identify 5-8 relevant internal links** from the warehouse tabs related to topic
2. **Weave them naturally:**
   - Inline within body paragraphs
   - Inside callout boxes
   - In FAQ answers where relevant
3. **Select 6-8 sidebar links:**
   - Always include "See Homes Before They List" featured (coming soon for target area)
   - Relevant market report page
   - Dane County Market Hub (`https://integrityhomeswi.com/market-reports/`)
   - Madison Homebuyer Guide (for buyer content): `https://integrityhomeswi.com/first-time-homebuyer-guide-madison-wi`
   - 2-4 related blog posts
   - "Get My Home Value" (`https://integrityhomeswi.com/evaluation`) for seller content
4. **2-3 external links** to authoritative sources (Freddie Mac, Redfin, Realtor.com, NAR) per Blog Post Writer requirements

---

### Step 6: Format to Gold-Standard HTML

**Invoke: `lofty-blog-html-builder` skill.**

#### 6.0 — HARD REQUIREMENT: Invoke the spec skills fresh before generating

**Before generating any HTML, you MUST invoke these two skills fresh on every pipeline run** (using the Skill tool with the skill names — do not rely on remembered output from a prior conversation):

1. `lofty-blog-html-builder`
2. `brand-style-guide`

**This is non-negotiable.** Do not generate HTML from memory, from a prior conversation, or from interpretation of what you think the spec says. The skills are the source of truth and they may have been updated.

After invoking, confirm in your working notes:
- Navy hex (must be `#002850`)
- Gold hex (must be `#C9A84C`)
- Headings font (must be Playfair Display)
- Body font (must be Source Sans 3 or Inter)
- The four exact speakable class names (`.speakable-intro`, `.speakable-answer`, `.speakable-summary`, `.speakable-conclusion`)
- The seven JSON-LD `@graph` entities (Organization, Person, WebSite, WebPage, BlogPosting, BreadcrumbList, FAQPage)
- Organization name = "Integrity Homes" (NOT "Integrity Homes Wisconsin")
- Organization legalName = "Integrity Homes of Wisconsin"

**If any of these don't match what the skill says when you invoke it, the skill wins.** Update your working values to match.

#### 6.1 — Generate the HTML

Feed `lofty-blog-html-builder`:
1. Blog title (H1)
2. Meta description (under 155 chars)
3. Slug (lowercase, hyphenated)
4. Featured image alt text
5. Body content
6. FAQ
7. Sidebar internal links from Step 5
8. Schema.org markup (single `@graph` array with all seven entities — Organization, Person, WebSite, WebPage, BlogPosting, BreadcrumbList, FAQPage)
9. Speakable selectors using the four exact class names

**Output:** complete HTML ready for Lofty — except hero image URL, still placeholder (`[VAULT_URL]`).

---

### Step 7: Quality Review (Gold-Standard Grep)

Before pulling vault image, run this grep-based validation against the full HTML. **All checks must pass before proceeding to Step 8.** When a check fails, fix it and re-run the grep.

#### 7.1 — Brand naming (corrected v5)

- `grep -c "Integrity Homes Wisconsin"` (no "of") → **must equal 0**. This is forbidden everywhere. If found, replace with "Integrity Homes" (visible copy) or "Integrity Homes of Wisconsin" (legal contexts only).
- `grep -c "Integrity Homes of Wisconsin"` → **allowed only inside JSON-LD `legalName` field**. If found anywhere else (body, meta, alt, hero, footer, signature, CTA, sidebar, author card), replace with "Integrity Homes."
- `grep -c "Integrity Homes"` → must be present multiple times (brand name in body, signature, schema `name` field).
- `grep -c '"legalName": "Integrity Homes of Wisconsin"'` → **must equal 1** (in the Organization JSON-LD entity).

#### 7.2 — Brand colors and fonts (must match Brand Style Guide)

- `grep -c "#002850"` → must be ≥ 1 (navy CSS variable). If `#0A1628` or `#1a3a5c` appears, the HTML was built from outdated cache — regenerate after re-invoking skill.
- `grep -c "#C9A84C"` → must be ≥ 1 (gold CSS variable). If `#C8960C` or `#c9a961` appears, regenerate.
- `grep -c "Playfair Display"` → must be ≥ 1 (in `<link>` tag and CSS `h1, h2, h3, h4` rule).
- `grep -c "Source Sans 3"` → must be ≥ 1 (in `<link>` tag and CSS `body` rule).
- `grep -c "Cormorant Garamond"` → **must equal 0** in blog HTML (this is for carousels, not blogs).
- `grep -c "Jost"` → **must equal 0** in blog HTML.

#### 7.3 — Speakable classes (four exact names)

All four must appear at least once each:
- `grep -c 'class="speakable-intro"'` → must be ≥ 1
- `grep -c 'class="speakable-answer"'` → must be ≥ 1
- `grep -c 'class="speakable-summary"'` → must be ≥ 1
- `grep -c 'class="speakable-conclusion"'` → must be ≥ 1

Generic `.speakable` class without one of the four suffixes is wrong. If found, regenerate.

#### 7.4 — JSON-LD @graph schema (single block, seven entities)

- `grep -c '"@graph"'` → **must equal 1**. Single block, not three separate scripts.
- Every required entity present (search for the @id values):
  - `grep -c '"@id": "https://integrityhomeswi.com/#org"'` → ≥ 1 (Organization)
  - `grep -c '"@id": "https://integrityhomeswi.com/#john"'` → ≥ 1 (Person)
  - `grep -c '"@id": "https://integrityhomeswi.com/#site"'` → ≥ 1 (WebSite)
  - `grep -c '"@type": "WebPage"'` → ≥ 1
  - `grep -c '"@type": "BlogPosting"'` → ≥ 1
  - `grep -c '"@type": "BreadcrumbList"'` → ≥ 1
  - `grep -c '"@type": "FAQPage"'` → ≥ 1 (only if FAQ section is present)
- `grep -c '"@type": "RealEstateAgent"'` → **must equal 0**. John is `Person`, not RealEstateAgent.
- `grep -c '"speakable"'` → ≥ 1 (SpeakableSpecification on WebPage entity).

#### 7.5 — HTML structure (gold-standard required elements)

- `grep -c '<link rel="canonical"'` → **must equal 1**.
- `grep -c 'property="og:'` → must be ≥ 4 (og:title, og:description, og:image, og:url at minimum).
- `grep -c 'name="twitter:'` → must be ≥ 3 (twitter:card, twitter:title, twitter:description at minimum).
- `grep -c '<details>'` → must be ≥ 1 if FAQ present. FAQ uses `<details>/<summary>` accordion, NOT `<h3>` headers.
- Visible breadcrumb navigation present (Home › Blog › Post).
- Hero section with eyebrow pills, hero subtitle, byline with publish/modified dates.

#### 7.6 — Author block credentials (must include all)

The author card must reference at least:
- Broker/Owner (NOT "The Veteran Realtor")
- MRP designation
- Ramsey Trusted Real Estate Advisor
- Brokered by Real Broker, LLC (Broker Dan Dyslin)
- Top 5% of Realtors, seven consecutive years OR 2024 RASCW Good Neighbor Award
- Retired USAF veteran reference

#### 7.7 — Phone, address, ROH brand separation

- `grep -c "608-492-0515"` → **must equal 0** (ROH phone never on IH content).
- `grep -c "608-669-4226"` → must be ≥ 1 (IH phone is the contact phone).
- `grep -c "608\\.669\\.4226"` → **must equal 0** (Brand Style Guide uses hyphens, not periods).
- `grep -c "1025 Quinn Drive"` → must be ≥ 1 (correct address).
- ROH co-mention check: if "Reward Our Heroes" appears, confirm it's IH→ROH (passing reference, not page-dominant).

#### 7.8 — Content rules (brand-voice.md)

- `grep -c "—"` (em dash) → **must equal 0**. Use periods, commas, or parentheses.
- `grep -ciE "nestled|boasts|dream home|must.see|in today's market"` → **must equal 0**.
- No emojis (icons inside `.pill-local` excepted).
- All community-level statistics must have a source link (current-month Nerd Page or external citation).
- No fabricated data points.
- Fair Housing compliant (no school ratings, no demographic claims).

#### 7.9 — SEO

- Meta title under 60 characters (count from `<title>` tag content).
- Meta description under 155 characters.
- Primary keyword in headline, meta description, first paragraph.
- City name in H1 and first sentence.
- City mentioned 3+ times with natural variations.
- 5-8 internal links naturally placed.
- 2-3 external authoritative links (Freddie Mac, Redfin, Realtor.com, NAR).

#### 7.10 — Date formatting

- Dates in JSON-LD use ISO 8601 with Central timezone: `2026-05-10T08:00:00-05:00` (CDT) or `-06:00` (CST).
- `datePublished` and `dateModified` both present on BlogPosting entity.

**If any check fails, fix and re-run the entire Step 7 grep before proceeding.**

---

### Step 8: Select Hero Image From the Vault

The Integrity Homes Image Vault is the homemade DAM. Image bytes live on hidden Lofty pages (city pools + brand pools); the catalog is the **Integrity Homes Image Vault** Google Sheet — all-brands, all-media, rebuilt 2026-05-28 with a Master tab plus 15 auto-populated view tabs (Brand, City, Hero Profession).

#### 8a. Open the vault

**File ID:** `1-7adErt886OpAjwBQB7APudowaLBQX8e6GwER32GJK0`
**URL:** `https://docs.google.com/spreadsheets/d/1-7adErt886OpAjwBQB7APudowaLBQX8e6GwER32GJK0/edit`

Use Claude in Chrome with `get_page_text`, or `read_file_content` via the Drive MCP.

**Schema (14 columns on Master tab):** Asset ID | Brand | Media Type | City | Hero Profession | Category | Season | Source | Topic/Description | Filename | CDN URL | Date Added | Last Used | Notes

**Tab structure:**
- **Master** — every asset, single source of truth, EDIT HERE ONLY
- **Brand views (3):** Integrity Homes, ROH, Shared — auto-populated by FILTER, READ-ONLY
- **City views (6):** Madison, Sun Prairie, DeForest, Verona, Waunakee, Middleton — auto-populated, READ-ONLY
- **Hero Profession views (6):** Military & Veterans, Law Enforcement, Firefighters, EMS, Healthcare, Teachers — auto-populated, READ-ONLY

**For IH blog hero-image picks:** read the city view tab for the blog's primary city (Sun Prairie, Waunakee, DeForest, Madison, Middleton, Verona). For cross-city or brand-level assets, filter Master where City=N/A or read the **Shared** view. There is no "Cross-Cutting" tab in the new schema — that concept maps to Brand=Shared or City=N/A on Master.

**Brand handling:** Shared-tagged assets auto-appear in both the Integrity Homes view and the ROH view, so John's headshot (`SHARED-PHOTO-0001`) and any other cross-brand asset is reachable from either workflow.

**Old IDs preserved:** every row's prior vault ID (MAD-001, SP-004, DEF-010, etc.) lives in the Notes column for audit trail. Use the new Asset ID (`IH-PHOTO-####`, `SHARED-PHOTO-####`, etc.) for any new logging or references.

#### 8b. Select best-fit image

Match topic to **Category** column: Downtown / Subdivisions / Parks & Trails / Coffee & Dining / Aerials / Seasonal / Lifestyle / Brand / Headshot.

**Rules:**
- Match the **Season** column to the season the blog publishes in (Spring/Summer/Fall/Winter/All-Season)
- Avoid images with a "Last Used" date within the past 30 days
- Living-in guides → Lifestyle or Downtown
- Listicles → match topic literally
- Market data → Aerials or Downtown
- Hero spotlight blogs → filter to the matching Hero Profession view

#### 8c. Insert the CDN URL

1. Copy CDN URL from "CDN URL" column (column K on Master)
2. Replace `[VAULT_URL]` in HTML — updates `og:image`, `twitter:image`, `<img>` src, `BlogPosting.image` JSON-LD
3. Update alt text to match image subject

#### 8d. Log the use

Find the row for the selected asset on the **Master tab** (use Asset ID or CDN URL to locate it). Update the **"Last Used"** column (column M) to today's date. The city/brand/profession views will reflect the update automatically through the FILTER formulas. Do NOT try to edit a view tab — they are READ-ONLY and any direct edit will be wiped on the next view refresh.

#### 8e. If no suitable vault image

1. Generate via Nano Banana 2 (Gemini 3.1 Flash Image, model `gemini-3.1-flash-image-preview`) at `https://aistudio.google.com`
2. Prompt template:
   ```
   A photorealistic editorial photograph for a real estate blog hero image.
   Subject: [specific scene tied to topic and city]
   Style: warm natural light, slight golden hour glow, shallow depth of field,
   editorial photography, magazine-quality, no people in foreground unless
   lifestyle requires it.
   Composition: centered subject, breathing space at top, clear horizon line.
   Mood: calm, credible, locally rooted, neighborly.
   Setting: Wisconsin / Dane County visual cue — Midwestern architecture,
   mature trees, sidewalks with character, four-season feel.
   Avoid: text, logos, watermarks, fake-looking AI faces, oversaturated colors,
   generic suburbia stock imagery, palm trees, mountains.
   Aspect ratio: 16:9
   Resolution: 1280x720
   ```
3. Download. Rename per project file naming convention: `{YYYY-MM-DD}_{city-slug}_{topic-slug}_blog-cover.jpg`
4. Upload to appropriate hidden vault page in Lofty
5. Copy CDN URL
6. **Add new row to the Master tab** of the vault Sheet with the new schema:
   - **Asset ID:** next sequential `IH-PHOTO-####` (or `SHARED-PHOTO-####` if cross-brand, `IH-LOGO-####` if a brand asset)
   - **Brand:** IH / ROH / Shared
   - **Media Type:** Photo / Video / Graphic / Logo
   - **City:** matching city or N/A
   - **Hero Profession:** N/A unless hero-themed
   - **Category:** Downtown / Aerials / Lifestyle / etc.
   - **Season:** matching season
   - **Source:** Nano Banana (when AI-generated)
   - **Topic/Description, Filename, CDN URL:** as generated
   - **Date Added:** today
   - **Last Used:** leave blank (8d updates it next blog)
   - **Notes:** any context worth keeping
7. Return to Step 8c

The vault grows organically on the Master tab. Every generation becomes a permanent reusable asset visible automatically in the relevant view tabs.

---

### Step 9: Publish Draft in Lofty

Use Claude in Chrome. John's credentials are saved.

**9a.** Navigate to Lofty → CMS → blog management → "Create New Blog Post"

**9b.** Switch to HTML/code view, paste complete HTML (image already inserted from Step 8)

**9c.** Set metadata in Lofty:
- Title
- URL slug (canonical from Step 6)
- Category/tags
- Author: John Reuter
- Featured image: same vault CDN URL used in body

**9d.** Save as DRAFT — do NOT publish. John reviews first.

**9e.** Once John publishes, capture final URL for Step 10.

**9f.** Report:
- Confirm draft saved
- Share URL slug
- Note items needing review
- Ask if ready to proceed to Step 10 distribution package

---

### Step 9.5: Generate the Lofty Metadata Sheet

Produce a single `lofty-metadata.md` file containing the exact field-by-field values John pastes into Lofty.

```markdown
# Lofty CMS Metadata — [Blog Title]

**Use this when creating the blog post in Lofty. Each field maps directly to a Lofty CMS input.**

---

## Blog Title (H1)
[Full headline]

## URL Slug
[the-canonical-slug-only-no-domain]

Full URL: https://integrityhomeswi.com/blog/[the-canonical-slug-only-no-domain]

## Category / Categories
Primary: [Market Insight / Buyer Education / Seller Education / Lifestyle Guide / Listicle / Case Study]
Secondary (if applicable): [city tag]
Tags: [3-5 tags]

## Meta Title (under 60 chars)
[SEO title]
Character count: [X] / 60

## Meta Keywords
[6-10 comma-separated]

## Meta Description (under 155 chars)
[SEO description]
Character count: [X] / 155

## Featured Image
CDN URL: [vault URL used in blog body]
Alt text: [matches blog body alt]

## Author
John Reuter

## Publish Status
Save as DRAFT (do not publish until John reviews)
```

**Validation before delivering:**
- Meta title under 60 chars (count and confirm)
- Meta description under 155 chars (count and confirm)
- Slug lowercase, hyphenated, no special chars, no trailing slash
- Slug includes city name when city-specific
- Slug matches BlogPosting JSON-LD canonical URL
- Featured image CDN URL matches hero image URL in blog HTML
- Primary keyword in meta title and meta description
- Meta keywords include city name and primary topic

If any check fails, regenerate that field.

---

### Step 10: Generate the Distribution Package

Produce all assets as a single `distribution.md` file. If published URL not available yet, use `{{LINK}}` placeholder and flag.

**Important:** all 8 assets are generated every run. Whether they get used depends on the blog's distribution tier (A/B/C from Step 1 or Daily Blog Spine default). The tier guidance is included at the top of the file so John knows which to actually post.

**Top of distribution.md:**

```markdown
# Distribution Package — [Blog Title]

**Distribution Tier:** [A / B / C]
**Authority Tag:** [HUMAN-REQUIRED / HUMAN-PREFERRED / HYBRID / AI-OK]
**Day of Week:** [Mon / Tue / Wed / Thu / Fri / Sat]

**Tier guidance (from OPERATING_SYSTEM → Blog Distribution tab):**
- **Tier A** — Use everything below. Reel + carousel + LI + TT + GBP + FB + IG + Stories.
- **Tier B** — GBP + FB Feed + IG Single + Story Q&A. Skip Reel, carousel, LinkedIn, TikTok, Reddit unless tied to featured market.
- **Tier C** — GBP only (or skip entirely). Other assets are below in case the blog gets a tier bump.

---
```

Then produce the 8 assets below. They're all in the file regardless of tier — John picks based on the guidance above.

#### 1. Google Business Profile Post (pull from approved templates if available)

**Source (in progress, may be unavailable):** `GBP_Copy_Templates.docx` + the v1.1 patch `GBP_Copy_Templates_PATCH_v1_1.docx`.

NOTE (v6): the clean GBP template bank is still being drafted as of 2026-05-28. Until John confirms a current file ID, generate the GBP post from scratch following the structure below and apply the v1.1 patch rules inline.

**How to build the GBP post:**
1. Identify the city for the blog (Madison / Sun Prairie / Waunakee / DeForest / Verona / Middleton — or ROH for Foundation content).
2. Pick the variant that best matches blog topic:
   - Variant A → market update / city hub angle
   - Variant B → buyer education / subdivision spotlight / DOM angle
   - Variant C → seller-focused / luxury / commuter / move-up angle
3. Drop the current month's data (from Step 3) into the post body.
4. Apply the v1.1 patch:
   - First 80 characters carry the hook (mobile truncates here)
   - Soften unverified claims: "best value" → "one of the stronger value plays"; "strongest" → "consistently strong"; "top-rated schools" → "consistently top-ranked schools"; delete "best of both worlds"
   - Strip exact commute minute counts unless verified peak + off-peak. Use ranges or geographic positioning instead.
   - "Top 5% Realtor" is fine on IH content (credentialed)
5. Pick CTA per the rotation (Wk 1 = Nerd Page, Wk 2 = Hub, Wk 3 = Call now, Wk 4 = Pillar Blog)

**Rules:**
- 80-150 words
- Zero hashtags. Zero emojis. No phone numbers in body. No URLs in body (Lofty link gets attached via the CTA button).
- First sentence MUST include the city name.
- Self-correction: scan for emojis, em dashes, and the forbidden phrases before delivering.

**For Reward Our Heroes Foundation GBP posts (only when blog is ROH-themed):**
- Drop the Realtor language
- Lead with mission (programs, grants, scholarships, recognition, support)
- Cite 501(c)(3) status (EIN 39-3358820) when relevant
- Never lead with John's individual credentials. If a Realtor angle is essential, say "a Reward Our Heroes partner Realtor."

#### 2. Short-Form Video Script (Reels / Shorts)
- 30-45 seconds (~90-130 spoken words)
- Conversational. No hype.
- Hook in line one → 3-5 short talking points → natural sign-off
- Sign-off: "John Reuter, Integrity Homes."

#### 3. Instagram Reel Caption
- Short, clean. No links.
- Soft CTA only: "Link in bio" / "Save this" / "Follow for more Dane County."
- Attribution at bottom: "John Reuter | Integrity Homes (Real Broker, LLC)"

#### 4. Facebook Reel Caption (Comments-First)
- **Part A (Main Post):** 3-6 sentences. No links. Community-focused. Soft question.
- **Part B (First Comment):** Brief 1-2 sentence context + `{{LINK}}` + Attribution.

#### 5. Nextdoor Post
- Helpful, resident-pro tone. City name natural.
- No sales pitch. No emojis. No links in main post.
- **First Comment:** Short explanation + `{{LINK}}`.

#### 6. Reddit Post (Moderator Style)
- Subreddit by city: r/madisonwi for Madison/Middleton/Verona/DeForest/Windsor/Waunakee (with city tag in title); r/SunPrairie for Sun Prairie.
- **Part A (Main Post):** 3-6 sentences. No links. End with community-focused question.
- **Part B (First Comment / Data Drop):** 1-3 short paragraphs or bullets. Deep insight. Neutral tone. No emojis.
- **Part C (Second Comment):** "Optional further reading: `{{LINK}}`"

#### 7. YouTube Short Package
- **Title:** Hyper-local, plain language, includes city name. Under 65 chars.
- **Description:** 2-4 short paragraphs. Calm tone. Include: John Reuter | Integrity Homes | Real Broker LLC | 608-669-4226 | john@integrityhomeswi.com | integrityhomeswi.com
- **Full Transcript:** Verbatim script from item #2. Must naturally include "John Reuter," "Integrity Homes," and "Real Broker."

#### 8. Carousel Concept (for Tier A and Tier B blogs)

**Source (in progress, may be unavailable):** `Carousel_Design_System.html` — design tokens, slide formats, and example layouts.

NOTE (v6): the Carousel Design System html does not yet exist as of 2026-05-28. Until John confirms a current file ID, use the reproduced design tokens below.

**When to produce:** Tier A always. Tier B only when the blog is tied to the featured market that week (per the Daily Blog Spine). Tier C — skip; leave a one-line note "Carousel skipped — Tier C blog."

**What to deliver in distribution.md:** the carousel *concept* + slide-by-slide copy (not the actual designed PDF — John or his designer designs in Canva or via the HTML reference).

**Carousel format:**
- 5-7 slides
- Slide 1 = hook only (big serif headline, brand mark, swipe cue)
- Slide 2 doubles as alt cover (IG re-shows posts using slide 2 if engagement low)
- One idea per slide. Big text. Lots of breathing room.
- Final slide CTA = one specific action ("DM me WAUNAKEE" not "Reach out!")
- IH palette: Cormorant Garamond + Jost; navy (`#002850`) + gold (`#C9A84C`)
- ROH palette: Cormorant Garamond + Jost; deep red + cream
- Cross-post IG carousel as LinkedIn PDF (same content, different upload)

**Output format in distribution.md:**
```
Slide 1 (Hook): [headline copy]
Slide 2 (Alt Cover): [headline copy]
Slide 3: [single idea + 1-2 supporting line]
Slide 4: [single idea + 1-2 supporting line]
Slide 5: [single idea + 1-2 supporting line]
Slide 6 (optional): [single idea + 1-2 supporting line]
Slide 7 (CTA): [one specific action]
```

#### 9. Internal Voice Check (silent — do this before delivering)

Re-read every output and confirm:
- Sounds like a data-rich neighbor, not a salesperson?
- Zero em dashes? (Replace any found.)
- Zero emojis where they don't belong?
- "Integrity Homes" used correctly in visible copy (never "IH," never "Integrity Homes Wisconsin")? "Integrity Homes of Wisconsin" allowed only in legal/disclosure context.
- City name in first sentence of GBP post?
- All `{{LINK}}` placeholders flagged?
- ROH phone (608-492-0515) does NOT appear in IH content?
- IH phone (608-669-4226) is the contact phone in IH content?
- IH→ROH co-mention only (not the reverse)?

If any check fails, rewrite that section.

---

### Step 11: Final Status Report & Master Plan Update

Output in chat:

1. **Lofty draft URL** (or published URL if live)
2. **Vault image used** (Asset ID + CDN URL — audit trail)
3. **Lofty metadata sheet location** (`lofty-metadata.md` in Drive folder)
4. **Distribution.md location** (Google Drive folder path)
5. **Distribution tier** (A / B / C)
6. **Authority tag** (HUMAN-REQUIRED / HUMAN-PREFERRED / HYBRID / AI-OK) — for the Sunday Weekly Audit human/AI ratio check
7. **Outstanding items** (anything still requiring John — URL paste, scheduling, Lofty publishing, recording the human Reel for HUMAN-REQUIRED content, etc.)
8. **Daily Blog Spine update line** in this exact format for the OPERATING_SYSTEM workbook (`113NVFTaJ6e1GUILrKeySxA0eTWg1_LNw`, Daily Blog Spine tab):
   ```
   Status: Drafted    Blog Written: Yes    Date: {today's date}
   ```

---

## Error Handling

**OPERATING_SYSTEM unreachable (Step 0):** Use the defaults table from the Daily Blog Spine reproduced inline in Step 0. Flag to John that the framework read failed.

**Google Drive access fails (Step 1):** Ask John to share the topic directly. Pipeline can proceed without automated topic pulling.

**Spreadsheet can't be read:** Ask John to export as CSV or paste key URLs. Or use Claude in Chrome for direct read.

**Market data stale or unavailable:** Flag estimates and ask John to verify before publishing. Never fabricate.

**Vault image selection unclear:** Ask John, or fall to Step 8e.

**Vault is empty for a city:** Fall to Step 8e (generate via Nano Banana 2). Flag that city vault needs population.

**Vault file inaccessible:** File ID `1-7adErt886OpAjwBQB7APudowaLBQX8e6GwER32GJK0`. Ask John to confirm sharing or paste relevant tab. (Old vault `1AjrZWvFRfcHQSjMd3rUQqIM83FD0Laqp` is retired — do not fall back to it.)

**Market Reports folder/PDF missing:** Try both folder patterns described in Step 3a. If neither finds the PDF, fall through to Nerd Page (Step 3b) and flag the gap.

**Nerd Page for current month not yet published:** Fall back to previous month. Flag.

**Nerd Page reachable but missing a stat:** Use John-provided MLS if available. Otherwise external sources, with clear notation of which numbers came from where.

**GBP Templates unavailable (Step 10):** The clean template bank is still being drafted. Generate the GBP post from scratch following the same structure (Hook → Body w/ stat → Soft positioning → CTA), apply the v1.1 patch rules from inline guidance, and flag that templates couldn't be read.

**Carousel Design System unavailable (Step 10 #8):** The HTML reference does not yet exist. Produce the carousel concept anyway following the format above. The design tokens (Cormorant Garamond + Jost, navy + gold for IH, deep red + cream for ROH) are reproduced in this skill.

**Lofty session expired:** Pause at Step 9 and wait for John to log in.

**Skill dependency missing:** Invoke the skills by name via the Skill tool. If still unavailable, read whatever copies exist in the project folder and follow inline.

---

## Quick-Start Commands

- **"Run the blog pipeline" / "Let's do this week's blog"** → Start at Step 0.
- **"Build the [city] Living guide"** → Start at Step 0, then jump to Step 4B (Living framework).
- **"Just do the distribution for [blog]"** → Skip to Step 10. Need blog content + published URL.
- **"Add to the vault"** → Skip to Step 8e standalone.

If John provides the topic directly, do Step 0, skip Step 1, start at Step 2.
