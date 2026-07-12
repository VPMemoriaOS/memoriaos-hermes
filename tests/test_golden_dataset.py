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


def test_golden_dataset(tmp_path: Path) -> None:
    repository_root = tmp_path / "memoria-repository"

    repository_root.mkdir()

    unit = CompilationUnit(
        source="manual",
        source_id="golden",
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
    # Golden Dataset
    #

    assert claim.subject == "John"
    assert claim.predicate == "lives_in"
    assert claim.object == "Prague"

    #
    # Traceability
    #

    assert observation.compilation_unit_id == unit.id
    assert observation.id in evidence.observation_ids
    assert evidence.id in claim.evidence_ids
    assert claim in knowledge.claims
    assert knowledge in memory.knowledge
