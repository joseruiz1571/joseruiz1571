# Scenario: NERC CIP-013 Supply Chain Vendor Assessment
## Relay Logic Partners, LLC — Protective Relay Firmware Update

---

## Constraints Block

| Constraint | Detail |
|------------|--------|
| **Budget** | No budget for independent third-party vendor audit; assessment must be conducted using questionnaire + documentation review |
| **Operational** | Firmware must be deployed during Q3 maintenance window (same window as WJSS-001 HMI patch); delaying beyond Q3 means the vulnerability remains unpatched for another 6-month cycle |
| **Vendor constraint** | Relay Logic Partners is the only qualified firmware maintainer for the SEL relay model at WJSS; no competitive alternative exists for this relay generation |
| **Regulatory deadline** | CIP-013 R2 requires that the supply chain risk management plan be followed for new software; this firmware update must go through the documented process before deployment |

---

## Background: The Relay Firmware Update

The protective relays at Waco Junction Substation (WJSS-003, WJSS-005, WJSS-006) are SEL-411L relays (fictional model designation) running firmware version 3.4, released in 2018. SEL (the relay manufacturer) released a security advisory in 2023 indicating that firmware versions prior to 3.6.2 contain a vulnerability allowing unauthenticated modification of protection settings via the relay's serial configuration port if an attacker has physical access to the relay panel.

SEL's firmware update process requires that the update be performed by a certified relay engineer. Lone Star does not employ SEL-certified relay engineers internally — this is common for smaller transmission operators. The company has a standing service agreement with **Relay Logic Partners, LLC** for relay maintenance, configuration, and firmware updates.

**What the firmware update contains:**
- Security fix for the unauthorized settings modification vulnerability
- Minor improvements to fault recording (non-functional for protection settings)
- Updated DNP3 handling library (note: the new DNP3 library has not been independently assessed for vulnerabilities)

**The deployment plan:** A Relay Logic engineer will travel to Waco Junction, connect to each relay via the serial configuration laptop, verify the current configuration backup, apply the firmware update, verify protection settings are intact post-update, and test trip/close functions before returning the relay to service. Estimated time: 8 hours per relay, across the 72-hour maintenance window.

---

## The Vendor: Relay Logic Partners, LLC

| Field | Detail |
|-------|--------|
| **Company type** | Private, independent ICS engineering services firm |
| **Employees** | 42 (as of last LinkedIn check) |
| **Founded** | 2011 |
| **Headquarters** | San Antonio, Texas |
| **Services** | Protective relay testing, configuration, firmware updates; SCADA integration; substation automation engineering |
| **Certifications** | NERC PRC-025 relay setting qualification; SEL Certified System Integrator designation |
| **Security certifications** | None (no SOC 2, no ISO 27001) |
| **SBOM capability** | None — company does not produce or maintain SBOMs for their service deliverables |
| **Cyber incident history** | Unknown — company has no public incident disclosures; ISAC membership status unknown |
| **Subcontractors** | Unknown — Lone Star's contract does not require disclosure of subcontractors |
| **Ownership** | Privately held; no publicly known foreign ownership or investment |

---

## The Dilemma

Lone Star faces a genuine tension between two real risks:

**Risk A: Approve Relay Logic Partners with limited documentation**
Deploying the firmware update via a vendor with no security certification, no SBOM, and no contractual audit rights means Lone Star is accepting the risk that:
- Relay Logic's internal practices are inadequate and the firmware could be tampered with before delivery
- Relay Logic's engineer could have compromised credentials or be a malicious insider
- Relay Logic may not disclose a breach that affects their systems or the firmware image
- If Relay Logic is acquired by a foreign entity after approval, Lone Star has no monitoring trigger

**Risk B: Reject Relay Logic Partners and leave the vulnerability unpatched**
The relay firmware vulnerability allows unauthorized settings modification via physical access. If a malicious actor gains physical access to the relay panels — possible for an insider, a contractor, or an attacker who bypasses physical security — they could modify protection settings in ways that cause nuisance trips or prevent legitimate fault clearing. This is a safety and reliability risk.

Neither option eliminates risk. The CIP-013 assessment process exists to make the vendor risk visible, document the decision rationale, and ensure appropriate conditions are attached to any approval.

---

## What Is Known and Unknown Going Into the Assessment

| Category | Known | Unknown |
|----------|-------|---------|
| Company background | Established 2011; 42 employees; Texas-based; active in ICS engineering | Ownership structure; subcontractor relationships; any prior security incidents |
| Technical capability | SEL-certified; track record with Lone Star (3 prior firmware updates, no incidents) | Internal development practices; how firmware images are stored and transported |
| Security posture | No SOC 2; no ISO 27001 | Patch management practices; employee security training; background check program |
| SBOM | No SBOM program | Whether the SEL firmware package contains any third-party components that Relay Logic has modified |
| Contract terms | Existing service agreement covers relay maintenance; no security-specific terms | Whether current contract language is sufficient for CIP-013 purposes; audit rights |
| Incident response | No known incidents with Lone Star | Whether Relay Logic has an IR plan; what their disclosure obligations would be if they had a breach |

---

## Stakeholders in the Approval Decision

| Role | Name | Interest |
|------|------|---------|
| OT Security Lead | Marcus Delgado | Wants adequate vendor controls; concerned about SBOM gap and lack of audit rights |
| Operations Manager | Scott Akers | Wants the firmware deployed in Q3; views relay maintenance as routine; concerned that security process is delaying necessary work |
| Compliance Analyst | Priya Nair | Needs this assessment to satisfy CIP-013 R2 documentation requirements; deadline-driven |
| CISO | Jennifer Wu | Organizational risk appetite authority; must sign off on any approval with documented gaps |
