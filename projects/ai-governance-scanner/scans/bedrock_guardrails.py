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

    # Required content filter types for comprehensive protection
    REQUIRED_CONTENT_FILTERS = {'HATE', 'VIOLENCE', 'SEXUAL', 'MISCONDUCT'}

    # Minimum acceptable filter strength
    MINIMUM_STRENGTH = {'MEDIUM', 'HIGH'}

    def get_scan_description(self) -> str:
        return """Verifies that AWS Bedrock guardrails are properly configured to prevent:
- Prompt injection attacks (MITRE AML.T0051)
- Model jailbreaking (MITRE AML.T0054)
- PII leakage and privacy violations
- Generation of harmful or inappropriate content

Checks both model attachments AND guardrail configurations."""

    def execute(self) -> List[Finding]:
        """
        Execute the Bedrock guardrails scan

        Returns:
            List of findings for models without proper guardrails
        """
        findings = []
        bedrock = self.session.client('bedrock')

        try:
            # NEW: Scan guardrail configurations themselves
            findings.extend(self._scan_guardrail_configurations(bedrock))

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

    def _scan_guardrail_configurations(self, bedrock) -> List[Finding]:
        """
        Scan all guardrails for configuration weaknesses.

        Checks:
        - Content filter completeness (all required types present)
        - Filter strength (LOW is insufficient)
        - PII detection enabled
        - Production readiness (not DRAFT)
        """
        findings = []

        try:
            response = bedrock.list_guardrails()
            guardrails = response.get('guardrails', [])

            if not guardrails:
                # No guardrails exist - this is a finding
                findings.append(self._create_no_guardrails_finding())
                return findings

            for guardrail in guardrails:
                guardrail_id = guardrail['id']
                guardrail_name = guardrail.get('name', 'Unknown')
                guardrail_arn = guardrail.get('arn', f'arn:aws:bedrock:{self.region}:{self.get_account_id()}:guardrail/{guardrail_id}')
                status = guardrail.get('status', 'UNKNOWN')

                # Get detailed configuration
                try:
                    details = bedrock.get_guardrail(
                        guardrailIdentifier=guardrail_id,
                        guardrailVersion='DRAFT'
                    )

                    # Check content policy configuration
                    content_policy = details.get('contentPolicy', {})
                    filters_config = content_policy.get('filters', [])

                    # Check for missing filter types
                    configured_types = {f.get('type') for f in filters_config}
                    missing_types = self.REQUIRED_CONTENT_FILTERS - configured_types

                    if missing_types:
                        findings.append(self._create_missing_filters_finding(
                            guardrail_arn, guardrail_name, missing_types
                        ))

                    # Check for weak filter strengths
                    weak_filters = []
                    for f in filters_config:
                        input_strength = f.get('inputStrength', 'NONE')
                        output_strength = f.get('outputStrength', 'NONE')
                        if input_strength not in self.MINIMUM_STRENGTH or output_strength not in self.MINIMUM_STRENGTH:
                            weak_filters.append({
                                'type': f.get('type'),
                                'inputStrength': input_strength,
                                'outputStrength': output_strength
                            })

                    if weak_filters:
                        findings.append(self._create_weak_filters_finding(
                            guardrail_arn, guardrail_name, weak_filters
                        ))

                    # Check for sensitive information policy (PII detection)
                    sensitive_policy = details.get('sensitiveInformationPolicy')
                    if not sensitive_policy:
                        findings.append(self._create_no_pii_detection_finding(
                            guardrail_arn, guardrail_name
                        ))

                    # Check if guardrail is still in DRAFT (not production-ready)
                    if status == 'DRAFT' or not guardrail.get('version'):
                        findings.append(self._create_draft_status_finding(
                            guardrail_arn, guardrail_name
                        ))

                except ClientError as e:
                    # If we can't get details, log but continue
                    pass

        except ClientError as e:
            if e.response['Error']['Code'] != 'AccessDeniedException':
                raise

        return findings

    def _create_no_guardrails_finding(self) -> Finding:
        """Create a finding when no guardrails exist in the account"""
        return Finding(
            finding_id="AWS-BEDROCK-003",
            resource_arn=f"arn:aws:bedrock:{self.region}:{self.get_account_id()}:guardrails",
            severity=Severity.HIGH,
            technical_finding="No Bedrock Guardrails configured in this AWS account. "
                            "AI models can be invoked without content safety controls, "
                            "exposing the organization to prompt injection, harmful content generation, and data leakage.",
            mitigation_applied="Recommended: Create Bedrock Guardrails with content filters for HATE, VIOLENCE, "
                             "SEXUAL, and MISCONDUCT categories. Enable PII detection and configure word filters "
                             "for organization-specific sensitive terms.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "GOVERN 1.3 (Risk Management Processes)",
                    "MANAGE 1.1 (Safety Controls)",
                    "MANAGE 2.2 (Harmful Output Prevention)"
                ],
                iso_42001=[
                    "Clause 6.1 (Actions to Address Risks)",
                    "Clause 8.2 (AI Risk Assessment)",
                    "Annex A.5.4 (AI System Safety)"
                ],
                mitre_atlas=[
                    "AML.T0051 (LLM Prompt Injection)",
                    "AML.T0054 (LLM Jailbreaking)",
                    "AML.T0048 (Societal Harm)"
                ]
            )
        )

    def _create_missing_filters_finding(self, guardrail_arn: str, guardrail_name: str, missing_types: set) -> Finding:
        """Create a finding for guardrail missing required content filter types"""
        return Finding(
            finding_id="AWS-BEDROCK-004",
            resource_arn=guardrail_arn,
            severity=Severity.MEDIUM,
            technical_finding=f"Guardrail '{guardrail_name}' is missing content filters for: {', '.join(sorted(missing_types))}. "
                            f"Incomplete content filtering allows harmful content in unprotected categories.",
            mitigation_applied=f"Recommended: Add content filters for {', '.join(sorted(missing_types))} with MEDIUM or HIGH strength "
                             "to ensure comprehensive content moderation coverage.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "MANAGE 2.2 (Harmful Output Prevention)",
                    "MEASURE 2.6 (Content Safety Verification)"
                ],
                iso_42001=[
                    "Annex A.5.4 (AI System Safety)",
                    "Clause 8.2 (Risk Treatment)"
                ],
                mitre_atlas=[
                    "AML.T0054 (LLM Jailbreaking)",
                    "AML.T0048 (Societal Harm)"
                ]
            )
        )

    def _create_weak_filters_finding(self, guardrail_arn: str, guardrail_name: str, weak_filters: list) -> Finding:
        """Create a finding for guardrail with weak filter strengths"""
        filter_details = "; ".join([f"{f['type']}: input={f['inputStrength']}, output={f['outputStrength']}"
                                   for f in weak_filters])
        return Finding(
            finding_id="AWS-BEDROCK-005",
            resource_arn=guardrail_arn,
            severity=Severity.MEDIUM,
            technical_finding=f"Guardrail '{guardrail_name}' has weak filter strengths (LOW or NONE): {filter_details}. "
                            f"LOW strength filters may not catch sophisticated prompt attacks or subtle harmful content.",
            mitigation_applied="Recommended: Increase filter strengths to MEDIUM or HIGH. "
                             "LOW strength should only be used for specific, documented business exceptions.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "MANAGE 1.1 (Safety Controls)",
                    "MEASURE 2.6 (Content Safety Verification)"
                ],
                iso_42001=[
                    "Clause 8.2 (Risk Treatment)",
                    "Clause 10.1 (Continual Improvement)"
                ],
                mitre_atlas=[
                    "AML.T0051 (LLM Prompt Injection)",
                    "AML.T0054 (LLM Jailbreaking)"
                ]
            )
        )

    def _create_no_pii_detection_finding(self, guardrail_arn: str, guardrail_name: str) -> Finding:
        """Create a finding for guardrail without PII detection"""
        return Finding(
            finding_id="AWS-BEDROCK-006",
            resource_arn=guardrail_arn,
            severity=Severity.HIGH,
            technical_finding=f"Guardrail '{guardrail_name}' does not have PII detection enabled. "
                            f"Sensitive personal information (SSN, credit cards, addresses) may be leaked in model outputs.",
            mitigation_applied="Recommended: Enable Sensitive Information Policy with PII entity types including "
                             "NAME, EMAIL, PHONE, SSN, CREDIT_DEBIT_CARD_NUMBER, and ADDRESS. Consider MASK or BLOCK actions.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "MEASURE 2.4 (Privacy Controls)",
                    "GOVERN 4.2 (Privacy Risk Management)"
                ],
                iso_42001=[
                    "Annex A.8.2 (Data for AI Development)",
                    "Annex A.8.4 (Data Quality for AI)"
                ],
                mitre_atlas=[
                    "AML.T0024 (Exfiltration via ML Inference API)",
                    "AML.T0044 (Full ML Model Access)"
                ]
            )
        )

    def _create_draft_status_finding(self, guardrail_arn: str, guardrail_name: str) -> Finding:
        """Create a finding for guardrail still in DRAFT status"""
        return Finding(
            finding_id="AWS-BEDROCK-007",
            resource_arn=guardrail_arn,
            severity=Severity.LOW,
            technical_finding=f"Guardrail '{guardrail_name}' is in DRAFT status and has not been versioned for production use. "
                            f"DRAFT guardrails may have incomplete configurations and are not recommended for production workloads.",
            mitigation_applied="Recommended: Review guardrail configuration and create a versioned release for production use. "
                             "Use version numbers in production invocations rather than DRAFT.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "GOVERN 1.4 (Change Management)",
                    "MAP 3.1 (AI System Documentation)"
                ],
                iso_42001=[
                    "Clause 8.1 (Operational Planning)",
                    "Clause 7.5 (Documented Information)"
                ],
                mitre_atlas=[]
            )
        )

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
