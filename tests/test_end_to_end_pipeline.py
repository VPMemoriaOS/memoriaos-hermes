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


def test_end_to_end_pipeline(tmp_path: Path) -> None:
    repository_root = tmp_path / "memoria-repository"

    repository_root.mkdir()

    unit = CompilationUnit(
        source="manual",
        source_id="test",
        text="John lives in Prague.",
    )

    observation_pipeline = ObservationPipeline(
        ObservationRepository(repository_root)
    )

    evidence_pipeline = EvidencePipeline(
        EvidenceRepository(repository_root)
    )

    claim_pipeline = ClaimPipeline(
        ClaimRepository(repository_root)
    )

    knowledge_pipeline = KnowledgePipeline(
        KnowledgeRepository(repository_root)
    )

    memory_pipeline = MemoryPipeline(
        MemoryRepository(repository_root)
    )

    observation = observation_pipeline.run(unit)
    evidence = evidence_pipeline.run(observation)
    claim = claim_pipeline.run(evidence)
    knowledge = knowledge_pipeline.run(claim)
    memory = memory_pipeline.run(knowledge)

    #
    # UUIDs
    #

    assert observation.id is not None
    assert evidence.id is not None
    assert claim.id is not None
    assert knowledge.id is not None
    assert memory.id is not None

    #
    # Extracted knowledge
    #

    assert claim.subject == "John"
    assert claim.predicate == "lives_in"
    assert claim.object == "Prague"

    #
    # Repository layout
    #

    assert (repository_root / "Observation").exists()
    assert (repository_root / "Evidence").exists()
    assert (repository_root / "Claim").exists()
    assert (repository_root / "Knowledge").exists()
    assert (repository_root / "Memory").exists()
