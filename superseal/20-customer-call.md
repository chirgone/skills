# Customer Call

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Post-Call

---

## Summary

Turn raw post-call notes — voice memos, bullet points, stream-of-consciousness text — into a clean, structured Customer Call Report. Researches attendee titles via LinkedIn when not provided. Produces structured Markdown with attendees (names + titles), topical notes organized by theme, action items with owners and due dates, and follow-up recommendations. Supports multiple call types: Check-In, QBR, AI Exchange, Discovery, EBC, Post-Incident, and Partnership Review — each with tailored section templates.

## When To Use

- "Clean up my call notes from the [account] meeting"
- "Turn these notes into a proper call report"
- "I just got off a call with [account] — here's what we discussed"
- After any customer-facing call that needs documentation
- When raw notes need to be shared with the broader account team
- Before logging call notes into SFDC
- When a manager or SE needs context on what happened in a call they missed
- After an EBC or QBR that requires formal documentation
- Post-incident calls where precise documentation matters for follow-up

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `raw_notes` | ✅ | Unstructured notes from the call — any format: bullets, paragraphs, voice transcript |
| `account_name` | ✅ | Customer account name |
| `call_type` | ❌ | `check-in`, `qbr`, `ai-exchange`, `discovery`, `ebc`, `post-incident`, `partnership-review` — defaults to `check-in` |
| `attendees` | ❌ | List of attendee names — titles auto-researched if not provided |
| `call_date` | ❌ | Date of the call — defaults to today |
| `opportunity_name` | ❌ | Associated opportunity for SFDC linking |
| `include_linkedin` | ❌ | If `true` (default), researches attendee titles via LinkedIn |

## Key Outputs

- **Customer Call Report** (Markdown) with sections:
  1. **Call Header** — account name, call type, date, duration (if known), opportunity link
  2. **Attendees** — name, title, company, role in the call (presenter / participant / executive sponsor)
  3. **Executive Summary** — 2-3 sentence overview of the call's purpose and outcome
  4. **Topical Notes** — organized by theme (not chronologically), each with:
     - Topic heading
     - Key discussion points
     - Customer statements (direct quotes when available)
     - Cloudflare position or response
  5. **Action Items** — table format: action, owner (Cloudflare or customer), due date, status
  6. **Follow-Up Recommendations** — suggested next steps, escalations, or internal actions
  7. **SFDC Activity Log** — condensed version suitable for pasting into SFDC activity notes
- Saved to: `~/helix-deck/call-reports/[account-slug]-call-[date].md`

## Quality Bar Highlights

1. **Organize by topic, not timeline** — chronological notes are hard to scan; group by theme so readers find what they need fast
2. **Attendee titles matter** — a call with a Director vs. a VP changes the follow-up strategy; always research titles if not provided
3. **Direct customer quotes are gold** — preserve exact customer language when the notes contain it; these are invaluable for deal strategy
4. **Action items must have owners** — an action item without an owner is a wish, not a commitment; flag any items missing ownership
5. **Call type drives template** — a Discovery call report emphasizes pain points and MEDDPICC; a Post-Incident report emphasizes root cause and remediation timeline; don't use a generic template
6. **SFDC-ready summary is mandatory** — always produce a condensed version that can be pasted directly into Salesforce without reformatting
