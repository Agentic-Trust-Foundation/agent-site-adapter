# Site Adapter V1 Security Review

**Date:** 2026-09-21  
**Status:** Release-candidate review complete

## Reviewed areas

- identity/origin binding;
- discovery versus trust separation;
- authentication versus authorization;
- capability versus authority;
- delegation attenuation;
- consent substitution;
- human approval;
- audience/resource binding;
- replay/idempotency;
- profile downgrade;
- dynamic metadata/SSRF;
- Agent-Pay authority boundary;
- sensitive-data handling;
- error disclosure.

## Required V1 invariants

1. Missing or indeterminate security evidence never produces ALLOW.
2. Authentication never substitutes for authorization.
3. Capability declarations never create authority.
4. Delegation cannot exceed delegator authority.
5. Consent cannot manufacture authority.
6. Agent-Pay cannot expand ATF authority.
7. Resource/audience substitution is denied.
8. Non-idempotent retries preserve the original idempotency key.
9. Security-critical unknown extensions fail closed.
10. Dynamic metadata retrieval is constrained against SSRF.
11. TLS validation is mandatory for network metadata and protected requests.
12. Sensitive payment credentials are outside Site Adapter discovery metadata.

## Residual deployment risks

The reference implementation is not a production security boundary. Production deployments still need:
- cryptographic verification;
- secure key storage and rotation;
- concrete token/credential validation;
- lifecycle/revocation infrastructure;
- hardened HTTP clients;
- rate limiting and abuse controls;
- environment-specific privacy/compliance controls.

These are deployment gates, not excuses to weaken the protocol invariants.
