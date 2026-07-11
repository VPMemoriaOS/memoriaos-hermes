from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True, slots=True)
class Claim:
    """
    Canonical semantic statement.

    A Claim is immutable and is always traceable to one or more Evidence
    artifacts.
    """

    id: str
    subject: str
    predicate: str
    object: str
    evidence_ids: Tuple[str, ...]
