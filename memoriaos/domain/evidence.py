from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True, slots=True)
class Evidence:
    """
    Canonical evidence derived from one or more Observations.

    Evidence is immutable and may later support one or more Claims.
    """

    id: str
    content: str
    observation_ids: Tuple[str, ...]
