from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any


class ArtifactRepository:
    """
    Base repository for persisting immutable artifacts as JSON documents.
    """

    ARTIFACT_DIR: str = ""

    def __init__(self, repository_root: Path):
        if not self.ARTIFACT_DIR:
            raise ValueError("ARTIFACT_DIR must be defined")

        self._artifact_dir = repository_root / self.ARTIFACT_DIR
        self._artifact_dir.mkdir(parents=True, exist_ok=True)

    def save(self, artifact: Any) -> Path:
        path = self._artifact_dir / f"{artifact.id}.json"

        with path.open("w", encoding="utf-8") as f:
            json.dump(asdict(artifact), f, indent=2, ensure_ascii=False)

        return path
