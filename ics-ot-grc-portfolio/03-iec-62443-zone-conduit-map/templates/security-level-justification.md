# Security Level Justification Template
## IEC 62443-3-2 — Zone/Conduit SL Assignment Reasoning

**Organization:** Lone Star Transmission Services, LLC
**Asset/Zone/Conduit:** _(ID and name)_
**Analyst:** _(Name)_
**Date:** _______________

---

> **How to use this template:** Complete one instance of this form for each zone or conduit where the Security Level assignment requires justification beyond a simple table entry. This is especially important for: (1) any SL-3 or higher assignment, (2) any assignment that differs from the zone it connects to, and (3) any assignment where a lower SL was chosen despite higher-consequence assets being present.

---

## 1. Asset/Zone/Conduit Description

| Field | Detail |
|-------|--------|
| **Type** | Zone / Conduit (circle one) |
| **Zone or Conduit ID** | _(e.g., Z-03 or C-02)_ |
| **Name** | _(e.g., Control Zone or Vendor Remote Access)_ |
| **Assets Included / Connected** | _(list assets in this zone, or the source/destination zones for a conduit)_ |
| **Primary Function** | _(one sentence: what does this zone/conduit do operationally?)_ |

---

## 2. Consequence of Compromise

> Assess what happens if this zone or conduit is compromised by a cyber attack. Use the four consequence categories defined in IEC 62443-3-2.

| Consequence Category | Assessment | Rationale |
|---------------------|-----------|----------|
| **Safety** | High / Medium / Low / Negligible | _(Could compromise result in physical harm to personnel or public? e.g., "Unauthorized SAC operation could result in energized equipment being worked on")_ |
| **Operational** | High / Medium / Low / Negligible | _(Could compromise disrupt grid operations or reliability? e.g., "HMI compromise eliminates operator visibility at 345 kV substation")_ |
| **Financial** | High / Medium / Low / Negligible | _(Direct cost of compromise: emergency restoration, equipment damage, regulatory fines)_ |
| **Reputational** | High / Medium / Low / Negligible | _(Impact on regulatory standing, customer confidence, NERC relationship)_ |
| **Overall Consequence** | **High / Medium / Low** | _(Summary judgment — use highest category unless a strong argument exists for weighting otherwise)_ |

---

## 3. Likelihood of Targeted Attack

> Assess how likely it is that a threat actor would specifically target this zone or conduit, and what capability level they would need. This is not the likelihood of *any* attack — it is the likelihood of an attack that specifically attempts to exploit this zone/conduit's vulnerabilities.

| Factor | Assessment | Rationale |
|--------|-----------|----------|
| **Target attractiveness** | High / Medium / Low | _(Is this zone a high-value target for known threat actors? Transmission SCADA is documented as a target; an NTP server is not.)_ |
| **Required attacker access** | Network-adjacent / Remote / Physical | _(What access does the attacker need? A conduit requiring physical access has lower exploitation likelihood than one accessible from a remote network.)_ |
| **Documented threat actor interest** | Yes / No / Unknown | _(Has CISA, FBI, or ISAC issued advisories specifically referencing this type of asset as a target?)_ |
| **Overall Likelihood** | **High / Medium / Low** | _(Summary judgment)_ |

---

## 4. Attacker Capability Assumed

> IEC 62443 Security Levels correspond to assumed attacker capability levels. Select the assumed attacker for this zone/conduit's SL assignment.

| SL | Attacker Profile |
|----|----------------|
| SL-1 | Incidental or unintentional; no specific ICS knowledge; casual IT attacker |
| SL-2 | Intentional; uses standard means; some ICS protocol knowledge; commercially available tools |
| SL-3 | Intentional; uses sophisticated means; ICS-specific tooling; knowledge of target environment |
| SL-4 | State-level adversary; nation-state resources; advanced persistent threat with long-term access |

**Assumed attacker capability for this assignment:** SL-___ (_____)

**Rationale:** _(Why this capability level? Reference specific threat actor profiles or CISA advisories if applicable. Be specific about what "sophisticated means" or "standard means" means for this specific zone/conduit.)_

---

## 5. Security Level Selection

| Option Evaluated | Consequence | Likelihood | Attacker Capability | Would This SL Apply? |
|-----------------|-------------|-----------|--------------------|--------------------|
| SL-1 | — | — | Incidental | _(Yes/No — and why)_ |
| SL-2 | — | — | Standard tools | _(Yes/No — and why)_ |
| SL-3 | — | — | Sophisticated/ICS-specific | _(Yes/No — and why)_ |
| SL-4 | — | — | Nation-state | _(Yes/No — rationale for why this is/is not appropriate)_ |

**Selected Security Level:** SL-___

**Selection Rationale:** _(Write 2–4 sentences. Explain why the selected SL is appropriate given the consequence, likelihood, and attacker capability assessments above. If you chose a lower SL than consequence alone might suggest, explain the countervailing factors. If you chose a higher SL than the connecting zones require, explain why.)_

---

## 6. Gap Analysis: Current Controls vs. SL Requirements

> IEC 62443-3-3 defines Foundational Requirements (FR) that must be met at each Security Level. The seven foundational requirement categories are: Identification and Authentication (IAC), Use Control (UC), System Integrity (SI), Data Confidentiality (DC), Restricted Data Flow (RDF), Timely Response to Events (TRE), and Resource Availability (RA).
>
> For the selected SL, list the key requirements and whether current controls meet them.

| FR Category | SL Requirement (abbreviated) | Current Control | Gap? |
|-------------|------------------------------|----------------|------|
| IAC — Identification & Authentication | _(e.g., SL-2 requires multi-factor authentication for all human users)_ | _(e.g., MFA implemented for remote access; local accounts use password only)_ | _(Yes/No — and gap description)_ |
| UC — Use Control | _(e.g., SL-2 requires least-privilege role-based access control)_ | _(current state)_ | _(gap)_ |
| SI — System Integrity | _(e.g., SL-2 requires software integrity verification)_ | _(current state)_ | _(gap)_ |
| DC — Data Confidentiality | _(e.g., SL-2 requires encryption for data in transit across zone boundaries)_ | _(current state)_ | _(gap)_ |
| RDF — Restricted Data Flow | _(e.g., SL-2 requires network segmentation and access control at zone boundaries)_ | _(current state)_ | _(gap)_ |
| TRE — Timely Response | _(e.g., SL-2 requires audit logging and security event monitoring)_ | _(current state)_ | _(gap)_ |
| RA — Resource Availability | _(e.g., SL-2 requires DoS protection for critical functions)_ | _(current state)_ | _(gap)_ |

**Overall gap assessment:** _(Are gaps minor (addressed by compensating controls) or material (require architectural changes)?_

---

## 7. Compensating Controls for Identified Gaps

> For each gap identified in Section 6 that cannot be immediately remediated, document the compensating control that reduces the residual risk.

| Gap | Compensating Control | Effectiveness | Remediation Plan |
|-----|---------------------|--------------|-----------------|
| _(e.g., No MFA for local accounts on HMI)_ | _(e.g., Physical access control limits who can reach local console; session monitoring on Dragos platform)_ | _(Partial — physical controls compensate for lack of logical MFA)_ | _(Implement Windows Hello or smartcard auth in next major maintenance window)_ |
| _(add rows as needed)_ | | | |

---

## 8. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | | |
| Substation Engineering Lead | Diana Flores | | |
