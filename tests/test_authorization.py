from datetime import datetime, timedelta, timezone

from agent_site_adapter import (
    AuthorityEvidence,
    ConsentEvidence,
    RequestContext,
    authorize,
)

NOW = datetime(2030, 1, 1, tzinfo=timezone.utc)


def authority(**overrides):
    values = dict(
        subject="agent-1",
        audience="https://service.example",
        actions=frozenset({"order.create"}),
        resources=frozenset({"merchant-1"}),
        expires_at=NOW + timedelta(hours=1),
    )
    values.update(overrides)
    return AuthorityEvidence(**values)


def request(**overrides):
    values = dict(
        request_id="req-1",
        subject="agent-1",
        service="https://service.example",
        capability="order",
        action="order.create",
        resource="merchant-1",
    )
    values.update(overrides)
    return RequestContext(**values)


def test_allow_valid_request():
    assert authorize(request(), authority(), now=NOW).outcome == "ALLOW"


def test_missing_authority_fails_closed():
    d = authorize(request(), None, now=NOW)
    assert (d.outcome, d.reason) == ("DENY", "AUTHORITY_MISSING")


def test_wrong_subject_denied():
    d = authorize(request(), authority(subject="agent-2"), now=NOW)
    assert d.reason == "AUTHORITY_SUBJECT_MISMATCH"


def test_wrong_audience_denied():
    d = authorize(request(), authority(audience="https://other.example"), now=NOW)
    assert d.reason == "AUTHORITY_AUDIENCE_MISMATCH"


def test_wrong_action_denied():
    d = authorize(request(), authority(actions=frozenset({"order.cancel"})), now=NOW)
    assert d.reason == "AUTHORITY_SCOPE_MISMATCH"


def test_wrong_resource_denied():
    d = authorize(request(), authority(resources=frozenset({"merchant-2"})), now=NOW)
    assert d.reason == "AUTHORITY_CONSTRAINT_VIOLATION"


def test_expired_authority_denied():
    d = authorize(request(), authority(expires_at=NOW), now=NOW)
    assert d.reason == "AUTHORITY_EXPIRED"


def test_revoked_authority_denied():
    d = authorize(request(), authority(revoked=True), now=NOW)
    assert d.reason == "AUTHORITY_REVOKED"


def test_invalid_delegation_denied():
    d = authorize(request(), authority(delegation_valid=False), now=NOW)
    assert d.reason == "DELEGATION_INVALID"


def test_amount_limit_is_enforced():
    r = request(parameters={"amount": 101, "currency": "USD"})
    d = authorize(r, authority(max_amount=100, currency="USD"), now=NOW)
    assert d.reason == "AUTHORITY_CONSTRAINT_VIOLATION"


def test_currency_is_bound():
    r = request(parameters={"amount": 10, "currency": "EUR"})
    d = authorize(r, authority(max_amount=100, currency="USD"), now=NOW)
    assert d.reason == "AUTHORITY_CONSTRAINT_VIOLATION"


def test_human_approval_does_not_create_authority():
    r = request(requires_human=True)
    d = authorize(r, None, now=NOW)
    assert d.outcome == "DENY"
    assert d.reason == "AUTHORITY_MISSING"


def test_human_approval_required_with_existing_authority():
    r = request(requires_human=True)
    d = authorize(r, authority(), now=NOW)
    assert (d.outcome, d.reason) == ("REQUIRE_HUMAN", "CONSENT_REQUIRED")


def test_bound_consent_allows_request():
    consent = ConsentEvidence(
        subject="agent-1",
        request_id="req-1",
        capability="order",
        action="order.create",
        resource="merchant-1",
        approved_at=NOW,
        expires_at=NOW + timedelta(minutes=5),
    )
    r = request(requires_human=True, consent=consent)
    d = authorize(r, authority(), now=NOW)
    assert d.outcome == "ALLOW"


def test_consent_substitution_is_denied():
    consent = ConsentEvidence(
        subject="agent-1",
        request_id="req-other",
        capability="order",
        action="order.create",
        resource="merchant-1",
        approved_at=NOW,
        expires_at=NOW + timedelta(minutes=5),
    )
    r = request(requires_human=True, consent=consent)
    d = authorize(r, authority(), now=NOW)
    assert d.reason == "CONSENT_MISMATCH"


def test_consent_cannot_bypass_missing_authority():
    consent = ConsentEvidence(
        subject="agent-1",
        request_id="req-1",
        capability="order",
        action="order.create",
        resource="merchant-1",
        approved_at=NOW,
        expires_at=NOW + timedelta(minutes=5),
    )
    r = request(requires_human=True, consent=consent)
    d = authorize(r, None, now=NOW)
    assert d.reason == "AUTHORITY_MISSING"
