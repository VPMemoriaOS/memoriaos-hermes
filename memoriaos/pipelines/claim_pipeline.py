from __future__ import annotations

from uuid import uuid4

from memoriaos.domain.claim import Claim
from memoriaos.domain.evidence import Evidence
from memoriaos.extractors.rule_based_claim_extractor import (
    RuleBasedClaimExtractor,
)


class ClaimPipeline:
    """
    Transforms Evidence into Claim.
    """

    def __init__(self) -> None:
        self._extractor = RuleBasedClaimExtractor()

    def run(self, evidence: Evidence) -> Claim:
        parts = self._extractor.extract(evidence.content)

        return Claim(
            id=uuid4(),
            subject=parts.subject,
            predicate=parts.predicate,
            object=parts.object,
            evidence_ids=evidence.observation_ids,
        )
