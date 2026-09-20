# Capability Model

**Status:** Architecture contract — Phase 5  
**Date:** 2026-09-21

A capability describes an operation that a Service Entity exposes to an agent. It is a machine-readable description of service functionality, not an authorization grant.

~~~text
Capability = what the service can do
Authority   = what this principal may do
~~~

## Capability object

~~~text
Capability
├── capability_id
├── version
├── operation/action
├── resource/resource-class
├── input schema
├── output/result contract
├── side effects
├── risk/sensitivity
├── preconditions
├── authorization requirements
├── consent requirements
├── financial flag/policy reference
├── protocol/profile requirements
└── lifecycle/status
~~~

This is not frozen serialization.

## Capability identifiers and scope

A capability should have a stable identifier within its protocol/profile namespace. It must not be inferred solely from a human-readable display name.

A capability must identify the operation and affected resource/resource class precisely enough to prevent accidental scope expansion.

Illustrative examples:

- catalog.read
- inventory.query
- booking.create
- booking.cancel
- order.create
- order.cancel
- account.profile.read
- infrastructure.instance.create

These are examples, not a mandatory V1 registry.

## Inputs and constraints

A declaration should identify required inputs, types/schema, allowed ranges/enumerations where relevant, resource identifiers, preconditions, side effects, sensitivity/risk, and payment implications.

Security-sensitive constraints must be enforceable, not merely descriptive.

## Capability versus authorization

~~~text
Service declares capability
        ↓
Agent selects capability
        ↓
Request supplies operation + parameters
        ↓
Authentication
        ↓
ATF authority/delegation evidence
        ↓
Authorization
        ↓
Consent if required
        ↓
Execution
~~~

Advertising an operation does not mean every agent may invoke it.

## Least privilege

Capability requests should be as narrow as the intended operation permits. Prefer specific operation + specific resource + constrained parameters over broad implicit permissions.

A capability declaration must not be interpreted as permission to invoke undocumented side effects.

## Capability constraints

Capabilities may carry constraints such as resource scope, operation, quantity, amount, currency, time window, geographic/service boundary, required user presence, required consent, and payment requirement.

These constraints are inputs to policy evaluation, not proof that the agent satisfies them.

## Financial capabilities

A capability that can cause financial consequences must be identifiable so Agent-Pay can be invoked.

~~~text
Capability
    ↓
financial = true
    ↓
Agent-Pay policy evaluation
~~~

This does not give Agent-Pay permission to expand ATF authority.

## Lifecycle

Capabilities should support active, deprecated, suspended, revoked/removed, replaced, and unknown states. Unknown status must not be interpreted as active for security-sensitive operations.

## Capability discovery

Capabilities may be discovered through a service manifest or other supported metadata mechanism. Discovery is informational until metadata is authenticated and bound according to the applicable profile.

## Compatibility

Consumers must verify protocol version, capability version, required security profile, required authentication mechanism, and input/output contract.

Unsupported or ambiguous capabilities must not silently fall back to a weaker or broader interpretation.

## Evidence correlation

Where a request is authorized against a declared capability, implementation should correlate service identity, capability identifier/version, request identifier, resource, relevant constraints, authorization evidence, consent evidence where applicable, and result.

## Next gate

Capability wire serialization remains open until Phase 4 interoperability and Phase 8 versioning are sufficiently stable.
