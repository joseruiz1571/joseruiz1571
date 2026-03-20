# IT/OT Convergence Data Flow Risk Analysis — COMPLETED
## Lone Star Transmission Services, LLC

**Connection Name:** AVEVA PI Historian to Azure Data Lake (Power BI Analytics Pipeline)
**Document ID:** CONV-RA-2025-001
**Connection Type:** Type A — Outbound Data Replication (retroactive approval review)
**Prepared by:** Marcus Delgado, OT Security Lead; Andrea Vasquez, IT Security Lead
**Date:** January 20, 2026
**Status:** ☑ Approved with Conditions (see Part 5)

---

> **Context:** This data flow risk analysis was initiated after the AVEVA PI historian-to-Azure connection was discovered in Q4 2025, approximately 90 days after it was established by the Operations Analytics team without OT Security or IT Security review. This analysis constitutes the retroactive approval review required under POL-OT-CONV-001 Section 5.3. The connection will transition from "Shadow Connection — Interim Status" to "Approved" upon completion of all conditions listed in Part 5.

---

## Part 1: Data Flow Segment Analysis

| Segment | Assets Involved | Data Traversing This Segment | Data Classification | Controls in Place | Gaps Identified | Risk Rating | Remediation Owner |
|---------|----------------|------------------------------|---------------------|------------------|-----------------|------------|------------------|
| **OT Source** | WJSS-008 (AVEVA PI Historian); WJSS-007 (IT/OT boundary switch); DMZ-FW-01 (OT DMZ firewall) | Real-time SCADA telemetry tags: switching state of all 345 kV breakers and disconnects at WJSS; voltage and current measurements from 345 kV circuits; equipment health metrics (relay operating hours, battery status, trip counter data); operational KPIs derived from SCADA data. Sent via HTTPS (PI Web API) outbound. Volume: approximately 45 tags at 30-second polling intervals. | Presumptive BCSI pending formal classification (see Part 4). Real-time 345 kV substation operational state is the type of information CIP-011 is designed to protect. | Outbound HTTPS firewall rule on DMZ-FW-01 permits historian HTTPS. Rule was added without IT Security review. The scope of the permit rule — whether it allows only historian-originated HTTPS or broader outbound HTTPS from the substation LAN — has not been verified. | **Gap 1:** Firewall rule scope not verified by IT Security. A rule added without review may be more permissive than required. Specifically: if the rule permits outbound HTTPS from any source on the substation VLAN rather than specifically from WJSS-008, it creates an unnecessary attack surface. **Gap 2:** No hardware data diode. Historian path is firewall-based bidirectional at protocol layer; ACL rules enforce intended unidirectionality but cannot provide hardware-enforced unidirectionality. | **High** (pending firewall rule verification) | Marcus Delgado — firewall rule scope review |
| **Corporate WAN** | Microwave link from WJSS to corporate datacenter; corporate network switches and routers | Historian data in transit; TLS-encrypted from historian to Azure. No unencrypted segment identified. | Encrypted in transit. TLS version not verified; certificate pinning not implemented. | TLS encryption; corporate WAN monitoring via standard IT network monitoring tools. | **Gap 3:** TLS version not confirmed as 1.3; may be 1.2. TLS 1.2 is still acceptable but 1.3 is preferred for new connections. Certificate pinning is not implemented — a man-in-the-middle scenario (unlikely but not impossible on corporate WAN) could intercept traffic without certificate pinning. | **Low** | Andrea Vasquez — TLS version verification |
| **Cloud Ingestion** | Azure Data Factory pipeline (East US 2 region); managed identity for authentication | Historian data received by ADF, transformed, and loaded to Azure Data Lake. | OT data in cloud. Formal BCSI determination required (see Part 4). | Azure Data Factory uses managed identity (no hardcoded credentials — this is correct practice). AES-256 encryption at rest. | **Gap 4:** Azure Data Factory endpoint has no IP restriction. The managed identity can be called from any Azure region or any internet-connected resource with the right authentication context. If the managed identity were compromised, an attacker could potentially inject data into the pipeline. **Gap 5:** No Lone Star IT Security review of the ADF configuration — permissions scope of the managed identity, what data transformations are occurring, and whether the ADF pipeline could be used to initiate reverse connections have not been assessed. | **High** | Andrea Vasquez — ADF configuration review and IP restriction |
| **Cloud Storage** | Azure Data Lake Storage Gen2; Power BI workspace | Historical and near-real-time OT telemetry. 90 days of data currently accumulated. Accessible to 14 Power BI user accounts. | Presumptive BCSI. 90 days of 345 kV substation operational data is a comprehensive view of Lone Star's grid state over that period — enough to characterize operational patterns, identify maintenance windows, and understand equipment health trends. | Azure AD access control; AES-256 encryption at rest. | **Gap 6:** MFA status for all 14 Power BI user accounts is unverified. If any user account does not have MFA, their credentials are a single point of failure for access to this OT data from any internet-connected device. **Gap 7:** No IP restriction on Power BI workspace. Data accessible from any internet-connected device with valid Azure AD credentials. **Gap 8:** No formal data retention policy. Data accumulates indefinitely at 30-second granularity. 90 days of data is already significant; without a retention policy, this will grow to years. **Gap 9:** No formal data owner designated. IT and OT have not agreed on who is responsible for protecting this data once it is in Azure. | **High** | Andrea Vasquez — MFA enforcement, IP restriction; Priya Nair — retention policy and data owner designation |

---

## Part 2: Reverse-Path Analysis

| Question | Assessment |
|----------|-----------|
| Does the OT source system (WJSS-008 historian) accept inbound connections from the IT network or cloud? | **Requires verification.** The historian's PI Web API is configured to push data outbound. Whether it also accepts inbound API calls (for data writes, configuration changes, or diagnostics) has not been confirmed. AVEVA PI systems typically support bidirectional API access. Marcus Delgado to confirm historian API inbound configuration. If inbound connections are enabled, this elevates the risk rating for this segment substantially. |
| Is the firewall rule at the IT/OT boundary an outbound-only rule? | **Unknown — gap identified.** The rule was added without IT Security review; the exact rule specification has not been validated. Marcus Delgado has identified the rule review as a required remediation action (Gap 1). Until the rule is reviewed and confirmed as outbound-only from WJSS-008 specifically, the reverse-path assessment cannot be completed. |
| If a threat actor compromised the Azure Data Factory managed identity, could they initiate a connection back toward the historian or the OT network? | **Low likelihood, but not zero.** The ADF managed identity is scoped to data ingestion from the historian and loading to ADLS. If properly scoped, it cannot initiate outbound connections from Azure toward the corporate network or OT. However, "properly scoped" has not been verified by IT Security (Gap 5). A misconfigured managed identity with excessive permissions could potentially be used to reach other Azure services that have connectivity to the corporate network. This scenario is assessed as low likelihood but requires the ADF configuration review to resolve definitively. |
| Is a hardware data diode (unidirectional gateway) implemented? | **No.** DMZ-FW-01 provides firewall-based directionality control through ACL rules. This is the minimum acceptable control per POL-OT-CONV-001 Section 3.1, with required written justification for the absence of a data diode. **Justification for absence of data diode:** A hardware data diode for the historian path would require capital expenditure not in the current budget and a maintenance window to install. The capital project to evaluate a data diode is in the FY2027 budget planning cycle. In the interim, the firewall-based architecture is the compensating control, contingent on Gap 1 (firewall rule scope verification) being resolved. |

---

## Part 3: Threat Scenario — Attack Path via Convergence Connection

### Threat Scenario Narrative

The most realistic attack path using this convergence connection does not go from Azure toward the OT — it goes from OT data in Azure toward an attacker's intelligence objective. A nation-state actor who wants to understand the operational state of Lone Star's 345 kV transmission infrastructure before conducting a disruptive attack would find the Power BI dashboard a high-value reconnaissance target. The 14 Power BI user accounts represent 14 potential credential theft targets, any one of which provides access to real-time and historical substation operational data from any internet-connected device.

The secondary and more operationally dangerous scenario — using this connection as an ingress path toward the OT network — faces a more difficult path but cannot be ruled out. If the historian accepts inbound connections and the ADF managed identity has overly broad permissions, an attacker who compromises an Azure-side account or the ADF service could potentially push data or configuration toward the historian. From the historian, pivot to the SCADA Control LAN would depend on the historian's network connectivity and the state of the firewall rules at DMZ-FW-02.

The most significant control gap in this connection is not the path from Azure to OT — it is the absence of MFA verification for the 14 Power BI users and the absence of IP restriction on the workspace. Fixing these two gaps substantially reduces the reconnaissance attack surface without any architectural changes.

### ATT&CK for ICS Technique Mapping

| Stage | Tactic | Technique | ID | How It Applies to This Connection |
|-------|--------|-----------|-----|----------------------------------|
| 1 | Initial Access | Valid Accounts — Cloud Accounts | T0866 (adapted) | Attacker compromises a Power BI user's Azure AD credentials (via phishing, credential stuffing, or password spray); gains access to OT telemetry dashboard from any internet-connected device |
| 2 | Collection | Automated Collection | T0802 | Attacker uses compromised Azure AD session to export 90 days of historian data from ADLS — substation switching state, equipment health, and operational patterns at 30-second resolution |
| 3 | Discovery | Remote System Discovery | T0846 | Attacker analyzes historian data to identify maintenance windows (periods when equipment health alarms spike), operational patterns (normal switching sequences), and anomalies that reveal equipment vulnerabilities |
| 4 | Impact | Manipulation of View | T0832 | If attacker achieves historian write access (not confirmed possible — requires inbound connection capability), they could inject false data into the replication pipeline, causing Power BI dashboards to display incorrect operational state to executives and operations managers |
| 5 (conditional) | Lateral Movement | (via Azure tenant → corporate network) | Multiple | If ADF managed identity has excessive permissions and corporate network is reachable from Azure tenant, attacker may attempt to traverse from Azure toward corporate LAN and onward to OT — this path is highly contingent on Azure configuration (Gap 5) and is assessed as low likelihood with proper ADF scoping |

### Adversary Stopping Points

| Stage | Where the Adversary Is Stopped | Control Responsible | Control Effectiveness |
|-------|-------------------------------|--------------------|--------------------|
| Cloud access via compromised Power BI user | Azure AD MFA (if enabled) | IT Security / Azure configuration | **Unknown** — MFA enforcement for all 14 users has not been verified (Gap 6). This is the highest-priority control to verify. If any user lacks MFA, that user account is a viable attack vector. |
| Cloud access via ADF managed identity | Managed identity scope and permissions | IT Security / Azure configuration | **Unknown** — permissions scope not reviewed (Gap 5). If correctly scoped to read-from-historian and write-to-ADLS only, this stops the lateral movement path. Verification required. |
| Reverse path from Azure toward OT | DMZ-FW-01 outbound-only rule (if confirmed) | OT Security / IT Security | **Unknown** — rule scope not verified (Gap 1). If the rule is outbound-only from WJSS-008, this stops the inbound-from-Azure path. If the rule is broader, the firewall may not stop it. |
| OT system access from corporate network | DMZ-FW-02 + Z-02 DMZ architecture | OT Security | **Medium** — DMZ architecture provides segmentation but has known gaps (bidirectional firewall, no data diode). An attacker who reaches the corporate LAN still faces the DMZ barrier. |

---

## Part 4: CIP-011 BCSI Determination

| Question | Assessment |
|----------|-----------|
| Does this data flow include information about the configuration, architecture, or operational state of BES Cyber Systems? | **Yes.** The historian data includes real-time switching state of 345 kV equipment, voltage and current measurements, relay operating parameters, and equipment health metrics from WJSS — which is classified as a Medium impact BES Cyber System under CIP-002-5.1a. |
| If disclosed, could this data be used to facilitate unauthorized access to BES Cyber Systems? | **Yes.** Real-time switching state and equipment health data from a 345 kV substation could inform an adversary about: (1) current operational state (which breakers are open or closed); (2) maintenance patterns inferred from equipment health degradation and operational anomalies; (3) SCADA system behavior patterns that could inform spoofing or replay attacks. |
| **BCSI determination** | **BCSI — formal determination.** The historian replication data constitutes BES Cyber System Information under CIP-011. This determination was not made before the connection was established. |
| Are the CIP-011 access control requirements met by the cloud storage controls? | **No — currently non-compliant.** CIP-011 R1 requires that BCSI be identified and protected with appropriate access controls. The current Azure storage configuration has: (1) unverified MFA for 14 users; (2) no IP restriction; (3) no formal access review or recertification process; (4) no designated data owner; (5) no formal retention policy. None of these conditions meet CIP-011 R2 access control requirements for BCSI. |
| Remediation plan for BCSI compliance | See Part 5 conditions. All conditions must be completed to bring this connection into CIP-011 compliance. Compliance Analyst to document remediation completion as a CIP-011 evidence record. Self-report evaluation: Compliance Analyst to assess within 5 business days of this determination whether the 90-day period of non-compliant BCSI storage constitutes a reportable event under NERC's self-report guidelines. |

---

## Part 5: Risk Summary and Approval Recommendation

| Segment | Risk Rating | Key Control Gap |
|---------|------------|----------------|
| OT Source | High (pending remediation) | Firewall rule scope not verified (Gap 1); no hardware data diode (accepted with justification) |
| Corporate WAN | Low | TLS version confirmation pending (Gap 3) — minor |
| Cloud Ingestion | High (pending remediation) | ADF IP restriction absent (Gap 4); ADF configuration not reviewed (Gap 5) |
| Cloud Storage | High (pending remediation) | MFA enforcement for 14 users unverified (Gap 6); no IP restriction (Gap 7); no retention policy (Gap 8); no data owner (Gap 9) |
| **Overall** | **High (pending completion of conditions)** | Multiple control gaps in cloud infrastructure; BCSI determination requires immediate access control remediation |

**Approval recommendation:** ☑ Approve with Conditions

The connection is approvable — it is a legitimate business need (executive operational visibility), the data flow architecture is reasonable (outbound historian replication), and the control gaps are remediable without architectural redesign. However, the connection cannot move to Approved status until all conditions below are completed. Until conditions are complete, the connection remains in "Shadow Connection — Interim Approval" status.

**Required conditions:**

| Condition | Deadline | Verification Owner |
|-----------|---------|------------------|
| Firewall rule scope review — verify that DMZ-FW-01 rule permits HTTPS only from WJSS-008 source IP, not from any substation LAN host. If rule is broader than intended, narrow it. | February 28, 2026 | Marcus Delgado |
| Historian inbound connection verification — confirm whether WJSS-008 AVEVA PI accepts inbound connections via the PI Web API. If yes, restrict inbound access via firewall rule or API configuration. | February 28, 2026 | Marcus Delgado |
| ADF configuration review — IT Security Lead reviews ADF managed identity permissions scope, data transformation logic, and confirms no inbound connectivity to corporate network is possible via ADF | February 28, 2026 | Andrea Vasquez |
| ADF IP restriction — restrict ADF ingestion endpoint to permitted source IPs (corporate WAN egress IPs and WJSS historian IP) | February 28, 2026 | Andrea Vasquez |
| MFA enforcement — verify and enforce MFA for all 14 Power BI user accounts; any account without MFA has access suspended until MFA is configured | January 31, 2026 | Andrea Vasquez |
| Power BI workspace IP restriction — implement conditional access policy restricting Power BI workspace access to Lone Star corporate network IPs (or defined approved networks) | February 15, 2026 | Andrea Vasquez |
| Data owner designation — OT Security Lead and IT Security Lead formally designate a data owner for the OT data in Azure (agreed owner: IT Security Lead with OT Security Lead as secondary owner for BCSI classification purposes) | January 31, 2026 | Marcus Delgado / Andrea Vasquez |
| Data retention policy — establish and implement a 12-month rolling retention policy for ADLS; data older than 12 months deleted automatically | February 28, 2026 | Andrea Vasquez |
| CIP-011 self-report evaluation — Compliance Analyst assesses whether the 90-day period of non-compliant BCSI exposure requires a NERC self-report | January 25, 2026 | Priya Nair |
| Access recertification — first quarterly review of the 14 Power BI user accounts conducted within 90 days of conditions completion | April 30, 2026 | Andrea Vasquez |

---

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | *[signed]* | January 20, 2026 |
| IT Security Lead | Andrea Vasquez | *[signed]* | January 21, 2026 |
| Compliance Analyst | Priya Nair | *[signed]* | January 21, 2026 |
| CISO | Jennifer Wu | *[signed]* | January 22, 2026 |
