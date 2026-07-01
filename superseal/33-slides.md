# Slides

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Presentations

---

## Summary

Generate a Cloudflare prospect slide deck following the Challenge → Solution → Proof → Close narrative arc. Produces 14–17 slides output as a SlideData[] JSON array for the Seal viewer with PPTX and PDF export support. Supports 17 layout types covering title, section breaks, content, diagrams, metrics, quotes, comparisons, and closing slides. Every deck is tailored to the prospect's industry, use case, and buying stage — not a generic Cloudflare overview. Decks are designed to be presented (not read), with minimal text per slide and strong visual hierarchy.

## When To Use

- "Build a deck for [account]"
- "Create slides for my meeting with [prospect]"
- "I need a presentation for [use case] at [company]"
- Before a first presentation to a new prospect
- When preparing for an executive briefing and need tailored slides
- When a generic Cloudflare overview deck isn't specific enough
- When building a proposal deck for a competitive deal
- When preparing for an EBC and need session-specific presentations
- "Make me a Zero Trust pitch deck for a [industry] company"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Prospect or customer name |
| `use_case` | ✅ | Primary use case: `zero-trust`, `app-security`, `network-services`, `developer-platform`, `email-security`, `full-platform` |
| `audience` | ❌ | `CISO`, `CTO`, `VP-Infrastructure`, `IT-Director`, `Board` — drives content depth and framing |
| `industry` | ❌ | Prospect's industry — used for relevant case studies and pain points |
| `competitive_context` | ❌ | Known competitors being evaluated — adds competitive slides |
| `slide_count` | ❌ | Target slide count: `short` (10–12), `standard` (14–17, default), `extended` (18–22) |
| `include_pricing` | ❌ | If `true`, includes a pricing overview slide (requires deal context) |
| `acv` | ❌ | Deal size — determines level of detail and proof points |

## Key Outputs

- **SlideData[] JSON** for Seal viewer with sections:
  1. **Title Slide** — account name, use case, Cloudflare branding, presenter name, date
  2. **Challenge Slides** (3–4 slides):
     - Industry-specific pain points with data
     - Cost of the current approach
     - What's changing (threat landscape, digital transformation, regulation)
  3. **Solution Slides** (4–6 slides):
     - Cloudflare platform overview (contextual, not exhaustive)
     - Product-specific value propositions mapped to stated challenges
     - Architecture diagram showing how Cloudflare fits
     - Differentiation vs. alternatives (if competitive context provided)
  4. **Proof Slides** (3–4 slides):
     - Relevant case studies (same industry or similar use case)
     - Performance benchmarks and security metrics
     - Customer quotes or testimonials
     - Third-party validation (Gartner, Forrester, analyst reports)
  5. **Close Slides** (2–3 slides):
     - Recommended next steps (POC, technical workshop, commercial discussion)
     - Proposed timeline
     - Contact information and resources
- **17 Layout Types Available:**
  - `title`, `section-break`, `text-image`, `two-column`, `three-column`, `bullet-list`
  - `metric-highlight`, `comparison-table`, `quote`, `diagram`, `architecture`
  - `case-study`, `timeline`, `pricing`, `team`, `next-steps`, `closing`
- Exported to: `~/helix-deck/slides/[account-slug]-deck-[date].json` + PPTX/PDF via Seal viewer

## Quality Bar Highlights

1. **Challenge before solution** — never lead with Cloudflare products; lead with the prospect's problems and build the case for change before introducing the solution
2. **Minimal text per slide** — if a slide has more than 30 words of body text, it's a document, not a presentation; use visuals, metrics, and short phrases
3. **Industry relevance is mandatory** — case studies must be from the same industry or an adjacent one; a retail case study for a healthcare prospect undermines credibility
4. **Every slide must pass the "so what?" test** — if the audience can see a slide and think "so what?", it doesn't belong in the deck; every slide must advance the narrative
5. **Competitive slides only when context exists** — don't add competitive comparison slides unless a specific competitor has been identified; generic "we're better" slides are counterproductive
6. **The ask must be specific** — "next steps: let's stay in touch" is not a close; "next steps: 2-week POC starting [date] focused on [use case]" is
