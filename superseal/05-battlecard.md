# Battlecard

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Competitive Intelligence

---

## Summary

Pre-call competitive prep for AEs, SEs, and BDRs. Given a target account and known or suspected incumbent vendor(s), generates a structured battlecard covering competitive positioning, landmine questions to ask, objection handling, proof points, and recommended Cloudflare plays. Pulls from Cloudflare competitive intelligence, product catalog, published case studies, and analyst data to produce a document usable in live calls.

## When To Use

- "Prep me against [Zscaler/Akamai/Fastly/Palo Alto/etc.] for my call with [account]"
- "I'm going up against [competitor] — what should I say?"
- Pre-call competitive prep for any deal with a known incumbent
- BDR outbound prep when targeting accounts with known vendor relationships
- SE technical deep-dive prep when displacement is the play
- RFP/RFI response where competitive differentiation is required

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `competitor` | ✅ | One or more competitor names (e.g., `Zscaler`, `Akamai`, `Palo Alto Networks`) |
| `account_name` | ❌ | Target account for context-specific positioning |
| `product_area` | ❌ | Focus area: `SASE`, `Zero Trust`, `CDN`, `WAF`, `DDoS`, `DNS`, `Bot Management`, `Workers`, `all` |
| `deal_stage` | ❌ | Current deal stage: `prospecting`, `discovery`, `evaluation`, `negotiation`, `closed-lost-review` |
| `audience` | ❌ | Who's on the call: `CISO`, `CTO`, `NetOps`, `SecOps`, `Developer`, `Procurement` |
| `include_pricing` | ❌ | Boolean — include pricing comparison guidance (default: false, requires internal data) |

## Key Outputs

- **Battlecard Document** (Markdown) with sections:
  1. **Competitor Overview** — positioning, market share, recent moves, analyst sentiment
  2. **Head-to-Head Comparison** — feature matrix across the selected product area(s)
  3. **Cloudflare Advantages** — top 5 differentiators with proof points
  4. **Known Weaknesses** — honest assessment of where Cloudflare is weaker (with mitigation strategies)
  5. **Landmine Questions** — 5-7 questions to ask the prospect that expose competitor gaps
  6. **Objection Handling** — top 5 objections you'll hear and scripted responses
  7. **Proof Points** — relevant case studies, benchmarks, and analyst quotes
  8. **Recommended Play** — specific Cloudflare positioning strategy for this deal
  9. **Talk Track** — 60-second elevator pitch tailored to the audience persona
- Saved to: `~/helix-deck/battlecards/[competitor-slug]-[date].md`

## Quality Bar Highlights

1. **Never trash-talk** — position Cloudflare's strengths, don't insult competitors; AEs lose credibility with FUD
2. **Honest weaknesses** — every battlecard must include at least 2 areas where the competitor is genuinely strong, with Cloudflare's mitigation strategy
3. **Proof points must be real** — cite actual case studies, published benchmarks, or analyst reports; never fabricate customer quotes
4. **Audience-aware language** — a CISO cares about risk reduction; a developer cares about DX; adjust terminology accordingly
5. **Date-stamp competitive intel** — competitors ship features fast; always note when competitive data was last verified
