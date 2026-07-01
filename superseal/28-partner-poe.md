# Partner POE

**Catalog:** Cloudflare SuperSeal  
**Category:** Channel / Partner

---

## Summary

Builds a proof-of-execution (POE) package for MDF (Market Development Fund) claims. Validates attendance lists, event photos, lead lists, and invoices against the Cloudflare partner portal schema and MDF program requirements. Checks regional compliance requirements including GDPR (EMEA), LGPD (Brazil), and CCPA (US) for lead data handling. Produces a submission-ready package that meets all documentation requirements for MDF reimbursement, reducing the back-and-forth between partner managers and the channel ops team.

## When To Use

- "Build a POE package for the [event] MDF claim"
- "Validate these MDF documents before submission"
- "Check if this POE is complete for [partner]"
- After a partner-funded event, webinar, or campaign has been executed
- When a partner submits MDF claim documents that need validation
- When preparing MDF documentation for quarterly reconciliation
- Before submitting a POE to avoid rejection and resubmission delays
- When a partner asks "what do I need to submit for my MDF claim?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `partner_name` | ✅ | Partner company name |
| `event_name` | ✅ | Name of the event, campaign, or activity being claimed |
| `mdf_amount` | ✅ | MDF amount being claimed (USD or local currency) |
| `region` | ✅ | Region for compliance requirements: `LATAM`, `EMEA`, `NAM`, `APAC` |
| `attendance_list` | ❌ | Uploaded CSV or file with attendee names, titles, companies, emails |
| `photos` | ❌ | Event photos showing Cloudflare branding, partner branding, and attendance |
| `lead_list` | ❌ | Generated leads from the activity with contact details and consent status |
| `invoices` | ❌ | Vendor invoices, receipts, or proof of spend |
| `event_date` | ❌ | Date of the event or campaign |

## Key Outputs

- **POE Validation Report** (Markdown) with sections:
  1. **Submission Status** — Ready to Submit / Incomplete / Needs Correction
  2. **Document Checklist:**
     - ✅/❌ Attendance list — minimum attendee threshold met, required fields present
     - ✅/❌ Event photos — Cloudflare branding visible, partner branding visible, crowd shots
     - ✅/❌ Lead list — contacts with opt-in consent, required fields (name, email, company, title)
     - ✅/❌ Invoices — amounts match MDF claim, dates align with event, payable to valid vendor
     - ✅/❌ Event summary — description of activity, objectives, and outcomes
  3. **Compliance Check:**
     - GDPR compliance (EMEA) — consent records, data processing basis, retention policy
     - LGPD compliance (Brazil) — consent mechanism, data subject rights notice
     - CCPA compliance (US) — opt-out mechanism, privacy notice
  4. **Data Quality Issues** — duplicate contacts, missing fields, invalid emails, non-business emails
  5. **Discrepancies** — mismatches between attendance list and lead list, invoice amounts vs. MDF claim, date inconsistencies
  6. **Missing Items** — specific documents or fields needed to complete the submission
  7. **Submission Package** — organized, named files ready for upload to partner portal
- Saved to: `~/helix-deck/partner/[partner-slug]-poe-[event-slug]-[date].md`

## Quality Bar Highlights

1. **Regional compliance is non-negotiable** — a POE with GDPR-non-compliant lead data in EMEA will be rejected and creates legal risk; validate consent mechanisms for every region
2. **Invoice amounts must match** — if the MDF claim is $10,000 but invoices total $8,500, flag it immediately; this is the #1 reason for claim rejection
3. **Photo requirements are specific** — generic stock photos or photos without visible Cloudflare branding are insufficient; specify exactly what's needed
4. **Lead quality over quantity** — 50 qualified leads with proper consent beat 500 badge scans with no opt-in; flag non-compliant leads for removal
5. **Reduce partner friction** — the goal is to make MDF claims painless for partners; clearly list exactly what's missing in plain language, not portal jargon
6. **Date alignment matters** — the event date, invoice dates, and MDF approval date must form a coherent timeline; flag any sequence that doesn't make sense
