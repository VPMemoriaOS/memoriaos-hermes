from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(slots=True, frozen=True)
class CompilationUnit:
    """
    Raw information entering MemoriaOS.
    """

    id: UUID = field(default_factory=uuid4)

    source: str = ""
    source_id: str = ""
    text: str = ""
