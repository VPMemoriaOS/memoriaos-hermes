from memoriaos.context import MemoryContext
from memoriaos.domain import Claim, Knowledge, Memory
from memoriaos.repository import KnowledgeRepository


class KnowledgePipeline:
    """
    Initial implementation of KNOWLEDGE-PIPELINE-001.

    Creates and stores a Knowledge artifact from a single Claim.
    """

    def __init__(self, repository: KnowledgeRepository):
        self._repository = repository

    def run(
        self,
        claim: Claim,
        context: MemoryContext | None = None,
    ) -> Knowledge:
        candidate_memories = self._collect_candidate_memories(context)

        # Sprint 4 (S4-001):
        # Candidate memories are intentionally not yet used.
        # This stage establishes deterministic memory-aware execution
        # while preserving existing behaviour.
        _ = candidate_memories

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
