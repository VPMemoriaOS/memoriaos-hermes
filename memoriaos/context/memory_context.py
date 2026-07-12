from __future__ import annotations

from dataclasses import dataclass

from memoriaos.domain import Memory


@dataclass(frozen=True, slots=True)
class MemoryContext:
    """
    Immutable processing context containing retrieved memories.
    """

    memories: tuple[Memory, ...]
