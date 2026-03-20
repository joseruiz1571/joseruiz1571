# Annotated Reasoning Example — NERC CIP-002 Asset Classification
## Lone Star Transmission Services, LLC

**Purpose:** This file walks through the Attachment 1 analysis for three representative assets — one Medium impact, one that required evaluating both High and Medium before landing, and one excluded asset. The `> [REASONING]` blocks after each decision step are the core of this document.

---

## How to Read This File

Each asset analysis:
1. States the asset and its basic function
2. Walks through Attachment 1 criteria in order (High first, then Medium)
3. Records a criterion determination (Applies / Does Not Apply) with reasoning
4. Ends with a classification decision and a note on what would change that decision

The `> [REASONING]` callout blocks explain *why* a criterion was evaluated the way it was — including the alternative interpretation and why it was rejected.

---

---

# Asset 1: WJSS-003 — Protective Relay, 345 kV Line 1
**Classification: Medium**
**Analysis type: Straightforward Medium; included to show the clean version before showing a hard case**

## Asset Summary
- **Function:** Line protection for the primary 345 kV transmission circuit at Waco Junction
- **Relevant connectivity:** DNP3 communication to WJSS-002 (SCADA data concentrator); no direct ERCOT link; no IP connectivity to corporate WAN
- **Operational role:** Automatically detects faults on the 345 kV circuit and initiates breaker trip within cycles. This is a protection function, not an operational control function.

---

## Step 1: Does this asset meet the BES Cyber Asset definition?

**Criterion:** Is this a programmable electronic device that, if compromised or unavailable, would within 15 minutes of its required operation adversely impact one or more Facilities, systems, or equipment that could impact the reliable operation of the BES?

**Determination: Yes.**

The relay performs an automatic protection function. If it fails to trip on a genuine fault, or if it is caused to trip spuriously, the impact on the 345 kV transmission line would be immediate. This is well within the 15-minute threshold.

> [REASONING]
> The 15-minute threshold is the threshold test that separates BES Cyber Assets from general IT assets in an OT environment. Protective relays are the clearest case: their required operation is measured in cycles (milliseconds), not minutes. A relay that fails to trip on a fault creates a condition that ERCOT protection coordination systems are designed to handle — but it is not a case where the impact is delayed or indirect.
>
> Some analysts argue that relays should be evaluated based on whether an *attacker* could compromise them in a way that causes an impact within 15 minutes, not just whether their *failure* would cause an impact. The standard text supports the former interpretation: "if compromised or unavailable." Unavailability includes both cyberattack-induced failure and compromised operation (e.g., a firmware modification that causes nuisance tripping or prevents legitimate tripping). WJSS-003 meets this threshold on both readings.

---

## Step 2: Attachment 1 §1 — High Impact Criteria

**Criterion §1.1:** Control Centers and backup Control Centers performing real-time monitoring or control of BES Cyber Systems.
**Determination: Does Not Apply.** This is a protective relay, not a Control Center.

**Criterion §1.2:** Transmission substations that are part of the applicable systems identified in Attachment 1.
**Determination: Does Not Apply** at the High level. WJSS is a 345 kV transmission substation. However, the High impact criteria for transmission substations under §1.3 require the substation to have specific characteristics: it must be a substation at which a fault would result in the de-energization of 1500 MW or more generation, or it must be part of a specific SPS/RAS scheme qualifying under §1.5. ERCOT load flow analysis does not indicate that faulting Waco Junction would de-energize ≥1500 MW of generation. WJSS does not qualify under §1.3.

> [REASONING]
> This is the distinction many CIP-002 practitioners miss. **345 kV ≠ High impact.** The voltage class is a factor in the Medium criteria (§2.3 captures substations operating above certain voltage thresholds with qualifying interconnection characteristics), but the High criteria for substations are more specific — they focus on the operational consequence of losing the substation, not just its voltage class.
>
> At Lone Star's scale (a transmission-only operator with two substations), meeting the High threshold would require WJSS to be a node at which generation at or above 1500 MW interconnects, or a node whose loss would trigger qualifying system impacts. The ERCOT transmission planning record does not support that characterization for WJSS. The compliance team documented this by referencing the specific ERCOT contingency analysis on file with the company.
>
> The temptation to over-classify — to call things High because it feels safer — is a real dynamic in CIP compliance. The cost is high: High impact BES Cyber Systems carry significantly greater CIP-003 through CIP-011 requirements. At Lone Star's resourcing level (2 FTE compliance team), over-classification would make an audit-ready compliance program practically unachievable. The conservative choice is to correctly classify, not to inflate.

**Criterion §1.5:** Special Protection Systems (SPS) or Remedial Action Schemes (RAS).
**Determination: Does Not Apply.** WJSS does not host a qualifying SPS/RAS.

**Conclusion, High criteria:** None of the §1 High impact criteria apply to WJSS-003 or to the Waco Junction substation at which it operates.

---

## Step 3: Attachment 1 §2 — Medium Impact Criteria

**Criterion §2.3:** Transmission substations that meet the criteria in Attachment 1 §2.3.

The current version of CIP-002-5.1a §2.3 captures transmission substations operated at ≥200 kV at which a BES transmission element operates at ≥200 kV and is directly connected to another transmission substation with a similar voltage threshold (i.e., a substation that, if lost, would create a single contingency impacting the BES above the qualifying threshold in the applicable footprint).

**Determination: Applies.** WJSS operates at 345 kV. Three 345 kV lines terminate here, connecting to other transmission nodes. The station meets the voltage and interconnection characteristics in §2.3. WJSS is a Medium impact transmission substation.

**Criterion §2.6:** Protection Systems associated with Transmission substations identified as Medium or High.

**Determination: Applies.** WJSS-003 is a Protection System component associated with WJSS, which is classified Medium under §2.3. The relay inherits Medium classification under this criterion.

> [REASONING]
> §2.6 is a derivative criterion — it classifies protection system components based on the classification of the substation they protect. This is intentional: the protection system is what prevents a fault on a Medium impact circuit from becoming a cascading event. The relay cannot independently qualify for High without the substation also qualifying for High. In this case, the substation is Medium, so the relay is Medium.
>
> Some practitioners ask whether the relay should be classified independently against the BES impact criteria, rather than deriving its classification from the substation. The standard text does not support that approach for protection systems. §2.6 explicitly addresses protection systems at Medium and High substations and does not require independent Attachment 1 analysis for each relay. This is worth documenting because auditors sometimes ask about the classification basis for relays, and "it's a relay at a Medium substation" is the complete answer under §2.6.

---

## Classification Decision

**WJSS-003: Medium Impact BES Cyber Asset**
**Basis:** Attachment 1 §2.6 — Protection System associated with Waco Junction Substation, classified Medium under §2.3.
**What would change this:** If Waco Junction were re-evaluated and classified High (e.g., due to a change in the interconnected generation profile that causes WJSS to meet the §1.3 threshold), WJSS-003 would also move to High.

---

---

# Asset 2: WJSS-004 — Substation Automation Controller
**Classification: Medium (after evaluating the High argument)**
**Analysis type: Non-obvious — both the High argument and the Medium argument are presented before reaching a conclusion**

## Asset Summary
- **Function:** Executes automatic switching sequences at Waco Junction for voltage regulation purposes; can open and close 345 kV breakers via direct I/O to control circuits
- **Connectivity:** Substation LAN; direct I/O to breaker control circuits; no direct ERCOT link; no corporate WAN connectivity as of this classification review
- **Operational role:** This is not passive. The SAC makes and executes switching decisions autonomously in response to voltage and load conditions. Unlike a relay (which reacts to faults), the SAC operates under steady-state and near-steady-state conditions to maintain power quality.

---

## Step 1: BES Cyber Asset Definition Test

**Determination: Yes.**

The SAC can open and close 345 kV breakers. Unauthorized operation — whether through direct compromise or a logic manipulation that causes improper switching — would affect BES operations immediately. This is unambiguous.

---

## Step 2: Attachment 1 §1 — High Impact Evaluation

**Criterion §1.3:** Transmission substations at which the following conditions apply: [qualifying generation interconnection or system impact thresholds].

This is the relevant criterion. The question is not whether WJSS-004 is an important asset — it clearly is. The question is whether **the substation at which it operates** qualifies as High under §1.3.

> [REASONING]
> The High vs. Medium question for WJSS-004 is not really about the SAC itself — it is about the substation it operates within. CIP-002 Attachment 1 classifies BES Cyber Systems based on the characteristics of the Facilities they support, not on the individual capabilities of each device. A SAC at a High impact substation would be High. A SAC at a Medium impact substation would be Medium. The device's ability to operate breakers on 345 kV infrastructure is what makes it a BES Cyber Asset, but it does not independently determine the impact level.
>
> This is a point of confusion in some compliance programs: people look at what a device *can do* (operate 345 kV breakers) and assume that capability drives the classification level. It does not, under Attachment 1. The classification is driven by the substation's characteristics under the applicable criteria.

**Argument for High:** The SAC has direct control authority over 345 kV breakers. Compromise of this device could cause a deliberate mis-switching event that creates a sustained outage at a critical transmission node. Given the load served from the Waco Junction corridor (~180,000 customers per ERCOT load flow), the argument is that this device warrants High classification regardless of the formal substation criteria, because the consequence of compromise is high-impact by any reasonable measure.

**Why this argument fails under Attachment 1:** CIP-002-5.1a Attachment 1 does not classify assets based on consequence of targeted attack alone. The High impact criteria are defined by specific operational characteristics of the Facility (generation interconnection thresholds, SPS/RAS presence, specific load thresholds). WJSS does not meet those specific thresholds. The standard is clear that consequence-based reasoning cannot substitute for the defined criteria.

> [REASONING]
> This is an important intellectual discipline in CIP compliance: the standard's defined criteria are the classification standard, not a practitioner's independent judgment about what seems important. If the compliance team believes the standard's criteria under-classify a genuinely high-risk asset, the correct response is to (1) document that concern, (2) apply the standard correctly, and (3) consider whether compensating security measures are warranted beyond what the standard requires. The incorrect response is to over-classify to satisfy intuition about risk — doing so creates a compliance program that cannot be explained to an auditor without self-contradiction.
>
> That said, Lone Star should document the following in the classification record: "WJSS-004 is classified Medium under Attachment 1 §2.3/§2.x criteria applicable to WJSS. The compliance team notes that this asset has direct breaker control authority over 345 kV infrastructure and recommends that enhanced monitoring and access controls be applied at the High impact level voluntarily, as a risk management measure beyond the minimum compliance requirement." That is a defensible position that is honest about both the classification and the underlying risk.

**Conclusion, High criteria:** The SAC does not independently qualify for High. WJSS does not meet the §1.3 High threshold. High classification is rejected.

---

## Step 3: Attachment 1 §2 — Medium Impact Evaluation

**Criterion §2.3 / §2.x:** SAC operates within WJSS. WJSS is Medium. The SAC is part of the WJSS BES Cyber System.

**Determination: Medium.**

**What would change this:** If WJSS were reclassified High, or if the SAC were networked into a qualifying Control Center, the SAC would be re-evaluated. Additionally, if ERCOT modifies its contingency analysis in a way that causes WJSS to meet the §1.3 High criteria, this classification must be re-opened.

---

## Classification Decision

**WJSS-004: Medium Impact BES Cyber Asset**
**Basis:** Attachment 1 §2.x — asset is part of the Waco Junction BES Cyber System, classified Medium under §2.3. The High argument was evaluated and rejected on the basis that WJSS does not meet §1.3 High substation criteria.
**Documented note:** Compliance team recommends voluntary application of High-equivalent access controls to this asset given its direct breaker control authority. This recommendation is a risk management measure, not a compliance reclassification.

---

---

# Asset 3: BJSS-004 — NTP Server / Timekeeping Appliance
**Classification: Not a BES Cyber Asset (Excluded)**
**Analysis type: Exclusion with documented rationale and explicit statement of what would change the analysis**

## Asset Summary
- **Function:** Provides time synchronization signals to BJSS-001 (RTU) and BJSS-002/003 (protective relays) at Brazos Switching Station
- **Connectivity:** Serial connections only; no IP network access; does not communicate with any device outside the Brazos control cabinet
- **Physical location:** Brazos Switching Station control cabinet

---

## Step 1: BES Cyber Asset Definition Test

**Criterion:** Programmable electronic device that, if compromised or unavailable, would within 15 minutes of its required operation adversely impact BES operations.

> [REASONING]
> Before running the Attachment 1 criteria, the foundational question must be answered: is this a BES Cyber Asset at all? If it fails the BES Cyber Asset definition, no further Attachment 1 analysis is required.
>
> The NTP server's function is timekeeping. Two questions drive the analysis:
> 1. If this device is unavailable (e.g., fails), do the relays and RTU stop functioning within 15 minutes?
> 2. If this device is compromised (e.g., its time signals are manipulated), does that adversely impact BES operations within 15 minutes?
>
> For question 1: protective relays store their last synchronized time and continue operating using that reference. A loss of NTP sync does not cause a relay to stop tripping on fault. The 15-minute operational impact test is not met.
>
> For question 2: time manipulation could theoretically affect time-stamping of event logs, but it would not affect the relay's trip logic or the RTU's ability to transmit telemetry. Synchrophasor-based protection schemes ARE time-dependent in ways that NTP compromise could affect — but Brazos is not running a synchrophasor protection scheme. The relays at BJSS are conventional overcurrent and distance protection, not synchrophasor-based.

**Determination: Does Not Meet BES Cyber Asset Definition.**

The NTP server's unavailability or compromise would not cause an adverse impact on BES-connected Facilities within 15 minutes. Time synchronization supports logging and coordination functions but is not a real-time operational control or protection function at this site.

---

## Step 2: Secondary Analysis — Excluded or Protected Cyber Asset?

Even assets excluded from BES Cyber Asset classification may qualify as Protected Cyber Assets (PCAs) if they are within an Electronic Security Perimeter (ESP). PCAs carry their own CIP-003 obligations.

**Relevant question:** Is BJSS-004 within an established ESP?

**Determination:** BJSS currently has no formally established ESP. The SCADA link from BJSS to WJSS-002 is a serial (non-routable) link, and serial links do not create an ESP connection under CIP-005. BJSS-004 is not within an ESP and therefore does not qualify as a PCA under CIP-006.

> [REASONING]
> This is a consequential determination. If BJSS ever receives an IP-connected network upgrade (which the scenario notes is in planning), the ESP question will need to be revisited. A future IP connection from BJSS to the WJSS LAN would potentially bring BJSS assets inside an ESP, at which point BJSS-004 would need to be re-evaluated — both as a potential BES Cyber Asset and as a potential PCA.
>
> The compliance team's obligation is to document this condition: "BJSS-004 is currently excluded from BES Cyber Asset classification and is not within an established ESP. If BJSS network connectivity is upgraded from serial to IP, this determination must be re-evaluated before the new connectivity is operationalized." That sentence in the classification record converts a future-state risk into a managed condition.

---

## Exclusion Decision

**BJSS-004: Not a BES Cyber Asset**
**Basis:** Does not meet BES Cyber Asset definition — loss or compromise of this device would not adversely impact BES operations within 15 minutes given current BJSS architecture (conventional relay protection, serial-only connectivity, no synchrophasor scheme).
**Not a PCA:** No established ESP at BJSS under current serial-link architecture.

**What would change this exclusion:**
1. Upgrade of BJSS network connectivity to IP-based — triggers ESP determination and re-evaluation
2. Implementation of synchrophasor-based protection at BJSS — time synchronization would become operationally critical, potentially meeting the BES Cyber Asset definition
3. Connection of the NTP server to devices that are BES Cyber Assets within an established ESP — converts the NTP server to a PCA regardless of the BES Cyber Asset analysis

---

## Cross-Reference Note

The BJSS-004 exclusion rationale documented above should be cross-referenced in the project change management log. Specifically, the planned BJSS IP connectivity upgrade (referenced in scenario.md) must trigger a mandatory re-evaluation of all BJSS asset classifications before that project goes live. Priya Nair (Compliance Analyst) should coordinate with Diana Flores (Substation Engineering Lead) to ensure classification review is part of the project change control gate.
