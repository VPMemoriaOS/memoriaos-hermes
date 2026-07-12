from memoriaos.context import MemoryContext
from memoriaos.domain import Claim, Knowledge, Memory
from memoriaos.repository import KnowledgeRepository
from memoriaos.reasoning import ReasoningService

class KnowledgePipeline:
    """
    Initial implementation of KNOWLEDGE-PIPELINE-001.

    Creates and stores a Knowledge artifact from a single Claim.
    """

    def __init__(
        self,
        repository: KnowledgeRepository,
        reasoning_service: ReasoningService,
    ):
        self._repository = repository
        self._reasoning_service = reasoning_service

    def run(
        self,
        claim: Claim,
        context: MemoryContext | None = None,
    ) -> Knowledge:
        candidate_memories = self._collect_candidate_memories(context)

        reasoning_result = self._reasoning_service.reason(
            claim,
            candidate_memories,
        )

        # Sprint 4 (S4-005):
        # The reasoning result is intentionally not yet used.
        # Future Sprint 4 steps will incorporate it into
        # knowledge construction.
        _ = reasoning_result

        knowledge = Knowledge.from_claim(claim)

        self._repository.save(knowledge)

        return knowledge

    def _collect_candidate_memories(
        self,
        context: MemoryContext | None,
    ) -> tuple[Memory, ...]:
        """
        Collect candidate memories from the processing context.

        The returned memories are read-only and deterministic.
        Future Sprint 4 steps will use this collection during
        knowledge construction.
        """
        if context is None:
            return ()

        return tuple(context.memories)
