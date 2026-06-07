# Jose Ruiz-Vazquez

**Building the data layer for AI governance.**

AI governance today produces documents — Model Cards, System Cards, risk assessments, control narratives — when it should produce **data**. These artifacts live in PDFs and wiki pages that no pipeline can read, no auditor can query, and no agent can consume. I'm an information professional (MLIS) treating that gap as a cataloging problem: structured schemas, stable identifiers, and crosswalks between threats (MITRE ATLAS) and controls (NIST AI RMF, ISO 42001, SR 11-7), exported in machine-readable formats (OSCAL) so governance becomes something CI/CD gates, GRC platforms, and agents can actually run on.

I call the working synthesis the **Governance Card Stack** — Model, System, and Agent Cards as a unified, machine-readable spine.

## Featured

| Project | What it is |
|---------|------------|
| [**governance-card-stack**](https://github.com/joseruiz1571/governance-card-stack) | OSCAL-compatible Agent Card schema (JSON Schema, draft 2020-12) — the *assurance* layer for agentic AI: autonomy levels, MITRE ATLAS threat mappings, signed-evidence references. v0.1 ships with a validated worked example. |
| [**mltrack**](https://github.com/joseruiz1571/mltrack) | CLI for AI model inventory & compliance tracking. Maps model metadata to NIST AI RMF, ISO 42001, and SR 11-7 controls. |
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
- Shipping the Governance Card Stack — v0.1 Agent Card schema validated; building the Conftest/OPA gate that fails CI when an agent ships without a current Card
- Facilitating AI Security Fundamentals Level 1 at Mileva Security Labs

**Next**
- Stubbing Model and System Card schemas — making the Stack visibly three-card
- Mapping the CRI Financial Services AI RMF (230 controls) to MITRE ATLAS realized threats
- Completing AWS Certified Cloud Practitioner → AI Practitioner → Solutions Architect - Associate

**Later**
- The Governance Card Stack as an adopted spec — something other teams' pipelines and auditors run on, not just mine
- Authority records for agent governance — writing the heading the field doesn't have yet

## Connect

- **Substack:** [controlledvocabulary.substack.com](https://controlledvocabulary.substack.com)
- **LinkedIn:** [linkedin.com/in/joseruiz1571](https://linkedin.com/in/joseruiz1571)
- **Location:** Austin, Texas
