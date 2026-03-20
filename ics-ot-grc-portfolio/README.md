# ICS/OT GRC Portfolio

**Author:** Jose Ruiz | Austin, Texas
**Focus:** Industrial Control System and Operational Technology Governance, Risk, and Compliance
**Fictional Anchor Organization:** Lone Star Transmission Services, LLC

---

## What This Portfolio Demonstrates

This portfolio demonstrates **judgment in ICS/OT governance contexts** — not framework memorization.

Anyone can quote NERC CIP-002 Attachment 1 criteria. This portfolio shows what happens when you have to apply those criteria to an asset that genuinely could be classified either way, with a two-person compliance team, a 90-day audit deadline, and a budget that does not include external consultants.

Each project is structured around a constraint-laden scenario, a defensible decision, and an honest accounting of what residual risk remains after controls are in place. The annotated reasoning files are the core of this work. They are where the analytical process is made visible — the kind of reasoning a technical interviewer at ERCOT, a grid operator, or a critical infrastructure security firm would want to evaluate.

GRC work done well is the practice of defending uncomfortable truths to people who want simple answers. This portfolio tries to reflect that honestly.

---

## Why ICS/OT GRC Is Different From Enterprise GRC

| Dimension | Enterprise GRC | ICS/OT GRC |
|-----------|---------------|------------|
| **Patching cadence** | Monthly or quarterly patch cycles are standard | Patching may require 72-hour maintenance windows and void vendor support agreements |
| **Availability priority** | CIA triad — Confidentiality often leads | Inverted: Availability and Integrity precede Confidentiality — grid reliability is a public safety issue |
| **System age** | 3–7 year refresh cycles typical | 15–25 year operational lifespans common; firmware from 2009 running on substations today |
| **Vendor ecosystem** | Large vendors with security programs | Specialized OT vendors with 40 employees, no SOC 2, and a single relay model in their catalog |
| **Regulatory framework** | SOC 2, ISO 27001, HIPAA — largely voluntary or sector-specific | NERC CIP is mandatory for Bulk Electric System entities; violations carry civil penalties up to $1M/day |
| **Change management** | Agile deployment pipelines | Change requests require multi-stakeholder approval, operations manager sign-off, and often NERC notification |
| **Air gap assumption** | Network segmentation is a control | Air gaps were the foundational architecture; IT/OT convergence is dismantling them in real time |
| **Failure consequence** | Data breach, financial loss, regulatory fine | Substation failure, cascading grid events, potential physical harm to field personnel |

The mental model shift is this: in enterprise GRC, security optimizes for protection. In ICS/OT GRC, security optimizes for **reliable operation** — and any control that degrades reliability requires a higher bar of justification than in the IT world.

---

## Portfolio

| # | Project | Standards / Frameworks | Core Judgment Question |
|---|---------|----------------------|----------------------|
| [01](./01-nerc-cip-002-asset-classification/) | NERC CIP-002 BES Cyber Asset Classification | NERC CIP-002-5.1a | Where is the classification boundary, and how do you defend an ambiguous call? |
| [02](./02-ot-patch-management-risk-acceptance/) | OT Patch Management Risk Acceptance | NERC CIP-007, MITRE ATT&CK for ICS | How do you formally accept a known vulnerability when patching is operationally impossible? |
| [03](./03-iec-62443-zone-conduit-map/) | IEC 62443 Zone and Conduit Map | IEC 62443-2-1, 62443-3-3 | Where do zone boundaries belong, and what Security Level justifies a vendor remote access conduit? |
| [04](./04-nerc-cip-013-vendor-assessment/) | NERC CIP-013 Supply Chain Vendor Assessment | NERC CIP-013-2 | How do you evaluate a sole-source ICS vendor with no SOC 2 and no SBOM capability? |
| [05](./05-it-ot-convergence-governance-policy/) | IT/OT Convergence Governance Policy | NERC CIP-007, CIP-011, IEC 62443, MITRE ATT&CK for ICS | How do you govern a historian-to-cloud data path that was stood up without proper review? |

---

## Regulatory Landscape

### NERC CIP
The North American Electric Reliability Corporation Critical Infrastructure Protection standards are **mandatory** for entities that own, operate, or use assets that are part of the Bulk Electric System (BES). NERC CIP is not a voluntary framework — violations are enforceable by FERC and carry civil penalties. The standards are numbered CIP-002 through CIP-014 and cover everything from asset classification (CIP-002) to supply chain risk management (CIP-013). Regional Entities — historically organizations like Texas RE — conduct compliance audits on NERC's behalf, though oversight structures have consolidated over time.

The foundational judgment is always CIP-002: correctly classifying assets as High, Medium, or Low impact determines which of the remaining CIP standards apply. Over-scoping creates unnecessary compliance burden. Under-scoping creates audit findings and potential reliability exposure.

### IEC 62443
IEC 62443 is the international standard family for industrial automation and control system cybersecurity. Unlike NERC CIP, it is not mandatory in the US by regulation — but it is increasingly required by:
- **Vendor contracts** for capital projects
- **Procurement standards** at utilities and grid operators
- **Insurance underwriters** for OT cyber coverage
- **Federal guidance** (CISA has referenced it in critical infrastructure frameworks)

The core concept is **Security Zones and Conduits**: group assets by function and protection requirement, then explicitly manage the communication paths between zones. Assign Security Levels (SL 1–4) based on consequence of compromise, likelihood of attack, and attacker capability assumptions.

### How They Relate
NERC CIP and IEC 62443 are complementary, not redundant. CIP is prescriptive and compliance-focused — you either have a patch management program or you do not. IEC 62443 is architecture-focused — it asks how you designed the system to limit the blast radius when a control fails. A mature ICS/OT security program uses CIP for regulatory compliance and IEC 62443 for design governance.

---

## The Honest Gap Statement

This portfolio does **not** cover:

- **Physical security** (NERC CIP-006) — perimeter controls, visitor logs, physical access monitoring for Control Centers and substations
- **Incident response** — CIP-008 and the operational mechanics of coordinated IR for BES Cyber Systems
- **Recovery planning** — CIP-009 and backup/restore procedures for OT environments
- **Personnel risk management** — CIP-004 and background investigation requirements for personnel with BES Cyber System access
- **Live regulatory filing mechanics** — how to actually submit compliance evidence to a Regional Entity, navigate the CIP Self-Report process, or respond to an audit data request
- **SCADA/EMS architecture depth** — these scenarios describe systems in enough detail to frame GRC decisions, not to serve as system design documents
- **Active defense and threat hunting in OT networks** — network monitoring, protocol anomaly detection, and ICS-specific threat intelligence are in scope for security operations, not this GRC portfolio

Why these gaps exist: a 5-project portfolio can demonstrate analytical depth or breadth. This portfolio chose depth — the scenarios above are deliberately difficult, and shallow treatment of 10 additional topics would dilute the signal. A hiring manager who wants to see incident response can ask about CIP-008; this portfolio gives them something substantive to interrogate.

---

## How to Use This Portfolio

### For Learning
Start with Project 01. The asset classification exercise is foundational — if you cannot explain why a specific asset is or is not a BES Cyber Asset, the rest of CIP compliance has unstable footing. Then work through Projects 02–05 in order; each builds on the organizational context of Lone Star Transmission Services.

The annotated reasoning examples are the highest-value files in each project. Read them before the templates.

### For Job Applications
Projects 01 and 04 map most directly to CIP compliance analyst roles. Project 03 is relevant for OT security architecture positions. Projects 02 and 05 demonstrate risk management maturity beyond pure compliance — useful for GRC manager and security program lead roles.

When referencing this portfolio in interviews, be prepared to defend the decisions made in the annotated examples, not just describe what the files contain.

### For Interview Prep
Each project README contains a **"What the Auditor Will Challenge"** section — 3 to 5 specific hard questions someone reviewing this work would ask. Practice answering them out loud before the interview. The questions are not rhetorical; they have real answers that require knowing both the regulatory framework and the specific scenario context.

---

## Fictional Organization Reference

All five projects use **Lone Star Transmission Services, LLC** as the anchor organization:

- **Type:** Transmission-only utility; does not generate or distribute power
- **Location:** Texas (subject to ERCOT market and NERC reliability standards)
- **BES footprint:** Two substations — Waco Junction Substation (345 kV) and Brazos Switching Station (138 kV)
- **Compliance team:** 2 FTEs (OT Security Lead and Compliance Analyst); no dedicated GRC tool; uses shared SharePoint for documentation
- **IT/OT boundary:** Partial convergence; historian replication to enterprise network was enabled informally; no formal data diode in place
- **Regulatory standing:** No prior CIP violations; audit scheduled within current cycle

Assets, personnel names, and scenario details are consistent across all five projects. Where a decision in Project 02 references an asset first introduced in Project 01, the classification context carries over.
