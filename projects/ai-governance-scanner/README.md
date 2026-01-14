# AI Governance Scanner

**Automated compliance scanning for AWS AI services** - bridging technical reality with executive governance.

## 🎯 Overview

The AI Governance Scanner is a command-line tool that audits AWS AI services (Bedrock, SageMaker) for compliance with:
- **NIST AI Risk Management Framework (AI RMF)**
- **ISO/IEC 42001:2023** (AI Management Systems)
- **MITRE ATLAS** (Adversarial Threat Landscape for AI Systems)

Unlike traditional security scanners, this tool creates an "evidence chain" from technical vulnerabilities to regulatory requirements, making AI governance actionable for both technical teams and executives.

## 🚀 Key Features

### 1. The "Rosetta Stone" Architecture
Each finding maps technical reality to three dimensions:
```json
{
  "technical_finding": "No Bedrock Guardrail attached to production model",
  "mappings": {
    "nist_ai_rmf": ["MEASURE 2.4 (Privacy)", "MANAGE 1.1 (Safety)"],
    "iso_42001": ["Annex A.8.2 (Data for AI)", "Clause 8.2 (Risk)"],
    "mitre_atlas": ["AML.T0051 (Prompt Injection)", "AML.T0054 (Jailbreaking)"]
  }
}
```

### 2. AI-Generated Executive Summaries
Uses AWS Bedrock (Claude) to translate technical findings into business impact:

> "The absence of guardrails on this production chatbot model creates direct regulatory exposure under the EU AI Act's transparency and safety requirements. Attackers can exploit this vulnerability through prompt injection (MITRE AML.T0051) to bypass content policies and extract sensitive training data. Implementing guardrails satisfies NIST AI RMF MEASURE 2.4 privacy controls and ISO 42001 Clause 8.2 risk treatment requirements."

### 3. Multiple Output Formats
- **JSON**: Machine-readable for SIEM/GRC platform integration
- **Summary**: Human-readable terminal output for quick review
- **Dashboard**: Interactive HTML report for executive presentations

### 4. Framework Crosswalk - The Implementation Guide
The scanner detects *what's wrong*. The **[Framework Crosswalk](crosswalk/)** shows *how to fix it* while satisfying multiple frameworks simultaneously.

**Includes**:
- **Master Crosswalk**: Row-by-row mapping of ISO 42001, NIST AI RMF, EU AI Act, and SOC 2 requirements
- **Executive Summary**: Business case for integrated governance (67% faster, 60% cost reduction, 827% Year 1 ROI)
- **Unified Controls**: 22 implementation-ready controls (TIAG-R-001 through TIAG-I-003) with AWS code examples

**Example Integration**:
```
Scanner Finding → "No Bedrock Guardrail attached"
         ↓
Crosswalk Impact → Violates ISO 42001 Annex A.8.1, NIST MANAGE 1.1,
                   EU AI Act Article 15, SOC 2 CC6.8
         ↓
Unified Controls → TIAG-S-005 provides Bedrock Guardrail implementation
                   that satisfies all four frameworks at once
```

👉 **[Explore the Framework Crosswalk →](crosswalk/)**

## 📦 Installation

```bash
# Clone the repository
cd projects/ai-governance-scanner

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure
```

## 🔍 Available Scans

### Current Implementation (Proof of Concept)

| Scan | Service | Checks | Frameworks |
|------|---------|--------|-----------|
| **bedrock-guardrails** | AWS Bedrock | Guardrail attachment and configuration | NIST AI RMF MEASURE 2.4<br>ISO 42001 Annex A.8.2<br>MITRE AML.T0051/T0054 |
| **sagemaker-model-cards** | SageMaker | Model documentation completeness | NIST AI RMF MAP 1.2, MEASURE 2.1<br>ISO 42001 Clause 7.2, 8.3<br>MITRE AML.T0020 |

### Roadmap (Remaining 3 Core Scans)

| Scan | Service | Attack Vector | Impact |
|------|---------|---------------|---------|
| **s3-training-data** | S3 Buckets | Data Poisoning (AML.T0020) | Unauthorized tampering with training datasets |
| **sagemaker-model-monitor** | SageMaker | Performance Drift (MEASURE 2.1) | Unsafe or inaccurate model predictions |
| **iam-ai-permissions** | IAM Roles | Lateral Movement | Over-privileged AI execution roles |

## 💻 Usage

### List Available Scans
```bash
python scanner.py --list-scans
```

### Run Specific Scan
```bash
# Bedrock guardrails check
python scanner.py --scan bedrock-guardrails --format summary

# SageMaker model cards audit
python scanner.py --scan sagemaker-model-cards --format json --output findings.json
```

### Run All Scans
```bash
# Terminal output
python scanner.py --scan all --format summary

# JSON output for integration
python scanner.py --scan all --format json --output report.json

# HTML dashboard for executives
python scanner.py --scan all --format dashboard --output governance-report.html
```

### Advanced Options
```bash
# Specify AWS region and profile
python scanner.py --scan all --region us-west-2 --profile production

# Disable AI-generated summaries (use templates instead)
python scanner.py --scan all --no-ai-narrator
```

## 📊 Output Examples

### Summary Format
```
================================================================================
AI GOVERNANCE SCAN REPORT
================================================================================
Scan Time:    2025-01-15T14:30:00Z
AWS Account:  123456789012
AWS Region:   us-east-1

SUMMARY
--------------------------------------------------------------------------------
Total Findings: 3

  Critical    : 0
  High        : 2
  Medium      : 1

FINDINGS DETAIL
--------------------------------------------------------------------------------

[1] AWS-BEDROCK-001 - High
    Resource: arn:aws:bedrock:us-east-1:123456789012:provisioned-model/prod-chatbot
    Issue:    No Bedrock Guardrail attached to production model...

    Executive Summary:
    The absence of guardrails creates regulatory exposure under the EU AI Act...
```

### Dashboard Format

**[View Sample Dashboard →](examples/sample_dashboard.html)** | **[Generate Your Own](examples/generate_dashboard.py)**

The HTML dashboard includes:
- ✅ Executive summary cards (Critical/High/Medium/Low counts)
- ✅ Risk exposure meter (weighted by severity)
- ✅ Detailed findings with compliance tag visualization
- ✅ Print-optimized layout for audit documentation

## 🏗️ Architecture

### Project Structure
```
ai-governance-scanner/
├── scanner.py                 # CLI entry point
├── requirements.txt           # Python dependencies
├── core/                      # Core framework
│   ├── schema.py             # JSON schema definitions
│   ├── scanner_base.py       # Abstract base scanner class
│   └── narrator.py           # AI executive summary generator
├── scans/                     # Individual scan modules
│   ├── bedrock_guardrails.py
│   └── sagemaker_model_cards.py
├── outputs/                   # Output generators
│   └── templates/
│       └── dashboard.py      # HTML dashboard generator
└── examples/
    └── sample_output.json    # Example scan result
```

### Design Principles

1. **Separation of Concerns**
   - Each scan is a standalone module inheriting from `BaseScanner`
   - Findings use standardized schema for consistent output
   - Narrator layer handles AI translation independently

2. **Extensibility**
   - Add new scans by creating a class in `scans/` directory
   - Register in `scans/__init__.py` AVAILABLE_SCANNERS dict
   - No changes to core framework required

3. **Evidence Chain**
   ```
   AWS API Response → Technical Finding → Attack Vector → Compliance Control
   ```

## 🎓 Why This Approach Excels

### For Auditors
- **Direct framework mapping**: "Show me ISO 42001 Clause 8.2 compliance" → filtered findings
- **Evidence collection**: AWS API responses prove control effectiveness
- **Audit trail**: JSON output includes timestamps, resource ARNs, control citations

### For Security Engineers
- **Attack context**: MITRE ATLAS references explain exploit scenarios
- **Actionable remediation**: AWS CLI commands for mitigation
- **Integration ready**: JSON output for SIEM, Splunk, Datadog

### For Executives
- **Business impact**: AI-generated summaries focus on liability and risk
- **Regulatory alignment**: EU AI Act, SOX, GLBA compliance visibility
- **Visual dashboards**: HTML reports for board presentations

## 🔐 IAM Permissions Required

The scanner requires read-only permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:ListProvisionedModelThroughputs",
        "bedrock:GetProvisionedModelThroughput",
        "bedrock:ListCustomModels",
        "sagemaker:ListModels",
        "sagemaker:ListModelCards",
        "sagemaker:DescribeModelCard",
        "sts:GetCallerIdentity"
      ],
      "Resource": "*"
    }
  ]
}
```

For AI narrator functionality, add:
```json
{
  "Effect": "Allow",
  "Action": ["bedrock:InvokeModel"],
  "Resource": "arn:aws:bedrock:*::foundation-model/anthropic.claude-*"
}
```

## 🛣️ Roadmap

### Phase 1: Core Scans (Current)
- ✅ Bedrock Guardrails
- ✅ SageMaker Model Cards
- ⏳ S3 Training Data Security
- ⏳ SageMaker Model Monitor
- ⏳ IAM AI Permissions

### Phase 2: Enhanced Reporting
- ⏳ PDF export for audit documentation
- ⏳ Trend analysis (compare scans over time)
- ⏳ Compliance posture scoring
- ⏳ Integration with Vanta, Drata, OneTrust

### Phase 3: Expanded Coverage
- ⏳ AWS Comprehend (PII detection in production data)
- ⏳ AWS Rekognition (facial recognition governance)
- ⏳ AWS Forecast (prediction accuracy monitoring)
- ⏳ Azure OpenAI Service support
- ⏳ Google Vertex AI support

## 📚 References

### Standards & Frameworks
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) - AI Management Systems
- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial Threat Landscape for AI

### AWS Documentation
- [AWS Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [SageMaker Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)

## 🤝 Contributing

This is a proof-of-concept project demonstrating the "Rosetta Stone" approach to AI governance scanning. To extend:

1. **Add a new scan**: Create a class in `scans/` inheriting from `BaseScanner`
2. **Enhance narrator**: Improve prompt engineering in `core/narrator.py`
3. **Improve dashboard**: Add charts/graphs in `outputs/templates/dashboard.py`

## 📄 License

This project is part of a professional portfolio demonstrating AI governance expertise.

## 👤 Author

**Jose Ruiz-Vazquez**
AI Governance & Risk Professional
ISO/IEC 42001:2023 Lead Auditor
[LinkedIn](https://linkedin.com/in/joseruiz1571) | [Email](mailto:joseruiz1571@gmail.com)

---

*Building trust through systematic AI governance and risk management.*
