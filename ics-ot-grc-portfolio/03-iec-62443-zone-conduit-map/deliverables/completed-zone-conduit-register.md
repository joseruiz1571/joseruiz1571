# Zone and Conduit Register — COMPLETED
## IEC 62443-3-2 — Waco Junction Substation

**Organization:** Lone Star Transmission Services, LLC
**Facility:** Waco Junction Substation (WJSS)
**Prepared by:** Marcus Delgado, OT Security Lead
**Reviewed by:** Diana Flores, Substation Engineering Lead
**Review date:** March 1, 2026
**Contract reference:** Capital project — P&C Infrastructure Upgrade (Contract #LST-2026-PP-007)
**IEC 62443 revision basis:** IEC 62443-3-2:2020 (Risk assessment), IEC 62443-3-3:2013 (System requirements)

---

## Part 1: Zone Register

| Zone ID | Zone Name | Assets Included | Required Security Level | Justification | Gap Notes |
|---------|-----------|----------------|------------------------|---------------|-----------|
| Z-01 | Corporate IT Zone | Corporate workstations, email systems, IT-managed network infrastructure, enterprise data lake access point, corporate VPN concentrator | SL-1 | Corporate IT assets have no direct BES control function. Compromise affects business operations but not substation control on its own. Standard enterprise security controls apply. This zone is managed by IT, not OT Security. The SL-1 designation is accurate given the indirect nature of the risk — however, it underscores why the Z-01/Z-02 boundary controls are critical: Z-01 is the highest-likelihood initial access point for a sophisticated attacker targeting OT assets, and the controls at that boundary must reflect the consequence of what lies beyond it, not the consequence of Z-01 itself. | IT security program should be periodically reviewed for adequacy. The historian replication path and vendor remote access VPN both originate from Z-01, making Z-01 a meaningful attack surface even though it is SL-1. |
| Z-02 | OT DMZ Zone | DMZ-FW-01 (IT-side firewall, Cisco ASA 5545-X, 2016), DMZ-FW-02 (Control-side firewall, Cisco ASA 5545-X, 2016), WJSS-007 (IT/OT boundary switch), WJSS-008 (AVEVA PI Historian) | **SL-2** | The DMZ bridges Z-01 (SL-1) and Z-03 (SL-2). A DMZ rated below the zones it bridges becomes the weak link — all traffic entering the OT environment transits Z-02, and if Z-02 is inadequately secured, the higher SL of Z-03 provides no protection. SL-2 is therefore the minimum appropriate assignment. The historian is placed in Z-02 rather than Z-03 because it replicates data outbound to Z-01; placing it in Z-03 would extend the Z-03 boundary to include corporate-WAN-connected traffic flows. Note: the as-built 2016 DMZ does not fully satisfy SL-2 Foundational Requirements — specifically, the absence of a hardware data diode is a gap. See gap notes. | **Gap 1:** DMZ firewalls implement permit/deny ACL rules but do not enforce hardware-level unidirectionality. Historian replication creates a bidirectional protocol-layer path between Z-01 and Z-03 without a data diode. An attacker who compromises the Azure endpoint could potentially craft traffic that reaches the historian. **Gap 2:** DMZ firewall firmware patched quarterly, not on emergency basis for active CVEs. **Remediation:** Evaluate hardware data diode (Waterfall Security or similar) for historian outbound path. Estimated capital cost and implementation in remediation backlog. |
| Z-03 | Control Zone | WJSS-001 (EcoStruxure GridAdvance HMI), WJSS-002 (SCADA Data Concentrator), WJSS-004 (Substation Automation Controller) | **SL-2** | Z-03 contains the primary SCADA monitoring, control, and automation assets for Waco Junction. The consequence of compromise for this zone is High — compromise of the HMI enables display manipulation and unauthorized command issuance; compromise of the data concentrator disrupts SCADA telemetry; compromise of the SAC could trigger unauthorized automatic breaker operations. SL-2 is the minimum appropriate level for transmission SCADA: it assumes intentional attackers using standard means and commercially available tools, which is consistent with the documented threat actor profile for US electric sector targets. SL-3 was evaluated and declined for Z-03 as a whole (see Security Level Justification for Z-03 in this deliverables package) — the argument for SL-3 is strong but the compensating control profile and the practical difficulty of achieving SL-3 system requirements on 2014-vintage HMI hardware without vendor support led to SL-2 as the target with SL-3 aspirational for the next capital refresh. **EWS-001 note:** The Engineering Workstation (EWS-001) is assigned to Z-05 rather than Z-03. See Z-05 for rationale. | **Gap 1:** Z-03 is a flat Ethernet network — no internal segmentation between HMI, data concentrator, and SAC. A compromised HMI can reach the SAC and data concentrator directly. Lateral movement within Z-03 is unrestricted. **Gap 2:** WJSS-001 is running Windows Embedded Standard 7, which is end-of-life for Microsoft security patches. CIP-007 patch management program documents this with risk acceptance. **Gap 3:** DNP3 protocol between data concentrator and field devices in Z-04 uses DNP3 without Secure Authentication v5 — authentication on the DNP3 session is not enforced. Remediation is a long-term item requiring relay firmware upgrades. |
| Z-04 | Field Device Zone | WJSS-003 (Protective Relay — 345 kV Line 1), WJSS-005 (Protective Relay — 345 kV Line 2), WJSS-006 (Protective Relay — 345 kV Line 3), WJSS-004-IO (Breaker Control I/O — hardwired to SAC) | **SL-2 (Target); current state SL-1 compliant with SL-2 compensating controls** | Z-04 contains assets with direct consequence to 345 kV transmission operations — the protective relays trip breakers on fault detection, and the SAC's hardwired I/O controls the breaker actuator circuits. The consequence of compromise is High for safety (relay manipulation could prevent fault clearing, creating live-equipment hazard for field personnel) and High for operational reliability (nuisance trips or failure-to-trip on a 345 kV circuit has direct BES reliability impact). SL-2 is the assigned target. However, the protective relays run firmware from 2018 and use serial/DNP3 connectivity — they do not support all SL-2 Foundational Requirements natively. Specifically, per-user authentication on relay configuration ports is not available in the current firmware version. The Q3 2026 firmware update (Relay Logic Partners engagement, see Project 04) addresses the unauthorized settings modification vulnerability and includes updated DNP3 library — but does not add per-user authentication at the relay level. Full SL-2 compliance for Z-04 will require the next relay generation. Compensating controls (physical access controls to relay panels, escort requirement for all relay work, Dragos monitoring) address the gap in the interim. | **Gap 1:** Relay firmware does not support per-user authentication; physical access is the primary access control for relay configuration. **Gap 2:** DNP3 SAv5 not implemented on relay-to-data-concentrator sessions. **Gap 3:** Relay firmware versions 3.4 (2018) and 4.2 (2017) — both beyond vendor-recommended update cycle. Firmware update scheduled Q3 2026. |
| Z-05 | Engineering Access Zone | EWS-001 (Engineering Workstation — relay configuration and SAC programming terminal) | **SL-2 (conduit to Z-04 via relay configuration software requires SL-2 boundary controls)** | EWS-001 is isolated in its own zone rather than placed in Z-03 for one reason: it is the terminus of the vendor remote access conduit (C-02). If EWS-001 shared Z-03 with the HMI and SAC, a vendor access compromise would give the attacker unrestricted lateral access to SCADA operations assets. By isolating EWS-001 in Z-05, the blast radius of a vendor access compromise is limited to the engineering workstation and the relay configuration functions accessible from it. The conduit from Z-05 to Z-04 (C-04, relay configuration sessions) is separately controlled and can be disabled when no vendor work is in progress. **Key constraint:** This zone isolation is a design recommendation from this assessment. As of this writing, EWS-001 is physically and logically on the same flat Control LAN as Z-03 assets. Implementing Z-05 requires VLAN segmentation on the Control LAN switch — a configuration change that requires a maintenance window and the Q3 2026 maintenance window is the earliest opportunity. Gap documented accordingly. | **Gap:** Z-05 is a recommended architecture, not current state. EWS-001 currently sits on the same Layer 2 segment as Z-03 assets. The VLAN segmentation required to implement Z-05 has not yet been deployed. Until Q3 2026, the vendor remote access path (C-02) effectively terminates in an undifferentiated Control LAN. This is the most significant architectural gap identified in this assessment. Compensating control: on-site escort for all vendor access sessions; remote access sessions require OT Security Lead approval. |

---

## Part 2: Conduit Register

| Conduit ID | Name | Source Zone | Destination Zone | Protocol/Port | Direction | Assigned SL | Justification | Compensating Controls | Gap Notes |
|------------|------|-------------|-----------------|---------------|-----------|-------------|---------------|-----------------------|-----------|
| C-01 | Corporate-to-DMZ | Z-01 (Corporate IT) | Z-02 (OT DMZ) | HTTPS/443 (historian replication), RDP/3389 (jump server to EWS-001 via DMZ), SNMP/161 (network management) | Bidirectional at ACL level | **SL-2** | This conduit is the primary ingress point for all traffic entering the OT environment from the corporate network. The assigned SL matches the destination zone (Z-02, SL-2). DMZ-FW-01 enforces port-based ACL filtering; only explicitly permitted protocols from permitted source IPs pass. The bidirectional nature of this conduit is a gap — ideally all OT-bound traffic would be inspected before entry, but encrypted RDP sessions and HTTPS traffic cannot be fully inspected at DMZ-FW-01 without SSL inspection capabilities. | DMZ-FW-01 enforces source IP restrictions for RDP sessions (permitted source IPs are the corporate jump server only, not arbitrary corporate LAN endpoints); Cisco Duo MFA required for all VPN sessions before traffic reaches corporate LAN; session logging at jump server | **Gap:** RDP from jump server to EWS-001 is encrypted and cannot be content-inspected at DMZ-FW-01. If the jump server is compromised, malicious payloads could pass through this conduit without inspection. Compensating control: session recording on jump server (implemented 2023). |
| C-02 | Vendor Remote Access | Z-01 (Corporate IT) | Z-05 (Engineering Access Zone) via Z-02 and Z-03 (transit) | Cisco AnyConnect VPN → RDP/3389 (to EWS-001) → Relay config protocol TCP 4999 (from EWS-001 to relays) | Inbound (internet → corporate VPN → Z-05) | **SL-2 (current); SL-3 recommended for this conduit given consequence of compromise** | **Conduit boundary assessment:** This conduit is documented as terminating in Z-05 (EWS-001), not Z-02 (DMZ). The VPN session terminates at the corporate concentrator, then RDP traverses corporate LAN → DMZ → Control LAN to reach EWS-001. DMZ-FW-02 permits RDP from the corporate jump server to EWS-001. The encrypted RDP tunnel provides no meaningful inspection by DMZ-FW-02 — the firewall passes the TCP session but cannot evaluate the payload. Effective terminus is EWS-001 in Z-05 (currently, the flat Control LAN). **SL-2 vs SL-3:** SL-3 is recommended given that a successful compromise of this conduit gives the attacker relay configuration access — including firmware modification capability on 345 kV protective relays. However, implementing SL-3 controls (specifically, hardware-based isolation and privileged access management with session brokering) requires a capital investment that is not in the current budget. SL-2 with enhanced compensating controls is the current position, with SL-3 as the remediation target. | Cisco Duo MFA on VPN; source IP filtering on jump server RDP sessions; session recording at jump server; on-site escort required for all vendor field access; vendor must provide personnel list ≥14 days in advance; OT Security Lead approval required before each remote session | **Gap 1 (Critical):** Conduit effectively bypasses Z-02 DMZ controls via encrypted tunnel. The architectural intent of the DMZ — to inspect and control OT-bound traffic — is not achieved for this conduit. **Gap 2:** Conduit should terminate in Z-02 or Z-05, with a separate, audited session required to reach Z-03 or Z-04. Current architecture extends the conduit to the flat Control LAN. **Remediation:** (1) VLAN segmentation to create Z-05; (2) PAM system (CyberArk or similar) to broker all vendor sessions and prevent direct RDP; (3) Estimated timeline: Q3 2026. |
| C-03 | DMZ-to-Control | Z-02 (OT DMZ) | Z-03 (Control Zone) | SCADA/OPC-DA (historian pull from data concentrator), RDP/3389 (currently permitted as part of jump server path) | Bidirectional | **SL-2** | This conduit is controlled by DMZ-FW-02. SCADA historian data pull is the legitimate business traffic. RDP is permitted for vendor access path (see C-02 architectural gap). The SL matches Z-03 (SL-2). All traffic between Z-02 and Z-03 must pass through DMZ-FW-02. | DMZ-FW-02 enforces port-based ACL; only explicitly permitted traffic passes; firewall rule review semi-annually per governance policy | **Gap:** DMZ-FW-02 rule set has not been reviewed since 2022. Permit rules were added for the historian replication project without IT Security review (see Project 05). A firewall rule review is due and is a tracked remediation action. |
| C-04 | SCADA Polling | Z-03 (Control Zone) | Z-04 (Field Device Zone) | DNP3/TCP 20000 (data concentrator to relays), Hardwired I/O (SAC to breaker circuits) | Bidirectional (poll/response for DNP3); unidirectional hardware (SAC I/O) | **SL-2** | SCADA polling is the primary operational data path — the data concentrator continuously polls each relay for telemetry and sends the results to the HMI. This conduit carries the operational state data that operators rely on for grid management. The hardwired I/O from the SAC to breaker control circuits is not a network conduit in the traditional sense — it is a direct electrical connection — but it is documented here because it represents the highest-consequence data path in the facility: this is where software commands become physical breaker operations. SL-2 reflects the consequence of manipulation on this path. | Dragos platform monitors DNP3 traffic on this segment for protocol anomalies, unexpected sources, and unauthorized polling; physical access to relay panels requires escort; SAC I/O circuits terminate in locked relay panels | **Gap:** DNP3 Secure Authentication v5 not implemented. DNP3 sessions between data concentrator and relays are unauthenticated — a device on the Control LAN could send DNP3 commands that the relay would accept as legitimate. Full mitigation requires SAv5 support in relay firmware and data concentrator — a long-term remediation item. Compensating control: Control LAN is not directly accessible from the internet or corporate LAN without traversing Z-02 controls. |
| C-05 | Engineering Access to Field Devices | Z-05 (Engineering Access Zone) | Z-04 (Field Device Zone) | Relay configuration protocol TCP 4999 (SEL Compass), DNP3 serial via WJSS-002 for legacy relay access | Inbound (EWS-001 to relay configuration ports) | **SL-2 (minimum); SL-3 recommended** | This conduit carries firmware updates and relay protection setting changes — the highest-consequence write operations in the facility. A malicious firmware image delivered via this conduit could disable protection on a 345 kV circuit. SL-3 is the appropriate target given the safety consequence of a relay protection failure. Current state: SL-2 compensating controls (on-site escort, named personnel, hash verification per CIP-013 assessment). Achieving SL-3 formally requires hardware-based session isolation. | Named personnel requirement — all relay engineers must be on approved list; hash verification of all firmware images before deployment; on-site escort for all relay work; firmware backup taken before each update; protection setting verification test before relay returned to service | **Gap:** This conduit should require dual approval for any firmware deployment — a "four-eyes" control to prevent a single compromised vendor engineer from deploying a malicious firmware image without a second witness. Recommended: require both vendor engineer and Lone Star OT engineer to be physically present and sign off on each relay firmware deployment. |

---

## Zone and Conduit Summary Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│  Z-01: Corporate IT Zone (SL-1)                                  │
│  Corporate workstations, VPN concentrator, Azure data lake       │
└────────────────┬─────────────────────────────────────────────────┘
                 │  C-01: Corporate-to-DMZ (SL-2)
                 │  HTTPS/443, RDP/3389, SNMP/161 | DMZ-FW-01
                 ▼
┌──────────────────────────────────────────────────────────────────┐
│  Z-02: OT DMZ Zone (SL-2)                                        │
│  DMZ-FW-01, DMZ-FW-02, WJSS-007 (boundary switch),              │
│  WJSS-008 (AVEVA PI Historian)                                   │
└────────────────┬─────────────────────────────────────────────────┘
                 │  C-03: DMZ-to-Control (SL-2)
                 │  SCADA/OPC-DA, RDP | DMZ-FW-02
                 ▼
┌──────────────────────────────────────────────────────────────────┐
│  Z-03: Control Zone (SL-2)                  Z-05: Eng Zone (SL-2)│
│  WJSS-001 (HMI)                             EWS-001 (Eng WS)     │
│  WJSS-002 (Data Concentrator)               [Z-05 is recommended │
│  WJSS-004 (SAC)                              architecture; VLAN   │
│                                              segmentation pending]│
└────────────────┬──────────────────────────┬─────────────────────┘
                 │  C-04: SCADA Polling      │  C-05: Eng to Field
                 │  DNP3/TCP 20000 +         │  TCP 4999 (relay cfg)
                 │  Hardwired I/O (SAC)      │
                 ▼                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  Z-04: Field Device Zone (SL-2 target; SL-1 current with         │
│         compensating controls)                                   │
│  WJSS-003, WJSS-005, WJSS-006 (protective relays)               │
│  WJSS-004-IO (Breaker control I/O — hardwired to SAC)           │
└──────────────────────────────────────────────────────────────────┘

Vendor Remote Access Path (C-02) — ARCHITECTURAL GAP:
Z-01 → [Cisco AnyConnect VPN] → Corporate LAN → [RDP]
→ DMZ-FW-02 (passes encrypted RDP; cannot inspect) → Z-03/Z-05 flat LAN
Intent: terminate in Z-02 or Z-05 with PAM brokering
Reality: extends to flat Control LAN; DMZ inspection bypassed

Gap Remediation (Q3 2026):
- VLAN segmentation to create Z-05 as separate segment
- PAM system (CyberArk or equivalent) to broker all vendor sessions
- Conduit C-02 terminates at PAM, not directly at EWS-001
```

---

## Architectural Gap Summary

| Gap ID | Zone/Conduit | Description | Risk Level | Remediation | Timeline |
|--------|-------------|-------------|-----------|-------------|---------|
| GAP-01 | Z-02 | No hardware data diode for historian replication; bidirectional firewall rules create potential reverse-path | High | Hardware data diode (Waterfall Security or equivalent) for outbound historian path | Evaluate in next capital budget cycle |
| GAP-02 | C-02 | Vendor remote access conduit bypasses DMZ inspection via encrypted RDP; terminates on flat Control LAN | High | Z-05 VLAN segmentation + PAM session brokering | Q3 2026 maintenance window |
| GAP-03 | Z-03 | Flat Layer 2 network inside Control Zone — no internal segmentation between HMI, data concentrator, and SAC | Medium | Internal VLAN segmentation within Z-03 | Q3 2026 |
| GAP-04 | C-04 | DNP3 Secure Authentication v5 not implemented on polling sessions | Medium | Requires relay firmware upgrade to SAv5-capable version | Next relay generation cycle |
| GAP-05 | C-03 | DMZ-FW-02 rule set not reviewed since 2022; historian replication rules added without IT Security review | Medium | Firewall rule review and clean-up | Q2 2026 |
| GAP-06 | C-05 | No dual-approval ("four-eyes") requirement for relay firmware deployment | Medium | Add named Lone Star OT engineer as required co-signer on relay work sign-off forms | Next CIP-013 contract cycle |

---

## Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | *[signed]* | March 1, 2026 |
| Substation Engineering Lead | Diana Flores | *[signed]* | March 3, 2026 |
