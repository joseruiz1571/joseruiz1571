# Annotated Reasoning Example — IEC 62443 Zone and Conduit Map
## Waco Junction Substation — Vendor Remote Access Conduit and Ambiguous Zone Assignment

---

## Purpose

This file works through two of the hardest judgment calls in the Waco Junction zone and conduit map:

1. **The vendor remote access conduit (C-02):** Should it be SL-2 or SL-3? Where does it actually terminate — in the DMZ or in the Control Zone? Both arguments are shown.

2. **EWS-001 (Engineering Workstation) zone assignment:** Should the engineering workstation share the Control Zone with the HMI and SAC, or should it be isolated in its own zone given that it is the vendor remote access terminus?

---

---

# Analysis 1: Vendor Remote Access Conduit (C-02)
## SL-2 vs SL-3 — Both Arguments

### Conduit Description

Relay Logic Partners, LLC (the third-party relay maintenance vendor) connects to Waco Junction as follows:

```
Relay Logic Engineer (remote)
    → Lone Star Corporate VPN (Cisco AnyConnect, MFA)
    → Corporate LAN (Z-01)
    → Jump Server (corporate LAN)
    → RDP session to EWS-001 (Engineering Workstation in Z-03 Control Zone)
    → Relay configuration software on EWS-001
    → DNP3/TCP to WJSS-003, WJSS-005, WJSS-006 (protective relays in Z-04)
```

**Current reality:** The remote access path traverses the Z-01/Z-02 boundary (corporate to DMZ) and then the Z-02/Z-03 boundary (DMZ to Control Zone) — but the RDP session uses an encrypted tunnel that DMZ-FW-02 cannot deep-packet inspect. The effective conduit terminus is EWS-001 in the Control Zone, not the DMZ.

---

### Step 1: Identify the Conduit Boundaries

**Argument A (conduit ends in DMZ):** The vendor remote access path terminates in the OT DMZ at the jump server, which then initiates a separate session to EWS-001. Under this interpretation, there are two conduits: Corporate→DMZ (C-01, SL-2) and DMZ→Control Zone (a sub-conduit of C-03). The vendor never has a direct connection to the Control Zone.

**Argument B (conduit ends in Control Zone):** The RDP session is a single logical connection from the vendor's machine to EWS-001. The DMZ boundary switch and firewall pass this session transparently — they are infrastructure for the conduit, not the conduit's terminus. Under this interpretation, C-02 is a single conduit from Z-01 (Corporate) to Z-03 (Control Zone), passing through Z-02 (DMZ) as a transit zone.

> [REASONING]
> This distinction matters for SL assignment and for the architectural gap finding. If you treat the conduit as ending in the DMZ (Argument A), you can claim the vendor remote access is constrained by DMZ controls. But the DMZ firewall does not inspect the RDP payload — it only permits the TCP session. A vendor engineer (or an attacker with vendor credentials) has a direct logical path to EWS-001 from the internet. The DMZ provides no meaningful inspection of what travels through it on this path.
>
> Argument B is the honest architectural description. The conduit terminates in the Control Zone. This is an architectural gap — the vendor remote access should terminate in the DMZ, and a separate, audited session should be required to access the Control Zone from the DMZ. That is not the current design.
>
> **Decision: Argument B.** The conduit is documented as terminating in the Control Zone (Z-03). The gap — that it bypasses meaningful DMZ inspection — is documented as a remediation item, not papered over.

---

### Step 2: Consequence of Compromise

If C-02 is compromised (attacker gains vendor access credentials and uses them to reach EWS-001):

| Consequence Category | Assessment |
|---------------------|-----------|
| Safety | Medium — EWS-001 is used to configure relays; a malicious firmware modification could disable protection on 345 kV circuits, creating a safety risk for field crews |
| Operational | High — attacker with EWS-001 access can reconfigure relay settings, potentially causing nuisance trips or blocking legitimate fault clearing |
| Financial | Medium — relay misconfiguration requiring emergency reconfiguration; potential NERC CIP violation if access was not properly controlled |
| Reputational | Medium |

**Overall consequence: High**

---

### Step 3: The SL-2 Argument

**SL-2 is appropriate because:**

- The conduit already requires multi-factor authentication (Cisco Duo) at the VPN layer
- Sessions are logged and recorded on the jump server
- Vendor access is limited to scheduled maintenance windows by policy (not enforced technically, but audited)
- The engineering workstation (EWS-001) is not on the live SCADA network during normal operations; it is connected to the relay configuration network, which is separate from the SCADA polling network
- Attack complexity requires compromising a specific vendor's credentials and knowing the internal network architecture to navigate from the VPN to EWS-001 to the relays — not a trivial attack chain

> [REASONING]
> The SL-2 argument is not wrong. The controls described are real and meaningful. VPN with MFA is a meaningful barrier. Session recording deters insider threats. The operational separation of EWS-001 from live SCADA (when not in use) limits what an attacker can do through this path.
>
> However, SL-2 assumes an attacker using "standard means" with "some ICS knowledge." The US government has documented campaigns where nation-state actors specifically targeted utility vendor remote access paths as an initial access vector (cf. CISA advisory AA22-265A on ICS-targeting actors). Those actors have ICS-specific knowledge, have researched target architectures in advance, and use stolen vendor credentials as a known-good initial access technique. That is closer to SL-3 attacker capability than SL-2.

---

### Step 4: The SL-3 Argument

**SL-3 is more appropriate because:**

- The conduit's terminus (EWS-001) has access to protective relay configuration on 345 kV circuits — this is high-consequence access
- Known threat actors specifically target vendor remote access paths for initial entry into utility OT environments
- The conduit bypasses meaningful DMZ inspection (as documented in Step 1) — the actual security controls on this path are weaker than the zone architecture implies
- A nation-state actor with Relay Logic Partners' credentials (obtained through a supply chain compromise or credential theft) could navigate this entire path with no additional barriers beyond the VPN MFA

> [REASONING]
> SL-3 implies that your controls are designed to resist a sophisticated attacker with ICS-specific knowledge. For this conduit, that is the relevant threat actor. The consequence is high (relay reconfiguration on 345 kV protection), and the attack vector (vendor credential compromise → VPN → EWS-001 → relay config) is a documented, real-world attack pattern.
>
> The counterargument to SL-3 is resource intensity: meeting SL-3 requirements for this conduit would require privileged access management (PAM) for vendor sessions, network monitoring with ICS-protocol awareness at the relay config protocol layer, and potentially hardware-enforced session isolation. Lone Star's current architecture does not support those controls.
>
> **This is the honest tension in IEC 62443 implementation for small utilities:** the "correct" SL based on consequence and threat is SL-3. The practical SL given current architecture and resource constraints is SL-2 with documented gaps. Pretending SL-2 is sufficient because the controls are good enough is different from saying SL-2 is the target, SL-3 is the aspiration, and here is the gap and the remediation plan.

---

### Step 5: Decision and Documented Gap

**Assignment: SL-2 (current state) with documented gap and SL-3 remediation roadmap**

| Item | Detail |
|------|--------|
| **Assigned SL** | SL-2 |
| **Basis** | Current controls (VPN+MFA, session recording, access scheduling) meet SL-2 requirements |
| **Documented gap** | Conduit bypasses DMZ inspection; SL-3 would be appropriate given threat profile and consequence; current architecture cannot support SL-3 controls |
| **Compensating controls** | Privileged access management review for Relay Logic credentials; session recording reviewed after each vendor access event; vendor access windows limited to business hours with on-site Lone Star escort |
| **Remediation plan** | Redesign vendor access path to terminate in DMZ (new jump server in Z-02); implement PAM solution for vendor sessions; re-evaluate SL assignment after remediation |
| **Target SL** | SL-3 post-remediation |

---

---

# Analysis 2: EWS-001 Zone Assignment
## Single Control Zone vs. Isolated Engineering Zone

### The Question

EWS-001 (Engineering Workstation) is physically on the Control LAN alongside WJSS-001 (HMI), WJSS-002 (data concentrator), and WJSS-004 (SAC). Should it be in the same Control Zone (Z-03), or should it be in a separate Engineering Zone?

---

### Argument for Single Zone (EWS-001 in Z-03 with HMI and SAC)

**Position:** All Control LAN devices share the same network segment and the same security requirements. Defining a separate zone for EWS-001 adds documentation overhead without adding meaningful security — EWS-001 can still communicate with the HMI and SAC on the same Layer 2 network.

> [REASONING]
> This argument is pragmatically appealing but architecturally weak. Zones in IEC 62443 are not just documentation constructs — they are meant to reflect actual security boundaries. If EWS-001 and the HMI are on the same flat LAN with no access controls between them, you can call them two zones, but it is a fiction. The zone designation provides no operational protection if a compromised EWS-001 can directly communicate with the HMI or the SAC.

---

### Argument for Separate Engineering Zone (EWS-001 in Z-05)

**Position:** EWS-001 is the terminus for vendor remote access. That makes it the highest-risk device on the Control LAN — it is the most likely initial compromise point. Placing it in the same zone as the HMI and SAC means that a compromised EWS-001 is effectively inside the zone boundary, with no internal boundary between it and the devices that control 345 kV breakers.

If EWS-001 is in its own zone (Z-05: Engineering Zone), then:
- The conduit from Z-05 to Z-03 can be defined and controlled (e.g., only relay configuration protocol traffic permitted; no RDP from EWS to HMI)
- A compromised EWS-001 does not automatically have lateral access to the HMI or SAC — it must traverse a documented conduit with defined controls
- The zone boundary makes the blast radius of a vendor access compromise explicit and limited

> [REASONING]
> This argument is architecturally correct and reflects IEC 62443's intent. Zones should be defined by security requirements and consequence profiles, not just by network topology. EWS-001's risk profile — it is the vendor access terminus, it has lower operational uptime requirements, it is occasionally disconnected from the network — is different from the HMI and SAC, which are operational 24/7 and have direct control authority.
>
> The practical implementation of Z-05 requires that EWS-001 be on a different network segment from the rest of the Control LAN, with a managed device enforcing access control at the boundary. Today, that enforcement does not exist — EWS-001 is on the same flat LAN. So Z-05, like the SL-3 conduit analysis, is the aspirational state, not the current state.

---

### Decision

**Assignment: EWS-001 placed in Z-03 (Control Zone) in current-state documentation; Z-05 (Engineering Zone) defined as target state**

| Item | Detail |
|------|--------|
| **Current state** | EWS-001 in Z-03 (Control Zone) — reflects actual flat LAN architecture; no physical or logical boundary exists between EWS-001 and HMI/SAC today |
| **Documented gap** | EWS-001 is the vendor access terminus and should be isolated from live SCADA assets; current flat LAN means a compromised EWS-001 has unrestricted L2 access to HMI and SAC |
| **Compensating control** | EWS-001 is powered off and disconnected from the network when not in use for engineering work (enforced by operations policy; verified by monthly access log review) |
| **Target state** | Create Z-05 (Engineering Zone) with EWS-001 on a separate VLAN; define C-05 conduit from Z-05 to Z-03 permitting only relay configuration protocols; implement access control at the conduit boundary |
| **Remediation timeline** | VLAN reconfiguration at Q3 maintenance window (same window as patch deployment for CVE-2024-LST-0047) |

> [REASONING]
> The powered-off compensating control is meaningful but imperfect. It works as long as the operations policy is followed. The risk is that "disconnect EWS-001 when not in use" is a procedural control that can be forgotten, bypassed during a rush maintenance call, or simply not enforced if the person who normally does it is unavailable. Procedural controls are better than nothing; they are not as good as architectural controls.
>
> Documenting this honestly — "we know EWS-001 should be isolated, here is why it isn't yet, here is what we are doing in the meantime, and here is the remediation timeline" — is the right approach. It is more defensible in an audit or post-incident review than a zone map that implies architectural isolation that does not exist.
