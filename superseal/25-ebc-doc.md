# EBC Doc

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / EBC

---

## Summary

Turn a BriefingSource PDF into a fully populated internal Executive Briefing Center document. Maps structured fields from the BriefingSource PDF — attendees, objectives, agenda, account context, competitive landscape, and desired outcomes — into the standard Cloudflare EBC briefing structure. Eliminates the manual copy-paste workflow between BriefingSource and the internal briefing doc template. Produces a ready-to-circulate internal document that the account team, presenters, and CXTP coordinators can use to prepare for the engagement.

## When To Use

- "Convert this BriefingSource PDF into an EBC briefing doc"
- "I have the BriefingSource form — build the internal briefing"
- "Populate the EBC doc from this PDF"
- When a BriefingSource PDF has been completed and needs to become an internal briefing
- When the CXTP team needs to distribute briefing materials to presenters
- When an account team has filled out BriefingSource but hasn't created the internal doc yet
- Before an EBC planning call to ensure all stakeholders have the same context

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `briefingsource_pdf` | ✅ | The BriefingSource PDF file (uploaded or file path) |
| `account_name` | ❌ | Account name — auto-extracted from PDF if omitted |
| `ebc_date` | ❌ | EBC date — auto-extracted from PDF if omitted |
| `additional_context` | ❌ | Any context not in the PDF: recent deal updates, competitive intel, internal politics |
| `template_version` | ❌ | Internal briefing template version to use — defaults to latest |
| `enrich_sfdc` | ❌ | If `true`, enriches the doc with SFDC data (account, opportunities, cases) beyond what's in the PDF |

## Key Outputs

- **Internal EBC Briefing Doc** (Markdown + DOCX export) with sections:
  1. **EBC Overview** — date, location, account name, account team, CXTP coordinator
  2. **Customer Attendees** — names, titles, roles, LinkedIn profiles, known priorities
  3. **Cloudflare Attendees** — presenters, executives, account team members with session assignments
  4. **Account Context** — industry, current Cloudflare products, ACV, contract status, relationship history
  5. **EBC Objectives** — what the account team wants to achieve, mapped from BriefingSource
  6. **Customer Priorities** — what the customer cares about, extracted from BriefingSource and enriched
  7. **Competitive Landscape** — incumbents, alternatives being evaluated, known competitive positioning
  8. **Agenda** — session-by-session breakdown with topic, presenter, duration, and key messages
  9. **Desired Outcomes** — specific, measurable outcomes for the EBC (not "strengthen the relationship")
  10. **Pre-Read Materials** — links to relevant case studies, product briefs, or technical docs for presenters
  11. **Open Questions** — gaps in the BriefingSource data that need to be filled before the EBC
- Saved to: `~/helix-deck/ebc/[account-slug]-ebc-briefing-[date].md`

## Quality Bar Highlights

1. **PDF extraction must be accurate** — validate every extracted field against the source PDF; a wrong attendee name or misread objective undermines the entire doc
2. **Enrich, don't just copy** — the value is in adding context beyond the PDF: SFDC data, competitive intel, relationship history; a straight copy is not worth the skill
3. **Open questions must be flagged prominently** — if the BriefingSource has gaps (missing attendee titles, vague objectives), call them out clearly so they get resolved before the EBC
4. **Desired outcomes must be specific** — "build the relationship" is not an outcome; "secure agreement to run a 30-day POC on Zero Trust" is
5. **Presenter prep depends on this doc** — if a presenter walks into a session without reading the briefing doc, that's a process failure; but if the briefing doc is bad, that's our failure
