---
name: Lofty Blog HTML Builder
description: Converts blog content into gold-standard HTML for Lofty CMS. Outputs complete HTML with inline CSS, JSON-LD schema, speakable classes, geo meta tags, and two-column layout. Use after drafting content with Blog Post Writer.
---

# Lofty Blog HTML Builder

Package finished blog content into Integrity Homes' gold-standard HTML format for Lofty CMS. This skill handles all technical formatting — schema markup, speakable classes, meta tags, sidebar, and CTAs. Alfred pastes the output directly into Lofty.

## When To Use This Skill

Use this skill AFTER the blog content is drafted and approved. This skill does not write content — it packages it.

Input: Finished blog content (from Blog Post Writer, a Google Doc, or provided directly)
Output: Complete HTML file ready for Lofty CMS paste

## Required Inputs

Collect these before generating HTML:

1. **Blog title** (H1)
2. **Meta description** (under 155 characters)
3. **Canonical URL slug** (e.g., `homes-coming-soon-deforest-wi`)
4. **Hero image URL** (from cdn.lofty.com)
5. **Location** (city for geo tags — Madison, Sun Prairie, Waunakee, DeForest, Verona, or Middleton)
6. **Published date** (YYYY-MM-DD)
7. **Updated date** (YYYY-MM-DD — can be same as published for new posts)
8. **Article section** (e.g., "Buyer Education", "Seller Education", "Market Update", "Community")
9. **Keywords** (5-7 comma-separated for schema)
10. **The blog content itself** — body text, H2s, FAQs, etc.

## Geo Coordinates Reference

Use these for geo meta tags based on location:

| City | Latitude | Longitude |
|------|----------|-----------|
| Madison | 43.0731 | -89.4012 |
| Sun Prairie | 43.1836 | -89.2137 |
| Waunakee | 43.1919 | -89.4554 |
| DeForest | 43.2439 | -89.3373 |
| Verona | 42.9908 | -89.5332 |
| Middleton | 43.0972 | -89.5043 |

## HTML Structure

The output follows this exact structure:

```
1. Canonical link
2. Geo meta tags
3. Open Graph meta tags
4. Twitter Card meta tags
5. <style> block with all CSS (inline, no external stylesheets)
6. Breadcrumb navigation
7. Hero section
   - Eyebrow with pills
   - H1 title
   - Hero subtitle
   - Byline with dates
   - Direct Answer box (speakable-intro, speakable-answer)
   - Primary CTA pill (if applicable)
8. Main content
   - Lead paragraph
   - Two-column grid
     - Main column: content sections as .card elements, CTA blocks, FAQ accordion
     - Sidebar: resource links, author card
   - Closing summary (speakable-summary, speakable-conclusion)
   - Signature block
9. JSON-LD @graph schema (single block at bottom of body)
```

## CSS Variables (Required)

Always use these exact CSS variables:

```css
:root {
  --navy: #002850;
  --navy2: #0a3a6b;
  --gold: #C9A84C;
  --ink: #111827;
  --muted: #4B5563;
  --line: #E5E7EB;
  --bg: #FFFFFF;
  --soft: #F7F8FB;
  --red: #B40000;
  --red-soft: #FEF2F2;
  --green: #059669;
  --green-soft: #ECFDF5;
  --radius: 16px;
  --shadow: 0 10px 28px rgba(10,22,40,.10);
  --max: 980px;
}
```

## Typography (Required)

Always load and use these exact fonts — they are the Brand Style Guide standard:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
```

```css
body { font-family: 'Source Sans 3', system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
h1, h2, h3, h4 { font-family: 'Playfair Display', Georgia, serif; }
```

- **Headings:** Playfair Display (600/700/800 weights)
- **Body:** Source Sans 3 (400/500/600/700 weights)
- **Fallback for body:** system-ui, -apple-system, Segoe UI, Roboto, sans-serif
- **Fallback for headings:** Georgia, serif

Do NOT substitute Cormorant Garamond, Jost, Inter, or any other display font without explicit approval. These two fonts are the published brand standard.

## Speakable Classes

Apply these classes to enable voice search optimization:

- `.speakable-intro` — The question in the Direct Answer box
- `.speakable-answer` — The answer in the Direct Answer box
- `.speakable-summary` — The summary paragraph near the end
- `.speakable-conclusion` — The final takeaway sentence

## JSON-LD Schema Structure

Single `@graph` array at bottom of body containing:

1. **Organization** (`#org`)
   - @type: Organization
   - @id: https://integrityhomeswi.com/#org
   - name: Integrity Homes
   - legalName: Integrity Homes of Wisconsin
   - alternateName: John Reuter - Integrity Homes
   - url: https://integrityhomeswi.com

2. **Person** (`#john`)
   - @type: Person (NOT RealEstateAgent)
   - @id: https://integrityhomeswi.com/#john
   - name: John Reuter
   - jobTitle: Broker/Owner
   - worksFor: reference to #org
   - url, telephone, email, description
   - sameAs: LinkedIn, Facebook, theveteranrealtor.com

3. **WebSite** (`#site`)
   - @type: WebSite
   - @id: https://integrityhomeswi.com/#site
   - publisher: reference to #org

4. **WebPage** (`#webpage`)
   - @type: WebPage
   - isPartOf: reference to #site
   - about: reference to #blogposting
   - breadcrumb: reference to #breadcrumb
   - speakable: SpeakableSpecification with all 4 CSS selectors

5. **BlogPosting** (`#blogposting`)
   - @type: BlogPosting
   - mainEntityOfPage: reference to #webpage
   - headline, description, image
   - datePublished, dateModified (ISO format with timezone)
   - author: reference to #john
   - publisher: reference to #org
   - keywords, articleSection

6. **BreadcrumbList** (`#breadcrumb`)
   - Home → Blog → [Current Post]

7. **FAQPage** (`#faq`) — if FAQs are present
   - mainEntity: array of Question/Answer pairs

## Component Classes

**Cards:** `.card` — white background, border, border-radius, padding
**Alert Cards:** `.inventory-alert` — dark gradient background for urgent content
**Callouts:** `.callout` (gold border), `.callout-green` (green border)
**CTA Blocks:** `.cta-block` — navy gradient, white text, button row
**Buttons:** `.btn-primary` (gold), `.btn-secondary` (transparent with border)
**FAQ:** `<details>` with `<summary>` and `.answer` div
**Sidebar:** `.side` with `.side-links` list and `.author-card`

## Sidebar Resources

Default sidebar links (adjust based on content location):

- Coming Soon / Early Access page (featured link)
- Market Report for the location
- Dane County Market Hub
- Madison Homebuyer Guide
- Related blog posts (2-3)
- Home Value Evaluation

## Author Card Content

```
John Reuter
Broker/Owner · Integrity Homes · [Location]
Retired USAF veteran, 2024 RASCW Good Neighbor Award recipient. Quoted by CNN Business on Wisconsin housing trends. Serving [Location] and Dane County buyers and sellers.
```

## Signature Block

```
John Reuter
Integrity Homes · [Location] & Dane County
Brokered by Real Broker, LLC
608-669-4226 · john@integrityhomeswi.com
```

## Rules

- Output complete, valid HTML that can be pasted directly into Lofty
- All styles must be inline in a single `<style>` block — no external CSS
- No `<script>` tags in body except the JSON-LD block
- JSON-LD must be valid JSON — escape quotes, no trailing commas
- Use HTML entities for special characters: `&mdash;`, `&rsaquo;`, `&middot;`, `&amp;`
- Dates in schema must be ISO 8601 with timezone: `2026-03-08T08:00:00-06:00`
- Preserve original blog titles and H2 headings exactly — do not modify them
- Include all 4 speakable classes in appropriate locations
- FAQ section uses `<details>` accordion pattern, not headers

## Naming Rules (Brand Style Guide enforcement)

- **Brand name in all visible content** (headlines, body, meta title, meta description, alt text, og:site_name, twitter:title, hero, footer, signature, CTA, breadcrumb, sidebar, author card): "Integrity Homes"
- **Legal name** (only inside JSON-LD `legalName` field, or in disclosures/legal language where the legal entity is specifically required): "Integrity Homes of Wisconsin"
- **Forbidden everywhere — no exceptions**: "Integrity Homes Wisconsin" (this is the wrong form Google and AI sometimes invent — never appears in any output)
- **Phone format**: `608-669-4226` with hyphens, never `608.669.4226` with periods
- **Schema `alternateName` field may include**: "John Reuter - Integrity Homes" (this is how Google indexes the brand on social platforms)

## Output Format

Deliver as a single HTML file. Do not wrap in markdown code blocks — output raw HTML that Alfred can copy directly.
