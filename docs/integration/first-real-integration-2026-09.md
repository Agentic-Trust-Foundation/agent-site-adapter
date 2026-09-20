# First Real Integration — Web HTTP → Agent-Pay

This is the first executable integration profile for Site Adapter V1.

## Flow

1. Service exposes a Site Adapter-compatible manifest.
2. Agent authenticates using the deployment's established mechanism.
3. ATF authority evidence is supplied to Site Adapter.
4. Site Adapter evaluates identity, audience, action, resource, constraints, and consent.
5. Only `ALLOW` may produce an Agent-Pay handoff.
6. The handoff carries the original request identity, financial parameters, idempotency key, and authorization-context hash.
7. Agent-Pay re-verifies the evidence at its own boundary and applies financial policy.
8. Agent-Pay executes or requests human approval.
9. Provider result is correlated to the same payment intent.
10. Result/evidence is returned to the service and audit records retain the correlation IDs.

## Boundary
The adapter never executes a payment and never becomes a payment authority.

## Local test
The reference integration test proves both:
- valid authority reaches the handoff;
- missing authority cannot reach payment.

A deployment still needs real cryptographic evidence verification, TLS, secrets, provider credentials, and an actual service endpoint before production use.
