from datetime import datetime, timedelta, timezone

from agent_site_adapter import AuthorityEvidence, RequestContext, authorize
from agent_site_adapter.agent_pay import build_agent_pay_handoff

NOW = datetime(2030, 1, 1, tzinfo=timezone.utc)


def test_authorized_financial_request_produces_bounded_handoff():
    request = RequestContext(
        request_id="req-pay-1",
        subject="agent-1",
        service="https://merchant.example",
        capability="commerce.checkout",
        action="purchase.create",
        resource="order-123",
        parameters={"amount": 250000, "currency": "IRR"},
    )
    authority = AuthorityEvidence(
        subject="agent-1",
        audience="https://merchant.example",
        actions=frozenset({"purchase.create"}),
        resources=frozenset({"order-123"}),
        expires_at=NOW + timedelta(minutes=10),
        max_amount=250000,
        currency="IRR",
    )

    decision = authorize(request, authority, now=NOW)
    handoff = build_agent_pay_handoff(
        request, decision, idempotency_key="idem-req-pay-1"
    )

    assert handoff.authorization_outcome == "ALLOW"
    assert handoff.amount == 250000
    assert handoff.currency == "IRR"
    assert len(handoff.authorization_context_hash) == 64


def test_denied_request_cannot_reach_payment():
    request = RequestContext(
        request_id="req-pay-2",
        subject="agent-1",
        service="https://merchant.example",
        capability="commerce.checkout",
        action="purchase.create",
        resource="order-123",
        parameters={"amount": 250000, "currency": "IRR"},
    )
    decision = authorize(request, None, now=NOW)

    try:
        build_agent_pay_handoff(request, decision, idempotency_key="idem")
    except ValueError as exc:
        assert "ALLOW" in str(exc)
    else:
        raise AssertionError("denied request reached payment handoff")
