# Site Adapter Protocol V1

**Status:** Normative V1 — frozen 2026-09-21

## Scope

Site Adapter V1 standardizes the semantic and HTTP integration contract needed for an agent to interact with a Service Entity.

It does not create a centralized registry or replace ATF, OAuth, MCP, A2A, UCP or Agent-Pay.

## V1 objects

### Service Manifest

A manifest contains:
- `service_id`
- `origin`
- `protocol_version`
- `profiles[]`
- `capabilities[]`
- `auth_requirements[]`
- `endpoints[]`
- optional `agent_pay` support declaration.

The manifest is signed or authenticated by the deployment's established identity mechanism where required by the selected profile. A manifest alone is not authority.

### Request Context

A request is evaluated against:
- request ID;
- authenticated subject;
- service/audience;
- capability;
- action;
- resource;
- parameters;
- authority evidence;
- consent/approval evidence;
- profile version.

### Authorization result

Exactly one semantic outcome:
- `ALLOW`
- `DENY`
- `REQUIRE_HUMAN`

`REQUIRE_HUMAN` is valid only when the underlying authority is already valid.

## HTTP binding

The V1 HTTP binding uses HTTPS and JSON. Deployments expose service-specific operation endpoints; Site Adapter does not impose one universal URL layout.

Required headers/metadata:
- `Site-Adapter-Profile`
- `Site-Adapter-Version`
- `X-Request-ID`
- `Idempotency-Key` for non-idempotent operations.

The exact authentication header is inherited from the selected authentication profile (for example OAuth Bearer/DPoP or mTLS).

## Request envelope

The adapter metadata MUST semantically contain:

```json
{
  "profile": "site-adapter/web-http/1",
  "request_id": "req-123",
  "capability": "order",
  "action": "order.create",
  "resource": "merchant-123",
  "authority": {"id": "atf-evidence-123"},
  "consent": {"id": "consent-123"},
  "parameters": {}
}
```

Implementations MAY map this envelope into an adopted protocol such as UCP, MCP or A2A instead of sending it literally.

## Response envelope

A conforming response MUST provide equivalent semantics for:
- request ID;
- outcome/status;
- result or structured error;
- evidence/reference when material.

## Idempotency

A logical retry MUST use the same idempotency key. A new business operation MUST use a new key.

Services MUST NOT execute two distinct operations under one idempotency key.

## Errors

Error responses MUST be machine-readable and stable. Security-sensitive details MUST be minimized.

## Compatibility

V1 major version is `1`. A peer MUST reject incompatible major versions. Security-critical unknown extensions MUST fail closed.

## Normative boundary

ATF owns authority establishment and trust/delegation semantics. Site Adapter owns service integration and contextual enforcement. Agent-Pay owns financial controls and execution. No V1 component may cross these boundaries by implication.
