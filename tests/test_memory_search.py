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


def build_memory(memory_pipeline, knowledge_pipeline,
                 claim_pipeline, evidence_pipeline,
                 observation_pipeline, text):

    unit = CompilationUnit(
        source="test",
        source_id=text,
        text=text,
    )

    observation = observation_pipeline.run(unit)
    evidence = evidence_pipeline.run(observation)
    claim = claim_pipeline.run(evidence)
    knowledge = knowledge_pipeline.run(claim)

    return memory_pipeline.run(knowledge)


def test_memory_repository_search(tmp_path):

    repository = MemoryRepository(tmp_path)

    assert repository.search() == []

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

    memory_pipeline = MemoryPipeline(repository)

    first = build_memory(
        memory_pipeline,
        knowledge_pipeline,
        claim_pipeline,
        evidence_pipeline,
        observation_pipeline,
        "John lives in Prague.",
    )

    second = build_memory(
        memory_pipeline,
        knowledge_pipeline,
        claim_pipeline,
        evidence_pipeline,
        observation_pipeline,
        "Alice lives in Brno.",
    )

    result = repository.search()

    assert len(result) == 2

    ids = {item["id"] for item in result}

    assert str(first.id) in ids
    assert str(second.id) in ids
