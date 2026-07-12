from __future__ import annotations

from typing import Any

from memoriaos.hydration.claim_hydrator import ClaimHydrator
from memoriaos.hydration.knowledge_hydrator import KnowledgeHydrator
from memoriaos.hydration.memory_hydrator import MemoryHydrator


class ArtifactHydrator:
    """
    Base infrastructure for artifact hydration.
    """

    def __init__(self) -> None:
        self._claim_hydrator = ClaimHydrator()
        self._knowledge_hydrator = KnowledgeHydrator()
        self._memory_hydrator = MemoryHydrator()

    def hydrate_claim(self, document: dict[str, Any]):
        return self._claim_hydrator.hydrate(document)

    def hydrate_knowledge(self, document: dict[str, Any]):
        return self._knowledge_hydrator.hydrate(document)

    def hydrate_memory(self, document: dict[str, Any]):
        return self._memory_hydrator.hydrate(document)
