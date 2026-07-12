#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys

from pathlib import Path

from memoriaos.domain import CompilationUnit
from memoriaos.pipelines.observation_pipeline import ObservationPipeline
from memoriaos.repository import ObservationRepository

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


def repository_root() -> Path:
    workspace = Path(__file__).resolve().parents[2]

    repository = workspace / "memoria-repository"

    if not repository.exists():
        raise RuntimeError(
            f"Repository not found: {repository}"
        )

    return repository


def main() -> int:
    args = parse_arguments()

    log("Starting pipeline...")

    unit = CompilationUnit(
        source=args.source,
        source_id=args.source_id,
        text=args.text,
    )

    repository = ObservationRepository(
        repository_root()
    )

    pipeline = ObservationPipeline(repository)

    observation = pipeline.run(unit)

    log(f"Source : {observation.provenance.source_type}")
    log(f"Source ID : {observation.provenance.source_identifier}")
    log(f"Observation : {observation.id}")
    log("Done.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
