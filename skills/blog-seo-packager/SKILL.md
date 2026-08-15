---
name: Blog SEO Packager
description: Pre-publish SEO and linking packager for Integrity Homes blog posts. Takes a finished or near-finished blog draft and produces the publish-ready metadata bundle - slug, meta description, meta tags, categories - plus ranked internal links pulled from a sitemap John provides, image candidates matched from the media-vault Google Sheet, an AI-visibility cross-check (Semrush AI Visibility + optional ChatGPT/Perplexity tabs in Cowork), and a ready-to-paste Gemini image-generation prompt. Use AFTER a blog is drafted and BEFORE (or alongside) the Lofty Blog HTML Builder. Trigger when John says: "package this blog," "SEO package," "get me the slug and meta," "find internal links for this post," "what should this blog link to," "find a blog image," "metadata for this post," or drops a sitemap and asks for linking. Do NOT use this to write blog content (that's Blog Post Writer) or to build final HTML (that's Lofty Blog HTML Builder).
---

# Blog SEO Packager

Wraps a finished blog draft with everything needed to publish in Lofty: metadata, real internal links, an image candidate, an AI-visibility check, and a Gemini prompt. This skill does NOT write content and does NOT build HTML. It runs in the gap between drafting and publishing.

## Why this skill exists

Two recurring failures this skill prevents:
1. **Dead internal links.** integrityhomeswi.com sits behind a Cloudflare bot challenge, so the live sitemap and pages CANNOT be fetched with plain `curl`/web_fetch - every URL returns the same JavaScript challenge page, not real content. Guessing URLs produces broken links. The fix: John provides the sitemap as a file; the skill reads URLs from that file instead of fetching them live.
2. **Weak AI/GEO visibility.** Pages get cited by AI engines but the brand isn't attributed. This skill cross-checks AI sources at packaging time so the metadata and linking reinforce entity attribution.

## When To Use

Use AFTER blog content is drafted and approved. Input: finished/near-finished draft (from Blog Post Writer, a Google Doc, or pasted). Output: the publish bundle below.

Do NOT trigger for: writing the blog (Blog Post Writer), building final HTML (Lofty Blog HTML Builder), or ROH content (ROH Content Writer).

## Required Inputs

Collect before packaging:
1. The blog draft (body, headings, topic, target city)
2. The sitemap file - see Step 1 for accepted formats
3. Confirmation of which environment: **Cowork** (browser + folder access) or **plain chat** (file/paste only)

If the sitemap is missing, ask for it before producing internal links. Do not guess URLs.

## Environment Awareness

This skill behaves differently in Cowork vs plain chat. Detect and state which path is being used.

| Step | Cowork | Plain chat |
|------|--------|------------|
| Sitemap | Read PDF dropped in folder (primary); optionally open Chrome to live sitemap (clears Cloudflare) | Read pasted/attached file only |
| AI sources | Semrush AI Visibility (MCP) + open ChatGPT/Perplexity tabs for human-approved check | Semrush AI Visibility (MCP) + generate paste-back prompts |
| Image vault | Search media-vault Google Sheet (MCP) | Same |
| Gemini prompt | Output text | Output text |

Never claim to have "searched ChatGPT/Perplexity" autonomously. Those are logged-in, anti-bot apps. In Cowork the skill OPENS the tab and pre-fills the query for John to review; in chat it produces prompts John pastes. Semrush AI Visibility is the automated, reliable AI-source signal (already in John's ~$359/mo Semrush One plan).

---

## Step 1 - Internal Links (from the sitemap John provides)

**Primary input: a PDF dropped in the Cowork folder.** A PDF sitemap is a rendered URL list, not XML - extract URLs from the PDF *text*, do not expect XML tags.

Accepted formats (handle all):
- **PDF** (primary) - read text, regex out every `integrityhomeswi.com/...` URL
- **XML** sitemap or sitemap index - parse `<loc>` tags; if it's an index, read each child sitemap file John provides
- **Pasted text / GSC or Lofty export** - pull URLs line by line

Process:
1. Read the sitemap file. Extract all URLs. Dedupe. Strip tracking params.
2. Identify the post's **target city** and **primary topic/keywords** from the draft.
3. Rank candidate links by relevance:
   - **Cluster-mates first** (same city: city hub, subdivision pages, market report)
   - **Topic matches** (buyer/seller/loan/lifestyle pages sharing keywords)
   - **Peer blogs** (other posts on a related subject)
4. Return 4-8 ranked candidates with: URL, page title (from sitemap or inferred from slug), and a one-line "why this link" + suggested anchor text.
5. Flag any city whose URL structure looks ambiguous (e.g. `/waunakee/neighborhoods/...` vs `/neighborhoods/waunakee/...`) and tell John to confirm once.

Output the **reverse-link suggestions** too: which existing pages should link BACK to this post (this is the higher-value direction for lifestyle/supporting content). Provide drop-in HTML snippets.

If no sitemap is provided: STOP this step, state that internal links require the sitemap, and ask for it. Do not fabricate URLs.

---

## Step 2 - AI Source Cross-Check

Goal: see how AI engines treat this topic/keyword and whether the brand is attributed, so metadata reinforces it.

**Always (any environment): Semrush AI Visibility via the connected Semrush MCP.**
- Pull AI-citation data for the target keyword/topic and for integrityhomeswi.com.
- Report: is the brand mentioned, which pages get cited, what gap exists.
- This maps to John's known GEO problem (many cited pages, few brand mentions) - so recommend author-attribution / entity-schema reinforcement when the gap shows.

**Cowork only (optional, human-approved): open browser tabs.**
- Open a Chrome tab to ChatGPT and one to Perplexity, pre-filled with a query like: `What are the best [topic] in [city], and which local sources are cited?`
- John reads the answers and approves/pastes back. The skill does NOT scrape or claim to have read them autonomously.

**Plain chat: paste-back prompts.**
- Output two ready-to-paste prompts (one ChatGPT, one Perplexity) using the query pattern above. John pastes answers back; fold useful framing into the metadata.

Use whatever comes back to sharpen the meta description and tags toward how people actually ask AI engines about the topic.

---

## Step 3 - Image Library Search (media-vault Google Sheet)

Source: the media-vault **Google Sheet** (single master sheet, permanent IDs like `IH-PHOTO-0001`). Search it directly via the Google Drive / Sheets MCP.

Process:
1. Search the sheet for rows tagged with the post's **city** and **topic** (e.g. Waunakee + downtown/restaurants/lifestyle).
2. Return up to 3 candidates: image ID, CDN URL (cdn.lofty.com), and a one-line fit note.
3. If nothing matches, say so plainly and go straight to Step 4 (Gemini prompt).

Never invent an image ID or URL. If the sheet returns nothing, the answer is "no existing match - generate one."

---

## Step 4 - Gemini Image-Generation Prompt

Always output a ready-to-paste Gemini prompt, whether or not Step 3 found a match (John may want a fresh image).

The prompt must specify:
- **Subject** tied to the post topic + city (real, recognizable feel; no fake landmarks)
- **Style**: clean, editorial, photographic, natural light - not illustrated, not AI-glossy
- **Brand palette** reference: navy #002850, gold #C9A84C accents where natural
- **Aspect ratio**: 16:9 for blog hero (1200x675 target)
- **No text overlay** (text gets added in Lofty/Canva), no logos, no people's faces as focal subjects unless requested
- A negative line: avoid watermarks, distorted text, cartoonish rendering

Give the prompt as a single copy-paste block.

---

## Final Output Block (the deliverable)

Produce this exact structure, ready for Lofty:

```
=== BLOG SEO PACKAGE: [Post Title] ===
Environment: [Cowork | Plain chat]
Target city: [city]   Primary keyword: [kw]

--- METADATA ---
Slug:             [lowercase-hyphenated, no stop-word bloat]
Meta description: [<155 characters, includes primary keyword naturally]
Meta tags:        [6-10 comma-separated, primary first]
Categories:       [Lofty categories, e.g. Community, Buyer Education]

--- INTERNAL LINKS (from sitemap) ---
OUTBOUND (this post links to):
 1. [URL] - anchor: "[text]" - why
 ...
REVERSE (pages that should link back to this post):
 1. [URL] - drop-in snippet provided below
 ...
[⚠ URL-structure confirmations, if any]

--- REVERSE-LINK SNIPPETS ---
[HTML snippets ready to paste into each page]

--- AI VISIBILITY ---
Semrush AI Visibility: [brand mentioned? cited pages? gap?]
Recommendation: [attribution/schema action if gap]
[Cowork: tabs opened for review | Chat: paste-back prompts below]

--- IMAGE ---
Library candidates: [ID + URL + fit, or "no match"]
Gemini prompt:
[copy-paste block]
```

## Rules

- Never fabricate a URL, image ID, or sitemap content. If a source is missing, say so and ask.
- The sitemap John provides is the ONLY trusted source for live URLs - do not "verify" by fetching the site (Cloudflare blocks it).
- Meta description hard limit: under 155 characters.
- Brand naming follows the Brand Style Guide: visible text always "Integrity Homes"; never "Integrity Homes Wisconsin"; legal name only in JSON-LD.
- Phone format 608-669-4226 with hyphens.
- This skill hands off to **Lofty Blog HTML Builder** for final HTML - it does not produce the HTML itself.
- State the environment (Cowork vs chat) at the top of every run so expectations are clear.
- Be honest about the human-in-the-loop seam on AI sources. Never claim autonomous ChatGPT/Perplexity reads.
