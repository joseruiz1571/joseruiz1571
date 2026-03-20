# Scenario: OT Patch Management Risk Acceptance
## Lone Star Transmission Services, LLC

---

## Constraints Block

| Constraint | Detail |
|------------|--------|
| **Budget** | No budget for hardware replacement; existing 2014 HMI has 4 years of useful life remaining per capital plan |
| **Operational** | Patching requires a 72-hour maintenance window; next approved maintenance window is Q3 (approximately 6 months from this risk acceptance) |
| **Vendor constraint** | Schneider Electric support agreement explicitly prohibits application of unauthorized patches; applying a third-party or self-developed patch voids the support contract |
| **Vendor patch timeline** | Vendor has acknowledged CVE-2024-LST-0047 and stated patch availability in approximately 18 months (v6.2.1 firmware) |
| **Regulatory deadline** | NERC CIP-007 compliance evidence must be current; this risk acceptance is the CIP-007 R2 compensating control documentation for this asset |

---

## Asset Description

**Asset ID:** WJSS-001
**Asset Name:** Schneider Electric EcoStruxure GridAdvance HMI (fictional product designation)
**Asset Type:** SCADA Human-Machine Interface
**Firmware/OS:** Windows Embedded Standard 7, EcoStruxure GridAdvance v5.4.2 (2014 vintage)

### Role in Grid Operations

WJSS-001 is the primary operator interface for the Waco Junction Substation control room. Operators use this terminal to:
- Monitor real-time status of all 345 kV switching positions and protection relay alarms
- Issue manual switching commands to breakers via the SCADA data concentrator (WJSS-002)
- Receive ERCOT system alerts via the unidirectional data link
- View event logs for post-incident analysis

This terminal is the only local HMI at WJSS. Loss of this asset does not immediately disable substation protection (relays operate independently), but it eliminates the operator's visibility and manual control capability. Operators would be working blind on a 345 kV substation until remote SCADA from the corporate WAN was confirmed functional.

### Why Patching Is Not Possible Without This Risk Acceptance

Three independent constraints prevent immediate patching:

1. **Maintenance window:** The 72-hour window is necessary because the HMI must be taken offline, the patch applied, functional testing completed, and the system restored — all before resuming operational responsibility. No 72-hour window is available until Q3.

2. **Support agreement:** Schneider Electric's support contract for this system explicitly states that applying patches not released by Schneider voids the hardware and software support agreement. No unauthorized patch exists; the only available patch is the vendor's forthcoming v6.2.1. Voiding support creates a separate risk category: if the system fails after unauthorized patching, Lone Star bears full remediation cost with no vendor assistance.

3. **No test environment:** Lone Star does not have a duplicate HMI environment for patch testing. The vendor patch will be applied to a test image provided by Schneider, but that image cannot be completed until the patch is available.

---

## Vulnerability Details

### CVE-2024-LST-0047 (Fictional CVE — Plausible Detail)

| Field | Value |
|-------|-------|
| **CVE ID** | CVE-2024-LST-0047 |
| **CVSS v3.1 Score** | 8.1 (High) |
| **CVSS Vector** | AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L |
| **Attack Vector** | Adjacent Network (attacker must be on the same network segment) |
| **Attack Complexity** | Low |
| **Privileges Required** | None |
| **User Interaction** | None |
| **Confidentiality Impact** | High |
| **Integrity Impact** | High |
| **Availability Impact** | Low |
| **Vendor Advisory** | SEVD-2024-LST-003 |
| **Affected versions** | EcoStruxure GridAdvance v5.0 through v6.2.0 |
| **Fixed version** | v6.2.1 (not yet released; ETA 18 months) |

### Vulnerability Summary

CVE-2024-LST-0047 is a memory corruption vulnerability in the EcoStruxure GridAdvance HMI's process data parsing library. When the HMI parses malformed DNP3 Application Layer messages from a device on the same network segment, it is possible for an unauthenticated attacker to achieve arbitrary code execution on the HMI operating system.

**Attack path summary:** An attacker with access to the substation LAN can craft a malformed DNP3 packet addressed to WJSS-001. The HMI's data parsing process does not perform adequate bounds checking on the Application Layer data object. A heap overflow in the parsing library allows the attacker to overwrite a function pointer and redirect execution to attacker-controlled code. Successful exploitation gives the attacker a session running as the HMI process user — which, in the default GridAdvance configuration, is a local administrator equivalent.

**What an attacker who exploits this vulnerability can do:**
- Read all SCADA telemetry displayed on the HMI (confidentiality impact — grid operational state data)
- Modify the HMI display to show operators false system state (integrity impact — this is the more dangerous scenario operationally)
- Issue switching commands through the HMI's SCADA interface (integrity impact — if the HMI's command functions are accessible from the compromised process)
- Pivot to other devices on the substation LAN using the HMI's network credentials and established connections

**What an attacker cannot directly do via this vulnerability alone:**
- Bypass protective relay logic (relays operate independently)
- Issue commands to ERCOT systems (ERCOT link is unidirectional)
- Access the corporate WAN without traversing WJSS-007 (the IT/OT boundary switch)

---

## Threat Scenario

### Threat Actor Profile
For risk acceptance purposes, Lone Star must characterize the realistic threat. This acceptance addresses:

- **Nation-state actors with ICS capability:** CISA has documented multiple campaigns targeting US transmission infrastructure. Actors in this category have the capability to achieve network adjacency through supply chain compromise, vendor access abuse, or corporate network pivot. They would research target HMI vulnerabilities in advance and have DNP3 protocol expertise.
- **Opportunistic attackers:** Less likely to target this specific asset; network-adjacent requirement limits opportunistic exploitation from the internet. However, a penetration tester or insider threat with substation LAN access would not need advanced capability to exploit this vulnerability (AC:L).

### MITRE ATT&CK for ICS Mapping

| ATT&CK Tactic | Technique | Technique ID | Relevance to This Scenario |
|---------------|-----------|--------------|---------------------------|
| Initial Access | Exploit Public-Facing Application | T0819 | Attacker exploits CVE-2024-LST-0047 via adjacent network access |
| Execution | Exploit of Remote Services | T0866 | DNP3 packet crafted to exploit parsing vulnerability |
| Persistence | Modify Program | T0889 | Post-exploitation: attacker modifies HMI software to maintain access |
| Discovery | Remote System Discovery | T0846 | Attacker enumerates other devices on substation LAN from compromised HMI |
| Lateral Movement | Lateral Tool Transfer | T0867 | Attacker moves tooling from HMI to other LAN-connected devices |
| Impact | Manipulation of View | T0832 | **Primary concern:** attacker causes HMI to display false grid state to operators |
| Impact | Unauthorized Command Message | T0855 | **Secondary concern:** attacker uses HMI's SCADA interface to issue unauthorized switching commands |

### Stakeholder Sign-Off Required

| Role | Name | Basis for Sign-Off |
|------|------|-------------------|
| OT Security Lead | Marcus Delgado | Technical assessment of vulnerability and compensating controls |
| Operations Manager | Scott Akers | Operational authorization — confirmation that grid operations can continue safely under accepted risk |
| CISO | Jennifer Wu | Organizational risk acceptance authority; ties this to enterprise risk register |

---

## Connection to CIP-007 Patch Management Program

Under NERC CIP-007-6, Requirement R2, Lone Star must:
- Track and document known software vulnerabilities in BES Cyber Systems (R2.1)
- Document a mitigation plan for vulnerabilities that cannot be patched within 35 days of notification (R2.2)

CVE-2024-LST-0047 was identified 47 days ago (beyond the 35-day threshold). The mitigation plan for CIP-007 R2.2 compliance is this risk acceptance document, supplemented by the compensating controls defined in the risk acceptance form. This document serves dual purpose: organizational risk management and CIP-007 compliance evidence.
