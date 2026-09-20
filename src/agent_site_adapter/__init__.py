"""Reference implementation for Agent Site Adapter V1."""

from .agent_pay import AgentPayHandoff, build_agent_pay_handoff
from .authorize import AuthorizationDecision, authorize
from .manifest import ServiceManifest
from .model import AuthorityEvidence, ConsentEvidence, RequestContext
from .profiles import (
    V1_PROFILES,
    ProfileRequirements,
    ProfileSelection,
    requirements_for,
)

__all__ = [
    "AuthorityEvidence",
    "ConsentEvidence",
    "RequestContext",
    "AuthorizationDecision",
    "AgentPayHandoff",
    "ServiceManifest",
    "ProfileRequirements",
    "ProfileSelection",
    "V1_PROFILES",
    "authorize",
    "build_agent_pay_handoff",
    "requirements_for",
]
