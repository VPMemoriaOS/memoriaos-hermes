from memoriaos.domain import Claim, Knowledge


class KnowledgePipeline:
    """
    Initial implementation of KNOWLEDGE-PIPELINE-001.

    Creates a Knowledge artifact from a single Claim.
    """

    def run(self, claim: Claim) -> Knowledge:
        return Knowledge.from_claim(claim)
