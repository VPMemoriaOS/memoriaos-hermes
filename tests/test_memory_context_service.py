from memoriaos.context import MemoryContext
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
from memoriaos.services import (
    MemoryRetrievalService,
    MemoryContextService,
)


def test_memory_context_service(tmp_path):
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

    retrieval_service = MemoryRetrievalService(
        memory_repository
    )

    context_service = MemoryContextService(
        retrieval_service
    )

    context = context_service.build()

    assert isinstance(context, MemoryContext)
    assert context.memories == ()

    unit = CompilationUnit(
        source="test",
        source_id="memory-context",
        text="John lives in Prague.",
    )

    observation = observation_pipeline.run(unit)
    evidence = evidence_pipeline.run(observation)
    claim = claim_pipeline.run(evidence)
    knowledge = knowledge_pipeline.run(claim)
    memory = memory_pipeline.run(knowledge)

    context = context_service.build()

    assert len(context.memories) == 1
    assert context.memories[0].id == memory.id
