from __future__ import annotations

from uuid import uuid4

from memoriaos.domain.evidence import Evidence
from memoriaos.domain.observation import Observation
from memoriaos.repository.evidence_repository import EvidenceRepository


class EvidencePipeline:
    """Transforms Observations into Evidence artifacts."""

    def __init__(self, repository: EvidenceRepository):
        self._repository = repository

    def run(self, observation: Observation) -> Evidence:
        # Placeholder implementation.
        evidence = Evidence(
            id=str(uuid4()),
            content=observation.text,
            observation_ids=(observation.id,),
        )

        self._repository.save(evidence)
        return evidence
