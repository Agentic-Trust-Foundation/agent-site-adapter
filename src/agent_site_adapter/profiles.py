from dataclasses import dataclass
from typing import FrozenSet


V1_PROFILE_WEB_HTTP = "site-adapter/web-http/1"
V1_PROFILE_OAUTH_HTTP = "site-adapter/oauth-http/1"
V1_PROFILE_MCP = "site-adapter/mcp/1"
V1_PROFILE_A2A = "site-adapter/a2a/1"
V1_PROFILE_COMMERCE = "site-adapter/commerce/1"
V1_PROFILE_BOOKING = "site-adapter/booking/1"
V1_PROFILE_SAAS_API = "site-adapter/saas-api/1"
V1_PROFILE_ENTERPRISE = "site-adapter/enterprise/1"
V1_PROFILE_HEALTHCARE = "site-adapter/healthcare/1"
V1_PROFILE_CLOUD = "site-adapter/cloud/1"
V1_PROFILE_AGENT_PAY = "site-adapter/agent-pay/1"


@dataclass(frozen=True)
class ProfileRequirements:
    profile_id: str
    requires_https: bool = True
    requires_request_id: bool = True
    requires_idempotency_for_mutation: bool = True
    requires_authority_evidence: bool = True
    requires_audience_binding: bool = True
    requires_fail_closed: bool = True


@dataclass(frozen=True)
class ProfileSelection:
    protocol_version: str
    profile: str
    capabilities: FrozenSet[str]

    def compatible_with(self, supported_profiles: FrozenSet[str], supported_capabilities: FrozenSet[str]) -> bool:
        return (
            self.profile in supported_profiles
            and self.capabilities.issubset(supported_capabilities)
        )


V1_PROFILES = frozenset({
    V1_PROFILE_WEB_HTTP,
    V1_PROFILE_OAUTH_HTTP,
    V1_PROFILE_MCP,
    V1_PROFILE_A2A,
    V1_PROFILE_COMMERCE,
    V1_PROFILE_BOOKING,
    V1_PROFILE_SAAS_API,
    V1_PROFILE_ENTERPRISE,
    V1_PROFILE_HEALTHCARE,
    V1_PROFILE_CLOUD,
    V1_PROFILE_AGENT_PAY,
})


def requirements_for(profile: str) -> ProfileRequirements:
    if profile not in V1_PROFILES:
        raise ValueError(f"unsupported profile: {profile}")
    return ProfileRequirements(profile_id=profile)
