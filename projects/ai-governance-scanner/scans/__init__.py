"""
AI Governance Scanner - Scan Modules

Collection of specific scanners for AWS AI services.
Each scanner focuses on a single control domain.
"""

from .bedrock_guardrails import BedrockGuardrailsScanner
from .sagemaker_model_cards import SageMakerModelCardsScanner

# Registry of all available scanners
AVAILABLE_SCANNERS = {
    'bedrock-guardrails': BedrockGuardrailsScanner,
    'sagemaker-model-cards': SageMakerModelCardsScanner,
}

__all__ = [
    'BedrockGuardrailsScanner',
    'SageMakerModelCardsScanner',
    'AVAILABLE_SCANNERS'
]
