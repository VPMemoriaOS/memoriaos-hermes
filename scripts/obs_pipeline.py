#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
import uuid

from datetime import UTC, datetime
from pathlib import Path


PIPELINE_NAME = "OBS-PIPELINE-001"

SUPPORTED_SOURCES = (
    "manual",
    "telegram",
    "email",
    "webhook",
    "cron",
    "api",
)


def log(message: str) -> None:
    print(f"[{PIPELINE_NAME}] {message}")


def parse_arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="MemoriaOS Observation Pipeline"
    )

    parser.add_argument(
        "--source",
        required=True,
        choices=SUPPORTED_SOURCES,
        help="Origin of the observation.",
    )

    parser.add_argument(
        "--text",
        required=True,
        help="Observation text.",
    )

    return parser.parse_args()


def repository_root() -> Path:

    current = Path(__file__).resolve()

    workspace = current.parents[2]

    repo = workspace / "memoria-repository"

    if not repo.exists():
        raise RuntimeError(
            f"Repository not found: {repo}"
        )

    return repo


def build_filename() -> tuple[str, uuid.UUID]:

    observation_id = uuid.uuid4()

    now = datetime.now(UTC)

    timestamp = now.strftime("%Y%m%d-%H%M%S")

    filename = f"{timestamp}-{observation_id}.md"

    return filename, observation_id


def write_observation(
    source: str,
    text: str,
) -> Path:

    repo = repository_root()

    observations = repo / "Observations"

    observations.mkdir(
        parents=True,
        exist_ok=True,
    )

    filename, observation_id = build_filename()

    now = datetime.now(UTC)

    target = observations / filename

    content = f"""# Observation

id: {observation_id}

created: {now.isoformat()}

source: {source}

status: raw

---

{text}
"""

    target.write_text(
        content,
        encoding="utf-8",
    )

    return target


def main() -> int:

    args = parse_arguments()

    log("Starting pipeline...")

    file = write_observation(
        source=args.source,
        text=args.text,
    )

    log(f"Source : {args.source}")
    log(f"Output : {file}")

    log("Done.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
