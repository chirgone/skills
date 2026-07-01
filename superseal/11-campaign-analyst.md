# Campaign Analyst

**Catalog:** Cloudflare SuperSeal  
**Category:** Marketing / Analytics

---

## Summary

Analyze marketing campaign performance data to surface what's working, what's not, and what to do next. Ingests campaign metrics (impressions, clicks, conversions, pipeline generated, cost) across channels and produces a structured analysis with channel attribution, funnel analysis, ROI calculations, and actionable optimization recommendations. Designed for field marketers, demand gen managers, and campaign owners reviewing campaign health.

## When To Use

- "How did the [campaign name] perform?"
- "Analyze last quarter's marketing campaigns for LATAM"
- "Which campaigns are generating the most pipeline?"
- Post-campaign performance review
- Mid-campaign optimization check
- Quarterly marketing review preparation
- Budget reallocation decisions between channels
- "Show me campaign ROI by channel"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `campaign_data` | ✅ | Campaign performance data (CSV, spreadsheet link, or structured JSON) |
| `time_period` | ❌ | Analysis period: `last-30d`, `last-quarter`, `last-6mo`, `ytd`, or custom date range |
| `channels` | ❌ | Filter to specific channels: `email`, `paid-social`, `paid-search`, `events`, `webinars`, `content-syndication`, `all` |
| `region` | ❌ | Filter by region: `LATAM`, `NAM`, `EMEA`, `APAC`, `Global` |
| `segment` | ❌ | Filter by segment: `enterprise`, `mid-market`, `commercial`, `startup` |
| `benchmark_data` | ❌ | Industry or historical benchmarks for comparison |
| `goals` | ❌ | Campaign goals/KPIs for performance-vs-target analysis |

## Key Outputs

- **Campaign Analysis Report** (Markdown) with sections:
  1. **Performance Summary** — top-line metrics: total spend, pipeline generated, ROI, cost per lead, cost per opportunity
  2. **Channel Attribution** — performance breakdown by channel with relative efficiency ranking
  3. **Funnel Analysis** — conversion rates at each stage (impression → click → lead → MQL → SAL → opportunity → closed-won)
  4. **Top Performers** — top 5 campaigns by pipeline generated and by ROI
  5. **Underperformers** — bottom 5 campaigns with root cause hypothesis
  6. **Trend Analysis** — performance trends over time (improving, declining, stable)
  7. **A/B Test Results** — if applicable, variant performance with statistical significance
  8. **Optimization Recommendations** — 5-7 specific, actionable recommendations ranked by expected impact
  9. **Budget Reallocation Proposal** — where to shift spend based on performance data
  10. **Executive Summary** — 3-5 bullet points for leadership reporting
- Saved to: `~/helix-deck/campaigns/campaign-analysis-[date].md`

## Quality Bar Highlights

1. **Data integrity first** — validate input data for completeness before analysis; flag missing fields, date gaps, or suspicious values (e.g., 0 impressions with 50 clicks)
2. **Attribution honesty** — if multi-touch attribution data isn't available, say so; don't over-credit last-touch
3. **Statistical significance matters** — don't declare a winner in A/B tests without sufficient sample size; state confidence intervals
4. **Recommendations must be specific** — "Invest more in paid social" is not actionable; "Shift $15K from content syndication to LinkedIn Sponsored Content targeting security personas, which showed 3x higher MQL conversion" is
5. **Benchmark context is mandatory** — raw numbers without benchmarks are meaningless; always compare to industry averages, historical performance, or stated goals
