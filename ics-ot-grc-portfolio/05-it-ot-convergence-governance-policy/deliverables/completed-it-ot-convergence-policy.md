# IT/OT Convergence Governance Policy — COMPLETED
## Lone Star Transmission Services, LLC

**Document ID:** POL-OT-CONV-001
**Version:** 1.0
**Effective Date:** January 15, 2026
**Owner:** OT Security Lead
**Approved by:** CISO
**Review cycle:** Annual (next review: January 15, 2027)

---

## Section 1: Purpose and Scope

### 1.1 Purpose

This policy governs the connection of Operational Technology (OT) systems to Information Technology (IT) networks, enterprise applications, and cloud services at Lone Star Transmission Services, LLC. It establishes approval requirements, security controls, and oversight mechanisms for IT/OT convergence connections.

The purpose is not to prohibit IT/OT convergence. Business drivers for operational data visibility, remote monitoring, and analytics are legitimate. The purpose is to ensure that convergence connections are established with full visibility into the associated risks, with appropriate controls in place, and with documented accountability for those controls.

This policy exists in part because of a specific incident: in Q1 2025, the Operations Analytics team established a live data replication connection between the AVEVA PI historian at Waco Junction Substation and an Azure Data Factory pipeline — without OT Security review, without IT Security review, and without compliance assessment. The connection ran for approximately 90 days before it was discovered during a routine network traffic review. That incident is not treated as a compliance failure in this document; it is treated as the evidence that governance was needed. This policy is the governance.

### 1.2 Scope

This policy applies to:

- All connections between OT networks (including substation control LANs, SCADA networks, and field device networks) and IT networks (including corporate LANs, enterprise applications, and cloud services)
- All data flows from OT systems to IT systems, regardless of whether those flows carry control commands
- All personnel who initiate, configure, operate, or maintain IT/OT convergence connections
- All third-party vendors whose systems connect to, or receive data from, Lone Star OT systems through an IT pathway

This policy does **not** apply to:
- OT-to-OT connections between Lone Star substations that do not traverse the corporate IT network
- ERCOT data links (governed separately under CIP-005 Electronic Security Perimeter controls)

### 1.3 Relationship to NERC CIP

IT/OT convergence connections may implicate NERC CIP standards:
- **CIP-005:** Connections crossing the Electronic Security Perimeter boundary require Electronic Access Point controls
- **CIP-007:** Logging and monitoring requirements for BES Cyber System assets connected to converged networks
- **CIP-011:** Information protection requirements for BES Cyber System Information that may traverse or reside on IT systems or cloud platforms

This policy supplements, and does not replace, Lone Star's NERC CIP compliance program. Where this policy and NERC CIP requirements conflict, NERC CIP governs.

---

## Section 2: Definitions

| Term | Definition |
|------|-----------|
| **IT/OT Convergence Connection** | Any network path, data flow, or application integration that connects an OT system to an IT network, enterprise application, or cloud service |
| **OT System** | Any system whose primary function is the monitoring, control, protection, or automation of physical infrastructure, including SCADA systems, HMIs, PLCs, protective relays, RTUs, historians, and engineering workstations |
| **BES Cyber System Information (BCSI)** | Per NERC CIP-011: information about BES Cyber Systems that, if disclosed, could be used to gain unauthorized access to BES Cyber Systems or could pose a threat to the reliable operation of the BES |
| **Unidirectional Gateway** | A hardware-enforced device that permits data flow in only one direction; data can flow from OT to IT but not from IT to OT; no protocol-layer bidirectional communication is possible |
| **Data Diode** | A hardware security device implementing a unidirectional gateway; typically implemented as paired optical transceivers with no reverse data path |
| **Historian** | An OT data historian system (e.g., AVEVA PI, OSIsoft PI) that archives time-series process data; commonly the source of IT/OT convergence data flows |
| **Converged Zone** | A network segment or data system that receives data from both OT and IT sources, or that has connectivity to both OT and IT networks |
| **Approved Connection** | An IT/OT convergence connection that has completed the approval workflow defined in Section 5 of this policy |
| **Shadow Connection** | Any IT/OT convergence connection that was established without completing the approval workflow in Section 5; Shadow Connections are a policy violation |

---

## Section 3: Approved Connection Types and Requirements

### 3.1 Type A — Outbound Data Replication (Low Risk)

**Description:** OT historical or telemetry data is replicated outbound from OT to IT or cloud systems. No return data path exists at the protocol layer. Data flow is one-directional in intent.

**Requirements:**
- Unidirectional gateway (hardware data diode) is the preferred architecture; if not implemented, bidirectional firewall with egress-only rules is the minimum control, with written justification for why a data diode was not implemented, reviewed and accepted by OT Security Lead
- Data classification assessment completed by Compliance Analyst (see Section 6)
- Receiving IT or cloud system documented and approved by IT Security
- Data owner designated for data in the IT or cloud system — OT Security and IT Security must agree on who owns the data once it leaves the OT environment
- Access controls on receiving system reviewed and approved by IT Security
- If data qualifies as BCSI per CIP-011: enhanced access controls required per Section 6

**Examples of this connection type in Lone Star's environment:** The AVEVA PI historian-to-Azure connection established by Operations Analytics in Q1 2025 is a Type A connection that was established without completing this approval workflow. It is currently operating under an interim approval pending completion of the data flow risk analysis (see Project 05 deliverables) and full approval workflow.

### 3.2 Type B — Remote Monitoring (Medium Risk)

**Description:** IT systems or users have read-only visibility into OT systems. No control commands traverse the connection. Data flow is primarily outbound (OT to IT) with authentication and session management traffic inbound.

**Requirements:**
- All Type A requirements
- Encrypted transport (TLS 1.3 minimum) for all connections
- Multi-factor authentication required for all user access — no exceptions for executives or business unit personnel
- Session logging for all remote access events, retained minimum 90 days
- Network monitoring at the OT/IT boundary
- Written notification to OT Security Lead when remote monitoring access is first enabled; OT Security Lead must confirm architecture before go-live

**Examples:** Read-only SCADA dashboards accessible to IT-network users; remote alarm monitoring; cloud-based equipment analytics platforms with read-only data access

### 3.3 Type C — Remote Access with Write Capability (High Risk)

**Description:** IT-side users or systems can write to, configure, or send commands to OT systems through an IT/OT pathway. This includes engineering workstation remote access and vendor maintenance remote access.

**Requirements:**
- All Type A and Type B requirements
- Privileged Access Management (PAM) system controls all sessions; no direct RDP or SSH to OT assets without PAM intermediation (target architecture — see gap note below)
- All vendor and third-party access must complete a CIP-013 supply chain vendor assessment before any access is provisioned
- Just-in-time access model: sessions are enabled only for the approved duration of the work activity and automatically terminated after completion
- Dual approval required to activate each session (requestor plus OT Security Lead or designated approver)
- All session activity recorded and retained for minimum 90 days
- Change control ticket required for each access event, referencing the approved activity

**Current state gap note:** PAM system (Privileged Access Management) is not yet implemented at Lone Star. Type C connections currently rely on enhanced manual controls (session recording at jump server, named personnel requirements, escort for on-site work) as compensating controls. PAM implementation is a tracked remediation item. Until PAM is in place, OT Security Lead must personally approve each Type C access event.

---

## Section 4: Prohibited Connection Patterns

The following connection patterns are **prohibited** regardless of business justification. Exceptions require CISO written approval and documented risk acceptance; no exception is automatic.

| Prohibited Pattern | Rationale |
|-------------------|----------|
| Direct internet connectivity for OT systems | No OT system shall have a directly routable internet IP address or internet-facing service. All external connectivity must traverse IT infrastructure with monitoring and access control. This is an absolute prohibition — there is no business justification that overrides it. |
| Bidirectional OT control protocol connectivity to cloud | SCADA protocols (DNP3, Modbus, IEC 61850) shall not traverse the IT network to cloud systems. These protocols have no authentication or integrity protection suitable for internet transport. Any legitimate operational need for remote SCADA can be met through secure remote access to the SCADA HMI — not by extending the SCADA protocol to the cloud. |
| Shared accounts for IT/OT convergence connections | All accounts used to authenticate convergence sessions — including service accounts for historian replication — must be individually attributed. Shared credentials for OT-adjacent systems are prohibited. This includes shared Windows service accounts used by data replication pipelines. |
| IT system writes to OT process historian tag data | IT applications shall not write to OT historian tag values. Historian tag writes are an OT operational change and require OT engineering change control approval. Analytics pipelines that require tagging, annotation, or enrichment must do so in the IT-side copy of the data, not in the OT historian itself. |
| OT data in unsanctioned cloud services | OT data (including historian replicas) shall not be stored in cloud services that have not been approved through the Section 5 workflow. Personal cloud storage, unsanctioned SaaS applications, and vendor-hosted platforms without explicit review are prohibited. |
| Shadow Connections | All IT/OT convergence connections must complete the approval workflow in Section 5 before being established. Connections established without approval — regardless of business urgency, regardless of who authorized them within the business unit — are Shadow Connections and constitute a policy violation. |

---

## Section 5: Approval Authority and Workflow

### 5.1 Approval Tiers

| Connection Type | Approval Authority |
|----------------|-------------------|
| Type A — Outbound Data Replication | OT Security Lead + IT Security Lead (co-approval required) |
| Type B — Remote Monitoring | OT Security Lead + IT Security Lead + Operations Manager (all three required) |
| Type C — Remote Access with Write Capability | OT Security Lead + CISO (mandatory) + Operations Manager |
| Exceptions to Prohibited Patterns | CISO (sole authority) + written risk acceptance; no business unit manager can grant this exception |

### 5.2 Approval Workflow

**Step 1 — Request submission:** Business unit or IT lead submits a Convergence Connection Request using the standard request form (available from IT Security). Request must include: data flow description in plain language, assets involved, receiving system documentation, proposed security controls, and business justification. Requests without all required fields will be returned without review.

**Step 2 — Data classification:** Compliance Analyst reviews data flow for BCSI status under CIP-011 within 5 business days of request receipt. BCSI determination is documented and attached to the request. All OT telemetry data from Medium or High impact BES Cyber Systems should be treated as potentially BCSI until classification is complete.

**Step 3 — OT Security review:** OT Security Lead reviews the connection architecture, proposed controls, and BCSI determination. May request additional information or require architectural modifications before approval. OT Security Lead review is complete within 10 business days of receiving the completed request.

**Step 4 — IT Security review:** IT Security Lead reviews receiving system configuration, cloud tenant settings (if applicable), and access control design. Concurrent with Step 3 where possible.

**Step 5 — Risk assessment:** If gaps are identified, the data flow risk analysis template is completed by OT Security and IT Security jointly.

**Step 6 — Approval decision:** Per tier above. All approvals documented in the request ticket and retained in the OT security program documentation. The documented approval record is the evidence of compliance with this policy.

**Step 7 — Post-approval verification:** Before the connection goes live, OT Security Lead verifies that the implementation matches the approved architecture. A connection that is implemented differently from what was approved must return to Step 1.

### 5.3 Retroactive Approval (Shadow Connection Remediation)

When a Shadow Connection is discovered, the following process applies:

1. OT Security Lead is notified within 24 hours of discovery.
2. The connection is assessed within 5 business days — is it a prohibited pattern, or is it a Type A/B/C connection that could be approved?
3. If approvable: complete the approval workflow retroactively (Steps 2-6). Connection may remain active during this review at OT Security Lead discretion.
4. If not approvable (prohibited pattern): connection is terminated within 30 days of discovery unless CISO grants an exception with documented risk acceptance.
5. Shadow Connection is logged in the risk register. Recurrence from the same team is escalated to CISO.

**Note:** The Q1 2025 PI-to-Azure connection is in retroactive approval status as of this policy's effective date. The data flow risk analysis (CONV-RA-2025-001) must be completed and approved before the connection can be moved to Approved status. The connection will remain in interim status until that process is complete.

### 5.4 Emergency Exceptions

If a business unit requires a convergence connection on an emergency basis (e.g., to support incident response), a temporary exception may be granted by the CISO with documented justification. Temporary exceptions expire after 30 days and must be converted to an Approved Connection or terminated by the expiration date. No temporary exception renews automatically.

---

## Section 6: BES Cyber System Information (BCSI) Data Classification

### 6.1 Classification Criteria

Data flowing through IT/OT convergence connections must be assessed for BCSI status under NERC CIP-011. Data qualifies as BCSI if it:
- Describes the configuration, design, or operational parameters of BES Cyber Systems
- If disclosed, could be used to facilitate unauthorized access to BES Cyber Systems
- If disclosed, could inform an attacker about grid operational state, vulnerabilities, or maintenance patterns

**Guideline for substation SCADA data:** Real-time SCADA telemetry from Medium or High impact transmission substations — including switching state, voltage and current measurements, equipment health metrics, and operational KPIs — is presumptively BCSI until assessed otherwise. The operational state of a 345 kV substation is information that a grid adversary could use to plan an attack or understand the impact of their actions.

### 6.2 Controls Required for BCSI in IT/Cloud Systems

If data is determined to qualify as BCSI:
- Access restricted to specifically authorized individuals; access list maintained by IT Security and reviewed quarterly
- All access logged with user attribution; logs reviewed quarterly by Compliance Analyst
- Annual access recertification required — access not recertified is revoked
- Data not accessible to general enterprise user population; specific authorization required
- Data deletion and retention policy in place; data retained no longer than operationally necessary
- Cloud service must meet Lone Star's approved cloud provider standards before BCSI is stored there

---

## Section 7: Logging and Monitoring Requirements

### 7.1 At the IT/OT Boundary

All convergence connections must generate logs at the boundary device:
- Session initiation and termination (source/destination IP, port, timestamp)
- Authentication events (success and failure)
- Volume anomalies — data transfers significantly above or below established baseline trigger an alert
- Protocol anomalies — unexpected protocols at the IT/OT boundary generate an immediate alert

Log retention: minimum 90 days (CIP-007 R4 minimum); 12 months recommended for Medium and High impact connections.

### 7.2 For Cloud-Hosted OT Data

- Azure activity logs enabled for all storage accounts containing OT data
- Azure AD sign-in logs retained and reviewed for all accounts with access to OT data
- Alerts configured for: access from unexpected geographies; bulk data downloads; new service principal access; storage configuration changes
- Weekly manual review in the absence of SIEM integration; automated alerting preferred

### 7.3 Quarterly Review Cycle

OT Security Lead conducts a quarterly review of all active IT/OT convergence connections:
- Verify connection is still operating as approved
- Verify access lists are current
- Review logs for anomalies
- Confirm receiving systems are still meeting the security requirements that were in place at approval

Connections that fail the quarterly review are placed in remediation status.

---

## Section 8: Incident Escalation for Convergence Events

### 8.1 Policy Violations

| Violation Type | Finding Classification | Required Action |
|---------------|----------------------|----------------|
| Shadow Connection discovered | **Policy Violation — Category 2** | Retroactive approval workflow initiated within 5 business days; CISO notified; finding logged in risk register |
| Prohibited connection pattern enabled | **Policy Violation — Category 1** | Connection suspended pending CISO risk acceptance review; OT Security Lead notified within 24 hours; if suspension creates a reliability risk, Operations Manager decision required with immediate documentation |
| BCSI exposed to unauthorized access | **Potential CIP-011 Violation** | OT Security Lead and Compliance Analyst notified immediately; CIP self-report evaluation initiated within 5 business days |

### 8.2 Security Incidents on Convergence Connections

If a security incident involves or may involve an IT/OT convergence connection:
- OT Security Lead notified within 1 hour of detection
- Connection suspended pending investigation unless suspension itself creates a reliability risk
- Incident documented per CIP-007 R4 event logging requirements
- CISO briefed within 4 hours
- NERC CIP-008 notification evaluated if incident has or may have BES reliability impact

---

## Section 9: Review and Recertification Cycle

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Policy review | Annual | OT Security Lead |
| Approved connection inventory review | Annual | OT Security Lead + IT Security Lead |
| Cloud access recertification (OT data) | Annual | IT Security Lead |
| BCSI data classification review | Annual | Compliance Analyst |
| Firewall rule review (IT/OT boundary) | Semi-annual | IT Security |
| Quarterly monitoring review | Quarterly | OT Security Lead |
| New connection requests | As submitted | Per Section 5 workflow |

---

## Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | *[signed]* | January 10, 2026 |
| IT Security Lead | Andrea Vasquez | *[signed]* | January 12, 2026 |
| Compliance Analyst | Priya Nair | *[signed]* | January 12, 2026 |
| CISO | Jennifer Wu | *[signed]* | January 15, 2026 |

**Document change log:**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | January 15, 2026 | M. Delgado / P. Nair | Initial policy — developed in response to Q1 2025 Shadow Connection discovery |
