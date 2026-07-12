from memoriaos.hydration import MemoryHydrator
from memoriaos.repository.artifact_repository import ArtifactRepository


class MemoryRepository(ArtifactRepository):
    """
    Repository for Memory artifacts.
    """

    ARTIFACT_DIR = "Memory"

    def __init__(self, repository_root):
        super().__init__(repository_root)
        self._hydrator = MemoryHydrator()

    def load(self, artifact_id: str):
        document = super().load(artifact_id)
        return self._hydrator.hydrate(document)

    def search(self):
        result = []

        for path in sorted(self._artifact_dir.glob("*.json")):
            result.append(self.load(path.stem))

        return result
