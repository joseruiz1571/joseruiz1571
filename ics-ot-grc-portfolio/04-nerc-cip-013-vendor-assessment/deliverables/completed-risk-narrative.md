# Vendor Assessment Risk Narrative — COMPLETED
## NERC CIP-013 Supply Chain Risk Management
### Lone Star Transmission Services, LLC

**Vendor:** Relay Logic Partners, LLC
**Engagement:** Protective relay firmware update — WJSS-003, WJSS-005, WJSS-006 (SEL-411L relays, firmware v3.4 → v3.6.2)
**Assessment date:** February 12, 2026
**Prepared by:** Priya Nair, Compliance Analyst; Marcus Delgado, OT Security Lead
**Document ID:** CIP013-VA-2026-001

---

## Section 1: Vendor Summary and Engagement Context

| Field | Detail |
|-------|--------|
| **Vendor name** | Relay Logic Partners, LLC |
| **Engagement type** | On-site firmware update — protective relay firmware deployment |
| **BES Cyber System components affected** | WJSS-003, WJSS-005, WJSS-006 — SEL-411L protective relays, 345 kV lines 1-3 at Waco Junction Substation. All three are Medium impact BES Cyber Assets under CIP-002-5.1a §2.6. |
| **Engagement date(s)** | Scheduled Q3 2026 maintenance window (72-hour window) |
| **Sole source?** | Yes — Relay Logic Partners is the only vendor with SEL Certified System Integrator designation for this relay model that Lone Star has an active agreement with. SEL's certification program limits the field of qualified vendors; no alternative is available within Lone Star's current vendor roster for this relay generation. |
| **Prior engagements** | Three prior firmware updates on the same relay models at WJSS (2019, 2021, 2023). No incidents, no protection setting discrepancies on post-update testing in any prior engagement. |
| **Security certifications held** | None (no SOC 2, no ISO 27001, no IEC 62443 certification) |
| **SBOM capability** | No |
| **Assessment method** | Vendor questionnaire (completed February 12, 2026) + documentation review (incident report, IR plan summary, background check confirmation) + assessment call with Relay Logic CEO and Operations Lead |

### Engagement Description

Relay Logic Partners is being engaged to deploy firmware version 3.6.2 to three SEL-411L protective relays at Waco Junction Substation. The firmware update addresses a vulnerability identified in SEL Security Advisory 2023-002: unauthorized modification of relay protection settings via the serial configuration port when an attacker has physical access to the relay panel. The update also includes a minor enhancement to fault recording and an updated DNP3 handling library.

This engagement requires a CIP-013 assessment because it involves the delivery and application of new software to Medium impact BES Cyber Assets. Under Lone Star's CIP-013 supply chain risk management plan (Section 4.2: Software and Patch Deployments), any new firmware applied to Medium or High impact BES Cyber Systems must be preceded by a documented vendor assessment using this questionnaire.

The consequences of a compromised firmware deployment are substantial: a malicious firmware image could silently modify protection settings, disable trip functions, or create a persistent backdoor on a relay that protects 345 kV transmission lines. The risks are not hypothetical — CISA ICS-CERT has documented supply chain attacks targeting protective relay firmware in the broader electric sector.

### What Drove This Assessment

The SEL firmware update was triggered by the 2023 SEL security advisory. It was delayed from a 2024 deployment window due to the Q3 2025 maintenance window being consumed by the WJSS-001 HMI patching (RA-WJSS-2024-001). This is the first Relay Logic engagement since Lone Star formalized its CIP-013 vendor assessment program in 2024. Prior engagements were managed under the predecessor vendor assessment process. This is therefore Relay Logic's first assessment under the current program.

---

## Section 2: Assessment Findings

### Critical Findings

| Finding ID | Category | Description | Vendor Response | Required Resolution |
|------------|----------|-------------|----------------|---------------------|
| C-01 | Contractual | The existing service agreement between Lone Star and Relay Logic Partners contains no provision for security incident notification. If Relay Logic experienced a breach affecting their development environment, firmware custody, or delivery chain, they have no contractual obligation to notify Lone Star. This is a direct CIP-013 requirement gap. | Vendor acknowledged the gap during assessment call. CEO (Ryan Harlow) stated that their internal practice is to notify affected customers within 72 hours of incident confirmation, but acknowledged this is not contractually committed. Expressed willingness to add contract language. | Contract amendment required before engagement proceeds. Amendment must include: (1) mandatory notification to Lone Star within 72 hours of any security incident that may have affected Relay Logic's ability to deliver secure firmware or services; (2) audit rights for Lone Star or designated third party with 30-day advance notice for on-site, 14-day for documentation review; (3) notification requirement for any ownership change or change in key personnel with access to Lone Star's site or firmware delivery chain. Contract amendment in process as of assessment date; work order for Q3 2026 engagement cannot be signed until amendment is executed. |

### Significant Findings

| Finding ID | Category | Description | Compensating Control | Remediation Timeline |
|------------|----------|-------------|---------------------|---------------------|
| S-01 | Vulnerability Notification | Vendor has no formal SLA for notifying customers of security vulnerabilities in firmware or services delivered. Vendor stated a practice of notifying customers within the past 12 months of engagement within approximately 2 business days of receiving an advisory, but this is not contractually binding and does not cover relays deployed in prior engagement cycles. | Contract amendment (addressing C-01) will include a specific term requiring Relay Logic to notify Lone Star within 2 business days of receiving any SEL advisory or CISA ICS-CERT advisory affecting relay firmware deployed at Lone Star sites. This converts the stated practice into a contractual obligation. | Resolved by contract amendment (concurrent with C-01). |
| S-02 | SBOM | Vendor cannot provide an SBOM for the firmware to be deployed. SEL does not publish an SBOM for SEL-411L firmware v3.6.2. The firmware includes an updated DNP3 handling library whose name, version, and vulnerability history are unknown. This is particularly relevant because CVE-2024-LST-0047 (affecting WJSS-001 HMI) is also a DNP3 library vulnerability — the same vulnerability class exists in the firmware being deployed to the relays. | (1) Lone Star will monitor CISA ICS-CERT for any CVE disclosures against SEL-411L v3.6.2 post-deployment; (2) Lone Star will independently verify the SHA-256 hash of the firmware image against SEL's published checksum before deployment; (3) SEL itself will be added to Lone Star's CIP-013 vendor assessment list for the next annual review — the manufacturer is the appropriate entity to respond to SBOM requests for OEM firmware. | SBOM gap: persistent until SEL implements SBOM program (industry-wide issue). Monitoring: ongoing. SEL assessment: initiate Q4 2026. |

### Notable Findings

| Finding ID | Category | Description | Monitoring Action |
|------------|----------|-------------|------------------|
| N-01 | Security Certifications | Vendor holds no cybersecurity certifications. No SOC 2, no ISO 27001. NIST CSF self-assessment planned for 2026. | Request NIST CSF self-assessment results when complete (Q4 2026). Add as a condition of next contract renewal. |
| N-02 | Incident History | Vendor disclosed a 2023 phishing-related credential compromise. Disclosed proactively. Incident was contained; no customer data affected; MFA mandated post-incident. | Review Relay Logic's incident response plan for any updates since 2023. Confirm MFA is implemented across all accounts. |
| N-03 | ISAC Membership | Vendor does not have formal E-ISAC membership and does not receive real-time threat intelligence. | Add contract term: vendor will notify Lone Star within 2 business days of receiving any CISA advisory affecting SEL relays deployed at Lone Star (covered by S-01 contract amendment). Lone Star retains E-ISAC membership to receive sector-specific intelligence directly. |
| N-04 | IR Testing | No third-party tabletop or red team exercise in past 24 months. Internal walk-throughs conducted semi-annually. | Add to next contract renewal conditions: third-party tabletop exercise annually or every 24 months. |

---

## Section 3: Compensating Controls Required for Approval

| Control | Description | Implementation Deadline | Verification Method | Owner |
|---------|-------------|------------------------|--------------------|----|
| Contract amendment — notification and audit rights | Amend existing Relay Logic service agreement to add: (1) 72-hour security incident notification; (2) 2-business-day advisory notification; (3) audit rights with 30-day/14-day advance notice; (4) ownership change notification. | Before work order signature for Q3 2026 engagement | Legal review of executed amendment; Priya Nair confirms amendment is on file before work order approval | Priya Nair / Legal |
| Firmware hash verification | Prior to deployment: Relay Logic provides SHA-256 hash of firmware image signed by the engagement lead (Ryan Harlow); Lone Star independently verifies against SEL's publicly posted checksum for v3.6.2; any discrepancy is an automatic stop-work condition with escalation to Marcus Delgado and CISO. | Minimum 5 business days before deployment date | Marcus Delgado verifies hash against SEL published checksum; documents hash comparison in pre-deployment checklist | Marcus Delgado |
| Named personnel requirement | Relay Logic must provide full names and identification of all personnel attending the engagement at least 14 calendar days before scheduled start. Lone Star cross-references against the approved personnel list (Ryan Harlow, Demetrius Okoye confirmed). Any change to named personnel requires OT Security Lead approval and a new background check cross-reference. | 14 days before engagement | Priya Nair verifies names against approved list; documents in engagement authorization record | Priya Nair |
| On-site Lone Star escort | All Relay Logic personnel must be escorted by a Lone Star OT Security or Operations employee for the full duration of the engagement, including transit within the substation. No unsupervised access to P&C room or relay panels. | Day of engagement start | Scott Akers assigns Lone Star escort; escort documents attendance throughout engagement in site access log | Scott Akers |
| Post-update protection setting verification | Before any relay is returned to service after firmware deployment: Relay Logic and Lone Star OT engineer jointly verify that all protection settings match the pre-update configuration backup taken by Relay Logic at the start of the engagement. Any discrepancy is a stop-work condition. Trip/close function test required before relay is returned to service. | At completion of each relay update within the maintenance window | Diana Flores (Substation Engineering Lead) signs protection setting verification form for each relay; forms retained in OT Security documentation | Diana Flores |

---

## Section 4: Conditions for Ongoing Monitoring

| Condition | Monitoring Action | Frequency | Owner |
|-----------|-----------------|-----------|-------|
| Annual reassessment | Reassess Relay Logic via updated questionnaire and documentation review; evaluate whether N-01 (certifications) and N-04 (IR testing) gaps have been remediated; confirm named personnel list is current | Annual (before each scheduled engagement) | Marcus Delgado |
| Ownership change | Monitor for acquisition, merger, or investment by entities of concern; Relay Logic is privately held by US founders — any ownership change triggers immediate reassessment; ISAC news monitoring for vendor company names | Ongoing | Marcus Delgado |
| Security incident notification | Per amended contract, Relay Logic must notify within 72 hours; Lone Star evaluates impact on any pending or recent firmware deployments and reassesses as needed | Event-triggered | Priya Nair |
| CVE monitoring for SEL-411L v3.6.2 | Monitor CISA ICS-CERT advisories for any CVE disclosure affecting SEL-411L v3.6.2 components post-deployment; if new CVE disclosed, initiate patch prioritization review with Diana Flores | Monthly (during standard vulnerability scanning cycle) | Marcus Delgado |
| SBOM program development | Monitor SEL's SBOM program development; request SBOM for future firmware versions once SEL has established a program; raise at next SEL vendor review | Annual (at next SEL assessment) | Priya Nair |
| Contract renewal | Full re-assessment at next contract renewal | Per contract schedule | Priya Nair |

---

## Section 5: Residual Risk and Approval Recommendation

### Residual Risk Assessment

| Risk Area | Inherent Risk | Compensating Controls Applied | Residual Risk |
|-----------|--------------|-------------------------------|--------------|
| Firmware integrity | High — relay firmware modification is a documented ICS attack vector; no SBOM means component vulnerability status is unknown | SHA-256 hash verification against SEL-published checksum; dedicated chain-of-custody USB; independent verification before deployment | Medium — hash verification confirms image integrity against SEL's published release; does not address the risk of a compromise within SEL's own supply chain, but that risk is inherent to all OEM firmware deployments and is not uniquely elevated by Relay Logic's practices |
| Personnel access | Medium — on-site access to 345 kV relay panels; background checks confirmed for named personnel | Named personnel requirement; on-site escort; background check confirmation for Ryan Harlow and Demetrius Okoye | Low-Medium — escort eliminates unsupervised access risk; named personnel creates accountability; residual risk is a motivated insider or compromised engineer (low probability for a vetted, repeat-engagement vendor) |
| Incident notification | High (inherent) — no contractual obligation in existing agreement | Contract amendment (C-01 resolution) adds mandatory notification commitment | Low — contractual obligation established; vendor has demonstrated willingness to cooperate and has incident response capability confirmed by prior incident handling |
| SBOM / unknown firmware components | High — DNP3 library update in v3.6.2 has unknown vulnerability status | Post-deployment CISA monitoring; SEL assessment planned | Medium-Low — monitoring compensates for inability to assess library-specific risk pre-deployment; risk is industry-wide for OEM firmware |
| Sole-source dependency | Medium — no alternative vendor for this relay model; sole-source creates leverage concentration | Annual reassessment condition; contract terms protect Lone Star's interests | Medium — sole-source status is an inherent business risk; compensating controls limit the damage of vendor failure but cannot eliminate the dependency |

**Overall residual risk: Medium**

This assessment reflects that Relay Logic Partners is a known vendor with a documented track record at Lone Star, transparent about the 2023 incident, willing to accept contractual conditions, and without any foreign ownership concerns. The significant findings (SBOM gap, notification SLA) are being addressed by contract amendment. The remaining residual risk is inherent to the OT vendor ecosystem — small ICS integrators without security certifications are the industry norm, not the exception — and is manageable through ongoing monitoring and the compensating controls defined above.

### Recommendation

☑ **Approve with Conditions** — Material gaps exist but have been mitigated by compensating controls documented in Section 3. Approval is contingent on all conditions being met before engagement proceeds. Conditions must be verified by OT Security Lead before work order is issued.

**Recommendation detail:** Relay Logic Partners is approved for the Q3 2026 firmware deployment engagement, subject to: (1) execution of the contract amendment adding notification and audit rights; (2) receipt and independent verification of firmware SHA-256 hash at least 5 business days before deployment; (3) confirmation of named personnel (Ryan Harlow, Demetrius Okoye) against approved list at least 14 days before engagement. The SBOM gap and notification SLA gap are both addressed by the contract amendment and post-deployment monitoring program — they are not individually disqualifying for a sole-source integrator in the current OT vendor ecosystem.

### What Would Change This Recommendation

**Upgrade (improve to Approve):** Relay Logic achieving SOC 2 Type II certification or NIST CSF maturity level 3 at next annual assessment; SEL providing an SBOM for v3.6.2 firmware enabling pre-deployment component vulnerability assessment.

**Downgrade (reduce to Defer or Reject):** Failure to execute contract amendment before engagement; withdrawal of consent to named personnel requirement or on-site escort; any indication of ownership change or foreign investment not disclosed in this assessment; any CISA advisory indicating active exploitation of SEL-411L firmware prior to the Q3 engagement that would require emergency reassessment.

---

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | *[signed]* | February 19, 2026 |
| Compliance Analyst | Priya Nair | *[signed]* | February 19, 2026 |
| CISO | Jennifer Wu | *[signed]* | February 21, 2026 |

**CIP-013 R2 Reference:** CIP013-VA-2026-001 — this document is filed as the CIP-013 R2 vendor assessment record for the Relay Logic Partners Q3 2026 firmware deployment engagement. It is cross-referenced in the CIP-013 supply chain risk management plan audit evidence package.
