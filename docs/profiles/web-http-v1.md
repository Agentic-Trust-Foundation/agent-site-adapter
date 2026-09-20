# Web HTTP Profile V1

**Identifier:** `site-adapter/web-http/1`

This is the baseline generic HTTPS profile.

## Discovery

A service publishes a Site Adapter manifest at a deployment-selected HTTPS metadata location. When OAuth applies, OAuth Protected Resource Metadata at `/.well-known/oauth-protected-resource` SHOULD also be published.

The manifest identifies:
- service identifier;
- canonical origin;
- supported Site Adapter profiles;
- capabilities and versions;
- supported authentication profiles;
- endpoint templates;
- Agent-Pay support, if any.

Discovery metadata is descriptive only and grants no authority.

## Request

A protected request MUST carry:
- correlation/request ID;
- authenticated principal;
- selected capability/action;
- target resource;
- authority evidence reference;
- profile version.

Non-idempotent operations MUST carry an idempotency key.

## Response

A response MUST identify:
- request/correlation ID;
- outcome;
- service result or structured error;
- evidence reference when an authorization/payment decision was material.

## Errors

Use HTTP status semantics plus a stable machine-readable error code. Do not disclose whether hidden credentials or policies exist when that disclosure would create a security risk.

Recommended codes include:
`AUTHENTICATION_REQUIRED`, `AUTHENTICATION_INVALID`, `AUTHORITY_MISSING`, `AUTHORITY_INVALID`, `AUDIENCE_MISMATCH`, `CAPABILITY_UNSUPPORTED`, `CONSENT_REQUIRED`, `POLICY_DENIED`, `REPLAY_DETECTED`, `IDEMPOTENCY_CONFLICT`, `TEMPORARY_UNAVAILABLE`.

## Security

TLS certificate validation and origin binding are mandatory. Authorization artifacts SHOULD be audience-restricted. Sender-constrained tokens MAY be used where supported.
