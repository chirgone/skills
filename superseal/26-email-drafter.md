# Email Drafter

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Outreach

---

## Summary

Write personalized outreach emails and multi-step cadence sequences for sales engagement. Supports 7 email types: Cold Outreach, Follow-Up, Nurture, Event Invite, Partnership, Re-Engagement, and Expansion. Generates 5-step cadence sequences with varied angles, escalating urgency, and breakup emails. Subject lines capped at 8 words. Emails are written in the operator's voice, not Cloudflare marketing voice — conversational, specific, and value-led. Every email includes a single, clear call-to-action. Never sends automatically — always produces drafts for review.

## When To Use

- "Write a cold email to [persona] at [company]"
- "Build an outreach cadence for [account]"
- "Draft a follow-up after my meeting with [contact]"
- "Write a re-engagement email — they've gone dark"
- "I need an event invite email for [event]"
- When starting outreach to a new prospect
- When a deal has stalled and you need to re-engage
- When building a multi-touch cadence for a target account
- After an event or webinar for follow-up outreach
- When expanding into a new buying center within an existing customer

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `recipient_name` | ✅ | Name of the person you're emailing |
| `recipient_title` | ✅ | Title or role of the recipient |
| `company` | ✅ | Recipient's company name |
| `email_type` | ✅ | `cold-outreach`, `follow-up`, `nurture`, `event-invite`, `partnership`, `re-engagement`, `expansion` |
| `context` | ❌ | Relevant context: recent meeting, trigger event, product interest, mutual connection |
| `product_focus` | ❌ | Cloudflare products to reference — keeps the email focused |
| `cadence` | ❌ | If `true`, generates a full 5-step cadence sequence instead of a single email |
| `tone` | ❌ | `executive` (formal, strategic), `technical` (peer-to-peer, detailed), `casual` (conversational, human) — defaults to matching recipient seniority |
| `language` | ❌ | `en` (default), `es`, `pt` — for LATAM outreach |

## Key Outputs

- **Email Draft** (or 5-step cadence) with:
  1. **Subject Line** — under 8 words, no clickbait, specific to the recipient's context
  2. **Email Body** — personalized, value-led, with a single clear CTA:
     - Opening — relevant hook tied to recipient's world (not "I hope this finds you well")
     - Value proposition — one specific benefit, not a product dump
     - Social proof — relevant customer reference or data point (if applicable)
     - Call-to-action — one ask, specific and easy to say yes to
  3. **Cadence Sequence** (if cadence mode):
     - Email 1 — value-led introduction with insight
     - Email 2 — different angle (case study, data point, or industry trend)
     - Email 3 — social proof or mutual connection
     - Email 4 — provocative question or competitive insight
     - Email 5 — breakup email (polite close, leave the door open)
  4. **Sending Notes** — recommended send time, spacing between cadence steps, A/B test suggestions
- Saved to: `~/helix-deck/emails/[company-slug]-[type]-[date].md`

## Quality Bar Highlights

1. **Subject lines under 8 words** — every word in a subject line must earn its place; "Quick question about your network security strategy" is 7 words too many
2. **No "I hope this finds you well"** — ban all filler openings; start with something relevant to the recipient's world
3. **One CTA per email** — never ask for a meeting AND ask them to read a document AND ask them to forward to a colleague; pick one
4. **Personalization must be real** — using their company name is not personalization; referencing their recent earnings call, a specific initiative, or a mutual connection is
5. **Cadence steps must vary the angle** — sending the same value prop 5 times is spam; each step should offer a different reason to engage
6. **Never send automatically** — always produce drafts; the operator reviews and sends from their own email
