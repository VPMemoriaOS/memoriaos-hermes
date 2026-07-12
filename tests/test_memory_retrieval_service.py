from memoriaos import (
    ClaimPipeline,
    CompilationUnit,
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
from memoriaos.services import MemoryRetrievalService


def test_memory_retrieval_service(tmp_path):
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

    service = MemoryRetrievalService(memory_repository)

    assert service.retrieve() == []

    unit = CompilationUnit(
        source="test",
        source_id="memory-retrieval",
        text="John lives in Prague.",
    )

    observation = observation_pipeline.run(unit)
    evidence = evidence_pipeline.run(observation)
    claim = claim_pipeline.run(evidence)
    knowledge = knowledge_pipeline.run(claim)
    memory = memory_pipeline.run(knowledge)

    result = service.retrieve()

    assert len(result) == 1
    assert result[0].id == memory.id
