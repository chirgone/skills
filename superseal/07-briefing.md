# Briefing

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Meeting Preparation

---

## Summary

Generates an executive briefing document for a customer meeting. Combines account intelligence (Lighthouse, CRM, public data), attendee research, meeting context, and Cloudflare product positioning into a concise, action-oriented brief that an AE, SE, or executive can review in 5 minutes before walking into the room. Covers who's in the meeting, what they care about, what Cloudflare should propose, and what to avoid.

## When To Use

- "Prep me for my meeting with [customer] tomorrow"
- "Executive briefing for [account] QBR"
- "Who's going to be on the call and what should I know?"
- Pre-meeting prep for any customer-facing interaction
- Executive briefing for C-level customer visits
- Board meeting prep where a customer case study will be presented
- Partner meeting preparation

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name |
| `meeting_type` | ❌ | `discovery`, `qbr`, `executive-briefing`, `technical-review`, `renewal`, `expansion`, `incident-followup` |
| `attendees` | ❌ | List of expected attendees (names and/or titles) |
| `meeting_date` | ❌ | Date of the meeting (for calendar context and recency weighting) |
| `agenda` | ❌ | Known agenda items or topics |
| `cf_attendees` | ❌ | Cloudflare attendees (to tailor brief depth — exec vs. IC) |
| `previous_meeting_notes` | ❌ | Notes from the last interaction for continuity |
| `open_items` | ❌ | Known open action items or commitments |

## Key Outputs

- **Executive Briefing** (1-2 page Markdown) with sections:
  1. **Meeting Snapshot** — date, time, type, attendees (customer + CF), location/virtual
  2. **Account Context** — relationship status, ARR, contract dates, health score, recent support trends
  3. **Attendee Intelligence** — for each customer attendee: role, background, LinkedIn summary, known priorities, communication style
  4. **Key Topics & Talking Points** — what to discuss, in priority order, with supporting data
  5. **Proposals & Asks** — specific Cloudflare products/services to propose, with justification
  6. **Landmines to Avoid** — sensitive topics, known frustrations, open support escalations, competitive sensitivities
  7. **Open Items** — commitments from previous meetings with status
  8. **Success Criteria** — what does "good" look like for this meeting? 2-3 measurable outcomes
  9. **Post-Meeting Actions** — pre-drafted follow-up email skeleton
- Saved to: `~/helix-deck/briefings/[account-slug]-brief-[date].md`

## Quality Bar Highlights

1. **5-minute readable** — the entire brief must be consumable in under 5 minutes; no section longer than 5 bullet points
2. **Attendee research must be current** — LinkedIn data older than 6 months should be flagged; role changes matter
3. **Landmines are critical** — never omit known open escalations or customer frustrations; an executive walking into a meeting unaware of a P1 incident looks incompetent
4. **Proposals must be justified** — "Propose Workers" is not enough; "Propose Workers because they're running 40% of compute on Lambda and expressed interest in edge compute during the last QBR" is
5. **No classified data in external-facing briefs** — if the brief will be shared with the customer, strip internal health scores, propensity data, and pricing strategy
