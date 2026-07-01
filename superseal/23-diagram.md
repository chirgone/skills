# Diagram

**Catalog:** Cloudflare SuperSeal  
**Category:** Technical / Visual

---

## Summary

Translate a natural-language description into a self-contained SVG diagram on a 1400×900 canvas using Cloudflare diagram primitives. Supports 4 core templates: Anycast network topology, Hub-and-Spoke architecture, SASE three-column layout, and Simple Flow (left-to-right or top-to-bottom). Uses the Cloudflare visual palette: Blue #1A6FD4, Orange #F6821F, White #FFFFFF, with Dark Gray #36393B for text and Light Gray #F4F4F4 for backgrounds. Produces clean, presentation-ready SVGs that can be embedded in decks, docs, or wiki pages. No external dependencies — every SVG is fully self-contained with inline styles.

## When To Use

- "Draw me a diagram of [architecture]"
- "Show how traffic flows from users to origin through Cloudflare"
- "Create a SASE architecture diagram for [account]"
- "I need a visual for my deck showing [topology]"
- When explaining a technical concept and words aren't enough
- When a customer deck needs an architecture slide
- When documenting a POC architecture or proposed deployment
- When a wiki page needs a visual reference
- "Make a flow diagram showing [process]"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `description` | ✅ | Natural-language description of what to diagram — be specific about components, connections, and flow direction |
| `template` | ❌ | `anycast`, `hub-and-spoke`, `sase-three-column`, `simple-flow` — auto-detected from description if omitted |
| `title` | ❌ | Diagram title displayed at the top of the canvas |
| `components` | ❌ | Explicit list of components to include (overrides auto-detection from description) |
| `canvas_size` | ❌ | `standard` (1400×900, default), `wide` (1920×1080), `compact` (1000×600) |
| `style` | ❌ | `clean` (default — minimal lines, lots of whitespace) or `detailed` (more labels, annotations) |

## Key Outputs

- **SVG Diagram** (self-contained SVG file) with:
  1. **Canvas** — 1400×900 default with Cloudflare-branded color palette
  2. **Components** — boxes, circles, icons, and labels representing infrastructure elements
  3. **Connections** — lines, arrows, and flow indicators with optional labels
  4. **Legend** — component key if more than 5 distinct element types
  5. **Title Block** — diagram title and optional subtitle
- **Template-Specific Layouts:**
  - Anycast — global edge nodes radiating from central Cloudflare network
  - Hub-and-Spoke — central hub with spoke connections to satellite nodes
  - SASE Three-Column — Users | Cloudflare Edge | Applications in three distinct columns
  - Simple Flow — linear left-to-right or top-to-bottom process flow
- Saved to: `~/helix-deck/diagrams/[slug]-diagram-[date].svg`

## Quality Bar Highlights

1. **Self-contained SVGs only** — no external CSS, no linked fonts, no image references; every SVG must render identically in any viewer
2. **Cloudflare palette is mandatory** — Blue #1A6FD4 for primary elements, Orange #F6821F for highlights and call-outs, White #FFFFFF backgrounds, Dark Gray #36393B for text
3. **Whitespace is a feature** — clean diagrams communicate better than cluttered ones; if it feels crowded, remove elements or increase canvas size
4. **Labels must be readable at 100% zoom** — minimum 14px font size for labels, 18px for titles; tiny text defeats the purpose of a diagram
5. **Flow direction must be obvious** — use arrowheads, numbered steps, or color gradients to make the flow unmistakable; if a viewer has to guess the direction, the diagram fails
6. **Use `font-family="Inter"` inline on every `<text>` element** — CSS font inheritance doesn't work in all SVG renderers; always set it inline
