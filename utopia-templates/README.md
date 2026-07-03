# Utopia Gold Templates

These are the gold-standard Confluence Storage Format (XHTML) bodies
for replicating Utopia vertical pages.

## Files

| File | Vertical | Page ID | Version |
|------|----------|---------|---------|
| `gold-retail.html` | Retail | 1214482141 | v21 |
| `gold-hospitality.html` | Hospitality | 1431715803 | v1 |
| `gold-healthcare.html` | Healthcare & Pharma | 1182735362 | v9 |
| `gold-finserv.html` | Financial Services | 1187496098 | v13 |
| `validate_section_order.py` | Validator | -- | -- |

## Canonical Section Order (MANDATORY)

Every Utopia vertical page MUST follow this exact section sequence.
This is the single source of truth, derived from gold-retail.html.
The validator (`validate_section_order.py`) enforces this order.

| # | Section ID | H1 / EXPAND Title | Required |
|---|-----------|-------------------|----------|
| 1 | INTRO | Banner image + opening paragraph + sub-verticals list | Yes |
| 2 | USE_CASES | H1: Customer Use Cases and Journeys / EXPAND: Explore sector-specific use cases | Yes |
| 3 | TOP_10 | H1: Top 10 [Vertical] Sector Use Cases (inside table) | Yes |
| 4 | PRODUCT_CHECKLIST | H1: [Vertical] Product Checklist / EXPAND: Product Deployment Status | No |
| 5 | MEDDPICC | H1: [Vertical] Sector MEDDPICC / EXPAND: MEDDPICC for [Vertical] | Yes |
| 6 | UTOPIA_VISION | H1: Cloudflare's Utopia for [Vertical] / EXPAND: Cloudflare's vision | Yes |
| 7 | FRAMEWORK | H2: Cloudflare [Vertical] Framework + EXPAND: Get Started + Architectural Framework | Yes |
| 8 | PHASED_DEPLOYMENT | H1: ...implementation by phases / EXPAND: Phased Deployment (6 phases) | Yes |
| 9 | COMMERCIAL_FOCUS | H1: Commercial Focus & Value Proposition / EXPAND: Products to Lead With... | Yes |
| 10 | SCOPING_QUESTIONS | H1: Phased Commercial Qualification / EXPAND: Sequential Opportunity Assessment | Yes |
| 11 | BUNDLES | H1: Cloudflare Service Models / EXPAND: Cloudflare Bundles | Yes |
| 12 | CONCLUSION | H1: Conclusion / EXPAND: Conclusions | Yes |
| 13 | RESOURCES | H1: Featured Videos / EXPAND: Cloudflare Resources | Yes |
| 14 | BACK_LINK | H1: Back to Utopia Framework (linked to Framework page) | Yes |

## How to Create a New Vertical

### Step 1: Prepare

```bash
# Copy Retail gold as skeleton
cp gold-retail.html gold-VERTICAL.html
```

### Step 2: Replace Content (NOT Structure)

Replace ONLY text content. Do NOT change:
- Section order
- XHTML tag structure
- Expand macro nesting
- Table column counts

Key replacements:
- Vertical name (Retail -> Healthcare, etc.)
- Sub-verticals list
- Compliance frameworks (PCI DSS -> HIPAA, GDPR, etc.)
- Use case examples and metrics
- MEDDPICC methodology content
- All 6 phases in Phased Deployment
- Discovery/scoping questions
- Bundle examples
- Resource links

### Step 3: Validate BEFORE Publishing

```bash
python3 validate_section_order.py gold-VERTICAL.html
```

The validator checks:
1. All 14 sections present (or 13 if Product Checklist is optional)
2. Sections in correct canonical order
3. No cross-vertical contamination (retail terms in healthcare, etc.)
4. No raw ampersands (must be `&amp;` in XHTML)
5. Phase 6 (AI Security) exists

**DO NOT PUBLISH if the validator fails.**

### Step 4: Publish

```bash
# Via REST API for pages > 95KB
TOKEN=$(cat ~/.cloudflared/lighthouse.insights.cfdata.org-*-token 2>/dev/null | head -1)

curl -s -X PUT "https://wiki.cfdata.org/rest/api/content/PAGE_ID" \
  -H "Content-Type: application/json" \
  -H "cf-access-token: $TOKEN" \
  -d @payload.json
```

### Step 5: Update This README

Add the new gold template to the Files table above.

## Anti-Patterns (DO NOT)

1. **DO NOT generate sections out of order** - The generator script MUST assemble
   sections in canonical order (1-14). If writing a Python generator, use the
   numbered section IDs as variable names.

2. **DO NOT rewrite from scratch** - Always start from `gold-retail.html` as
   skeleton. Full rewrites produce XHTML balance errors (mismatched tags, stray
   macros). Surgical replacement of text content is cleaner and faster.

3. **DO NOT skip the validator** - Every generated page MUST pass
   `validate_section_order.py` before publish. No exceptions.

4. **DO NOT copy bundles verbatim** - Bundle examples (Accelerate Global Shoppers,
   Black Friday, etc.) are vertical-specific. Replace them entirely.

5. **DO NOT omit Commercial Focus** - Section 9 (Commercial Focus & Value
   Proposition) is required. Healthcare v8 was missing this section.

6. **DO NOT omit Phase 6** - All verticals must include Phase 6: AI Security &
   Governance in Phased Deployment.

## Contamination Terms (Forbidden Cross-Vertical Language)

The validator checks for these. If any appear in a page that is NOT their
source vertical, the validator fails.

- **Retail**: retailer, shopping cart, shopper, Black Friday, e-commerce,
  inventory scanner, POS system, live shopping, product demos, boosting
  conversion, merchandise, scalper, Global Shoppers
- **Hospitality**: check-in, concierge, hotel guest, room service (exception:
  "Waiting Room services" is a Cloudflare product), booking engine, front desk,
  housekeeping
- **Casino**: gambling, betting, casino, wager, poker, sportsbook, Apuesta Total
- **Government**: citizen portal, government entities, public sector, municipal,
  civic, e-government

## Verticals Status

| Vertical | Page ID | Status | Notes |
|----------|---------|--------|-------|
| Retail | 1214482141 | GOLD v21 | Reference template |
| Hospitality | 1431715803 | GOLD v1 | Has retail contamination in bundles (known) |
| Healthcare & Pharma | 1182735362 | GOLD v9 | Reordered from v8 |
| Financial Services | 1187496098 | GOLD v13 | Patched from v12 |
| Government | 1092896800 | 70% | Missing Phase 6, retail bundles |
| Telco & SP | -- | Not started | 5 sub-verticals planned |
| Media & Entertainment | 1182734455 | Needs audit | Casino language found |
| Universities | 1182730943 | Needs audit | -- |
| Utilities | 1239967266 | Needs audit | -- |
| Airlines | 1182745297 | Needs audit | -- |
| Automotive | 1295366832 | Needs audit | -- |
