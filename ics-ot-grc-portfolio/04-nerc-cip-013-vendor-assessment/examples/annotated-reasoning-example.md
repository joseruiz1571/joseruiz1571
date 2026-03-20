# Annotated Reasoning Example — NERC CIP-013 Vendor Assessment
## Relay Logic Partners, LLC — Firmware Update Assessment

**Document ID:** CIP013-VA-2024-002
**Vendor:** Relay Logic Partners, LLC
**Engagement:** SEL-411L firmware update (v3.4 → v3.6.2) for WJSS-003, WJSS-005, WJSS-006
**Recommendation:** Approve with Conditions

---

## Section 1: Vendor Summary

| Field | Detail |
|-------|--------|
| **Vendor** | Relay Logic Partners, LLC — San Antonio, TX |
| **Engagement** | On-site firmware update for three SEL-411L protective relays at Waco Junction Substation |
| **BES Cyber Systems affected** | WJSS-003, WJSS-005, WJSS-006 — Medium impact per CIP-002-5.1a classification |
| **Sole source?** | Yes — Relay Logic is the only SEL-certified firm with an active service agreement for this relay model at this facility |
| **Prior engagements** | Three prior firmware updates (2018, 2020, 2022); one relay settings audit (2021); no incidents reported |
| **Security certifications** | None |
| **SBOM capability** | None |
| **Assessment method** | Written questionnaire + documentation review; no on-site audit |

### Engagement Context

The SEL-411L relays at Waco Junction are running firmware v3.4 (2018). SEL's security advisory SA-2023-SEL411L identifies a vulnerability in v3.4 and earlier that permits unauthorized modification of protection settings via the relay's serial configuration port if physical access to the relay panel is achieved. The fix is firmware v3.6.2.

Lone Star does not employ SEL-certified relay engineers. Relay Logic Partners holds SEL's Certified System Integrator designation and has been Lone Star's relay maintenance contractor since 2017. There is no alternative certified firm within the Texas market with an active service agreement for this relay generation.

The consequence of not proceeding: the relays remain vulnerable to physical-access settings modification. The consequence of proceeding with inadequate vendor controls: the firmware update process itself becomes a supply chain attack vector.

---

## Section 2: Assessment Findings

### Critical Findings

| ID | Category | Description | Vendor Response | Resolution |
|----|----------|-------------|----------------|------------|
| C-01 | Contractual | Existing service agreement (Contract RLP-LST-2017-001) contains no security incident notification requirement. Relay Logic has no contractual obligation to disclose a breach to Lone Star, even if that breach affected systems used to deliver firmware. | Relay Logic acknowledged the gap. Legal contact (Robert Hanks, General Counsel) confirmed they will accept a contract addendum. | **Contract addendum executed before work order is signed.** Addendum adds: 72-hour notification obligation for any security incident affecting Lone Star systems or deliverables; audit rights with 30-day advance notice; obligation to disclose material subcontractor changes. |

> [REASONING]
> C-01 is a non-negotiable condition. Without contractual notification and audit rights, Lone Star's CIP-013 program has no mechanism to learn about vendor incidents that could affect the integrity of firmware deployed on its BES Cyber Systems. The fact that Relay Logic agreed to the addendum is a positive signal — a vendor that resists basic notification and audit rights is a red flag regardless of how technically competent they are.
>
> The auditor question here will be: "What right do you have to audit this vendor?" The answer must be in the contract. "We have a good working relationship" is not an auditable control.

### Significant Findings

| ID | Category | Description | Compensating Control | Timeline |
|----|----------|-------------|---------------------|---------|
| S-01 | SBOM / Component Transparency | Relay Logic cannot produce an SBOM for the firmware update. They confirmed that v3.6.2 includes an updated DNP3 handling library (third-party, vendor not named) and two internal modules. Version numbers of third-party components are unknown to Relay Logic's project team — they would need to request this from SEL directly. | (1) Relay Logic to provide SHA-256 hash of firmware image, signed by their lead engineer, before delivery. (2) Lone Star to verify hash upon receipt and again before deployment. (3) SEL's component inventory to be requested by Relay Logic before engagement; if unavailable, Lone Star accepts this gap with hash-based integrity verification as the substitute. | Relay Logic to request SEL component inventory within 30 days. Hash verification protocol in place before Q3 window. |
| S-02 | Subcontractor transparency | Relay Logic discloses that they use one subcontractor (Clearwater ICS Consulting, Austin TX) for overflow relay work. Clearwater's background check and security training practices are unknown to Relay Logic's management. | Named personnel requirement: Relay Logic must identify all personnel (employees and subcontractors) attending this engagement ≥2 weeks in advance. Lone Star verifies prior approval status. Clearwater personnel not previously authorized must complete Lone Star's contractor background cross-check before site access is granted. On-site escort required for all Relay Logic and Clearwater personnel. | Prior to engagement. |

> [REASONING]
> S-01 (the SBOM gap) is the most technically significant finding. The updated DNP3 library in v3.6.2 is a concern because: (a) the specific library version is unknown, and (b) the prior version of the DNP3 library (in the HMI firmware, CVE-2024-LST-0047) was found to have a parsing vulnerability. An updated library is not guaranteed to be vulnerability-free. Without knowing what the library is and what version it is, Lone Star cannot check it against known CVE databases.
>
> The honest answer is that hash verification does not substitute for SBOM. Hash verification confirms that the image was not tampered with *after* Relay Logic released it. It does not tell you what is in the image or whether those components have known vulnerabilities. This is documented as residual risk. The path to closing this gap is Relay Logic requesting the component inventory from SEL — a reasonable ask that should happen regardless of this engagement.
>
> S-02 (subcontractor gap) is common for small ICS vendors. Relay Logic's response was candid — they acknowledged they do not formally verify subcontractor security practices. The compensating control (named personnel + escort) addresses the immediate risk: no unverified person enters the substation P&C room. The underlying gap (Relay Logic's subcontractor risk management program) is addressed in ongoing monitoring.

### Notable Findings

| ID | Category | Description | Monitoring |
|----|----------|-------------|-----------|
| N-01 | Security training | Relay Logic provides annual security awareness training but could not produce training completion records for the two engineers named for this engagement. They verbally confirmed both engineers have completed the current year's training. | Lone Star to request training completion records for named engineers before each future engagement; verify at annual reassessment. |
| N-02 | Incident response | Relay Logic has an incident response plan but it was last tested via tabletop exercise in 2021 (3 years ago). No documented IR test in the past 24 months. | Note for annual reassessment. Lone Star to encourage Relay Logic to conduct annual IR exercise; verify at next assessment. |
| N-03 | ISAC membership | Relay Logic is not a member of E-ISAC or any ICS/OT security information sharing community. They rely on vendor advisories (SEL, Schneider) for vulnerability information. | Note for annual reassessment. Relay Logic informed about E-ISAC membership benefits; no condition attached. |

> [REASONING]
> The notable findings are real gaps but not engagement-blocking. N-02 (IR plan not recently tested) is worth noting because an untested IR plan is worth less than a tested one, but many small vendors have this gap. The question is whether Relay Logic's IR plan is *plausible* — does it identify what a breach looks like, who is responsible, and what the notification steps are? Based on the documentation they provided, the plan is adequate in structure even if not recently exercised.
>
> N-03 (no ISAC membership) is not a disqualifying gap. E-ISAC membership is not a CIP-013 requirement. But a vendor that is not connected to ICS-specific threat intelligence is more likely to be caught off-guard by a novel attack technique. This is a minor risk factor that is noted and tracked, not a condition of engagement.

---

## Section 3: Compensating Controls Required

| Control | Description | Deadline | Verification |
|---------|-------------|---------|-------------|
| Contract addendum (C-01) | Amend RLP-LST-2017-001 to add notification, audit rights, and subcontractor disclosure terms | Before work order issued | Priya Nair to verify executed addendum on file |
| Firmware hash verification (S-01) | Relay Logic provides SHA-256 hash signed by lead engineer; Lone Star verifies before and at deployment | Before Q3 window | Marcus Delgado documents verification in engagement log |
| SEL component inquiry (S-01) | Relay Logic to formally request component inventory for v3.6.2 from SEL; provide results to Lone Star | 30 days post-assessment | Marcus Delgado receives and reviews results; update SBOM gap status |
| Named personnel (S-02) | All personnel named ≥14 days in advance; not-previously-approved individuals complete background cross-check | 14 days before engagement | Priya Nair verifies against approved list |
| On-site escort | All Relay Logic/subcontractor personnel escorted by Lone Star employee throughout engagement | Day of engagement | Scott Akers assigns escort; logged in site access record |

---

## Section 4: Ongoing Monitoring

| Condition | Action | Frequency | Owner |
|-----------|--------|-----------|-------|
| Annual reassessment | Full questionnaire + documentation review; evaluate S-01 and S-02 remediation status | Annual | Marcus Delgado |
| Ownership change | Monitor for acquisition or foreign investment; immediate escalation if detected | Ongoing | Marcus Delgado |
| Security incident | Per contract addendum: vendor notifies within 72 hours; Lone Star evaluates and reassesses | Event-triggered | Priya Nair |
| CVE in v3.6.2 components | Monitor NVD and SEL advisories for components in deployed firmware | Monthly | Marcus Delgado |
| Clearwater ICS (subcontractor) | If Clearwater personnel are used in future engagements, reassess their security practices at next annual review | Annual | Marcus Delgado |

---

## Section 5: Residual Risk and Recommendation

| Risk Area | Residual Risk | Notes |
|-----------|--------------|-------|
| Firmware integrity | Medium | Hash verification confirms post-release integrity; SBOM gap means component vulnerabilities are unknown; SEL inquiry may partially close this gap |
| Personnel access | Low-Medium | Named personnel + escort eliminates unsupervised access; subcontractor background gap remains until cross-check is performed |
| Incident notification | Low (post-addendum) | Contractual obligation established |
| Overall | **Medium** | Meaningful gaps remain but are addressed by compensating controls or monitored; no unresolved Critical findings post-addendum |

### Recommendation: **Approve with Conditions**

The conditions are:
1. Contract addendum executed (C-01 resolved)
2. Hash verification protocol confirmed (S-01 compensating control)
3. Named personnel submitted and verified (S-02 compensating control)

All three conditions must be met and documented before the work order for the Q3 engagement is issued.

> [REASONING]
> The approval recommendation is justified despite the SBOM and subcontractor gaps because: (1) the sole-source reality means rejection does not eliminate risk — it just shifts it from vendor supply chain risk to unpatched vulnerability risk; (2) the compensating controls are substantive and specific, not generic; (3) Relay Logic has a 7-year working relationship with Lone Star with no prior incidents; and (4) the contract addendum addresses the most important gap (no notification/audit rights).
>
> The argument for rejection would require believing that the vendor supply chain risk (firmware tampering, subcontractor inside threat) is higher than the unpatched vulnerability risk (physical access settings modification). Given that the relay vulnerability requires physical access to the P&C room — which is access-controlled — and that a firmware supply chain attack would require compromising a vendor with whom Lone Star has a long working relationship, the risk calculus favors conditional approval.
>
> **What would change this recommendation to Reject:**
> - Discovery that Relay Logic has been acquired by or received investment from a foreign entity of concern
> - Discovery of a prior security incident that Relay Logic did not disclose
> - Refusal to execute the contract addendum
> - Introduction of a previously unknown subcontractor without consent or background verification
>
> **What would change this to Unconditional Approval:** SBOM capability demonstrating clean component inventory; ISO 27001 or SOC 2 certification; right-to-audit language already present in contract.

---

| Role | Signature | Date |
|------|-----------|------|
| OT Security Lead (Marcus Delgado) | _[signed]_ | 2024-07-15 |
| Compliance Analyst (Priya Nair) | _[signed]_ | 2024-07-15 |
| CISO (Jennifer Wu) | _[signed]_ | 2024-07-16 |
