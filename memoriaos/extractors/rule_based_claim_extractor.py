from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ClaimParts:
    subject: str
    predicate: str
    object: str


class RuleBasedClaimExtractor:
    """
    Very small MVP extractor.

    Currently understands only sentences of the form:

        "<subject> lives in <object>"
    """

    def extract(self, text: str) -> ClaimParts:
        text = text.strip().rstrip(".")

        marker = " lives in "

        if marker not in text:
            raise ValueError(
                "Unsupported sentence. "
                "Expected format: '<subject> lives in <object>'."
            )

        subject, obj = text.split(marker, maxsplit=1)

        return ClaimParts(
            subject=subject.strip(),
            predicate="lives_in",
            object=obj.strip(),
        )
