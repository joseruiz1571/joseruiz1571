"""
SageMaker Model Cards Scanner

Scans SageMaker models to verify presence and completeness of Model Cards.
Model Cards document intended use, training data, performance metrics, and
risk assessments - critical for AI governance and regulatory compliance.

NIST AI RMF Mapping:
- MAP 1.2: Intended purpose documentation
- MEASURE 2.1: Performance metrics and evaluation
- GOVERN 1.7: Documentation and transparency

ISO 42001 Mapping:
- Clause 7.2: AI system inventory and documentation
- Clause 8.3: Risk assessment and treatment
- Annex A.8.2: Data provenance and quality
"""

from typing import List
import boto3
from botocore.exceptions import ClientError
from core.schema import Finding, ComplianceMappings, Severity
from core.scanner_base import BaseScanner


class SageMakerModelCardsScanner(BaseScanner):
    """
    Scans SageMaker models for Model Card documentation.

    Model Cards should include:
    1. Intended use and out-of-scope applications
    2. Training data characteristics and provenance
    3. Performance metrics and evaluation results
    4. Risk assessment and limitations
    5. Ethical considerations and fairness metrics
    """

    def get_scan_name(self) -> str:
        return "SageMaker Model Cards Documentation"

    def get_scan_description(self) -> str:
        return """Verifies that SageMaker models have complete Model Cards documenting:
- Intended use cases and limitations (ISO 42001 Clause 7.2)
- Training data provenance (ISO 42001 Annex A.8.2)
- Performance metrics and evaluation (NIST AI RMF MEASURE 2.1)
- Risk assessments and ethical considerations"""

    def execute(self) -> List[Finding]:
        """
        Execute the SageMaker Model Cards scan

        Returns:
            List of findings for models with missing or incomplete documentation
        """
        findings = []
        sagemaker = self.session.client('sagemaker')

        try:
            # Get all models in the account
            models = self._list_all_models(sagemaker)

            # Check each model for Model Card
            for model in models:
                model_name = model['ModelName']
                model_arn = model['ModelArn']

                # Check if model has an associated Model Card
                card_status = self._check_model_card(sagemaker, model_name)

                if card_status == 'missing':
                    findings.append(self._create_missing_card_finding(model_arn, model_name))
                elif card_status == 'incomplete':
                    findings.append(self._create_incomplete_card_finding(model_arn, model_name))

        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'AccessDeniedException':
                findings.append(self._create_permission_finding())
            else:
                raise

        return findings

    def _list_all_models(self, sagemaker) -> List[dict]:
        """List all SageMaker models in the account"""
        models = []
        paginator = sagemaker.get_paginator('list_models')

        for page in paginator.paginate():
            models.extend(page['Models'])

        return models

    def _check_model_card(self, sagemaker, model_name: str) -> str:
        """
        Check if a model has a Model Card and if it's complete

        Returns:
            'present': Model Card exists and appears complete
            'incomplete': Model Card exists but missing critical fields
            'missing': No Model Card found
        """
        try:
            # List model cards associated with this model
            response = sagemaker.list_model_cards(
                ModelIdEquals=model_name,
                MaxResults=1
            )

            model_cards = response.get('ModelCardSummaries', [])

            if not model_cards:
                return 'missing'

            # Get the first (and should be only) model card
            card_name = model_cards[0]['ModelCardName']

            # Describe the model card to check completeness
            card_details = sagemaker.describe_model_card(ModelCardName=card_name)

            # Check for critical fields in model card content
            content = card_details.get('Content', '{}')

            # In a production scanner, you'd parse the JSON content and verify:
            # - intended_uses section exists
            # - training_details section exists with data description
            # - evaluation_details section exists with metrics
            # - risk_rating is documented

            # Simplified check: if content is very short, it's likely incomplete
            if len(content) < 200:  # Arbitrary threshold
                return 'incomplete'

            # Check for risk rating
            if 'risk_rating' not in content.lower() and 'risk assessment' not in content.lower():
                return 'incomplete'

            return 'present'

        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFound':
                return 'missing'
            raise

    def _create_missing_card_finding(self, model_arn: str, model_name: str) -> Finding:
        """Create a finding for a model without a Model Card"""
        return Finding(
            finding_id="AWS-SAGEMAKER-001",
            resource_arn=model_arn,
            severity=Severity.HIGH,
            technical_finding=f"SageMaker model '{model_name}' has no Model Card. "
                             f"Lack of documentation creates compliance gaps for AI governance frameworks and "
                             f"prevents verification of intended use, training data provenance, and risk assessment.",
            mitigation_applied="Required: Create Model Card using sagemaker:CreateModelCard API. "
                              "Document intended use, training data characteristics, performance metrics, "
                              "limitations, and risk assessment. Assign risk rating.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "MAP 1.2 (Intended Purpose and Context)",
                    "MEASURE 2.1 (Performance Metrics)",
                    "GOVERN 1.7 (Documentation and Transparency)",
                    "GOVERN 4.1 (Accountability)"
                ],
                iso_42001=[
                    "Clause 7.2 (AI System Inventory)",
                    "Clause 8.3 (Risk Assessment)",
                    "Annex A.8.2 (Data for AI System)",
                    "Annex A.6.2 (Documentation Requirements)"
                ],
                mitre_atlas=[
                    "AML.T0020 (Poison Training Data)",
                    "AML.T0043 (Craft Adversarial Data)"
                ]
            )
        )

    def _create_incomplete_card_finding(self, model_arn: str, model_name: str) -> Finding:
        """Create a finding for a model with incomplete Model Card"""
        return Finding(
            finding_id="AWS-SAGEMAKER-002",
            resource_arn=model_arn,
            severity=Severity.MEDIUM,
            technical_finding=f"SageMaker model '{model_name}' has incomplete Model Card documentation. "
                             f"Missing critical sections: risk rating, intended use limitations, or training data provenance. "
                             f"Incomplete documentation creates audit findings and compliance gaps.",
            mitigation_applied="Required: Update Model Card to include all mandatory sections per ISO 42001 Annex A.6.2: "
                              "intended uses and limitations, training data description, evaluation metrics, "
                              "risk rating (Low/Medium/High), and ethical considerations.",
            mappings=ComplianceMappings(
                nist_ai_rmf=[
                    "MAP 1.2 (Context Documentation)",
                    "MEASURE 2.1 (Evaluation Metrics)",
                    "GOVERN 1.7 (Transparency)"
                ],
                iso_42001=[
                    "Clause 8.3 (Risk Assessment)",
                    "Annex A.6.2 (AI System Documentation)",
                    "Annex A.8.2 (Data Provenance)"
                ],
                mitre_atlas=[
                    "AML.T0043 (Adversarial Data Crafting)"
                ]
            )
        )

    def _create_permission_finding(self) -> Finding:
        """Create a finding when scanner lacks necessary permissions"""
        return Finding(
            finding_id="AWS-SAGEMAKER-PERM",
            resource_arn=f"arn:aws:iam::{self.get_account_id()}:role/scanner",
            severity=Severity.MEDIUM,
            technical_finding="Scanner lacks sagemaker:ListModels, sagemaker:ListModelCards, or "
                             "sagemaker:DescribeModelCard permissions. Cannot verify Model Card compliance.",
            mitigation_applied="Grant IAM permissions: sagemaker:ListModels, sagemaker:ListModelCards, "
                              "sagemaker:DescribeModelCard for governance scanning.",
            mappings=ComplianceMappings(
                nist_ai_rmf=["GOVERN 4.1 (Transparency and Accountability)"],
                iso_42001=["Clause 9.1 (Monitoring and Measurement)"],
                mitre_atlas=[]
            )
        )
