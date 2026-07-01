# Challenger

**Catalog:** Cloudflare SuperSeal  
**Category:** Generic / Quality Assurance

---

## Summary

Independent review step for anything you're about to send — an email, a proposal, a deck, a business case, a blog post, or any customer-facing deliverable. Acts as a critical friend who challenges assumptions, catches errors, identifies weak arguments, and stress-tests the content from the recipient's perspective. Based on the Challenger Sale methodology: teach, tailor, take control — applied to content review rather than selling.

## When To Use

- "Review this before I send it"
- "Challenge this proposal"
- "What would a skeptical CTO think of this?"
- Before sending any high-stakes customer communication
- Before submitting a proposal, RFP response, or business case
- Before presenting a deck to leadership or customers
- Before publishing a blog post or external-facing content
- "Poke holes in this argument"
- "What am I missing?"
- As a final quality gate before any deliverable exits the team

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `content` | ✅ | The content to review (email draft, proposal, deck, document, blog post, etc.) |
| `audience` | ❌ | Who will receive this: `customer-CISO`, `customer-CTO`, `internal-leadership`, `prospect`, `partner`, `public` |
| `context` | ❌ | Background context: deal stage, relationship history, known sensitivities |
| `goal` | ❌ | What the content is trying to achieve (close a deal, get a meeting, secure budget, inform, persuade) |
| `tone` | ❌ | Desired tone: `executive`, `technical`, `casual`, `urgent`, `diplomatic` |
| `review_depth` | ❌ | `quick` (grammar + logic check), `standard` (default — full review), `deep` (adversarial red-team) |

## Key Outputs

- **Challenger Review** (Markdown) with sections:
  1. **Verdict** — one of:
     - ✅ **Send it** — content is ready; minor suggestions only
     - ⚠️ **Fix and send** — good content with specific issues to address first
     - 🛑 **Rework** — fundamental problems that require significant revision
  2. **Strength Assessment** — what's working well (top 3 things to keep)
  3. **Critical Issues** — problems that must be fixed before sending:
     - Factual errors or unsupported claims
     - Logical gaps or weak arguments
     - Tone mismatches for the audience
     - Missing information the recipient will ask about
     - Commitments or promises that shouldn't be made
  4. **Recipient Perspective** — "If I were the [audience], I would think/ask/feel..."
  5. **Competitive Vulnerability** — could a competitor use this content against us?
  6. **Suggestions** — specific rewrites for problem areas (not just "make it better")
  7. **Final Check** — grammar, formatting, link verification, attachment reminder
- Saved to: reviews are inline, not saved to file (ephemeral by design)

## Quality Bar Highlights

1. **Be genuinely critical** — the whole point of this skill is to catch problems; being polite about bad content helps no one
2. **Recipient's perspective is paramount** — review from the audience's viewpoint, not the author's; a technically brilliant email that talks past the CFO is still a bad email
3. **Flag commitments** — any sentence that could be read as a commitment, SLA, or guarantee must be flagged for review
4. **Check for Cloudflare confidential data** — internal pricing, roadmap details, competitive intelligence, and customer data must never appear in external-facing content
5. **Suggest, don't just criticize** — every critical issue must include a suggested fix; "this is weak" is not helpful; "replace this with [specific alternative]" is
6. **Speed matters** — this is a pre-send check, not a doctoral thesis review; complete the review in under 2 minutes of reading time
