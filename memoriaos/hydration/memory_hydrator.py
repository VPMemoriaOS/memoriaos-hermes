from __future__ import annotations

from uuid import UUID

from memoriaos.domain import Memory
from memoriaos.hydration.knowledge_hydrator import KnowledgeHydrator


class MemoryHydrator:
    """
    Hydrates Memory domain objects from persisted JSON documents.
    """

    def __init__(self) -> None:
        self._knowledge_hydrator = KnowledgeHydrator()

    def hydrate(self, document: dict) -> Memory:
        return Memory(
            id=UUID(document["id"]),
            knowledge=tuple(
                self._knowledge_hydrator.hydrate(item)
                for item in document["knowledge"]
            ),
        )
