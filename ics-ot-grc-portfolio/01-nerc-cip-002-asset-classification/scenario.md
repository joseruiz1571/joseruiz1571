# Scenario: NERC CIP-002 Asset Classification
## Lone Star Transmission Services, LLC

---

## Constraints Block

| Constraint | Detail |
|------------|--------|
| **Budget** | No external consultant budget approved; all classification work performed by 2-FTE compliance team |
| **Operational** | No maintenance windows available until Q3; classification is a documentation exercise but operational teams have limited availability for interviews |
| **Legacy systems** | Three assets at Brazos Switching Station are running vendor-EOL firmware; vendor ceased support in 2020 |
| **Regulatory deadline** | NERC CIP compliance audit scheduled in 87 days; classification worksheet must be signed before evidence package is due |

---

## Organization Background

**Lone Star Transmission Services, LLC** is a transmission-only utility operating in Texas under ERCOT market rules and subject to NERC reliability standards. The company owns and maintains high-voltage transmission infrastructure but does not generate or distribute power. Its BES footprint consists of two substations.

**Key personnel referenced in this project:**

| Role | Name |
|------|------|
| OT Security Lead | Marcus Delgado |
| Compliance Analyst | Priya Nair |
| Operations Manager | Scott Akers |
| Substation Engineering Lead | Diana Flores |

---

## Substation Descriptions

### Waco Junction Substation (WJSS)
- **Voltage class:** 345 kV
- **Function:** Transmission switching point connecting three 345 kV lines from different generators to the main transmission corridor. Loss of this substation would de-energize transmission segments serving approximately 180,000 customers (based on ERCOT load flow analysis on file).
- **Control architecture:** Has a dedicated Protection and Control room housing an Energy Management System (EMS) workstation, protective relays, and a substation automation controller. Remote access is enabled for ERCOT real-time data exchange and vendor maintenance.
- **Network connectivity:** Connected to Lone Star's corporate WAN via a microwave link, with a separate ERCOT data link (unidirectional). An IT-managed network switch was installed in 2021 to support a historian replication project.

### Brazos Switching Station (BJSS)
- **Voltage class:** 138 kV
- **Function:** Switching station on the 138 kV sub-transmission network. Serves as a tie point between two 138 kV circuits feeding a neighboring distribution cooperative. Loss of this station would affect cooperative load but no BES generation interconnection.
- **Control architecture:** Smaller footprint. Protection controlled by individual bay-level protective relays. A remote terminal unit (RTU) provides SCADA visibility to the Waco Junction control room. No dedicated local control room.
- **Network connectivity:** Serial SCADA link to WJSS control room. No direct IP connectivity to corporate WAN as of this classification exercise (a future upgrade project is in planning).

---

## Asset Inventory

The following 12 assets are in scope for the classification exercise. Assets are numbered by substation prefix (WJSS = Waco Junction, BJSS = Brazos).

| Asset ID | Asset Name | Asset Type | Location | Firmware / OS Version | Key Function | Connectivity |
|----------|------------|------------|----------|----------------------|--------------|--------------|
| WJSS-001 | EMS Workstation | Human-Machine Interface (HMI) | Waco Junction — P&C Room | Windows 10 LTSC 2019 | Operator interface for substation monitoring and control via SCADA | ERCOT data link (unidirectional), corporate WAN, local LAN |
| WJSS-002 | SCADA Data Concentrator | Data Concentrator / Comm Front-End | Waco Junction — P&C Room | Vendor-proprietary OS, v4.1.2 | Aggregates field data; serves as communication interface between RTUs and EMS workstation | Corporate WAN, WJSS-001, BJSS RTU serial link |
| WJSS-003 | Protective Relay — 345 kV Line 1 | Protective Relay (IED) | Waco Junction — Relay Panel A | SEL firmware v3.4 (2018) | Protection for the primary 345 kV transmission line; trips breakers on fault detection | Substation LAN via DNP3 to data concentrator |
| WJSS-004 | Substation Automation Controller | Programmable Logic Controller (PLC) / SAC | Waco Junction — P&C Room | ABB firmware v2.7.1 (2016) | Executes automatic switching sequences for voltage regulation; can open/close breakers | Substation LAN; direct I/O to breaker control circuits |
| WJSS-005 | Protective Relay — 345 kV Line 2 | Protective Relay (IED) | Waco Junction — Relay Panel B | SEL firmware v3.4 (2018) | Protection for the secondary 345 kV transmission line | Substation LAN via DNP3 to data concentrator |
| WJSS-006 | Protective Relay — 345 kV Line 3 | Protective Relay (IED) | Waco Junction — Relay Panel C | SEL firmware v3.4 (2018) | Protection for the third 345 kV transmission line | Substation LAN via DNP3 to data concentrator |
| WJSS-007 | IT/OT Boundary Switch | Managed Network Switch | Waco Junction — P&C Room | Cisco IOS 15.2 | Connects historian replication path to corporate WAN; was installed for analytics project | Corporate WAN, historian server, SCADA LAN |
| WJSS-008 | Historian Server | Process Historian | Waco Junction — P&C Room | Windows Server 2016, AVEVA PI v2019 | Archives real-time SCADA data; replicates to enterprise data lake | SCADA LAN, corporate WAN via WJSS-007 |
| BJSS-001 | Remote Terminal Unit | RTU | Brazos Switching Station — Control Cabinet | GE D20MX firmware v1.3 (2014) | Provides SCADA telemetry from Brazos to Waco Junction data concentrator | Serial link to WJSS-002 |
| BJSS-002 | Protective Relay — 138 kV Line A | Protective Relay (IED) | Brazos Switching Station — Panel 1 | GE Multilin firmware v4.2 (2017) | Protection for 138 kV line feeding cooperative load | Local hardwired to RTU; no network connectivity |
| BJSS-003 | Protective Relay — 138 kV Line B | Protective Relay (IED) | Brazos Switching Station — Panel 2 | GE Multilin firmware v4.2 (2017) | Protection for 138 kV line feeding cooperative load | Local hardwired to RTU; no network connectivity |
| BJSS-004 | Network Time Protocol Server | NTP Server / Timekeeping Appliance | Brazos Switching Station — Control Cabinet | Linux-based, vendor-proprietary (EOL 2020) | Provides time synchronization to the RTU and both protective relays at Brazos | Serial link only; no IP connectivity to any network |

---

## Classification Context

### Applicable Standard
NERC CIP-002-5.1a, specifically Attachment 1 which defines categorization criteria for High, Medium, and Low impact BES Cyber Systems.

### Classification Timeline
- **Classification worksheet due:** 60 days from today (allows 27 days buffer before audit package submission)
- **Approval required from:** OT Security Lead (Marcus Delgado), Operations Manager (Scott Akers)
- **Review by:** Compliance Analyst (Priya Nair) — primary author

### Non-Obvious Assets — Classification Note

Two assets in this inventory require a documented argument **in both directions** before a final classification is recorded:

**WJSS-004 (Substation Automation Controller):** This asset executes automatic breaker operations. The question is whether it qualifies as a High impact BES Cyber System component because of its ability to affect the operational status of the 345 kV transmission assets at Waco Junction, or whether it should be classified Medium because its automatic functions are bounded in scope and do not affect the transmission system at the level that would meet Attachment 1 High criteria. Both arguments are presented in the annotated reasoning example.

**WJSS-007 (IT/OT Boundary Switch):** This switch is a network device, not a control system asset. But it sits inside the Electronic Security Perimeter (if one is correctly drawn) and is the path through which the historian server communicates with the corporate WAN. The question is whether it is a BES Cyber Asset (i.e., does it perform a function that, if compromised, would impact the BES within 15 minutes?) or whether it is a Protected Cyber Asset (PCA) or excluded entirely. This classification has downstream consequences for the CIP-005 Electronic Access Point determination.

### ERCOT Load Analysis Reference
WJSS serves as a critical node in the Texas transmission network. ERCOT's publicly available transmission planning data indicates that loss of the 345 kV switching capability at this location, combined with the concurrent loss of the Brazos tie, would stress multiple contingency scenarios. This supports a more conservative (higher) classification for the primary WJSS control assets. The compliance team should document the specific ERCOT contingency analysis reference in the approval record.
