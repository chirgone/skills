# POC Plan

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Technical Validation

---

## Summary

Binding two-phase proof-of-concept plan that treats a POC as a structured evaluation, not an open-ended trial. Phase 1 defines success criteria with measurable tokens — specific, quantifiable thresholds that determine pass/fail (e.g., "TTFB < 200ms at p95 from 3 regions," "100% of SSO logins succeed within 2 seconds"). Phase 2 documents results against those criteria and produces a deterministic recommendation: proceed, conditional-proceed, extend, or disqualify. Generates two outputs: a customer-facing POC plan (shared with the prospect) and an internal SE working file (with risk assessment, competitive notes, and fallback strategies). Enterprise mode adds multi-workstream tracking, executive checkpoint scheduling, and vendor comparison matrices.

## When To Use

- "Build a POC plan for [account]"
- "We need to set up a proof of concept for [product] at [company]"
- "Define success criteria for the [account] evaluation"
- When a deal requires technical validation before purchase
- When a customer insists on "trying before buying"
- When the SE needs a structured evaluation framework instead of ad-hoc testing
- When a competitive bake-off requires clear, objective comparison criteria
- When a POC is at risk of scope creep and needs boundaries
- "This POC has been running for 3 months with no conclusion — help me close it"
- When enterprise deals require multi-workstream evaluation with executive checkpoints

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name |
| `products` | ✅ | Cloudflare products being evaluated |
| `use_case` | ✅ | Primary use case being validated: `zero-trust-access`, `app-security`, `performance`, `email-security`, `network-services`, etc. |
| `success_criteria` | ❌ | Customer-stated requirements — if omitted, skill proposes criteria based on use case and industry best practices |
| `duration` | ❌ | POC duration: `2-week` (default), `30-day`, `60-day`, `90-day` (enterprise) |
| `competitors` | ❌ | Other vendors in the evaluation — adds comparison framework |
| `enterprise_mode` | ❌ | If `true`, enables multi-workstream tracking, executive checkpoints, and extended evaluation framework |
| `customer_contacts` | ❌ | Technical and business contacts on the customer side for the POC |

## Key Outputs

- **Customer-Facing POC Plan** (Markdown + PDF export):
  1. **POC Overview** — objective, scope, duration, key contacts (both sides)
  2. **Phase 1: Success Criteria Definition**
     - Measurable tokens for each evaluation area (performance, security, usability, integration)
     - Pass/fail thresholds with specific numbers, not subjective ratings
     - Testing methodology and data collection approach
     - Environment requirements and prerequisites
  3. **Timeline & Milestones**
     - Kickoff meeting and environment setup (Week 1)
     - Configuration and initial testing (Week 1–2)
     - Production traffic validation (Week 2–3)
     - Results review and recommendation (Week 3–4)
  4. **Phase 2: Results & Recommendation**
     - Results matrix: each criterion with target, actual, and pass/fail
     - Deterministic recommendation:
       - **Proceed** — all criteria met, ready for procurement
       - **Conditional-Proceed** — most criteria met, specific items need resolution
       - **Extend** — insufficient data, defined additional testing period
       - **Disqualify** — criteria not met, documented reasons
  5. **Escalation Path** — what happens if blockers arise during the POC
- **Internal SE Working File** (Markdown, not shared with customer):
  1. **Risk Assessment** — technical risks, competitive risks, political risks
  2. **Competitive Notes** — how to position against specific competitors in the evaluation
  3. **Fallback Strategies** — what to do if specific criteria aren't met
  4. **Internal Resources Needed** — product team engagement, escalation contacts, lab environments
  5. **Close Plan** — how to convert POC success into a purchase decision
- Saved to: `~/helix-deck/poc/[account-slug]-poc-plan-[date].md` (customer) + `~/helix-deck/poc/[account-slug]-poc-internal-[date].md` (SE file)

## Quality Bar Highlights

1. **Success criteria must be measurable** — "good performance" is not a success criterion; "TTFB < 200ms at p95 measured from US-East, EU-West, and APAC endpoints over 7 days" is
2. **Duration must be bounded** — an open-ended POC is a free trial, not an evaluation; always set a hard end date with an explicit decision checkpoint
3. **The recommendation must be deterministic** — the results either meet criteria or they don't; eliminate ambiguity by defining pass/fail before testing begins
4. **Two documents, two audiences** — the customer-facing plan is collaborative and professional; the internal SE file is candid about risks, competitive tactics, and fallback strategies; never mix them
5. **Scope creep is the #1 POC killer** — if the customer adds requirements mid-POC, flag them as out-of-scope for this evaluation and offer to address in a follow-up phase
6. **Enterprise mode is for deals over $250K** — multi-workstream POCs with executive checkpoints are expensive to run; only enable enterprise mode when the deal size justifies the investment
