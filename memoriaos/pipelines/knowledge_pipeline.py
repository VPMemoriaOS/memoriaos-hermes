from memoriaos.domain import Claim, Knowledge
from memoriaos.repository import KnowledgeRepository


class KnowledgePipeline:
    """
    Initial implementation of KNOWLEDGE-PIPELINE-001.

    Creates and stores a Knowledge artifact from a single Claim.
    """

    def __init__(self, repository: KnowledgeRepository):
        self._repository = repository

    def run(self, claim: Claim) -> Knowledge:
        knowledge = Knowledge.from_claim(claim)
        self._repository.save(knowledge)
        return knowledge
