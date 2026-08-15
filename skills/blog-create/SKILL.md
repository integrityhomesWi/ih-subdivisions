---
name: Blog Create
description: One-command, end-to-end blog creation for Integrity Homes. When John says "create a blog," "write a blog about X," "do a blog on X," "make me a blog post," or similar, this orchestrator runs the full chain - research, write, package (SEO metadata + internal links + image), and build the final Lofty-ready HTML - and delivers one publish-ready file. It does the work by calling three existing skills in order: Blog Post Writer (drafts the content), Blog SEO Packager (slug, meta, tags, categories, internal links from a sitemap, image candidate, Gemini prompt), and Lofty Blog HTML Builder (final HTML). Use this for AD-HOC blog topics on demand. Do NOT use for the scheduled weekly market/pillar content - that belongs to the Integrity Blog Pipeline skill, which this orchestrator hands off to. Do NOT trigger for ROH content (ROH Content Writer).
---

# Blog Create (Orchestrator)

This skill turns a single request - "create a blog about X" - into a finished, publish-ready Lofty HTML file. It writes no content and builds no HTML on its own. It is a conductor: it runs three existing skills in sequence and passes the output of each into the next.

## What this is for

ONE trigger, the whole job. John should be able to say "Cowork, create a blog about the best parks in Verona" and get back a packaged HTML file without naming the sub-steps.

## Lane separation (read first)

- **This skill (`blog-create`)** = ad-hoc blogs on ANY topic, on demand.
- **`integrity-blog-pipeline`** = the scheduled WEEKLY market/pillar content that reads the OPERATING_SYSTEM workbook (Daily Blog Spine, market reports, pillar blogs).

If the request is for monthly/weekly **market reports** or **pillar blogs** (driving prices / how fast selling / buyer's vs seller's market), STOP and hand off to `integrity-blog-pipeline` or `market-report-page`. Do not duplicate that work here. When unsure which lane, ask one question: "Is this the weekly market content, or a standalone topic?"

## The Chain

Run these in order. Do not skip a stage. Carry each stage's output forward.

### Stage 1 - WRITE  (calls: Blog Post Writer)
Invoke the **Blog Post Writer** skill to draft the post.
- Run its intake (blog type, market area, audience, keywords, data source, CTA). In Cowork, ask all intake questions up front in one batch so the rest of the chain can run uninterrupted.
- If John already gave the topic and enough context in his request, infer the intake answers and state the assumptions rather than re-asking everything. Only ask what you genuinely can't infer.
- Output: the Markdown draft (title, snippet answer, body, FAQ, ROH footer, CTA, suggested meta title/description).
- Respect Blog Post Writer's rules exactly (no fabricated data; Dane County stats only from what John provides; Fair Housing compliance).

### Stage 2 - PACKAGE  (calls: Blog SEO Packager)
Pass the finished draft into the **Blog SEO Packager** skill.
- Internal links require a **sitemap** (PDF dropped in the Cowork folder is primary). If no sitemap is present, ask for it before producing links - never guess URLs (the site is Cloudflare-blocked and cannot be crawled live).
- Produces: slug, meta description (<155), meta tags, categories, ranked outbound internal links, reverse-link snippets, AI-visibility check (Semrush AI Visibility; optional ChatGPT/Perplexity tabs in Cowork), image library candidates (from the media-vault Google Sheet), and a Gemini image prompt.

### Stage 3 - BUILD HTML  (calls: Lofty Blog HTML Builder)
Pass the draft + packaged metadata into the **Lofty Blog HTML Builder** skill.
- It needs: title, meta description, slug, hero image URL (use a Step-2 image candidate if found; otherwise leave a clearly-marked placeholder and note the Gemini prompt), location, published/updated dates, article section/category, keywords, and the body content.
- Produces the complete Lofty-ready HTML with inline CSS, JSON-LD @graph, speakable classes, geo tags, sidebar (wired with the Step-2 internal links), and CTAs.

## Final Delivery

Deliver as ONE package:
1. The **publish-ready HTML file** (the main deliverable).
2. A short **publish checklist**: slug, meta description, categories/tags, the internal links used, the reverse-link snippets to add elsewhere, the image (library ID/URL or "generate via Gemini prompt below"), and any URL-structure confirmations flagged in Stage 2.

Present the HTML file via present_files. Keep the checklist tight - John pastes the HTML into Lofty and works the checklist.

## Cowork vs Plain Chat

- **Cowork:** batch all intake at the start; read the sitemap PDF from the folder; can open AI tabs for human-approved visibility check; searches the media-vault Sheet via MCP. Aim for a single uninterrupted run.
- **Plain chat:** same chain, but the sitemap must be pasted/attached, AI sources come as paste-back prompts, and the file is delivered for download.

State which environment is active at the start of the run.

## Rules

- This skill NEVER writes content or HTML itself - it always routes through the three sub-skills so John's style stays defined in one place.
- Never fabricate URLs, stats, image IDs, or sitemap content. Missing source -> ask.
- Hand off market/pillar content to `integrity-blog-pipeline`; never duplicate it here.
- Brand Style Guide always applies: visible text "Integrity Homes"; phone 608-669-4226 with hyphens.
- If any stage is blocked (e.g. no sitemap), complete what you can, deliver it, and clearly list what's pending - don't stall the whole chain on one missing input.
