from memoriaos.domain import Memory
from memoriaos.repository import MemoryRepository


class MemoryRetrievalService:
    """
    Retrieves Memory artifacts from the repository.
    """

    def __init__(self, repository: MemoryRepository):
        self._repository = repository

    def retrieve(self) -> list[Memory]:
        return self._repository.search()
