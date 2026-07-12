from __future__ import annotations

from uuid import UUID

from memoriaos.domain import Claim


class ClaimHydrator:
    """
    Hydrates Claim domain objects from persisted JSON documents.
    """

    def hydrate(self, document: dict) -> Claim:
        return Claim(
            id=UUID(document["id"]),
            subject=document["subject"],
            predicate=document["predicate"],
            object=document["object"],
            evidence_ids=tuple(
                UUID(value)
                for value in document["evidence_ids"]
            ),
        )
