from __future__ import annotations

from pathlib import Path


def repository_root() -> Path:
    workspace = Path(__file__).resolve().parents[2]

    repository = workspace / "memoria-repository"

    if not repository.exists():
        raise RuntimeError(
            f"Repository not found: {repository}"
        )

    return repository
