# CF1 CES Opportunity

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Opportunity Qualification

---

## Summary

Qualify a CES (Cloudflare for Enterprise Security / Cloudflare One) opportunity through a structured assessment framework. Evaluates the opportunity across technical fit, business drivers, competitive landscape, decision process, and timeline to produce a qualification scorecard, risk assessment, and recommended next steps. Ensures the deal is real, winnable, and worth pursuing before investing SE and leadership resources.

## When To Use

- "Is this CF1 opportunity real?"
- "Qualify this SASE deal for me"
- "Should we invest SE time in this opportunity?"
- New CF1/SASE opportunity assessment
- Deal review preparation for pipeline inspection
- Go/no-go decision on a competitive SASE deal
- AE requesting SE engagement — need to validate qualification first
- Manager reviewing pipeline quality for CF1 opportunities

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name |
| `opportunity_name` | ❌ | Salesforce opportunity name or description |
| `products` | ❌ | CF1 products in scope: `ZTNA`, `SWG`, `CASB`, `DLP`, `RBI`, `Magic WAN`, `Email Security`, `DEX` |
| `deal_value` | ❌ | Estimated ACV/TCV |
| `current_vendor` | ❌ | Incumbent vendor(s) being displaced or augmented |
| `champion` | ❌ | Internal champion name and title |
| `decision_maker` | ❌ | Economic buyer / budget holder |
| `timeline` | ❌ | Expected close date or evaluation timeline |
| `discovery_notes` | ❌ | Notes from discovery calls or initial conversations |
| `use_cases` | ❌ | Primary use cases: `vpn-replacement`, `saas-security`, `data-protection`, `branch-connectivity`, `contractor-access` |

## Key Outputs

- **CES Opportunity Qualification Report** (Markdown) with sections:
  1. **Qualification Scorecard** — MEDDPICC-based assessment:
     - **M**etrics: quantified business impact
     - **E**conomic Buyer: identified and engaged?
     - **D**ecision Criteria: technical and business requirements defined?
     - **D**ecision Process: procurement path, legal, security review understood?
     - **P**aper Process: contract vehicle, PO process, approvals mapped?
     - **I**dentified Pain: compelling event driving urgency?
     - **C**hampion: internal advocate with power and influence?
     - **C**ompetition: who else is in the deal and what's our position?
  2. **Technical Fit Assessment** — gap analysis between customer requirements and CF1 capabilities
  3. **Competitive Position** — where we win, where we're at risk, and where we need to differentiate
  4. **Risk Register** — top 5 deal risks with mitigation strategies
  5. **Resource Recommendation** — SE engagement level, specialist resources needed, executive sponsorship
  6. **Next Steps** — prioritized action plan with owners and deadlines
  7. **Go/No-Go Recommendation** — clear recommendation: 🟢 Pursue, 🟡 Pursue with Conditions, 🔴 Deprioritize
- Saved to: `~/helix-deck/opportunities/cf1-ces-[account-slug]-[date].md`

## Quality Bar Highlights

1. **MEDDPICC must be scored** — each element rated RED/YELLOW/GREEN with evidence; no blank fields
2. **"Champion" requires validation** — someone who takes your calls is not a champion; a champion has power, access, and motivation to drive the deal internally
3. **Competitive intel must be current** — Zscaler and Palo Alto ship updates quarterly; outdated competitive positioning loses deals
4. **Go/No-Go must be honest** — if 4+ MEDDPICC elements are RED, the recommendation must be 🔴 regardless of deal size; don't chase bad deals
5. **Technical gaps must be flagged** — if the customer needs a capability CF1 doesn't have today, say so with a timeline for roadmap delivery (if known) or a workaround
