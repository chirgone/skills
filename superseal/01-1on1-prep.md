# 1:1 Prep

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Management Enablement

---

## Summary

Pre-call competitive prep skill for managers preparing for a 1:1 with a direct report or skip-level. Generates a concise brief covering the rep's pipeline health, deal progression, blockers, coaching opportunities, and suggested talking points. Supports two modes: **first-line mode** (manager ↔ AE/SE) and **skip-level mode** (director+ ↔ IC), adjusting depth and tone accordingly.

## When To Use

- Before a scheduled 1:1 with a direct report or skip-level
- "Prep me for my 1:1 with [rep name]"
- "What should I ask [rep] about their deals?"
- "Skip-level prep for [IC name]"
- Weekly/biweekly 1:1 cadence preparation
- When a manager needs to coach on stalled pipeline or deal execution

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `rep_name` | ✅ | Name of the direct report or skip-level IC |
| `mode` | ❌ | `first-line` (default) or `skip-level` |
| `focus_area` | ❌ | Optional focus: `pipeline`, `deals`, `skills`, `career`, `all` |
| `time_range` | ❌ | Lookback period for activity data (default: 2 weeks) |
| `crm_data` | ❌ | Pipeline/opportunity data from Salesforce or CRM |
| `previous_1on1_notes` | ❌ | Notes from the last 1:1 for continuity |

## Key Outputs

- **1:1 Brief** — Single-page Markdown document containing:
  - Rep snapshot: quota attainment, pipeline coverage, activity metrics
  - Deal highlights: top 3 deals by size, deals at risk, stalled opportunities
  - Coaching signals: patterns in win/loss, skill gaps, development areas
  - Suggested questions: 5-7 open-ended coaching questions tailored to mode
  - Follow-up tracker: open items from previous 1:1
- **Mode-specific adjustments:**
  - First-line: granular deal-level coaching, forecast accuracy, activity metrics
  - Skip-level: career development, team dynamics, cross-functional friction, engagement signals
- Saved to: `~/helix-deck/1on1/[rep-slug]-[date].md`

## Quality Bar Highlights

1. **Never fabricate CRM data** — if pipeline data is unavailable, state it explicitly and shift to qualitative coaching questions
2. **Coaching tone, not interrogation** — questions should be curious and developmental, not accusatory
3. **Continuity matters** — always reference previous 1:1 notes when available; flag overdue follow-ups
4. **Respect confidentiality** — skip-level briefs must not include data the IC wouldn't expect their skip to have
5. **Actionable over exhaustive** — limit to top 3 deals, top 3 coaching points; managers have 30 minutes, not 3 hours
