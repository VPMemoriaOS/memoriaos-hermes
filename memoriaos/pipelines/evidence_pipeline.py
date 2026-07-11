from __future__ import annotations

from uuid import uuid4

from memoriaos.domain.evidence import Evidence
from memoriaos.domain.observation import Observation
from memoriaos.repository.evidence_repository import EvidenceRepository


class EvidencePipeline:
    """
    Transforms an Observation into an Evidence artifact.
    """

    def __init__(self, repository: EvidenceRepository):
        self._repository = repository

    def run(self, observation: Observation) -> Evidence:
        """
        Create and persist Evidence from a single Observation.
        """

        self._validate(observation)

        evidence = Evidence(
            id=uuid4(),
            content=observation.text,
            observation_ids=(observation.id,),
        )

        self._repository.save(evidence)

        return evidence

    @staticmethod
    def _validate(observation: Observation) -> None:
        if not observation.text.strip():
            raise ValueError("Observation text must not be empty.")
