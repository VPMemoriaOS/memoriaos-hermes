#!/usr/bin/env python3

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import uuid


PIPELINE_NAME = "OBS-PIPELINE-001"


def log(message: str) -> None:
    print(f"[{PIPELINE_NAME}] {message}")


def repository_root() -> Path:
    """
    Locate memoria-repository next to memoriaos-hermes.
    """

    current = Path(__file__).resolve()

    workspace = current.parents[2]

    repo = workspace / "memoria-repository"

    if not repo.exists():
        raise RuntimeError(f"Repository not found: {repo}")

    return repo


def create_observation_file() -> Path:

    repo = repository_root()

    observations = repo / "Observations"

    observations.mkdir(parents=True, exist_ok=True)

    observation_id = uuid.uuid4()

    now = datetime.now(UTC)

    timestamp = now.strftime("%Y%m%d-%H%M%S")

    filename = observations / f"{timestamp}-{observation_id}.md"

    content = f"""# Observation

id: {observation_id}

created: {now.isoformat()}

status: test

---

This is the first Observation created by MemoriaOS.
"""

    filename.write_text(content, encoding="utf-8")

    return filename


def main() -> int:

    log("Starting pipeline...")

    file = create_observation_file()

    log(f"Observation written:")

    log(str(file))

    log("Done.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
