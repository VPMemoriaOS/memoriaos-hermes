from memoriaos.domain import Knowledge, Memory
from memoriaos.repository import MemoryRepository


class MemoryPipeline:
    """
    MEMORY-PIPELINE-002

    Creates and stores a Memory artifact from a single Knowledge artifact.
    """

    def __init__(self, repository: MemoryRepository):
        self._repository = repository

    def run(self, knowledge: Knowledge) -> Memory:
        memory = Memory.from_knowledge(knowledge)
        self._repository.save(memory)
        return memory
