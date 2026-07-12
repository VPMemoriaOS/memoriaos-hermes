class MockReasoningService(ReasoningService):

    def reason(
        self,
        claim: Claim,
        candidate_memories: tuple[Memory, ...],
    ) -> ReasoningResult:

        return ReasoningResult(
            decision="NEW",
            confidence=1.0,
            explanation="Mock reasoning.",
            related_memory_ids=(),
        )
