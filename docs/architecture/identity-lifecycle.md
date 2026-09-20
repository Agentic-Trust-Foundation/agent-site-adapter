# Identity and Binding Lifecycle

**Status:** Phase 1 architecture contract  
**Date:** 2026-09-21

## Lifecycle states

Conceptually, a Service Identity and each binding may be:

- ACTIVE
- SUSPENDED
- EXPIRED
- REVOKED
- REPLACED
- UNKNOWN

UNKNOWN is not a successful verification state.

## Transitions

```text
UNKNOWN -> ACTIVE
ACTIVE -> SUSPENDED
ACTIVE -> EXPIRED
ACTIVE -> REVOKED
ACTIVE -> REPLACED
SUSPENDED -> ACTIVE
SUSPENDED -> REVOKED
EXPIRED -> REPLACED
```

The concrete transition authority and wire representation remain profile-specific.

## Key rotation

Key rotation should normally transition the binding from an old key to a new active key while preserving the Service Entity identifier.

```text
Service A
  |
  +-- Key A: REPLACED
  +-- Key B: ACTIVE
```

A new key must not silently create a new Service Entity.

## Service replacement

When control of a service changes in a way that invalidates the prior identity binding, the old binding must not be treated as active merely because the endpoint remains unchanged.

## Revocation

Revocation must be observable enough for a security-sensitive verifier to avoid accepting known-invalid evidence.

The exact status mechanism is deferred to the authentication/discovery profile.

## Fail-closed behavior

If lifecycle status cannot be established where status is required, the verification result is not VERIFIED.

## Auditability

Lifecycle events should be correlatable with service identifier, binding identifier, key/credential reference, event time, actor/authority, reason or event type, and successor binding where relevant.

This is an architecture requirement, not a commitment to one audit storage technology.
