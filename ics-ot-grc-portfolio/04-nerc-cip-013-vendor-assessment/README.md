# Project 04 — NERC CIP-013 Supply Chain Vendor Assessment

## Overview

NERC CIP-013 requires Responsible Entities to have a documented supply chain risk management plan covering software and hardware used in BES Cyber Systems. The standard is deliberately non-prescriptive — it requires a *plan* and *processes*, not a checklist. The judgment question is: given limited resources, which vendors get deep scrutiny, and what criteria actually matter when a vendor cannot produce standard documentation?

This project evaluates a sole-source firmware vendor for substation protective relays — a vendor with no SOC 2, no SBOM capability, and 40 employees — that is nonetheless the only qualified source for a security-critical firmware update. Approving them means accepting documentation gaps. Rejecting them means accepting an unpatched vulnerability. Both are real risks.

## Scenario Summary

- **Organization:** Lone Star Transmission Services, LLC
- **Vendor:** Relay Logic Partners, LLC (fictional sole-source ICS vendor)
- **Engagement:** Firmware update for protective relays at Waco Junction Substation (WJSS-003, WJSS-005, WJSS-006)
- **Stakes:** Relays are Medium impact BES Cyber System components; firmware update contains a critical security fix
- **Vendor profile:** 40 employees, no SOC 2, no formal SBOM program, sole-source qualifier
- **Dilemma:** Approve a poorly-documented vendor, or accept the unpatched vulnerability risk

## Files

| File | Purpose |
|------|---------|
| [scenario.md](./scenario.md) | Vendor relationship, firmware dilemma, what is known/unknown |
| [templates/vendor-assessment-questionnaire.md](./templates/vendor-assessment-questionnaire.md) | 6-section questionnaire with disqualifying answer notes |
| [templates/risk-narrative-template.md](./templates/risk-narrative-template.md) | Assessment findings and approval recommendation structure |
| [examples/annotated-reasoning-example.md](./examples/annotated-reasoning-example.md) | Full assessment for Relay Logic Partners with reasoning annotations |
| [deliverables/](./deliverables/) | Completed vendor assessment outputs |

## What the Auditor Will Challenge

1. **This vendor has no SOC 2 and no SBOM — why was it approved?** Walk me through the compensating controls that substituted for those missing assurance mechanisms.

2. **What contractual right do you have to audit this vendor?** If Relay Logic Partners has a security incident, does your contract give you the right to know? To audit their practices?

3. **How will you validate that the firmware update is what the vendor says it is?** Hash verification is table stakes — what else are you doing to confirm the firmware image's integrity before deploying it on 345 kV protection circuits?

4. **What ongoing monitoring is in place post-approval?** The assessment is a point-in-time snapshot. What happens when Relay Logic's practices change, or they have a breach, or they are acquired by a foreign entity?

5. **How does this connect to your CIP-013 plan as documented to NERC?** CIP-013 R1 requires a documented plan. Is this assessment process described in that plan, and is the vendor approval record linked to it?

## Standards Referenced

- NERC CIP-013-2, Requirements R1–R2
- NIST SP 800-161 Rev. 1 (Cybersecurity Supply Chain Risk Management)
- CISA ICT Supply Chain Risk Management guidance
