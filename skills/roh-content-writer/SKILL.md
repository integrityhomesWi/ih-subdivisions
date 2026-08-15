---
name: roh-content-writer
description: Writes content for the Reward Our Heroes Foundation, Foundation grant announcements, Hero of the Month/Year spotlights, ROH educational blogs, and copy for hero profession landing pages. Use whenever John asks to write, draft, or create anything for rewardourheroes.com or the Reward Our Heroes Foundation. Trigger on phrases like "ROH blog," "Reward Our Heroes post," "grant announcement," "Hero of the Month," "Hero of the Year," "scholarship spotlight," "Foundation story," "write copy for the [profession] page," "VA loan blog," or "veteran blog." Also trigger when the subject is a Wisconsin hero profession (military, veterans, law enforcement, firefighters, EMS, healthcare workers, teachers) and the writing is for ROH rather than Integrity Homes. Do NOT trigger for Integrity Homes blog posts that merely mention ROH in the footer, that's the Blog Post Writer skill.
---

# ROH Content Writer

## Reference docs — read these first via Google Drive MCP

Before writing anything, read these files from the `0 - Skills & Systems` folder (Drive folder ID: `1Fq1IupOP6qGyHyOtmEor_BZJ0rEVmTQe`):

| File | Drive ID | What it covers |
|---|---|---|
| `brand-voice.md` | `1gGEYNpOvpkS8_98RdeQGcPXp4BywBgRb` | Colors, phones, voice rules, banned phrases for both brands |
| `roh-standards.md` | `13UE2p8mMRng0XL75CkBYPlbZH6FImLbD` | Full ROH compliance checklist — apply every item to every piece |
| `accounts.md` | `1BJ11_l83VP6OA3cdoccZfrewN4NUvuPH` | Confirmed ROH social handles, CMS URL patterns |

These are the single source of truth. If a rule in the reference doc conflicts with something below, the reference doc wins. If a rule changes, it changes in the reference doc — not here.

---

## When This Skill Runs (vs. Blog Post Writer)

- **This skill**: primary subject is ROH, the Foundation, a Wisconsin hero profession, a grant, a scholarship, or a hero story. Audience: heroes, donors, nominators, supporters.
- **Blog Post Writer**: primary subject is Integrity Homes real estate (Dane County buyers/sellers, market reports, listings, neighborhood guides). The ROH footer block on those posts is brand boilerplate, not ROH content.

If unsure, ask: "Is this for rewardourheroes.com or integrityhomeswi.com?"

---

## Outputs

Two files per run:
1. **Gold-standard Lofty/Wix-ready HTML** — complete `<head>` with SEO meta, OG, Twitter card, geo meta, font preconnects, inline CSS using the ROH design system, JSON-LD `@graph` schema, breadcrumb bar, hero, snippet box (for blog posts), all body sections, FAQ with inline microdata, CTA block, author bio, ROH footer, and the Wix iframe anchor-fix script if the post uses internal anchors.
2. **Publishing Packet (.docx)** — navy/gold cover banner, CMS metadata (title, slug, canonical, OG, geo, breadcrumb), schema notes, pre-publish checklist, and Distribution Snippet Pack (Reel script HUMAN-REQUIRED, IG carousel outline HYBRID, GBP post AI-OK, LinkedIn post HUMAN-REQUIRED, Facebook approach, Nextdoor decision).

Use the female veteran grant post (`/post/emergency-housing-grant-female-veteran-wisconsin`) as the structural template for grant announcements, hero spotlights, and Foundation news. Use the Law Enforcement page (`/law-enforcement-services`) for profession landing pages.

---

## Intake (Ask in One Message)

1. **Content type** — pick one:
   - **Grant announcement** — a Foundation grant has been awarded
   - **Hero spotlight** — Hero of the Month or Hero of the Year feature
   - **Educational blog** — topical post (VA loans, teacher homebuyer programs, WRS pension timing, hero profession explainers)
   - **Profession page copy** — landing page for a hero profession (military, LE, fire, EMS, healthcare, teachers)
2. **Subject details** — name (anonymized if needed), profession, city, what happened, dates, any specific facts/figures
3. **Source material** — case notes, interview, transcript, MLS data, links, or "write from general knowledge"
4. **Primary CTA** — Donate / Sign up / Nominate / Apply / Refer / Contact (default matches content type)
5. **Anonymization** — if a real person is involved, confirm consent and what details can be used

---

## Voice

The ROH voice is **respectful, not pandering. Specific, not sentimental. Honest about what the Foundation can and can't do.**

Anchor lines from existing pages (use as voice references, not verbatim copy):
- "We don't pretend a Realtor's job is the same as yours."
- "I know what it means to walk a post nobody thanks you for."
- "No veteran should ever feel like they have no options."
- "Hero supporting hero, across Wisconsin."

**Do:**
- Use profession-correct vocabulary — officers know WRS pension timing, veterans know BAH and PCS. Get the words right.
- Be honest about scope — the Foundation gives emergency grants case-by-case; it is not a guaranteed program.
- Lead with the person, not the program — even program pages start with the human reality before the offer.

**Don't (see roh-standards.md for the full checklist):**
- Generic gratitude filler — "Heroes among us," "selfless service," "thank you for your sacrifice," "we salute"
- Promises the Foundation can't keep
- Sales pitch inside emotional content
- Conflate a general business event with a veteran-focused gathering
- Em-dashes anywhere — use commas, periods, or parentheses (mid-dot · or pipe | for separators in eyebrows/pills)

---

## Credibility Placement Rules

ROH content has three credibility stacks — do not mix them on the same conversion CTA:
- **CNN/national media** → profession pages and buyer guides only
- **HNG News** → mission/impact, About John
- **AF.mil/service record** → About John, "Why We Exist"

---

## About Reward Our Heroes™ Footer

Append verbatim to any long-form text asset (YouTube description, GBP update, email). Short captions reference the brand and Foundation line but do not need the full footer block. Current footer text is in roh-standards.md.

---

## Reverent-Only Days

Memorial Day, Patriot Day, Gold Star Mother's Day — no promotional CTAs on these dates. Recognition only.
