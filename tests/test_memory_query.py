from memoriaos.domain import CompilationUnit
from memoriaos.pipelines import (
    ObservationPipeline,
    EvidencePipeline,
    ClaimPipeline,
    KnowledgePipeline,
    MemoryPipeline,
)
from memoriaos.repository import (
    ObservationRepository,
    EvidenceRepository,
    ClaimRepository,
    KnowledgeRepository,
    MemoryRepository,
)


def test_memory_repository_load(tmp_path):
    observation_pipeline = ObservationPipeline(
        ObservationRepository(tmp_path)
    )

    evidence_pipeline = EvidencePipeline(
        EvidenceRepository(tmp_path)
    )

    claim_pipeline = ClaimPipeline(
        ClaimRepository(tmp_path)
    )

    knowledge_pipeline = KnowledgePipeline(
        KnowledgeRepository(tmp_path)
    )

    memory_repository = MemoryRepository(tmp_path)

    memory_pipeline = MemoryPipeline(
        memory_repository
    )

    unit = CompilationUnit(
        source="test",
        source_id="memory-query",
        text="John lives in Prague.",
    )

    observation = observation_pipeline.run(unit)
    evidence = evidence_pipeline.run(observation)
    claim = claim_pipeline.run(evidence)
    knowledge = knowledge_pipeline.run(claim)
    memory = memory_pipeline.run(knowledge)

    loaded = memory_repository.load(str(memory.id))

    assert loaded["id"] == str(memory.id)
    assert len(loaded["knowledge"]) == 1
