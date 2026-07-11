from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CompilationUnit:
    """
    Raw information entering MemoriaOS.
    """

    source: str
    source_id: str
    text: str
