from __future__ import annotations

from pathlib import Path

from memoriaos.domain import Observation


class ObservationRepository:
    """
    Repository responsible for storing Observations.
    """

    def __init__(self, repository_root: Path):

        self.repository_root = repository_root

        self.observations = (
            repository_root /
            "Observations"
        )

        self.observations.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        observation: Observation,
    ) -> Path:

        timestamp = observation.created.strftime(
            "%Y%m%d-%H%M%S"
        )

        filename = (
            self.observations /
            f"{timestamp}-{observation.id}.md"
        )

        content = f"""# Observation

id: {observation.id}

created: {observation.created.isoformat()}

source: {observation.provenance.source_type}

source_identifier: {observation.provenance.source_identifier}

captured_at: {observation.provenance.captured_at.isoformat()}

captured_by: {observation.provenance.captured_by}

status: raw

---

{observation.text}
"""

        filename.write_text(
            content,
            encoding="utf-8",
        )

        return filename
