from __future__ import annotations

from typing import Any


class ArtifactHydrator:
    """
    Base infrastructure for artifact hydration.

    Concrete implementations will progressively support individual
    domain artifacts.
    """

    def hydrate(self, document: dict[str, Any]) -> Any:
        raise NotImplementedError
