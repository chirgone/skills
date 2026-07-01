# Discovery Guide

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Pre-Call

---

## Summary

Generate a consultative discovery conversation guide — not a checklist of questions, but a structured conversation framework. Orchestrates account intelligence gathering, persona research, business outcome mapping, and Challenger reframes into a single pre-call document. Questions are MEDDPICC-mapped so every answer fills a qualification gap. Includes Challenger-style insights and reframes designed to teach the customer something new about their problem. The output is a conversation guide the rep can internalize, not a script to read from.

## When To Use

- "Help me prepare discovery questions for [account]"
- "I have a first call with [persona] at [company] — what should I ask?"
- "Build a discovery guide for a [industry] [title]"
- Before a first meeting with a new prospect
- When entering a new buying center within an existing account
- When the current discovery approach isn't uncovering compelling events
- When an SE needs to run a technical discovery separate from business discovery
- "I keep getting stuck at surface-level answers — help me go deeper"
- When preparing for a multi-persona discovery across IT, Security, and Network teams

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | ✅ | Prospect or customer account name |
| `persona` | ✅ | Title or role of the primary contact: `CISO`, `CTO`, `VP-Infrastructure`, `Network-Architect`, `IT-Director`, etc. |
| `industry` | ❌ | Customer's industry — used for industry-specific pain points and benchmarks |
| `products_in_scope` | ❌ | Cloudflare products being considered — focuses questions on relevant use cases |
| `known_pain_points` | ❌ | Any pain points already identified — used to deepen rather than repeat discovery |
| `competitive_context` | ❌ | Known incumbent or competitive solutions being evaluated |
| `meddpicc_gaps` | ❌ | Specific MEDDPICC elements that need filling — focuses the guide on gaps |

## Key Outputs

- **Discovery Conversation Guide** (Markdown) with sections:
  1. **Account Intelligence Brief** — what we know before the call: company overview, recent news, technology stack signals, hiring patterns
  2. **Persona Profile** — typical priorities, KPIs, reporting structure, and communication preferences for this role
  3. **Opening Frame** — a Challenger-style insight or perspective that earns the right to ask questions (teach before you ask)
  4. **Discovery Questions by MEDDPICC Element:**
     - Metrics — "How do you measure success for [initiative]?"
     - Economic Buyer — "Who signs off on investments of this size?"
     - Decision Criteria — "What are your must-haves vs. nice-to-haves?"
     - Decision Process — "Walk me through how a decision like this gets made"
     - Identify Pain — "What breaks when [scenario] happens?"
     - Paper Process — "What does procurement look like on your side?"
     - Champion — "Who else on your team cares about solving this?"
     - Competition — "What else are you evaluating or using today?"
  5. **Depth Ladders** — for each question, a follow-up sequence that goes from surface to root cause (Level 1 → Level 2 → Level 3)
  6. **Challenger Reframes** — 2–3 insights that reframe the customer's problem in a way they haven't considered, with supporting data
  7. **Business Outcome Map** — connects technical capabilities to business outcomes the persona cares about
  8. **Red Flags to Listen For** — signals during the conversation that indicate risk: no compelling event, no budget, tire-kicking, coach-not-champion
- Saved to: `~/helix-deck/discovery/[account-slug]-discovery-guide-[date].md`

## Quality Bar Highlights

1. **This is a conversation guide, not a questionnaire** — if it reads like a survey, it's wrong; questions should flow naturally and build on each other
2. **Challenger insight must come first** — earn the right to ask questions by teaching something valuable; don't start with "tell me about your challenges"
3. **Every question maps to MEDDPICC** — if a question doesn't fill a qualification gap, cut it; discovery time is limited
4. **Depth ladders prevent surface-level answers** — "What keeps you up at night?" gets a generic answer; the follow-up "What happened last time that occurred?" gets a real one
5. **Persona-specific language** — a CISO cares about risk and compliance; a CTO cares about velocity and architecture; a CFO cares about cost and ROI; same product, different framing
6. **Red flags are as valuable as green flags** — knowing when to disqualify is as important as knowing when to advance; flag the warning signs explicitly
