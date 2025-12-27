# ISO 42001 to AWS Services Mapping

A comprehensive Python script that maps ISO/IEC 42001:2023 AI Management System controls to relevant AWS services that support compliance implementation.

## Overview

This project provides a practical mapping between ISO 42001 controls and AWS services, helping organizations:

- **Identify AWS services** that support specific ISO 42001 requirements
- **Implement AI governance** using cloud-native AWS capabilities
- **Accelerate compliance** by understanding which AWS services address specific controls
- **Design AI systems** that align with ISO 42001 from the ground up

## ISO 42001 Coverage

The mapping covers all major ISO 42001 clauses and Annex A controls:

### Mapped Controls

- **Clause 6:** Planning (Risk and opportunity management)
- **Clause 7:** Support (Documentation and data management)
- **Clause 9:** Performance Evaluation (Monitoring and internal audit)
- **Annex A Controls:**
  - A.2 - AI System Impact Assessment
  - A.3 - Data for AI System
  - A.4 - AI System Design and Development
  - A.5 - AI System Verification and Validation
  - A.6 - AI System Operation
  - A.7 - Human Oversight
  - A.8 - Transparency and Communication
  - A.9 - Information Security
  - A.10 - Privacy
  - A.11 - AI System Incident Management
  - A.12 - Logging and Monitoring
  - A.13 - AI System Lifecycle Management
  - A.14 - Third-Party AI Systems and Services
  - A.15 - Business Continuity for AI Systems

## AWS Services Mapped

The script maps to 50+ AWS services across multiple categories:

### AI/ML Platform
- Amazon SageMaker (Model Monitor, Clarify, Pipelines, Model Registry, Ground Truth, Data Wrangler)
- Amazon A2I (Augmented AI)
- Amazon Bedrock

### Data Management
- Amazon S3
- AWS Lake Formation
- AWS Glue (Data Catalog, DataBrew, Data Quality)
- Amazon Macie

### Security & Compliance
- AWS IAM
- AWS KMS
- AWS Security Hub
- AWS Audit Manager
- AWS Secrets Manager

### Monitoring & Observability
- Amazon CloudWatch
- AWS CloudTrail
- AWS X-Ray
- Amazon Detective

### Governance
- AWS Config
- AWS Service Catalog
- AWS Systems Manager

### Development & Deployment
- AWS CodePipeline
- AWS CodeCommit
- Amazon SageMaker Pipelines
- AWS Step Functions

## Usage

### Basic Usage

Run the script to generate mapping files in multiple formats:

```bash
python3 iso42001_aws_mapper.py
```

This generates three output files:

1. **iso42001_aws_mapping.json** - Complete mapping with metadata
2. **iso42001_aws_mapping.csv** - Spreadsheet format for analysis
3. **iso42001_aws_mapping.md** - Human-readable documentation

### Advanced Usage

Import as a Python module for custom analysis:

```python
from iso42001_aws_mapper import ISO42001AWSMapper

# Initialize mapper
mapper = ISO42001AWSMapper()

# Get all mappings
all_controls = mapper.get_all_mappings()

# Filter by ISO clause
planning_controls = mapper.get_mappings_by_clause("6 - Planning")

# Find all controls using specific service
sagemaker_controls = mapper.get_mappings_by_service("SageMaker")

# Get unique AWS services
services = mapper.get_unique_aws_services()

# Generate service usage statistics
stats = mapper.generate_service_summary()
```

## Output Formats

### JSON Structure

```json
{
  "metadata": {
    "title": "ISO 42001 to AWS Services Mapping",
    "version": "1.0",
    "date": "2025-12-27",
    "author": "Jose Ruiz-Vazquez"
  },
  "mappings": [
    {
      "control_id": "A.2",
      "control_name": "AI System Impact Assessment",
      "control_description": "...",
      "iso_clause": "Annex A",
      "aws_services": [
        {
          "service": "Amazon SageMaker Clarify",
          "implementation": "...",
          "control_support": "..."
        }
      ]
    }
  ]
}
```

### CSV Columns

- Control ID
- Control Name
- ISO Clause
- Control Description
- AWS Service
- Implementation Guidance
- Control Support

### Markdown Format

Organized by ISO clause with detailed service mappings and implementation guidance.

## Use Cases

### 1. ISO 42001 Implementation Planning

Identify which AWS services to deploy for each control requirement:

```python
mapper = ISO42001AWSMapper()
impact_assessment = mapper.get_mappings_by_clause("Annex A")
# Review AWS services needed for Annex A controls
```

### 2. AWS Service Inventory

Understand which ISO 42001 controls are addressed by your current AWS usage:

```python
# Check which controls CloudWatch supports
cloudwatch_coverage = mapper.get_mappings_by_service("CloudWatch")
print(f"CloudWatch supports {len(cloudwatch_coverage)} controls")
```

### 3. Gap Analysis

Compare current AWS architecture against ISO 42001 requirements:

1. Export mapping to CSV
2. Document current AWS services in use
3. Identify unmapped controls requiring additional services

### 4. Audit Preparation

Generate evidence of control implementation:

```python
# Export comprehensive mapping for auditors
mapper.export_to_markdown("audit_evidence/iso42001_aws_controls.md")
```

## Key AWS Services by Control Category

### AI System Development (A.4)
- Amazon SageMaker - End-to-end ML platform
- AWS CodePipeline - ML CI/CD
- Amazon SageMaker Pipelines - ML workflows

### Bias & Fairness (A.2)
- Amazon SageMaker Clarify - Bias detection and explainability
- Amazon SageMaker Model Cards - Model documentation

### Data Quality (A.3)
- AWS Glue DataBrew - Data quality profiling
- AWS Glue Data Quality - Automated quality checks
- Amazon SageMaker Data Wrangler - Data preparation

### Model Monitoring (A.5, A.6)
- Amazon SageMaker Model Monitor - Drift detection
- Amazon CloudWatch - Metrics and alarms
- AWS X-Ray - Distributed tracing

### Human Oversight (A.7)
- Amazon A2I - Human review workflows
- AWS Step Functions - Approval gates

### Security & Privacy (A.9, A.10)
- AWS IAM - Access control
- AWS KMS - Encryption
- Amazon Macie - PII discovery
- AWS Lake Formation - Data governance

### Audit & Compliance (A.12, 9.2)
- AWS Audit Manager - Evidence collection
- AWS CloudTrail - Audit logging
- AWS Config - Compliance monitoring

## Requirements

- Python 3.6 or higher
- No external dependencies (uses Python standard library only)

## Installation

```bash
# Clone or download the script
cd projects/iso42001-aws-mapping

# Make script executable
chmod +x iso42001_aws_mapper.py

# Run the script
python3 iso42001_aws_mapper.py
```

## Example Output

```
======================================================================
ISO 42001 to AWS Services Mapping Tool
======================================================================

Generating mapping files...

JSON export complete: iso42001_aws_mapping.json
CSV export complete: iso42001_aws_mapping.csv
Markdown export complete: iso42001_aws_mapping.md

Mapping Statistics:
----------------------------------------------------------------------
Total ISO 42001 Controls Mapped: 17
Total AWS Services Referenced: 50+

AWS Services by Usage Frequency:
----------------------------------------------------------------------
Amazon SageMaker Model Monitor                      4 controls
Amazon CloudWatch                                   4 controls
AWS CloudTrail                                      3 controls
Amazon SageMaker Clarify                           3 controls
```

## Project Context

This mapping tool was developed as part of an AI governance portfolio demonstrating:

- **AI Risk Management** - Practical control implementation using cloud services
- **ISO 42001 Expertise** - Deep understanding of AI management system requirements
- **Cloud Architecture** - AWS service selection for governance and compliance
- **Compliance Engineering** - Translating standards into technical implementation

## Integration with AI Governance Framework

This mapping complements other AI governance activities:

1. **AI Impact Assessment** - Use mapped services to implement assessment processes
2. **Risk Mitigation** - Select AWS services that address identified risks
3. **Audit Readiness** - Document AWS service usage as control evidence
4. **Continuous Monitoring** - Deploy AWS monitoring services per ISO 42001 requirements

## Future Enhancements

Potential expansions of this tool:

- Azure and GCP service mappings
- Control implementation templates
- Automated AWS resource compliance checking
- Integration with AWS Config for real-time compliance
- Cost analysis for ISO 42001 compliance architecture

## References

- **ISO/IEC 42001:2023** - Information technology — Artificial intelligence — Management system
- **AWS Well-Architected Framework** - Machine Learning Lens
- **NIST AI Risk Management Framework** - Complementary risk framework
- **AWS Security Best Practices** - Implementation guidance

## Author

**Jose Ruiz-Vazquez**
AI Governance & Risk Professional
ISO/IEC 42001:2023 Lead Auditor

## License

This mapping is provided for educational and professional purposes. ISO 42001 standard content remains property of ISO.

---

*Part of the AI Governance Portfolio - Demonstrating practical AI risk management and compliance engineering.*
