from __future__ import annotations

from uuid import UUID

from memoriaos.domain import Knowledge
from memoriaos.hydration.claim_hydrator import ClaimHydrator


class KnowledgeHydrator:
    """
    Hydrates Knowledge domain objects from persisted JSON documents.
    """

    def __init__(self) -> None:
        self._claim_hydrator = ClaimHydrator()

    def hydrate(self, document: dict) -> Knowledge:
        return Knowledge(
            id=UUID(document["id"]),
            claims=tuple(
                self._claim_hydrator.hydrate(claim)
                for claim in document["claims"]
            ),
        )
