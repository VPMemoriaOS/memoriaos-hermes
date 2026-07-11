from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class Provenance:
    """
    Describes where an Observation originated.
    """

    source_type: str

    source_identifier: str

    captured_at: datetime

    captured_by: str
