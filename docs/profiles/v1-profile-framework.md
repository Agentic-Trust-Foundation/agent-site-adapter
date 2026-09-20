# Site Adapter V1 — Integration Profile Framework

**Status:** Normative V1  
**Date:** 2026-09-21

## Purpose

This document defines how Site Adapter V1 maps its stable semantic contracts onto concrete interoperability environments without creating a new transport for every ecosystem.

A profile selects:
- transport/binding;
- discovery mechanism;
- authentication mechanism;
- capability representation;
- request/response mapping;
- error mapping;
- lifecycle and idempotency rules;
- applicable security controls.

A profile MUST NOT redefine ATF authority semantics or Agent-Pay financial policy.

## Profile identifiers

| Profile | Identifier | Primary use |
|---|---|---|
| Web HTTP | `site-adapter/web-http/1` | Generic HTTPS APIs/services |
| OAuth HTTP | `site-adapter/oauth-http/1` | OAuth-protected services |
| MCP | `site-adapter/mcp/1` | MCP tool/service integration |
| A2A | `site-adapter/a2a/1` | Agent-to-agent/service-to-service |
| Commerce | `site-adapter/commerce/1` | Commerce journeys |
| Booking | `site-adapter/booking/1` | Reservations and scheduling |
| SaaS/API | `site-adapter/saas-api/1` | SaaS and enterprise APIs |
| Enterprise | `site-adapter/enterprise/1` | Internal/partner enterprise services |
| Healthcare | `site-adapter/healthcare/1` | Healthcare service integration |
| Cloud | `site-adapter/cloud/1` | Infrastructure/cloud operations |
| Agent-Pay | `site-adapter/agent-pay/1` | Financial handoff |

The named ecosystem protocols remain authoritative for their own wire semantics. Site Adapter profiles describe the adapter boundary and required security semantics around them.

## Common profile contract

Every V1 profile MUST identify:
1. Service Entity;
2. protocol/profile version;
3. endpoint/origin;
4. capability and action;
5. authenticated principal;
6. target resource;
7. authority evidence reference;
8. request correlation identifier;
9. idempotency key for non-idempotent operations;
10. consent/approval state where required;
11. result status and evidence reference.

## Security rules

- HTTPS is mandatory for network profiles.
- Authentication MUST be verified before authorization.
- Authorization MUST bind subject, audience/resource, action, target resource and security-sensitive parameters.
- Capability declaration is not authority.
- Discovery is not trust.
- Human approval cannot create missing authority.
- Unknown security-critical profile extensions fail closed.
- Cross-profile downgrade is prohibited.
- Sensitive credentials MUST NOT be copied into discovery metadata.
- Implementations MUST protect against SSRF when dynamically following metadata.

## Version negotiation

The peer selects a mutually supported profile version. A major-version mismatch is incompatible. A minor revision may be accepted only when the profile declares backward-compatible semantics.

Security-sensitive unknown extensions MUST cause rejection rather than silent downgrade.

## Conformance classes

- **Discovery:** metadata and identity binding.
- **Authentication:** principal verification and audience/resource binding.
- **Authorization:** ATF authority enforcement.
- **Execution:** request lifecycle and idempotency.
- **Evidence:** correlation, result and audit references.
- **Financial:** Agent-Pay handoff where applicable.

A profile is conformant only when all mandatory classes for that profile pass.
