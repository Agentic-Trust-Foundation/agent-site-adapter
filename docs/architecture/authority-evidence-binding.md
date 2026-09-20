# Authority Evidence Binding

**Status:** Phase 6 architecture contract  
**Date:** 2026-09-21

This document defines the minimum semantic binding required when Site Adapter consumes ATF authority evidence. It intentionally does not define one universal credential serialization.

## 1. Evidence is contextual

Authority evidence is meaningful only in the security context for which it was issued.

A verifier should establish, as applicable:

- issuer/trust domain;
- subject/principal;
- delegate/agent identity;
- service/resource audience;
- requested capability/action;
- target resource;
- parameter constraints;
- validity period;
- lifecycle/revocation state;
- delegation constraints;
- protocol/profile compatibility.

A valid signature alone is insufficient.

## 2. Binding model

~~~text
Authority evidence
       +
Authenticated principal
       +
Target service/resource
       +
Requested capability/action
       +
Target resource
       +
Request parameters
       +
Time/lifecycle
       ↓
Contextual authorization input
~~~

If the evidence cannot be safely bound to the request context, the request must not be authorized.

## 3. Subject binding

The authenticated agent must correspond to the principal/delegate represented by the authority evidence.

The adapter must not accept:

- another agent's authority;
- a service credential as agent authority;
- adapter identity as user authority;
- user identity as automatic proof of agent authority.

Where an agent acts on behalf of a user, the relevant principal relationships must be explicitly represented by the applicable ATF profile.

## 4. Service/resource binding

Authority must be constrained to the intended service/resource.

The verifier should reject evidence when:

- audience/resource is absent where required;
- audience/resource does not match;
- the evidence was issued for another protected resource;
- a cross-service substitution would be possible.

## 5. Capability and action binding

The evidence must authorize the requested action, not merely a broader-looking category inferred by the adapter.

A capability identifier, human-readable name, or service metadata entry must not be treated as authority unless the authority evidence and applicable policy establish the permission.

## 6. Resource binding

When an operation targets a specific resource, authorization should bind to that resource or to an explicitly permitted resource set.

Examples:

- one merchant/account;
- one booking;
- one infrastructure cluster;
- one customer record;
- one payment recipient.

Broad resource substitution must not be inferred from a matching capability name.

## 7. Constraint binding

Where authority contains constraints, the request must satisfy them.

Common constraints include:

- maximum amount;
- currency;
- quantity;
- destination;
- resource identifier;
- operation;
- time window;
- geographic/service boundary;
- required user presence;
- required consent.

The effective request must remain within every applicable upstream constraint.

## 8. Delegation chain binding

When authority is delegated:

~~~text
Root authority
    ↓
Delegation 1
    ↓
Delegation 2
    ↓
Authenticated delegate
    ↓
Requested operation
~~~

Every step must be valid and bounded by the preceding step.

A verifier must not accept a downstream delegation that exceeds upstream authority.

Exact chain representation is deferred to the applicable ATF profile.

## 9. Consent binding

Consent is additional evidence when required by policy.

Consent must not be accepted as a substitute for authority evidence.

Where transaction-specific consent is required, it should be bound to the same security-sensitive operation and parameters that will be executed.

## 10. Financial binding

For financial operations, the authority evidence passed to Agent-Pay must describe the same authorized intent that Site Adapter evaluated.

At minimum, the handoff should preserve relevant:

- principal/agent;
- service/resource;
- capability/action;
- amount;
- currency;
- recipient/resource;
- validity;
- authorization decision;
- authority evidence reference;
- request/correlation identifier.

Agent-Pay may further restrict the transaction, but may not expand these constraints.

## 11. Integrity and substitution resistance

Implementations should provide integrity protection for the relationship between:

- authority evidence;
- request context;
- authorization decision;
- consent;
- financial intent where applicable.

A reference identifier alone is not sufficient if an attacker can substitute the referenced context.

Where a profile uses a digest/hash of an authorization context, all security-sensitive fields included in the decision must be covered by the defined canonicalization and digest rules.

## 12. Lifecycle

Authority evidence must support profile-defined lifecycle semantics.

The verifier must not treat unknown, expired, revoked, or otherwise invalid evidence as valid authority.

Caching is allowed only when the profile's freshness and revocation requirements are satisfied.

## 13. Failure handling

Verification failures should produce semantic authorization errors rather than silent fallback.

Examples:

- AUTHORITY_MISSING
- AUTHORITY_INVALID
- AUTHORITY_EXPIRED
- AUTHORITY_REVOKED
- AUTHORITY_AUDIENCE_MISMATCH
- AUTHORITY_SUBJECT_MISMATCH
- AUTHORITY_SCOPE_MISMATCH
- AUTHORITY_CONSTRAINT_VIOLATION
- DELEGATION_INVALID
- CONSENT_MISSING
- CONSENT_MISMATCH
- AUTHORITY_STATUS_INDETERMINATE

These are semantic classes, not frozen wire error codes.

## 14. No universal credential format

This contract does not require JWT, VC, DID, mTLS, or another single credential technology.

An implementation may use an established credential mechanism selected by its interoperability/security profile, provided that the resulting evidence satisfies these semantic binding requirements.

## 15. Conformance target

Phase 9 should test authority evidence with:

- valid and invalid subjects;
- wrong service audience;
- wrong resource;
- wrong capability/action;
- expired and revoked evidence;
- delegation exceeding upstream authority;
- changed amount/currency/recipient;
- replayed consent;
- stale lifecycle state;
- Agent-Pay attempts to exceed upstream authority.
