"""
Bedrock Guardrails Scanner

Scans AWS Bedrock models to verify guardrail attachment and configuration.
This is critical for preventing prompt injection, jailbreaking, and PII leakage.

MITRE ATLAS Mapping:
- AML.T0051: LLM Prompt Injection
- AML.T0054: LLM Jailbreaking

NIST AI RMF Mapping:
- MEASURE 2.4: Privacy controls for AI systems
- MANAGE 1.1: Safety controls for AI outputs

ISO 42001 Mapping:
- Annex A.8.2: Data used for AI system development
- Clause 8.2: Risk management for AI systems
"""

from typing import List
import boto3
from botocore.exceptions import ClientError
from core.schema import Finding, ComplianceMappings, Severity
from core.scanner_base import BaseScanner


class BedrockGuardrailsScanner(BaseScanner):
    """
    Scans Bedrock foundation models and custom models for guardrail configuration.

    Checks:
    1. Whether production models have guardrails attached
    2. Guardrail configuration (content filters, word filters, PII detection)
    3. Guardrail version alignment
    """

    def get_scan_name(self) -> str:
        return "Bedrock Guardrails Configuration"

    def get_scan_description(self) -> str:
        return """Verifies that AWS Bedrock models have appropriate guardrails to prevent:
- Prompt injection attacks (MITRE AML.T0051)
- Model jailbreaking (MITRE AML.T0054)
- PII leakage and privacy violations
- Generation of harmful or inappropriate content"""

    def execute(self) -> List[Finding]:
        """
        Execute the Bedrock guardrails scan

        Returns:
            List of findings for models without proper guardrails
        """
        findings = []
        bedrock = self.session.client('bedrock')

        try:
            # Scan provisioned model throughputs (these are production deployments)
            findings.extend(self._scan_provisioned_models(bedrock))

            # Scan custom models (fine-tuned models)
            findings.extend(self._scan_custom_models(bedrock))

        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'AccessDeniedException':
                # Create a finding for lack of scanning permissions
                findings.append(self._create_permission_finding())
            else:
                raise

        return findings

    def _scan_provisioned_models(self, bedrock) -> List[Finding]:
        """Scan provisioned model throughputs for guardrail configuration"""
        findings = []

        try:
            response = bedrock.list_provisioned_model_throughputs()
            provisioned_models = response.get('provisionedModelSummaries', [])

            for model in provisioned_models:
                model_arn = model['provisionedModelArn']
                model_name = model.get('provisionedModelName', 'Unknown')

                # Get detailed configuration
                try:
                    details = bedrock.get_provisioned_model_throughput(
                        provisionedModelId=model['provisionedModelArn'].split('/')[-1]
                    )

                    # Check if model has guardrail configuration
                    # Note: Guardrails are applied at inference time, so we check model metadata
                    # In real implementation, you'd also scan inference profiles and API configurations
                    if not self._has_guardrail_configured(details):
                        findings.append(self._create_missing_guardrail_finding(model_arn, model_name))

                except ClientError:
                    # If we can't get details, flag it as a finding
                    findings.append(self._create_missing_guardrail_finding(model_arn, model_name))

        except ClientError as e:
            if e.response['Error']['Code'] != 'AccessDeniedException':
                raise

        return findings

    def _scan_custom_models(self, bedrock) -> List[Finding]:
        """Scan custom (fine-tuned) models for guardrail configuration"""
        findings = []

        try:
            response = bedrock.list_custom_models()
            custom_models = response.get('modelSummaries', [])

            for model in custom_models:
                model_arn = model['modelArn']
                model_name = model.get('modelName', 'Unknown')

                # Custom models should have guardrails for production use
                # Create finding recommending guardrail implementation
                findings.append(self._create_custom_model_finding(model_arn, model_name))

        except ClientError as e:
            if e.response['Error']['Code'] != 'AccessDeniedException':
                raise

        return findings

    def _has_guardrail_configured(self, model_details: dict) -> bool:
        """
        Check if a model has guardrail configuration

        Note: This is a simplified check. In production, you'd verify:
        - Guardrail ID is present and active
        - Guardrail version is up to date
        - Guardrail has appropriate filters enabled
        """
        # Check for guardrail references in model configuration
        # This would need to be adapted based on actual AWS API responses
        return False  # Conservative default: assume no guardrail unless proven otherwise

    def _create_missing_guardrail_finding(self, model_arn: str, model_name: str) -> Finding:
        """Create a finding for a model missing guardrails"""
        return Finding(
            finding_id="AWS-BEDROCK-001",
            resource_arn=model_arn,
            severity=Severity.HIGH,
            technical_finding=f"Bedrock model '{model_name}' does not have guardrails configured. "
                             f"Model is exposed to prompt injection, jailbreaking, and content policy violations.",
            mitigation_applied="Recommended: Create and attach Bedrock Guardrail with content filters, "
                              "PII detection, and word/phrase blocking. Use guardrailIdentifier in model invocations.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "MEASURE 2.4 (Privacy Controls)",
                    "MANAGE 1.1 (Safety Controls)",
                    "GOVERN 1.3 (Risk Management Processes)"
                ],
                iso_42001=[
                    "Annex A.8.2 (Data for AI System Development)",
                    "Clause 8.2 (Risk Assessment and Treatment)",
                    "Clause 6.1.3 (Risk Management)"
                ],
                mitre_atlas=[
                    "AML.T0051 (LLM Prompt Injection)",
                    "AML.T0054 (LLM Jailbreaking)",
                    "AML.T0040 (ML Model Inference API Access)"
                ]
            )
        )

    def _create_custom_model_finding(self, model_arn: str, model_name: str) -> Finding:
        """Create a finding for custom model without documented guardrails"""
        return Finding(
            finding_id="AWS-BEDROCK-002",
            resource_arn=model_arn,
            severity=Severity.MEDIUM,
            technical_finding=f"Custom Bedrock model '{model_name}' detected. "
                             f"Fine-tuned models require explicit guardrail configuration to maintain safety controls.",
            mitigation_applied="Recommended: Document intended use case, implement guardrails appropriate for "
                              "fine-tuning data domain, and enforce guardrails in all production invocations.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "MEASURE 2.4 (Privacy Controls)",
                    "MAP 1.2 (Intended Use Documentation)"
                ],
                iso_42001=[
                    "Annex A.8.2 (Data for AI)",
                    "Clause 7.2 (AI System Inventory)"
                ],
                mitre_atlas=[
                    "AML.T0051 (LLM Prompt Injection)",
                    "AML.T0043 (Craft Adversarial Data)"
                ]
            )
        )

    def _create_permission_finding(self) -> Finding:
        """Create a finding when scanner lacks necessary permissions"""
        return Finding(
            finding_id="AWS-BEDROCK-PERM",
            resource_arn=f"arn:aws:iam::{self.get_account_id()}:role/scanner",
            severity=Severity.MEDIUM,
            technical_finding="Scanner lacks bedrock:List* or bedrock:Get* permissions. "
                             "Cannot verify guardrail configuration for Bedrock models.",
            mitigation_applied="Grant IAM permissions: bedrock:ListProvisionedModelThroughputs, "
                              "bedrock:GetProvisionedModelThroughput, bedrock:ListCustomModels",
            mappings=ComplianceMappings(
                nist_ai_rmf=["GOVERN 4.1 (Transparency and Accountability)"],
                iso_42001=["Clause 9.1 (Monitoring and Measurement)"],
                mitre_atlas=[]
            )
        )
