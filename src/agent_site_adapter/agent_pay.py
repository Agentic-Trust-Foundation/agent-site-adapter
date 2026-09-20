"""Reference Agent-Pay handoff for Site Adapter V1.

This module does not perform payment execution. It produces a bounded,
hash-linked handoff after Site Adapter authorization succeeds.
"""
from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any, Mapping

from .authorize import AuthorizationDecision
from .model import RequestContext


@dataclass(frozen=True)
class AgentPayHandoff:
    request_id: str
    subject: str
    service: str
    action: str
    resource: str
    amount: int
    currency: str
    authorization_outcome: str
    authorization_context_hash: str
    idempotency_key: str


def build_agent_pay_handoff(
    request: RequestContext,
    decision: AuthorizationDecision,
    *,
    idempotency_key: str,
) -> AgentPayHandoff:
    """Build a financial handoff only from an ALLOW decision."""
    if decision.outcome != "ALLOW":
        raise ValueError("financial handoff requires ALLOW")

    amount = request.parameters.get("amount")
    currency = request.parameters.get("currency")
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("financial handoff requires a positive integer amount")
    if not isinstance(currency, str) or not currency:
        raise ValueError("financial handoff requires currency")

    canonical = {
        "request_id": request.request_id,
        "subject": request.subject,
        "service": request.service,
        "action": request.action,
        "resource": request.resource,
        "amount": amount,
        "currency": currency,
        "outcome": decision.outcome,
    }
    digest = sha256(
        json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    return AgentPayHandoff(
        request_id=request.request_id,
        subject=request.subject,
        service=request.service,
        action=request.action,
        resource=request.resource,
        amount=amount,
        currency=currency,
        authorization_outcome=decision.outcome,
        authorization_context_hash=digest,
        idempotency_key=idempotency_key,
    )
