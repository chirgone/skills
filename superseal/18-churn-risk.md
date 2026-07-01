# Churn Risk

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Renewals

---

## Summary

Renewal churn-risk assessment designed for AMs, RAMs, CSMs, and renewal managers. Adapted from Liliana Ahmed's renewals-os methodology. Classifies risk across 5 categories: Infrastructure & Network, Product, Account Management, CS & Support, and Business Reasons. Scores each category 0–3 (None / Low / Medium / High) and produces an aggregate churn-risk rating. Outputs a save plan with immediate, 30-day, and 90-day actions. Pulls live SFDC data — contracts, open cases, recent opportunities, and renewal pipeline — to ground every assessment in real account signals, not gut feel.

## When To Use

- "Is this renewal at risk?"
- "Build a churn-risk assessment for [account]"
- "What's the save plan for [account]?"
- Renewal is within 120 days and no health check has been run
- CSM flags declining usage or engagement
- Support case volume has spiked in the last 90 days
- Champion or economic buyer has changed roles
- Competitor displacement detected or mentioned in calls
- Manager asks for a portfolio-level risk view across renewals
- Preparing for a renewal strategy meeting with AM + CSM + manager

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name (used for SFDC lookup) |
| `renewal_date` | ❌ | Contract renewal date — auto-pulled from SFDC if omitted |
| `acv` | ❌ | Annual contract value — auto-pulled from SFDC if omitted |
| `risk_signals` | ❌ | Known risk signals: `champion_left`, `competitor_eval`, `budget_cut`, `usage_decline`, `support_escalation` |
| `csm_notes` | ❌ | Free-text notes from CSM on account health |
| `include_portfolio` | ❌ | If `true`, runs churn-risk across all renewals in next 120 days for the owner |
| `sfdc_account_id` | ❌ | Salesforce Account ID for direct lookup — bypasses name search |

## Key Outputs

- **Churn Risk Assessment** (Markdown) with sections:
  1. **Account Snapshot** — account name, ACV, renewal date, days to renewal, contract term, products
  2. **Risk Scoring Matrix** — 5 categories scored 0–3:
     - Infrastructure & Network — architecture complexity, migration difficulty, integration depth
     - Product — usage trends, feature adoption, unresolved product gaps, roadmap alignment
     - Account Management — relationship health, champion stability, engagement frequency
     - CS & Support — case volume trend, CSAT scores, escalation history, time-to-resolution
     - Business Reasons — budget pressure, M&A activity, leadership changes, strategic pivots
  3. **Aggregate Risk Rating** — weighted composite: Low (0–4) / Medium (5–8) / High (9–12) / Critical (13–15)
  4. **Key Risk Drivers** — top 3 factors contributing to risk with evidence
  5. **Save Plan:**
     - Immediate (this week) — escalation calls, executive engagement, quick wins
     - 30-day actions — product adoption push, value realization sessions, competitive displacement defense
     - 90-day actions — expansion positioning, multi-year incentive, strategic alignment
  6. **SFDC Data Pull** — contracts, open cases, recent opps, last activity date, NPS/CSAT if available
  7. **Renewal Forecast Recommendation** — commit / best-case / at-risk with justification
- Saved to: `~/helix-deck/renewals/[account-slug]-churn-risk-[date].md`

## Quality Bar Highlights

1. **Every risk score must cite evidence** — "Medium risk" without data is useless; link to specific cases, usage metrics, or relationship gaps
2. **Pull SFDC first, then assess** — never score risk without checking contracts, cases, and opportunity history; gut feel alone is not acceptable
3. **Save plan must be actionable** — "improve relationship" is not an action; "schedule exec-to-exec call with [name] by [date]" is
4. **Champion stability is the #1 predictor** — always check if the economic buyer or champion has changed; if unknown, flag as risk
5. **Days-to-renewal determines urgency** — inside 90 days with High risk = immediate escalation to manager; never let this sit
6. **Portfolio mode must rank-stack** — when running across multiple renewals, sort by risk × ACV to prioritize manager attention
