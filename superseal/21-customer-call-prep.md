# Customer Call Prep

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Pre-Call

---

## Summary

Generate a pre-call preparation document that arms the rep with everything needed to run an informed, productive customer conversation. Pulls account metadata, opportunity history, and case data from Salesforce (6–7 queries covering Account, Opportunity, Case, Contact, Activity, and Contract objects). Follows the KJ customer-notes style with synthesis sections that go beyond raw data: What I want to learn, What I should be ready to say, and What I should NOT promise. Designed to take 5 minutes to read and make the rep sound like they've been on the account for a year.

## When To Use

- "Prep me for my call with [account]"
- "What do I need to know before meeting [contact]?"
- "I'm meeting [account] in 30 minutes — give me the quick brief"
- Before any customer call where you haven't spoken to the account recently
- When joining an account team and need to get smart fast
- Before an executive sponsor call where you can't afford to ask basic questions
- Before a renewal discussion where history matters
- When the AE asks the SA to join a call and you need context

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name (triggers SFDC lookup) |
| `meeting_context` | ❌ | Type of meeting: `discovery`, `check-in`, `renewal`, `escalation`, `qbr`, `executive`, `technical-review` |
| `attendees` | ❌ | Known attendees — enriched with SFDC contact data and LinkedIn if available |
| `specific_topics` | ❌ | Topics the rep knows will come up — used to focus the prep |
| `sfdc_account_id` | ❌ | Direct SFDC Account ID for faster lookup |
| `depth` | ❌ | `quick` (5 min read, key facts only) or `full` (default — comprehensive prep with synthesis) |

## Key Outputs

- **Customer Call Prep** (Markdown) with sections:
  1. **Account Snapshot** — name, industry, ACV, products, contract dates, account team, last activity
  2. **Relationship Map** — key contacts with titles, roles, last interaction date, and sentiment (if known)
  3. **Recent History** (from SFDC):
     - Open opportunities — stage, amount, close date, next steps
     - Recent cases — open/closed last 90 days, severity, resolution status
     - Recent activities — last 5 logged activities with summaries
     - Contract details — start/end dates, products, auto-renewal terms
  4. **What I Want To Learn** — 3–5 questions tailored to the meeting context that fill known intelligence gaps
  5. **What I Should Be Ready To Say** — anticipated customer questions with suggested responses, talking points on active issues
  6. **What I Should NOT Promise** — known product gaps, roadmap items under NDA, pricing commitments that need approval, anything requiring legal review
  7. **Competitive Context** — known or suspected competitive activity on the account
  8. **Meeting Agenda Suggestion** — proposed agenda based on context and open items
- Saved to: `~/helix-deck/call-prep/[account-slug]-prep-[date].md`

## Quality Bar Highlights

1. **SFDC data is the foundation** — run 6–7 queries minimum (Account, Opportunity, Case, Contact, Activity, Contract); prep without data is just guessing
2. **"What I should NOT promise" is the most important section** — reps get in trouble by over-committing; this section prevents that
3. **Recency matters** — highlight anything from the last 30 days prominently; a case opened yesterday is more relevant than a deal closed 6 months ago
4. **Meeting context changes the prep** — a renewal prep emphasizes value delivered and contract terms; a discovery prep emphasizes pain points and competitive landscape; never use a generic template
5. **5-minute read max for quick mode** — if the rep has 30 minutes before a call, they need the essentials fast; save the deep analysis for the full mode
6. **Flag knowledge gaps explicitly** — if SFDC data is sparse, say so; "No logged activities in 60 days" is itself a finding worth noting
