from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .knowledge import Knowledge


@dataclass(frozen=True)
class Memory:
    """
    Stable long-term semantic state created from one or more Knowledge artifacts.
    """

    id: UUID = field(default_factory=uuid4)
    knowledge: tuple[Knowledge, ...] = field(default_factory=tuple)

    @classmethod
    def from_knowledge(cls, knowledge: Knowledge) -> "Memory":
        return cls(knowledge=(knowledge,))
