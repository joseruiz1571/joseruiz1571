# OT Vulnerability Risk Acceptance Form — COMPLETED
## Lone Star Transmission Services, LLC

**Document ID:** RA-WJSS-2024-001
**Asset:** WJSS-001 — EcoStruxure GridAdvance HMI
**CVE / Vulnerability Reference:** CVE-2024-LST-0047
**Prepared by:** Marcus Delgado, OT Security Lead
**Date Prepared:** October 14, 2024
**Review Date:** October 14, 2025 (or when vendor patch v6.2.1 is released — whichever is sooner)
**Status:** ☑ Approved

---

> **Purpose of this form:** To formally document the organizational decision to accept the risk of a known, unpatched vulnerability in an OT/ICS asset when patching within the standard CIP-007 R2 timeframe is operationally or technically infeasible. This form is a NERC CIP-007 R2.2 mitigation plan and an entry in Lone Star's enterprise risk register.
>
> This is not a "get out of jail free" document. It commits the organization to specific compensating controls, a review cadence, and a remediation timeline.

---

## Section 1: Asset and Vulnerability Identification

| Field | Detail |
|-------|--------|
| **Asset ID** | WJSS-001 |
| **Asset Name** | Schneider Electric EcoStruxure GridAdvance HMI |
| **Asset Classification (CIP-002)** | Medium |
| **Location** | Waco Junction Substation — Protection and Control Room |
| **Asset Function** | Primary operator interface for WJSS; provides real-time SCADA monitoring and manual switching control for all 345 kV assets at Waco Junction |
| **CVE / Vulnerability ID** | CVE-2024-LST-0047 |
| **CVSS v3.1 Score** | 8.1 (High) |
| **CVSS Vector** | AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L |
| **Vulnerability Summary** | Memory corruption vulnerability in the EcoStruxure GridAdvance HMI's DNP3 Application Layer parsing library. An unauthenticated attacker on the same network segment can send a crafted malformed DNP3 packet to trigger a heap overflow, redirecting execution to attacker-controlled code. Successful exploitation yields a session with local administrator-equivalent privileges. |
| **Affected Versions** | EcoStruxure GridAdvance v5.0 through v6.2.0 |
| **Vendor Acknowledgment** | Yes — Schneider Electric Security Advisory SEVD-2024-LST-003 |
| **Vendor Patch ETA** | Firmware v6.2.1 — approximately 18 months from CVE disclosure (April 2026 estimate) |
| **Date CVE First Identified** | September 27, 2024 (date Lone Star received CISA advisory) |
| **Days Since Identification** | 47 days as of preparation date — exceeds CIP-007 R2 35-day mitigation plan threshold |

### 1a. Why Patching Is Not Possible at This Time

| Constraint | Detail |
|------------|--------|
| **Maintenance window requirement** | Applying the firmware patch requires a minimum 72-hour planned maintenance window: take HMI offline, apply update, perform functional verification testing, restore to service. The next approved maintenance window at WJSS is Q3 2025 (approximately 6 months from this acceptance date). No unscheduled outage window is available — unplanned SCADA outages at a 345 kV substation require ERCOT notification and create operational risk. |
| **Vendor restriction** | Schneider Electric's EcoStruxure GridAdvance support agreement explicitly prohibits application of patches not released by Schneider. Applying any unofficial patch voids the hardware and software support contract. Without vendor support, any subsequent system failure becomes a full-cost emergency replacement with no manufacturer assistance. |
| **No patch available** | Vendor patch v6.2.1 is not yet released. The only available remediation is the vendor's forthcoming patch. Independent patch development is not possible without voiding support. |
| **Test environment gap** | Lone Star does not operate a duplicate HMI environment for pre-deployment testing. Schneider is providing a test image environment, but that cannot be completed until the patch exists. |

---

## Section 2: Threat Scenario Description

### 2a. Threat Actor Profile

| Actor Type | Capability | Likelihood of Targeting This Asset | Basis for Assessment |
|------------|-----------|-----------------------------------|---------------------|
| Nation-state / ICS-capable | High — documented ICS exploitation capability, including DNP3 protocol expertise | Medium — US transmission infrastructure is a documented target category; WJSS is not individually high-profile, but transmission SCADA is a class of target | CISA AA22-083A; VOLT TYPHOON advisory; documented campaigns against US electric sector |
| Insider threat (disgruntled employee or malicious contractor) | Medium — insider with substation LAN access would not need advanced capability (AC:L) | Low-Medium — organization has no known insider threat indicators; disgruntled employee with substation access represents the lowest-sophistication viable attack path | AC:L in CVSS vector means low complexity for adjacent attackers; personnel vetting program mitigates but does not eliminate |
| Opportunistic attacker | Low — adjacent network access (AV:A) eliminates internet-facing exploitation | Low — CVE is not internet-exploitable; attacker must be on the substation LAN segment | AV:A vector substantially limits opportunistic attackers; network segmentation is the primary mitigating control |

### 2b. Attack Path Description

**Step 1 — Initial Access:** The attacker must achieve network adjacency to the substation Control LAN. The most plausible paths are: (a) compromise of a vendor remote access session (Relay Logic Partners or Schneider support) with MFA bypass or credential theft; (b) lateral movement from the corporate WAN through WJSS-007 (the IT/OT boundary switch) following a corporate network compromise; (c) physical access to the substation P&C room, which requires bypassing badge-and-PIN physical access controls. Option (b) is the highest-probability path for a sophisticated attacker given the historian replication path from the SCADA LAN to the corporate WAN.

**Step 2 — Vulnerability Exploitation:** Once on the Control LAN, the attacker crafts a malformed DNP3 Application Layer packet addressed to WJSS-001 (IP address determinable via substation LAN enumeration or prior OSINT). The packet exploits the heap overflow in the EcoStruxure GridAdvance parsing library. The exploit does not require credentials and succeeds against all v5.0–6.2.0 versions on first attempt given AC:L complexity. Post-exploitation, the attacker has a session running as a local administrator equivalent on the HMI operating system.

**Step 3 — Post-Exploitation Impact:** With local admin access on WJSS-001, the attacker can: (1) access all SCADA telemetry displayed on the HMI, including real-time 345 kV switching state; (2) modify the HMI display to present false operational data to operators — this is the operationally dangerous scenario because operators may take switching actions based on false state information; (3) attempt to issue unauthorized switching commands through the HMI's SCADA interface to WJSS-002 (data concentrator) and onward to field devices; (4) use the HMI's established network sessions to pivot to WJSS-002 or WJSS-007.

### 2c. MITRE ATT&CK for ICS Technique Mapping

| Tactic | Technique | ID | Relevance |
|--------|-----------|-----|-----------|
| Initial Access | Exploit Public-Facing Application | T0819 | Attacker exploits CVE-2024-LST-0047 via adjacent network; the "public-facing" element is the adjacent LAN exposure of the HMI's DNP3 parsing service |
| Execution | Exploit of Remote Services | T0866 | DNP3 packet crafted to trigger the parsing vulnerability; no user interaction required |
| Persistence | Modify Program | T0889 | Post-exploitation: attacker could modify HMI application binaries to maintain access across restarts; relevant given vendor patch will eventually require deployment |
| Discovery | Remote System Discovery | T0846 | Attacker enumerates SCADA LAN from compromised HMI to identify WJSS-002, relay IP addresses, and IT/OT boundary switch |
| Lateral Movement | Lateral Tool Transfer | T0867 | Attacker transfers tooling from HMI to data concentrator or other LAN assets using HMI's established network sessions |
| Impact | Manipulation of View | T0832 | **Primary concern:** attacker causes the HMI to display false grid state to operators — open breakers shown as closed, fault alarms suppressed, load readings falsified |
| Impact | Unauthorized Command Message | T0855 | **Secondary concern:** attacker uses HMI's SCADA protocol interface to issue unauthorized breaker trip/close commands to WJSS-002 |

### 2d. Blast Radius Assessment

| Impact Category | Assessment | Notes |
|----------------|------------|-------|
| **Operator visibility** | High | Loss of HMI or HMI compromise eliminates operators' primary interface; operators would be working blind on a 345 kV substation until remote SCADA access confirmed functional |
| **Control capability** | High | Compromised HMI could issue unauthorized switching commands via SCADA interface to data concentrator |
| **Lateral movement potential** | Medium | HMI has LAN connectivity to WJSS-002 (data concentrator) and WJSS-007 (IT/OT boundary switch); both are reachable from a compromised HMI session |
| **Data exfiltration** | Medium | Real-time SCADA telemetry accessible; historical data accessible; ERCOT data link state accessible — this is operationally sensitive information |
| **Grid reliability impact** | Medium | Worst case: operator acts on falsified display state and creates a dangerous switching configuration; protective relays would operate independently to clear faults, but the operator-induced switching error itself could create a contingency |

---

## Section 3: Current Compensating Controls in Place

| Control | Description | How It Mitigates CVE-2024-LST-0047 | Implementation Date | Owner |
|---------|-------------|-----------------------------------|--------------------|----|
| Network segmentation — SCADA LAN isolation | SCADA LAN at WJSS is not directly routable from the internet; all external access must traverse the corporate WAN and pass through WJSS-007 (boundary switch) and DMZ firewall rules | Restricts attacker adjacent network access to the pool of devices/personnel with network access to the SCADA LAN segment; eliminates opportunistic internet-based exploitation (AV:A risk is contained) | 2016 (OT DMZ deployment) | Marcus Delgado |
| Individual account authentication on HMI | WJSS-001 login requires individual named user credentials; no shared accounts; local administrator account is disabled for interactive use | Post-exploitation control — attacker who achieves code execution via CVE still operates under the HMI process user context; does not prevent the CVE from being triggered, but limits what lateral movement is possible using cached credentials | 2021 (account hygiene review) | Marcus Delgado |
| Vendor remote access MFA enforcement | All remote access sessions to the substation network via corporate VPN require Cisco Duo MFA in addition to credentials | Reduces probability that attacker achieves initial access via compromised vendor credentials — one of the primary paths to network adjacency | 2022 (MFA deployment) | IT Security |
| Session logging — vendor remote access jump server | All vendor remote access sessions are logged at the corporate jump server including session duration, source IP, and activity summary | Detection control — does not prevent exploitation but reduces dwell time if exploitation occurs via the vendor access path | 2023 | IT Security |
| Physical access control — P&C room | WJSS P&C room requires badge plus PIN for entry; visitor escort required; no tailgating; access log maintained | Prevents attacker from achieving network adjacency via physical substation access without bypassing two independent physical controls | 2018 (substation security upgrade) | Scott Akers |
| Network traffic monitoring — anomalous DNP3 detection | Dragos platform monitors for anomalous DNP3 traffic patterns on substation LAN, including unexpected sources and malformed packet signatures | Detection control — Dragos anomaly detection would flag malformed DNP3 packets consistent with CVE exploitation; does not prevent the first exploit attempt but enables rapid response | 2023 | Marcus Delgado |

### 3a. Controls Considered But Not Implemented

| Control Considered | Reason Not Implemented |
|-------------------|----------------------|
| VLAN isolation — HMI on dedicated micro-segment | The current managed switch (WJSS-007) does not support VLAN segmentation at the required granularity without a firmware upgrade. The firmware upgrade itself requires a maintenance window. Planned for Q3 maintenance window as an architectural improvement — see Section 6. |
| Application whitelisting on HMI | EcoStruxure GridAdvance v5.4.2 does not support third-party application control tools; Schneider's support agreement prohibits installation of unauthorized software on the HMI. This control is not available until after the v6.2.1 patch is applied and Schneider confirms compatibility. |
| Emergency patch via Schneider emergency support | Schneider does not offer an emergency patching program for this CVE at this time. The v6.2.1 patch is the only available remediation. A Schneider representative confirmed this in writing on October 9, 2024 (correspondence on file). |
| DNP3 Secure Authentication v5 (DNP3 SAv5) | Implementing DNP3 SAv5 authentication would require firmware updates on all relays and SCADA infrastructure — a scope far exceeding this single CVE. This is a long-term architectural improvement item, not a compensating control for this specific vulnerability. |

---

## Section 4: Residual Risk Assessment

### 4a. Likelihood Assessment

| Factor | Assessment | Rationale |
|--------|-----------|----------|
| Threat actor capability | High | Nation-state actors with documented ICS capability represent the worst-case scenario; DNP3 exploitation is a documented capability. Insider/opportunistic scenarios are lower capability but not zero. |
| Attacker access to adjacent network | Low-Medium | Network segmentation and MFA on remote access reduce the pool of potential attackers significantly. An internet-based attacker cannot directly exploit this CVE. A nation-state actor would need to traverse corporate network or vendor access path first. |
| Ease of exploitation (CVSS AC) | Low complexity | This is fixed by the CVE characteristics — AC:L means any attacker who achieves adjacency has a straightforward exploitation path. |
| Detection likelihood before impact | Medium | Dragos monitoring provides anomalous DNP3 detection. However, a sophisticated attacker could potentially craft packets that avoid signature-based detection. Detection is not guaranteed. |
| **Overall Residual Likelihood** | **Medium** | Network segmentation and MFA substantially reduce the likelihood compared to inherent risk, but the detection gap and the potential corporate-WAN-to-SCADA-LAN pivot path prevent assessment below Medium. |

### 4b. Impact Assessment

| Factor | Assessment | Rationale |
|--------|-----------|----------|
| Confidentiality impact | High | SCADA telemetry, real-time switching state, and ERCOT data link information are all accessible from a compromised HMI; this is operationally sensitive data under CIP-011 BCSI classification |
| Integrity impact | High | HMI display manipulation is the most operationally dangerous impact; an operator acting on falsified state information could create a grid contingency |
| Availability impact | Low-Medium | Loss of HMI creates a 345 kV substation operating blind; however, protective relay function continues independently; operators can fall back to remote SCADA via corporate WAN if necessary |
| BES reliability impact | Medium | Worst-case: unauthorized switching commands via HMI could de-energize 345 kV transmission segments serving approximately 180,000 customers per ERCOT load flow analysis; protective relays would continue to operate but cannot prevent operator-initiated or attacker-initiated switching errors |
| **Overall Residual Impact** | **High** | Integrity impact (display manipulation) and the potential for unauthorized switching commands constitute a High impact scenario if exploitation occurs |

### 4c. Residual Risk Matrix

|  | **Low Impact** | **Medium Impact** | **High Impact** |
|--|---|---|---|
| **Low Likelihood** | Low | Low-Medium | Medium |
| **Medium Likelihood** | Low-Medium | Medium | **Medium-High** |
| **High Likelihood** | Medium | Medium-High | High |

**Residual Risk Rating: Medium-High**

This rating reflects the combination of Medium likelihood (substantially reduced by compensating controls) and High impact (HMI manipulation at a 345 kV substation). The risk is not acceptable on a permanent basis — it is accepted conditionally pending vendor patch availability, with explicit trip wires for reassessment.

---

## Section 5: Business Justification for Acceptance

**Why acceptance is the appropriate decision:**

The three independent constraints documented in Section 1a are not theoretical — they are the operational reality of this substation. Taking WJSS-001 offline requires a 72-hour maintenance window because the station has no standby HMI and no process for operating the 345 kV substation without local monitoring and control access for an extended period. Unplanned outages at this station require ERCOT notification under tariff requirements and create compounding reliability risk during the outage window.

The alternative most people ask about — "can you just apply a patch anyway and risk the support contract?" — has been evaluated. The support contract risk is not abstract. The HMI hardware has 4 years of remaining useful life on its capital plan. If the system fails after an unauthorized patch and vendor support is void, Lone Star would bear the full cost of emergency replacement at a live 345 kV substation, with no vendor assistance, and without the approved capital budget to do so. The organization would be trading a managed, monitored cyber risk for an unmanaged operational and financial risk.

Acceptance with compensating controls is the appropriate decision. The compensating controls in Section 3 are not nominal — they represent meaningful reduction in the likelihood that the vulnerability is exploited during the acceptance period. Network segmentation is the primary mitigating control: an internet-based attacker cannot trigger this CVE. MFA enforcement and session logging substantially reduce the vendor access pivot scenario. The Dragos DNP3 anomaly detection provides a detection layer that would not exist without this assessment process.

**Alternatives evaluated:**

| Alternative | Why Rejected |
|-------------|-------------|
| Patch now with unofficial patch | Voids Schneider support agreement; no test environment; would require a maintenance window anyway; risk of system instability on a production OT asset without vendor backup |
| Replace the asset immediately | Capital plan does not include HMI replacement for 4 years; replacement still requires a 72-hour maintenance window; no approved budget; replacement asset would also require CIP re-evaluation |
| Take the asset offline pending vendor patch | Loss of HMI creates full operational blindness at WJSS 345 kV substation; operators cannot safely manage the substation without local monitoring; this creates a larger operational risk than accepting the cyber risk with compensating controls in place |
| Accept with no compensating controls | Not acceptable; compensating controls in Section 3 are a precondition for this acceptance; they are active and verified, not planned |

---

## Section 6: Conditions That Would Trigger Reassessment

| Trigger | Action Required |
|---------|----------------|
| Vendor patch v6.2.1 becomes available | Patch must be tested and deployed within the next available maintenance window, not to exceed 90 days from patch availability. Marcus Delgado is responsible for monitoring Schneider advisory for patch release. |
| Evidence of active exploitation of CVE-2024-LST-0047 in the wild | Escalate to CISO within 24 hours of ICS-CERT advisory or peer utility notification. Convene emergency risk review within 48 hours. Evaluate whether emergency maintenance window can be justified by the increased threat level. |
| Change in network architecture that increases HMI exposure | Any new connectivity to WJSS-001, any changes to DMZ firewall rules affecting the substation LAN, or any new vendor access paths must trigger re-evaluation of this acceptance. |
| WJSS-007 VLAN segmentation implemented | When HMI is isolated on its own VLAN (planned Q3 2025), re-evaluate likelihood rating — network segmentation improvement may reduce residual risk rating from Medium-High to Medium. |
| Maintenance window becomes available earlier than Q3 2025 | Operations Manager must notify OT Security Lead; patching opportunity will be re-evaluated. |
| NERC CIP audit finding related to this vulnerability | Escalate to CISO; review whether this risk acceptance document is sufficient as CIP-007 R2.2 evidence. |
| Expiration without patch deployment | Risk acceptance expires October 14, 2025. If the vendor patch has not been deployed by that date, this form must be re-reviewed and re-approved. Automatic extension is not permitted. |

**Review Date:** October 14, 2025
**Responsible Party for Triggering Review:** Marcus Delgado, OT Security Lead

---

## Section 7: Approval Signatures and Review Date

By signing below, each approver acknowledges:
- They have reviewed this risk acceptance form and the compensating controls documentation
- They understand the residual risk as described in Section 4 (Medium-High)
- They authorize acceptance of this risk for the period indicated
- They understand that this authorization does not relieve the organization of its obligation to remediate the vulnerability when the vendor patch is available

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | *[signed]* | October 14, 2024 |
| Operations Manager | Scott Akers | *[signed]* | October 16, 2024 |
| CISO | Jennifer Wu | *[signed]* | October 17, 2024 |

**Risk Acceptance Valid Through:** October 14, 2025
**Next Mandatory Review Date:** October 14, 2025
**CIP-007 R2.2 Mitigation Plan Reference:** RA-WJSS-2024-001 (this document)
