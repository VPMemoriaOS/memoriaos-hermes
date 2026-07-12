class HermesReasoningService(ReasoningService):

    def reason(
        self,
        claim: Claim,
        candidate_memories: tuple[Memory, ...],
    ) -> ReasoningResult:
        raise NotImplementedError(
            "Hermes integration is not implemented yet."
        )
