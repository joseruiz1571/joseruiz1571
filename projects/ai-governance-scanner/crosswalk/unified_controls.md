# Unified AI Governance Control Set

**Purpose**: This is the **minimum viable control set** that satisfies ISO 42001, NIST AI RMF, EU AI Act, and SOC 2 simultaneously.

**How to Use**:
1. Treat this as a checklist for AI governance implementation
2. Each control includes implementation guidance and AWS-specific examples
3. Controls are numbered using the TIAG (Threat-Informed AI Governance) system
4. Use the "Framework Coverage" to understand which requirements each control satisfies

---

## Control Domain 1: Risk Management (TIAG-R)

### TIAG-R-001: AI-Specific Risk Assessment

**Description**: Conduct risk assessments that identify AI-specific threats (algorithmic bias, data poisoning, model drift, prompt injection) using structured threat taxonomy.

**Framework Coverage**:
- ISO 42001: Clause 6.1.3 (Risk assessment)
- NIST AI RMF: GOVERN 1.3 (Risk management processes)
- EU AI Act: Article 9 (Risk management system)
- SOC 2: CC3.1 (Risk assessment)

**Implementation Guidance**:
1. **Establish Risk Assessment Process**:
   - Conduct AI risk assessment for each high-risk AI system before deployment
   - Use MITRE ATLAS threat taxonomy to identify attack vectors
   - Assess traditional risks (confidentiality, integrity, availability) + AI-specific risks (fairness, transparency, robustness)

2. **Risk Rating Methodology**:
   - Likelihood: Rare (1) → Almost Certain (5)
   - Impact: Negligible (1) → Catastrophic (5)
   - Risk Score = Likelihood × Impact
   - Risk Level: Low (1-5), Medium (6-12), High (15-25)

3. **Documentation Requirements**:
   - AI Risk Register (spreadsheet or GRC tool)
   - Columns: Risk ID, AI System, Threat Scenario (MITRE ATLAS), Likelihood, Impact, Risk Score, Control(s), Residual Risk
   - Review quarterly with executive oversight

4. **AWS Implementation**:
   - Use AWS Security Hub for infrastructure risks
   - Custom CloudWatch metrics for model-specific risks (drift, bias)
   - Tag AI resources with risk classification (High/Medium/Low)

**Evidence Examples**:
- [ ] AI Risk Register covering all production AI systems
- [ ] Risk assessment methodology document (approved by leadership)
- [ ] MITRE ATLAS threat mapping for each high-risk system
- [ ] Quarterly risk review meeting minutes

---

### TIAG-R-003: Risk Treatment Plans

**Description**: Document risk treatment decisions (mitigate, accept, transfer, avoid) with clear rationale and accountability.

**Framework Coverage**:
- ISO 42001: Clause 8.2 (Risk treatment)
- NIST AI RMF: GOVERN 1.5 (Risk tolerance)
- EU AI Act: Article 9(4) (Risk mitigation measures)
- SOC 2: CC3.3 (Risk mitigation activities)

**Implementation Guidance**:
1. For each identified risk, document treatment approach:
   - **Mitigate**: Implement controls to reduce likelihood or impact
   - **Accept**: Formally accept risk with executive approval (for low risks)
   - **Transfer**: Use insurance or contractual terms (limited applicability for AI)
   - **Avoid**: Discontinue AI feature or change design to eliminate risk

2. Control Selection:
   - Reference controls from this unified set (TIAG-*)
   - Map to framework requirements (ISO Annex A, NIST functions)
   - Document control effectiveness metrics

3. Residual Risk Assessment:
   - After controls applied, reassess risk score
   - All High residual risks require executive acceptance
   - Document risk appetite thresholds

**Evidence Examples**:
- [ ] Risk treatment plan for each AI system
- [ ] Executive approval for accepted high risks
- [ ] Control implementation tracking (with completion dates)
- [ ] Residual risk assessment after control implementation

---

## Control Domain 2: Documentation & Data (TIAG-D)

### TIAG-D-001: AI System Inventory

**Description**: Maintain centralized inventory of all AI systems with metadata on risk classification, framework applicability, and ownership.

**Framework Coverage**:
- ISO 42001: Clause 7.2 (AI system inventory)
- NIST AI RMF: MAP 1.1 (Context documentation)
- EU AI Act: Article 11 (Technical documentation)
- SOC 2: CC2.1 (System inventory)

**Implementation Guidance**:
1. **Inventory Database** (spreadsheet or CMDB):
   - Columns: AI System Name, Description, Owner, Risk Classification, Framework Scope, Status (Dev/Prod), Model Card Link, Last Review Date

2. **Classification Criteria**:
   - **High-Risk**: EU AI Act Annex III systems (hiring, credit scoring, law enforcement) OR systems with significant harm potential
   - **Medium-Risk**: Customer-facing AI with moderate impact
   - **Low-Risk**: Internal tools, non-critical applications

3. **Maintenance Process**:
   - Update inventory when new AI systems are deployed
   - Quarterly review to identify shadow AI (unregistered systems)
   - Annual comprehensive audit of inventory accuracy

4. **AWS Implementation**:
   - Use AWS Resource Tags: `ai-system:name`, `ai-risk:high|medium|low`, `ai-owner:email`
   - AWS Config rules to detect untagged AI resources (SageMaker, Bedrock)
   - Lambda function to auto-generate inventory from tags

**Evidence Examples**:
- [ ] AI system inventory database (current as of last quarter)
- [ ] Inventory update procedure document
- [ ] Quarterly inventory review reports
- [ ] AWS resource tagging compliance report

---

### TIAG-D-003: Model Cards

**Description**: Document each AI model's intended use, training data, performance metrics, limitations, and risk assessment using standardized Model Card format.

**Framework Coverage**:
- ISO 42001: Annex A.6.2 (AI system documentation)
- NIST AI RMF: MAP 1.2 (Intended use), MEASURE 2.1 (Performance metrics)
- EU AI Act: Article 11(1) (Description of AI system and intended purpose)
- SOC 2: CC8.1 (System documentation)

**Implementation Guidance**:
1. **Model Card Template** (following Mitchell et al. 2019 standard):
   - **Model Details**: Name, version, type (classification/regression/LLM), owner
   - **Intended Use**: Primary use cases, out-of-scope applications
   - **Training Data**: Dataset description, size, collection method, bias analysis
   - **Performance Metrics**: Accuracy, precision, recall, F1 (include fairness metrics)
   - **Limitations**: Known weaknesses, edge cases, failure modes
   - **Risk Assessment**: Risk rating, MITRE ATLAS threats, control mapping

2. **Creation Workflow**:
   - Model Cards created during model development
   - Reviewed and approved before production deployment
   - Updated when model is retrained or materially changed
   - Version controlled alongside model artifacts

3. **AWS Implementation**:
   - Use **AWS SageMaker Model Cards** (native support)
   - Store Model Cards in S3 with model artifacts
   - Link from AI System Inventory to Model Card
   - Enforce Model Card creation via deployment pipeline (CI/CD gate)

**Evidence Examples**:
- [ ] Model Card for each production AI system
- [ ] Model Card template (standardized across organization)
- [ ] Model Card approval workflow documentation
- [ ] Version history showing Model Card updates

---

### TIAG-D-005: Training Data Documentation

**Description**: Document provenance, quality, bias analysis, and security controls for all training datasets.

**Framework Coverage**:
- ISO 42001: Annex A.8.2 (Data used for AI system development)
- NIST AI RMF: MAP 2.1 (Data quality)
- EU AI Act: Article 10 (Data governance)
- SOC 2: CC6.2 (Data quality for AI)

**Implementation Guidance**:
1. **Data Provenance**:
   - Document data source (internal systems, third-party, web scraping)
   - Collection method and date
   - Licensing and usage rights
   - Data refresh frequency

2. **Data Quality Metrics**:
   - Completeness: % of missing values by feature
   - Accuracy: Validation against ground truth (if available)
   - Consistency: Duplicate detection, format standardization
   - Timeliness: Age of data, staleness indicators

3. **Bias Analysis**:
   - Demographic representation analysis (if applicable)
   - Label distribution (class imbalance)
   - Feature correlation with protected attributes
   - Mitigation strategies for identified bias

4. **Security Controls**:
   - Encryption at rest (S3 SSE-KMS)
   - Access control (IAM policies limiting data access)
   - Data retention policy
   - PII detection and handling procedures

5. **AWS Implementation**:
   - S3 bucket for training data with encryption and versioning
   - AWS Glue Data Catalog for metadata management
   - AWS Macie for PII detection in datasets
   - Data lineage tracking using SageMaker Feature Store

**Evidence Examples**:
- [ ] Data lineage diagrams for each AI system
- [ ] Data quality assessment reports
- [ ] Bias analysis reports with mitigation strategies
- [ ] S3 bucket policies showing encryption and access controls

---

## Control Domain 3: Monitoring & Measurement (TIAG-M)

### TIAG-M-001: Model Performance Monitoring

**Description**: Continuously monitor AI model performance, drift, and accuracy degradation in production.

**Framework Coverage**:
- ISO 42001: Clause 9.1 (Monitoring and measurement)
- NIST AI RMF: MEASURE 2.1 (Performance metrics)
- EU AI Act: Article 15 (Accuracy monitoring)
- SOC 2: CC7.2 (Model performance monitoring)

**Implementation Guidance**:
1. **Metrics to Monitor**:
   - **Prediction Accuracy**: Compare predictions to ground truth (when available)
   - **Data Drift**: Distribution shift in input features vs. training data
   - **Concept Drift**: Change in relationship between features and target
   - **Throughput**: Requests per second, latency percentiles
   - **Error Rates**: 4xx/5xx errors, timeout rates

2. **Alerting Thresholds**:
   - Set baselines from initial deployment
   - Alert when drift exceeds 10% threshold
   - Alert when accuracy drops below SLA (e.g., 95% → 90%)
   - Escalate to AI Owner after 3 consecutive alerts

3. **Response Procedures**:
   - Investigate root cause of drift (data shift, model staleness)
   - Trigger model retraining if drift persists
   - Rollback to previous model version if accuracy drops significantly
   - Document incidents and resolutions

4. **AWS Implementation**:
   - **SageMaker Model Monitor**: Schedule hourly/daily monitoring jobs
   - **CloudWatch Dashboards**: Visualize drift and performance metrics
   - **CloudWatch Alarms**: Automated alerts to Slack/PagerDuty
   - **EventBridge Rules**: Trigger Lambda for automated responses

**Evidence Examples**:
- [ ] SageMaker Model Monitor schedules for all production models
- [ ] CloudWatch dashboards showing model health metrics
- [ ] Alert logs and incident response tickets
- [ ] Monthly model health reports sent to stakeholders

---

### TIAG-M-003: AI Audit Program

**Description**: Conduct regular internal audits of AI governance controls and framework compliance.

**Framework Coverage**:
- ISO 42001: Clause 9.2 (Internal audit)
- NIST AI RMF: GOVERN 5.1 (Audit mechanisms)
- EU AI Act: Article 17 (Conformity assessment)
- SOC 2: CC4.2 (AI system audits)

**Implementation Guidance**:
1. **Audit Scope**:
   - Annual comprehensive audit of all AI systems
   - Quarterly focused audits on high-risk systems
   - Unannounced spot checks for critical controls

2. **Audit Checklist** (use framework crosswalk):
   - Verify AI inventory is complete and up-to-date
   - Review Model Cards for completeness
   - Test monitoring alert functionality
   - Verify incident response procedures
   - Confirm human oversight mechanisms are operational
   - Check compliance with data governance policies

3. **Audit Team**:
   - Internal audit team (independent from AI development)
   - Or third-party auditors for ISO 42001 certification
   - AI Subject Matter Expert (SME) to assess technical controls

4. **Findings Management**:
   - Document findings in audit report
   - Classify severity: Critical, High, Medium, Low
   - Assign remediation owners with due dates
   - Track remediation in corrective action register
   - Verify closure of findings in next audit

**Evidence Examples**:
- [ ] Annual AI audit plan and schedule
- [ ] Audit reports with findings and recommendations
- [ ] Corrective action tracking register
- [ ] Evidence of finding remediation (before/after)

---

## Control Domain 4: Security & Safety (TIAG-S)

### TIAG-S-001: AI Access Controls

**Description**: Implement role-based access control (RBAC) for AI systems with principle of least privilege.

**Framework Coverage**:
- ISO 42001: Annex A.7.1 (Access control for AI systems)
- NIST AI RMF: GOVERN 2.1 (Roles and responsibilities)
- EU AI Act: Article 16 (Human oversight mechanisms)
- SOC 2: CC6.1 (Logical access controls)

**Implementation Guidance**:
1. **AI Role Definitions**:
   - **AI Developer**: Full access to dev environments, read-only to prod
   - **AI Operator**: Deploy to prod, configure monitoring, no model modification
   - **AI Auditor**: Read-only access to all environments and logs
   - **AI User**: Inference API access only, no model access

2. **Access Control Enforcement**:
   - Use AWS IAM policies to enforce roles
   - MFA required for prod access
   - Service Control Policies (SCPs) for organization-wide guardrails
   - Session recording for privileged access (CloudTrail)

3. **Access Review Process**:
   - Quarterly access reviews (verify users still need access)
   - Automated removal of access after 90 days of inactivity
   - Immediate revocation upon termination (integrated with HR system)

4. **AWS Implementation**:
   ```json
   // Example IAM policy for AI Developer
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "sagemaker:CreateModel",
           "sagemaker:CreateTrainingJob",
           "bedrock:InvokeModel"
         ],
         "Resource": "*",
         "Condition": {
           "StringEquals": {
             "aws:RequestedRegion": "us-east-1",
             "sagemaker:Environment": "dev"
           }
         }
       }
     ]
   }
   ```

**Evidence Examples**:
- [ ] IAM role definitions for AI personas
- [ ] IAM policies implementing least privilege
- [ ] Quarterly access review reports
- [ ] CloudTrail logs showing MFA enforcement

---

### TIAG-S-003: Model Protection

**Description**: Protect AI models and training data using encryption, integrity verification, and access logging.

**Framework Coverage**:
- ISO 42001: Annex A.7.3 (Model security)
- NIST AI RMF: MANAGE 2.1 (Security controls)
- EU AI Act: Article 15(4) (Cybersecurity measures)
- SOC 2: CC6.6 (Encryption of AI assets)

**Implementation Guidance**:
1. **Encryption Requirements**:
   - **At Rest**: All model artifacts encrypted with AWS KMS
   - **In Transit**: TLS 1.3 for all API communications (Bedrock, SageMaker)
   - **Key Management**: Separate KMS keys per environment (dev/staging/prod)

2. **Model Integrity**:
   - Sign model artifacts with digital signatures
   - Verify signatures before deployment
   - Maintain chain of custody from training to production
   - Version control models in model registry (SageMaker, MLflow)

3. **Access Logging**:
   - Log all model access (training, deployment, inference)
   - CloudTrail for API calls
   - VPC Flow Logs for network traffic
   - Retain logs for 1 year minimum

4. **AWS Implementation**:
   ```bash
   # S3 bucket for model artifacts with encryption
   aws s3api create-bucket \
     --bucket ai-models-prod \
     --server-side-encryption-configuration \
     'Rules=[{ApplyServerSideEncryptionByDefault={SSEAlgorithm=aws:kms,KMSMasterKeyID=alias/ai-models}}]'

   # SageMaker model with encryption
   aws sagemaker create-model \
     --model-name fraud-detection-v2 \
     --primary-container ModelDataUrl=s3://ai-models-prod/fraud-v2.tar.gz \
     --enable-network-isolation \
     --vpc-config SecurityGroupIds=[sg-xxx],Subnets=[subnet-xxx]
   ```

**Evidence Examples**:
- [ ] KMS key policies for model encryption
- [ ] S3 bucket policies requiring SSE-KMS
- [ ] Model signing and verification procedures
- [ ] CloudTrail logs showing model access

---

### TIAG-S-005: Guardrails & Input Validation

**Description**: Deploy content filters, PII detection, and prompt injection defenses for LLM systems.

**Framework Coverage**:
- ISO 42001: Annex A.8.1 (Prompt injection controls)
- NIST AI RMF: MANAGE 1.1 (Safety controls)
- EU AI Act: Article 15(1) (Prevention of manipulation)
- SOC 2: CC6.8 (Input validation for AI)

**Implementation Guidance**:
1. **Content Filtering**:
   - Block hate speech, violence, sexual content, misinformation
   - Use AWS Bedrock Guardrails with pre-configured filters
   - Custom word/phrase blocklists for domain-specific content
   - Thresholds: Low (permissive) → High (strict)

2. **PII Detection & Redaction**:
   - Detect and block/redact: SSN, credit cards, email, phone numbers
   - Bedrock Guardrails PII filters
   - Custom regex patterns for organization-specific PII

3. **Prompt Injection Defense**:
   - Detect attempts to override system prompts
   - Rate limiting per user (prevent brute-force attacks)
   - Anomaly detection for unusual prompt patterns
   - Logging of blocked prompts for analysis

4. **AWS Implementation**:
   ```python
   # Create Bedrock Guardrail
   guardrail = bedrock.create_guardrail(
       name='prod-chatbot-guardrail',
       contentPolicyConfig={
           'filtersConfig': [
               {'type': 'HATE', 'inputStrength': 'HIGH', 'outputStrength': 'HIGH'},
               {'type': 'VIOLENCE', 'inputStrength': 'MEDIUM', 'outputStrength': 'HIGH'},
               {'type': 'SEXUAL', 'inputStrength': 'MEDIUM', 'outputStrength': 'HIGH'}
           ]
       },
       sensitiveInformationPolicyConfig={
           'piiEntitiesConfig': [
               {'type': 'EMAIL', 'action': 'BLOCK'},
               {'type': 'CREDIT_DEBIT_CARD_NUMBER', 'action': 'BLOCK'},
               {'type': 'US_SOCIAL_SECURITY_NUMBER', 'action': 'BLOCK'}
           ]
       },
       wordPolicyConfig={
           'wordsConfig': [
               {'text': 'confidential'},
               {'text': 'internal-only'}
           ],
           'managedWordListsConfig': [{'type': 'PROFANITY'}]
       }
   )
   ```

**Evidence Examples**:
- [ ] Bedrock Guardrail configurations for all LLM systems
- [ ] Content filter testing reports (attempt jailbreak, verify blocked)
- [ ] PII detection testing results
- [ ] Logs of blocked prompts and false positive review

---

## Control Domain 5: Transparency (TIAG-T)

### TIAG-T-001: User Transparency

**Description**: Disclose AI use to end users with clear, understandable language.

**Framework Coverage**:
- ISO 42001: Annex A.5.1 (Transparency to affected parties)
- NIST AI RMF: GOVERN 4.3 (Transparency practices)
- EU AI Act: Article 13 (Transparency obligations for users)
- SOC 2: CC2.3 (User notification of AI use)

**Implementation Guidance**:
1. **Disclosure Locations**:
   - Privacy Policy: "We use AI for [specific purposes]"
   - Terms of Service: AI usage clauses, limitations of liability
   - In-App Indicators: "You're chatting with AI" labels
   - User Education: Help center articles explaining AI features

2. **Disclosure Content**:
   - What AI is being used for (e.g., "AI summarizes customer reviews")
   - Limitations (e.g., "AI may make mistakes, verify important information")
   - Opt-out mechanisms (where feasible)
   - Contact for questions/complaints

3. **Plain Language Requirements**:
   - Avoid technical jargon ("machine learning model" → "AI tool")
   - Use active voice ("We use AI to..." not "AI is used...")
   - 8th-grade reading level
   - Available in all languages supported by the application

4. **Implementation Examples**:
   ```html
   <!-- Chatbot UI indicator -->
   <div class="ai-indicator">
     🤖 You're chatting with an AI assistant.
     <a href="/help/ai-chatbot">Learn more</a>
   </div>

   <!-- Privacy policy excerpt -->
   <h3>How We Use AI</h3>
   <p>We use artificial intelligence to:</p>
   <ul>
     <li>Suggest products you might like</li>
     <li>Summarize long documents</li>
     <li>Detect fraudulent transactions</li>
   </ul>
   <p>AI may make mistakes. For important decisions, we recommend
      consulting with a human representative.</p>
   ```

**Evidence Examples**:
- [ ] Privacy policy with AI disclosure section
- [ ] Screenshots of in-app AI indicators
- [ ] User education materials about AI features
- [ ] User research showing disclosure comprehension

---

### TIAG-T-003: Model Explainability

**Description**: Provide explanations for AI decisions, scaled to risk level.

**Framework Coverage**:
- ISO 42001: Annex A.5.2 (Explainability of AI decisions)
- NIST AI RMF: MAP 3.4 (Explainability measures)
- EU AI Act: Article 13(1) (Meaningful information about logic)
- SOC 2: CC8.3 (AI decision explainability)

**Implementation Guidance**:
1. **Tiered Explainability** (based on risk):
   - **High-Risk** (credit decisions, hiring): Individual prediction explanations
     - Use SHAP values showing feature contributions
     - Example: "Loan denied because: income too low (40%), debt-to-income ratio (35%), short credit history (25%)"
   - **Medium-Risk** (product recommendations): Global model explanations
     - Feature importance charts
     - Example: "Recommendations based on: purchase history, browsing behavior, similar users"
   - **Low-Risk** (content moderation): General model description
     - Example: "AI classifies content into safe/unsafe using trained model"

2. **Explanation Methods**:
   - **SHAP (SHapley Additive exPlanations)**: For tabular data models
   - **LIME (Local Interpretable Model-agnostic Explanations)**: For any model type
   - **Attention Visualizations**: For NLP models
   - **Counterfactual Explanations**: "If income was $10K higher, loan would be approved"

3. **Delivery Mechanisms**:
   - **User Interface**: Inline explanations in decision notifications
   - **API**: Explanation endpoint returning SHAP values
   - **Documentation**: Model Card includes explainability methodology
   - **Customer Support**: Training on how to explain AI decisions

4. **AWS Implementation**:
   ```python
   # SageMaker Clarify for explainability
   from sagemaker import clarify

   clarify_processor = clarify.SageMakerClarifyProcessor(
       role=role,
       instance_count=1,
       instance_type='ml.m5.xlarge'
   )

   explainability_config = clarify.ExplainabilityConfig(
       shap_config=clarify.SHAPConfig(
           baseline=baseline_data,
           num_samples=100,
           agg_method='mean_abs'
       )
   )

   clarify_processor.run_explainability(
       data_config=data_config,
       model_config=model_config,
       explainability_config=explainability_config
   )
   ```

**Evidence Examples**:
- [ ] Explainability methodology documented in Model Cards
- [ ] SHAP/LIME implementation for high-risk models
- [ ] Screenshots of user-facing explanations
- [ ] Customer support training materials on AI explanations

---

## Control Domain 6: Human Oversight (TIAG-H)

### TIAG-H-001: Human Oversight Controls

**Description**: Implement human review mechanisms scaled to AI system risk level.

**Framework Coverage**:
- ISO 42001: Annex A.3.1 (Human oversight mechanisms)
- NIST AI RMF: GOVERN 2.3 (Oversight roles)
- EU AI Act: Article 14 (Human oversight requirements)
- SOC 2: CC5.1 (Human review of AI outputs)

**Implementation Guidance**:
1. **Oversight Tiers**:
   - **Human-in-the-Loop (HITL)**: Human approves every AI decision before execution
     - Use for: High-risk decisions (credit, hiring, medical diagnosis)
     - Example: AI recommends loan approval → underwriter reviews → final decision
   - **Human-on-the-Loop (HOTL)**: Human monitors AI decisions, intervenes when needed
     - Use for: Medium-risk automated decisions (content moderation, fraud detection)
     - Example: AI blocks transaction → human reviews flagged cases → override if false positive
   - **Human-over-the-Loop (HOVL)**: Periodic human audit of AI decisions
     - Use for: Low-risk decisions (product recommendations, email categorization)
     - Example: Weekly review of 100 random AI decisions for quality assurance

2. **Override Authority**:
   - Document who can override AI decisions
   - Track override rates as KPI (high rates indicate model problems)
   - Analyze override patterns to improve model

3. **Escalation Procedures**:
   - Unclear cases escalate from operator → manager → executive
   - Time-based escalation (if unresolved in 24h, escalate)
   - Critical cases bypass queue for immediate review

4. **AWS Implementation**:
   ```python
   # SageMaker Human Review Workflow (Amazon A2I)
   from sagemaker import get_execution_role
   import boto3

   a2i = boto3.client('sagemaker-a2i-runtime')

   # Start human loop for low-confidence predictions
   if prediction_confidence < 0.85:
       response = a2i.start_human_loop(
           HumanLoopName=f'review-{prediction_id}',
           FlowDefinitionArn=flow_arn,
           HumanLoopInput={
               'InputContent': json.dumps({
                   'prediction': prediction,
                   'confidence': prediction_confidence,
                   'features': feature_values
               })
           }
       )
   ```

**Evidence Examples**:
- [ ] Human oversight procedures documented per AI system
- [ ] Override authority matrix (who can override what)
- [ ] Human review queue dashboards (pending reviews, SLA compliance)
- [ ] Override rate reports and trend analysis

---

### TIAG-H-003: AI Accountability Matrix

**Description**: Assign clear ownership and accountability for AI systems and decisions.

**Framework Coverage**:
- ISO 42001: Annex A.3.2 (Accountability assignment)
- NIST AI RMF: GOVERN 1.1 (Governance structure)
- EU AI Act: Article 16(a) (Identified natural persons for oversight)
- SOC 2: CC2.1 (AI accountability roles)

**Implementation Guidance**:
1. **RACI Matrix for AI Governance**:
   - **Responsible**: AI Product Manager (day-to-day operations)
   - **Accountable**: VP of AI / Chief AI Officer (ultimate ownership)
   - **Consulted**: Legal, Security, Compliance, Data Science
   - **Informed**: Executive team, Board of Directors

2. **Role Definitions**:
   - **AI Owner**: Accountable for AI system performance, risks, compliance
   - **AI Ethics Committee**: Reviews high-risk AI systems before deployment
   - **AI Incident Response Team**: Responds to AI failures and incidents
   - **AI Auditor**: Independent validation of controls

3. **Governance Meetings**:
   - **Monthly**: AI Owner reviews model performance, incidents, risks
   - **Quarterly**: AI Ethics Committee reviews new high-risk deployments
   - **Annually**: Board review of AI strategy and risk posture

4. **Documentation**:
   - Org chart showing AI governance structure
   - Role descriptions with specific responsibilities
   - Decision-making authority levels (what requires executive approval)

**Evidence Examples**:
- [ ] AI governance RACI matrix
- [ ] AI Ethics Committee charter and membership
- [ ] Meeting minutes from governance forums
- [ ] Escalation pathways documented in procedures

---

## Control Domain 7: Incident Response (TIAG-I)

### TIAG-I-001: AI Incident Response Plan

**Description**: Establish procedures to detect, respond to, and recover from AI system failures and security incidents.

**Framework Coverage**:
- ISO 42001: Annex A.4.1 (AI incident response plan)
- NIST AI RMF: MANAGE 3.1 (Incident response)
- EU AI Act: Article 62 (Serious incident reporting)
- SOC 2: CC7.3 (Incident response for AI)

**Implementation Guidance**:
1. **AI Incident Types**:
   - **Performance Degradation**: Accuracy drops below SLA
   - **Bias/Fairness Issues**: Discriminatory outcomes detected
   - **Security Breach**: Model theft, data poisoning attack
   - **Safety Violation**: AI generates harmful outputs
   - **Regulatory Non-Compliance**: Failure to meet framework requirements

2. **Incident Classification** (aligns with EU AI Act "serious incident"):
   - **Critical**: Death, serious injury, fundamental rights violation
   - **High**: Significant financial loss, reputational damage, regulatory penalty risk
   - **Medium**: Service degradation, user complaints, minor compliance gap
   - **Low**: Isolated errors, no material impact

3. **Response Procedures**:
   - **Detection**: Automated monitoring alerts (TIAG-M-001)
   - **Triage**: Incident response team assesses severity
   - **Containment**: Disable affected AI system if necessary
   - **Investigation**: Root cause analysis using logs and telemetry
   - **Remediation**: Fix model, retrain, update controls
   - **Communication**: Notify stakeholders per communication matrix
   - **Post-Mortem**: Document lessons learned, update procedures

4. **EU AI Act Reporting**:
   - Serious incidents must be reported to authorities within 15 days
   - Maintain incident register with timeline, impact, resolution
   - Annual summary report to Board

5. **AWS Implementation**:
   ```python
   # CloudWatch alarm triggers Lambda for incident response
   import boto3

   def lambda_handler(event, context):
       # Parse alarm
       alarm = event['detail']['alarmName']

       if 'model-drift' in alarm:
           # Disable model endpoint
           sagemaker = boto3.client('sagemaker')
           sagemaker.delete_endpoint(EndpointName='prod-model')

           # Notify incident team
           sns = boto3.client('sns')
           sns.publish(
               TopicArn='arn:aws:sns:us-east-1:123456789012:ai-incidents',
               Subject='AI Incident: Model Drift Detected',
               Message=f'Model drift exceeded threshold. Endpoint disabled. Investigate immediately.'
           )
   ```

**Evidence Examples**:
- [ ] AI incident response playbook
- [ ] Incident classification matrix with EU AI Act mapping
- [ ] Incident register with all incidents (resolved and open)
- [ ] Post-incident review reports

---

### TIAG-I-003: AI Telemetry & Logging

**Description**: Collect and retain comprehensive logs of AI system activity for forensics, compliance, and monitoring.

**Framework Coverage**:
- ISO 42001: Annex A.4.2 (Logging and monitoring)
- NIST AI RMF: MEASURE 4.1 (Monitoring mechanisms)
- EU AI Act: Article 12 (Record-keeping obligations)
- SOC 2: CC7.2 (System monitoring)

**Implementation Guidance**:
1. **Required Logs**:
   - **API Access**: All Bedrock/SageMaker API calls (CloudTrail)
   - **Model Invocations**: Inputs, outputs, timestamps, user ID
   - **Guardrail Violations**: Blocked prompts, content filter hits
   - **Performance Metrics**: Latency, error rates, drift scores
   - **Configuration Changes**: Model updates, parameter changes, retraining events

2. **Retention Requirements**:
   - **EU AI Act**: Minimum 6 months for high-risk AI systems
   - **SOC 2**: 1 year minimum (aligned with audit cycle)
   - **Best Practice**: 2 years for forensic analysis capability

3. **Log Security**:
   - Encrypt logs at rest (S3 SSE-KMS)
   - Restrict access to authorized personnel (IAM policies)
   - Enable log integrity validation (S3 Object Lock, CloudTrail validation)
   - Centralize logs in secure account (AWS Security Lake, SIEM)

4. **AWS Implementation**:
   ```yaml
   # CloudTrail configuration for AI governance
   Resources:
     AIGovernanceTrail:
       Type: AWS::CloudTrail::Trail
       Properties:
         TrailName: ai-governance-trail
         S3BucketName: !Ref LogBucket
         IncludeGlobalServiceEvents: true
         IsLogging: true
         IsMultiRegionTrail: true
         EventSelectors:
           - ReadWriteType: All
             IncludeManagementEvents: true
             DataResources:
               - Type: AWS::SageMaker::Model
                 Values: ["arn:aws:sagemaker:*:*:model/*"]
               - Type: AWS::Bedrock::Model
                 Values: ["arn:aws:bedrock:*:*:*"]
   ```

**Evidence Examples**:
- [ ] CloudTrail configuration showing AI API logging
- [ ] S3 bucket policies for log retention and encryption
- [ ] Log access audit (who accessed logs, when, why)
- [ ] Log completeness verification (no gaps in timeline)

---

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)
- [ ] TIAG-R-001: Conduct AI risk assessment
- [ ] TIAG-D-001: Create AI system inventory
- [ ] TIAG-H-003: Establish AI accountability matrix
- [ ] TIAG-I-003: Enable comprehensive logging

**Deliverable**: Risk register, AI inventory, governance structure, logging infrastructure

### Phase 2: Security & Safety (Weeks 5-8)
- [ ] TIAG-S-001: Implement AI access controls (IAM roles)
- [ ] TIAG-S-003: Configure model encryption and protection
- [ ] TIAG-S-005: Deploy Bedrock Guardrails for LLM systems
- [ ] TIAG-M-001: Set up SageMaker Model Monitor

**Deliverable**: Security baseline, guardrails, monitoring dashboards

### Phase 3: Documentation & Transparency (Weeks 9-12)
- [ ] TIAG-D-003: Create Model Cards for all systems
- [ ] TIAG-D-005: Document training data provenance
- [ ] TIAG-T-001: Add user transparency disclosures
- [ ] TIAG-T-003: Implement explainability (SHAP/LIME)

**Deliverable**: Model Cards, data documentation, transparency notices, explainability tools

### Phase 4: Oversight & Incident Response (Weeks 13-16)
- [ ] TIAG-H-001: Implement human oversight workflows
- [ ] TIAG-I-001: Finalize AI incident response plan
- [ ] TIAG-M-003: Conduct first internal AI audit
- [ ] TIAG-R-003: Complete risk treatment plans

**Deliverable**: Oversight mechanisms, incident response playbook, audit report, risk treatment plans

### Phase 5: Continuous Compliance (Ongoing)
- [ ] Quarterly risk reviews
- [ ] Monthly model performance reviews
- [ ] Annual comprehensive audits
- [ ] Framework updates as regulations evolve

---

## Checklist: Minimum Viable AI Governance

Use this checklist to verify readiness for ISO 42001, NIST AI RMF, EU AI Act, and SOC 2 audits:

### Risk Management
- [ ] AI risk register covering all production systems
- [ ] Risk assessment methodology approved by leadership
- [ ] Quarterly risk reviews documented
- [ ] Risk treatment plans for all high risks

### Documentation
- [ ] AI system inventory is complete and current
- [ ] Model Cards exist for all production models
- [ ] Training data provenance is documented
- [ ] Documentation is version controlled

### Monitoring
- [ ] Model performance monitoring is automated
- [ ] Drift detection alerts are configured
- [ ] Monthly model health reports are generated
- [ ] Annual internal audit is scheduled

### Security
- [ ] IAM roles enforce least privilege for AI systems
- [ ] Models are encrypted at rest and in transit
- [ ] Guardrails are deployed for all LLM systems
- [ ] Access is logged via CloudTrail

### Transparency
- [ ] Users are notified of AI use
- [ ] Privacy policy describes AI processing
- [ ] Explainability is implemented for high-risk systems
- [ ] User education materials are available

### Oversight
- [ ] Human oversight mechanisms are defined per system
- [ ] Override authority is documented
- [ ] AI governance roles are assigned (RACI)
- [ ] AI Ethics Committee is established (for high-risk systems)

### Incident Response
- [ ] AI incident response plan is documented
- [ ] Incident classification includes EU AI Act criteria
- [ ] Logs are retained for 6+ months
- [ ] Post-incident reviews are conducted

---

**Document Version**: 1.0
**Last Updated**: 2025-01-15
**Maintained By**: Jose Ruiz-Vazquez, ISO/IEC 42001:2023 Lead Auditor
**Purpose**: Practical implementation guide for unified AI governance
