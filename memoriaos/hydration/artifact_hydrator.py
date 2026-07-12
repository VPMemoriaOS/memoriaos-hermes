from __future__ import annotations

from typing import Any

from memoriaos.hydration.claim_hydrator import ClaimHydrator


class ArtifactHydrator:
    """
    Base infrastructure for artifact hydration.

    Concrete artifact support is progressively added.
    """

    def __init__(self) -> None:
        self._claim_hydrator = ClaimHydrator()

    def hydrate_claim(self, document: dict[str, Any]):
        return self._claim_hydrator.hydrate(document)
