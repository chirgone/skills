# Business Case

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Deal Acceleration

---

## Summary

Generate a customer-internal business case document that a champion can use to secure budget approval from their CFO, CTO, or procurement team. Produces a structured document with problem statement, proposed solution, financial justification (ROI, TCO, payback period), risk analysis, and implementation timeline. Written from the customer's perspective, not Cloudflare's — this is a document the champion presents internally, not a Cloudflare sales pitch.

## When To Use

- "Help my champion build an internal business case"
- "The deal is stalled at procurement — they need a business case"
- "How do I help [contact] justify this purchase internally?"
- Champion needs to present to a budget committee or CFO
- Deal stuck at "budget not approved" stage
- Multi-product deal requiring cross-functional budget alignment
- Customer's procurement process requires a formal business case document
- Renewal at risk due to budget scrutiny — need to re-justify value

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name |
| `products` | ✅ | Cloudflare products in scope (e.g., `SASE`, `Workers`, `WAF + Bot Management`) |
| `deal_value` | ❌ | Annual deal value or total contract value |
| `champion_name` | ❌ | Name of the internal champion presenting the case |
| `champion_title` | ❌ | Champion's role (determines what financial metrics to emphasize) |
| `decision_maker` | ❌ | Who approves the budget (CFO, CTO, VP Eng, etc.) |
| `current_solution` | ❌ | What the customer is using today (for cost comparison) |
| `pain_points` | ❌ | Known business problems the solution addresses |
| `timeline` | ❌ | Desired implementation timeline |
| `industry` | ❌ | Customer's industry (for relevant benchmarks and proof points) |

## Key Outputs

- **Customer-Internal Business Case** (Markdown + DOCX export) with sections:
  1. **Executive Summary** — 1-page overview: problem, solution, financial impact, ask
  2. **Business Problem** — quantified pain points with industry benchmarks
  3. **Proposed Solution** — what's being purchased and why (customer-voice, not vendor-voice)
  4. **Financial Justification:**
     - ROI calculation with conservative, moderate, and aggressive scenarios
     - TCO comparison: current state vs. proposed state (3-year view)
     - Payback period analysis
     - Cost-of-inaction analysis (what happens if we don't do this?)
  5. **Risk Analysis** — implementation risks, vendor risks, and mitigation strategies
  6. **Implementation Plan** — high-level timeline with milestones
  7. **Proof Points** — industry-relevant case studies, benchmarks, and references
  8. **Recommendation** — clear ask with budget amount, approval timeline, and next steps
  9. **Appendix** — detailed calculations, assumptions, and data sources
- Saved to: `~/helix-deck/business-cases/[account-slug]-bcase-[date].md`

## Quality Bar Highlights

1. **Customer voice, not vendor voice** — this document must read as if the champion wrote it; no "Cloudflare is the leader in..." language
2. **Conservative ROI by default** — always lead with the conservative scenario; overpromising kills deals at procurement
3. **Quantify the cost of inaction** — every business case must include "what happens if we do nothing" with real numbers (breach costs, downtime costs, productivity loss)
4. **Industry benchmarks must be cited** — use Ponemon, Gartner, Forrester, or published Cloudflare data; never fabricate statistics
5. **Champion must be able to present this alone** — the document must stand on its own without a Cloudflare person in the room explaining it
