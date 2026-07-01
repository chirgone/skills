# Campaign Command Center

**Catalog:** Cloudflare SuperSeal  
**Category:** Marketing / Campaign Strategy

---

## Summary

Segment territory accounts into campaign tracks and orchestrate multi-touch, multi-channel marketing plays. Given a list of accounts with firmographic and engagement data, assigns each account to the optimal campaign track (awareness, nurture, acceleration, retention, win-back), generates personalized messaging frameworks per segment, and produces an execution calendar with channel mix, content mapping, and success metrics. Designed for field marketers and campaign managers planning territory-level programs.

## When To Use

- "Segment my territory for Q3 campaigns"
- "Which accounts should go into which campaign track?"
- "Build a campaign plan for my LATAM territory"
- Quarterly campaign planning for a defined territory
- Account-based marketing (ABM) program design
- Event follow-up campaign orchestration
- Re-engagement campaign for dormant accounts
- New product launch campaign segmentation

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_list` | ✅ | List of accounts with available data (name, industry, stage, engagement score, etc.) |
| `territory` | ❌ | Territory name/region for context (e.g., `Mexico`, `Brazil`, `LATAM-South`) |
| `campaign_goal` | ❌ | Primary goal: `pipeline-generation`, `pipeline-acceleration`, `retention`, `awareness`, `product-launch` |
| `available_channels` | ❌ | Channels available: `email`, `paid-social`, `events`, `webinars`, `direct-mail`, `BDR-outreach`, `content-syndication` |
| `budget` | ❌ | Total campaign budget (for channel allocation) |
| `timeline` | ❌ | Campaign duration (default: 90 days) |
| `content_assets` | ❌ | Available content assets (whitepapers, case studies, webinars, videos) |
| `engagement_data` | ❌ | Historical engagement scores or activity data per account |

## Key Outputs

- **Campaign Command Center Plan** (Markdown + optional spreadsheet) with sections:
  1. **Territory Segmentation** — accounts assigned to tracks:
     - 🟢 **Acceleration** — active pipeline, high intent, accelerate to close
     - 🟡 **Nurture** — engaged but not in pipeline, build relationship
     - 🔵 **Awareness** — low engagement, need air cover and brand awareness
     - 🟠 **Retention** — existing customers, drive adoption and expansion
     - 🔴 **Win-Back** — churned or lost deals, re-engagement play
  2. **Segment Profiles** — persona descriptions, messaging themes, and value propositions per track
  3. **Channel Mix** — recommended channels per track with budget allocation
  4. **Content Mapping** — which content assets map to which track and stage
  5. **Execution Calendar** — week-by-week activity plan with owners, channels, and content
  6. **Personalization Framework** — email/ad copy templates per segment with merge fields
  7. **Success Metrics** — KPIs per track with targets and measurement methodology
  8. **BDR Coordination** — outreach sequences aligned with campaign touches
- Saved to: `~/helix-deck/campaigns/command-center-[territory-slug]-[date].md`

## Quality Bar Highlights

1. **Every account must land in exactly one track** — no orphans, no duplicates across tracks
2. **Segmentation logic must be transparent** — document why each account is in its track; "because the model said so" is not acceptable
3. **Channel mix must respect budget** — if budget is $50K, don't propose a $200K plan; scale recommendations to reality
4. **Content gaps must be flagged** — if a track needs a case study that doesn't exist, call it out as a gap with a recommendation to create it
5. **BDR sequences must align** — if marketing sends an email on Tuesday, the BDR follow-up call should be Wednesday, not the same hour
