from __future__ import annotations

from memoriaos.context import MemoryContext
from memoriaos.services import MemoryRetrievalService


class MemoryContextService:
    """
    Builds a MemoryContext from retrieved Memory artifacts.
    """

    def __init__(self, retrieval_service: MemoryRetrievalService):
        self._retrieval_service = retrieval_service

    def build(self) -> MemoryContext:
        memories = tuple(self._retrieval_service.retrieve())
        return MemoryContext(memories=memories)
