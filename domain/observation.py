from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from .provenance import Provenance


@dataclass(slots=True, frozen=True)
class Observation:
    """
    Canonical Observation.
    """

    id: UUID

    created: datetime

    provenance: Provenance

    text: str
