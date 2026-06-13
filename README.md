# Jose Ruiz-Vazquez

**Building the data layer for AI governance.**

AI governance today produces documents — Model Cards, System Cards, risk assessments, control narratives — when it should produce **data**. These artifacts live in PDFs and wiki pages that no pipeline can read, no auditor can query, and no agent can consume. I'm an information professional (MLIS) treating that gap as a cataloging problem: structured schemas, stable identifiers, and crosswalks between threats (MITRE ATLAS) and controls (NIST AI RMF, ISO 42001, SR 11-7), exported in machine-readable formats (OSCAL) so governance becomes something CI/CD gates, GRC platforms, and agents can actually run on.

The work is one mechanism in four layers: a **spec layer** (the Governance Card Stack — Model, System, and Agent Cards as machine-readable governance records), an **inventory layer** (mltrack), an **evidence layer** (a signed, retained artifact pipeline), and an **assurance layer** (**mlassure**): an agentic tool that assesses AI controls and is only allowed to assert what it actually retrieved.

## Featured

| Project | What it is |
|---------|------------|
| [**mlassure**](https://github.com/joseruiz1571/mlassure) | Agentic AI-control assurance. Deterministic evidence collectors over AWS; an LLM judgment loop that runs only where judgment is required; a citation guard that enforces the core invariant: *the agent may only assert what it actually retrieved*. v0.1.0 ships one control assessed end-to-end against fixtures. OSCAL Assessment Results out. |
| [**governance-card-stack**](https://github.com/joseruiz1571/governance-card-stack) | OSCAL-compatible Agent Card schema (JSON Schema, draft 2020-12) — autonomy levels, MITRE ATLAS threat mappings, signed-evidence references. v0.1.1 ships with a validated worked example and an OPA/Conftest CI gate that fails closed. |
| [**mltrack**](https://github.com/joseruiz1571/mltrack) | CLI for AI model inventory & compliance tracking. Maps model metadata to NIST AI RMF, ISO 42001, and SR 11-7 controls. 615 tests. |
| [**cgep-capstone**](https://github.com/joseruiz1571/cgep-capstone) | CMMC L2 / NIST 800-171 compliance-as-code pipeline. Terraform + OPA/Rego + OSCAL + cosign-signed evidence vault. CI gate fails closed on non-compliant commits. |

## Writing

**[Controlled Vocabulary](https://controlledvocabulary.substack.com)** — AI governance and safety through a library and information science lens. The thinking behind the code above.

## Credentials

| Certification | Issuer |
|---------------|--------|
| Certified AI Governance Professional | BABL AI |
| ISO 42001 Lead Auditor | Mastermind |
| ISO 27701 Lead Auditor | Mastermind |
| ISO 27001 Lead Auditor | Mastermind |
| Certified GRC Engineer - Practitioner | GRC Engineering Club |
| Security+ | CompTIA |

**Selected training** — AI Security Fundamentals Level 1 | Mileva Security Labs · AIS247: AI Security Essentials for Business Leaders | SANS Institute

## Now / Next / Later

**Now**
- Building **mlassure** — agentic AI-control assurance: deterministic evidence collectors over AWS, an LLM judgment loop that runs only where judgment is genuinely required, and a citation guard enforcing the core invariant: *the agent may only assert what it actually retrieved*. First demo: one control assessed end-to-end, every claim citing its evidence. OSCAL Assessment Results out.
- Facilitating AI Security Fundamentals Level 1 at Mileva Security Labs

**Next**
- One shared `evidence` schema across the Card Stack and mlassure — the stack's layers joined by format, not prose
- `mltrack card export` / `card validate` — an inventory entry plus an evidence bundle becomes a validated Card
- Field-testing the autonomy vocabulary ([autonomy-levels](https://github.com/joseruiz1571/governance-card-stack/blob/main/docs/autonomy-levels.md)) against real public agent systems — and revising it in public where it fails

**Later**
- Agent provenance records — chain of custody for agentic systems, extracted as a spec from mlassure's running implementation
- The Governance Card Stack as an adopted spec — something other teams' pipelines and auditors run on, not just mine
- Authority records for agent governance — writing the heading the field doesn't have yet

## Connect

- **Substack:** [controlledvocabulary.substack.com](https://controlledvocabulary.substack.com)
- **LinkedIn:** [linkedin.com/in/joseruiz1571](https://linkedin.com/in/joseruiz1571)
- **Location:** Austin, Texas
