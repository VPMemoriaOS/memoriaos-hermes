from memoriaos.context import MemoryContext
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
    KnowledgeRepository,
)


def test_knowledge_pipeline_accepts_memory_context(tmp_path):
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

    unit = CompilationUnit(
        source="test",
        source_id="memory-aware",
        text="John lives in Prague.",
    )

    observation = observation_pipeline.run(unit)
    evidence = evidence_pipeline.run(observation)
    claim = claim_pipeline.run(evidence)

    context = MemoryContext(memories=())

    knowledge = knowledge_pipeline.run(
        claim,
        context=context,
    )

    assert knowledge.claims[0].id == claim.id
