# Project 05 — IT/OT Convergence Governance Policy

## Overview

Utilities are connecting OT historian servers to enterprise networks for analytics, reporting, and operational visibility. This breaks the traditional air-gap model that older security architectures assumed. The GRC challenge is not whether to allow convergence — business units are going to enable it with or without governance — but how to govern it so the organization can capture the business value without unknowingly expanding attack surface.

This project governs a specific convergence event: an AVEVA PI historian at Waco Junction Substation that was connected to the corporate network and is now replicating operational data to an Azure-hosted enterprise data lake. The connection was stood up informally three months ago without IT/OT security review. The policy is partially retroactive. The retroactive nature creates a finding that must be documented honestly.

## Scenario Summary

- **Organization:** Lone Star Transmission Services, LLC
- **Connection:** AVEVA PI historian (WJSS-008) → corporate LAN → Azure data lake
- **Data:** Real-time grid telemetry, equipment health, operational KPIs (no control commands)
- **Problem:** Business unit stood this up without governance review; 3 months of unauthorized operation
- **Cloud complication:** OT data is now leaving the facility network to Azure; CIP-011 implications
- **Stakeholders in conflict:** Operations (wants data), IT Security (cloud concern), OT Security (exposure concern), Compliance (CIP-007/011 documentation need)

## Files

| File | Purpose |
|------|---------|
| [scenario.md](./scenario.md) | Business driver, data flow description, stakeholder interests, what is unknown |
| [templates/convergence-policy-template.md](./templates/convergence-policy-template.md) | Governance policy with 8 sections |
| [templates/data-flow-risk-analysis.md](./templates/data-flow-risk-analysis.md) | Segment-by-segment risk analysis + MITRE ATT&CK threat scenario |
| [examples/annotated-reasoning-example.md](./examples/annotated-reasoning-example.md) | Completed risk analysis, retroactive finding language, cloud segment controls |
| [deliverables/](./deliverables/) | Completed policy and risk analysis outputs |

## What the Auditor Will Challenge

1. **This connection was stood up without review — what is the finding classification under your own policy?** And what is the remediation requirement and timeline?

2. **How do you ensure OT data in Azure is protected under CIP-011 Electronic Access Controls?** CIP-011 applies to BES Cyber System Information. If operational telemetry from a Medium impact substation is in Azure, what access controls govern that data?

3. **What prevents this data path from being used in reverse — commands flowing back toward the historian?** The historian is on the Control LAN. A compromised Azure tenant or enterprise network could potentially reach back through this path. What prevents it?

4. **Who approved the Azure tenant configuration, and is that documented?** The Azure tenant was provisioned by the business unit. Is there a documented configuration review, and does it meet Lone Star's cloud security standards for OT data?

5. **How does this policy interact with your incident response plan if the cloud tenant is breached?** If the Azure data lake containing OT telemetry is breached, what is the incident response and NERC notification process?

## Standards Referenced

- NERC CIP-007-6, Requirement R4 (Security event monitoring — convergence logging)
- NERC CIP-011-3 (Information protection — BES Cyber System Information)
- IEC 62443-3-2 (Zone and conduit — historian conduit to corporate/cloud)
- MITRE ATT&CK for ICS v2 (threat scenario mapping)
- NIST SP 800-82 Rev. 3 (OT security — convergence guidance)
