# Close Plan

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Deal Execution

---

## Summary

Single-deal forensic review for close execution. Tactical, not strategic — this is about getting a specific deal across the finish line, not building a long-term account plan. Performs a Deal Memory sweep across the operator's Gmail, GChat, and Calendar to reconstruct the deal's recent history. Validates MEDDPICC completeness, SE Technical Validation status, and stage-gate criteria. Asks 7 Challenger questions to stress-test the close plan. Outputs either a structured Markdown close plan or a slides deck based on ACV threshold (>$100K gets slides). Every output includes a risk-adjusted close date and specific next actions with owners.

## When To Use

- "Build a close plan for [deal]"
- "What do I need to close [deal] this quarter?"
- "This deal is slipping — what am I missing?"
- Deal is in Stage 4+ and needs a clear path to close
- Forecast call prep — need to defend a commit
- Manager asks "walk me through how this deal closes"
- Deal has been in the same stage for more than 30 days
- Multiple stakeholders involved and sequence of events is unclear
- SE needs to validate that technical requirements are met before paper
- "Is this deal real or am I fooling myself?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `deal_name` | ✅ | Opportunity name or SFDC Opportunity ID |
| `account_name` | ❌ | Account name — auto-resolved from deal if omitted |
| `close_date_target` | ❌ | Target close date — if omitted, uses SFDC close date |
| `acv` | ❌ | Deal ACV — auto-pulled from SFDC if omitted |
| `output_format` | ❌ | `markdown` (default) or `slides` (auto-selected if ACV > $100K) |
| `deal_memory_sweep` | ❌ | If `true` (default), scans Gmail, GChat, Calendar for deal context from last 90 days |
| `include_meddpicc` | ❌ | If `true` (default), runs full MEDDPICC validation with gap analysis |

## Key Outputs

- **Close Plan** (Markdown or Slides) with sections:
  1. **Deal Snapshot** — account, ACV, products, stage, close date, age, owner, SE
  2. **Deal Memory Timeline** — reconstructed from Gmail/GChat/Calendar: key emails, meetings, commitments, and decisions from last 90 days
  3. **MEDDPICC Validation** — each element scored Green/Yellow/Red:
     - Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Paper Process, Champion, Competition
  4. **SE Technical Validation** — POC status, technical requirements met, blockers, SE confidence rating
  5. **Stage Validation** — does the deal actually meet criteria for its current stage? Recommendation to advance, hold, or regress
  6. **7 Challenger Questions:**
     - Why will they buy from us (not just "buy")?
     - What happens if they do nothing?
     - Who can kill this deal and have we talked to them?
     - What's the paper process and have we confirmed it?
     - Is our champion actually a champion or just a coach?
     - What does the competition know that we don't?
     - If this slips, what's the real reason?
  7. **Risk-Adjusted Close Date** — realistic close date based on evidence, not hope
  8. **Close Actions** — sequenced next steps with owners and dates: mutual action plan format
- Saved to: `~/helix-deck/close-plans/[deal-slug]-close-plan-[date].md`

## Quality Bar Highlights

1. **Deal Memory is non-negotiable** — the sweep of Gmail/GChat/Calendar is what makes this forensic, not speculative; skip it and you're guessing
2. **MEDDPICC gaps must be specific** — "Champion: Yellow" is not enough; specify what's missing and what action closes the gap
3. **Stage validation must be honest** — if the deal doesn't meet stage criteria, say so; moving deals back a stage is better than missing forecast
4. **Every action needs an owner and a date** — "follow up with procurement" is not actionable; "[AE name] sends MSA redlines to [contact] by [date]" is
5. **Challenger questions are for the rep, not the customer** — these questions force the rep to confront uncomfortable truths about their deal
6. **ACV threshold drives output format** — deals over $100K get slides because they're likely reviewed in forecast calls; smaller deals get Markdown for speed
