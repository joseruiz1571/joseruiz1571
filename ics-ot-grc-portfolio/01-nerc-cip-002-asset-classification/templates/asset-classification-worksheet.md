# Asset Classification Worksheet
## NERC CIP-002-5.1a — BES Cyber System Categorization

**Organization:** Lone Star Transmission Services, LLC
**Prepared by:** _(Compliance Analyst name)_
**Reviewed by:** _(OT Security Lead name)_
**Approved by:** _(Operations Manager name)_
**Date:** _______________
**Revision:** 1.0 — Initial Classification

---

## Instructions

1. For each asset, evaluate applicability against CIP-002-5.1a Attachment 1 criteria.
2. Start with High impact criteria (Attachment 1 §1). If no High criteria apply, evaluate Medium (§2). If no Medium criteria apply, classify Low or evaluate for exclusion.
3. Document the **specific Attachment 1 criterion** that drives the classification — "it seems important" is not a justification.
4. For excluded assets, document **why** the asset does not meet the BES Cyber Asset definition (i.e., why compromise would not impact the BES within 15 minutes) or why the grouping does not form a BES Cyber System.
5. All non-obvious classifications (including all High impact assignments) require secondary review by OT Security Lead before finalization.

---

## Classification Reference Summary

| Impact Level | Key Attachment 1 Criteria (abbreviated) |
|---|---|
| **High** | Control Centers operating Automatic Generation Control (AGC) or performing real-time monitoring of >1500 MW of generation; Transmission substations at certain voltage thresholds; Generation exceeding 1500 MW; certain SPS/RAS systems |
| **Medium** | Control Centers performing monitoring/control not meeting High thresholds; Transmission substations operating at ≥200 kV that are subject to certain interconnection characteristics; Generation 300–1500 MW; certain communication systems |
| **Low** | All other BES Cyber Systems that do not meet High or Medium criteria but are still part of a Responsible Entity's BES operations |
| **Not a BES Cyber Asset** | Assets that, if compromised, would not impact the BES within 15 minutes; assets not used in real-time operations; purely administrative assets |

---

## Classification Worksheet

> **Note:** Rows 1–4 are pre-filled as examples demonstrating the expected level of specificity. Rows 5–12 are for completion by the practitioner.

| Asset ID | Asset Name | Asset Type | Connected BES Functions | Proposed Impact Level | Attachment 1 Criterion | Justification Summary | Exclusion Rationale (if Not a BES Cyber Asset) |
|----------|-----------|-----------|------------------------|----------------------|----------------------|----------------------|----------------------------------------------|
| WJSS-001 | EMS Workstation | HMI / Operator Console | SCADA monitoring and control of Waco Junction 345 kV assets; ERCOT real-time telemetry link | **Medium** | Attachment 1 §2.3 — Transmission substations ≥200 kV subject to specific interconnection criteria (Waco Junction at 345 kV meets voltage threshold; does not meet the additional High criteria of §1.3 which require specific BES generation interconnection or qualifying SPS) | WJSS is a 345 kV switching substation without generation interconnection at or above 1500 MW. The EMS workstation controls and monitors these assets in real time. Medium classification per §2.3 is supported by voltage class. High was evaluated under §1.3 and rejected — see annotated reasoning example. | N/A — asset is a BES Cyber Asset |
| WJSS-002 | SCADA Data Concentrator | Data Concentrator / Communication Front-End | Aggregates SCADA telemetry from all WJSS and BJSS field devices; serves as the communication interface to WJSS-001 (EMS) | **Medium** | Attachment 1 §2.3 (same criterion as WJSS-001; this asset is part of the same BES Cyber System at WJSS and shares the classification of the controlling workstation) | The data concentrator is functionally inseparable from the EMS workstation for real-time monitoring and control operations. Compromise of this asset would interrupt SCADA visibility and control capability within 15 minutes. Grouped with WJSS-001 as part of the Waco Junction BES Cyber System. | N/A — asset is a BES Cyber Asset |
| WJSS-003 | Protective Relay — 345 kV Line 1 | Protective Relay (IED) | Line protection for the primary 345 kV transmission circuit at Waco Junction | **Medium** | Attachment 1 §2.6 — Protection Systems associated with transmission substations classified at Medium or High | The relay is a Protection System component for the 345 kV circuit at WJSS. The substation is Medium per §2.3. The relay therefore inherits Medium classification under §2.6. Note: if WJSS were classified High, the relays would be High. The relay does not independently qualify for High under §1.x criteria. | N/A — asset is a BES Cyber Asset |
| BJSS-004 | NTP Server / Timekeeping Appliance | Time Synchronization Appliance | Provides time sync to BJSS-001 (RTU) and BJSS-002/003 (protective relays) | **Not a BES Cyber Asset** | Not applicable — excluded | This asset provides time synchronization only. It has no control or monitoring function for BES operations. Compromise of this device (e.g., time drift) would not cause a BES operational impact within 15 minutes — relays would continue to operate using their last synchronized time reference, and protective functions are not time-dependent for trip execution. Additionally, the NTP server has serial-only connectivity with no IP network access. This device is excluded from BES Cyber System scope. | **Exclusion justification:** (1) Function is timekeeping only — not monitoring or control; (2) Loss of NTP sync does not impair relay trip function or SCADA operations within 15 minutes; (3) No network connectivity that could be a vector to other BES Cyber Assets; (4) Does not meet the BES Cyber Asset definition under NERC Glossary. **What would change this:** If this device were upgraded to IP-connected and provided synchronization directly to a time-dependent protection scheme (e.g., synchrophasor-based protection), the analysis would require re-evaluation. |
| WJSS-004 | Substation Automation Controller | PLC / Substation Automation Controller | Automatic switching sequences at WJSS; direct I/O to 345 kV breaker control circuits | _[Complete]_ | _[Identify specific Attachment 1 criterion]_ | _[Explain why this criterion applies and document the High vs. Medium argument before landing on a conclusion]_ | _[Complete only if excluded]_ |
| WJSS-005 | Protective Relay — 345 kV Line 2 | Protective Relay (IED) | Line protection for the secondary 345 kV transmission circuit at WJSS | _[Complete]_ | _[Identify specific Attachment 1 criterion]_ | _[Is the analysis parallel to WJSS-003, or are there differences? Explain]_ | _[Complete only if excluded]_ |
| WJSS-006 | Protective Relay — 345 kV Line 3 | Protective Relay (IED) | Line protection for the third 345 kV transmission circuit at WJSS | _[Complete]_ | _[Identify specific Attachment 1 criterion]_ | _[Is the analysis parallel to WJSS-003 and WJSS-005? If the analysis is identical, note that — but confirm it is actually identical]_ | _[Complete only if excluded]_ |
| WJSS-007 | IT/OT Boundary Switch | Managed Network Switch | Connects WJSS SCADA LAN to corporate WAN; enables historian replication | _[Complete — this is the other non-obvious asset; document the BES Cyber Asset vs. Protected Cyber Asset vs. exclusion argument]_ | _[Identify specific criterion, or note that no criterion applies and document why]_ | _[Key question: does this switch perform a function that, if compromised, would impact the BES within 15 minutes? Or is it a network infrastructure asset that enables access but does not itself perform BES functions?]_ | _[If excluded or classified as PCA rather than BES Cyber Asset, document the reasoning carefully]_ |
| WJSS-008 | Historian Server | Process Historian | Archives SCADA data; replicates to enterprise data lake — no control function | _[Complete]_ | _[Key question: historians are commonly debated. Does this asset qualify as a BES Cyber Asset, or is it excluded? What is the argument?]_ | _[Document the control function test: can this asset send commands to BES field devices? If not, that is relevant to the classification]_ | _[If excluded, explain the basis — particularly in light of the IT/OT connectivity through WJSS-007]_ |
| BJSS-001 | Remote Terminal Unit | RTU | SCADA telemetry from Brazos to Waco Junction; no direct control function (monitoring only per current configuration) | _[Complete]_ | _[Does the RTU qualify as a BES Cyber Asset? Does the Brazos 138 kV station meet Medium or Low criteria?]_ | _[Consider: what is the BES reliability impact of losing SCADA visibility to Brazos? Is the loss of monitoring equivalent to loss of control for BES classification purposes?]_ | _[Complete only if excluded]_ |
| BJSS-002 | Protective Relay — 138 kV Line A | Protective Relay (IED) | Line protection for 138 kV circuit feeding cooperative load | _[Complete]_ | _[Does a 138 kV relay at a station that only feeds cooperative distribution load qualify? Apply Attachment 1 criteria carefully — voltage class alone does not determine impact level]_ | _[What criterion, if any, causes this station to meet Medium? Or does it fall to Low?]_ | _[Complete only if excluded]_ |
| BJSS-003 | Protective Relay — 138 kV Line B | Protective Relay (IED) | Line protection for 138 kV circuit feeding cooperative load | _[Complete — analysis will parallel BJSS-002]_ | _[Same criteria as BJSS-002 — confirm the analysis is parallel]_ | _[If the classification differs from BJSS-002, explain why]_ | _[Complete only if excluded]_ |

---

## Classification Summary

| Impact Level | Asset Count | Asset IDs |
|---|---|---|
| High | _[#]_ | _[List]_ |
| Medium | _[#]_ | _[List]_ |
| Low | _[#]_ | _[List]_ |
| Not a BES Cyber Asset (excluded) | _[#]_ | _[List]_ |
| **Total assets reviewed** | **12** | |

---

## Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Analyst (Preparer) | Priya Nair | | |
| OT Security Lead (Reviewer) | Marcus Delgado | | |
| Operations Manager (Approver) | Scott Akers | | |

**Next review date:** ________________ (not to exceed 15 months from approval date per CIP-002 R1)

---

## Change Log

| Revision | Date | Author | Change Description |
|----------|------|--------|--------------------|
| 1.0 | ____________ | P. Nair | Initial classification exercise |
