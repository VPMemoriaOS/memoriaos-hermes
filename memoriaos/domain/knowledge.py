from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .claim import Claim


@dataclass(frozen=True)
class Knowledge:
    """
    Stable collection of one or more Claims.

    The evaluation of claim sufficiency is intentionally outside the
    scope of the initial Knowledge pipeline.
    """

    id: UUID = field(default_factory=uuid4)
    claims: tuple[Claim, ...] = field(default_factory=tuple)

    @classmethod
    def from_claim(cls, claim: Claim) -> "Knowledge":
        return cls(claims=(claim,))
