# IT/OT Convergence Data Flow Risk Analysis
## Lone Star Transmission Services, LLC

**Connection Name:** _______________
**Document ID:** _(e.g., CONV-RA-2024-001)_
**Connection Type:** _(Type A / B / C per governance policy)_
**Prepared by:** _______________
**Date:** _______________
**Status:** ☐ Draft  ☐ Approved  ☐ Active (approved and implemented)

---

## Part 1: Data Flow Segment Analysis

> **Instructions:** Break the data flow into segments at each network or system boundary. Document what assets are involved, what data classification applies, what controls are in place at each segment, what gaps exist, and the risk rating for each segment. The risk analysis is not complete until every segment has been addressed — a gap at any single segment can expose the entire data path.

| Segment | Assets Involved | Data Traversing This Segment | Data Classification | Controls in Place | Gaps Identified | Risk Rating | Remediation Owner |
|---------|----------------|------------------------------|---------------------|------------------|-----------------|------------|------------------|
| OT Source | _(e.g., WJSS-008 AVEVA PI Historian; WJSS-007 IT/OT boundary switch)_ | _(e.g., PI tag data: real-time SCADA telemetry, equipment health metrics, operational KPIs; HTTPS/443 outbound)_ | _(e.g., Potentially BCSI per CIP-011 — pending formal classification; operationally sensitive)_ | _(e.g., Outbound firewall rule on DMZ-FW-01 permits historian HTTPS; rule added without IT Security review)_ | _(e.g., Firewall rule scope not verified; may permit broader HTTPS than intended; no deep packet inspection on outbound historian traffic)_ | _(High/Medium/Low)_ | _(Name)_ |
| Corporate WAN | _(e.g., Microwave link from WJSS to corporate datacenter; corporate network switches)_ | _(e.g., Same historian data in transit; TLS-encrypted)_ | _(e.g., Encrypted in transit; classification of data at rest on WAN infrastructure not assessed)_ | _(e.g., TLS 1.2 encryption; corporate WAN monitoring)_ | _(e.g., TLS version — is TLS 1.3 enforced or is TLS 1.2 acceptable? Certificate pinning not implemented)_ | _(High/Medium/Low)_ | _(Name)_ |
| Cloud Ingestion | _(e.g., Azure Data Factory pipeline in East US 2; managed identity authentication)_ | _(e.g., Historian data received, transformed, and loaded to Azure Data Lake)_ | _(e.g., OT data now in cloud — CIP-011 BCSI determination required)_ | _(e.g., Managed identity; Azure AD authentication; AES-256 encryption at rest)_ | _(e.g., No IP restriction on Data Factory endpoint; managed identity permissions scope not reviewed; no Lone Star IT Security review of Azure configuration)_ | _(High/Medium/Low)_ | _(Name)_ |
| Cloud Storage | _(e.g., Azure Data Lake Storage Gen2; Power BI workspace)_ | _(e.g., Historical and near-real-time OT telemetry; accessible to 14 Power BI users)_ | _(e.g., OT operational data; BCSI determination pending)_ | _(e.g., Azure AD access control; AES-256 encryption; Power BI row-level security not configured)_ | _(e.g., 14 user accounts — MFA status unverified; no IP restriction; data accessible from any internet-connected device with valid Azure AD credentials; no formal data retention or deletion policy)_ | _(High/Medium/Low)_ | _(Name)_ |
| _(Add segments as needed)_ | | | | | | | |

---

## Part 2: Reverse-Path Analysis

> **This section is required for all connections involving historian or data replication paths.** The question is not just what data flows outbound — it is whether the established path could be used to send traffic back toward the OT system. Hardware data diodes prevent this absolutely. Firewall-based architectures do not.

| Question | Assessment |
|----------|-----------|
| Does the OT source system accept inbound connections from the IT network or cloud? | _(Yes / No / Unknown — and explain)_ |
| Is the firewall rule at the IT/OT boundary an outbound-only rule, or does it permit any return traffic? | _(Describe the specific rule; "permit established" is different from "permit only outbound sessions")_ |
| If a threat actor compromised the Azure Data Factory managed identity, could they initiate a connection back toward the historian or the OT network? | _(Trace the reverse path; document what barriers exist)_ |
| Is a hardware data diode (unidirectional gateway) implemented? If not, what is the justification? | _(Yes/No — if no, document the compensating controls and the remediation plan)_ |

---

## Part 3: Threat Scenario — Attack Path via Convergence Connection

> **Instructions:** Map the attack path an adversary could follow if this convergence connection were used as an intrusion vector. Use MITRE ATT&CK for ICS technique references where applicable. This is not a hypothetical exercise — adversaries have used IT/OT convergence paths as a primary attack route in documented incidents (TRITON, Ukraine power grid attacks).

### Threat Scenario Narrative

_(Write 2–4 paragraphs describing the realistic worst-case attack path. Start from the adversary's assumed initial access point — typically the cloud tenant, corporate network, or vendor access path — and trace the path toward OT. Identify where the path is blocked, where it is weak, and what the OT-side impact would be if the adversary successfully traversed it.)_

### ATT&CK for ICS Technique Mapping

| Stage | Tactic | Technique | ID | How It Applies to This Connection |
|-------|--------|-----------|-----|----------------------------------|
| 1 | Initial Access | _(e.g., Phishing for Azure AD credentials)_ | _(e.g., T0817)_ | _(Attacker compromises Power BI user account; gains access to OT telemetry data)_ |
| 2 | Discovery | Remote System Discovery | T0846 | _(Attacker uses OT telemetry in Azure to map substation operational state; identifies maintenance windows from equipment health data patterns)_ |
| 3 | _(Lateral movement stage if applicable)_ | _(technique)_ | _(ID)_ | _(How the attacker moves from cloud/IT toward OT)_ |
| 4 | Impact | Manipulation of View | T0832 | _(If attacker achieves historian write access, they could inject false data into the replication stream, causing dashboards to show incorrect operational state)_ |
| _(add stages)_ | | | | |

### Adversary Stopping Points

| Stage | Where the Adversary Is Stopped | Control Responsible | Control Effectiveness |
|-------|-------------------------------|--------------------|--------------------|
| Cloud access | _(e.g., Azure AD MFA — if enabled)_ | _(IT Security / Azure config)_ | _(High if MFA enforced; Unknown — MFA status not verified)_ |
| Corporate network pivot | _(e.g., Firewall rule at DMZ-FW-01 — only outbound sessions from historian permitted)_ | _(OT Security / IT Security)_ | _(Medium — depends on rule specificity; not reviewed)_ |
| OT system access | _(e.g., Historian does not accept inbound connections from Azure — if true)_ | _(Architecture)_ | _(Unknown — reverse-path analysis in Part 2 needed)_ |

---

## Part 4: CIP-011 BCSI Determination

> **Instructions:** This section must be completed for all connections involving data from BES Cyber System assets. NERC CIP-011 applies to BES Cyber System Information — information about BES Cyber Systems that, if disclosed, could facilitate unauthorized access or threaten BES reliability.

| Question | Assessment |
|----------|-----------|
| Does this data flow include information about the configuration, architecture, or operational state of BES Cyber Systems? | _(Yes / No — and explain)_ |
| If disclosed, could this data be used to facilitate unauthorized access to BES Cyber Systems? | _(e.g., Real-time switching state and equipment health data from a 345 kV substation could inform an adversary about operational conditions, maintenance patterns, and equipment vulnerabilities)_ |
| **BCSI determination** | _(BCSI / Not BCSI / Requires further analysis)_ |
| If BCSI: are the CIP-011 access control requirements met by the cloud storage controls? | _(Assess against CIP-011 R1 and R2 requirements)_ |
| If BCSI and cloud controls are inadequate: what is the remediation plan? | _(Required actions and timeline)_ |

---

## Part 5: Risk Summary and Approval Recommendation

| Segment | Risk Rating | Key Control Gap |
|---------|------------|----------------|
| OT Source | _(H/M/L)_ | _(Gap)_ |
| Corporate WAN | _(H/M/L)_ | _(Gap)_ |
| Cloud Ingestion | _(H/M/L)_ | _(Gap)_ |
| Cloud Storage | _(H/M/L)_ | _(Gap)_ |
| **Overall** | _(H/M/L)_ | _(Summary)_ |

**Approval recommendation:** ☐ Approve  ☐ Approve with Conditions  ☐ Remediate Before Approval  ☐ Terminate Connection

**Required conditions (if conditional approval):**

| Condition | Deadline | Verification Owner |
|-----------|---------|------------------|
| _(e.g., Azure AD MFA verified for all 14 Power BI users)_ | _(date)_ | _(name)_ |
| _(e.g., Data Factory IP restriction implemented)_ | _(date)_ | _(name)_ |
| _(e.g., Firewall rule scope reviewed and confirmed)_ | _(date)_ | _(name)_ |

---

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | | |
| IT Security Lead | _(Name)_ | | |
| Compliance Analyst | Priya Nair | | |
| CISO (if Type C or exception) | Jennifer Wu | | |
