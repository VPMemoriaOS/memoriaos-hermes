#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
import uuid

from datetime import UTC, datetime
from pathlib import Path

from memoriaos.domain import (
    CompilationUnit,
    Observation,
    Provenance,
)

from memoriaos.repository import (
    ObservationRepository,
)

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
        "--source-id",
        required=True,
        help="Unique identifier of the original source.",
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
        source_id=args.source_id,
        text=args.text,
    )


def validate(unit: CompilationUnit) -> None:

    if not unit.text.strip():
        raise ValueError("Observation text is empty.")

    if not unit.source_id.strip():
        raise ValueError("Source identifier is empty.")


def canonicalize(unit: CompilationUnit) -> CompilationUnit:

    return CompilationUnit(
        source=unit.source,
        source_id=unit.source_id.strip(),
        text=unit.text.strip(),
    )


def create_observation(unit: CompilationUnit) -> Observation:

    now = datetime.now(UTC)

    provenance = Provenance(
        source_type=unit.source,
        source_identifier=unit.source_id,
        captured_at=now,
        captured_by=PIPELINE_NAME,
    )

    return Observation(
        id=uuid.uuid4(),
        created=now,
        provenance=provenance,
        text=unit.text,
    )


# ---------------------------------------------------------------------
# Repository
# ---------------------------------------------------------------------

def repository_root() -> Path:

    workspace = Path(__file__).resolve().parents[2]

    repository = workspace / "memoria-repository"

    if not repository.exists():
        raise RuntimeError(
            f"Repository not found: {repository}"
        )

    return repository


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

    repository = ObservationRepository(
        repository_root()
    )

    filename = repository.save(
        observation
    )

    log(f"Source : {observation.provenance.source_type}")
    log(f"Source ID : {observation.provenance.source_identifier}")
    log(f"Output : {filename}")
    log("Done.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
