# CXTP EBC Advisor

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / EBC

---

## Summary

Strategic advisory for Executive Briefing Center engagements. Provides material validation for executive readiness across 5 criteria (relevance, personalization, business impact, competitive differentiation, and ask clarity). Builds a common-thread narrative that connects every session into a coherent story arc. Performs stakeholder-to-presenter matching based on seniority, domain expertise, and customer priorities. Tracks post-EBC follow-up compliance to ensure the engagement converts into pipeline momentum rather than just a good meeting. Designed for the CXTP (Customer Experience & Technology Programs) team and account teams preparing for high-stakes executive briefings.

## When To Use

- "Review my EBC materials for [account]"
- "Help me prepare for the [account] executive briefing"
- "Match our presenters to their executives"
- Before any Executive Briefing Center engagement
- When the EBC agenda is set but materials haven't been validated
- When multiple Cloudflare presenters need to deliver a unified narrative
- After an EBC to track follow-up compliance and action item completion
- When the CXTP team needs a quality check on EBC readiness
- "Are we ready for the [account] EBC next week?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Customer account name |
| `ebc_date` | ✅ | Date of the Executive Briefing |
| `customer_attendees` | ✅ | List of customer executives attending (names + titles) |
| `cloudflare_presenters` | ❌ | Proposed Cloudflare presenters (names + topics) |
| `agenda` | ❌ | Draft EBC agenda with session topics and time slots |
| `materials` | ❌ | Uploaded presentation decks, demos, or briefing docs for validation |
| `ebc_objectives` | ❌ | What the account team wants to achieve from this EBC |
| `mode` | ❌ | `prep` (default — pre-EBC validation) or `follow-up` (post-EBC compliance tracking) |

## Key Outputs

- **EBC Advisory Report** (Markdown) with sections:
  1. **Readiness Score** — overall rating: Ready / Needs Work / Not Ready — with specific gaps
  2. **Material Validation** — each presentation scored against 5 criteria:
     - Relevance — does this address the customer's stated priorities?
     - Personalization — is this customized or a generic pitch?
     - Business Impact — does it quantify value in customer's terms?
     - Competitive Differentiation — does it address known competitive alternatives?
     - Ask Clarity — is there a clear next step or call to action?
  3. **Common-Thread Narrative** — the unifying story arc connecting all sessions; ensures the EBC doesn't feel like disconnected presentations
  4. **Stakeholder-to-Presenter Match** — recommended pairing of customer execs to Cloudflare presenters based on seniority alignment, domain expertise, and customer priorities
  5. **Gap Analysis** — missing topics, unaddressed customer priorities, or audience members without a tailored session
  6. **Post-EBC Follow-Up Tracker** (follow-up mode):
     - Action items from the EBC with owners and due dates
     - Follow-up compliance: what was promised vs. what was delivered
     - Days since EBC vs. follow-up completion rate
     - Escalation flags for overdue items
  7. **Recommendations** — specific improvements, additions, or changes before the EBC
- Saved to: `~/helix-deck/ebc/[account-slug]-ebc-advisory-[date].md`

## Quality Bar Highlights

1. **Executive readiness means no generic decks** — if a presentation could be given to any customer without changes, it fails validation; every slide must reference the customer's specific context
2. **Seniority matching is critical** — a VP-level customer exec should not sit through a presentation from an IC without a strategic framing from a Cloudflare exec; flag mismatches
3. **Common-thread narrative prevents "presentation fatigue"** — each session must build on the previous one; without a thread, EBCs feel like a series of vendor pitches
4. **Post-EBC follow-up is where deals are won or lost** — the EBC itself is just the setup; track every commitment and flag anything overdue within 5 business days
5. **The ask must be explicit** — every EBC should end with a clear, agreed-upon next step; if the agenda doesn't include a closing session with an ask, flag it immediately
