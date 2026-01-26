# AI Project Documentation for Compliance: Bridging Daily Work and Framework Requirements

*A practical guide to making your existing project artifacts audit-ready for ISO 42001, NIST AI RMF, and EU AI Act compliance.*

---

## Introduction: The Lightbulb Moment

Here's a realization that changes everything about AI compliance: the messy, day-to-day tactical work of AI project management is actually the exact evidence auditors look for.

That Jira ticket you created to track a data quality issue? That's evidence of operational control under ISO 42001 Clause 8.1. The trade-off discussion in your meeting notes about choosing between model accuracy and inference speed? That's documented risk treatment per NIST AI RMF MANAGE-4. The spreadsheet where your team scored risks on a 1-5 scale? That's your risk assessment methodology per Clause 6.1.2.

Most AI teams are already creating compliance artifacts. They just don't realize it.

The goal isn't to create new work for compliance—it's to ensure existing project artifacts are "framework-ready." This means adding the right metadata, establishing proper retention practices, and understanding which framework requirements each artifact satisfies. The gap isn't usually in doing the work; it's in capturing it with sufficient context to prove you did it.

This matters for three reasons. First, certification pressure is mounting as organizations pursue ISO 42001 certification or need to demonstrate NIST AI RMF alignment. Second, regulatory requirements under the EU AI Act create explicit documentation obligations for high-risk systems. Third, when something goes wrong (and eventually it will), your audit trail becomes your defense—showing that you identified risks, made informed decisions, and implemented appropriate controls.

This guide provides a framework for understanding what to track regardless of your tooling. Whether you use Jira, Linear, Asana, Notion, or spreadsheets, the principles remain the same.

---

## Part 1: Essential AI Project Artifacts Matrix

The following matrix maps common project artifacts to their compliance purposes across three major frameworks. Each artifact represents something most AI teams already produce—the question is whether it's captured in a way that serves as governance evidence.

### 1. Risk Assessment/Register

**What project teams call it:** Risk register, risk log, risk backlog

**Description:** A structured inventory of identified risks to the AI system, typically including likelihood and impact scores, risk categories, and current status. Often maintained in project management tools or spreadsheets.

**Compliance Purpose:** Demonstrates systematic identification and evaluation of AI-specific risks, showing that the organization doesn't operate blind to potential harms. Auditors look for evidence that risks were identified proactively, not just reactively.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 6.1.2 (AI risk assessment), Annex A.5.2 (AI system risk assessment) |
| NIST AI RMF | MAP-1 (Context established), MEASURE-2 (Metrics tracked), MEASURE-3 (Impacts analyzed) |
| EU AI Act | Article 9 (Risk management system for high-risk AI) |

**Key Fields to Capture:**
- Unique risk ID (for traceability)
- AI system/model ID (links to specific system in scope)
- Risk description and category (technical, legal, operational, ethical)
- Inherent risk score (before controls)
- Residual risk score (after controls)
- Risk owner (named individual, not just a team)
- Date identified and last review date
- Assessment methodology used (e.g., SWIFT, FMEA, semi-quantitative)

**Retention Consideration:** Retain for the operational life of the AI system plus 3-5 years post-decommissioning. Risk registers serve as historical evidence of due diligence if issues emerge after a system is retired.

---

### 2. Risk Treatment Plan/Tickets

**What project teams call it:** Mitigation tickets, risk response tasks, control implementation work items

**Description:** Actionable work items that address identified risks. These are the Jira tickets, GitHub issues, or Asana tasks that track actual mitigation work—what's being done, by whom, and when.

**Compliance Purpose:** Shows that risks aren't just identified but actively managed. Provides evidence of operational control and demonstrates that the organization moves from awareness to action.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 6.1.3 (AI risk treatment), Clause 8.1 (Operational planning and control), Annex A.6 (Controls for AI systems) |
| NIST AI RMF | MANAGE-1 (Risks prioritized/responded to), MANAGE-2 (Risk treatment plans implemented) |
| EU AI Act | Article 9(4) (Elimination or mitigation of risks) |

**Key Fields to Capture:**
- Link to parent risk ID (traceability)
- Treatment type (mitigate, transfer, accept, avoid)
- Implementation status and dates
- Assigned owner and approver
- Success criteria or acceptance threshold
- Evidence of completion (test results, deployment confirmation)
- Residual risk after implementation

**Retention Consideration:** Retain alongside the parent risk record. Treatment tickets are evidence that you did something about identified risks—this is often more valuable than the risk identification itself.

---

### 3. Trade-off Decision Matrix

**What project teams call it:** Decision matrix, options analysis, trade-off table, ADR (architecture decision record)

**Description:** Documentation of choices made when competing factors couldn't all be optimized. Common examples include accuracy vs. privacy, speed vs. cost, transparency vs. competitive advantage, or fairness across different demographic groups.

**Compliance Purpose:** Demonstrates informed decision-making rather than arbitrary choices. Shows that trade-offs were explicit, considered multiple stakeholders, and were approved by appropriate authority. This is often the most overlooked compliance artifact.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Annex A.5.3 (AI system impact assessment), Annex A.6.2.6 (Trade-offs documentation) |
| NIST AI RMF | GOVERN-5 (Risk processes integrated), MANAGE-4 (Trade-offs managed) |
| EU AI Act | Article 9(3) (Balancing risks with benefits) |

**Key Fields to Capture:**
- Decision context and alternatives considered
- Evaluation criteria and weights
- Stakeholders involved
- Final decision and rationale
- Decision authority (who approved)
- Date of decision
- Conditions for revisiting the decision

**Retention Consideration:** Permanent retention recommended. Trade-off decisions explain why the system behaves as it does—critical for incident response and regulatory inquiries years later.

---

### 4. AI System Impact Assessment

**What project teams call it:** Impact assessment, DPIA (data protection impact assessment), algorithmic impact assessment, AIIA

**Description:** Systematic analysis of potential impacts on individuals, groups, and society from the AI system's deployment. Covers rights impacts, safety considerations, fairness implications, and societal effects.

**Compliance Purpose:** Demonstrates consideration of broader impacts beyond technical performance. Required for high-risk systems under the EU AI Act and strongly implied by ISO 42001 and NIST AI RMF.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Annex A.5 (AI impact assessment), specifically A.5.3 and A.5.4 |
| NIST AI RMF | MAP-2 (Categorization), MAP-5 (Impacts characterized) |
| EU AI Act | Article 9 (Risk management), Article 13 (Transparency), Article 29 (Fundamental rights impact assessment for deployers) |

**Key Fields to Capture:**
- AI system scope and use case description
- Affected stakeholders and groups
- Potential positive and negative impacts
- Likelihood and severity assessments
- Mitigation measures for negative impacts
- Review and update schedule
- Approval and sign-off records

**Retention Consideration:** Retain for system lifetime plus regulatory limitation periods (typically 5-7 years). May be required for regulatory submissions.

---

### 5. Model Technical Documentation

**What project teams call it:** Model card, model documentation, technical spec, model registry entry

**Description:** Technical details of the AI model including architecture, training data characteristics, validation approach, performance metrics, known limitations, and intended use cases.

**Compliance Purpose:** Provides the technical evidence base for claims about system capabilities and limitations. Required for EU AI Act conformity assessments and essential for demonstrating NIST AI RMF MEASURE function.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Annex A.6.2.4 (Documentation of AI system), Annex A.7.2 (Data for AI systems) |
| NIST AI RMF | MEASURE-1 (Appropriate methods selected), MEASURE-2 (Metrics tracked) |
| EU AI Act | Article 11 (Technical documentation), Annex IV (Technical documentation content) |

**Key Fields to Capture:**
- Model architecture and version
- Training data sources, characteristics, and limitations
- Validation methodology and results
- Performance metrics with confidence intervals
- Known limitations and failure modes
- Intended use and out-of-scope uses
- Hardware/software requirements
- Authors and last update date

**Retention Consideration:** Retain for 10 years after the AI system is placed on the market or put into service (EU AI Act requirement for high-risk systems). Version all updates.

---

### 6. Data Governance Records

**What project teams call it:** Data dictionary, data lineage docs, data quality reports, provenance records

**Description:** Documentation of data sources, quality characteristics, transformations, and governance controls applied to training and operational data.

**Compliance Purpose:** Demonstrates appropriate data stewardship and enables traceability from model behavior back to training data characteristics. Essential for investigating bias or performance issues.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Annex A.7 (Data for AI systems), specifically A.7.2 (Data acquisition), A.7.3 (Data quality), A.7.5 (Data provenance) |
| NIST AI RMF | MAP-4 (Risks and benefits mapped), MEASURE-2.7 (Data quality assessed) |
| EU AI Act | Article 10 (Data and data governance) |

**Key Fields to Capture:**
- Data source identification and acquisition method
- Data quality metrics and assessment dates
- Bias testing results and mitigation applied
- Data transformations and preprocessing steps
- Retention and deletion schedules
- Access controls and usage restrictions
- Consent and legal basis for processing

**Retention Consideration:** Retain data governance records as long as the model trained on that data remains in use, plus an additional period for audits.

---

### 7. Deployment and Change Management Plans

**What project teams call it:** Deployment runbook, release notes, change request, rollback plan

**Description:** Documentation of how the AI system is deployed, updated, and managed in production, including versioning, rollback procedures, and change approval workflows.

**Compliance Purpose:** Shows controlled deployment practices and the ability to respond to incidents. Demonstrates that changes to AI systems follow a governed process rather than ad-hoc modifications.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 8.1 (Operational planning and control), Annex A.6.2.3 (AI system verification and validation) |
| NIST AI RMF | MANAGE-3 (Post-deployment monitoring planned), GOVERN-1.5 (Deployment decisions governed) |
| EU AI Act | Article 12 (Record-keeping), Article 17 (Quality management system) |

**Key Fields to Capture:**
- Deployment environment specifications
- Version identifiers and change description
- Pre-deployment testing results
- Approval chain and sign-offs
- Rollback procedures and triggers
- Monitoring thresholds for deployment success
- Communication plan for stakeholders

**Retention Consideration:** Retain deployment records for the system lifetime. Rollback capability requires maintaining access to previous versions.

---

### 8. Event Logs and Monitoring Records

**What project teams call it:** System logs, monitoring dashboards, drift reports, incident tickets

**Description:** Automated and manual records of system behavior, performance, anomalies, and incidents during operation. Includes performance metrics, drift detection alerts, and user feedback.

**Compliance Purpose:** Provides evidence of ongoing monitoring and the ability to detect issues. Essential for incident investigation and demonstrating continuous compliance rather than point-in-time certification.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 9.1 (Monitoring, measurement, analysis, and evaluation), Annex A.6.2.7 (AI system operation and monitoring) |
| NIST AI RMF | MEASURE-4 (Feedback gathered), MANAGE-3 (Post-deployment monitoring) |
| EU AI Act | Article 12 (Record-keeping), Article 72 (Reporting of serious incidents) |

**Key Fields to Capture:**
- Timestamp and event type
- System/model version in operation
- Performance metrics vs. baselines
- Anomaly indicators and thresholds breached
- User complaints or feedback
- Incident classification if applicable
- Response actions taken

**Retention Consideration:** Operational logs typically 1-2 years; incident-related logs retained longer (5+ years). EU AI Act requires logs enabling traceability throughout the system's lifetime.

---

### 9. Management Review Minutes

**What project teams call it:** Leadership review notes, steering committee minutes, governance board records

**Description:** Documentation of leadership oversight activities including review of AI system performance, risk posture, resource allocation, and strategic decisions about AI initiatives.

**Compliance Purpose:** Demonstrates "tone at the top" and active governance rather than delegated-and-forgotten oversight. Required by ISO 42001 and strongly implied by NIST AI RMF GOVERN function.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 9.3 (Management review), Clause 5.1 (Leadership and commitment) |
| NIST AI RMF | GOVERN-1 (Governance structures established), GOVERN-2 (Accountability structures) |
| EU AI Act | Article 17 (Quality management system) |

**Key Fields to Capture:**
- Meeting date, attendees, and roles
- Agenda items and AI systems reviewed
- Decisions made with rationale
- Action items assigned with owners and deadlines
- Resource allocation decisions
- Escalated risks and strategic direction
- Sign-off by appropriate authority

**Retention Consideration:** Retain for 5-7 years minimum. Management review records demonstrate governance continuity across personnel changes.

---

### 10. Internal Audit Reports

**What project teams call it:** Audit findings, compliance assessment, AIMS audit report

**Description:** Formal assessment of whether AI management practices conform to internal policies and external framework requirements. Identifies gaps and tracks remediation.

**Compliance Purpose:** Provides independent verification of compliance claims. Required for ISO 42001 certification and considered best practice under NIST AI RMF.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 9.2 (Internal audit) |
| NIST AI RMF | GOVERN-4 (Organizational practices reviewed) |
| EU AI Act | Article 17 (Quality management system including audits) |

**Key Fields to Capture:**
- Audit scope and criteria
- AI systems and processes assessed
- Findings classified by severity
- Evidence reviewed and gaps identified
- Recommendations with priority
- Management response and remediation plan
- Follow-up audit schedule

**Retention Consideration:** Retain for two audit cycles minimum (typically 6 years for annual audits). Audit trails support certification maintenance.

---

### 11. Nonconformity and Corrective Action Logs

**What project teams call it:** Bug tracker, incident log, problem tickets, exception register

**Description:** Records of when things didn't go as planned—whether policy violations, control failures, incidents, or audit findings—and what was done to fix them.

**Compliance Purpose:** Demonstrates a learning organization that identifies problems and implements improvements. The absence of nonconformities is a red flag; their presence with corrective actions shows maturity.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 10.2 (Nonconformity and corrective action) |
| NIST AI RMF | MANAGE-2.4 (Incidents documented), GOVERN-4 (Continuous improvement) |
| EU AI Act | Article 72 (Serious incident reporting), Article 20 (Corrective actions) |

**Key Fields to Capture:**
- Nonconformity description and discovery date
- Root cause analysis
- Immediate containment actions
- Corrective actions to prevent recurrence
- Owner and target completion date
- Verification of effectiveness
- Closure approval and date

**Retention Consideration:** Retain for 5+ years. Nonconformity patterns over time reveal systemic issues and demonstrate improvement trajectories.

---

### 12. Competence Records

**What project teams call it:** Training records, skill matrix, certification tracker, team capabilities

**Description:** Documentation of personnel qualifications, training completed, and demonstrated competencies relevant to AI development, deployment, and governance roles.

**Compliance Purpose:** Shows that people working on AI systems have appropriate knowledge and skills. Required for quality management and demonstrates due diligence in team composition.

| Framework | Mapping |
|-----------|---------|
| ISO 42001 | Clause 7.2 (Competence), Clause 7.3 (Awareness) |
| NIST AI RMF | GOVERN-3 (Workforce diverse/knowledgeable), GOVERN-3.2 (Training adequate) |
| EU AI Act | Article 14 (Human oversight competence) |

**Key Fields to Capture:**
- Personnel identifier and role
- Required competencies for role
- Training completed with dates
- Certifications held with expiry
- Demonstrated competencies (project experience)
- Gap analysis and development plans
- Records of awareness training

**Retention Consideration:** Retain during employment plus 3-5 years. Consider longer retention for personnel who made key decisions on high-risk systems.

---

## Part 2: The Three Elements for Audit-Proofing

Creating project artifacts is necessary but not sufficient. To make them "framework-ready," each artifact needs three elements that transform it from project documentation into governance evidence.

### Traceability

Can you link this artifact to a specific AI system, model version, or decision point?

Traceability answers the question: "Which AI system does this relate to?" Without clear identifiers connecting artifacts to specific systems, auditors cannot verify that required documentation exists for each AI system in scope. This seems obvious, but many organizations fail here—they have risk registers without AI system IDs, meeting minutes without model version references, or training records without role assignments.

Practical implementation means every artifact should include an AI system identifier that maps to your AI Management System scope. If you're documenting a risk, specify which model version it affects. If you're recording a decision, note which deployment it applies to. This identifier should be consistent across all your systems—the same system should have the same ID in your risk register, your model registry, your change management system, and your audit reports.

### Evidence of Review

Is there a digital signature, approval status, or signed-off decision from a Risk Owner or Manager?

Evidence of review answers the question: "Who verified this, and when?" Artifacts without approval trails could have been created by anyone at any time—they don't demonstrate organizational accountability. Risk acceptance without documented approval from the appropriate authority is indistinguishable from risk ignorance.

Practical implementation means building approval workflows into your processes. When a risk is accepted, the risk owner (a named individual with authority) must explicitly approve. When a deployment proceeds, someone with appropriate authority signs off. These don't need to be physical signatures—status transitions in issue trackers, approval buttons in workflow tools, or even email confirmations can serve as evidence when properly retained.

### The "Why"

Is there context explaining the rationale behind scores, decisions, or trade-offs?

The "why" answers the question: "What informed this decision?" A risk score of "High" without explanation doesn't demonstrate thoughtful assessment. A trade-off decision without rationale looks arbitrary. Context transforms checkbox compliance into demonstrated judgment.

Practical implementation means requiring rationale fields in your templates. When assigning a likelihood score, document why you chose that value. When accepting a residual risk, explain what makes it acceptable. When selecting one option over another, record the factors that drove the choice. Future you (and future auditors) will need to understand what present you was thinking.

---

## Part 3: Platform-Agnostic Implementation Guide

The following field list works in any system—Jira, Linear, Asana, Notion, spreadsheets, or custom databases. The tool matters less than capturing the right information consistently.

### Core Fields for Risk and Artifact Tracking

**Identification Fields:**
- Record ID: Unique identifier (auto-generated where possible)
- AI System ID: Link to the AI system this record relates to
- Model Version: Specific version affected (if applicable)
- Record Type: Risk, decision, finding, action, etc.
- Title: Brief descriptive name
- Description: Full context and details

**Classification Fields:**
- Category: Technical, legal, operational, ethical, safety
- Severity/Priority: Using your chosen scale
- Status: Current state in workflow
- Created Date: When first recorded
- Last Updated: Most recent modification

**Ownership and Accountability:**
- Owner: Individual responsible (name, not just role)
- Approver: Authority for decisions/sign-offs
- Stakeholders: Others with interest or input

**Traceability Fields:**
- Related Records: Links to connected items
- Framework Mapping: ISO 42001 clause, NIST function, EU AI Act article
- Source: How this was identified (audit, incident, proactive, etc.)

**Lifecycle Fields:**
- Target Date: When action should complete
- Actual Completion: When actually resolved
- Review Date: Next scheduled review
- Retention Period: How long to keep this record

### Recommended Workflow States

Standard project management workflows (To Do → In Progress → Done) are insufficient for compliance. Risk management requires states that reflect the compliance lifecycle.

**For Risk Records:**
1. **Identified** – Risk has been documented but not yet assessed
2. **Under Assessment** – Actively evaluating likelihood, impact, and controls
3. **Treatment Open** – Mitigation or response actions are in progress
4. **Pending Review** – Treatment complete, awaiting verification
5. **Risk Accepted** – Residual risk formally accepted by appropriate authority
6. **Closed - Mitigated** – Risk eliminated or reduced to acceptable level
7. **Monitoring** – Ongoing tracking for recurrence or changes

**For Decisions:**
1. **Proposed** – Option under consideration
2. **Under Analysis** – Gathering information and stakeholder input
3. **Pending Approval** – Analysis complete, awaiting decision authority
4. **Approved** – Decision made and documented
5. **Implemented** – Decision executed
6. **Superseded** – Replaced by newer decision

**For Audit Findings:**
1. **Finding Documented** – Issue identified and recorded
2. **Root Cause Analysis** – Investigating underlying causes
3. **Corrective Action Planned** – Response defined
4. **Implementation In Progress** – Fixes being applied
5. **Verification Pending** – Awaiting confirmation of effectiveness
6. **Closed - Verified** – Corrective action confirmed effective

### Automation Opportunities

Regardless of platform, certain automations significantly improve compliance posture.

**Threshold-Based Escalation:** When a risk score exceeds defined thresholds, automatically notify the appropriate authority. A critical risk sitting unacknowledged for days is a governance failure.

**Recurring Risk Generation:** Some risks should be reassessed on a schedule (quarterly model drift reviews, annual bias audits). Automate the creation of recurring assessment tasks rather than relying on memory.

**Stale Record Alerts:** If a record in an active state hasn't been updated in a defined period, flag it for attention. Risks shouldn't languish indefinitely in "Under Assessment."

**Audit Snapshot Exports:** Monthly or quarterly, automatically export your risk register and decision log to a static format (CSV, PDF) with timestamps. These snapshots provide point-in-time evidence that's independent of ongoing system changes.

**Approval Gate Enforcement:** Before allowing transition to certain states (like "Risk Accepted"), require mandatory fields or attachments (like completed decision matrices or approver sign-off).

---

## Part 4: Reference Tables

### ISO 42001 Mandatory Documented Information

| Category | Document | Clause Reference |
|----------|----------|------------------|
| **Foundational** | AIMS Scope | 4.3 |
| | AI Policy | 5.2 |
| | AI Objectives | 6.2 |
| **Risk** | Risk Assessment Process | 6.1.2 |
| | Risk Treatment Plan | 6.1.3 |
| **Evidence** | Statement of Applicability | Annex A reference |
| **Operational** | Operational Controls | 8.1 |
| | AI System Impact Assessment | Annex A.5 |
| **Technical** | AI System Documentation | Annex A.6.2.4 |
| | Data Governance Records | Annex A.7 |
| **Assurance** | Internal Audit Results | 9.2 |
| | Management Review Records | 9.3 |
| **Improvement** | Nonconformity Records | 10.2 |
| | Corrective Action Records | 10.2 |

### Project Activity to Framework Mapping

| Daily Project Activity | What It Actually Is | NIST AI RMF | ISO 42001 |
|------------------------|--------------------|--------------| ----------|
| Risk brainstorming session | Context establishment and risk identification | MAP-1, MAP-2 | 6.1.2 (Identification) |
| Assigning likelihood/impact scores | Risk quantification and prioritization | MEASURE-2, MEASURE-3 | 6.1.2 (Evaluation) |
| Creating mitigation Jira tickets | Risk treatment implementation | MANAGE-1, MANAGE-2 | 6.1.3, 8.1 |
| Choosing between design options | Trade-off management | GOVERN-5, MANAGE-4 | Annex A.6.2.6 |
| Reviewing model metrics dashboards | Performance monitoring | MEASURE-4, MANAGE-3 | 9.1 |
| Sprint retrospective discussions | Continuous improvement | GOVERN-4 | 10.1 |
| Onboarding new team members | Competence development | GOVERN-3 | 7.2, 7.3 |
| Documenting an incident | Nonconformity recording | MANAGE-2.4 | 10.2 |
| Leadership status updates | Management oversight | GOVERN-1, GOVERN-2 | 5.1, 9.3 |
| Compliance check before release | Verification and validation | MEASURE-1 | Annex A.6.2.3 |

---

## Part 5: Practical Mapping Examples

### Example 1: Semi-Quantitative Risk Prioritization

**Project Activity:** Your team uses a 5x5 matrix to score risks on likelihood (1-5) and impact (1-5), then multiplies to get a priority score (1-25). Risks above 15 get escalated.

**What You're Actually Doing:**
- **NIST AI RMF MEASURE-2:** You're tracking quantified risk metrics
- **NIST AI RMF MEASURE-3:** You're analyzing potential impacts
- **ISO 42001 Clause 6.1.2:** You're applying a documented risk assessment methodology
- **EU AI Act Article 9(2):** You're evaluating and addressing risks through systematic analysis

**Artifacts to Preserve:**
1. The risk scoring rubric (what does a "4" on likelihood mean?)
2. The completed risk register with scores and timestamps
3. Evidence of who assigned scores and their rationale
4. Records of threshold breaches and escalation responses

**Common Gap:** Teams score risks but don't document the scoring criteria. An auditor asks "Why is this a 4 and not a 3?" and there's no documented basis for the distinction.

---

### Example 2: Trade-off Decision in a Design Meeting

**Project Activity:** Your team debates whether to use a more accurate but less explainable model versus a simpler model with clearer decision rationale. After discussion, you choose the simpler model because the use case involves consequential decisions about individuals.

**What You're Actually Doing:**
- **NIST AI RMF GOVERN-5:** You're integrating risk considerations into project decisions
- **NIST AI RMF MANAGE-4:** You're explicitly managing trade-offs with documented rationale
- **ISO 42001 Annex A.5.3:** You're conducting AI system impact assessment
- **ISO 42001 Annex A.6.2.6:** You're documenting trade-offs between system properties

**Artifacts to Preserve:**
1. Meeting notes or decision record capturing the discussion
2. The options considered with pros/cons for each
3. The decision criteria (why explainability mattered here)
4. Who participated and who had decision authority
5. Any conditions for revisiting (e.g., "reassess if accuracy drops below threshold")

**Common Gap:** The decision happens in a meeting but only "Action: implement simple model" gets recorded. The reasoning evaporates when team members leave the organization.

---

### Example 3: Risk Mitigation Work Tracked in Jira

**Project Activity:** A privacy risk is identified during development. You create a Jira epic with child tickets for implementing differential privacy, updating the privacy impact assessment, and validating the mitigation effectiveness. The tickets flow through your sprint process until completed.

**What You're Actually Doing:**
- **NIST AI RMF MANAGE-1:** You're prioritizing risks and responding based on severity
- **NIST AI RMF MANAGE-2:** You're implementing risk treatment plans
- **ISO 42001 Clause 8.1:** You're applying operational planning and control
- **ISO 42001 Clause 10.2:** If this was a finding, you're implementing corrective action
- **EU AI Act Article 9(4):** You're applying mitigation measures to eliminate or reduce risks

**Artifacts to Preserve:**
1. The original risk record with initial assessment
2. The treatment plan linking risk to mitigation tickets
3. Each ticket's history showing work done and by whom
4. The validation results confirming effectiveness
5. Updated risk record showing residual risk post-treatment
6. Point-in-time exports showing risk posture evolution

**Common Gap:** Tickets are closed when work is done, but there's no update to the original risk record, no verification of effectiveness, and no documentation of residual risk level.

---

### Example 4: Quarterly Model Performance Review

**Project Activity:** Every quarter, your ML team reviews model performance metrics, checks for drift, analyzes user feedback, and decides whether retraining or intervention is needed.

**What You're Actually Doing:**
- **NIST AI RMF MEASURE-4:** You're gathering feedback from relevant AI actors
- **NIST AI RMF MANAGE-3:** You're conducting post-deployment monitoring
- **ISO 42001 Clause 9.1:** You're performing monitoring, measurement, analysis, and evaluation
- **ISO 42001 Annex A.6.2.7:** You're executing AI system operation and monitoring
- **EU AI Act Article 12:** You're maintaining logs that enable traceability

**Artifacts to Preserve:**
1. Performance metrics with timestamps and version identifiers
2. Drift analysis results and detection thresholds
3. User feedback summary and categorization
4. Review meeting minutes with attendees and decisions
5. Any intervention actions triggered with rationale
6. Sign-off from appropriate authority on continued operation

**Common Gap:** Dashboards exist but nobody captures point-in-time snapshots. When an auditor asks "What was the model's accuracy six months ago?" you can only report current state.

---

## Part 6: Common Questions

### What's the minimum viable documentation for ISO 42001 certification?

At minimum, you need the mandatory documented information specified in the standard: AIMS scope, AI policy, AI objectives, risk assessment results, risk treatment plan, Statement of Applicability, internal audit results, management review records, and nonconformity/corrective action records. However, "minimum viable" is risky thinking—certifiers evaluate whether your documentation is sufficient for your context, not whether you've checked the required boxes. A simple AI use case needs less than a complex, high-risk deployment.

### How do you retrofit existing practices to be compliance-ready?

Start with an inventory of what you already produce. Map each artifact type to framework requirements. Identify gaps in three areas: missing artifact types, missing fields within existing artifacts, and missing metadata (timestamps, approvers, rationale). Prioritize based on risk—high-risk AI systems need complete evidence trails first. Don't try to retroactively create perfect documentation for past decisions; focus on getting it right going forward.

### What's the difference between project artifacts and governance artifacts?

Project artifacts support delivery—they help the team build and ship. Governance artifacts support accountability—they help the organization demonstrate responsible practices to auditors, regulators, and stakeholders. Many artifacts serve both purposes, but governance artifacts require additional characteristics: formal approval, retention management, traceability to controlled systems, and preservation of decision rationale.

### How long should different artifacts be retained?

General guidance: retain records for the operational life of the AI system plus post-decommissioning periods that cover regulatory limitation periods and potential litigation. The EU AI Act specifies 10 years for high-risk AI system documentation. ISO 42001 requires records for at least the last management system cycle plus one. When in doubt, err toward longer retention—storage is cheap, and recreating evidence is impossible.

### What if your project tools don't map cleanly to framework requirements?

Most tools can be extended with custom fields, tags, or linked documents to capture required metadata. The key is establishing conventions that are consistently applied. If your tool genuinely can't capture essential information, consider whether a parallel tracking mechanism (even a spreadsheet) might be needed for compliance-critical records. Document your approach so auditors understand how your tooling maps to requirements.

### How do you handle evidence for distributed teams using different tools?

Establish a "source of truth" for each record type. It's acceptable for work to happen in multiple tools, but define which tool holds the authoritative record. Ensure cross-references between systems. Implement periodic reconciliation to catch gaps. Consider a centralized evidence repository that aggregates exports from various systems for audit purposes.

---

## Conclusion: Your Daily Work Is Your Evidence

The gap between AI project management and AI compliance is smaller than it appears. Every risk discussion, design decision, and deployment review is already compliance activity—it just needs the right framing and metadata to serve as governance evidence.

Treat your project artifacts as institutional records. Apply information stewardship principles: know what you're creating, understand why it matters, capture the context that future readers will need, and manage retention intentionally. This isn't additional work; it's doing the same work with awareness of its dual purpose.

When the auditor arrives or the regulator inquires, you won't need to scramble to create documentation. You'll open your project management tool and show them exactly how you identified risks, made decisions, implemented controls, and monitored outcomes. Your daily work, properly captured, is your compliance evidence.

---

*This guide is part of the TAIGR (Threat-Informed AI Governance & Risk) methodology, which integrates threat modeling frameworks with AI risk standards to help organizations build accountable AI systems.*
