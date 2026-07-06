# Helix Customer 360 -- Trust Advisor Engine

**Catalog:** Cloudflare SuperSeal
**Category:** Sales / Strategic Intelligence
**Methodology:** Helix Framework -- Trusted Advisor Methodology for Platform Conversations

---

## Summary

Unified Trust Advisor Engine that combines the Helix 3-Act Methodology (Hook, Platform, Vision) with Utopia vertical intelligence and live account data to produce a complete customer engagement package for any named account. Every output is structured around the 3 acts of the Helix funnel: ACT 1 (Hook Setup) defines the branded demo strategy, ACT 2 (Trusted Advisor) delivers 6 Critical Findings and incumbent analysis from public reconnaissance, and ACT 3 (Customer Roadmap) maps a 6-phase sequential deployment plan with per-phase status (Active, Proposed, Explore). Pulls account data from Salesforce, enriches with Utopia wiki pages (11 verticals via Wiki MCP), cross-references Cloudflare Docs for product accuracy, and applies vertical-specific context (regulatory frameworks, industry pain points, competitive landscape, MEDDPICC patterns). Delivers role-tailored output for 9 consumer roles (BDR, AE, SE, SSE, SA, Manager, Director, VP, Intel). Supports `partner_mode` for channel partners where internal Cloudflare data is excluded. Designed to replace 5 separate skills (account-plan, customer-call-prep, cf1-bdr, discovery-guide, expansion-finder) with a single unified Trust Advisor workflow.

## When To Use

- "Run a 360 on [account]"
- "Build me a Trusted Advisor brief for [customer]"
- "I need to prep for [account] as a [BDR/AE/SE/SA]"
- "What's the customer roadmap for [account]?"
- "Generate the 3-act funnel for [customer]"
- "Give me the partner brief for [account]"
- "What are the critical findings for [customer]?"
- "What should I demo to [account]?"
- When a new AE/SE/SA inherits an account and needs a complete ramp document in one shot
- When preparing for an EBC, QBR, or executive sponsor meeting and need the full Helix funnel
- When a partner asks "what should we sell this customer?" and you need a data-backed answer without exposing internal Cloudflare data
- When building territory plans and need consistent intelligence across 10+ accounts
- When onboarding a new Cloudflare employee to a strategic account
- When an SA needs a publishable dossier with architecture diagrams, customer roadmap, and phased deployment plan

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | Yes | Customer account name (triggers Salesforce lookup) |
| `role` | No | Requesting role: `bdr`, `ae`, `se`, `sse`, `sa`, `manager`, `director`, `vp`, `intel` (default: `sa`) |
| `vertical` | No | Industry vertical: `telco`, `finserv`, `government`, `media`, `retail`, `hospitality`, `healthcare`, `utilities`, `airlines`, `automotive`, `education` -- auto-detected from Salesforce if omitted |
| `region` | No | Geographic region: `latam`, `emea`, `apac`, `amer` -- drives regulatory context and competitive landscape (default: `latam`) |
| `partner_mode` | No | If `true`, excludes all internal Cloudflare data (Salesforce, Lighthouse); output based on public intelligence, Cloudflare Docs product catalog, and vertical context only |
| `domains` | No | Customer domains for DNS/technical reconnaissance when available |
| `focus` | No | Specific focus area: `expansion`, `retention`, `competitive-displacement`, `greenfield`, `all` (default: `all`) |
| `depth` | No | Output depth: `min` (5-min read, key facts only), `standard` (default, full analysis), `executive` (board-ready narrative with financial framing) |
| `language` | No | Output language: `es` (default), `en`, `pt` |
| `sfdc_account_id` | No | Direct Salesforce Account ID for faster lookup |

---

## The Helix 3-Act Structure

Every output follows the Helix Framework 3-act funnel. This is not optional, it is the methodology:

### ACT 1: THE HOOK

_"Look what AI agents can do for your industry"_

The skill generates hook setup recommendations:
- **Vertical selection** for the branded portal (which industry demo to run)
- **WAF demo scenarios**: which PII categories to demonstrate (credit cards, passports, emails, phones, internal IPs)
- **AI Gateway demo scenarios**: fraud intent blocking with Llama Guard 3 (multilingual EN/ES)
- **Chat suggestions**: 2 industry use cases + 1 WAF demo prompt + 1 Gateway demo prompt
- **Language default**: `es` for LATAM, `en` for international, based on customer profile

### ACT 2: THE PLATFORM (Trusted Advisor)

_"We analyzed [Customer] before this conversation"_

The skill produces the Trusted Advisor section:
- **6 Critical Findings** from public reconnaissance (DNS records, HTTP headers, TXT records, certificate analysis, email configuration, security posture gaps)
- **Observed Technology Stack** with vendors detected via public evidence (no internal data)
- **Incumbent identification** with evidence: CDN vendor (Akamai, CloudFront, Fastly), WAF provider (Imperva, Radware), DNS provider (Route53, Azure DNS, NS1), email provider, certificate authority
- **Displacement targets** ranked by evidence strength and deal impact

### ACT 3: THE VISION (Customer Roadmap)

_"This is the complete path. Your Customer Roadmap with Cloudflare"_

The skill generates a 6-phase Customer Roadmap with per-phase status:

| Phase | Name | Products | Entry Point |
|-------|------|----------|-------------|
| F1 | CORE | DNS, SSL/TLS, DDoS Protection, WAF, CDN, Argo Smart Routing | Landing deal |
| F2 | AppSec + API | PageShield, Bot Management, API Shield, Load Balancing, Spectrum, Waiting Room | Expansion |
| F3 | SASE | Access, SWG, Email Security, DLP, CASB, RBI, Tunnels | Cloudflare One |
| F4 | Content + Dev | Images, Workers, R2, D1, Pages, Stream, Zaraz | Developer platform |
| F5 | Network | Magic WAN, Magic Transit, Magic Firewall, CNI | Network transformation |
| F6 | AI | AI Gateway, Inference Gateway, AI Firewall, Workers AI, DLP for AI, MCP Servers | AI governance |

**Product deduplication rules (no product appears in more than one phase):**
- Argo Smart Routing: F1 only (not F5)
- Workers AI: F6 only (not F4)
- Workers (compute): F4 only; Workers AI (inference): F6 only
- DLP (data protection): F3 only; DLP for AI (model input redaction): F6 only

Phase status per customer:
- **Active** -- already deployed and in use (confirmed via Salesforce or Lighthouse)
- **Proposed** -- part of the current sales conversation or active opportunity
- **Explore** -- future phases, not yet in any deal cycle

**Key insight for Cloudflare One GTM:** SASE enters at Phase 3 (F3), but the conversation starts with AI Gateway (F6) and CORE displacement (F1) as hooks. Cloudflare One becomes inevitable when you are already inside as the CORE platform.

---

## Key Outputs

The skill produces different deliverables based on the `role` input. All roles receive the 3-act structure; role-specific sections are added or removed based on what that persona needs to act.

### Core Intelligence (all roles)

- **Customer 360 Dossier** (Markdown, publishable to Wiki) structured as:
  1. **Executive Summary** -- 3-paragraph synthesis: who they are, where they stand with Cloudflare, and the single most important action to take now
  2. **Account Snapshot** -- firmographics, vertical classification, Cloudflare relationship tenure, contract dates, account team, last meaningful interaction
  3. **ACT 2: Trusted Advisor Section**
     - 6 Critical Findings (public recon: DNS, HTTP headers, certificates, email, security gaps)
     - Observed Technology Stack (incumbent vendors with public evidence)
     - Displacement targets with evidence and deal impact
  4. **ACT 3: Customer Roadmap** -- F1 through F6 with per-phase status (Active/Proposed/Explore), product mapping, and sequencing rationale
  5. **Vertical Context** -- industry-specific pain points, regulatory requirements, competitive pressure, digital transformation maturity, loaded dynamically from Utopia wiki pages
  6. **Gap Analysis** -- products not adopted vs. products they should have based on vertical context, architecture patterns, and peer benchmarks; scored by fit, urgency, and revenue impact
  7. **MEDDPICC Assessment** -- pre-filled framework: Metrics (quantified business impact), Economic Buyer (identified or gap), Decision Criteria, Decision Process, Paper Process, Identified Pain, Champion (named or gap), Competition
  8. **ACT 1: Hook Setup** -- recommended demo vertical, WAF scenarios, Gateway scenarios, chat suggestions, portal language
  9. **Commercial Strategy** -- prioritized expansion plays with estimated ACV impact, recommended bundles (Starter, Professional, Utopia), phased commercial approach aligned to F1-F6
  10. **Sources, Confidence, and Methodology** -- data sources used, MCP capability report, confidence levels, gaps that need human input

### Role-Specific Additions

- **BDR** (`role: bdr`): Adds outreach sequence (8-touch multi-channel cadence), persona-specific messaging matrix, discovery question framework, qualification criteria, LinkedIn connection request templates. Omits: architecture diagrams, MEDDPICC deep-dive, phased deployment technical detail.
- **AE** (`role: ae`): Adds deal strategy brief, MEDDPICC coaching notes, negotiation playbook, executive sponsor engagement plan, pipeline forecast inputs. Omits: technical architecture detail, POC specifications.
- **SE** (`role: se`): Adds POC proposal template, demo script aligned to identified pain points, technical validation checklist, integration architecture notes, Hook Setup with specific demo scenarios. Omits: BDR sequences, financial forecast detail.
- **SSE** (`role: sse`): Adds detailed architecture review, migration guide from incumbent, performance benchmarking framework, technical risk assessment. Omits: BDR sequences, commercial strategy detail.
- **SA** (`role: sa`): Full dossier -- all 10 sections plus architecture diagrams, Customer Roadmap visual, deal bridge analysis. This is the maximum output.
- **Manager** (`role: manager`): Adds pipeline health dashboard, coaching brief for the account team, resource allocation recommendation, escalation triggers. Omits: technical architecture, POC specs.
- **Director** (`role: director`): Adds territory-level context (how this account fits the territory strategy), partner leverage analysis, QBR-ready executive summary. Omits: technical detail, BDR sequences.
- **VP** (`role: vp`): Adds board-ready narrative, regional strategy alignment, competitive market share context, logo-level strategic value. Omits: all tactical and technical detail.
- **Intel** (`role: intel`): Pure intelligence mode. Produces all 3 acts without sales framing, coaching, or outreach. Sections: Account Snapshot, Current State, Vertical Intelligence, Competitive Landscape, Gap Analysis (neutral), Customer Roadmap (neutral, no "sell" language), MEDDPICC Facts (observed only, no coaching), Risk Signals, Sources and Confidence. Audience-agnostic: safe to share across roles without role-specific bias. No deal strategy, no email templates, no negotiation playbook.

### Output Formats

- Markdown file saved to: `~/helix-deck/360/[account-slug]-360-[role]-[date].md`
- Wiki page published to: `wiki.cfdata.org` in the operator's personal space (requires Wiki MCP)
- Google Doc created via Google Workspace MCP (optional, for sharing with non-wiki users)
- Jira ticket created for follow-up actions identified in the dossier (optional, requires Jira MCP)

---

## Execution Pipeline

### Phase 0: MCP CAPABILITY CHECK (always first, no exceptions)

Before any data collection, the skill detects which MCP servers are connected and reports availability:

```
MCP Capability Report
---------------------
Salesforce MCP:      CONNECTED    -- Account, Opportunity, Case, Contact data available
Wiki MCP:            CONNECTED    -- Utopia vertical pages available for dynamic fetch
Cloudflare Docs MCP: CONNECTED    -- Product catalog and battlecards available
Google Workspace:    CONNECTED    -- Email threads and meeting notes available
Jira MCP:            CONNECTED    -- Ticket history available
Elasticsearch MCP:   CONNECTED    -- Log analysis available
Lighthouse MCP:      NOT AVAILABLE -- Product usage, health alerts, propensity data DEGRADED
Radar MCP:           NOT AVAILABLE -- DNS recon, incumbent detection DEGRADED
Network MCP:         CONNECTED    -- Flow data and BGP data available

Confidence Impact:
- Without Lighthouse: Product usage and health data unavailable. Gap analysis based on Salesforce records only.
- Without Radar: Technical stack detection requires manual dig/nslookup. ACT 2 Critical Findings limited to Salesforce-derived data.

Overall Confidence: 7/10 (HIGH with Salesforce + Wiki; DEGRADED without Lighthouse and Radar)
```

The skill adapts subsequent phases based on what is available. Missing MCPs are never silently ignored.

### Phase 1: RECON

Salesforce lookup (minimum 6 queries: Account, Opportunity, Case, Contact, Activity, Contract) + DNS/domain analysis (if Radar MCP available and domains provided).

### Phase 2: DISCOVERY (Utopia Vertical Intelligence)

Dynamically fetch the Utopia wiki page for the detected vertical via Wiki MCP:

| Vertical | Wiki Page ID | Fallback |
|----------|-------------|----------|
| Telco | 1431715994 | Local context file |
| FinServ | 1187496098 | Local context file |
| Government | 1092896800 | Local context file |
| Media | 1182734455 | Local context file |
| Retail | 1214482141 | Local context file |
| Hospitality | 1431718498 | Local context file |
| Healthcare | 1182735362 | Local context file |
| Utilities | 1239967266 | Local context file |
| Airlines | 1182745297 | Local context file |
| Automotive | 1295366832 | Local context file |
| Education | 1182730943 | Local context file |

Extract from the Utopia page: pain points, regulatory framework, product mapping, competitive landscape, MEDDPICC patterns, discovery questions, bundles, case studies, and phased deployment guidance.

If Wiki MCP is unavailable, fall back to local `context/Verticals/[region]/[vertical].md` files bundled with the skill.

### Phase 3: EVALUATION

Product adoption analysis from Salesforce + Lighthouse (if available). Map currently deployed products to F1-F6 phases to determine phase status (Active/Proposed/Explore).

### Phase 4: ARCHITECTURE (ACT 2 -- Trusted Advisor)

Build the Trusted Advisor section:
- 6 Critical Findings from DNS/HTTP recon (Radar MCP) or Salesforce-derived data
- Observed Technology Stack with incumbent vendors
- Displacement targets ranked by evidence and deal impact
- Current vs. recommended architecture mapping

### Phase 5: GAP ANALYSIS

Cross-reference Utopia vertical "should have" products against Salesforce "actually has" products. Score each gap by fit (0-10), urgency (0-10), and revenue impact (estimated ACV). Sequence gaps according to F1-F6 phase order.

### Phase 6: STRATEGY

MEDDPICC pre-fill with explicit gaps. Competitive positioning from Cloudflare Docs battlecards. Champion mapping from Salesforce contacts. For `role: intel`, present facts only without coaching language.

### Phase 7: PIPELINE (ACT 3 -- Customer Roadmap)

Generate the 6-phase Customer Roadmap with per-phase status. Map active opportunities to phases. Recommend next phase based on sequential progression (never skip phases). Bundle recommendations aligned to Utopia tiers (Starter, Professional, Utopia).

### Phase 8: COMMERCIAL

Deal structure + negotiation context + pricing guidance. Phased commercial approach aligned to F1-F6. Omitted in `partner_mode` and `role: intel`.

### Phase 9: EXEC PREP (ACT 1 -- Hook Setup)

Generate Hook Setup: recommended demo vertical, WAF PII scenarios, AI Gateway fraud scenarios, chat suggestions, portal language. Generate executive talking points and "what not to promise" guardrails.

### Phase 10: METADATA

Source attribution + confidence scoring + gap documentation + MCP capability report (from Phase 0).

---

## Data Source Priority

The skill consults data sources in this priority order. If a higher-priority source is unavailable, it falls back to the next level and documents the gap:

| Priority | Source | What It Provides | MCP Required |
|----------|--------|------------------|--------------|
| 1 | Salesforce | Account, opportunities, cases, contacts, activities, contracts | Salesforce MCP |
| 2 | Lighthouse API | Products purchased, usage vs. caps, health alerts, propensity, billing, Halo ROI | Lighthouse MCP (not yet in SuperSeal) |
| 3 | Cloudflare Docs | Product catalog, feature specs, battlecards, best practices | Cloudflare Docs MCP |
| 4 | DNS/Domain Recon | Incumbent detection, security posture, email provider, DNSSEC status | Radar MCP (not yet in SuperSeal) |
| 5 | Utopia Wiki Pages | Industry pain points, regulatory requirements, competitive landscape, MEDDPICC patterns, bundles, case studies | Wiki MCP (11 pages, IDs mapped above) |
| 6 | Elasticsearch | Error patterns, log analysis for existing customers | Elasticsearch MCP |
| 7 | Wiki/Confluence | Existing account documentation, team pages, methodology docs | Wiki MCP |
| 8 | Google Workspace | Previous meeting notes, email threads, shared documents | Google Workspace MCP |

When a data source is unavailable, the skill must:
- State which source is missing in the Metadata section
- Describe what intelligence is degraded as a result
- Recommend how to fill the gap manually
- Never substitute assumptions for missing data

---

## Quality Bar: Helix Rules + Technical Standards

### The 6 Rules of the Helix Portal (from the methodology)

| # | Rule |
|---|------|
| 1 | **Everything comes from the 360 dossier** -- nothing invented, nothing generic |
| 2 | **No internal data shown to prospect** -- no ACV, no pipeline, no Lighthouse scores in customer-facing output |
| 3 | **Incumbent always mentioned** -- Akamai, CloudFront, Imperva, with public evidence |
| 4 | **Gateway demo = explicit fraud** -- not social manipulation (Llama Guard requires explicit harmful intent) |
| 5 | **defaultLang reflects the customer** -- LATAM = es, international = en |
| 6 | **6 phases always, only status changes** -- Prospect = all Proposed/Explore; Customer = F1/F2 Active, rest varies |

### Technical Quality Standards

1. **Salesforce-first, always** -- run a minimum of 6 queries (Account, Opportunity, Case, Contact, Activity, Contract) before writing a single word. If Salesforce returns empty, classify as PROSPECT and state it explicitly -- never fabricate a customer relationship.
2. **Vertical context is mandatory** -- every 360 must load the relevant Utopia wiki page (or local fallback). A hospitality 360 without PCI DSS, guest Wi-Fi, or seasonal traffic is incomplete.
3. **Role determines output, not truncation** -- a BDR output is fundamentally different from an SA output. Never truncate a full 360 and call it role-appropriate.
4. **MEDDPICC must have gaps** -- a perfect score on first generation means guessing. Champion and Economic Buyer must have explicit gaps with recommended actions.
5. **Customer Roadmap phases are sequential** -- F1 is always foundation; never recommend F4 (Developer) to an account without F1 (CORE). The roadmap reflects where the customer is today and what comes next.
6. **Partner mode is a hard boundary** -- `partner_mode: true` means zero internal Cloudflare data. No Salesforce IDs, no ACV, no health scores, no account team names.
7. **Competitive claims must be sourced** -- cite Cloudflare Docs battlecard, analyst report, or verified benchmark. Unsourced claims damage credibility.
8. **Language consistency** -- entire output in one language. Technical product names stay in English regardless.
9. **Action items must have owners and dates** -- "Follow up" is not an action item. "AE: Schedule discovery call with [CTO name] by [date]" is.
10. **Acknowledge what you don't know** -- missing MCP = explicit gap statement, never assumptions presented as facts.
11. **3-act structure is mandatory** -- every output must contain ACT 1 (Hook Setup), ACT 2 (Trusted Advisor), and ACT 3 (Customer Roadmap), even in `depth: min` mode.
12. **Phase 0 MCP report is mandatory** -- every execution starts with the capability check. The user must know what data sources are available before reading the analysis.

---

## Partner Mode

When `partner_mode: true`:

- **Excluded**: Salesforce data, Lighthouse data, internal health scores, ACV/ARR figures, account team names, internal opportunity IDs, Jira tickets, internal escalation history
- **Included**: Cloudflare Docs product catalog, Utopia vertical context, public DNS/domain data, general competitive intelligence, industry benchmarks, regulatory frameworks
- **Output label**: Every page and section header includes "(Partner Brief)" to prevent confusion with internal documents
- **Use case**: Channel partner enablement, partner SE training, joint selling preparation, partner onboarding to a vertical

---

## Vertical Context System

### Dynamic Source: Utopia Wiki Pages (Primary)

The skill dynamically fetches vertical-specific intelligence from Cloudflare's Utopia wiki pages via Wiki MCP. Each Utopia page is a Gold-standard vertical playbook containing: 6-phase use cases, top 10 pain points, MEDDPICC patterns, regulatory framework, competitive landscape, bundles, and phased deployment guidance.

All 11 verticals have dedicated Utopia pages with mapped wiki IDs (see Phase 2 table above).

### Static Fallback: Local Context Files

When Wiki MCP is unavailable, the skill loads from bundled context files:

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
- **Cloudflare Product Mapping** -- which products solve which pain points, mapped to F1-F6
- **Competitive Landscape** -- who the incumbents are in this vertical
- **MEDDPICC Patterns** -- common decision criteria, buying processes, champions by title
- **Discovery Questions** -- vertical-specific questions that demonstrate expertise
- **Bundles** -- recommended product bundles by maturity level (Starter, Professional, Utopia)
- **Case Studies** -- reference customers and outcomes (anonymized where required)

---

## Relationship to Existing Skills

This skill unifies and supersedes several existing SuperSeal skills:

| Existing Skill | What Customer 360 Replaces | How |
|----------------|---------------------------|-----|
| Account Plan | ACT 2 + ACT 3 of the SA output | 360 produces a superset with vertical context, Trusted Advisor findings, and Customer Roadmap |
| Customer Call Prep | Exec Prep phase (Phase 9) + Hook Setup | 360 includes ACT 1 demo recommendations and "what not to promise" |
| CF1 BDR | BDR role output | 360 with `role: bdr` produces outreach sequences with vertical-specific messaging from Utopia |
| Discovery Guide | Discovery phase (Phase 2) + Utopia context | 360 loads industry-specific discovery questions from Utopia wiki pages |
| Expansion Finder | Gap Analysis phase (Phase 5) | 360 produces scored whitespace analysis with F1-F6 Customer Roadmap sequencing |

Existing skills remain available for users who need only a specific output. Customer 360 is for users who need the complete Trust Advisor package in one execution.

---

## Diagram Integration (SuperSeal `Diagram` Skill)

After generating the 360 dossier, call the SuperSeal `Diagram` skill to produce architecture visuals. The 360 provides the data; Diagram renders it as SVG.

### 3 Diagrams per 360 (when role = sa, sse, or se)

| # | Diagram Type | Diagram Skill Template | Description |
|---|---|---|---|
| 1 | Architecture Map | `sase-three-column` | Current vs proposed: left = customer sources (identities, devices, locations), center = Cloudflare Edge with product grid mapped to F1-F6, right = destinations (apps, infra, networks) |
| 2 | Deal Bridge | `simple-flow` | Financial transformation: incumbent cost (left) through Cloudflare platform (center) to projected value (right), with ACV per phase |
| 3 | Customer Roadmap | `simple-flow` | 6-phase timeline F1-F6: each phase as a node with status color (green=Active, orange=Proposed, blue=Explore), products listed below, timeline on bottom axis |

### How to Call Diagram from 360

After completing ACT 3, generate the diagram description from the 360 data:

**Architecture Map prompt example:**
```
"SASE three-column architecture for [Account]. Left: [sources from dossier]. Center: Cloudflare Edge with [products from F1-F6]. Right: [destinations from dossier]. Title: [Account] - Proposed Cloudflare Architecture"
```

**Customer Roadmap prompt example:**
```
"Simple left-to-right flow showing 6 phases for [Account]. F1 CORE ([status]): [products]. F2 AppSec ([status]): [products]. F3 SASE ([status]): [products]. F4 Dev ([status]): [products]. F5 Network ([status]): [products]. F6 AI ([status]): [products]. Timeline at bottom. Title: [Account] - Customer Roadmap F1-F6"
```

### Diagram Rules
- Use data from the 360 dossier only -- never invent components
- Phase status colors: Active = green (#22C55E), Proposed = orange (#F6821F), Explore = blue (#1A6FD4)
- Incumbent products shown in red-dashed boxes when displacement is recommended
- Labels in the same language as the 360 output; product names always in English
- Canvas: 1400x900 default; 1920x1080 for Architecture Map if >12 products

### When NOT to Generate Diagrams
- `role: bdr, manager, director, vp` -- these roles get narrative, not diagrams
- `depth: min` -- minimal output skips diagrams
- `partner_mode: true` -- skip unless explicitly requested

---

## Output Format Template (MANDATORY)

Every 360 output MUST follow this exact document structure. The ORDER and NAMING is non-negotiable:

```
# HELIX 360 -- [Account Name]
Dossier de Trusted Advisor | Rol: [Role] | Fecha: [Date] | Vertical: [Vertical]

## Reporte de Capacidad MCP (Fase 0)
[Table: MCP source | Status | Confidence Impact]

## Snapshot de la Cuenta
[Firmographics, SFDC entities, domains, relationship status]

## ACTO 1: EL HOOK
### Estrategia de Demo / Escenarios WAF PII / Escenarios AI Gateway / Sugerencias de Chat

## ACTO 2: LA PLATAFORMA (Trusted Advisor)
### 6 Hallazgos Criticos / Stack Tecnologico / Incumbentes para Desplazamiento

## ACTO 3: LA VISION (Customer Roadmap)
### F1-F6 with status, product tables, and visual roadmap

## MEDDPICC / Estructura Comercial / POC / Talking Points / Metadata

## Diagramas (role: sa, sse, se only)
[Call Diagram skill with prompts derived from ACT 3 data]
```

---

## Methodology Reference

This skill implements the **Helix Framework -- Trusted Advisor Methodology for Platform Conversations**, documented at:

`https://wiki.cfdata.org/spaces/~janguiano/pages/1427854878/Helix+Framework+%E2%80%94+Trusted+Advisor+Methodology+for+Platform+Conversations`

The methodology was piloted with 6 LATAM accounts including Palace Resorts (validated June 24, 2026) and presented to Annika Garbers (Head of Cloudflare One GTM) on June 26, 2026, with approval for expansion to additional regions.
