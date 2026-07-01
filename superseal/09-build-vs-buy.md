# Build vs Buy vs Blend

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Strategic Analysis

---

## Summary

Evaluate whether a customer should build a capability in-house, purchase a commercial solution (Cloudflare or competitor), or blend both approaches. Produces a structured decision framework with TCO analysis, risk assessment, time-to-value comparison, and a clear recommendation. Designed for SEs and architects working with customers who are evaluating DIY alternatives to Cloudflare products, or for internal teams evaluating build-vs-buy for Cloudflare's own platform.

## When To Use

- "The customer says they can build this themselves"
- "How do I counter a build-it-yourself objection?"
- Customer evaluating open-source or DIY alternatives to Cloudflare products
- Internal team evaluating whether to build or buy a capability
- TCO comparison requested during a sales cycle
- Technical decision-maker asking for a framework to present to their CFO
- "Help me build a business case against the DIY approach"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `capability` | ✅ | What capability is being evaluated (e.g., "WAF", "CDN", "Zero Trust Network Access", "Edge Compute") |
| `context` | ❌ | `customer-facing` (default) or `internal` — adjusts framing and language |
| `customer_profile` | ❌ | Company size, industry, engineering team size, existing infrastructure |
| `diy_approach` | ❌ | Description of the build option being considered (e.g., "Nginx + ModSecurity", "custom edge proxy on K8s") |
| `buy_option` | ❌ | Commercial product(s) being considered (default: Cloudflare equivalent) |
| `time_horizon` | ❌ | TCO analysis period: `1yr`, `3yr` (default), `5yr` |
| `engineering_cost` | ❌ | Loaded cost per engineer per year (default: $200K for US, adjusted by region) |

## Key Outputs

- **Build vs Buy vs Blend Analysis** (Markdown + optional slide-ready format) with sections:
  1. **Decision Framework** — structured evaluation matrix across 8 dimensions
  2. **TCO Comparison** — 3-year cost model for Build, Buy, and Blend options
  3. **Time-to-Value** — estimated time to production for each option
  4. **Risk Assessment** — operational, security, compliance, and talent risks per option
  5. **Hidden Costs of Build** — maintenance, on-call, upgrades, talent retention, opportunity cost
  6. **Blend Scenarios** — hybrid architectures where partial build + partial buy optimizes outcomes
  7. **Decision Matrix** — weighted scorecard with customizable weights
  8. **Recommendation** — clear recommendation with confidence level and caveats
  9. **Executive Summary** — 1-slide summary for CFO/CTO presentation
- Saved to: `~/helix-deck/analysis/build-vs-buy-[capability-slug]-[date].md`

## Quality Bar Highlights

1. **Honest TCO** — include Cloudflare's actual costs, not a cherry-picked comparison; customers lose trust when they find hidden fees later
2. **Acknowledge build advantages** — there are legitimate reasons to build (control, customization, core competency); acknowledge them before countering
3. **Engineering cost must be realistic** — $200K loaded cost is US average; adjust for LATAM ($80-120K), EMEA ($150-180K), APAC (varies widely)
4. **Hidden costs are the differentiator** — the build option always looks cheaper on day 1; the skill must quantify maintenance, on-call, security patching, and talent retention costs
5. **Blend is often the right answer** — don't force a binary; many customers benefit from building on top of Cloudflare primitives (Workers, R2, D1) rather than replacing everything
