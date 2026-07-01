# Solution Brief

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Technical

---

## Summary

Concise 1–2 page brief mapping Cloudflare products to specific vendor or technology platforms — Epic, SAP, Workday, ServiceNow, Salesforce, Oracle, Microsoft 365, AWS/Azure/GCP workloads, and similar. Structured in 7 sections: Executive Summary, Architecture Overview, Integration Points, Key Benefits, Security & Compliance, Deployment Considerations, and Sources. Written for technical decision-makers and architects who need to understand how Cloudflare fits into their existing technology stack. Not a product datasheet — a solution mapping that shows how Cloudflare solves problems specific to the target platform.

## When To Use

- "Write a solution brief for Cloudflare + [vendor/technology]"
- "How does Cloudflare work with [platform]?"
- "I need a 1-pager showing Cloudflare + SAP integration"
- When a customer asks how Cloudflare fits with their core platform
- When an SE needs a quick reference for a technology-specific conversation
- When responding to an RFP that asks about specific platform integrations
- When a partner who specializes in [platform] needs Cloudflare positioning
- When building a library of solution briefs for common technology stacks
- "The customer runs [platform] — what's our story?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `platform` | ✅ | Target vendor or technology: `Epic`, `SAP`, `Workday`, `ServiceNow`, `Salesforce`, `Oracle`, `Microsoft-365`, `AWS`, `Azure`, `GCP`, or any named platform |
| `use_case` | ❌ | Specific use case to focus on: `performance`, `security`, `zero-trust-access`, `api-protection`, `ddos-protection`, `compliance` |
| `customer_context` | ❌ | Customer-specific context to personalize the brief |
| `industry` | ❌ | Customer's industry — used for compliance and regulatory context |
| `audience` | ❌ | `technical` (default — architects, engineers) or `executive` (CTO, CIO — emphasizes business outcomes over technical detail) |
| `length` | ❌ | `one-page` (default) or `two-page` (adds deployment detail and case studies) |

## Key Outputs

- **Solution Brief** (Markdown + PDF export) with sections:
  1. **Executive Summary** — 3–4 sentences: what this brief covers, why Cloudflare + [platform] matters, key value proposition
  2. **Architecture Overview** — how Cloudflare sits in front of, beside, or integrated with the target platform; includes a reference architecture description (or diagram reference)
  3. **Integration Points** — specific technical touchpoints:
     - DNS and traffic management
     - WAF and application security rules for the platform
     - Zero Trust access to the platform's admin consoles and APIs
     - API Gateway protection for platform APIs
     - Performance optimization (caching, Argo Smart Routing)
     - Bot Management for platform-facing endpoints
  4. **Key Benefits** — 4–6 benefits specific to this platform (not generic Cloudflare benefits):
     - Performance improvements with quantified benchmarks where available
     - Security posture improvements specific to the platform's threat model
     - Operational simplification and reduced complexity
     - Compliance enablement relevant to the platform's industry
  5. **Security & Compliance** — regulatory frameworks addressed (HIPAA for Epic, SOX for SAP, etc.), data residency considerations, audit trail capabilities
  6. **Deployment Considerations** — prerequisites, typical timeline, DNS cutover approach, rollback plan, platform-specific gotchas
  7. **Sources** — Cloudflare documentation links, case studies, benchmark data, and vendor integration guides
- Saved to: `~/helix-deck/solution-briefs/cf-[platform-slug]-brief-[date].md`

## Quality Bar Highlights

1. **Platform-specific, not generic** — "Cloudflare improves security" could be on any datasheet; "Cloudflare blocks credential stuffing attacks targeting Epic MyChart patient portals" is a solution brief
2. **Architecture must be accurate** — get the integration topology right; Cloudflare in front of SAP Fiori is different from Cloudflare protecting SAP BTP APIs
3. **Compliance mapping is critical** — if the platform serves healthcare (Epic), finance (SAP), or HR (Workday), the compliance section is often the most important part of the conversation
4. **Benefits must be quantifiable** — "faster performance" is weak; "40% reduction in TTFB for Workday dashboard loads based on Argo Smart Routing" is credible
5. **One page means one page** — brevity is the entire point; if it can't fit in 1–2 pages, it's a whitepaper, not a solution brief
6. **Sources must be verifiable** — every claim needs a link to Cloudflare docs, a published case study, or a cited benchmark; unsourced claims undermine credibility
