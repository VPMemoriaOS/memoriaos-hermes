#!/usr/bin/env python3
from pathlib import Path

from memoriaos.domain.observation import Observation
from memoriaos.pipelines import EvidencePipeline
from memoriaos.repository import EvidenceRepository


def main() -> None:
    # Temporary manual example until ObservationRepository integration.
    observation = Observation(
        id="demo-observation",
        text="John lives in Prague.",
        provenance=None,  # TODO: replace with real Observation loading
    )

    repository = EvidenceRepository(Path("../memoria-repository"))
    pipeline = EvidencePipeline(repository)

    evidence = pipeline.run(observation)

    print(f"Evidence created: {evidence.id}")


if __name__ == "__main__":
    main()
