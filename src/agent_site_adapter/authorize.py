from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from .model import AuthorityEvidence, RequestContext


@dataclass(frozen=True)
class AuthorizationDecision:
    outcome: str
    reason: str


def _now() -> datetime:
    return datetime.now(timezone.utc)


def authorize(
    request: RequestContext,
    authority: Optional[AuthorityEvidence],
    *,
    now: Optional[datetime] = None,
) -> AuthorizationDecision:
    now = now or _now()

    if authority is None:
        return AuthorizationDecision("DENY", "AUTHORITY_MISSING")

    if authority.revoked:
        return AuthorizationDecision("DENY", "AUTHORITY_REVOKED")

    if not authority.delegation_valid:
        return AuthorizationDecision("DENY", "DELEGATION_INVALID")

    if authority.expires_at <= now:
        return AuthorizationDecision("DENY", "AUTHORITY_EXPIRED")

    if authority.subject != request.subject:
        return AuthorizationDecision("DENY", "AUTHORITY_SUBJECT_MISMATCH")

    if authority.audience != request.service:
        return AuthorizationDecision("DENY", "AUTHORITY_AUDIENCE_MISMATCH")

    if request.action not in authority.actions:
        return AuthorizationDecision("DENY", "AUTHORITY_SCOPE_MISMATCH")

    if request.resource not in authority.resources:
        return AuthorizationDecision("DENY", "AUTHORITY_CONSTRAINT_VIOLATION")

    amount = request.parameters.get("amount")
    currency = request.parameters.get("currency")
    if amount is not None:
        if amount <= 0:
            return AuthorizationDecision("DENY", "AUTHORITY_CONSTRAINT_VIOLATION")
        if authority.max_amount is not None and amount > authority.max_amount:
            return AuthorizationDecision("DENY", "AUTHORITY_CONSTRAINT_VIOLATION")
        if authority.currency is not None and currency != authority.currency:
            return AuthorizationDecision("DENY", "AUTHORITY_CONSTRAINT_VIOLATION")

    if request.consent is not None:
        consent = request.consent
        if consent.expires_at <= now:
            return AuthorizationDecision("DENY", "CONSENT_MISMATCH")
        if (
            consent.subject != request.subject
            or consent.request_id != request.request_id
            or consent.capability != request.capability
            or consent.action != request.action
            or consent.resource != request.resource
        ):
            return AuthorizationDecision("DENY", "CONSENT_MISMATCH")

    if request.requires_human and request.consent is None:
        return AuthorizationDecision("REQUIRE_HUMAN", "CONSENT_REQUIRED")

    return AuthorizationDecision("ALLOW", "AUTHORIZED")
