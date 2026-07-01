# Account Plan

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Strategic Planning

---

## Summary

Generates a strategic account plan deck for a named Cloudflare account. Combines Lighthouse data (products purchased, usage, billing, propensity), CRM pipeline context, public intelligence (earnings, press, tech stack), and Cloudflare product catalog to produce a structured plan covering current state, whitespace analysis, expansion strategy, competitive landscape, stakeholder map, and a 90-day action plan. Output is a presentation-ready document suitable for QBRs, account reviews, and executive sponsorship requests.

## When To Use

- "Build an account plan for [customer]"
- "I need a strategic plan for [account] for next quarter"
- QBR preparation for a strategic or enterprise account
- New AE/SE inheriting an account and needing a ramp document
- Executive sponsorship request requiring a structured account overview
- Annual/semi-annual account planning cycles

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Cloudflare account name (must exist in Lighthouse or CRM) |
| `planning_horizon` | ❌ | `90d` (default), `6mo`, `1yr` |
| `focus` | ❌ | Specific focus area: `expansion`, `retention`, `competitive-displacement`, `all` |
| `include_stakeholder_map` | ❌ | Boolean — include org chart and stakeholder analysis (default: true) |
| `executive_sponsor` | ❌ | Name of CF executive sponsor, if assigned |
| `salesforce_opp_ids` | ❌ | Specific opportunity IDs to include in pipeline section |
| `competitive_context` | ❌ | Known incumbent vendors to analyze against |

## Key Outputs

- **Account Plan Document** (Markdown + optional DOCX export) with sections:
  1. **Account Snapshot** — firmographics, vertical, CF relationship tenure, contract dates
  2. **Current State** — products deployed, usage vs. entitlements, health score, support trends
  3. **Whitespace Analysis** — products not purchased vs. propensity scores, upsell/cross-sell matrix
  4. **Competitive Landscape** — incumbent vendors, displacement opportunities, competitive talking points
  5. **Stakeholder Map** — key contacts, roles, influence level, engagement history
  6. **Expansion Strategy** — prioritized plays ranked by revenue potential and probability
  7. **Risk & Retention** — churn signals, contract renewal timeline, mitigation actions
  8. **90-Day Action Plan** — week-by-week milestones with owners and success criteria
  9. **Financial Summary** — ARR, ACV history, pipeline, forecast
  10. **Appendix** — Lighthouse data sources, methodology notes
- Saved to: `~/helix-deck/plans/[account-slug]-plan-[date].md`

## Quality Bar Highlights

1. **Lighthouse-first** — always pull live Lighthouse data before relying on cached or manually provided information
2. **No empty sections** — if data is unavailable for a section, state why and recommend how to fill the gap (e.g., "Stakeholder map requires AE input — schedule discovery session")
3. **Quantify everything** — every expansion play must include estimated ACV impact and probability
4. **Action plan must be specific** — "Schedule technical deep-dive" is not acceptable; "Schedule Workers + D1 technical deep-dive with [CTO name] by [date]" is
5. **Competitive claims must be sourced** — never assert competitive weakness without citing a battlecard, analyst report, or verified customer feedback
