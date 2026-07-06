---
name: helix-customer-360
description: >
  Unified Trust Advisor Engine implementing the Helix 3-Act Methodology
  (Hook, Platform, Vision) combined with Utopia vertical intelligence and
  live account data. Produces a complete customer engagement package for
  any named account structured around 3 acts: ACT 1 (Hook Setup) defines
  branded demo strategy, ACT 2 (Trusted Advisor) delivers 6 Critical
  Findings and incumbent analysis from public reconnaissance, ACT 3
  (Customer Roadmap) maps a 6-phase sequential deployment plan with
  per-phase status (Active/Proposed/Explore). Pulls from Salesforce,
  Utopia wiki pages (11 verticals via Wiki MCP), Cloudflare Docs, and
  vertical-specific context (regulatory, competitive, MEDDPICC). Delivers
  role-tailored output for 9 roles: BDR, AE, SE, SSE, SA, Manager,
  Director, VP, and Intel (pure intelligence without sales framing).
  Supports partner_mode for channel partners. Starts every execution with
  Phase 0 MCP Capability Check to report available vs missing data sources.
  Designed for LATAM but applicable globally. Replaces 5 separate skills
  (account-plan, customer-call-prep, cf1-bdr, discovery-guide,
  expansion-finder) with a single unified Trust Advisor workflow.
---

## When to Use

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

## What I Do

Executes the Helix Trust Advisor pipeline against a named account. Starts with Phase 0 (MCP Capability Check) to detect connected data sources and report confidence impact. Then runs an 11-phase intelligence pipeline: Recon (Salesforce 6-query minimum), Discovery (Utopia wiki page fetch for the detected vertical covering 11 industries), Evaluation (product adoption mapped to 6 canonical phases), Architecture (ACT 2 Trusted Advisor: 6 Critical Findings, incumbent detection, tech stack), Gap Analysis (Utopia "should have" vs Salesforce "actually has"), Strategy (MEDDPICC with explicit gaps), Pipeline (ACT 3 Customer Roadmap: F1 CORE, F2 AppSec+API, F3 SASE, F4 Content+Dev, F5 Network, F6 AI with Active/Proposed/Explore status), Commercial (deal structure aligned to F1-F6), Exec Prep (ACT 1 Hook Setup: demo vertical, WAF PII scenarios, AI Gateway fraud scenarios, chat suggestions), and Metadata (source attribution, confidence scoring, MCP capability report). Delivers role-appropriate output: BDR gets outreach sequences; AE gets deal briefs and MEDDPICC coaching; SE gets POC proposals and Hook Setup; SSE gets architecture reviews; SA gets the full 360 dossier; Manager gets pipeline coaching; Director gets territory summaries; VP gets board-ready narratives; Intel gets pure facts without sales framing. Supports partner_mode (hard boundary: zero internal data) and three output languages (Spanish, English, Portuguese). Publishes to Wiki, Google Docs, or local Markdown. Implements the 6 Rules of the Helix Portal as quality standards.

## Do NOT use me for

- A single-question account lookup (use account-plan or customer-call-prep for lighter outputs)
- Real-time product usage and health data (Lighthouse MCP not yet available in SuperSeal; the skill documents this gap and recommends manual lookup)
- Technical DNS/domain reconnaissance (Radar MCP not yet available in SuperSeal; the skill documents this gap and recommends manual dig/nslookup)
- Generating architecture SVG/PNG diagrams without Diagram skill (call the `Diagram` skill from SuperSeal to render architecture, SASE, or flow diagrams as self-contained SVGs)
- Accounts with zero presence in Salesforce and no public domain (no data sources available to analyze)
- Any output intended for direct external customer delivery without human review and approval
- Non-account questions (product documentation, pricing, Worker code debugging, DNS troubleshooting)

---

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `account_name` | Yes | Customer account name (triggers Salesforce lookup) |
| `role` | No | Requesting role: `bdr`, `ae`, `se`, `sse`, `sa`, `manager`, `director`, `vp`, `intel` (default: `sa`) |
| `vertical` | No | Industry vertical: `telco`, `finserv`, `government`, `media`, `retail`, `hospitality`, `healthcare`, `utilities`, `airlines`, `automotive`, `education` -- auto-detected from Salesforce if omitted |
| `region` | No | Geographic region: `latam`, `emea`, `apac`, `amer` -- drives regulatory context (default: `latam`) |
| `partner_mode` | No | If `true`, excludes all internal Cloudflare data |
| `domains` | No | Customer domains for DNS/technical reconnaissance |
| `focus` | No | Focus area: `expansion`, `retention`, `competitive-displacement`, `greenfield`, `all` (default: `all`) |
| `depth` | No | Output depth: `min`, `standard` (default), `executive` |
| `language` | No | Output language: `es` (default), `en`, `pt` |

## The Helix 3-Act Structure

Every output follows this structure (non-negotiable):

**ACT 1: THE HOOK** -- "Look what AI agents can do for your industry"
- Vertical selection for branded portal demo
- WAF PII demo scenarios (credit cards, passports, emails, phones)
- AI Gateway fraud demo scenarios (Llama Guard 3, multilingual)
- 4 chat suggestions (2 use cases + 1 WAF + 1 Gateway)

**ACT 2: THE PLATFORM (Trusted Advisor)** -- "We analyzed [Customer] before this conversation"
- 6 Critical Findings from public reconnaissance
- Observed Technology Stack with vendors and evidence
- Incumbent identification and displacement targets

**ACT 3: THE VISION (Customer Roadmap)** -- "This is the complete path"
- F1 CORE (DNS, SSL, DDoS, WAF, CDN, Argo Smart Routing)
- F2 AppSec + API (PageShield, Bot Mgmt, API Shield, LB, Spectrum, Waiting Room)
- F3 SASE (Access, SWG, Email Security, DLP, CASB, RBI, Tunnels)
- F4 Content + Dev (Images, R2, D1, Pages, Stream, Workers, Zaraz)
- F5 Network (Magic WAN, Magic Transit, Magic Firewall, CNI)
- F6 AI (AI Gateway, Inference Gateway, AI Firewall, Workers AI, DLP for AI, MCP Servers)
- Per-phase status: Active / Proposed / Explore

**IMPORTANT -- Product Deduplication Rules:**
- Argo Smart Routing belongs ONLY in F1 CORE (never in F5 Network)
- Workers AI belongs ONLY in F6 AI (never in F4 Content + Dev)
- Workers (compute platform) belongs in F4; Workers AI (inference) belongs in F6
- DLP (data protection) belongs in F3 SASE; DLP for AI (model input redaction) belongs in F6 AI
- Each product appears in exactly ONE phase -- no duplicates across phases

## Execution Pipeline

```
Phase 0:  MCP CHECK       Detect connected MCPs, report confidence impact
Phase 1:  RECON           Salesforce 6-query lookup + DNS/domain analysis
Phase 2:  DISCOVERY       Utopia wiki page fetch for vertical context
Phase 3:  EVALUATION      Product adoption mapped to F1-F6 phase status
Phase 4:  ARCHITECTURE    ACT 2: 6 Critical Findings + incumbent detection
Phase 5:  GAP ANALYSIS    Utopia "should have" vs Salesforce "actually has"
Phase 6:  STRATEGY        MEDDPICC pre-fill + competitive positioning
Phase 7:  PIPELINE        ACT 3: Customer Roadmap F1-F6 with status
Phase 8:  COMMERCIAL      Deal structure aligned to F1-F6 phases
Phase 9:  EXEC PREP       ACT 1: Hook Setup + talking points
Phase 10: METADATA        Source attribution + confidence + MCP report
```

## Utopia Wiki Pages (Dynamic Vertical Intelligence)

The skill fetches vertical context from Utopia wiki pages via Wiki MCP:

| Vertical | Wiki Page ID |
|----------|-------------|
| Telco | 1431715994 |
| FinServ | 1187496098 |
| Government | 1092896800 |
| Media | 1182734455 |
| Retail | 1214482141 |
| Hospitality | 1431718498 |
| Healthcare | 1182735362 |
| Utilities | 1239967266 |
| Airlines | 1182745297 |
| Automotive | 1295366832 |
| Education | 1182730943 |

Fallback: local context files bundled with the skill.

## Quality Bar: 6 Helix Rules + 6 Technical Standards

**Helix Portal Rules:**
1. Everything comes from the 360 dossier -- nothing invented
2. No internal data shown to prospect
3. Incumbent always mentioned with public evidence
4. Gateway demo = explicit fraud intent
5. defaultLang reflects the customer
6. 6 phases always, only status changes

**Technical Standards:**
7. Salesforce-first (6-query minimum before writing)
8. MEDDPICC must have explicit gaps
9. Customer Roadmap phases are sequential (F1 always first)
10. Partner mode is a hard boundary (zero internal data)
11. 3-act structure is mandatory in every output
12. Phase 0 MCP report is mandatory in every execution

## Role: Intel (9th Role)

Pure intelligence mode without sales framing. Produces:
- Account Snapshot, Current State, Vertical Intelligence
- Competitive Landscape (neutral), Gap Analysis (neutral)
- Customer Roadmap (F1-F6 with status, no "sell" language)
- MEDDPICC Facts (observed only, no coaching)
- Risk Signals, Sources and Confidence

Does NOT produce: coaching, outreach sequences, deal strategy, negotiation playbook, email templates, pipeline forecasts. Audience-agnostic: safe to share across all roles.

## Diagram Integration (SuperSeal `Diagram` Skill)

After generating the 360 dossier, call the SuperSeal `Diagram` skill to produce architecture visuals. The 360 provides the data; Diagram renders it as SVG.

### 3 Diagrams per 360 (when role = sa, sse, or se)

| # | Diagram Type | Diagram Skill Template | Description |
|---|---|---|---|
| 1 | Architecture Map | `sase-three-column` | Current vs proposed state: left column = customer sources (identities, devices, locations), center = Cloudflare Edge with product grid mapped to F1-F6, right = customer destinations (apps, infra, networks) |
| 2 | Deal Bridge | `simple-flow` | Financial transformation: incumbent cost (left) through Cloudflare platform (center) to projected value (right), with ACV per phase F1-F6 |
| 3 | Customer Roadmap | `simple-flow` | 6-phase timeline F1 through F6: each phase as a node with status color (green=Active, orange=Proposed, blue=Explore), products listed below each node, timeline on the bottom axis |

### How to Call Diagram from 360

After completing ACT 3, generate the diagram description from the 360 data:

**Architecture Map prompt example:**
```
"SASE three-column architecture for Palace Resorts. Left: Guest devices (mobile, laptop, kiosk), Staff devices (POS, PMS terminals), 10+ properties (Cancun, Riviera Maya, Cozumel, Jamaica). Center: Cloudflare Edge with DNS, WAF, CDN, Bot Management, PageShield, API Shield, Waiting Room. Right: Booking engine (palaceresorts.com), PMS (Opera), Loyalty (palaceelite.com), Payment gateway, SaaS apps. Title: Palace Resorts - Proposed Cloudflare Architecture"
```

**Customer Roadmap prompt example:**
```
"Simple left-to-right flow showing 6 phases for Palace Resorts. F1 CORE (Proposed, green border): DNS, WAF, CDN, DDoS, SSL. F2 AppSec (Proposed, orange border): Bot Mgmt, PageShield, API Shield. F3 SASE (Explore, blue border): Access, Gateway, Email Security. F4 Dev (Explore, blue border): Workers, R2, Images. F5 Network (Explore, blue border): Magic WAN, Magic Transit. F6 AI (Explore, blue border): AI Gateway, FW for AI. Timeline bar at bottom: Mes 1, Mes 2-3, Mes 4-6, Mes 6-9, Mes 9-12, Mes 12+. Title: Palace Resorts - Customer Roadmap F1-F6"
```

### Diagram Rules
- Use data from the 360 dossier only -- never invent components not in the analysis
- Phase status colors: Active = green (#22C55E), Proposed = orange (#F6821F), Explore = blue (#1A6FD4)
- Incumbent products shown in red-dashed boxes when displacement is recommended
- All labels in the same language as the 360 output (es/en/pt)
- Product names always in English regardless of output language
- Canvas: 1400x900 default; use 1920x1080 for Architecture Map if >12 products

### When NOT to Generate Diagrams
- `role: bdr` -- BDRs don't need architecture visuals
- `role: manager, director, vp` -- leadership roles get narrative, not diagrams
- `depth: min` -- minimal output skips diagrams
- `partner_mode: true` -- diagrams may reveal internal strategy; skip unless explicitly requested

---

## Output Format Template (MANDATORY)

Every 360 output MUST follow this exact document structure. Sections may be shorter or omitted based on `role` and `depth`, but the ORDER and NAMING is non-negotiable:

```
# HELIX 360 -- [Account Name]
Dossier de Trusted Advisor | Rol: [Role] | Fecha: [Date] | Vertical: [Vertical] | Region: [Region]

## Reporte de Capacidad MCP (Fase 0)
[Table: MCP source | Status | Confidence Impact]
Overall Confidence: [X/10 with explanation]

## Snapshot de la Cuenta
[Firmographics, SFDC entities, domains, properties/brands, relationship status]

## ACTO 1: EL HOOK
### Estrategia de Demo
[Vertical selection, narrative hook]
### Escenarios de Demo WAF PII
[Table: 4 scenarios with PII type, attack pattern, CF product]
### Escenarios de Demo AI Gateway
[Table: 4 scenarios with fraud type, model defense, CF product]
### Sugerencias de Chat
[4 numbered suggestions: 2 use cases + 1 WAF + 1 Gateway]

## ACTO 2: LA PLATAFORMA (Trusted Advisor)
### 6 Hallazgos Criticos
[Numbered 1-6, each with: severity badge, description, technical impact, recommendation]
### Stack Tecnologico Observado
[Table: category, technology, evidence, incumbent]
### Incumbentes para Desplazamiento
[Table: incumbent, area, displacement strategy]

## ACTO 3: LA VISION (Customer Roadmap)
### F1: CORE -- [Active/Proposed/Explore]
[Product table with purpose and priority P0/P1/P2]
### F2: AppSec + API -- [status]
[Product table]
### F3: SASE -- [status]
[Product table]
### F4: Content + Dev -- [status]
[Product table]
### F5: Network -- [status]
[Product table]
### F6: AI -- [status]
[Product table]
### Resumen Visual del Roadmap
[ASCII table or call Diagram skill for SVG]

## MEDDPICC
[All 8 components with explicit gaps marked]

## Estructura Comercial
[Deal structure table: phase, SKUs, ACV range, timeline]

## Propuesta de POC (role: se, sse, sa only)
[Scope, timeline, success criteria]

## Talking Points y Guardrails
[What to say, what NOT to say, meeting flow]

## Metadata y Atribucion de Fuentes
[Table: section, source, confidence level]
[Gaps requiring manual investigation]

## Diagramas (role: sa, sse, se only)
[Call Diagram skill with prompts derived from ACT 3 data]
[3 diagrams: Architecture Map, Deal Bridge, Customer Roadmap]
```

---

## Methodology Reference

Implements the Helix Framework -- Trusted Advisor Methodology for Platform Conversations.
Wiki: https://wiki.cfdata.org/spaces/~janguiano/pages/1427854878/Helix+Framework+%E2%80%94+Trusted+Advisor+Methodology+for+Platform+Conversations
Piloted with 6 LATAM accounts. Validated by Palace Resorts (June 24, 2026).
Approved by Annika Garbers (Head of CF1 GTM, June 26, 2026) for regional expansion.
