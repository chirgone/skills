# Expansion Finder

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Expansion

---

## Summary

Whitespace analysis for existing Cloudflare customers. Maps current product adoption against the full Cloudflare portfolio to identify upsell and cross-sell opportunities. Cross-references external signals — hiring patterns, M&A activity, digital transformation initiatives, regulatory changes, and technology stack shifts — to validate expansion timing. Scores each opportunity as High, Medium, or Low based on fit, timing, and estimated revenue impact. Produces a prioritized expansion playbook with specific talk tracks and recommended entry points for each opportunity.

## When To Use

- "What else can we sell to [account]?"
- "Find expansion opportunities for [account]"
- "Run a whitespace analysis for my top 10 accounts"
- "Where's the cross-sell potential in [account]?"
- When an account is up for renewal and you want to expand the deal
- When a customer's usage has grown and they may need additional products
- When preparing for a QBR and need to present expansion recommendations
- After a successful POC or deployment — what's next?
- When building territory plan and need to identify expansion pipeline
- When a customer announces a digital transformation, cloud migration, or zero trust initiative

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name (triggers SFDC + Lighthouse lookup) |
| `current_products` | ❌ | Products currently purchased — auto-pulled from SFDC/Lighthouse if omitted |
| `industry` | ❌ | Customer's industry — used for industry-specific expansion patterns |
| `acv` | ❌ | Current ACV — used to size expansion opportunities |
| `signals` | ❌ | Known external signals: `hiring`, `m&a`, `cloud-migration`, `zero-trust`, `compliance`, `international-expansion` |
| `batch_mode` | ❌ | If `true`, accepts a list of accounts and runs whitespace analysis across all of them |
| `sfdc_account_id` | ❌ | Direct SFDC Account ID for faster lookup |

## Key Outputs

- **Expansion Analysis** (Markdown) with sections:
  1. **Current Footprint** — products purchased, usage levels, contract value, deployment scope
  2. **Whitespace Map** — full Cloudflare portfolio vs. current adoption, organized by product family:
     - Application Services (CDN, WAF, Bot Management, API Gateway, etc.)
     - Zero Trust / SASE (Access, Gateway, CASB, DLP, Browser Isolation, etc.)
     - Network Services (Magic Transit, Magic WAN, Spectrum, Argo, etc.)
     - Developer Platform (Workers, Pages, R2, D1, Durable Objects, etc.)
     - Email Security (Area 1)
  3. **Expansion Opportunities** — each scored High / Medium / Low:
     - Product recommendation and rationale
     - Fit score — how well the product matches their architecture and use case
     - Timing signals — external events that make this relevant now
     - Estimated revenue impact — T-shirt size (S/M/L/XL) based on company profile
     - Entry point — who to talk to and what to lead with
  4. **External Signals** — hiring trends, M&A activity, technology announcements, regulatory changes that indicate expansion readiness
  5. **Competitive Displacement Opportunities** — products where the customer is using a competitor that Cloudflare can replace
  6. **Recommended Talk Tracks** — conversation starters for the top 3 expansion opportunities
  7. **Prioritized Action Plan** — sequenced next steps: which opportunity to pursue first and why
- Saved to: `~/helix-deck/expansion/[account-slug]-expansion-[date].md`

## Quality Bar Highlights

1. **Current adoption must be verified** — never recommend a product the customer already owns; always validate the current footprint against SFDC and Lighthouse
2. **Timing signals matter more than fit** — a perfectly fitting product with no trigger event will stall; prioritize opportunities where external signals create urgency
3. **Revenue sizing must be grounded** — "Large opportunity" is meaningless; estimate based on company size, industry benchmarks, and comparable deals
4. **Entry point is critical** — knowing what to sell is only half the battle; knowing who to talk to and what message resonates with that persona is what makes it actionable
5. **Batch mode must rank-stack** — when analyzing multiple accounts, sort by opportunity size × probability to focus rep time on the highest-impact accounts
6. **Competitive displacement is the highest-value play** — replacing an incumbent generates more ACV than adding a net-new capability; always flag these prominently
