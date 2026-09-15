# Jose Ruiz-Vazquez

**Building the data layer for AI governance.**

AI governance today produces documents — Model Cards, System Cards, risk assessments, control narratives — when it should produce **data**. These artifacts live in PDFs and wiki pages that no pipeline can read, no auditor can query, and no agent can consume. I'm an information professional (MLIS) treating that gap as a cataloging problem: structured schemas, stable identifiers, and crosswalks between threats (MITRE ATLAS) and controls (NIST AI RMF, ISO 42001, SR 11-7), exported in machine-readable formats (OSCAL) so governance becomes something CI/CD gates, GRC platforms, and agents can actually run on.

The work is one mechanism in four layers: a **spec layer** (the Governance Card Stack — Model, System, and Agent Cards as machine-readable governance records), an **inventory layer** (mltrack), an **evidence layer** (signed, retained artifact pipelines — including **Colophon** for agent tool-use sessions), and an **assurance layer** (**mlassure**): an agentic tool that assesses AI controls and is only allowed to assert what it actually retrieved.

## Featured

| Project | What it is |
|---------|------------|
| [**colophon**](https://github.com/joseruiz1571/colophon) | Assessment and attestation for AI agent tool use. Emits a Cosign-signed session packet — Declaration → Record → PEP Decisions → hash-chained Trace → Evidence → OSCAL Assessment Results — that a stranger can verify with only the directory and a public key. *Custody is provable. Judgment is not.* |
| [**grc-pipeline-challenge**](https://github.com/joseruiz1571/grc-pipeline-challenge) | The 6-Week GRC Pipeline Challenge (GRC Engineering Club), implemented on GCP — **third place overall**. Terraform controls, Rego policies with a fail-closed CI gate, Cosign keyless-signed evidence with a vault-backed chain of custody, an entitlement-drift gate built from a live SCC tier-drift incident, and OSCAL claims an assessor can traverse to signed bundles. Full write-up: [case study](https://github.com/joseruiz1571/grc-pipeline-challenge/blob/main/PORTFOLIO-CASE-STUDY.md). |
| [**mlassure**](https://github.com/joseruiz1571/mlassure) | Agentic AI-control assurance (v0.4.0). Deterministic evidence collectors over AWS; an LLM judgment loop that runs only where judgment is required; a citation guard that enforces the core invariant: *the agent may only assert what it actually retrieved*. Eight controls, deterministic patterns that bypass the LLM loop entirely, tamper-evident Cosign-signed evidence bundles, schema-validated OSCAL Assessment Results, Docker-packaged, with reproducibility metadata on every report. |
| [**governance-card-stack**](https://github.com/joseruiz1571/governance-card-stack) | OSCAL-compatible Agent Card schema (JSON Schema, draft 2020-12) — autonomy levels, MITRE ATLAS threat mappings, signed-evidence references. v0.1.0 ships with a validated worked example and an OPA/Conftest CI gate that fails closed. |
| [**mltrack**](https://github.com/joseruiz1571/mltrack) | CLI for AI model inventory & compliance tracking. Maps model metadata to NIST AI RMF, ISO 42001, and SR 11-7 controls. 641 tests. |
| [**cgep-capstone**](https://github.com/joseruiz1571/cgep-capstone) | CMMC L2 / NIST 800-171 compliance-as-code pipeline. Terraform + OPA/Rego + OSCAL + cosign-signed evidence vault. CI gate fails closed on non-compliant commits. |

## Supporting Projects

| Project | What it is |
|---------|------------|
| [**Drift Sentinel**](https://github.com/joseruiz1571/drift-sentinel) | Cloudflare Workers compliance scanner. Scans zone settings every 6 hours against a declared baseline, stores results in append-only D1 audit trail. Maps 6 controls to SOC 2 CC6.x and ISO 27001 A.8.x. Point-in-time queries. Free tier. |

## Contributions

| Project | What I contributed |
|---------|--------------------|
| [**claude-grc-engineering**](https://github.com/GRCEngClub/claude-grc-engineering) | GRC Engineering Club framework registry. [NIST AI RMF 1.0 framework plugin](https://github.com/GRCEngClub/claude-grc-engineering/pull/213) — merged. Open in review: [NIST AI 600-1 GenAI Profile plugin](https://github.com/GRCEngClub/claude-grc-engineering/pull/218), [SCF API canonical-host cleanup](https://github.com/GRCEngClub/claude-grc-engineering/pull/219), and [gcp-inspector v1 finding fixtures](https://github.com/GRCEngClub/claude-grc-engineering/pull/233). |

## Writing

**[Controlled Vocabulary](https://controlledvocabulary.substack.com)** — AI governance and safety through a library and information science lens. The thinking behind the code above.

Selected:

- [Forcing an LLM to Cite Its Evidence](https://controlledvocabulary.substack.com/p/forcing-an-llm-to-cite-its-evidence) — the citation-guard invariant mlassure enforces, in essay form
- [Why AI Governance Stays in Prose](https://controlledvocabulary.substack.com/p/why-ai-governance-stays-in-prose) — why the field ships documents instead of data
- [How Library Science Principles Power Community AI Literacy](https://publiclibrariesonline.org/2026/07/how-library-science-principles-power-community-ai-literacy/) — *Public Libraries*, May/June 2026

## Credentials

| Certification | Issuer |
|---------------|--------|
| Certified AI Governance Professional | BABL AI |
| ISO 42001 Lead Auditor | Mastermind |
| ISO 27701 Lead Auditor | Mastermind |
| ISO 27001 Lead Auditor | Mastermind |
| Certified GRC Engineer - Practitioner | GRC Engineering Club |
| Certified GRC Engineer - Auditor Specialty | GRC Engineering Club |
| Security+ | CompTIA |

**Selected training** — AI Security Fundamentals Level 1 | Mileva Security Labs · AIS247: AI Security Essentials for Business Leaders | SANS Institute

## Now / Next / Later

**Now**
- Building **Colophon** — signed session packets for AI agent tool use; custody you can verify offline
- Shipping **mlassure** v0.4.0 — citation-guarded assessments with Cosign chain of custody and schema-validated OSCAL Assessment Results. Details in Featured above.
- Contributing to the [GRC Engineering Club framework registry](https://github.com/GRCEngClub/claude-grc-engineering) — NIST AI RMF plugin merged; AI 600-1, SCF host cleanup, and gcp-inspector fixtures awaiting maintainer review
- Facilitating AI Security Fundamentals Level 1 at Mileva Security Labs

**Next**
- One shared `evidence` schema across the Card Stack, Colophon, and mlassure — the stack's layers joined by format, not prose
- `mltrack card export` / `card validate` — an inventory entry plus an evidence bundle becomes a validated Card
- Field-testing the autonomy vocabulary ([autonomy-levels](https://github.com/joseruiz1571/governance-card-stack/blob/main/docs/autonomy-levels.md)) against real public agent systems — and revising it in public where it fails

**Later**
- Agent provenance records — chain of custody for agentic systems, extracted as a spec from Colophon and mlassure's running implementations
- The Governance Card Stack as an adopted spec — something other teams' pipelines and auditors run on, not just mine
- Authority records for agent governance — writing the heading the field doesn't have yet

## Connect

- **Substack:** [controlledvocabulary.substack.com](https://controlledvocabulary.substack.com)
- **LinkedIn:** [linkedin.com/in/joseruiz1571](https://linkedin.com/in/joseruiz1571)
- **GRC Engineering Club:** Vice President, Austin Chapter
- **Location:** Austin, Texas
