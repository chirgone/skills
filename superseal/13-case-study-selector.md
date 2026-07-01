# Case Study Selector

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Content Enablement

---

## Summary

Surface the right 2-3 case studies for a specific customer call or meeting. Given the target account's industry, size, product interest, and deal stage, searches and ranks the Cloudflare case study library to find the most relevant proof points. Returns a prioritized shortlist with relevance rationale, key talking points from each case study, and a recommended framing for the conversation.

## When To Use

- "Which case studies should I use for my [customer] call?"
- "Find me a case study for a [industry] company evaluating [product]"
- "I need proof points for a CISO meeting about Zero Trust"
- Pre-call preparation when social proof is needed
- RFP response requiring customer references
- Executive meeting where a comparable customer story would build credibility
- BDR outreach personalization with relevant customer examples
- "What similar companies use Cloudflare for [use case]?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ❌ | Target account name (for industry and size matching) |
| `industry` | ❌ | Target industry vertical (e.g., `Telco`, `Banking`, `Retail`, `SaaS`) |
| `company_size` | ❌ | Target company size: `startup`, `mid-market`, `enterprise`, `global-2000` |
| `product_area` | ❌ | Cloudflare products being discussed: `SASE`, `CDN`, `Workers`, `WAF`, `Zero Trust`, `Bot Management` |
| `use_case` | ❌ | Specific use case: `migration-from-legacy`, `multi-cloud`, `compliance`, `performance`, `security-consolidation` |
| `audience` | ❌ | Who's on the call: `CISO`, `CTO`, `VP-Engineering`, `Developer`, `Network-Architect` |
| `region` | ❌ | Preferred case study region (customers prefer references from their own region) |
| `competitors_mentioned` | ❌ | Known competitors in the deal (for displacement case studies) |

## Key Outputs

- **Case Study Recommendations** (Markdown) with:
  1. **Top 3 Recommended Case Studies** — each with:
     - Company name and industry
     - Relevance score (1-10) with justification
     - Key metrics and outcomes from the case study
     - 3 talking points customized for this conversation
     - Quote or pull-quote to use in the meeting
     - Link to full case study
  2. **Honorable Mentions** — 2-3 additional options if the top 3 don't resonate
  3. **Framing Guide** — how to introduce each case study naturally in conversation (not "let me read you a case study" but "a similar company in your space saw...")
  4. **Gap Alert** — if no good case study match exists, flag the gap and suggest alternative proof points (analyst reports, benchmarks, POC data)
- Saved to: `~/helix-deck/case-studies/selector-[account-slug]-[date].md`

## Quality Bar Highlights

1. **Relevance over recency** — a 2-year-old case study from the same industry beats a brand-new one from an unrelated vertical
2. **Region matters** — a LATAM telco prospect wants to hear about LATAM telco customers, not US SaaS companies; prioritize regional matches
3. **Never recommend a case study you haven't verified exists** — check that the link works and the content matches the summary
4. **Metrics must be accurate** — if the case study says "50% reduction in latency", quote that exactly; don't round or embellish
5. **Maximum 3 recommendations** — more choices paralyze the rep; pick the best 3 and commit
