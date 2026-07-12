from __future__ import annotations

import uuid

from datetime import UTC, datetime

from memoriaos.domain import (
    CompilationUnit,
    Observation,
    Provenance,
)
from memoriaos.repository import ObservationRepository


PIPELINE_NAME = "OBS-PIPELINE-001"


class ObservationPipeline:
    """
    Transforms a CompilationUnit into an Observation artifact.
    """

    def __init__(self, repository: ObservationRepository):
        self._repository = repository

    def run(self, unit: CompilationUnit) -> Observation:
        self._validate(unit)

        unit = self._canonicalize(unit)

        observation = self._create_observation(unit)

        self._repository.save(observation)

        return observation

    @staticmethod
    def _validate(unit: CompilationUnit) -> None:
        if not unit.text.strip():
            raise ValueError("Observation text is empty.")

        if not unit.source_id.strip():
            raise ValueError("Source identifier is empty.")

    @staticmethod
    def _canonicalize(unit: CompilationUnit) -> CompilationUnit:
        return CompilationUnit(
            id=unit.id,
            source=unit.source,
            source_id=unit.source_id.strip(),
            text=unit.text.strip(),
        )

    @staticmethod
    def _create_observation(unit: CompilationUnit) -> Observation:
        now = datetime.now(UTC)

        provenance = Provenance(
            source_type=unit.source,
            source_identifier=unit.source_id,
            captured_at=now,
            captured_by=PIPELINE_NAME,
        )

        return Observation(
            id=uuid.uuid4(),
            compilation_unit_id=unit.id,
            created=now,
            provenance=provenance,
            text=unit.text,
        )
