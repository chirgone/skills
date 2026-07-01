# Build a Skill

**Catalog:** Cloudflare SuperSeal  
**Category:** Generic / Meta-Skill

---

## Summary

Describe what you need and walk away with a working SuperSeal skill file. This meta-skill helps users author new skill specifications by guiding them through the required sections (summary, triggers, inputs, outputs, workflow, quality bar, references), validating completeness, and producing a properly formatted `.md` file ready for inclusion in the SuperSeal catalog. Acts as a skill authoring wizard with guardrails.

## When To Use

- "I want to create a new skill for [use case]"
- "Build me a skill that [does X]"
- "How do I write a SuperSeal skill?"
- Authoring a new automation for a repeatable workflow
- Converting a manual playbook into a structured skill specification
- Extending the SuperSeal catalog for team-specific needs
- "I keep doing [task] manually — can we automate it?"

## Key Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `description` | ✅ | Natural-language description of what the skill should do |
| `category` | ❌ | Skill category: `Sales`, `Marketing`, `Engineering`, `Generic`, `Management` |
| `trigger_phrases` | ❌ | Example phrases that should invoke this skill |
| `example_inputs` | ❌ | Sample input data for the skill |
| `example_outputs` | ❌ | What the ideal output looks like |
| `existing_playbook` | ❌ | Link or text of an existing manual process to convert |
| `owner` | ❌ | Team or individual who owns the skill (default: author) |

## Key Outputs

- **Complete Skill File** (`.md`) containing all required sections:
  1. **Header** — name, catalog, category
  2. **Summary** — one-paragraph description
  3. **When To Use** — trigger phrases and use cases
  4. **Key Inputs** — input table with required/optional flags and descriptions
  5. **Workflow** — step-by-step execution logic
  6. **Key Outputs** — what the skill produces, format, and save location
  7. **Quality Bar** — 5+ quality rules with rationale
  8. **References** — data sources, docs, and dependencies
  9. **Edge Cases** — known limitations and how to handle them
  10. **Changelog** — version history starting at v1.0
- **Validation Report** — checklist confirming all required sections are complete
- Saved to: `~/skills/superseal/[NN]-[skill-slug].md`

## Quality Bar Highlights

1. **No empty sections** — every section must have substantive content; placeholder text like "TBD" is rejected
2. **Inputs must be typed** — every input needs a description, required/optional flag, and example value
3. **Quality bar must be testable** — each rule should be verifiable by a reviewer (human or automated)
4. **Trigger phrases must be natural** — include at least 3 realistic phrases a user would actually say
5. **Output format must be explicit** — specify file format, naming convention, and save location
6. **Idempotent by default** — running the skill twice with the same inputs should produce consistent results
