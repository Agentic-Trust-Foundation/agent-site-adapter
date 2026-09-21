# Site Adapter V1 Conformance

**Status:** V1 FINAL — semantic and profile conformance baseline  
**Date:** 2026-09-21

## Purpose

The V1 conformance suite verifies the stable Site Adapter semantic contract and the required behavior of its integration profiles.

The suite is intentionally layered:

1. semantic authorization conformance;
2. profile-boundary conformance;
3. Agent-Pay handoff conformance where applicable.

It does not replace the native wire specifications of OAuth, MCP, A2A, UCP, or payment protocols.

## Required semantic assertions

| Area | Required behavior |
|---|---|
| Authority presence | Missing authority fails closed |
| Subject | Agent/principal mismatch is denied |
| Audience | Cross-service authority is denied |
| Action | Capability/action mismatch is denied |
| Resource | Unauthorized resource is denied |
| Delegation | Invalid delegation is denied |
| Expiry/revocation | Stale or revoked authority is denied |
| Parameters | Amount/currency constraints are enforced |
| Consent | Consent is bound to request material |
| Human approval | Approval cannot manufacture authority |
| Human approval | Existing authority may produce REQUIRE_HUMAN |
| Replay/substitution | Mismatched consent is denied |
| Agent-Pay boundary | Downstream controls cannot expand upstream authority |
| Fail closed | Indeterminate required security evidence is not ALLOW |

## V1 implementation coverage

The reference implementation provides deterministic semantic authorization tests covering positive and negative cases, including subject, audience, action, resource, delegation, expiry/revocation, parameter, consent, approval and fail-closed behavior.

The V1 profile framework defines these profile identifiers:

- `site-adapter/web-http/1`
- `site-adapter/oauth-http/1`
- `site-adapter/mcp/1`
- `site-adapter/a2a/1`
- `site-adapter/commerce/1`
- `site-adapter/booking/1`
- `site-adapter/saas-api/1`
- `site-adapter/enterprise/1`
- `site-adapter/healthcare/1`
- `site-adapter/cloud/1`
- `site-adapter/agent-pay/1`

Profile conformance requires the common identity, authentication, authorization, execution, evidence and applicable financial classes defined by `docs/profiles/v1-profile-framework.md`.

## Agent-Pay handoff

The Agent-Pay profile requires bounded authority evidence and request binding. Financial parameters may be restricted downstream but may not expand upstream authority.

## Conformance boundary

V1 conformance establishes semantic/profile compatibility. It is not a production certification, live-provider certification, or proof that an integrated service is trustworthy.

Production deployments still require concrete credential verification, key management, revocation/lifecycle enforcement, transport hardening, abuse controls, privacy controls and deployment-specific security review.

## Change control

V1 semantic changes require an explicit versioned decision. Additional profile coverage, tests and documentation may be added without changing the frozen V1 meaning.
