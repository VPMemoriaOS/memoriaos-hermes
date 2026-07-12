from uuid import uuid4

from memoriaos.domain import Claim
from memoriaos.hydration import ClaimHydrator


def test_claim_hydration():
    claim_id = uuid4()
    evidence_id = uuid4()

    document = {
        "id": str(claim_id),
        "subject": "John",
        "predicate": "lives_in",
        "object": "Prague",
        "evidence_ids": [
            str(evidence_id),
        ],
    }

    claim = ClaimHydrator().hydrate(document)

    assert isinstance(claim, Claim)

    assert claim.id == claim_id
    assert claim.subject == "John"
    assert claim.predicate == "lives_in"
    assert claim.object == "Prague"
    assert claim.evidence_ids == (evidence_id,)
