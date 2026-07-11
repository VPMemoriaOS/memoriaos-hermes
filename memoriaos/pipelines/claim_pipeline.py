from __future__ import annotations

from uuid import uuid4

from memoriaos.domain.claim import Claim
from memoriaos.domain.evidence import Evidence
from memoriaos.extractors.rule_based_claim_extractor import (
    RuleBasedClaimExtractor,
)
from memoriaos.repository.claim_repository import ClaimRepository


class ClaimPipeline:
    """
    Transforms Evidence into a Claim artifact.
    """

    def __init__(self, repository: ClaimRepository):
        self._repository = repository
        self._extractor = RuleBasedClaimExtractor()

    def run(self, evidence: Evidence) -> Claim:
        parts = self._extractor.extract(evidence.content)

        claim = Claim(
            id=uuid4(),
            subject=parts.subject,
            predicate=parts.predicate,
            object=parts.object,
            evidence_ids=(evidence.id,),
        )

        self._repository.save(claim)

        return claim
