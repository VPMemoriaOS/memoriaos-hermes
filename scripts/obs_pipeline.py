#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import uuid


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


def write_test_observation():

    repo = repository_root()

    observations = repo / "Observations"

    observations.mkdir(exist_ok=True)

    observation_id = uuid.uuid4()

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    filename = observations / f"{timestamp}-{observation_id}.md"

    filename.write_text(
f"""# Observation

id: {observation_id}

created: {datetime.utcnow().isoformat()}Z

status: test

---

This is the first Observation created by MemoriaOS.
"""
    )

    print(f"Observation written to:")

    print(filename)


if __name__ == "__main__":

    write_test_observation()
