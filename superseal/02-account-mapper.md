# Account Mapper

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Data Enrichment

---

## Summary

Paste 10–200 company names and get back a confidence-tagged, enriched Markdown table with firmographic data, Cloudflare relationship status, industry vertical, estimated employee count, HQ location, and domain. Designed for territory planning, event follow-up list scrubbing, and rapid account qualification. Each row includes a confidence score indicating data reliability.

## When To Use

- "Here's a list of companies from [event/report], enrich them"
- "Map these accounts to Cloudflare verticals"
- Territory planning: bulk-qualify a list of target accounts
- Event lead list processing and prioritization
- Partner-sourced account list validation
- "Which of these companies are already Cloudflare customers?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `company_list` | ✅ | Plain text list of 10–200 company names (one per line or comma-separated) |
| `enrich_fields` | ❌ | Fields to include: `domain`, `industry`, `employees`, `hq`, `revenue`, `cf_status` (default: all) |
| `region_filter` | ❌ | Filter results to a specific region (e.g., `LATAM`, `EMEA`, `NAM`) |
| `output_format` | ❌ | `markdown` (default), `csv`, `json` |
| `cf_customer_check` | ❌ | Boolean — cross-reference against known Cloudflare accounts (default: true) |

## Key Outputs

- **Enriched Markdown Table** with columns:
  - Company Name | Domain | Industry | Vertical | Employees (est.) | HQ | Region | CF Status | Confidence
- **Confidence tags per row:**
  - 🟢 HIGH (≥ 85%) — strong match, verified domain
  - 🟡 MEDIUM (50–84%) — partial match, some fields inferred
  - 🔴 LOW (< 50%) — ambiguous name, multiple possible matches, or no data found
- **Summary stats:** total mapped, high/medium/low breakdown, unmapped count
- **CF Status values:** `Customer`, `Prospect`, `Churned`, `Free-tier`, `Unknown`
- Saved to: `~/helix-deck/maps/account-map-[date].md`

## Quality Bar Highlights

1. **Never guess domains** — if a company name is ambiguous (e.g., "Mercury"), flag it as LOW confidence rather than picking the wrong entity
2. **Deduplicate intelligently** — "Grupo Televisa" and "Televisa" should resolve to one row, not two
3. **Region inference must be explicit** — don't assume US if HQ is unknown; mark as "Unknown"
4. **CF Status requires verification** — don't mark as "Customer" without Lighthouse or CRM confirmation; default to "Unknown"
5. **Cap at 200** — if input exceeds 200 names, warn the user and process the first 200 with a note
