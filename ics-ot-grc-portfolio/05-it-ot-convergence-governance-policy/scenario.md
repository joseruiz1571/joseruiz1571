# Scenario: IT/OT Convergence Governance Policy
## Lone Star Transmission Services, LLC — AVEVA PI Historian to Azure Data Lake

---

## Constraints Block

| Constraint | Detail |
|------------|--------|
| **Budget** | No budget for hardware data diode; Azure configuration changes are within existing cloud contract but require IT Security sign-off |
| **Operational** | Historian replication is now live and business users are actively using dashboards; taking the connection offline while governance is established would create executive-level friction |
| **Legacy architecture** | The OT DMZ was not designed with a data diode; the existing firewall-based architecture allows bidirectional protocol-layer traffic, filtered by ACL rules |
| **Regulatory** | CIP-007 patch management and CIP-011 information protection obligations are potentially implicated by this connection; compliance team must assess before the next audit evidence pull |

---

## How This Connection Came to Exist

In Q1 of the current year, the Operations Analytics team — part of Lone Star's business operations function — approached IT about creating an executive dashboard showing real-time substation performance metrics. The project was framed as a "data analytics initiative," not an OT security project. IT provisioned an Azure Data Factory pipeline and a Power BI workspace. The business unit's IT lead, working with the AVEVA PI system administrator (who reports to Operations, not IT Security), configured the PI-to-Azure connection.

The connection path: WJSS-008 (AVEVA PI Historian on the substation LAN) → WJSS-007 (IT/OT boundary switch) → corporate WAN → Azure Data Factory → Azure Data Lake Storage Gen2 → Power BI.

No security review was requested. No IT/OT governance approval was sought. Marcus Delgado (OT Security Lead) learned about the connection three months after it was enabled, when a routine network traffic review flagged outbound HTTPS traffic from the historian to an Azure endpoint.

**The connection has been running for approximately 90 days without governance review.**

---

## Data Flow Description

```
[WJSS-008: AVEVA PI Historian]
    Located: Waco Junction Substation Control LAN
    Data sent: Real-time SCADA telemetry tags (switching state, voltage,
               current measurements), equipment health metrics,
               operational KPIs derived from SCADA data
    Protocol: HTTPS (PI Web API) outbound to Azure
    Frequency: Every 30 seconds (configurable; currently default)
         |
         | (through WJSS-007 IT/OT boundary switch)
         | (through DMZ-FW-01 -- permitted outbound HTTPS rule added
         |  by AVEVA PI admin without IT Security review)
         ▼
[Corporate WAN]
    Path: Microwave link from WJSS to corporate datacenter
    Encryption: Traffic is HTTPS/TLS 1.2 from historian to Azure
         |
         ▼
[Azure Data Factory (East US 2 region)]
    Function: Receives PI Web API data; transforms and loads to ADLS
    Authentication: Managed identity (configured by business unit IT lead)
    Access: No IP restriction on Azure Data Factory endpoint currently
         |
         ▼
[Azure Data Lake Storage Gen2]
    Data at rest encryption: AES-256 (Azure default)
    Access control: Azure AD -- configured by business unit;
                    currently accessible to 14 Power BI user accounts
    Retention: 90 days rolling (currently; no formal retention policy set)
         |
         ▼
[Power BI Workspace]
    Users: 14 executives and operations managers
    Data shown: Substation real-time metrics, equipment health scores,
                historical trend charts
```

---

## Data Classification Analysis

The data flowing through this connection warrants classification evaluation under CIP-011:

**BES Cyber System Information (BCSI) assessment:** CIP-011 applies to information about BES Cyber Systems that, if disclosed, could be used to gain unauthorized access or could pose a threat to the BES. Real-time grid telemetry — specifically, the real-time switching state and operational data from a 345 kV substation — could inform an attacker about:
- Current operational state (which breakers are open/closed)
- Equipment vulnerabilities (anomaly data, equipment health degradation)
- Operational patterns (load cycles, maintenance windows inferred from state changes)

Lone Star's existing CIP-011 program does not currently address cloud-hosted data. This is a gap.

---

## Stakeholder Analysis

| Stakeholder | Role | Interest | Concern |
|-------------|------|---------|---------|
| Operations Analytics Team | Business unit — initiated the connection | Dashboard is in active use by executives; any disruption will require executive justification | Governance process will slow or block future analytics initiatives |
| Operations Manager (Scott Akers) | End user of dashboards | Real-time visibility improves operational decision-making; dashboards are useful | Does not want the connection taken offline |
| IT Security | Owns corporate network and Azure tenant governance | Azure tenant has OT data now; this is outside their normal governance scope | Who is responsible for securing OT data in Azure? IT or OT? |
| OT Security (Marcus Delgado) | Owns OT security program | The historian is on the Control LAN; this connection is a potential ingress path to OT | The firewall rule was added without OT Security review; this is a policy violation |
| Compliance (Priya Nair) | CIP-007 and CIP-011 compliance | This may implicate CIP-011 BCSI protection requirements; needs documentation before audit | Is this a self-reportable compliance finding? |
| CISO (Jennifer Wu) | Organizational risk authority | IT/OT convergence creates risk at the boundary; this one happened without governance | Needs a policy and process to prevent recurrence; needs to assess whether this specific connection is acceptable |

---

## What Is Currently Unknown

| Unknown | Why It Matters |
|---------|---------------|
| Whether the Azure endpoint has IP restrictions | An unrestricted Azure Data Factory endpoint could be reached from any internet IP; the historian's PI Web API credentials may be the only barrier |
| Whether the 14 Power BI users have MFA enabled on their Azure AD accounts | If a user account is compromised, an attacker could access historical and real-time OT telemetry from any internet-connected device |
| Whether the firewall rule added to DMZ-FW-01 permits only outbound historian traffic, or broader outbound HTTPS | A rule added without review may be more permissive than intended |
| Whether OT data in Azure falls under CIP-011 BCSI definition per Lone Star's current classification | This has not been assessed; audit risk if the answer is yes and controls are inadequate |
| Who is the designated data owner for OT data in Azure | No data owner designated; IT and OT are both pointing at each other |
| What the retention and deletion policy is for OT data in Azure | Currently no formal policy; data accumulates indefinitely at 30-second granularity |
