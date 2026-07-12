from abc import ABC, abstractmethod

from memoriaos.domain import Claim, Memory

from .reasoning_result import ReasoningResult


class ReasoningService(ABC):
    """
    Abstract interface for semantic reasoning over newly produced knowledge.

    A reasoning service analyses the relationship between a newly generated
    Claim and previously retrieved Memory artifacts.

    Implementations may use Hermes or any other compatible reasoning engine.
    """

    @abstractmethod
    def reason(
        self,
        claim: Claim,
        candidate_memories: tuple[Memory, ...],
    ) -> ReasoningResult:
        """
        Analyse the relationship between a new claim and existing memories.

        Parameters
        ----------
        claim
            Newly generated claim.

        candidate_memories
            Relevant memories retrieved from the memory repository.

        Returns
        -------
        ReasoningResult
            Structured reasoning outcome.
        """
        raise NotImplementedError
