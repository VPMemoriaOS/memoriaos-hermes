from pathlib import Path

from memoriaos.domain import CompilationUnit
from memoriaos.pipelines import (
    ClaimPipeline,
    EvidencePipeline,
    KnowledgePipeline,
    MemoryPipeline,
    ObservationPipeline,
)
from memoriaos.repository import (
    ClaimRepository,
    EvidenceRepository,
    KnowledgeRepository,
    MemoryRepository,
    ObservationRepository,
)


def test_traceability(tmp_path: Path) -> None:
    repository_root = tmp_path / "memoria-repository"
    repository_root.mkdir()

    unit = CompilationUnit(
        source="manual",
        source_id="traceability",
        text="John lives in Prague.",
    )

    observation = ObservationPipeline(
        ObservationRepository(repository_root)
    ).run(unit)

    evidence = EvidencePipeline(
        EvidenceRepository(repository_root)
    ).run(observation)

    claim = ClaimPipeline(
        ClaimRepository(repository_root)
    ).run(evidence)

    knowledge = KnowledgePipeline(
        KnowledgeRepository(repository_root)
    ).run(claim)

    memory = MemoryPipeline(
        MemoryRepository(repository_root)
    ).run(knowledge)

    #
    # Traceability
    #

    assert observation.compilation_unit_id == unit.id

    assert len(evidence.observation_ids) == 1
    assert evidence.observation_ids[0] == observation.id

    assert len(claim.evidence_ids) == 1
    assert claim.evidence_ids[0] == evidence.id

    assert len(knowledge.claims) == 1
    assert knowledge.claims[0].id == claim.id

    assert len(memory.knowledge) == 1
    assert memory.knowledge[0].id == knowledge.id
