from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, FrozenSet, Mapping, Optional


@dataclass(frozen=True)
class AuthorityEvidence:
    subject: str
    audience: str
    actions: FrozenSet[str]
    resources: FrozenSet[str]
    expires_at: datetime
    max_amount: Optional[float] = None
    currency: Optional[str] = None
    revoked: bool = False
    delegation_valid: bool = True


@dataclass(frozen=True)
class ConsentEvidence:
    subject: str
    request_id: str
    capability: str
    action: str
    resource: str
    approved_at: datetime
    expires_at: datetime


@dataclass(frozen=True)
class RequestContext:
    request_id: str
    subject: str
    service: str
    capability: str
    action: str
    resource: str
    parameters: Mapping[str, Any] = field(default_factory=dict)
    requires_human: bool = False
    consent: Optional[ConsentEvidence] = None
