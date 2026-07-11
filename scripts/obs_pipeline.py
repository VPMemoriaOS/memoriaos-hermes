#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
import uuid

from dataclasses import dataclass
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


# ---------------------------------------------------------------------
# Domain model
# ---------------------------------------------------------------------

@dataclass(slots=True)
class CompilationUnit:
    """
    Raw information entering MemoriaOS.
    """

    source: str
    text: str


@dataclass(slots=True)
class Observation:
    """
    Canonical Observation produced from a Compilation Unit.
    """

    id: uuid.UUID
    created: datetime
    source: str
    text: str


# ---------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------

def log(message: str) -> None:
    print(f"[{PIPELINE_NAME}] {message}")


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------

def parse_arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="MemoriaOS Observation Pipeline"
    )

    parser.add_argument(
        "--source",
        required=True,
        choices=SUPPORTED_SOURCES,
        help="Observation source.",
    )

    parser.add_argument(
        "--text",
        required=True,
        help="Observation text.",
    )

    return parser.parse_args()


# ---------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------

def build_compilation_unit(args: argparse.Namespace) -> CompilationUnit:

    return CompilationUnit(
        source=args.source,
        text=args.text,
    )


def validate(unit: CompilationUnit) -> None:

    if not unit.text.strip():
        raise ValueError("Observation text is empty.")


def canonicalize(unit: CompilationUnit) -> CompilationUnit:

    text = unit.text.strip()

    return CompilationUnit(
        source=unit.source,
        text=text,
    )


def create_observation(unit: CompilationUnit) -> Observation:

    return Observation(
        id=uuid.uuid4(),
        created=datetime.now(UTC),
        source=unit.source,
        text=unit.text,
    )


# ---------------------------------------------------------------------
# Repository
# ---------------------------------------------------------------------

def repository_root() -> Path:

    workspace = Path(__file__).resolve().parents[2]

    repo = workspace / "memoria-repository"

    if not repo.exists():
        raise RuntimeError(
            f"Repository not found: {repo}"
        )

    return repo


def publish(observation: Observation) -> Path:

    observations = repository_root() / "Observations"

    observations.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = observation.created.strftime("%Y%m%d-%H%M%S")

    filename = (
        observations /
        f"{timestamp}-{observation.id}.md"
    )

    content = f"""# Observation

id: {observation.id}

created: {observation.created.isoformat()}

source: {observation.source}

status: raw

---

{observation.text}
"""

    filename.write_text(
        content,
        encoding="utf-8",
    )

    return filename


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> int:

    args = parse_arguments()

    log("Starting pipeline...")

    unit = build_compilation_unit(args)

    validate(unit)

    unit = canonicalize(unit)

    observation = create_observation(unit)

    filename = publish(observation)

    log(f"Source : {observation.source}")
    log(f"Output : {filename}")
    log("Done.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
