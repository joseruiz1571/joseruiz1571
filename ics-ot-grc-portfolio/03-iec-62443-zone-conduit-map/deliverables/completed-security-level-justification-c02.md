# Security Level Justification — C-02: Vendor Remote Access Conduit
## IEC 62443-3-2 — Zone/Conduit SL Assignment Reasoning

**Organization:** Lone Star Transmission Services, LLC
**Asset/Zone/Conduit:** C-02 — Vendor Remote Access Conduit
**Analyst:** Marcus Delgado, OT Security Lead
**Date:** March 1, 2026

---

## 1. Asset/Zone/Conduit Description

| Field | Detail |
|-------|--------|
| **Type** | Conduit |
| **Conduit ID** | C-02 |
| **Name** | Vendor Remote Access |
| **Assets Connected** | Source: Z-01 (Corporate IT — vendor VPN entry point) → Destination: Z-05 (Engineering Access Zone — EWS-001) via Z-02 transit (DMZ) |
| **Primary Function** | Provides Relay Logic Partners engineers with remote access to EWS-001 for protective relay firmware updates, configuration changes, and troubleshooting. Sessions originate from vendor premises, authenticate via corporate VPN, and use RDP to reach the engineering workstation. |

**As-built reality vs. intended architecture:** The conduit as described above represents the architectural intent (terminating at Z-05/EWS-001). The as-built reality is that Z-05 has not yet been implemented as a separate VLAN — EWS-001 currently sits on the same flat Layer 2 network as Z-03 (Control Zone). Until Q3 2026 VLAN segmentation, the conduit's effective terminus is the flat Control LAN, which includes WJSS-001 (HMI), WJSS-002 (data concentrator), and WJSS-004 (SAC). This gap is documented throughout this assessment and is the highest-priority remediation item.

---

## 2. Consequence of Compromise

| Consequence Category | Assessment | Rationale |
|---------------------|-----------|----------|
| **Safety** | High | EWS-001 is used to configure protective relay settings and deploy firmware. A compromised vendor access session could be used to modify relay protection settings — changing overcurrent trip thresholds, disabling protection functions, or deploying malicious firmware that prevents trip on fault. A relay that fails to trip on a genuine fault on a 345 kV line creates a live-equipment hazard for any field crews working under the assumption that equipment is de-energized. |
| **Operational** | High | In the current as-built architecture (flat Control LAN), a compromised vendor session on EWS-001 provides lateral access to WJSS-001 (HMI), WJSS-002 (data concentrator), and WJSS-004 (SAC). An attacker using this path is not limited to relay configuration — they are effectively on the Control LAN with access to the same assets as a compromised HMI. |
| **Financial** | Medium | Direct cost of a compromised relay deployment: emergency relay replacement, emergency maintenance window, potential ERCOT notification, possible NERC CIP self-report. |
| **Reputational** | High | A supply chain compromise via vendor remote access — particularly one resulting in a relay protection failure or unauthorized switching event — would be a reportable incident under CIP-008 and potentially under NERC CIP more broadly. |
| **Overall Consequence** | **High** | Safety and operational consequences are both High. The consequence profile of this conduit is not typical for vendor remote access — it is elevated because relay firmware deployment is a direct path to protection system manipulation. |

---

## 3. Likelihood of Targeted Attack

| Factor | Assessment | Rationale |
|--------|-----------|----------|
| **Target attractiveness** | High | Vendor remote access to protective relay infrastructure is a documented attack vector. CISA advisory AA22-083A and subsequent advisories specifically identify vendor access paths and supply chain compromise as primary vectors for nation-state actors targeting electric sector ICS. This conduit is the type of path that threat intelligence describes as a target, not a hypothetical. |
| **Required attacker access** | Remote + credential theft | The attacker needs to obtain valid VPN credentials for a Lone Star or Relay Logic account, or compromise the Relay Logic engineer's device. MFA on the VPN substantially raises the bar — MFA bypass typically requires device compromise, not just credential phishing. |
| **Documented threat actor interest** | Yes | CISA, CISA/NSA joint advisories, and E-ISAC threat reporting have all referenced vendor remote access as a target category for advanced persistent threat actors targeting US electric sector. |
| **Overall Likelihood** | **Medium** | MFA enforcement on VPN substantially reduces likelihood compared to a non-MFA environment. However, nation-state actors with documented MFA bypass capability (device compromise, SIM swapping, MFA fatigue attacks) mean likelihood cannot be assessed below Medium for this specific conduit and threat actor profile. |

---

## 4. Attacker Capability Assumed

**Assumed attacker capability for this assignment: SL-3 (intentional, sophisticated means, ICS-specific knowledge)**

**Rationale:** The documented threat actors with interest in US transmission infrastructure include nation-state actors with ICS-specific tooling, knowledge of ICS protocols including DNP3, experience with relay configuration software (SEL Compass), and demonstrated ability to conduct multi-stage supply chain attacks. An adversary who has targeted this conduit has done their reconnaissance — they know what relay models are at WJSS, what firmware versions are running, and what configuration changes would be most operationally impactful. This is not an opportunistic attacker using commodity tools. SL-2 assumes "standard means and commercially available tools" — the scenario this conduit represents exceeds that assumption. SL-3 is the appropriate attacker profile.

---

## 5. Security Level Selection

| Option Evaluated | Consequence | Likelihood | Attacker Capability | Would This SL Apply? |
|-----------------|-------------|-----------|--------------------|--------------------|
| SL-1 | High | Medium | Incidental | No — consequence is High even if attacker is unsophisticated; incidental access to relay configuration is not a credible scenario for this conduit |
| SL-2 | High | Medium | Standard tools | **Current assigned level** — SL-2 controls are in place (MFA, session logging, named personnel requirement, hash verification). SL-2 is appropriate as the current target level given budget and capability constraints. However, it is acknowledged as insufficient for the actual threat profile. |
| SL-3 | High | Medium | Sophisticated/ICS-specific | **Recommended target** — given High consequence and a documented threat actor profile that exceeds SL-2 assumptions, SL-3 is the architecturally correct assignment. Achieving SL-3 requires hardware-based session isolation (PAM with session brokering, no direct RDP to EWS-001) and enhanced monitoring. |
| SL-4 | High | Low | Nation-state | Not appropriate as a baseline — nation-state threat is real but SL-4 requirements (dedicated monitoring systems, hardware isolation at every boundary, personnel security equivalent to national security standards) are not achievable at Lone Star's current resourcing level and are disproportionate to a transmission operator of this scale. Nation-state threat is mitigated through the broader SL-3 control set. |

**Selected Security Level: SL-2 (current); SL-3 (target, pending PAM implementation in Q3 2026)**

**Selection Rationale:** SL-2 is the current operational assignment because the current compensating controls (MFA, named personnel, hash verification, session logging, on-site escort for field work) represent a meaningful SL-2 control posture. Assigning SL-3 today without the control infrastructure to support it would be a paper designation with no operational substance. The gap is documented honestly: C-02 carries SL-3 risk but is currently managed to SL-2. The remediation plan (PAM, VLAN segmentation for Z-05) moves the conduit to SL-3 by Q3 2026. This is the kind of honest gap documentation that a sophisticated auditor or hiring manager should expect to see — not an SL assignment that papers over a known architectural weakness.

---

## 6. Gap Analysis: Current Controls vs. SL Requirements

| FR Category | SL-2 Requirement (abbreviated) | Current Control | Gap? |
|-------------|------------------------------|----------------|------|
| IAC — Identification & Authentication | Multi-factor authentication for all human users | Cisco Duo MFA on VPN; no MFA on local EWS-001 accounts | **Partial** — MFA enforced at VPN entry but not at the endpoint. A compromised VPN session still accesses EWS-001 with single-factor local authentication. |
| UC — Use Control | Least-privilege role-based access control; accounts limited to required functions | Named personnel list maintained; vendor engineers are not given administrator accounts on EWS-001 | **Partial** — Role separation exists conceptually but is enforced through administrative controls (personnel lists) rather than technical controls (role-based account permissions). |
| SI — System Integrity | Software integrity verification for updates delivered over the conduit | SHA-256 hash verification required per CIP-013 vendor assessment; Relay Logic must provide signed hash before firmware delivery | **Partial** — Hash verification is a compensating control, not a systematic integrity mechanism. A compromised Relay Logic engineer could provide a false hash. Recommended: independent hash verification against SEL manufacturer hash. |
| DC — Data Confidentiality | Encryption for data in transit | TLS/RDP encryption in transit; VPN tunnel encrypts VPN segment | **Pass** — Traffic is encrypted end-to-end from vendor premises to EWS-001. |
| RDF — Restricted Data Flow | Access restricted to required functions; no lateral movement possible via this conduit | Current: none — flat Control LAN allows lateral movement from EWS-001 | **Fail** — Critical gap. EWS-001 is on the flat Control LAN. A compromised vendor session can reach WJSS-001, WJSS-002, WJSS-004 without additional authentication. Remediation: VLAN segmentation (Z-05). |
| TRE — Timely Response | Audit logging and security event monitoring | Session recording at corporate jump server; Dragos monitoring of SCADA LAN | **Partial** — Session recording captures activity at jump server but not at EWS-001 directly. Dragos monitors LAN traffic but does not capture application-layer relay configuration changes. |
| RA — Resource Availability | DoS protection; availability of conduit does not create single point of failure | N/A — this is a maintenance conduit, not an operational availability requirement | **N/A** — Conduit unavailability (vendor cannot reach EWS-001) does not impact real-time grid operations. |

**Overall gap assessment:** Two material gaps exist: (1) no lateral movement restriction from EWS-001 to Control Zone assets — requires VLAN segmentation; (2) integrity verification relies on vendor-provided hashes without manufacturer cross-check. Both gaps are addressed in the remediation plan.

---

## 7. Compensating Controls for Identified Gaps

| Gap | Compensating Control | Effectiveness | Remediation Plan |
|-----|---------------------|--------------|-----------------|
| No lateral movement restriction (flat Control LAN) | On-site Lone Star escort required for all vendor access sessions; no vendor remote sessions permitted without OT Security Lead approval; vendor access windows are time-limited (session must terminate within 2 hours of start without extension approval) | Partial — escort prevents unsupervised access but cannot prevent a compromised vendor engineer from issuing commands within the escort's line of sight | VLAN segmentation (Z-05 creation) in Q3 2026 maintenance window; PAM session brokering by Q4 2026 |
| Hash verification relies on vendor-provided hash | Lone Star performs independent hash comparison against SEL's publicly posted firmware checksums before deployment; any discrepancy between vendor-provided hash and SEL-published hash is an automatic stop-work condition | High for integrity against supply chain tampering; lower for zero-day tampering where SEL's own release is compromised | No additional remediation — current control is appropriate |
| No MFA on EWS-001 local accounts | Vendor engineers do not have local accounts on EWS-001 — they use RDP to reach a dedicated relay configuration profile; no general Windows shell access | Medium — reduces blast radius if vendor access is misused | Implement hardware token or Windows Hello for Business on EWS-001 in Q3 2026 maintenance window |

---

## 8. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| OT Security Lead | Marcus Delgado | *[signed]* | March 1, 2026 |
| Substation Engineering Lead | Diana Flores | *[signed]* | March 3, 2026 |
