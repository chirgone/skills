# Blog Review

**Catalog:** Cloudflare SuperSeal  
**Category:** Marketing / Content

---

## Summary

Review a Cloudflare blog post draft for technical accuracy, messaging alignment, readability, SEO best practices, and brand voice consistency. Produces structured feedback with line-level suggestions, a severity-rated issue list, and an overall publish-readiness score. Designed for authors, editors, and PMMs preparing posts for the Cloudflare blog.

## When To Use

- "Review this blog draft before I submit it"
- "Check this post for technical accuracy"
- "Is this blog ready to publish?"
- Pre-publication review of any Cloudflare blog post
- PMM reviewing an engineering-authored post for messaging alignment
- Author self-review before submitting to editorial
- Post-mortem or incident blog review for sensitivity and accuracy

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `draft` | ✅ | Blog post content (Markdown, Google Doc link, or plain text) |
| `post_type` | ❌ | Type: `product-launch`, `technical-deep-dive`, `customer-story`, `industry-trends`, `incident-report`, `speed-week`, `birthday-week` |
| `target_audience` | ❌ | Primary audience: `developers`, `security-practitioners`, `CxO`, `general-tech`, `analysts` |
| `product_areas` | ❌ | Cloudflare products referenced (for technical accuracy validation) |
| `seo_keywords` | ❌ | Target SEO keywords for optimization check |
| `publish_date` | ❌ | Target publish date (for timeliness check on competitive/market references) |

## Key Outputs

- **Blog Review Report** (Markdown) with sections:
  1. **Publish-Readiness Score** — 1-10 scale with rationale
  2. **Executive Summary** — 3-sentence assessment: what works, what needs fixing, overall recommendation
  3. **Technical Accuracy** — flagged claims that need verification, incorrect statements, outdated information
  4. **Messaging Alignment** — does the post align with current Cloudflare positioning and approved messaging?
  5. **Readability** — reading level assessment, jargon density, paragraph length, flow
  6. **SEO Check** — title tag, meta description, keyword density, header structure, internal/external links
  7. **Brand Voice** — tone consistency with Cloudflare blog standards (authoritative but accessible)
  8. **Line-Level Feedback** — specific suggestions with severity: 🔴 Must Fix, 🟡 Should Fix, 🟢 Nice to Have
  9. **Recommended Next Steps** — prioritized action list for the author
- Saved to: `~/helix-deck/reviews/blog-review-[slug]-[date].md`

## Quality Bar Highlights

1. **Technical claims must be verifiable** — flag any performance claim, benchmark, or comparison that lacks a source or test methodology
2. **No superlatives without proof** — "fastest", "most secure", "only solution" require citations or must be removed
3. **Reading level check** — Cloudflare blog targets a technical audience but should be accessible at ~Grade 12 reading level; flag dense academic prose
4. **Link hygiene** — every product mention should link to the relevant docs or product page; flag orphan references
5. **Sensitivity scan** — flag any content that could be misread as competitive FUD, customer data exposure, or security vulnerability disclosure
