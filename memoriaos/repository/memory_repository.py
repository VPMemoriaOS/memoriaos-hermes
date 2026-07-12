from pathlib import Path

from memoriaos.repository.artifact_repository import ArtifactRepository


class MemoryRepository(ArtifactRepository):
    """
    Repository for Memory artifacts.
    """

    ARTIFACT_DIR = "Memory"

    def search(self) -> list[dict]:
        """
        Return all stored Memory artifacts.

        Results are ordered deterministically by filename.
        """

        result = []

        for path in sorted(self._artifact_dir.glob("*.json")):
            result.append(self.load(path.stem))

        return result
