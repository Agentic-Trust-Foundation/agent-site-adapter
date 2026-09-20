# Site Adapter Threat Model

**Status:** Phase 2 architecture contract  
**Date:** 2026-09-21

## Scope

This threat model covers discovery, identity, capability selection, authenticated requests, authorization, consent, execution, and evidence at the Site Adapter boundary. It does not freeze a credential format or replace the security model of ATF, OAuth/OIDC, TLS, or payment providers.

## Security objectives

The adapter must preserve correct Service Entity identity, Agent/User principal binding, integrity of requested operations and parameters, bounded authority, explicit consent where required, audience/resource/context binding, replay resistance for side-effecting operations, lifecycle/revocation enforcement, protocol compatibility, audit correlation, and fail-closed behavior for missing or indeterminate required evidence.

## Assets

- Service identity and origin bindings
- Agent identity and authentication credentials
- User identity and approval evidence
- ATF authority/delegation evidence
- Capability declarations
- Request parameters and resource identifiers
- Consent records
- Payment authorization handoff evidence
- Idempotency keys and request identifiers
- Result/evidence records
- Lifecycle/revocation state
- Cryptographic keys and key metadata
- Service metadata/manifests

## Principals and trust boundaries

User, Agent, Service Entity, Adapter software, identity/authorization issuer where used, Agent-Pay, external providers, and attackers are distinct principals.

~~~text
User -> approval boundary -> Agent
Agent -> authentication/authorization boundary -> Site Adapter
Site Adapter -> service identity boundary -> Service Entity
ATF -> authority evidence boundary -> Site Adapter
Agent-Pay -> financial control boundary -> Site Adapter
~~~

## Threat catalogue

| ID | Threat | Required control |
|---|---|---|
| T01 | Service impersonation | Authenticated origin/service binding, integrity-protected metadata, lifecycle checks |
| T02 | Agent impersonation | Established authentication, credential validation, audience/resource binding, lifecycle checks |
| T03 | Origin confusion | Explicit origin/resource/audience binding |
| T04 | Credential substitution | Subject, audience/resource, scope and context binding |
| T05 | Replay | Freshness, request identifiers/nonces where appropriate, idempotency, expiry |
| T06 | Confused deputy | Preserve principal and authority evidence; never substitute adapter authority |
| T07 | Capability escalation | Precise capability identifiers, resource/operation constraints, separate authorization |
| T08 | Authorization confusion | Separate authentication, capability, consent and authorization evidence |
| T09 | Consent forgery/substitution | Bind consent to operation/context and enforce freshness |
| T10 | Discovery poisoning | Authenticated/integrity-protected metadata and binding verification |
| T11 | Downgrade | Explicit compatibility rules and minimum security profile |
| T12 | Revocation failure | Defined lifecycle/status mechanisms and fail-closed verification |
| T13 | SSRF/endpoint abuse | Endpoint policy, URL normalization, egress controls, private-address protection, redirect policy |
| T14 | Parameter substitution | Bind authorization/consent to protected operation and validate final parameters |
| T15 | Cross-service confusion | Service/resource/audience binding and explicit trust-domain policy |
| T16 | Key rotation abuse | Authenticated lifecycle evidence and successor-binding rules |

## Security invariants

- Authentication does not imply authorization.
- Discovery does not imply trust.
- Capability declaration does not imply authority.
- Consent does not manufacture authority.
- Agent-Pay approval does not expand ATF authority.
- A credential valid for one audience/resource must not automatically be valid for another.
- Side-effecting operations require a replay/idempotency strategy.
- Required invalid, expired, revoked, inconsistent, or indeterminate evidence fails closed.
- Key rotation must not silently change service identity.
- Adapter/service authority must not be substituted for agent authority.
- Authorized parameters must be bound to executed parameters.
- Security-sensitive metadata must be authenticated/integrity-protected before it is trusted.

## Decision outcomes

- VERIFIED: required evidence passed.
- FAILED: required evidence is invalid.
- UNKNOWN: required evidence is indeterminate; this is not verification.
- REQUIRE_HUMAN: only where policy permits intervention; it cannot create missing authority.

## Next gate

Phase 3 maps these threats and invariants to concrete authentication building blocks and deployment profiles.
