# Scenario: IEC 62443 Zone and Conduit Map
## Lone Star Transmission Services, LLC — Waco Junction Substation

---

## Constraints Block

| Constraint | Detail |
|------------|--------|
| **Budget** | No capital funding for network redesign; zone mapping must reflect current architecture; identified gaps addressed through compensating controls or documented remediation backlog |
| **Operational** | No maintenance window until Q3; architectural changes requiring system downtime cannot be implemented before contract award deadline |
| **Legacy systems** | OT DMZ designed in 2016 using NIST 800-82 guidance, not IEC 62443; DMZ assets were not selected with IEC 62443 Security Level requirements in mind |
| **Regulatory deadline** | Capital project contract award requires IEC 62443 alignment documentation within 45 days |

---

## Contract Driver

Lone Star is bidding on a capital project to upgrade the protection and control infrastructure at Waco Junction. The project involves new relay panels, a substation automation upgrade, and a new engineering workstation. The prime contractor — a large EPC firm — has a procurement requirement that any facility hosting their equipment must demonstrate IEC 62443 alignment. Specifically, the contract requires:

> *"Owner shall provide a Zone and Conduit diagram documenting Security Level assignments for all zones in which Contractor equipment will be installed, consistent with IEC 62443-3-2 risk assessment methodology. Minimum required Security Level for the Control Zone is SL-2."*

This is not a regulatory compliance exercise. It is a contract qualification exercise. However, the outputs will also be used to improve Lone Star's OT security architecture documentation and to support future CIP-013 vendor assessments.

---

## Substation Architecture

Waco Junction Substation is organized into four functional layers. Each layer represents a candidate Security Zone under IEC 62443 terminology.

### Layer 1: Corporate IT Network
The enterprise network segment. Hosts corporate workstations, email systems, the enterprise data lake (Azure-hosted), and IT-managed network infrastructure. Managed by Lone Star's IT department. No direct operational technology function, but it is the network through which vendor remote access VPN sessions originate and through which historian replication traffic flows.

### Layer 2: OT DMZ
A semi-isolated network segment designed to buffer communication between the corporate IT network and the substation control infrastructure. Hosts the following assets:

| Asset ID | Asset Name | Type | Function |
|----------|-----------|------|---------|
| WJSS-007 | IT/OT Boundary Switch | Managed Network Switch | Routes traffic between corporate LAN and substation networks; enforces ACLs |
| WJSS-008 | AVEVA PI Historian | Process Historian | Archives SCADA data; replicates to Azure data lake via corporate WAN |
| DMZ-FW-01 | OT DMZ Firewall | Next-Gen Firewall | Enforces policy between corporate IT and OT DMZ; installed 2016, patched quarterly |
| DMZ-FW-02 | OT Control LAN Firewall | Next-Gen Firewall | Enforces policy between OT DMZ and Control LAN; installed 2016, patched quarterly |

**OT DMZ as-built notes:** The DMZ was designed to a basic segmentation model. The firewalls have permit rules allowing the historian to pull data from the Control LAN and forward it to corporate. There is no data diode or unidirectional gateway — data flows are bidirectional at the protocol layer, filtered by ACL rules. This is a known architectural gap.

### Layer 3: Control LAN
The primary operational technology network segment. Hosts SCADA and control system assets directly involved in substation monitoring and switching operations.

| Asset ID | Asset Name | Type | Function |
|----------|-----------|------|---------|
| WJSS-001 | EcoStruxure GridAdvance HMI | SCADA HMI | Primary operator interface; SCADA monitoring and control |
| WJSS-002 | SCADA Data Concentrator | Communication Front-End | Aggregates field device data; SCADA protocol translation |
| WJSS-004 | Substation Automation Controller | PLC/SAC | Automatic switching sequences; direct breaker control |
| EWS-001 | Engineering Workstation | Engineering Workstation | Relay configuration, SAC programming; not connected to HMI network during normal operations |

**Control LAN notes:** The Control LAN is a flat Ethernet network. No internal segmentation currently exists between the HMI, data concentrator, SAC, and engineering workstation. All devices are on the same Layer 2 broadcast domain. This is relevant to zone boundary analysis — should these assets be in a single zone or multiple zones?

### Layer 4: Field Devices
Hardwired and serial/network-connected protection and control devices at the switchyard level. Not all field devices have IP connectivity.

| Asset ID | Asset Name | Type | Connectivity |
|----------|-----------|------|-------------|
| WJSS-003 | Protective Relay — 345 kV Line 1 | IED | DNP3 over Ethernet to WJSS-002 |
| WJSS-005 | Protective Relay — 345 kV Line 2 | IED | DNP3 over Ethernet to WJSS-002 |
| WJSS-006 | Protective Relay — 345 kV Line 3 | IED | DNP3 over Ethernet to WJSS-002 |
| WJSS-004-IO | Breaker Control I/O | Hardwired I/O | Direct wired to WJSS-004 (SAC) |

---

## Remote Access Architecture

A third-party vendor — Relay Logic Partners, LLC — provides remote maintenance services for the protective relays at Waco Junction. When Relay Logic engineers need to perform firmware updates or configuration changes, they connect as follows:

1. Relay Logic engineer initiates a VPN session to Lone Star's corporate VPN concentrator (IT-managed)
2. Session is authenticated via username + password + Cisco Duo MFA
3. VPN tunnel terminates on the corporate LAN
4. Engineer uses an RDP jump server on the corporate LAN to connect to EWS-001 (Engineering Workstation) on the Control LAN
5. From EWS-001, engineer connects to individual protective relays via the relay configuration software (SEL Compass or similar)

**Zone boundary implication:** The remote access path traverses three network boundaries: Corporate IT → OT DMZ → Control LAN. The path currently bypasses the OT DMZ's relay inspection by using an encrypted RDP tunnel. The firewall between OT DMZ and Control LAN allows RDP from the DMZ to EWS-001.

This is the central zone and conduit design question: does the vendor remote access conduit terminate in the DMZ (the architecturally preferred model), or does it extend to the Control LAN (the current reality)? And what Security Level is appropriate for that conduit?

---

## Zone Boundary Decision Points

Three asset placement decisions require explicit documentation:

**Decision 1 — WJSS-008 (Historian):** The historian pulls data from the Control LAN and pushes it to the corporate network. It sits in the OT DMZ physically and logically. But its data connections bridge the Control LAN (SL-2 candidate) and Corporate IT (SL-1 or unzoned). Does the historian belong in the OT DMZ Zone, or does it warrant its own zone given the bidirectional data connections?

**Decision 2 — EWS-001 (Engineering Workstation):** The engineering workstation is on the Control LAN. But it is also the terminus for vendor remote access. Should it be in the same zone as the HMI and SAC (all in the "Control Zone"), or should it be isolated in its own zone (an "Engineering Zone") to limit the blast radius if the vendor access path is compromised?

**Decision 3 — WJSS-004 (SAC) and Field Devices:** The SAC has direct I/O connections to the field-level breaker control circuits. It also sits on the Control LAN with the HMI and data concentrator. Is the Control LAN a single zone, or should the SAC and its field device connections be in a separate, higher-Security-Level zone?
