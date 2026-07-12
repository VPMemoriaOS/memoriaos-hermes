from dataclasses import dataclass


@dataclass(frozen=True)
class ReasoningResult:
    """
    Structured output produced by a ReasoningService.
    """

    decision: str
    confidence: float
    explanation: str
    related_memory_ids: tuple[str, ...]
