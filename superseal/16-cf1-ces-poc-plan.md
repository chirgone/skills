# CF1 CES POC Plan

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Technical Validation

---

## Summary

Generate a CES (Cloudflare One) proof-of-concept plan with defined success criteria, timeline, technical scope, resource requirements, and evaluation framework. Produces a document that both the customer and Cloudflare team can align on before starting a POC, preventing scope creep, unclear success metrics, and "POC purgatory." Covers ZTNA, SWG, CASB, DLP, RBI, Magic WAN, Email Security, and DEX evaluation scenarios.

## When To Use

- "The customer wants a POC for CF1"
- "Plan a Zero Trust proof of concept"
- "We need a structured POC plan before we start the evaluation"
- Customer has agreed to evaluate CF1 and needs a structured plan
- SE preparing to kick off a SASE/ZTNA proof of concept
- Deal requires technical validation before procurement approval
- Competitive bake-off where a structured POC demonstrates professionalism
- "How do we avoid this POC dragging on for 6 months?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name |
| `products` | ✅ | CF1 products to evaluate: `ZTNA`, `SWG`, `CASB`, `DLP`, `RBI`, `Magic WAN`, `Email Security`, `DEX` |
| `use_cases` | ❌ | Primary use cases for the POC (e.g., `vpn-replacement`, `saas-security`, `branch-connectivity`) |
| `user_count` | ❌ | Number of users in the POC pilot group (default: 50-100) |
| `duration` | ❌ | POC duration: `2-weeks`, `30-days` (default), `60-days` |
| `success_criteria` | ❌ | Customer-defined success criteria (if known) |
| `current_vendor` | ❌ | Incumbent solution being compared against |
| `customer_contacts` | ❌ | Customer technical contacts for the POC |
| `cf_se` | ❌ | Assigned Cloudflare SE |
| `integration_requirements` | ❌ | Required integrations: `Okta`, `Azure AD`, `SIEM`, `SOAR`, `MDM`, etc. |

## Key Outputs

- **CES POC Plan** (Markdown + DOCX export) with sections:
  1. **Executive Summary** — 1-page overview: objectives, scope, timeline, success criteria
  2. **Scope Definition:**
     - In-scope products and use cases
     - Out-of-scope items (explicitly listed to prevent scope creep)
     - Pilot user group definition and selection criteria
  3. **Success Criteria** — measurable, time-bound criteria:
     - Technical: latency, throughput, uptime, policy enforcement accuracy
     - Operational: deployment time, admin UX, policy management efficiency
     - User Experience: end-user satisfaction, DEX scores, help desk ticket volume
  4. **Architecture & Design:**
     - Target architecture diagram
     - Integration points (IdP, SIEM, MDM, existing infrastructure)
     - DNS, routing, and traffic steering design
  5. **Implementation Plan** — week-by-week breakdown:
     - Week 1: Environment setup, IdP integration, initial policies
     - Week 2: Pilot group onboarding, baseline measurements
     - Week 3: Full use case testing, edge cases, load testing
     - Week 4: Results collection, analysis, executive readout
  6. **Resource Requirements:**
     - Customer resources needed (contacts, access, time commitment)
     - Cloudflare resources (SE, TAM, specialist, CSM)
  7. **Risk & Mitigation** — common POC risks and prevention strategies
  8. **Evaluation Framework** — scoring rubric for objective comparison
  9. **Exit Criteria** — what triggers early termination (success or failure)
  10. **Post-POC Path** — production rollout plan if POC succeeds
- Saved to: `~/helix-deck/pocs/cf1-poc-[account-slug]-[date].md`

## Quality Bar Highlights

1. **Success criteria must be measurable** — "works well" is not a success criterion; "ZTNA connection established in < 2 seconds for 95th percentile of users" is
2. **Scope must have explicit boundaries** — every POC plan must list what is OUT of scope; this prevents "can we also test X?" scope creep
3. **Duration must be fixed** — 30 days is the default; anything over 60 days is POC purgatory and must be flagged as a risk
4. **Pilot group must be representative** — 50 users from IT is not a real POC; include users from different locations, roles, and use cases
5. **Exit criteria protect both sides** — define when the POC is a clear success (proceed to purchase) and a clear failure (stop investing time) upfront
