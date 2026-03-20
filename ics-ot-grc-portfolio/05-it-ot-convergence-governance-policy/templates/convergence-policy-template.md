# IT/OT Convergence Governance Policy
## Lone Star Transmission Services, LLC

**Document ID:** POL-OT-CONV-001
**Version:** _(version number)_
**Effective Date:** _______________
**Owner:** OT Security Lead
**Approved by:** CISO
**Review cycle:** Annual

---

## Section 1: Purpose and Scope

### 1.1 Purpose

This policy governs the connection of Operational Technology (OT) systems to Information Technology (IT) networks, enterprise applications, and cloud services at Lone Star Transmission Services, LLC. It establishes approval requirements, security controls, and oversight mechanisms for IT/OT convergence connections.

The purpose is not to prohibit IT/OT convergence. Business drivers for operational data visibility, remote monitoring, and analytics are legitimate. The purpose is to ensure that convergence connections are established with full visibility into the associated risks, with appropriate controls in place, and with documented accountability for those controls.

### 1.2 Scope

This policy applies to:

- All connections between OT networks (including substation control LANs, SCADA networks, and field device networks) and IT networks (including corporate LANs, enterprise applications, and cloud services)
- All data flows from OT systems to IT systems, regardless of whether those flows carry control commands
- All personnel who initiate, configure, operate, or maintain IT/OT convergence connections
- All third-party vendors whose systems connect to, or receive data from, Lone Star OT systems through an IT pathway

This policy does **not** apply to:
- OT-to-OT connections between Lone Star substations that do not traverse the corporate IT network
- NERC ERCOT data links (governed separately under CIP-005 Electronic Security Perimeter controls)

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

---

## Section 3: Approved Connection Types and Requirements

### 3.1 Type A — Outbound Data Replication (Low Risk)

**Description:** OT historical or telemetry data is replicated outbound from OT to IT or cloud systems. No return data path exists. Data flow is one-directional.

**Requirements:**
- Unidirectional gateway (hardware data diode) **preferred**; if not implemented, bidirectional firewall with egress-only rules is the minimum control, with documented justification for why a data diode was not implemented
- Data classification assessment completed (see Section 6)
- Receiving IT/cloud system documented and approved
- Data owner designated for data in the IT/cloud system
- Access controls on receiving system reviewed and approved by IT Security
- If data qualifies as BCSI per CIP-011: enhanced access controls required (see Section 6)

**Examples:** Historian replication to enterprise data lake; SCADA KPI feeds to executive dashboards; equipment health metrics to maintenance systems

### 3.2 Type B — Remote Monitoring (Medium Risk)

**Description:** IT systems or users have read-only visibility into OT systems. No control commands traverse the connection. Data flow is primarily outbound (OT to IT) with authentication/session management traffic inbound.

**Requirements:**
- All Type A requirements
- Encrypted transport (TLS 1.3 minimum) for all connections
- Multi-factor authentication required for all user access
- Session logging for all remote access events
- Network monitoring at the OT/IT boundary
- Maintenance window notification when remote monitoring access is first enabled

**Examples:** Read-only SCADA dashboards accessible to IT-network users; remote alarm monitoring; cloud-based equipment analytics platforms with read-only data access

### 3.3 Type C — Remote Access with Write Capability (High Risk)

**Description:** IT-side users or systems can write to, configure, or send commands to OT systems through an IT/OT pathway. This includes engineering workstation remote access and vendor maintenance remote access.

**Requirements:**
- All Type A and Type B requirements
- Privileged Access Management (PAM) system controls all sessions; no direct RDP or SSH to OT assets without PAM intermediation
- Vendor and third-party access governed by CIP-013 vendor assessment (see Project 04)
- Just-in-time access: sessions are enabled only when needed and automatically terminated after work is complete
- Dual approval required to activate session (requestor + approver)
- All session activity recorded and retained for minimum 90 days
- Change control ticket required for each access event

---

## Section 4: Prohibited Connection Patterns

The following connection patterns are **prohibited** regardless of business justification. Exceptions require CISO approval and documented risk acceptance.

| Prohibited Pattern | Rationale |
|-------------------|----------|
| Direct internet connectivity for OT systems | No OT system shall have a directly routable internet IP address or an internet-facing service; all external connectivity must traverse IT infrastructure with monitoring and access control |
| Bidirectional control protocol connectivity between OT and cloud | SCADA protocols (DNP3, Modbus, IEC 61850) shall not traverse the IT network to cloud systems; these protocols are not designed for internet transport and provide no authentication or integrity protection |
| Shared accounts for IT/OT convergence connections | All accounts used to authenticate IT/OT convergence sessions (including service accounts for historian replication) must be individually attributed; shared credentials are prohibited |
| IT system writes to OT process historian without change control | IT applications shall not write to OT historian tag data; historian tag writes are an OT change and require OT change control approval |
| OT data in unsanctioned cloud services | OT data (including historian replicas) shall not be stored in cloud services that have not been approved through the process in Section 5; personal cloud storage, unsanctioned SaaS, and vendor-hosted platforms without review are prohibited |
| Shadow IT convergence connections | All IT/OT convergence connections must be approved through the process in Section 5; connections established without approval are prohibited and constitute a policy violation (see finding classification in Section 7) |

---

## Section 5: Approval Authority and Workflow

### 5.1 Approval Tiers

| Connection Type | Approval Authority |
|----------------|-------------------|
| Type A — Outbound Data Replication | OT Security Lead + IT Security Lead (co-approval) |
| Type B — Remote Monitoring | OT Security Lead + IT Security Lead + Operations Manager |
| Type C — Remote Access with Write Capability | OT Security Lead + CISO (mandatory) + Operations Manager |
| Exceptions to Prohibited Patterns | CISO (sole authority) + documented risk acceptance |

### 5.2 Approval Workflow

**Step 1 — Request submission:** Business unit or IT lead submits a Convergence Connection Request via _(IT ticketing system)_. Request must include: data flow description, assets involved, receiving system documentation, proposed security controls, and business justification.

**Step 2 — Classification assessment:** Compliance Analyst reviews data flow for BCSI status under CIP-011. Result is documented and attached to the request.

**Step 3 — OT Security review:** OT Security Lead reviews the connection architecture, proposed controls, and BCSI determination. May request additional information or require architectural changes before approval.

**Step 4 — IT Security review:** IT Security Lead reviews receiving system configuration, cloud tenant settings (if applicable), and access controls.

**Step 5 — Risk assessment:** If gaps are identified, a data flow risk analysis (template in this project) is completed.

**Step 6 — Approval decision:** Per tier above. All approvals documented in the request ticket and retained in the OT security program documentation.

**Step 7 — Post-approval:** Connection is implemented by IT/OT engineering per approved design. OT Security Lead verifies implementation matches approved architecture before connection goes live.

### 5.3 Emergency Exceptions

If a business unit requires an IT/OT convergence connection on an emergency basis (e.g., to support incident response), a temporary exception may be granted by the CISO with documented justification. Temporary exceptions expire after 30 days and must be converted to an approved connection or terminated.

---

## Section 6: Logging and Monitoring Requirements

### 6.1 At the IT/OT Boundary

All IT/OT convergence connections must generate logs at the boundary device (firewall, boundary switch, or data diode management interface):
- Session initiation and termination (source/destination IP, port, timestamp)
- Authentication events (success and failure)
- Volume anomalies (data transfers significantly above or below baseline)
- Protocol anomalies (unexpected protocols traversing the boundary)

Log retention: minimum 90 days (CIP-007 R4 minimum); 12 months recommended.

### 6.2 For Cloud-Hosted OT Data

- Azure activity logs enabled for all storage accounts containing OT data (minimum 90-day retention)
- Azure AD sign-in logs for all accounts with access to OT data storage
- Alerts configured for: access from unexpected geographies; bulk data downloads; new service principal access; storage configuration changes
- Logs forwarded to Lone Star's SIEM (or reviewed manually weekly if no SIEM integration is available)

### 6.3 For BCSI in Cloud Systems

If data is determined to qualify as BCSI under CIP-011:
- Access restricted to specifically authorized personnel (documented list)
- All access logged and reviewed quarterly
- Annual access recertification required
- Data not accessible to general Azure AD tenant users

---

## Section 7: Incident Escalation for Convergence Events

### 7.1 Convergence Policy Violations

| Violation Type | Finding Classification | Required Action |
|---------------|----------------------|----------------|
| Connection established without approval | **Policy Violation — Category 2** | Connection reviewed and either approved (retroactively, with full documentation) or terminated within 30 days; CISO notified; finding logged in risk register |
| Prohibited connection pattern enabled | **Policy Violation — Category 1** | Connection terminated immediately pending CISO risk acceptance review; OT Security Lead notified within 24 hours |
| BCSI exposed to unauthorized users | **Potential CIP-011 Violation** | OT Security Lead and Compliance Analyst notified immediately; CIP self-report evaluation initiated within 5 business days |

### 7.2 Security Incidents on Convergence Connections

If a security incident involves or may involve an IT/OT convergence connection:
- OT Security Lead notified within 1 hour of detection
- Connection suspended pending investigation (unless suspension creates a reliability risk, in which case Operations Manager decision required)
- Incident documented in compliance event log (CIP-007 R4)
- CISO briefed within 4 hours
- NERC notification evaluated per CIP-008 if incident has or may have BES reliability impact

---

## Section 8: Review and Recertification Cycle

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Policy review | Annual | OT Security Lead |
| Approved connection inventory review | Annual | OT Security Lead + IT Security Lead |
| Cloud access recertification (OT data) | Annual | IT Security Lead |
| BCSI data classification review | Annual | Compliance Analyst |
| Firewall rule review (IT/OT boundary) | Semi-annual | IT Security |
| New connection requests | As submitted | Per Section 5 workflow |
