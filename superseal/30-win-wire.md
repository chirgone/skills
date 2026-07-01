# Win Wire

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Post-Close

---

## Summary

Capture a deal win same day or within 3 days of close. Speed matters — details fade fast. Produces 3 distinct artifacts: Win Notes (~250 words, SFDC-ready for pasting into the opportunity), Win Wire (400–800 words, wiki-ready for internal sharing and enablement), and structured win-data JSON for analytics and pattern matching. Supports two paths: Fast Path (4 targeted questions, 8–10 minutes) for deals under $50K or time-pressed reps, and Deep Path (forensic sweep of Gmail, Calendar, and GChat) for strategic deals where the full story matters for enablement and competitive intelligence.

## When To Use

- "We just closed [deal] — capture the win"
- "Write a win wire for [account]"
- "I need to log my win notes for [deal]"
- Immediately after a deal is marked Closed-Won in SFDC
- Within 3 days of close while details are fresh
- When sales leadership requests a win wire for all-hands or enablement
- When the competitive intelligence team needs win/loss data
- When marketing needs a customer story lead based on a recent win
- When onboarding a new rep and need to share recent win patterns

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `deal_name` | ✅ | Opportunity name or SFDC Opportunity ID |
| `account_name` | ❌ | Account name — auto-resolved from SFDC if omitted |
| `path` | ❌ | `fast` (4 questions, 8–10 min) or `deep` (Gmail/Calendar/GChat forensic sweep) — defaults to `fast` for deals < $50K ACV |
| `rep_notes` | ❌ | Free-text notes from the rep about why they won — used to enrich both paths |
| `products` | ❌ | Products sold — auto-pulled from SFDC if omitted |
| `acv` | ❌ | Deal ACV — auto-pulled from SFDC if omitted |
| `competitive_displacement` | ❌ | Competitor displaced, if applicable — key for competitive intelligence |

## Key Outputs

- **Win Notes** (~250 words, SFDC-ready):
  - Deal summary: account, products, ACV, close date
  - Why they bought: top 3 reasons
  - Why Cloudflare won (vs. competition or status quo)
  - Key stakeholders involved in the decision
  - Implementation timeline and next steps
- **Win Wire** (400–800 words, wiki-ready):
  1. **Headline** — compelling one-liner: "[Company] selects Cloudflare for [use case]"
  2. **The Challenge** — what problem the customer was solving
  3. **The Journey** — how the deal progressed from first contact to close
  4. **Why Cloudflare** — competitive differentiation, technical proof points, business value
  5. **The Decision** — who made it, what tipped the scale, decision criteria
  6. **What's Next** — deployment plan, expansion potential, reference-ability
  7. **Lessons Learned** — what worked well and what the team would do differently
- **Win Data JSON** (structured):
  - `deal_id`, `account`, `acv`, `products`, `industry`, `close_date`, `cycle_length_days`
  - `competitor_displaced`, `decision_criteria`, `champion_title`, `economic_buyer_title`
  - `win_reasons[]`, `key_proof_points[]`, `use_case_tags[]`
- Saved to: `~/helix-deck/wins/[account-slug]-win-wire-[date].md` + `.json`

## Quality Bar Highlights

1. **Speed over perfection** — a good win wire captured today beats a perfect one captured never; the Fast Path exists for a reason
2. **Win reasons must be specific** — "better product" is not a win reason; "500ms latency reduction validated in POC vs. Akamai" is
3. **Competitive intelligence is the highest-value data** — if a competitor was displaced, capture exactly why; this feeds the entire competitive program
4. **SFDC notes must be paste-ready** — no formatting that breaks in SFDC's text field; plain text, clean paragraphs, no markdown
5. **Deep Path forensic sweep should surface commitments** — any promises made in emails or meetings during the sales cycle need to be flagged for the implementation team
6. **3-day window is a hard deadline** — after 3 days, rep memory degrades significantly; if the win wire isn't captured by then, switch to Deep Path regardless of deal size
