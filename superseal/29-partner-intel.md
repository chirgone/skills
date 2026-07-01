# Partner Intel

**Catalog:** Cloudflare SuperSeal  
**Category:** Channel / Partner

---

## Summary

Partnership evaluation brief for assessing potential or existing channel partners. Covers service portfolio analysis, technology alliance ecosystem, geographic reach, and Cloudflare fit across 4 dimensions: product alignment, vertical expertise, geographic coverage, and go-to-market motion compatibility. Produces a structured evaluation that helps channel managers decide whether to invest in a partnership, how to position Cloudflare within the partner's portfolio, and where the joint value proposition is strongest. Supports both new partner evaluation and existing partner relationship optimization.

## When To Use

- "Evaluate [partner] as a potential Cloudflare partner"
- "Build an intel brief on [partner]"
- "How does [partner] fit with Cloudflare?"
- "What should I know before meeting [partner]?"
- When evaluating a new partner for the Cloudflare channel program
- When preparing for a partner business planning session
- When a partner asks to become a Cloudflare reseller or referral partner
- When assessing whether to invest MDF or co-selling resources in a partner
- When a partner's service portfolio changes and you need to reassess alignment
- Before a partner QBR to understand the state of the partnership

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `partner_name` | ✅ | Partner company name |
| `partner_type` | ❌ | `reseller`, `referral`, `MSP`, `GSI`, `technology-alliance`, `distributor` — auto-detected if omitted |
| `region` | ❌ | Primary region of interest: `LATAM`, `EMEA`, `NAM`, `APAC` — or specific countries |
| `existing_relationship` | ❌ | If `true`, enriches with existing partner portal data and deal history |
| `evaluation_purpose` | ❌ | `new-partner`, `business-planning`, `mdf-investment`, `program-tier-review` |
| `verticals_of_interest` | ❌ | Specific verticals to evaluate partner expertise: `telco`, `financial-services`, `retail`, `government`, etc. |

## Key Outputs

- **Partner Intel Brief** (Markdown) with sections:
  1. **Partner Profile** — company overview, size, revenue (if public), headquarters, key leadership
  2. **Service Portfolio:**
     - Managed services offered (SOC, NOC, cloud management, etc.)
     - Professional services capabilities (implementation, migration, consulting)
     - Technology practices (security, networking, cloud, DevOps)
     - Vendor certifications and partnerships
  3. **Technology Alliance Ecosystem** — other vendors in their portfolio, competitive and complementary relationships
  4. **Geographic Reach** — countries/regions with active operations, number of technical staff by region, language capabilities
  5. **Cloudflare Fit Assessment** (scored 1–5 on each dimension):
     - Product Alignment — which Cloudflare products map to their service portfolio and customer base
     - Vertical Expertise — depth in industries where Cloudflare has strong solutions (financial services, telco, retail, government)
     - Geographic Coverage — overlap between their footprint and Cloudflare's territory priorities
     - GTM Motion Compatibility — alignment between their sales model and Cloudflare's channel programs (co-sell, resell, referral, MSP)
  6. **Joint Value Proposition** — where Cloudflare + this partner creates differentiated value for customers
  7. **Risks and Gaps** — competitive conflicts, capability gaps, cultural or operational concerns
  8. **Investment Recommendation** — recommended partnership level, MDF allocation, and co-selling priority with justification
- Saved to: `~/helix-deck/partner/[partner-slug]-intel-[date].md`

## Quality Bar Highlights

1. **Competitive conflicts must be surfaced** — if the partner sells Zscaler, Akamai, or Palo Alto as primary offerings, that's critical context; don't bury it
2. **Geographic coverage must be specific** — "Latin America" is not a geography assessment; "offices in Mexico City, São Paulo, and Bogotá with 45 certified engineers" is
3. **Fit scoring must be justified** — a "4 out of 5" on product alignment without explaining which products and why is not useful
4. **Technology alliances reveal priorities** — a partner's other vendor relationships tell you where they invest and where Cloudflare fits (or doesn't) in their portfolio strategy
5. **Recommendation must be actionable** — "good partner potential" is not a recommendation; "invest in co-sell motion for Zero Trust in Brazil, allocate $25K MDF for Q3 demand gen" is
6. **Existing relationship data matters** — if this is a current partner, pull deal registration history, pipeline contribution, and certification status before making recommendations
