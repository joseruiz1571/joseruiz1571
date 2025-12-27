#!/usr/bin/env python3
"""
ISO 42001 to AWS Services Mapping Script

This script maps ISO/IEC 42001:2023 AI Management System controls to relevant AWS services
that can help implement and support compliance with those controls.

Author: Jose Ruiz-Vazquez
"""

import json
import csv
from typing import Dict, List
from datetime import datetime


class ISO42001AWSMapper:
    """Maps ISO 42001 controls to AWS services with implementation guidance."""

    def __init__(self):
        self.mappings = self._initialize_mappings()

    def _initialize_mappings(self) -> List[Dict]:
        """Initialize the comprehensive mapping of ISO 42001 controls to AWS services."""

        return [
            # Clause 6: Planning - AI System Impact Assessment
            {
                "control_id": "6.1.2",
                "control_name": "Understanding AI System Risks and Opportunities",
                "control_description": "Organization shall determine risks and opportunities related to AI systems",
                "iso_clause": "6 - Planning",
                "aws_services": [
                    {
                        "service": "Amazon SageMaker Model Monitor",
                        "implementation": "Monitor ML models for data drift, model quality degradation, and bias detection to identify risks in production AI systems",
                        "control_support": "Continuous monitoring and alerting on model performance and data quality"
                    },
                    {
                        "service": "AWS Security Hub",
                        "implementation": "Centralized security findings and compliance checks across AWS resources used for AI/ML workloads",
                        "control_support": "Risk identification and security posture assessment"
                    },
                    {
                        "service": "Amazon CloudWatch",
                        "implementation": "Monitor AI system performance metrics, set alarms for anomalies, and track operational risks",
                        "control_support": "Real-time visibility into AI system health and performance"
                    }
                ]
            },

            # Clause 7.5: Data Management
            {
                "control_id": "7.5",
                "control_name": "Documented Information and Data Management",
                "control_description": "Organization shall determine documented information necessary for effectiveness of AI management system",
                "iso_clause": "7 - Support",
                "aws_services": [
                    {
                        "service": "Amazon S3",
                        "implementation": "Store training data, model artifacts, and documentation with versioning, lifecycle policies, and encryption",
                        "control_support": "Secure, versioned storage for AI system documentation and data"
                    },
                    {
                        "service": "AWS Lake Formation",
                        "implementation": "Centralized data governance for AI training data with fine-grained access controls and data catalog",
                        "control_support": "Data governance, lineage tracking, and access management"
                    },
                    {
                        "service": "AWS Glue Data Catalog",
                        "implementation": "Metadata management and data discovery for AI/ML datasets",
                        "control_support": "Data documentation, classification, and discovery"
                    },
                    {
                        "service": "Amazon Macie",
                        "implementation": "Automated discovery and classification of sensitive data in training datasets",
                        "control_support": "Data privacy and sensitive data identification"
                    }
                ]
            },

            # AI System Impact Assessment
            {
                "control_id": "A.2",
                "control_name": "AI System Impact Assessment",
                "control_description": "Assess potential impacts of AI systems on individuals, society, and environment",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon SageMaker Clarify",
                        "implementation": "Detect bias in training data and models, generate explainability reports for impact assessment",
                        "control_support": "Bias detection, fairness metrics, and model explainability"
                    },
                    {
                        "service": "AWS Audit Manager",
                        "implementation": "Automate evidence collection for impact assessment processes and compliance audits",
                        "control_support": "Audit trail and compliance evidence management"
                    },
                    {
                        "service": "Amazon SageMaker Model Cards",
                        "implementation": "Document model characteristics, intended use, performance metrics, and ethical considerations",
                        "control_support": "Model documentation and impact transparency"
                    }
                ]
            },

            # Data Quality Management
            {
                "control_id": "A.3",
                "control_name": "Data for AI System",
                "control_description": "Ensure data quality, relevance, and suitability for AI system purposes",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "AWS Glue DataBrew",
                        "implementation": "Data quality profiling, cleansing, and normalization for ML training data",
                        "control_support": "Data quality assessment and transformation"
                    },
                    {
                        "service": "Amazon SageMaker Data Wrangler",
                        "implementation": "Visual data preparation and quality checks for ML workflows",
                        "control_support": "Data quality validation and feature engineering"
                    },
                    {
                        "service": "Amazon SageMaker Ground Truth",
                        "implementation": "High-quality data labeling with built-in quality controls and validation",
                        "control_support": "Training data quality and labeling accuracy"
                    },
                    {
                        "service": "AWS Glue Data Quality",
                        "implementation": "Define and monitor data quality rules, detect anomalies in data pipelines",
                        "control_support": "Automated data quality monitoring and validation"
                    }
                ]
            },

            # AI System Development and Acquisition
            {
                "control_id": "A.4",
                "control_name": "AI System Design and Development",
                "control_description": "Establish processes for AI system design, development, and acquisition",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon SageMaker",
                        "implementation": "End-to-end ML development platform with built-in security, governance, and MLOps capabilities",
                        "control_support": "Standardized ML development lifecycle"
                    },
                    {
                        "service": "AWS CodePipeline",
                        "implementation": "Automated CI/CD pipelines for ML model training and deployment with approval gates",
                        "control_support": "Controlled and auditable model deployment process"
                    },
                    {
                        "service": "Amazon SageMaker Pipelines",
                        "implementation": "Define, orchestrate, and manage ML workflows with versioning and lineage tracking",
                        "control_support": "Reproducible and traceable ML development"
                    },
                    {
                        "service": "AWS CodeCommit",
                        "implementation": "Version control for ML code, models, and configurations",
                        "control_support": "Code versioning and change management"
                    }
                ]
            },

            # AI System Validation and Testing
            {
                "control_id": "A.5",
                "control_name": "AI System Verification and Validation",
                "control_description": "Verify and validate AI systems meet specified requirements and perform as intended",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon SageMaker Model Monitor",
                        "implementation": "Continuous validation of model quality, data drift, and model drift in production",
                        "control_support": "Automated model validation and performance monitoring"
                    },
                    {
                        "service": "Amazon SageMaker Experiments",
                        "implementation": "Track, compare, and evaluate ML experiments and model performance",
                        "control_support": "Model validation and performance comparison"
                    },
                    {
                        "service": "AWS Step Functions",
                        "implementation": "Orchestrate automated testing workflows for AI systems with error handling",
                        "control_support": "Automated validation workflows"
                    }
                ]
            },

            # AI System Operation and Monitoring
            {
                "control_id": "A.6",
                "control_name": "AI System Operation",
                "control_description": "Operate AI systems in accordance with intended use and monitor performance",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon SageMaker Endpoints",
                        "implementation": "Scalable, managed model hosting with auto-scaling and blue/green deployments",
                        "control_support": "Reliable and controlled model deployment"
                    },
                    {
                        "service": "Amazon CloudWatch",
                        "implementation": "Monitor AI system metrics, logs, and set alarms for operational issues",
                        "control_support": "Operational monitoring and alerting"
                    },
                    {
                        "service": "AWS X-Ray",
                        "implementation": "Distributed tracing for AI/ML applications to identify performance bottlenecks",
                        "control_support": "Application performance monitoring and debugging"
                    },
                    {
                        "service": "Amazon EventBridge",
                        "implementation": "Event-driven automation for AI system operations and incident response",
                        "control_support": "Automated operational responses"
                    }
                ]
            },

            # Transparency and Explainability
            {
                "control_id": "A.7",
                "control_name": "Human Oversight",
                "control_description": "Implement appropriate human oversight of AI system operation",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon A2I (Augmented AI)",
                        "implementation": "Human review workflows for ML predictions requiring oversight or low-confidence scenarios",
                        "control_support": "Human-in-the-loop AI systems"
                    },
                    {
                        "service": "Amazon SageMaker Clarify",
                        "implementation": "Generate explainability reports to support human understanding and oversight",
                        "control_support": "Model explainability for human reviewers"
                    },
                    {
                        "service": "AWS Step Functions",
                        "implementation": "Workflow orchestration with manual approval steps for critical AI decisions",
                        "control_support": "Human approval gates in AI workflows"
                    }
                ]
            },

            # AI System Transparency
            {
                "control_id": "A.8",
                "control_name": "Transparency and Communication",
                "control_description": "Provide transparency about AI system capabilities, limitations, and operation",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon SageMaker Model Cards",
                        "implementation": "Document and share model information including intended use, limitations, and performance",
                        "control_support": "Model transparency documentation"
                    },
                    {
                        "service": "Amazon SageMaker Clarify",
                        "implementation": "Generate bias reports and feature importance explanations for stakeholders",
                        "control_support": "Explainability and transparency reporting"
                    },
                    {
                        "service": "AWS Systems Manager Documents",
                        "implementation": "Document AI system operational procedures and runbooks",
                        "control_support": "Operational transparency and documentation"
                    }
                ]
            },

            # Information Security Controls
            {
                "control_id": "A.9",
                "control_name": "Information Security",
                "control_description": "Implement information security controls for AI systems and data",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "AWS IAM",
                        "implementation": "Fine-grained access control for AI/ML resources using roles and policies",
                        "control_support": "Identity and access management"
                    },
                    {
                        "service": "AWS KMS",
                        "implementation": "Encryption key management for data at rest and in transit for AI workloads",
                        "control_support": "Data encryption and key management"
                    },
                    {
                        "service": "Amazon Macie",
                        "implementation": "Automated sensitive data discovery and protection in AI training data",
                        "control_support": "Data privacy and protection"
                    },
                    {
                        "service": "AWS Secrets Manager",
                        "implementation": "Secure storage and rotation of API keys, credentials used by AI systems",
                        "control_support": "Credential management and rotation"
                    },
                    {
                        "service": "AWS PrivateLink",
                        "implementation": "Private connectivity between VPC and AI/ML services without internet exposure",
                        "control_support": "Network security and isolation"
                    }
                ]
            },

            # Privacy Controls
            {
                "control_id": "A.10",
                "control_name": "Privacy",
                "control_description": "Protect privacy of individuals in AI system data processing",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon Macie",
                        "implementation": "Identify and protect personally identifiable information (PII) in training data",
                        "control_support": "PII discovery and classification"
                    },
                    {
                        "service": "AWS Lake Formation",
                        "implementation": "Cell-level and column-level security for sensitive data in data lakes",
                        "control_support": "Fine-grained data access controls"
                    },
                    {
                        "service": "AWS Glue DataBrew",
                        "implementation": "Data masking and anonymization for privacy-preserving ML",
                        "control_support": "Data de-identification and pseudonymization"
                    },
                    {
                        "service": "AWS Clean Rooms",
                        "implementation": "Collaborative analytics without sharing underlying sensitive data",
                        "control_support": "Privacy-preserving data collaboration"
                    }
                ]
            },

            # Incident Management
            {
                "control_id": "A.11",
                "control_name": "AI System Incident Management",
                "control_description": "Manage incidents related to AI system operation and failures",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "AWS Systems Manager Incident Manager",
                        "implementation": "Incident response automation, escalation, and post-incident analysis for AI systems",
                        "control_support": "Structured incident response process"
                    },
                    {
                        "service": "Amazon CloudWatch Alarms",
                        "implementation": "Automated alerting on AI system anomalies and failures",
                        "control_support": "Incident detection and notification"
                    },
                    {
                        "service": "Amazon SNS",
                        "implementation": "Multi-channel incident notification and escalation",
                        "control_support": "Incident communication and alerting"
                    },
                    {
                        "service": "AWS CloudTrail",
                        "implementation": "Audit logs for incident investigation and root cause analysis",
                        "control_support": "Forensic analysis and audit trail"
                    }
                ]
            },

            # Audit and Logging
            {
                "control_id": "A.12",
                "control_name": "Logging and Monitoring",
                "control_description": "Maintain logs of AI system activities for audit and compliance",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "AWS CloudTrail",
                        "implementation": "Comprehensive API logging for all AWS AI/ML service interactions",
                        "control_support": "Audit trail and compliance logging"
                    },
                    {
                        "service": "Amazon CloudWatch Logs",
                        "implementation": "Centralized log aggregation and retention for AI system operations",
                        "control_support": "Log management and retention"
                    },
                    {
                        "service": "AWS Audit Manager",
                        "implementation": "Automated evidence collection and audit report generation",
                        "control_support": "Compliance auditing and reporting"
                    },
                    {
                        "service": "Amazon S3 with Object Lock",
                        "implementation": "Immutable log storage for regulatory compliance",
                        "control_support": "Tamper-proof log retention"
                    }
                ]
            },

            # Model Governance
            {
                "control_id": "A.13",
                "control_name": "AI System Lifecycle Management",
                "control_description": "Manage AI systems throughout their lifecycle from development to decommissioning",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "Amazon SageMaker Model Registry",
                        "implementation": "Centralized model versioning, approval workflows, and deployment tracking",
                        "control_support": "Model lifecycle and governance"
                    },
                    {
                        "service": "Amazon SageMaker Pipelines",
                        "implementation": "End-to-end ML workflow automation with lineage tracking",
                        "control_support": "Reproducible ML lifecycle management"
                    },
                    {
                        "service": "AWS Service Catalog",
                        "implementation": "Standardized, approved ML infrastructure and project templates",
                        "control_support": "Governance through approved patterns"
                    },
                    {
                        "service": "AWS Config",
                        "implementation": "Track configuration changes and compliance of AI/ML resources",
                        "control_support": "Configuration management and compliance"
                    }
                ]
            },

            # Supply Chain Management
            {
                "control_id": "A.14",
                "control_name": "Third-Party AI Systems and Services",
                "control_description": "Manage risks associated with third-party AI systems, components, and services",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "AWS Marketplace",
                        "implementation": "Curated ML models and algorithms from verified vendors with security scanning",
                        "control_support": "Vetted third-party AI components"
                    },
                    {
                        "service": "Amazon SageMaker JumpStart",
                        "implementation": "Pre-built, tested ML solutions and models from AWS and partners",
                        "control_support": "Managed third-party model integration"
                    },
                    {
                        "service": "AWS Artifact",
                        "implementation": "Access compliance reports and agreements for AWS services",
                        "control_support": "Vendor compliance documentation"
                    },
                    {
                        "service": "AWS Security Hub",
                        "implementation": "Security assessment of third-party integrations and dependencies",
                        "control_support": "Third-party security monitoring"
                    }
                ]
            },

            # Business Continuity
            {
                "control_id": "A.15",
                "control_name": "Business Continuity for AI Systems",
                "control_description": "Ensure continuity of AI system operations during disruptions",
                "iso_clause": "Annex A",
                "aws_services": [
                    {
                        "service": "AWS Backup",
                        "implementation": "Automated backup of ML models, training data, and configurations",
                        "control_support": "Data and model backup/recovery"
                    },
                    {
                        "service": "Amazon S3 Cross-Region Replication",
                        "implementation": "Geographic redundancy for critical AI system data and models",
                        "control_support": "Disaster recovery and redundancy"
                    },
                    {
                        "service": "AWS Elastic Disaster Recovery",
                        "implementation": "Fast recovery of AI system infrastructure and applications",
                        "control_support": "Business continuity and disaster recovery"
                    },
                    {
                        "service": "Amazon SageMaker Multi-AZ",
                        "implementation": "High availability model endpoints across availability zones",
                        "control_support": "Service availability and resilience"
                    }
                ]
            },

            # Performance Monitoring
            {
                "control_id": "9.1",
                "control_name": "Monitoring, Measurement, Analysis and Evaluation",
                "control_description": "Monitor and measure AI management system performance",
                "iso_clause": "9 - Performance Evaluation",
                "aws_services": [
                    {
                        "service": "Amazon CloudWatch Dashboards",
                        "implementation": "Custom dashboards for AI system KPIs and performance metrics",
                        "control_support": "Performance visualization and reporting"
                    },
                    {
                        "service": "Amazon QuickSight",
                        "implementation": "Business intelligence and analytics for AI system performance data",
                        "control_support": "Advanced analytics and insights"
                    },
                    {
                        "service": "AWS Cost Explorer",
                        "implementation": "Track and analyze costs of AI/ML workloads for ROI assessment",
                        "control_support": "Cost monitoring and optimization"
                    },
                    {
                        "service": "Amazon SageMaker Model Monitor",
                        "implementation": "Automated model performance monitoring with baseline comparisons",
                        "control_support": "ML-specific performance monitoring"
                    }
                ]
            },

            # Internal Audit
            {
                "control_id": "9.2",
                "control_name": "Internal Audit",
                "control_description": "Conduct internal audits of AI management system",
                "iso_clause": "9 - Performance Evaluation",
                "aws_services": [
                    {
                        "service": "AWS Audit Manager",
                        "implementation": "Automated audit evidence collection with pre-built and custom frameworks",
                        "control_support": "Continuous audit readiness"
                    },
                    {
                        "service": "AWS Config Rules",
                        "implementation": "Automated compliance checking against AI governance policies",
                        "control_support": "Continuous compliance monitoring"
                    },
                    {
                        "service": "AWS CloudTrail Insights",
                        "implementation": "Anomaly detection in AWS API usage for audit investigations",
                        "control_support": "Audit trail analysis"
                    },
                    {
                        "service": "Amazon Detective",
                        "implementation": "Security investigation and analysis for audit findings",
                        "control_support": "Forensic analysis for audits"
                    }
                ]
            }
        ]

    def get_all_mappings(self) -> List[Dict]:
        """Return all control mappings."""
        return self.mappings

    def get_mappings_by_clause(self, clause: str) -> List[Dict]:
        """Get mappings filtered by ISO clause."""
        return [m for m in self.mappings if clause.lower() in m['iso_clause'].lower()]

    def get_mappings_by_service(self, service_name: str) -> List[Dict]:
        """Get all controls that map to a specific AWS service."""
        results = []
        for mapping in self.mappings:
            for svc in mapping['aws_services']:
                if service_name.lower() in svc['service'].lower():
                    results.append({
                        'control_id': mapping['control_id'],
                        'control_name': mapping['control_name'],
                        'service': svc['service'],
                        'implementation': svc['implementation'],
                        'control_support': svc['control_support']
                    })
        return results

    def get_unique_aws_services(self) -> List[str]:
        """Get a unique list of all AWS services referenced."""
        services = set()
        for mapping in self.mappings:
            for svc in mapping['aws_services']:
                services.add(svc['service'])
        return sorted(list(services))

    def export_to_json(self, filename: str):
        """Export mappings to JSON file."""
        output = {
            'metadata': {
                'title': 'ISO 42001 to AWS Services Mapping',
                'version': '1.0',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'author': 'Jose Ruiz-Vazquez',
                'description': 'Comprehensive mapping of ISO/IEC 42001:2023 controls to AWS services'
            },
            'mappings': self.mappings,
            'summary': {
                'total_controls': len(self.mappings),
                'total_aws_services': len(self.get_unique_aws_services()),
                'aws_services': self.get_unique_aws_services()
            }
        }

        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)
        print(f"JSON export complete: {filename}")

    def export_to_csv(self, filename: str):
        """Export mappings to CSV file."""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Control ID',
                'Control Name',
                'ISO Clause',
                'Control Description',
                'AWS Service',
                'Implementation Guidance',
                'Control Support'
            ])

            for mapping in self.mappings:
                for svc in mapping['aws_services']:
                    writer.writerow([
                        mapping['control_id'],
                        mapping['control_name'],
                        mapping['iso_clause'],
                        mapping['control_description'],
                        svc['service'],
                        svc['implementation'],
                        svc['control_support']
                    ])

        print(f"CSV export complete: {filename}")

    def export_to_markdown(self, filename: str):
        """Export mappings to Markdown file."""
        with open(filename, 'w') as f:
            f.write("# ISO 42001 to AWS Services Mapping\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write(f"**Author:** Jose Ruiz-Vazquez\n\n")
            f.write("## Overview\n\n")
            f.write("This document maps ISO/IEC 42001:2023 AI Management System controls to AWS services ")
            f.write("that can help organizations implement and maintain compliance.\n\n")
            f.write(f"**Total Controls Mapped:** {len(self.mappings)}\n\n")
            f.write(f"**AWS Services Referenced:** {len(self.get_unique_aws_services())}\n\n")
            f.write("---\n\n")

            # Group by clause
            clauses = {}
            for mapping in self.mappings:
                clause = mapping['iso_clause']
                if clause not in clauses:
                    clauses[clause] = []
                clauses[clause].append(mapping)

            for clause in sorted(clauses.keys()):
                f.write(f"## {clause}\n\n")

                for mapping in clauses[clause]:
                    f.write(f"### {mapping['control_id']} - {mapping['control_name']}\n\n")
                    f.write(f"**Description:** {mapping['control_description']}\n\n")
                    f.write("**AWS Service Mappings:**\n\n")

                    for svc in mapping['aws_services']:
                        f.write(f"#### {svc['service']}\n\n")
                        f.write(f"- **Implementation:** {svc['implementation']}\n")
                        f.write(f"- **Control Support:** {svc['control_support']}\n\n")

                    f.write("---\n\n")

        print(f"Markdown export complete: {filename}")

    def generate_service_summary(self) -> Dict:
        """Generate summary statistics by AWS service."""
        service_stats = {}

        for mapping in self.mappings:
            for svc in mapping['aws_services']:
                service_name = svc['service']
                if service_name not in service_stats:
                    service_stats[service_name] = {
                        'control_count': 0,
                        'controls': []
                    }
                service_stats[service_name]['control_count'] += 1
                service_stats[service_name]['controls'].append(mapping['control_id'])

        return service_stats


def main():
    """Main execution function."""
    print("=" * 70)
    print("ISO 42001 to AWS Services Mapping Tool")
    print("=" * 70)
    print()

    mapper = ISO42001AWSMapper()

    # Export to all formats
    print("Generating mapping files...\n")
    mapper.export_to_json('iso42001_aws_mapping.json')
    mapper.export_to_csv('iso42001_aws_mapping.csv')
    mapper.export_to_markdown('iso42001_aws_mapping.md')

    print("\nMapping Statistics:")
    print("-" * 70)
    print(f"Total ISO 42001 Controls Mapped: {len(mapper.get_all_mappings())}")
    print(f"Total AWS Services Referenced: {len(mapper.get_unique_aws_services())}")

    print("\nAWS Services by Usage Frequency:")
    print("-" * 70)
    service_summary = mapper.generate_service_summary()
    sorted_services = sorted(service_summary.items(),
                            key=lambda x: x[1]['control_count'],
                            reverse=True)

    for service, stats in sorted_services[:10]:
        print(f"{service:45} {stats['control_count']:2} controls")

    print("\nSample Control Mapping:")
    print("-" * 70)
    sample = mapper.get_all_mappings()[0]
    print(f"Control: {sample['control_id']} - {sample['control_name']}")
    print(f"Clause: {sample['iso_clause']}")
    print(f"AWS Services: {len(sample['aws_services'])}")
    for svc in sample['aws_services'][:2]:
        print(f"  - {svc['service']}")

    print("\n" + "=" * 70)
    print("Mapping generation complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
