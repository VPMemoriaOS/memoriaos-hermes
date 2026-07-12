from abc import ABC, abstractmethod

from memoriaos.domain import Claim, Memory


class ReasoningService(ABC):

    @abstractmethod
    def reason(
        self,
        claim: Claim,
        candidate_memories: tuple[Memory, ...],
    ):
        """
        Analyse the relationship between a new claim and
        existing memories.
        """
