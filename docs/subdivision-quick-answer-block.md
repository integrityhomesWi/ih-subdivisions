# Subdivision Template — Quick-Answer Block + Speakable Schema (Phase 7a / 7b)

Two additions to the NAS subdivision template. Both target AI-citation and voice-answer surfaces without changing the page's visual structure much.

**Placement:** the Quick-Answer block goes immediately after the Stats Strip and before the Photo Strip / About section. It's the first substantial prose on the page, which is the point — retrieval-based AI systems weight a page's opening content heavily.

---

## 1. CSS — add to the existing `<style>` block

Uses the template's existing design tokens (`--navy`, `--gold`, `--cream`, `--font-display`, etc.) so it inherits the current look rather than introducing a new visual language.

```css
    /* QUICK ANSWER — GEO/AI citation block */
    .quick-answer {
      background: var(--cream);
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      padding: 40px 32px;
    }
    .quick-answer-inner {
      max-width: var(--max);
      margin: 0 auto;
      display: flex;
      gap: 28px;
      align-items: flex-start;
    }
    .quick-answer-line {
      width: 2px;
      background: var(--gold);
      flex-shrink: 0;
      align-self: stretch;
      min-height: 80px;
    }
    .quick-answer-eyebrow {
      font-size: 0.67rem;
      font-weight: 600;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 10px;
    }
    .qa-question {
      font-family: var(--font-display);
      font-size: clamp(1.3rem, 2.2vw, 1.7rem);
      font-weight: 400;
      color: var(--navy);
      line-height: 1.25;
      margin: 0 0 14px 0;
    }
    .quick-answer p {
      font-size: 1.02rem;
      color: var(--text-mid);
      line-height: 1.8;
      font-weight: 300;
      margin: 0;
    }
    .quick-answer p strong { color: var(--navy); font-weight: 600; }
    @media (max-width: 768px) {
      .quick-answer { padding: 28px 20px; }
      .quick-answer-inner { flex-direction: column; gap: 16px; }
      .quick-answer-line { width: 40px; height: 2px; min-height: unset; }
    }
```

---

## 2. HTML — insert after the Stats Strip

**Format: question as an `<h2>`, then the answer paragraph.** Including the literal question helps retrieval systems match a user's query directly, and gives human skimmers a visible heading instead of an unlabeled paragraph.

Question format: `What is [Subdivision] in [City], Wisconsin?`

### Worked example (Kilkenny Farms West)

```html
<!-- QUICK ANSWER -->
  <div class="quick-answer">
    <div class="quick-answer-inner">
      <div class="quick-answer-line"></div>
      <div>
        <h2 class="qa-question">What is Kilkenny Farms West in Waunakee, Wisconsin?</h2>
        <p class="qa-speakable"><strong>Kilkenny Farms West</strong> is a newer residential neighborhood in the southern corridor of Waunakee, Wisconsin, in Dane County. Developed by Livable Communities by Don Tierney on land settled by Irish immigrants in 1848, it features a saltwater pool complex, a trail system connecting directly to Waunakee schools, and a beer garden shelter. Homes sold between $900,000 and $1.3 million over the past 12 months per SCWMLS data. Aldi sits inside the neighborhood, with downtown Waunakee 1.1 miles away.</p>
      </div>
    </div>
  </div>
```

### The four-slot fact template

This is what makes the answers consistently good — each sentence has an assigned job. Fill the slots with facts and the specificity takes care of itself. Filler phrasing ("known for its character and charm," "a wonderful place to call home") can't fit, because it doesn't answer any of the four jobs.

| Sentence | Job | Must contain |
|---|---|---|
| 1 | What + where | "[Name] is a [established / newer / active new-construction] residential neighborhood in [area/direction] of [city], Wisconsin, in Dane County." |
| 2 | Origin + defining features | Developer or builder name, build era or a dated historical fact, then 2–3 **named** amenities (not "parks and trails" — "Prairie Park," "the saltwater pool complex") |
| 3 | Price | A sourced range with the source stated ("per SCWMLS data"). MLS data will be supplied for every subdivision, so this sentence is always present — never substitute a public-site estimate or builder-quoted pricing here |
| 4 | Anchor facts | School district name + a specific distance to a real named place (downtown, a school, a highway, an employer) |

### Writing rules
- **60–90 words total** across the four sentences. Long enough to stand alone as a complete answer, short enough to be lifted whole.
- **Answer first, no wind-up.** Sentence 1 opens with "[Subdivision] is a…" — never a narrative hook. The hero already does that job.
- **Don't spend a sentence on geography alone.** "Kilkenny West is located in Waunakee, Wisconsin" as its own sentence wastes a slot — fold the location into sentence 1.
- **No time-relative phrasing.** "Homes are 10–15 years old" goes stale on publication. Use a build year range instead ("built between 2018 and 2022").
- **Resident sentiment only if actually sourced.** "People who live here say they love it because…" is only usable if it comes from real Part 3 human intel (an actual Facebook group post, HOA newsletter, or local news item) with the source noted. Never paraphrase what a resident *might* say — that's precisely the fabricated local color the Kenzie SOP v2 rewrite exists to prevent, and this is the worst block on the page to put it in. Prefer the verifiable version anyway: "Aldi sits inside the neighborhood" beats "residents love being close to Aldi."
- **Must be self-contained.** Assume zero surrounding context — no "as mentioned above," no pronouns referring to hero copy.
- **Never put unverified data here.** This is the passage most likely to be quoted verbatim, so a wrong number here is worse than a wrong number anywhere else on the page. Price always comes from the SCWMLS export — never a public-site estimate.
- **Date the price range.** Since MLS figures get refreshed quarterly (Phase 7c), the sentence should carry a time window — "over the past 12 months per SCWMLS data" — so the number stays accurate as written rather than becoming a stale absolute claim.
- Bold the subdivision name only. Additional bolding dilutes it.

### Semrush input — what it should and shouldn't influence
Run a quick Semrush check before writing this block, but scope it narrowly:
- **Use it to pick the right name variant.** Several subdivisions have competing forms — "Six Mile Creek" vs "Sixmile Creek" (the entrance sign and golf course use one word, buyers and the MLS use two), "Crest at Eagle Trace" vs "Eagle Trace," "Heritage Gardens at Erickson Farms" vs "Heritage Gardens." Lead sentence 1 with whichever variant actually carries search volume, and mention the alternate form later in the body.
- **Use it to prioritize which facts earn a slot.** If "[subdivision] schools" pulls real volume and "[subdivision] HOA" doesn't, the school fact belongs in sentence 4 and the HOA detail waits for the body.
- **Do not let it influence phrasing.** The block only works if it reads as a clean factual answer. Keyword-shaped sentences read as marketing copy, which is the opposite of what gets cited.
- **Skip trend data here.** Trending signals belong in the Attack Plan's build-order prioritization, not in an evergreen answer block. This content gets refreshed quarterly anyway (Phase 7c).

---

## 3. Speakable schema — add to the existing `@graph`

Add as a new node inside the page's existing `@graph` array. Targets the Quick-Answer block and the FAQ section — the two passages most likely to be read aloud by a voice assistant.

```json
      {
        "@type": "WebPage",
        "@id": "https://integrityhomeswi.com/[city]/[subdivision-slug]/#webpage",
        "speakable": {
          "@type": "SpeakableSpecification",
          "cssSelector": [".qa-question", ".qa-speakable", ".faq-q", ".faq-a"]
        }
      }
```

**Note:** the page already has a `WebPage` node at that same `@id`. Rather than adding a second node, add the `speakable` property directly to the existing WebPage node — same `@id` means schema parsers merge them, but keeping it in one node is cleaner and easier to audit.

So the existing WebPage node becomes:

```json
      {
        "@type": "WebPage",
        "@id": "https://integrityhomeswi.com/waunakee/six-mile-creek/#webpage",
        "url": "https://integrityhomeswi.com/waunakee/six-mile-creek/",
        "name": "Six Mile Creek Waunakee WI | Neighborhood Guide | Integrity Homes",
        "description": "...",
        "inLanguage": "en-US",
        "isPartOf": { "@id": "https://integrityhomeswi.com/#website" },
        "breadcrumb": { "@id": "https://integrityhomeswi.com/waunakee/six-mile-creek/#breadcrumb" },
        "datePublished": "2026-06-26",
        "dateModified": "2026-06-26",
        "author": { "@id": "https://integrityhomeswi.com/#john" },
        "speakable": {
          "@type": "SpeakableSpecification",
          "cssSelector": [".qa-question", ".qa-speakable", ".faq-q", ".faq-a"]
        }
      }
```

**Two corrections folded into that example above, both previously flagged:**
- `isPartOf` now points to `#website` — matches the corrected master identity script (was pointing at `#site`, which didn't resolve)
- `author` now points to `#john` — matches the master script's actual Person node id (subdivision pages currently use `#johnreuter`, which doesn't exist)

---

## Checklist for adding this to an existing page
- [ ] Run a Semrush check on subdivision name variants — lead with whichever form carries search volume
- [ ] Add the CSS block to the page's `<style>`
- [ ] Insert the Quick-Answer HTML after the Stats Strip
- [ ] Write the question as an `<h2>`: "What is [Subdivision] in [City], Wisconsin?"
- [ ] Write the 60–90 word answer using the four-slot fact template (do not reuse the meta description — different length, different job)
- [ ] Add `speakable` to the existing WebPage node
- [ ] Fix `isPartOf` → `#website` and `author` → `#john` while you're in the schema
- [ ] Update `dateModified` to reflect the edit
- [ ] Add the Quick-Answer price sentence to the quarterly MLS refresh checklist (Phase 7c) — it carries a live number and needs updating alongside the Market Data section, not just the body copy
