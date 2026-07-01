# QBR Prep

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Account Management

---

## Summary

Quarterly Business Review preparation document for customer and partner engagements. Supports three modes: customer QBR (backward-looking value delivered + forward-looking roadmap), partner QBR (pipeline contribution, deal velocity, certification progress), and business plan (forward-looking 12-month strategic plan with quarterly milestones). Pulls SFDC data for deal history, case resolution metrics, and product adoption. Runs cross-sell analysis using the product-mapping methodology to identify expansion opportunities. Produces presentation-ready content that can be exported to slides or used as a Markdown briefing doc.

## When To Use

- "Build a QBR for [account]"
- "Prepare the quarterly review for [partner]"
- "Create a 12-month business plan for [account]"
- Before any scheduled QBR with a customer or partner
- When an AM or CSM needs a structured review of the last quarter
- When building a forward-looking business plan for a strategic account
- When a partner manager needs to present pipeline and performance data
- When preparing for an executive sponsor review
- "What's the story for [account] this quarter?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer or partner name |
| `mode` | ✅ | `customer` (default), `partner`, or `business_plan` |
| `quarter` | ❌ | Quarter to review: `Q1`, `Q2`, `Q3`, `Q4` — defaults to current quarter |
| `fiscal_year` | ❌ | Fiscal year — defaults to current FY |
| `include_cross_sell` | ❌ | If `true` (default), runs cross-sell analysis from product-mapping methodology |
| `output_format` | ❌ | `markdown` (default), `slides` (SlideData[] JSON), or `both` |
| `sfdc_account_id` | ❌ | Direct SFDC Account ID for faster lookup |

## Key Outputs

- **Customer QBR** with sections:
  1. **Executive Summary** — quarter-at-a-glance: key wins, challenges, and priorities
  2. **Value Delivered** — metrics showing Cloudflare's impact: threats blocked, performance improvements, uptime, cost savings
  3. **Product Adoption** — products deployed, usage trends, feature adoption rates
  4. **Support & Case Review** — cases opened/closed, MTTR, CSAT, escalation history
  5. **Roadmap Alignment** — Cloudflare product roadmap items relevant to this customer's priorities
  6. **Cross-Sell Recommendations** — expansion opportunities identified via product-mapping analysis
  7. **Next Quarter Priorities** — agreed-upon goals and success criteria for the next 90 days
- **Partner QBR** with sections:
  1. **Pipeline Contribution** — deals registered, pipeline generated, revenue closed
  2. **Deal Velocity** — average cycle time, conversion rates by stage
  3. **Certification Progress** — certifications earned, training completed, gaps
  4. **MDF Utilization** — MDF allocated vs. spent, ROI on funded activities
  5. **Co-Sell Activity** — joint calls, POCs, customer engagements
  6. **Next Quarter Plan** — target pipeline, planned activities, certification goals
- **Business Plan** (12-month) with sections:
  1. **Strategic Vision** — where we want this account/partnership to be in 12 months
  2. **Quarterly Milestones** — Q1–Q4 objectives, key results, and success metrics
  3. **Investment Requirements** — resources, MDF, executive engagement, technical support needed
  4. **Risk Factors** — competitive threats, budget cycles, organizational changes
- Saved to: `~/helix-deck/qbr/[account-slug]-qbr-[quarter]-[year].md`

## Quality Bar Highlights

1. **Data-driven, not anecdotal** — every claim about value delivered must be backed by metrics from the platform, SFDC, or Lighthouse; "we had a great quarter" is not a QBR
2. **Cross-sell analysis is not optional** — every customer QBR must include expansion recommendations; a QBR without a cross-sell section is a missed opportunity
3. **Forward-looking sections are as important as backward-looking** — customers attend QBRs to plan the future, not just review the past; next quarter priorities must be specific and actionable
4. **Partner QBRs must include deal velocity** — pipeline volume without conversion data is misleading; always show the funnel, not just the top
5. **Business plan milestones must be measurable** — "deepen the relationship" is not a milestone; "deploy Zero Trust to 5,000 users by Q3" is
6. **Output format matches the audience** — internal reviews use Markdown; customer-facing QBRs use slides; always produce the format that will actually be presented
