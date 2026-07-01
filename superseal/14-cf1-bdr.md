# CF1 BDR

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / BDR Enablement

---

## Summary

Coach a BDR through CF1/SASE outbound prospecting. Generates persona-specific outreach sequences, objection handling scripts, discovery question frameworks, and qualification criteria for Cloudflare One (SASE/Zero Trust) opportunities. Covers the full BDR workflow from account research to qualified meeting handoff, with industry-specific messaging and multi-touch cadence design.

## When To Use

- "Help me prospect into [account] for CF1"
- "Write me a cold outreach sequence for SASE"
- "How do I position Zero Trust to a CISO?"
- BDR building outbound sequences for CF1/SASE campaigns
- New BDR onboarding to Cloudflare One messaging
- Territory blitz planning for SASE pipeline generation
- Event follow-up for Zero Trust/SASE leads
- "Coach me on how to qualify a SASE opportunity"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `target_account` | ❌ | Account name for account-specific messaging |
| `persona` | ❌ | Target persona: `CISO`, `VP-Security`, `VP-Networking`, `IT-Director`, `Network-Architect`, `Security-Engineer` |
| `industry` | ❌ | Target industry for vertical-specific messaging |
| `trigger_event` | ❌ | Reason for outreach: `new-hire`, `funding`, `breach-in-news`, `compliance-deadline`, `vpn-pain`, `vendor-renewal`, `event-attendee` |
| `sequence_type` | ❌ | `cold-outbound`, `warm-follow-up`, `event-follow-up`, `inbound-response`, `referral` |
| `touch_count` | ❌ | Number of touches in the sequence (default: 8) |
| `channels` | ❌ | Available channels: `email`, `linkedin`, `phone`, `video` (default: all) |

## Key Outputs

- **BDR Coaching Package** (Markdown) with sections:
  1. **Account Research Brief** — company overview, tech stack signals, trigger events, key contacts
  2. **Persona Messaging Matrix** — value propositions by persona with pain points and Cloudflare differentiators
  3. **Outreach Sequence** — multi-touch cadence (8-12 touches over 3-4 weeks):
     - Day-by-day activity plan with channel, subject line, body copy, and call script
     - Each touch builds on the previous (not repetitive "just checking in")
     - Personalization tokens and where to insert account-specific intel
  4. **Discovery Questions** — 10 questions to qualify a SASE/CF1 opportunity:
     - Current VPN/ZTNA infrastructure
     - Remote workforce size and distribution
     - Security stack consolidation appetite
     - Compliance requirements (SOC2, PCI, HIPAA)
     - Network architecture and SD-WAN status
  5. **Objection Handling** — top 10 objections with scripted responses:
     - "We already have Zscaler/Palo Alto"
     - "Our VPN works fine"
     - "We're not ready for Zero Trust"
     - "Too expensive"
     - "We just renewed our contract"
  6. **Qualification Criteria** — BANT/MEDDPICC checklist for CF1 opportunities
  7. **Meeting Handoff Template** — what to include when passing a qualified meeting to the AE
- Saved to: `~/helix-deck/bdr/cf1-bdr-[account-slug]-[date].md`

## Quality Bar Highlights

1. **No generic copy** — every email must reference something specific about the account or persona; "Dear Sir/Madam" is a fireable offense
2. **Sequence must escalate** — each touch should add new value (insight, stat, case study, event invite); never "just bumping this up"
3. **Phone scripts must be conversational** — no reading from a card; provide a framework with 3 opener variants and 3 pivot questions
4. **Objection responses must be honest** — if the customer just renewed with a competitor for 3 years, acknowledge that and adjust the play (plant seeds for year 2 review)
5. **Qualification must be rigorous** — better to disqualify early than waste an AE's time on an unqualified meeting; include clear "no-go" criteria
