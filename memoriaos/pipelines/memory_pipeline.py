from memoriaos.domain import Knowledge, Memory


class MemoryPipeline:
    """
    Initial implementation of MEMORY-PIPELINE-001.

    Creates a Memory artifact from a single Knowledge artifact.
    """

    def run(self, knowledge: Knowledge) -> Memory:
        return Memory.from_knowledge(knowledge)
