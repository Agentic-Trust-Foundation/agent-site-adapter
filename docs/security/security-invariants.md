# Security Invariants

**Status:** Phase 2 normative architecture baseline  
**Date:** 2026-09-21

## Identity
1. Service Entity identity is distinct from adapter software identity.
2. Agent, user, service, and adapter principals remain distinguishable.
3. An origin/endpoint is not sufficient proof of service identity without required binding evidence.
4. Key rotation must not silently create a new service identity.
5. Unknown identity/binding status is not successful verification.

## Authentication
6. Authentication does not by itself authorize an operation.
7. Authentication evidence must be checked for subject, audience/resource, validity, and applicable lifecycle status.
8. A credential accepted for one service/resource/context must not be assumed valid for another.
9. Established authentication mechanisms should be preferred over inventing a new cryptographic scheme.

## Discovery
10. Discovery metadata is untrusted until authenticity, integrity, freshness, and identity binding requirements are satisfied.
11. Discovery does not grant authority.
12. A discovered capability does not grant authority.
13. Security-sensitive metadata must not silently change the security profile or destination of an authorized request.

## Capability
14. A capability describes an operation the service exposes, not what a particular agent is allowed to do.
15. Capability identifiers and parameters must be precise enough to prevent accidental broadening.
16. Ambiguity must not be interpreted as broader authority.
17. Capability constraints must be checked against the actual requested operation.

## Authorization
18. Authorization is contextual and accounts for principal, capability, resource, request context, authority/delegation evidence, validity, and policy.
19. Authority may not be expanded by the adapter.
20. Delegation may not exceed the authority of the delegator.
21. The executed operation must remain within the operation authorized.

## Consent
22. Human approval is evidence of a policy decision, not a source of authority.
23. Consent for a sensitive operation must be bound to the relevant operation and context.
24. Stale, substituted, or mismatched consent must not authorize execution.

## Execution
25. Side-effecting requests require replay and duplicate-execution controls appropriate to risk.
26. Authorized parameters must be bound to execution parameters.
27. Retry behavior must not turn one authorized intent into uncontrolled repeated side effects.
28. Partial failures must not be reported as successful completion.

## Financial boundary
29. Financial policy belongs to Agent-Pay.
30. Agent-Pay may constrain an already-authorized action but may not manufacture upstream authority.
31. Financial approval does not override ATF authority constraints.

## Failure handling
32. Missing, invalid, expired, revoked, inconsistent, or indeterminate required evidence fails closed.
33. Errors must not leak credentials, secrets, or sensitive internal security policy.
34. Security decisions must be auditable and correlatable where required.

## Compatibility
35. Security-critical downgrade must not occur silently.
36. Unsupported protocol, capability, or security profile must fail clearly rather than silently falling back to a weaker profile.
