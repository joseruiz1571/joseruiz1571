# Vendor Assessment Risk Narrative
## NERC CIP-013 Supply Chain Risk Management
### Lone Star Transmission Services, LLC

**Vendor:** _______________
**Engagement:** _______________
**Assessment date:** _______________
**Prepared by:** _______________
**Document ID:** _(e.g., CIP013-VA-2024-001)_

---

## Section 1: Vendor Summary and Engagement Context

| Field | Detail |
|-------|--------|
| **Vendor name** | |
| **Engagement type** | _(Firmware update / Software delivery / Remote access services / On-site services)_ |
| **BES Cyber System components affected** | _(Asset IDs and names; CIP-002 impact level)_ |
| **Engagement date(s)** | |
| **Sole source?** | Yes / No — _(if yes, explain why no alternative exists)_ |
| **Prior engagements** | _(History of prior work; any prior incidents or concerns)_ |
| **Security certifications held** | _(SOC 2, ISO 27001, IEC 62443, other — or "None")_ |
| **SBOM capability** | Yes / Partial / No |
| **Assessment method** | _(Questionnaire only / Questionnaire + documentation review / On-site audit)_ |

### Engagement Description

_(2–3 paragraphs. Describe what the vendor is being asked to do, why this engagement requires a CIP-013 assessment, what systems will be accessed or modified, and what the consequences would be if the vendor delivered compromised or defective work.)_

### What Drove This Assessment

_(Describe the trigger: new vendor, new software delivery, scope change from prior engagement, annual reassessment, etc. Reference the relevant CIP-013 R1 plan section.)_

---

## Section 2: Assessment Findings

> **Finding Tiers:**
> - **Critical:** Requires immediate escalation; engagement cannot proceed without resolution
> - **Significant:** Engagement can proceed only with documented compensating controls and time-bound remediation commitment
> - **Notable:** Documented and tracked; does not block approval; addressed at next contract renewal or reassessment

### Critical Findings

| Finding ID | Category | Description | Vendor Response | Required Resolution |
|------------|----------|-------------|----------------|---------------------|
| _(e.g., C-01)_ | _(e.g., Contractual)_ | _(e.g., Existing contract contains no security incident notification requirement; vendor has no obligation to disclose a breach to Lone Star)_ | _(What the vendor said when this was raised)_ | _(e.g., Contract must be amended to include 72-hour notification and audit rights before engagement proceeds)_ |

### Significant Findings

| Finding ID | Category | Description | Compensating Control | Remediation Timeline |
|------------|----------|-------------|---------------------|---------------------|
| _(e.g., S-01)_ | _(e.g., SBOM)_ | _(e.g., Vendor cannot produce an SBOM or component inventory for the firmware image; third-party library versions are unknown)_ | _(e.g., Lone Star will perform independent hash verification of firmware image; deployment will be preceded by a test relay bench deployment reviewed by Lone Star engineering)_ | _(e.g., Vendor to implement SBOM program within 12 months; verified at next annual reassessment)_ |
| _(S-02)_ | | | | |

### Notable Findings

| Finding ID | Category | Description | Monitoring Action |
|------------|----------|-------------|------------------|
| _(e.g., N-01)_ | _(e.g., Security training)_ | _(e.g., Vendor confirms annual security awareness training but cannot provide training completion records for the specific engineers assigned to this engagement)_ | _(e.g., Lone Star to request training completion records for named engineers before each future engagement; tracked in vendor management log)_ |

---

## Section 3: Compensating Controls Required for Approval

> **Instructions:** This section is only completed for "Approve with Conditions" recommendations. List every compensating control that is required before the engagement proceeds. These are non-negotiable — they must be implemented and verified, not just planned.

| Control | Description | Implementation Deadline | Verification Method | Owner |
|---------|-------------|------------------------|--------------------|----|
| Contract amendment | Add security incident notification (72 hours) and audit rights clause to existing service agreement | Before work order is signed | Legal review of amended contract | Priya Nair / Legal |
| Firmware hash verification | Vendor must provide SHA-256 hash of firmware image, signed by a named Relay Logic engineer, before delivery; Lone Star will verify hash upon receipt and again before deployment | Before Q3 maintenance window | Marcus Delgado to perform hash verification and document result | Marcus Delgado |
| Named personnel requirement | Relay Logic must provide names of all engineers attending the engagement ≥2 weeks in advance; Lone Star performs background check cross-reference against prior authorized personnel list | 14 days before engagement | Priya Nair to verify names against prior approved list | Priya Nair |
| On-site escort | All Relay Logic personnel must be escorted by a Lone Star employee (OT Security or Operations) for the duration of the engagement; no unsupervised access to P&C room or relay panels | Day of engagement | Scott Akers to assign escort; documented in site access log | Scott Akers |
| _(Add additional controls as needed)_ | | | | |

---

## Section 4: Conditions for Ongoing Monitoring

> **Instructions:** Approval is point-in-time. This section defines what Lone Star does between assessments to maintain awareness of vendor risk posture.

| Condition | Monitoring Action | Frequency | Owner |
|-----------|-----------------|-----------|-------|
| Annual reassessment | Reassess vendor via questionnaire + documentation review; evaluate whether gaps from this assessment have been remediated | Annual | Marcus Delgado |
| Ownership change | Monitor vendor for acquisition, merger, or investment by entities of concern; trigger immediate reassessment if change is detected | Ongoing (monitor via news, ISAC alerts) | Marcus Delgado |
| Security incident | Vendor must notify Lone Star within 72 hours per amended contract; Lone Star evaluates impact and re-assesses vendor as needed | Event-triggered | Priya Nair |
| CVE in delivered components | Monitor for CVEs affecting firmware components; if a CVE is identified in deployed firmware, trigger patch prioritization review | Monthly (during vulnerability scanning cycle) | Marcus Delgado |
| Contract renewal | Full assessment re-performed at each contract renewal | Per contract schedule | Priya Nair |

---

## Section 5: Residual Risk and Approval Recommendation

### Residual Risk Assessment

| Risk Area | Inherent Risk | Compensating Controls Applied | Residual Risk |
|-----------|--------------|-------------------------------|--------------|
| Firmware integrity | High — no SBOM; no vendor-side integrity verification at delivery | Hash verification by Lone Star; chain of custody documentation | Medium — hash verification confirms image integrity but does not substitute for SBOM (unknown third-party components) |
| Personnel access | Medium — background checks not verified for all subcontractors | Named personnel requirement; on-site escort | Low-Medium — escort eliminates unsupervised access risk; background gap for first-time named engineers remains |
| Incident notification | High — no contractual obligation in existing agreement | Contract amendment required before approval | Low after amendment — contractual obligation established |
| Supply chain (Relay Logic as conduit) | Medium — small vendor with unknown internal security practices | Annual reassessment; ownership monitoring | Medium — inherent uncertainty cannot be fully resolved without right to audit |

**Overall residual risk:** _(High / Medium-High / Medium / Low-Medium / Low)_

### Recommendation

☐ **Approve** — No material gaps; vendor meets Lone Star's supply chain risk threshold.

☐ **Approve with Conditions** — Material gaps exist but have been mitigated by compensating controls documented in Section 3. Approval is contingent on all conditions being met before engagement proceeds. Conditions must be verified by OT Security Lead before work order is issued.

☐ **Defer Pending Remediation** — Critical gaps exist that cannot be compensated by controls. Engagement is deferred until vendor demonstrates remediation. Re-assessment required before proceeding.

☐ **Reject** — Critical gaps cannot be remediated, or vendor's answers raise disqualifying concerns. Document the rejection and the basis. If rejection creates a separate operational risk (e.g., unpatched vulnerability), escalate that risk for a separate risk acceptance decision.

**Recommendation detail:** _(2–4 sentences explaining the recommendation, the key factors, and what would change the recommendation. If "Approve with Conditions," name the conditions that are load-bearing.)_

### What Would Change This Recommendation

_(Be explicit: what additional findings would downgrade a conditional approval to a reject? What remediation by the vendor would upgrade a defer to an approval? This section prevents the recommendation from being treated as final when conditions change.)_

---

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | | |
| Compliance Analyst | Priya Nair | | |
| CISO | Jennifer Wu | | |

**CIP-013 R2 Reference:** _(Link this document to the applicable section of Lone Star's CIP-013 supply chain risk management plan)_
