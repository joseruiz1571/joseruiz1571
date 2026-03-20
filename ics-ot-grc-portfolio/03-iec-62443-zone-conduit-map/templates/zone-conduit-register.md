# Zone and Conduit Register
## IEC 62443-3-2 — Waco Junction Substation

**Organization:** Lone Star Transmission Services, LLC
**Facility:** Waco Junction Substation (WJSS)
**Prepared by:** _(Name, Title)_
**Review date:** _______________
**Contract reference:** _(Capital project contract number)_
**IEC 62443 revision basis:** IEC 62443-3-2:2020 (Risk assessment), IEC 62443-3-3:2013 (System requirements)

---

## Part 1: Zone Register

> **Instructions:** A Security Zone is a grouping of logical or physical assets that share the same security requirements and are managed as a unit. Zone boundaries should reflect functional separation, not just network topology. Assets that perform different functions with different consequence profiles should generally be in different zones — even if they share a network segment today.
>
> Assign Security Levels using the consequence-of-compromise framework: SL-1 (incidental), SL-2 (intentional with modest means), SL-3 (intentional with sophisticated means), SL-4 (state-level, critical national infrastructure). For most utility OT environments, SL-2 is the baseline; SL-3 is appropriate for assets with direct safety or reliability consequences.

| Zone ID | Zone Name | Assets Included | Required Security Level | Justification | Gap Notes |
|---------|-----------|----------------|------------------------|---------------|-----------|
| Z-01 | Corporate IT Zone | Corporate workstations, email systems, IT infrastructure, enterprise data lake access point | SL-1 | Corporate IT assets have no direct BES control function. Compromise affects business operations but not substation control. Standard enterprise security controls apply. This zone is managed by IT, not OT Security. | IT security program should be periodically reviewed for adequacy; gaps here can enable pivot attacks toward higher-SL zones. |
| Z-02 | OT DMZ Zone | DMZ-FW-01 (IT-side firewall), DMZ-FW-02 (Control-side firewall), WJSS-007 (IT/OT boundary switch), WJSS-008 (historian) | **SL-2** | The DMZ bridges SL-1 (Corporate) and SL-2 (Control) zones. The DMZ itself must be at least SL-2 to maintain zone integrity — a DMZ rated below the zones it bridges becomes the weak link. The historian is assigned here because it pulls from the Control LAN but pushes to corporate; placing it in the Control Zone would extend that zone's boundary to include corporate-WAN-connected devices. Note: the 2016 as-built DMZ does not fully meet SL-2 system requirements (see gap notes). | **Gap:** DMZ firewalls do not enforce unidirectional data flow (no data diode); bidirectional firewall rules allow potential reverse-path exploitation. DMZ firewall firmware is patched quarterly but not on an emergency basis when CVEs are disclosed. Remediation: evaluate hardware data diode for historian replication path. |
| Z-03 | Control Zone | WJSS-001 (HMI), WJSS-002 (data concentrator), EWS-001 (engineering workstation) | _[Complete — should this be SL-2 or SL-3? Justify your choice]_ | _[Explain the consequence of compromise for these assets; consider whether the engineering workstation belongs here or in its own zone given vendor remote access path]_ | _[Identify gaps between current controls and the SL requirements]_ |
| Z-04 | Field Device Zone | WJSS-003, WJSS-005, WJSS-006 (protective relays), WJSS-004 (SAC), WJSS-004-IO (breaker I/O) | _[Complete — these assets have direct safety and reliability consequences; justify your SL]_ | _[The SAC and relays have different connectivity profiles. Does it make sense to group them together?]_ | _[Identify gaps — e.g., relay firmware update process, direct I/O hardening]_ |
| Z-05 | _(Optional: Engineering Access Zone)_ | _(If you decide EWS-001 should be isolated from the main Control Zone, define this zone)_ | _[Complete if you create this zone]_ | _[What is the argument for separating EWS-001? What is the argument against?]_ | |

---

## Part 2: Conduit Register

> **Instructions:** A Conduit is a communication path between two Security Zones. Each conduit must be identified, its direction documented, its Security Level assigned, and any compensating controls noted. The Security Level of a conduit is determined by the lower of the two zones it connects — but compensating controls on the conduit can raise the effective protection to a higher level.
>
> Remote access paths are conduits. Data replication paths are conduits. SCADA polling paths are conduits. If data flows between zones, it is a conduit and it belongs in this register.

| Conduit ID | Name | Source Zone | Destination Zone | Protocol/Port | Direction | Assigned SL | Justification | Compensating Controls | Gap Notes |
|------------|------|-------------|-----------------|---------------|-----------|-------------|---------------|-----------------------|-----------|
| C-01 | Corporate-to-DMZ | Z-01 (Corporate IT) | Z-02 (OT DMZ) | HTTPS/443 (historian replication), RDP/3389 (jump server to EWS-001), SNMP/161 (network management) | Bidirectional | SL-1 → SL-2 boundary; conduit assigned **SL-2** | This conduit is the primary ingress point for all traffic entering the OT environment from corporate IT. The assigned SL matches the destination zone (Z-02, SL-2). The firewall at DMZ-FW-01 enforces port-based filtering; only explicitly permitted protocols pass. RDP to EWS-001 is a known concern — see gap notes. | DMZ-FW-01 enforces ACL; only permitted source IPs can initiate sessions; VPN authentication required for vendor access sessions; session logging enabled | **Gap:** RDP traffic is encrypted and cannot be deep-packet inspected by DMZ-FW-01; an attacker with valid credentials can pass malicious payloads through RDP without firewall detection. Compensating control: session recording on jump server (implemented 2023). |
| C-02 | Vendor Remote Access | Z-01 (Corporate IT) | Z-03 (Control Zone) via Z-02 transit | RDP/3389 (corporate LAN to EWS-001), Relay configuration protocol/TCP 4999 (EWS-001 to relays) | Inbound (vendor to field devices) | _[Complete — this is the key judgment; argue SL-2 vs SL-3 before deciding]_ | _[Where does this conduit actually start and end? Does it terminate in the DMZ or go all the way to the Control Zone? What are the implications of each?]_ | _[What controls are on this conduit? Are they adequate for the SL you assigned?]_ | _[What gaps exist?]_ |
| C-03 | SCADA Polling | Z-03 (Control Zone) | Z-04 (Field Device Zone) | DNP3/TCP 20000 | Bidirectional (poll/response) | _[Complete]_ | _[SCADA polling is typically bidirectional — data concentrator polls relays, relays respond. What SL is appropriate?]_ | _[What controls exist on the DNP3 polling path?]_ | _[DNP3 lacks native authentication in many deployments — is DNP3 Secure Authentication v5 implemented?]_ |
| C-04 | Historian Data Pull | Z-04 (Control Zone) → Z-02 (OT DMZ) | Z-02 (OT DMZ) → Z-01 (Corporate IT) | OPC-DA/TCP (Control LAN to historian), HTTPS (historian to Azure) | Outbound (field data toward corporate/cloud) | _[Complete — this is the historian replication path. What SL applies to each segment?]_ | _[Is this one conduit or two? What are the zone transitions?]_ | _[What controls prevent this path from being used in reverse?]_ | _[The Azure segment takes data outside the facility — how is that addressed in this map?]_ |
| C-05 | _(Define any additional conduits identified)_ | | | | | | | | |

---

## Zone and Conduit Summary Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│  Z-01: Corporate IT Zone (SL-1)                                 │
│  Corporate workstations, Azure data lake endpoint              │
└──────────────────┬──────────────────────────────────────────────┘
                   │  C-01: Corporate-to-DMZ (SL-2)
                   │  HTTPS, RDP, SNMP | DMZ-FW-01
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  Z-02: OT DMZ Zone (SL-2)                                       │
│  DMZ-FW-01, DMZ-FW-02, WJSS-007, WJSS-008 (Historian)         │
└──────────────────┬──────────────────────────────────────────────┘
                   │  C-03-inner: DMZ-to-Control (SL-?)
                   │  SCADA, RDP | DMZ-FW-02
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  Z-03: Control Zone (SL-?)                                      │
│  WJSS-001 (HMI), WJSS-002 (data concentrator), EWS-001        │
└──────────────────┬──────────────────────────────────────────────┘
                   │  C-04: SCADA Polling (SL-?)
                   │  DNP3/TCP 20000
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  Z-04: Field Device Zone (SL-?)                                 │
│  WJSS-003, WJSS-005, WJSS-006 (relays), WJSS-004 (SAC)       │
└─────────────────────────────────────────────────────────────────┘

Vendor Remote Access Path (C-02):
Z-01 → [VPN] → Corporate LAN → [RDP] → EWS-001 in Z-03
(Bypasses Z-02 logical boundary via encrypted tunnel)
```

> **Note to practitioner:** The diagram above reflects current architecture, including the architectural gap where vendor remote access bypasses the DMZ. Your completed zone and conduit register should document this as a gap, not paper over it. The contract requirement is for documentation of current state with gaps identified — not a fictional architecture that doesn't exist.
