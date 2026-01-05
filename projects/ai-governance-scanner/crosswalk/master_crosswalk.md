# AI Governance Framework Crosswalk - Master Mapping

**Purpose**: This crosswalk shows how to implement AI governance controls once while satisfying multiple regulatory and compliance frameworks simultaneously.

**Frameworks Mapped**:
- ISO/IEC 42001:2023 (AI Management Systems)
- NIST AI Risk Management Framework (AI RMF)
- EU AI Act (High-Risk AI Systems)
- SOC 2 + AI Criteria (Trust Services Criteria for AI)

**How to Use**:
1. Identify your compliance requirements (which frameworks apply)
2. Use this mapping to design unified controls that satisfy all requirements
3. Reference the "Unified Implementation" column for how to satisfy multiple frameworks with one control
4. Use "Sample Evidence" to prepare for audits

---

## Domain 1: AI Risk Management

### Control Area: Risk Assessment & Treatment

| ISO 42001 Clause | NIST AI RMF Function | EU AI Act Requirement | SOC 2 AI Criteria | TIAG Control | Sample Evidence | Unified Implementation |
|------------------|---------------------|----------------------|-------------------|--------------|-----------------|------------------------|
| **6.1.3** Risk assessment for AI system | **GOVERN 1.3** Risk management processes | **Article 9** Risk management system for high-risk AI | **CC3.1** Risk assessment for AI processing | **TIAG-R-001** AI-Specific Risk Assessment | • AI risk register with MITRE ATLAS threat scenarios<br>• Risk assessment methodology document<br>• Board-approved risk appetite statement<br>• Quarterly risk review reports | Implement a single AI risk assessment process that:<br>1. Identifies AI-specific risks (algorithmic bias, data poisoning, model drift)<br>2. Maps threats to MITRE ATLAS taxonomy<br>3. Assigns risk ratings aligned with ISO 31000<br>4. Documents in format that satisfies all frameworks<br>5. Reviews quarterly with executive oversight |
| **8.2** Risk treatment plan | **GOVERN 1.5** Risk tolerance determination | **Article 9(4)** Risk mitigation measures | **CC3.3** Risk mitigation activities | **TIAG-R-003** Risk Mitigation Controls | • Control implementation plan<br>• Risk treatment decisions (accept/mitigate/transfer)<br>• Residual risk analysis<br>• Control effectiveness testing results | Create risk treatment plans that explicitly reference:<br>1. Control selection rationale (ISO 42001 Annex A)<br>2. NIST AI RMF functions addressed<br>3. EU AI Act Article 9 compliance<br>4. SOC 2 control mapping<br>Single document template satisfies all frameworks |
| **8.3** Risk communication | **GOVERN 4.1** Accountability structures | **Article 13** Transparency obligations | **CC2.2** Communication of AI risks | **TIAG-R-005** Risk Communication | • Risk communication matrix (stakeholder mapping)<br>• Board reporting templates<br>• Public AI transparency disclosures<br>• Incident communication playbooks | Develop tiered communication approach:<br>1. Board: Strategic AI risk dashboard (ISO/NIST)<br>2. Operators: Technical risk controls (NIST/SOC 2)<br>3. Users: Transparency disclosures (EU AI Act)<br>4. Regulators: Compliance reports (all frameworks) |

---

## Domain 2: Model Documentation & Inventory

### Control Area: AI System Documentation

| ISO 42001 Clause | NIST AI RMF Function | EU AI Act Requirement | SOC 2 AI Criteria | TIAG Control | Sample Evidence | Unified Implementation |
|------------------|---------------------|----------------------|-------------------|--------------|-----------------|------------------------|
| **7.2** AI system inventory | **MAP 1.1** Context of use documentation | **Article 11** Technical documentation | **CC2.1** AI system inventory | **TIAG-D-001** AI System Inventory | • AI system inventory database<br>• Model cards for each system<br>• Data flow diagrams<br>• Version control records | Maintain centralized AI inventory that captures:<br>1. Model metadata (name, version, purpose)<br>2. Risk classification (high/medium/low)<br>3. Framework applicability flags<br>4. Links to detailed documentation<br>Auto-generates compliance reports for each framework |
| **Annex A.6.2** AI system documentation requirements | **MAP 1.2** Intended use documentation | **Article 11(1)** Description of AI system and intended purpose | **CC8.1** AI system documentation | **TIAG-D-003** Model Cards | • SageMaker Model Cards<br>• MLflow model registry metadata<br>• Intended use statements<br>• Known limitations documentation<br>• Fairness/bias evaluation reports | Implement Model Card standard that includes:<br>1. Intended use cases (NIST MAP 1.2 / EU Article 11)<br>2. Training data description (ISO Annex A.8.2)<br>3. Performance metrics (NIST MEASURE 2.1)<br>4. Risk rating (ISO 8.3 / EU Article 9)<br>5. Control mapping (SOC 2)<br>AWS SageMaker Model Cards satisfy all requirements |
| **Annex A.8.2** Data used for AI system development | **MAP 2.1** Data quality documentation | **Article 10** Data governance | **CC6.2** Data quality for AI | **TIAG-D-005** Training Data Documentation | • Data lineage diagrams<br>• Data quality assessment reports<br>• Training/test/validation split documentation<br>• Data bias analysis reports<br>• Data retention policies | Document training data with:<br>1. Provenance tracking (source, collection method)<br>2. Quality metrics (completeness, accuracy)<br>3. Bias analysis (demographic representation)<br>4. Security controls (encryption, access control)<br>Single data governance process satisfies ISO/NIST/EU/SOC 2 |

---

## Domain 3: Model Monitoring & Performance

### Control Area: Continuous Validation

| ISO 42001 Clause | NIST AI RMF Function | EU AI Act Requirement | SOC 2 AI Criteria | TIAG Control | Sample Evidence | Unified Implementation |
|------------------|---------------------|----------------------|-------------------|--------------|-----------------|------------------------|
| **9.1** Monitoring and measurement | **MEASURE 2.1** Performance metrics | **Article 15** Accuracy monitoring | **CC7.2** Model performance monitoring | **TIAG-M-001** Model Monitoring | • SageMaker Model Monitor schedules<br>• Drift detection alerts<br>• Model performance dashboards<br>• Monthly model health reports<br>• Re-training trigger thresholds | Implement continuous monitoring that tracks:<br>1. Prediction accuracy vs. baseline (NIST/EU)<br>2. Data drift detection (ISO 9.1 / SOC 2)<br>3. Fairness metrics over time (EU Article 10)<br>4. Performance degradation alerts<br>AWS SageMaker Model Monitor provides framework-agnostic telemetry |
| **9.2** Internal audit | **GOVERN 5.1** Audit mechanisms | **Article 17** Conformity assessment | **CC4.2** AI system audits | **TIAG-M-003** AI Audit Program | • AI audit plan and schedule<br>• Internal audit findings<br>• Corrective action tracking<br>• Annual audit summary report | Conduct annual AI audits covering:<br>1. Control effectiveness (ISO 9.2 / SOC 2)<br>2. Framework compliance (NIST functions)<br>3. EU AI Act conformity (Article 17)<br>4. Findings tracked in unified register<br>Single audit program with framework-specific checklists |
| **10.2** Continual improvement | **MANAGE 4.1** Improvement processes | **Article 9(7)** Periodic updates to risk management | **CC1.4** Change management for AI | **TIAG-M-005** Model Lifecycle Management | • Model versioning records (MLflow/SageMaker)<br>• A/B testing results for new versions<br>• Rollback procedures documentation<br>• Model retirement policy<br>• Change advisory board minutes | Establish model lifecycle process:<br>1. Version control with semantic versioning<br>2. A/B testing for production changes<br>3. Rollback mechanisms for failed deployments<br>4. Periodic re-assessment (EU Article 9.7)<br>5. Change approval workflows (SOC 2)<br>GitOps approach satisfies all frameworks |

---

## Domain 4: Security & Access Controls

### Control Area: AI System Security

| ISO 42001 Clause | NIST AI RMF Function | EU AI Act Requirement | SOC 2 AI Criteria | TIAG Control | Sample Evidence | Unified Implementation |
|------------------|---------------------|----------------------|-------------------|--------------|-----------------|------------------------|
| **Annex A.7.1** Access control for AI systems | **GOVERN 2.1** Roles and responsibilities | **Article 16** Human oversight mechanisms | **CC6.1** Logical access controls | **TIAG-S-001** AI Access Controls | • IAM role definitions for AI services<br>• Least privilege access reviews<br>• Separation of duties matrix<br>• AWS IAM policies for Bedrock/SageMaker<br>• Access audit logs | Implement role-based access control (RBAC):<br>1. AI Developer (training, experimentation)<br>2. AI Operator (deployment, monitoring)<br>3. AI Auditor (read-only for compliance)<br>4. AI User (inference only)<br>Enforce principle of least privilege across all frameworks |
| **Annex A.7.3** Model security | **MANAGE 2.1** Security controls | **Article 15(4)** Cybersecurity measures | **CC6.6** Encryption of AI assets | **TIAG-S-003** Model Protection | • Model encryption at rest (S3 SSE-KMS)<br>• Model encryption in transit (TLS 1.3)<br>• Model signing/provenance verification<br>• Model access logs (CloudTrail)<br>• Adversarial robustness testing results | Protect AI models and data:<br>1. Encrypt models at rest (S3/SageMaker KMS)<br>2. Encrypt API traffic (TLS for Bedrock)<br>3. Sign models for integrity verification<br>4. Log all model access (CloudTrail)<br>5. Test adversarial robustness (MITRE ATLAS)<br>AWS native encryption satisfies all frameworks |
| **Annex A.8.1** Prompt injection controls | **MANAGE 1.1** Safety controls | **Article 15(1)** Prevention of manipulation | **CC6.8** Input validation for AI | **TIAG-S-005** Guardrails & Input Validation | • AWS Bedrock Guardrails configuration<br>• Content filtering policies<br>• PII detection rules<br>• Word/phrase blocklists<br>• Jailbreak attempt logs | Deploy guardrails for LLM systems:<br>1. Content filters (hate, violence, sexual)<br>2. PII detection and redaction<br>3. Prompt injection detection<br>4. Rate limiting per user<br>5. Anomaly detection for abuse<br>AWS Bedrock Guardrails natively support all controls |

---

## Domain 5: Transparency & Explainability

### Control Area: AI Transparency

| ISO 42001 Clause | NIST AI RMF Function | EU AI Act Requirement | SOC 2 AI Criteria | TIAG Control | Sample Evidence | Unified Implementation |
|------------------|---------------------|----------------------|-------------------|--------------|-----------------|------------------------|
| **Annex A.5.1** Transparency to affected parties | **GOVERN 4.3** Transparency practices | **Article 13** Transparency obligations for users | **CC2.3** User notification of AI use | **TIAG-T-001** User Transparency | • User-facing AI disclosure notices<br>• Privacy policy with AI usage description<br>• Terms of service AI clauses<br>• In-app AI indicators (chatbot labels)<br>• User education materials | Disclose AI use to end users:<br>1. Privacy policy: "We use AI for [purpose]"<br>2. UI indicators: "You're chatting with AI"<br>3. Opt-out mechanisms where feasible<br>4. Plain language explanations<br>Single disclosure template satisfies NIST/EU/SOC 2 |
| **Annex A.5.2** Explainability of AI decisions | **MAP 3.4** Explainability measures | **Article 13(1)** Meaningful information about logic | **CC8.3** AI decision explainability | **TIAG-T-003** Model Explainability | • SHAP/LIME implementation for predictions<br>• Feature importance reports<br>• Decision audit trails<br>• User-facing explanation interface<br>• Explainability testing reports | Implement explainability based on risk:<br>1. High-risk: Individual prediction explanations (SHAP)<br>2. Medium-risk: Global feature importance<br>3. Low-risk: General model description<br>4. Document explainability methods in Model Card<br>Tiered approach balances EU AI Act requirements with practicality |

---

## Domain 6: Human Oversight & Accountability

### Control Area: Human-in-the-Loop

| ISO 42001 Clause | NIST AI RMF Function | EU AI Act Requirement | SOC 2 AI Criteria | TIAG Control | Sample Evidence | Unified Implementation |
|------------------|---------------------|----------------------|-------------------|--------------|-----------------|------------------------|
| **Annex A.3.1** Human oversight mechanisms | **GOVERN 2.3** Oversight roles | **Article 14** Human oversight requirements | **CC5.1** Human review of AI outputs | **TIAG-H-001** Human Oversight Controls | • Human-in-the-loop workflow diagrams<br>• Override authority matrix<br>• Escalation procedures<br>• Human review sampling logs<br>• Override usage statistics | Define oversight based on AI risk:<br>1. High-risk: Human-in-the-loop (every decision)<br>2. Medium-risk: Human-on-the-loop (monitoring)<br>3. Low-risk: Human-over-the-loop (audit)<br>4. Document override authority<br>5. Track override rates as performance metric<br>Risk-tiered approach satisfies all frameworks |
| **Annex A.3.2** Accountability assignment | **GOVERN 1.1** Governance structure | **Article 16(a)** Identified natural persons for oversight | **CC2.1** AI accountability roles | **TIAG-H-003** AI Accountability Matrix | • AI governance RACI matrix<br>• Executive AI owner designation<br>• AI Ethics Committee charter<br>• Incident response roles for AI<br>• Escalation pathways documentation | Establish AI governance roles:<br>1. AI Owner (VP/C-level accountable)<br>2. AI Product Manager (day-to-day responsible)<br>3. AI Ethics Committee (oversight)<br>4. AI Incident Response Team (reactive)<br>RACI matrix satisfies ISO/NIST/EU/SOC 2 accountability requirements |

---

## Domain 7: Incident Response & Monitoring

### Control Area: AI Incident Management

| ISO 42001 Clause | NIST AI RMF Function | EU AI Act Requirement | SOC 2 AI Criteria | TIAG Control | Sample Evidence | Unified Implementation |
|------------------|---------------------|----------------------|-------------------|--------------|-----------------|------------------------|
| **Annex A.4.1** AI incident response plan | **MANAGE 3.1** Incident response | **Article 62** Serious incident reporting | **CC7.3** Incident response for AI | **TIAG-I-001** AI Incident Response | • AI incident response playbook<br>• Incident classification matrix<br>• EU AI Act serious incident criteria<br>• Regulatory reporting procedures<br>• Post-incident review template | Create AI-specific incident response plan:<br>1. Incident types (bias, drift, security breach)<br>2. Severity classification (maps to EU "serious")<br>3. Escalation triggers (board notification)<br>4. Regulatory reporting (EU 15-day requirement)<br>5. Post-mortem and remediation<br>Single playbook with framework-specific triggers |
| **Annex A.4.2** Logging and monitoring | **MEASURE 4.1** Monitoring mechanisms | **Article 12** Record-keeping obligations | **CC7.2** System monitoring | **TIAG-I-003** AI Telemetry & Logging | • CloudTrail logs for all AI API calls<br>• Model prediction logs (inputs/outputs)<br>• Guardrail violation logs<br>• Drift detection alerts<br>• 6-month log retention policy (EU AI Act) | Implement comprehensive logging:<br>1. Model invocation logs (who, when, what)<br>2. Prediction inputs/outputs (EU Article 12)<br>3. Guardrail violations and blocks<br>4. Performance metrics time-series<br>5. Retain 6 months minimum (EU AI Act)<br>AWS CloudWatch + CloudTrail satisfy all requirements |

---

## How to Use This Crosswalk

### Step 1: Identify Applicable Frameworks
Determine which frameworks apply to your organization:
- **ISO 42001**: If pursuing certification or customer contracts require it
- **NIST AI RMF**: U.S. federal contractors, industry best practice
- **EU AI Act**: Deploying high-risk AI in EU, or serving EU customers
- **SOC 2 AI**: SaaS providers, customer security questionnaires

### Step 2: Map Your Current Controls
For each control domain:
1. Review your existing controls (if any)
2. Identify which framework requirements they satisfy
3. Find gaps where requirements are unmet

### Step 3: Implement Unified Controls
Use the "Unified Implementation" column to:
1. Design controls that satisfy multiple frameworks simultaneously
2. Avoid redundant documentation and processes
3. Reduce audit burden by mapping once, satisfying many

### Step 4: Prepare Evidence
Use the "Sample Evidence" column to:
1. Understand what auditors will request
2. Set up systems to generate evidence automatically
3. Create evidence repositories organized by framework

### Step 5: Continuous Compliance
- Update this crosswalk as frameworks evolve
- Review mappings during internal audits
- Train teams on unified control approach

---

## Key Integration Insights

### 1. Risk Assessment is Universal
All four frameworks require AI risk assessment. Instead of four separate processes:
- **Single Process**: Risk assessment using MITRE ATLAS threat taxonomy
- **Four Outputs**: Reports formatted for ISO 42001 (Clause 6.1.3), NIST (GOVERN 1.3), EU AI Act (Article 9), SOC 2 (CC3.1)
- **Efficiency Gain**: 75% reduction in effort vs. separate assessments

### 2. Model Cards Satisfy Multiple Documentation Requirements
AWS SageMaker Model Cards (or equivalent) satisfy:
- ISO 42001 Annex A.6.2 (AI system documentation)
- NIST AI RMF MAP 1.2 (intended use)
- EU AI Act Article 11 (technical documentation)
- SOC 2 CC8.1 (system documentation)

### 3. Monitoring Infrastructure is Reusable
AWS CloudWatch + SageMaker Model Monitor + CloudTrail provides:
- ISO 42001 compliance (Clause 9.1 monitoring)
- NIST MEASURE 2.1 (performance metrics)
- EU AI Act Article 15 (accuracy monitoring)
- SOC 2 CC7.2 (system monitoring)

### 4. Guardrails Address Multiple Safety Requirements
AWS Bedrock Guardrails satisfy:
- ISO 42001 Annex A.8.1 (prompt injection controls)
- NIST MANAGE 1.1 (safety controls)
- EU AI Act Article 15 (manipulation prevention)
- SOC 2 CC6.8 (input validation)

---

## TIAG Control Numbering System

**TIAG-[Domain]-[Sequence]**

Domains:
- **R**: Risk Management
- **D**: Documentation & Data
- **M**: Monitoring & Measurement
- **S**: Security & Safety
- **T**: Transparency
- **H**: Human Oversight
- **I**: Incident Response

Examples:
- **TIAG-R-001**: AI-Specific Risk Assessment
- **TIAG-D-003**: Model Cards
- **TIAG-S-005**: Guardrails & Input Validation

This numbering system allows you to:
1. Reference controls consistently across client engagements
2. Build reusable control templates
3. Track control maturity over time
4. Map to multiple frameworks via this crosswalk

---

**Document Version**: 1.0
**Last Updated**: 2025-01-15
**Maintained By**: Jose Ruiz-Vazquez, ISO/IEC 42001 Lead Auditor
**Purpose**: Enable efficient, integrated AI governance implementation
