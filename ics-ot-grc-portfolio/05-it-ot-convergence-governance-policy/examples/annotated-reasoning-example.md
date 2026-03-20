# Annotated Reasoning Example — IT/OT Convergence Governance
## AVEVA PI Historian to Azure Data Lake — Risk Analysis, Finding Language, and Retroactive Approval

**Document ID:** CONV-RA-2024-001
**Connection:** WJSS-008 AVEVA PI Historian → Azure Data Lake → Power BI
**Connection Type:** Type A — Outbound Data Replication (per governance policy)
**Status:** Retroactive review — connection was live for 90 days without approval

---

## Part 1: Data Flow Segment Analysis

| Segment | Assets Involved | Data | Classification | Controls | Gaps | Risk | Owner |
|---------|----------------|------|---------------|---------|------|------|-------|
| OT Source (Historian → Boundary Switch) | WJSS-008 (AVEVA PI), WJSS-007 (boundary switch), DMZ-FW-01 | Real-time SCADA telemetry tags (switching state, voltage, current), equipment health metrics, operational KPIs. HTTPS/TLS 1.2 outbound from PI Web API. | Potentially BCSI — pending formal CIP-011 determination. Operationally sensitive regardless. | Outbound HTTPS permitted on DMZ-FW-01 (rule added without IT Security review per AVEVA PI admin). Historian process account uses a service account credential stored in PI Web API configuration. | (1) Firewall rule added without review — scope may be broader than intended. (2) Service account credentials stored in PI Web API config are plaintext on WJSS-008 — if historian is compromised, Azure credentials are accessible. (3) No log of outbound historian data volume — no anomaly baseline established. | **High** | Marcus Delgado |
| Corporate WAN | Microwave link from WJSS to corporate datacenter; corporate routers and switches | Historian data in transit; TLS-encrypted | Encrypted in transit; TLS 1.2 (not TLS 1.3) | TLS encryption; corporate WAN monitoring | (1) TLS 1.2 is acceptable but TLS 1.3 is preferred; no certificate pinning; if corporate WAN is compromised, a MITM attacker could potentially intercept (though TLS mitigates this). (2) Corporate WAN is shared with IT traffic — no OT traffic isolation at the transport layer. | **Medium** | IT Security |
| Azure Data Factory | Azure Data Factory pipeline (East US 2 region); managed identity | Historian data received, transformed, loaded | OT data in cloud; BCSI determination pending | Managed identity; Azure AD; AES-256 at rest | (1) No IP restriction on Data Factory endpoint — accessible from any internet IP with valid authentication. (2) Managed identity permissions scope has not been reviewed by Lone Star IT Security — scope of Azure resource access is unknown. (3) No Lone Star IT Security review of Azure Data Factory configuration was performed at setup. | **High** | IT Security |
| Azure Data Lake Storage + Power BI | ADLS Gen2 storage account; Power BI workspace; 14 user accounts | Historical and near-real-time OT telemetry | OT operational data; BCSI determination pending | Azure AD access control; AES-256 encryption; TLS in transit | (1) 14 user accounts — MFA status unverified for all accounts. (2) No IP restriction; data accessible from any internet-connected device with valid credentials. (3) No formal data retention policy — data accumulating at 30-second granularity indefinitely. (4) Power BI row-level security not configured — all 14 users see all data. (5) No Lone Star IT Security access review performed. | **High** | IT Security |

> [REASONING]
> The highest-risk segment is not the OT source — it is the cloud storage segment. This seems counterintuitive. Shouldn't the OT side be the focus of an OT security review?
>
> The answer is that the OT historian itself is relatively well-controlled: it is on a network-isolated Control LAN, physical access to the P&C room is badge-controlled, and the historian's outbound connectivity is limited to the corporate WAN path. The cloud segment is the opposite: it is accessible from any internet-connected device with valid credentials, those credentials have not been reviewed, MFA may not be enforced, and the data retention is indefinite.
>
> The attack path that keeps Marcus Delgado awake at night is not "attacker compromises historian to reach Azure." It is "attacker compromises a Power BI user account via phishing, logs into Azure from a coffee shop, and downloads 90 days of real-time switching state data for Waco Junction." That is a straightforward credential theft attack — no OT knowledge required — and the result is a detailed operational picture of a 345 kV substation available to whoever bought or stole those credentials.
>
> The service account credentials gap at the OT Source segment is also significant. Plaintext credentials in the PI Web API configuration on WJSS-008 mean that an attacker who gains access to the historian (via CVE-2024-LST-0047, for example) also gains the Azure authentication credentials. This creates a chained attack path: historian compromise → steal Azure credentials → access cloud data. Document this explicitly.

---

## Part 2: Reverse-Path Analysis

| Question | Assessment |
|----------|-----------|
| Does WJSS-008 accept inbound connections from the IT network or Azure? | PI Web API is configured for outbound connections only — the historian initiates the session to Azure Data Factory; Azure cannot initiate a session back to the historian under the current configuration. However, this is a configuration assumption, not a hardware guarantee. |
| Is the firewall rule at DMZ-FW-01 outbound-only? | The rule added by the AVEVA PI admin was reviewed by Marcus Delgado during the retroactive assessment. The rule permits outbound HTTPS (TCP 443) from WJSS-008 source IP to Azure Data Factory destination IP. The rule includes `permit established` for return traffic (necessary for TCP session completion). The rule does NOT permit new inbound connections from Azure to the OT network. This was the most important finding from the firewall rule review — the rule is more specific than feared. |
| Could a compromised Azure managed identity initiate a connection toward the historian? | No — the managed identity has Azure-internal permissions only. It cannot initiate outbound connections to non-Azure endpoints. This is an Azure architecture constraint, not a Lone Star control. |
| Is a hardware data diode implemented? | No. The connection uses bidirectional TCP (with ACL rules limiting inbound connections). A hardware data diode would provide absolute architectural assurance against reverse-path exploitation but is not currently implemented. |

> [REASONING]
> The firewall rule review finding (rule is more specific than feared) is a meaningful positive finding in this retroactive assessment. The compliance team's concern was that the rule was added carelessly and might be overly broad. A rule like `permit any any https` would be a critical gap. A rule that permits only outbound TCP 443 from the specific historian IP to the specific Azure endpoint is meaningfully more limited.
>
> The `permit established` clause warrants explanation for non-network practitioners: TCP requires return traffic for the session to function (the three-way handshake). `permit established` permits return packets for sessions *initiated from the inside* — it does not allow new connections to be initiated from outside. This is standard firewall behavior and does not create a reverse-path vulnerability for this specific rule. It would be worth having the IT Security team formally document this review in the approval record.
>
> The absence of a hardware data diode remains a gap. The architectural argument for a data diode here is compelling: the only data that legitimately needs to flow is OT → Azure (historian outbound). No data needs to flow Azure → OT. A data diode would make this architectural guarantee hardware-enforced rather than software-configured. The cost barrier is real (hardware data diodes are $10,000–$50,000 depending on implementation), but the remediation plan should include it as a target state.

---

## Part 3: Threat Scenario

### Narrative

The most realistic attack path using this convergence connection does not start in the OT environment — it starts with a compromised Power BI user account.

A threat actor targeting Lone Star's operational data conducts a spearphishing campaign against Lone Star employees with access to grid operational dashboards. One of the 14 Power BI users falls for a credential harvesting attack. The attacker logs into the Azure AD tenant using the stolen credentials. Because MFA is not enforced on this account (status currently unverified), no second factor is required.

From the Azure AD session, the attacker accesses the Power BI workspace and downloads 90 days of historian data: real-time switching state for all 345 kV breakers at Waco Junction, equipment health metrics, and operational KPIs. This data provides a detailed operational picture of how Lone Star operates, including switching patterns, maintenance windows (inferred from breaker state changes), and any anomalous equipment health trends.

In a more sophisticated scenario, the attacker also accesses the Azure Data Factory configuration and retrieves the managed identity permissions — discovering that the managed identity has access to the ADLS storage account. If the managed identity has broader Azure permissions than intended (gap: not reviewed), the attacker may discover additional resources.

The attacker does not need to reach the OT environment to cause harm. The operational intelligence gathered from the cloud is sufficient to plan a more targeted subsequent attack.

### ATT&CK for ICS Mapping

| Stage | Tactic | Technique | ID | Application |
|-------|--------|-----------|-----|-------------|
| 1 | Initial Access | Phishing | T0817 | Credential theft against Power BI user accounts via spearphishing |
| 2 | Collection | Data from Information Repositories | T0811 | Download of OT telemetry from Azure Data Lake |
| 3 | Discovery | Remote System Discovery | T0846 | Analysis of telemetry data to map substation operational state and patterns |
| 4 | Impact (if escalated) | Manipulation of View | T0832 | If attacker achieves write access to ADLS, could inject false data into historian replication, corrupting dashboard data seen by operators |
| 5 | Lateral Movement (if further escalated) | — | — | From corporate Azure AD session, attacker may discover corporate LAN resources; cloud → corporate pivot attempt. This is where OT network access becomes a theoretical risk — but corporate LAN to OT LAN traversal requires compromising WJSS-007, which is separately controlled. |

### Adversary Stopping Points

| Stage | Control | Effectiveness |
|-------|---------|--------------|
| Cloud credential theft | Azure AD MFA (if enforced) | **Unknown — MFA status not verified for all 14 accounts; this is the priority gap** |
| Cloud data access | Azure AD access control | Medium — controls are in place but scope has not been reviewed |
| Corporate-to-OT pivot | DMZ-FW-01 and DMZ-FW-02 firewall rules; WJSS-007 ACLs | Medium-High — separate from the historian path; not directly accessible via Azure |
| Reverse path to historian | Firewall rule verified as outbound-only (see Part 2) | High — rule review confirmed no inbound path from Azure to historian |

> [REASONING]
> Mapping the threat scenario to ATT&CK techniques is not an academic exercise. It forces specificity about what the attacker can do, what controls stop them, and where the gaps are. The natural human tendency in risk documentation is to describe a vague "attacker" doing vague "bad things." The ATT&CK mapping disciplines the analysis: what specific technique is being used, what tool does the attacker need, and what control in our environment would block or detect it?
>
> The T0832 (Manipulation of View) entry at stage 4 is a scenario worth calling out specifically to the CISO and Operations team. If an attacker with Azure write access to the ADLS can inject false data into the historian replication stream, the Power BI dashboards that executives and Operations managers are relying on could show incorrect data. This does not affect the control system — the historian is read-only from the OT side for this purpose — but it could affect decisions made by management based on what they see on the dashboard. This is a meaningful operational risk that the business unit did not consider when they stood up this connection.

---

## Part 4: CIP-011 BCSI Determination

| Question | Assessment |
|----------|-----------|
| Does this data include information about BES Cyber System configuration or operational state? | **Yes.** Real-time switching state data for WJSS-003, WJSS-005, WJSS-006 (protective relays) and WJSS-004 (SAC) is included in the historian telemetry. This is information about the operational state of Medium impact BES Cyber System assets. |
| Could this data facilitate unauthorized access? | **Yes.** Switching state data reveals which breakers are open/closed at any given time. Combined with protection trip data (also in the historian), an attacker could determine optimal timing for a physical or cyber attack against the substation, identify when equipment is in an anomalous state, and infer maintenance windows. |
| **BCSI determination** | **BCSI — Lone Star's OT telemetry from WJSS is BES Cyber System Information per CIP-011.** |
| Are CIP-011 access controls met by current Azure configuration? | **No.** CIP-011 requires that BCSI be protected with access controls that are at least as rigorous as those required for the BES Cyber System from which the information was derived. Current Azure controls: AD access for 14 users (MFA unverified), no IP restriction, no formal access recertification. These do not meet the CIP-011 standard for Medium impact BCSI. |
| Remediation plan | (1) Restrict ADLS access to specifically authorized personnel with documented justification. (2) Verify and enforce MFA for all 14 accounts. (3) Implement IP restriction limiting Azure access to Lone Star corporate IP ranges. (4) Conduct annual access recertification. (5) Document BCSI classification in CIP-011 data register. Timeline: 30 days for MFA verification; 60 days for IP restriction and access list formalization. |

> [REASONING]
> The BCSI determination is the finding that creates the most urgency in this retroactive review. Real-time switching state data from a 345 kV substation is exactly the kind of information CIP-011 was designed to protect. The fact that it is now in Azure with 14 users and no IP restriction is not a catastrophe — the data is encrypted, it is in an access-controlled system, and it does not include control system architecture details — but it does not meet the standard Lone Star has committed to in its CIP-011 program.
>
> The compliance question Priya Nair must answer is: does this rise to the level of a CIP self-report? The factors: (1) BCSI was outside the ESB without required access controls for approximately 90 days; (2) no evidence of unauthorized access; (3) the gap was discovered and is being remediated. A reasonable analysis would conclude this is a self-report candidate under CIP-011, but the specific determination depends on the severity of the access control gap and how Lone Star's CIP-011 program defines "protected." Priya should conduct a self-report evaluation within 5 business days of this finding and document the conclusion either way.

---

## Retroactive Finding: Policy Violation Documentation

### Finding Language

**Finding ID:** POL-VIOL-2024-003
**Standard:** Lone Star IT/OT Convergence Governance Policy (POL-OT-CONV-001), Section 4 (Prohibited Connection Patterns — Shadow IT)
**Finding classification:** Policy Violation — Category 2 (per Section 7.1)

**Description:** The AVEVA PI historian at Waco Junction Substation (WJSS-008) was connected to the corporate network and Azure cloud services in Q1 by the Operations Analytics team and the AVEVA PI system administrator without IT/OT Security review or CISO approval. The connection has been operational for approximately 90 days. During this period, real-time SCADA telemetry from Medium impact BES Cyber System assets was replicated to an Azure Data Lake with access controls that do not meet Lone Star's requirements for BCSI protection under CIP-011.

**How this happened:** The Operations Analytics team framed the project as a data analytics initiative and engaged IT, not OT Security. The AVEVA PI admin, reporting to Operations rather than IT Security, configured the outbound connection and added the firewall rule without routing through a security review. No single person in the process understood the full picture: Operations Analytics saw a data project; IT saw a cloud integration; the PI admin saw a configuration task. OT Security and Compliance were not in the review chain.

**What this is not:** This is not evidence of malicious intent by any of the parties involved. It is evidence of a governance gap — the organization did not have a clear policy or workflow that would have caught this before the connection was enabled. The retroactive review is the appropriate response.

**Remediation required:**
1. Complete the retroactive approval process (this document) — 30 days
2. Remediate cloud security gaps per Part 4 BCSI plan — 30–60 days
3. Amend governance policy to require OT Security notification when PI admin makes any network connectivity change — 30 days
4. Brief Operations Analytics team on IT/OT convergence governance requirements — 30 days
5. Evaluate CIP-011 self-report obligation — 5 business days

**Retroactive approval:** The connection may remain active during the remediation period, subject to CISO approval. CISO has reviewed this finding summary and authorized continuation pending remediation. Authorized by: Jennifer Wu, CISO, _(date)_.

> [REASONING]
> The retroactive finding language must be honest but not gratuitously punitive. The goal is to create a record that shows the organization discovered the issue, assessed it correctly, and remediated it — not to create a document that assigns blame or reads like an indictment.
>
> The "how this happened" section is important. Auditors and post-incident reviewers want to understand root cause, not just what happened. If the root cause was "no clear governance policy or workflow existed to catch this," that is an honest answer that also points toward a systemic fix. If the root cause was "the PI admin knowingly bypassed security review," that requires a different response. In this scenario, the root cause is organizational — a governance gap, not a bad actor.
>
> The self-report evaluation is mandatory to document. Even if Priya Nair concludes that a self-report is not required, the conclusion should be documented. "We considered whether this requires a CIP self-report and concluded it does not because [specific reasoning]" is a far stronger position than "nobody thought to ask."

---

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | _[signed]_ | 2024-10-28 |
| IT Security Lead | Raj Okonkwo | _[signed]_ | 2024-10-28 |
| Compliance Analyst | Priya Nair | _[signed]_ | 2024-10-28 |
| CISO | Jennifer Wu | _[signed]_ | 2024-10-29 |
