#!/usr/bin/env python3

from __future__ import annotations

import sys

from pathlib import Path

from memoriaos.domain import CompilationUnit
from memoriaos.pipelines import (
    ObservationPipeline,
    EvidencePipeline,
    ClaimPipeline,
    KnowledgePipeline,
)
from memoriaos.repository import (
    ObservationRepository,
    EvidenceRepository,
    ClaimRepository,
)


def repository_root() -> Path:
    workspace = Path(__file__).resolve().parents[2]

    repository = workspace / "memoria-repository"

    if not repository.exists():
        raise RuntimeError(
            f"Repository not found: {repository}"
        )

    return repository


def main() -> int:

    unit = CompilationUnit(
        source="manual",
        source_id="demo",
        text="John lives in Prague.",
    )

    root = repository_root()

    observation_pipeline = ObservationPipeline(
        ObservationRepository(root)
    )

    evidence_pipeline = EvidencePipeline(
        EvidenceRepository(root)
    )

    claim_pipeline = ClaimPipeline(
        ClaimRepository(root)
    )

    knowledge_pipeline = KnowledgePipeline()

    observation = observation_pipeline.run(unit)

    evidence = evidence_pipeline.run(observation)

    claim = claim_pipeline.run(evidence)

    knowledge = knowledge_pipeline.run(claim)

    print()
    print("========== RESULT ==========")
    print(f"Observation : {observation.id}")
    print(f"Evidence    : {evidence.id}")
    print(f"Claim       : {claim.id}")
    print(f"Knowledge   : {knowledge.id}")
    print()
    print(f"Subject     : {claim.subject}")
    print(f"Predicate   : {claim.predicate}")
    print(f"Object      : {claim.object}")
    print("============================")

    return 0


if __name__ == "__main__":
    sys.exit(main())
