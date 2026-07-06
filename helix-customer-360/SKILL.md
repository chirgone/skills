# Customer 360

**Catalog:** Cloudflare SuperSeal  
**Category:** Sales / Strategic Intelligence

---

## Summary

Role-aware strategic intelligence engine that produces a complete customer dossier for any named account. Executes a 10-phase analysis pipeline (Recon, Discovery, Evaluation, Architecture, Gap Analysis, Strategy, Pipeline, Commercial, Executive Prep, Metadata) and delivers a tailored output bundle based on the requesting role (BDR, AE, SE, SSE, SA, Manager, Director, VP). Pulls account data from Salesforce (Account, Opportunity, Case, Contact, Activity, Contract objects), enriches with Cloudflare product documentation, and cross-references vertical-specific context (regulatory frameworks, industry pain points, competitive landscape) to produce deliverables ranging from BDR outreach sequences to full SA-grade DOCX dossiers with architecture diagrams, MEDDPICC analysis, and Customer Roadmap methodology. Supports `partner_mode` for channel partners where internal Cloudflare data is excluded and only public intelligence and vertical context drive the analysis. Designed to replace 5 separate skills (account-plan, customer-call-prep, cf1-bdr, discovery-guide, expansion-finder) with a single unified workflow that adapts output depth, format, and focus to the consumer's role.

## When To Use

- "Run a 360 on [account]"
- "Build me a full dossier for [customer]"
- "I need to prep for [account] as a [BDR/AE/SE/SA]"
- "What's our full story on [customer]?"
- "Generate a customer roadmap for [account]"
- "Give me the partner brief for [account]"
- When a new AE/SE/SA inherits an account and needs a complete ramp document in one shot
- When preparing for an EBC, QBR, or executive sponsor meeting and need the full picture
- When a partner asks "what should we sell this customer?" and you need a data-backed answer without exposing internal Cloudflare data
- When building territory plans and need consistent intelligence across 10+ accounts
- When onboarding a new Cloudflare employee to a strategic account
- When an SA needs a publishable dossier with architecture diagrams, gap analysis, and phased deployment plan

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | Yes | Customer account name (triggers Salesforce lookup) |
| `role` | No | Requesting role: `bdr`, `ae`, `se`, `sse`, `sa`, `manager`, `director`, `vp` (default: `sa`) |
| `vertical` | No | Industry vertical: `telco`, `finserv`, `government`, `media`, `retail`, `hospitality`, `healthcare`, `utilities`, `airlines`, `automotive`, `education` -- auto-detected from Salesforce if omitted |
| `region` | No | Geographic region: `latam`, `emea`, `apac`, `amer` -- drives regulatory context and competitive landscape (default: `latam`) |
| `partner_mode` | No | If `true`, excludes all internal Cloudflare data (Salesforce, Lighthouse); output based on public intelligence, Cloudflare Docs product catalog, and vertical context only |
| `domains` | No | Customer domains for DNS/technical reconnaissance when available |
| `focus` | No | Specific focus area: `expansion`, `retention`, `competitive-displacement`, `greenfield`, `all` (default: `all`) |
| `depth` | No | Output depth: `min` (5-min read, key facts only), `standard` (default, full analysis), `executive` (board-ready narrative with financial framing) |
| `language` | No | Output language: `es` (default), `en`, `pt` |
| `sfdc_account_id` | No | Direct Salesforce Account ID for faster lookup |

## Key Outputs

The skill produces different deliverables based on the `role` input. All roles receive a core intelligence package; role-specific sections are added or removed based on what that persona needs to act.

### Core Intelligence (all roles)

- **Customer 360 Dossier** (Markdown, publishable to Wiki) with sections:
  1. **Executive Summary** -- 3-paragraph synthesis: who they are, where they stand with Cloudflare, and the single most important action to take now
  2. **Account Snapshot** -- firmographics, vertical classification, Cloudflare relationship tenure, contract dates, account team, last meaningful interaction
  3. **Current State** -- products deployed, usage patterns, support ticket trends, health indicators, satisfaction signals
  4. **Vertical Context** -- industry-specific pain points, regulatory requirements, competitive pressure, digital transformation maturity, loaded from `context/Verticals/[region]/[vertical].md`
  5. **Gap Analysis** -- products not adopted vs. products they should have based on vertical context, architecture patterns, and peer benchmarks; scored by fit, urgency, and revenue impact
  6. **Competitive Landscape** -- incumbent vendors identified via DNS/technical recon, displacement opportunities, competitive talking points sourced from Cloudflare Docs battlecards
  7. **MEDDPICC Assessment** -- pre-filled framework: Metrics (quantified business impact), Economic Buyer (identified or gap), Decision Criteria, Decision Process, Paper Process, Identified Pain, Champion (named or gap), Competition
  8. **Customer Roadmap** -- phased deployment plan using Cloudflare methodology:
     - Phase 1+2: CDN, WAF, Bot Management, DDoS
     - Phase 3: SASE (Access, Gateway, CASB, DLP, Browser Isolation)
     - Phase 4: Developer Platform (Workers, Pages, R2, D1)
     - Phase 5: Network Services (Magic WAN, Magic Transit, Spectrum)
     - Phase 6: AI and Innovation (Workers AI, AI Gateway, AI Firewall, MCP)
  9. **Commercial Strategy** -- prioritized expansion plays with estimated ACV impact, recommended bundles (Starter, Professional, Utopia), phased commercial approach
  10. **Sources and Methodology** -- data sources used, confidence levels, gaps that need human input

### Role-Specific Additions

- **BDR** (`role: bdr`): Adds outreach sequence (8-touch multi-channel cadence), persona-specific messaging matrix, discovery question framework, qualification criteria, LinkedIn connection request templates. Omits: architecture diagrams, MEDDPICC deep-dive, phased deployment technical detail.
- **AE** (`role: ae`): Adds deal strategy brief, MEDDPICC coaching notes, negotiation playbook, executive sponsor engagement plan, pipeline forecast inputs. Omits: technical architecture detail, POC specifications.
- **SE** (`role: se`): Adds POC proposal template, demo script aligned to identified pain points, technical validation checklist, integration architecture notes. Omits: BDR sequences, financial forecast detail.
- **SSE** (`role: sse`): Adds detailed architecture review, migration guide from incumbent, performance benchmarking framework, technical risk assessment. Omits: BDR sequences, commercial strategy detail.
- **SA** (`role: sa`): Full dossier -- all 10 sections plus architecture diagrams, Customer Roadmap visual, deal bridge analysis. This is the maximum output.
- **Manager** (`role: manager`): Adds pipeline health dashboard, coaching brief for the account team, resource allocation recommendation, escalation triggers. Omits: technical architecture, POC specs.
- **Director** (`role: director`): Adds territory-level context (how this account fits the territory strategy), partner leverage analysis, QBR-ready executive summary. Omits: technical detail, BDR sequences.
- **VP** (`role: vp`): Adds board-ready narrative, regional strategy alignment, competitive market share context, logo-level strategic value. Omits: all tactical and technical detail.

### Output Formats

- Markdown file saved to: `~/helix-deck/360/[account-slug]-360-[role]-[date].md`
- Wiki page published to: `wiki.cfdata.org` in the operator's personal space (requires Wiki MCP)
- Google Doc created via Google Workspace MCP (optional, for sharing with non-wiki users)
- Jira ticket created for follow-up actions identified in the dossier (optional, requires Jira MCP)

## Quality Bar Highlights

1. **Salesforce-first, always** -- run a minimum of 6 queries (Account, Opportunity, Case, Contact, Activity, Contract) before writing a single word; a 360 without CRM data is creative writing, not intelligence. If Salesforce returns empty for an account, classify as PROSPECT and state it explicitly -- never fabricate a customer relationship.
2. **Vertical context is mandatory** -- every 360 must load and apply the relevant vertical context file; a hospitality 360 that doesn't mention PCI DSS for payment processing, guest Wi-Fi architecture, or seasonal traffic patterns is incomplete. If no vertical context file exists for the industry, flag it as a gap and use the closest available vertical as a proxy.
3. **Role determines output, not truncation** -- a BDR output is not a shortened SA output; it is a fundamentally different document with different sections, different language, and different action items. A BDR needs email copy and LinkedIn templates; an SA needs architecture diagrams and MEDDPICC. Never truncate a full 360 and call it role-appropriate.
4. **MEDDPICC must have gaps** -- a perfect MEDDPICC score on first generation means the skill is guessing. At minimum, Champion and Economic Buyer should have explicit gaps noted with recommended actions to fill them (e.g., "Champion: Not identified -- recommend mapping org chart with AE before next call"). Marking every field as complete without direct customer input is dishonest.
5. **Customer Roadmap phases are sequential, not a menu** -- Phase 1+2 is always the foundation; do not recommend Phase 4 (Developer Platform) to an account that hasn't deployed Phase 1 (CDN/WAF). The roadmap must reflect where the customer actually is today and what comes next, not what generates the most pipeline.
6. **Partner mode is a hard boundary** -- when `partner_mode: true`, zero internal Cloudflare data appears in the output. No Salesforce IDs, no ACV figures, no internal health scores, no account team names. The output must be safe to hand to a channel partner without redaction. Violating this boundary is a trust-breaking event.
7. **Competitive claims must be sourced** -- never assert "Akamai is slower" or "Zscaler is more expensive" without citing a specific Cloudflare Docs battlecard, analyst report, or verified benchmark. Unsourced competitive claims damage credibility in front of customers and partners.
8. **Language consistency** -- the entire output must be in one language (set by `language` input); mixing Spanish and English within a document is never acceptable. Technical product names (Workers, Magic Transit, CASB) stay in English regardless of output language.
9. **Action items must have owners and dates** -- "Follow up with the customer" is not an action item. "AE: Schedule discovery call with [CTO name] by [date] to validate SASE timeline" is. Every action item in the dossier must specify who, what, and when.
10. **Acknowledge what you don't know** -- if DNS recon is unavailable (no Radar MCP), say "Technical stack detection unavailable -- recommend manual reconnaissance." If Lighthouse data is unavailable, say "Product usage and health data not available -- analysis based on Salesforce records and vertical benchmarks only." Never fill gaps with assumptions presented as facts.

---

## Vertical Context Files

The skill loads vertical-specific intelligence from context files stored alongside the skill:

```
context/Verticals/
  latam/
    hospitality.md    -- Hotel/resort/tourism: PCI, guest Wi-Fi, seasonal traffic, IoT
    finserv.md        -- Banking/insurance: CNBV, BACEN, SFC, eBanking, PCI DSS 4.0
    telco.md          -- MNO/MVNO/Cable/ISP: SP partnerships, DNS at scale, CGNAT
    media.md          -- Streaming/news/entertainment: live events, CDN at scale, DRM
    retail.md         -- E-commerce/omnichannel: peak traffic, bot protection, API security
    government.md     -- Federal/state/municipal: sovereignty, compliance, citizen services
    healthcare.md     -- Hospital/pharma/healthtech: HIPAA, HL7, telemedicine
    utilities.md      -- Energy/water/mining: OT/IT convergence, SCADA, remote sites
    airlines.md       -- Aviation/travel: booking engines, loyalty, seasonal
    automotive.md     -- Manufacturing/connected vehicles: supply chain, IoT, API
    education.md      -- Universities/edtech: research networks, student services
  emea/              -- (future: GDPR-centric regulatory context)
  apac/              -- (future: APAC regulatory and market context)
  amer/              -- (future: US/Canada regulatory context)
```

Each vertical file follows a standard structure:
- **Industry Overview** -- market dynamics, key players, LATAM specifics
- **Top 10 Pain Points** -- ranked by frequency across customer conversations
- **Regulatory Framework** -- country-by-country compliance requirements
- **Cloudflare Product Mapping** -- which products solve which pain points
- **Competitive Landscape** -- who the incumbents are in this vertical
- **MEDDPICC Patterns** -- common decision criteria, buying processes, champions by title
- **Discovery Questions** -- vertical-specific questions that demonstrate expertise
- **Bundles** -- recommended product bundles by maturity level (Starter, Professional, Utopia)
- **Case Studies** -- reference customers and outcomes (anonymized where required)

## Execution Pipeline

The skill executes 10 phases in sequence. Each phase adds data to the intelligence context; later phases reference earlier findings:

```
Phase 1: RECON          Salesforce lookup + DNS/domain analysis (if domains provided)
Phase 2: DISCOVERY      Vertical context loading + regulatory framework identification
Phase 3: EVALUATION     Product adoption analysis + health assessment + support trends
Phase 4: ARCHITECTURE   Current vs. recommended architecture mapping
Phase 5: GAP ANALYSIS   Whitespace identification + peer benchmarking + fit scoring
Phase 6: STRATEGY       MEDDPICC pre-fill + competitive positioning + champion mapping
Phase 7: PIPELINE       Commercial sizing + bundle recommendations + phased approach
Phase 8: COMMERCIAL     Deal structure + negotiation context + pricing guidance
Phase 9: EXEC PREP      Executive summary + talking points + "what not to promise"
Phase 10: METADATA      Source attribution + confidence scoring + gap documentation
```

In `partner_mode`, Phases 1 and 3 operate on public data only (no Salesforce). The output clearly states "Analysis based on public intelligence and vertical benchmarks" in the metadata.

## Data Source Priority

The skill consults data sources in this priority order. If a higher-priority source is unavailable, it falls back to the next level and documents the gap:

| Priority | Source | What It Provides | MCP Required |
|----------|--------|------------------|--------------|
| 1 | Salesforce | Account, opportunities, cases, contacts, activities, contracts | Salesforce MCP |
| 2 | Lighthouse API | Products purchased, usage vs. caps, health alerts, propensity, billing, Halo ROI | Lighthouse MCP (not yet in SuperSeal) |
| 3 | Cloudflare Docs | Product catalog, feature specs, battlecards, best practices | Cloudflare Docs MCP |
| 4 | DNS/Domain Recon | Incumbent detection, security posture, email provider, DNSSEC status | Radar MCP (not yet in SuperSeal) |
| 5 | Vertical Context | Industry pain points, regulatory requirements, competitive landscape, MEDDPICC patterns | Local context files (bundled with skill) |
| 6 | Elasticsearch | Error patterns, log analysis for existing customers | Elasticsearch MCP |
| 7 | Wiki/Confluence | Existing account documentation, team pages, methodology docs | Wiki MCP |
| 8 | Google Workspace | Previous meeting notes, email threads, shared documents | Google Workspace MCP |

When a data source is unavailable, the skill must:
- State which source is missing in the Metadata section
- Describe what intelligence is degraded as a result
- Recommend how to fill the gap manually
- Never substitute assumptions for missing data

## Partner Mode

When `partner_mode: true`:

- **Excluded**: Salesforce data, Lighthouse data, internal health scores, ACV/ARR figures, account team names, internal opportunity IDs, Jira tickets, internal escalation history
- **Included**: Cloudflare Docs product catalog, vertical context files, public DNS/domain data, general competitive intelligence, industry benchmarks, regulatory frameworks
- **Output label**: Every page and section header includes "(Partner Brief)" to prevent confusion with internal documents
- **Use case**: Channel partner enablement, partner SE training, joint selling preparation, partner onboarding to a vertical

## Relationship to Existing Skills

This skill is designed to unify and supersede several existing SuperSeal skills:

| Existing Skill | What Customer 360 Replaces | How |
|----------------|---------------------------|-----|
| Account Plan | Sections 1-9 of the SA output | 360 produces a superset with vertical context and Customer Roadmap |
| Customer Call Prep | Executive Prep phase (Phase 9) | 360 includes "What I want to learn / should say / should NOT promise" |
| CF1 BDR | BDR role output | 360 with `role: bdr` produces outreach sequences with vertical-specific messaging |
| Discovery Guide | Discovery phase (Phase 2) + vertical context | 360 loads industry-specific discovery questions from vertical context files |
| Expansion Finder | Gap Analysis phase (Phase 5) | 360 produces scored whitespace analysis with Customer Roadmap sequencing |

Existing skills remain available for users who need only a specific output. Customer 360 is for users who need the complete picture in one execution.
