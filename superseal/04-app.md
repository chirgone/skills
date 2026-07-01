# App

**Catalog:** Cloudflare SuperSeal  
**Category:** Generic / Engineering

---

## Summary

Turn a natural-language description into a single-file ES module deployed as a Cloudflare Worker. Accepts a plain-English description of the desired application behavior and produces a complete, production-ready `worker.js` (or `worker.ts`) with proper error handling, type safety, environment bindings, and a `wrangler.jsonc` configuration. Ideal for rapid prototyping, internal tools, demo apps, and hackathon builds.

## When To Use

- "Build me a Worker that [does X]"
- "I need a quick API that [handles Y]"
- Rapid prototyping for customer demos
- Internal tool creation (webhook handler, data transformer, proxy, redirect engine)
- Hackathon or proof-of-concept builds
- "Turn this idea into a deployable app"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `description` | ✅ | Natural-language description of the desired app behavior |
| `language` | ❌ | `typescript` (default) or `javascript` |
| `bindings` | ❌ | Required Cloudflare bindings: `KV`, `D1`, `R2`, `AI`, `Queue`, `DO`, `Vectorize`, etc. |
| `auth` | ❌ | Authentication method: `none` (default), `api-key`, `jwt`, `cloudflare-access` |
| `routes` | ❌ | Explicit route definitions if the app is multi-endpoint |
| `deploy` | ❌ | Boolean — auto-deploy via `wrangler deploy` after generation (default: false) |
| `name` | ❌ | Worker name for deployment (auto-generated from description if omitted) |

## Key Outputs

- **Single-file ES module** (`src/index.ts` or `src/index.js`) containing:
  - Fetch handler with proper request routing
  - Error handling with structured JSON error responses
  - Type-safe environment bindings (TypeScript mode)
  - CORS headers where appropriate
  - Health check endpoint at `GET /`
- **`wrangler.jsonc`** — complete configuration with:
  - Worker name, compatibility date, and compatibility flags
  - All required binding declarations
  - Route configuration if specified
- **`README.md`** — brief description, setup instructions, and deployment command
- **Optional:** auto-deploy output with Worker URL
- Saved to: `~/helix-deck/apps/[app-slug]/`

## Quality Bar Highlights

1. **Single file, zero dependencies** — the output must be one file with no `npm install` required unless bindings demand it
2. **Production error handling** — every handler must catch errors and return structured JSON, never a raw stack trace
3. **Compatibility date must be current** — use today's date or latest stable compatibility date
4. **Type safety in TS mode** — all `Env` bindings must be typed; no `any` types allowed
5. **Test with `wrangler dev`** — generated code must pass a local `wrangler dev` smoke test without errors
