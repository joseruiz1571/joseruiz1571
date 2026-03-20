# Vendor Security Assessment Questionnaire
## NERC CIP-013 Supply Chain Risk Management
### Lone Star Transmission Services, LLC

**Vendor Name:** _______________
**Engagement Type:** _(Firmware update / Software delivery / Remote access / On-site services)_
**BES Cyber System components affected:** _______________
**Assessment Date:** _______________
**Assessor:** _______________

---

> **Instructions to Vendor:** Please answer all questions in writing. For yes/no questions, provide a brief explanation supporting your answer. Where documentation is requested, attach it to your response. Lone Star will review responses and may follow up with clarifying questions. Incomplete or evasive responses will be treated as unfavorable findings.
>
> **Instructions to Assessor:** For each section, record the vendor's response and your evaluative note. Flag any "Disqualifying Answer" responses immediately — these require escalation to the OT Security Lead before the assessment continues.

---

## Section 1: Organizational Security Posture

*Purpose: Understand whether the vendor has a baseline security program. A vendor with no security practices is a higher risk regardless of their technical competence.*

| # | Question | Vendor Response | Assessor Note |
|---|----------|----------------|---------------|
| 1.1 | Does your organization have a documented information security policy? If yes, provide a summary or the policy document itself. | | |
| 1.2 | Does your organization hold any security certifications (SOC 2, ISO 27001, NIST CSF self-assessment, IEC 62443 certification)? If yes, provide the most recent report or certificate. | | |
| 1.3 | Do you conduct annual security awareness training for all employees who have access to customer systems or customer data? | | |
| 1.4 | Do you perform background checks on employees prior to hiring? Does this include employees who will have access to Lone Star's OT systems or facilities? | | |
| 1.5 | Have you experienced a cybersecurity incident in the last 36 months that affected customer data, customer systems, or your ability to deliver services? If yes, describe the incident and your response. | | |
| 1.6 | Are you a member of any ICS/OT security information sharing communities (E-ISAC, WaterISAC, ICS-CERT coordination)? | | |

> **Disqualifying Answer — 1.5:** A vendor that discloses a prior incident is not automatically disqualified. A vendor that discloses an incident and demonstrates no post-incident improvement, or that provides an evasive non-answer when pressed, is a disqualifying response. "We had a small issue but it didn't affect anything" without documentation is not an acceptable answer.

> **Disqualifying Answer — 1.4:** "No" to background checks for personnel accessing Lone Star's OT systems or facilities is a Critical finding. No compensating control substitutes for the inability to verify the identity and background of personnel with physical access to a 345 kV substation.

---

## Section 2: Software Development and Release Practices

*Purpose: For vendors delivering software or firmware, understand how that code is developed, tested, and delivered. The firmware update path is a documented attack vector — adversaries have used compromised software delivery to gain access to ICS environments (cf. SolarWinds, 3CX).*

| # | Question | Vendor Response | Assessor Note |
|---|----------|----------------|---------------|
| 2.1 | Describe your software/firmware development lifecycle. Is it based on a recognized secure development framework (e.g., NIST SSDF, IEC 62443-4-1)? | | |
| 2.2 | Do you perform security testing (code review, static analysis, penetration testing) on firmware or software before release? If yes, describe the process and who performs it. | | |
| 2.3 | How do you ensure that the firmware/software delivered to Lone Star has not been modified after your final release? Do you provide cryptographic hash values for delivered artifacts? | | |
| 2.4 | How is firmware stored and transported prior to delivery? Describe the chain of custody from your development environment to the customer's facility. | | |
| 2.5 | Do you use any open-source or third-party components in the firmware you deliver? If yes, do you track those components and monitor them for known vulnerabilities? | | |
| 2.6 | How do you notify customers of security vulnerabilities discovered in previously delivered software or firmware? What is your typical disclosure timeline? | | |

> **Disqualifying Answer — 2.3:** "We don't provide hashes" or "we just send the file" without any integrity verification mechanism. If the vendor cannot provide cryptographic verification of their firmware image, Lone Star has no way to confirm that what was delivered is what the vendor released. This is a Critical finding for firmware destined for 345 kV protection circuits.

> **Disqualifying Answer — 2.6:** "We don't have a vulnerability disclosure process" is a Critical finding. Lone Star needs assurance that if a vulnerability is discovered in deployed firmware, they will be notified. No notification process means Lone Star may be running vulnerable firmware indefinitely without knowing it.

---

## Section 3: Software Bill of Materials (SBOM) Capabilities

*Purpose: CIP-013 guidance and CISA recommendations increasingly reference SBOM as a supply chain transparency mechanism. For OT firmware, an SBOM reveals whether the firmware contains third-party libraries with known vulnerabilities.*

| # | Question | Vendor Response | Assessor Note |
|---|----------|----------------|---------------|
| 3.1 | Can you provide a Software Bill of Materials (SBOM) for the firmware update to be deployed at Lone Star? If yes, in what format (SPDX, CycloneDX, other)? | | |
| 3.2 | If you cannot provide a full SBOM, can you identify the major third-party libraries or components included in the firmware, and the version numbers? | | |
| 3.3 | Do you have a process for monitoring SBOM components for newly disclosed CVEs after firmware has been delivered to customers? | | |
| 3.4 | Is the firmware you deliver solely developed by your organization, or does it incorporate code or libraries from SEL (the relay manufacturer) or other third parties? | | |

> **Disqualifying Answer:** There is no disqualifying answer for SBOM absence alone — many small ICS vendors do not yet have SBOM programs. However, "No" to 3.1 AND "No" to 3.2 AND "No" to 3.3 together constitute a Significant finding that requires compensating controls (independent hash verification, deployment in isolated test environment first, enhanced post-deployment monitoring). Document the gap explicitly.

---

## Section 4: Incident Response and Disclosure Practices

*Purpose: If this vendor has a breach, Lone Star needs to know about it — especially if the breach affects systems used to build or deliver firmware for BES Cyber Systems.*

| # | Question | Vendor Response | Assessor Note |
|---|----------|----------------|---------------|
| 4.1 | Do you have a documented incident response plan? If yes, provide a summary or the plan itself (redacted as needed). | | |
| 4.2 | What is your process for notifying customers if you experience a security incident that may have affected your ability to deliver secure software or services? What is your notification timeline? | | |
| 4.3 | Do you maintain logs of access to systems used to develop, store, or deliver firmware or software? How long are logs retained? | | |
| 4.4 | Have you engaged a third party to test your incident response capability (tabletop exercise, red team exercise) in the past 24 months? | | |
| 4.5 | If asked by Lone Star after a suspected security event, would you be able to provide forensic artifacts or log data to support an investigation? | | |

> **Disqualifying Answer — 4.2:** "We don't have a process for customer notification" is a Critical finding. CIP-013 requires Lone Star to ensure that vendors notify them of incidents — if the vendor's answer is that they have no such process, the contract must be amended before the engagement can proceed. This is non-negotiable.

---

## Section 5: Third-Party and Subcontractor Risk

*Purpose: Small ICS vendors often subcontract specialized work. A subcontractor with weaker security practices is still Lone Star's risk if that subcontractor touches firmware that ends up on 345 kV protection circuits.*

| # | Question | Vendor Response | Assessor Note |
|---|----------|----------------|---------------|
| 5.1 | Will any work on this engagement be performed by subcontractors or third parties? If yes, identify them. | | |
| 5.2 | Do subcontractors who access customer systems or facilities go through the same background check and security training requirements as your direct employees? | | |
| 5.3 | Do you require subcontractors to meet minimum security standards as a condition of engagement? If yes, describe those standards and how you enforce them. | | |
| 5.4 | Do you maintain a list of approved subcontractors, and do you notify customers when a new subcontractor is introduced to an engagement? | | |

> **Disqualifying Answer — 5.1 + 5.2 combination:** "Yes, we use subcontractors" AND "No, subcontractors are not subject to the same background checks" is a Critical finding for engagements involving on-site access to OT facilities. The identity and background of any person entering Lone Star's substation P&C room must be verified regardless of their employment relationship with the prime vendor.

---

## Section 6: Contractual and Legal Posture

*Purpose: Confirm whether the existing contract language supports CIP-013 requirements. This section is reviewed by legal and compliance, not just the OT security team.*

| # | Question | Vendor Response | Assessor Note |
|---|----------|----------------|---------------|
| 6.1 | Does your organization agree to notify Lone Star within 72 hours of discovering a security incident that may have affected Lone Star's systems, data, or the integrity of deliverables? | | |
| 6.2 | Does your organization agree to cooperate with a security audit conducted by Lone Star or a designated third party, with reasonable advance notice? | | |
| 6.3 | Does your organization's legal jurisdiction create any restrictions on your ability to disclose security incidents to US utility customers? | | |
| 6.4 | Does your organization have ownership, investment, or operational relationships with entities in OFAC-sanctioned countries or countries of concern (China, Russia, Iran, North Korea)? | | |
| 6.5 | Are you aware of any pending litigation, regulatory action, or government investigation that could affect your ability to deliver services to Lone Star? | | |

> **Disqualifying Answer — 6.4:** Any affirmative answer requires immediate escalation to CISO and legal counsel. Foreign ownership or investment relationships with countries of concern are a NERC CIP-013 supply chain risk that cannot be mitigated by compensating controls alone — it requires legal review and potentially FERC/NERC notification depending on the nature of the relationship.

> **Disqualifying Answer — 6.1/6.2:** "No" to notification and audit rights in the contract is a Critical contractual finding. These terms must be added to the contract before any CIP-013-covered engagement proceeds. Lone Star cannot accept supply chain risk from a vendor it has no contractual ability to audit or require disclosure from.

---

## Assessment Summary

| Section | Finding Tier | Notes |
|---------|-------------|-------|
| 1 — Organizational Security Posture | Critical / Significant / Notable / Satisfactory | |
| 2 — Software Development & Release | Critical / Significant / Notable / Satisfactory | |
| 3 — SBOM Capabilities | Critical / Significant / Notable / Satisfactory | |
| 4 — Incident Response | Critical / Significant / Notable / Satisfactory | |
| 5 — Third-Party Risk | Critical / Significant / Notable / Satisfactory | |
| 6 — Contractual Posture | Critical / Significant / Notable / Satisfactory | |

**Critical findings:** _(List — any single Critical finding requires immediate escalation)_
**Significant findings:** _(List — require compensating controls before approval)_
**Notable findings:** _(List — documented and monitored; do not block approval)_

**Overall recommendation:** ☐ Approve  ☐ Approve with Conditions  ☐ Defer Pending Remediation  ☐ Reject
