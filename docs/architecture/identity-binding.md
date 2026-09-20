# Identity Binding and Verification

**Status:** Phase 1 architecture contract  
**Date:** 2026-09-21

## 1. Purpose

This document defines the evidence and verification requirements for binding a Service Entity to an origin, endpoint, or authenticated key. It does not freeze one credential or wire format.

## 2. Binding relationship

```text
Service Identity
      |
      +-- Origin / Endpoint
      |
      +-- Authentication Key / Credential
      |
      +-- Protocol/Profile Scope
      |
      +-- Validity / Lifecycle
```

A URL, hostname, display name, adapter package, or unsigned metadata document is not sufficient by itself.

## 3. Evidence requirements

Binding evidence should provide, as applicable:

- service identifier;
- bound origin or endpoint;
- authenticated key/credential reference;
- intended protocol/profile;
- validity period or freshness information;
- issuer/authority information when an external issuer is involved;
- status/revocation information when applicable;
- integrity/authenticity protection;
- a way to detect replacement or rotation.

## 4. Verification

Verification is contextual. A verifier must evaluate:

1. authenticity and integrity;
2. service identity consistency;
3. origin/endpoint consistency;
4. key/credential binding;
5. intended audience/resource/profile;
6. freshness and validity;
7. lifecycle/status;
8. protocol compatibility;
9. policy requirements for the requested operation.

Failure of a required check results in an indeterminate or failed verification outcome and must not be treated as successful identity verification.

## 5. Key rotation

Key rotation must preserve the Service Entity identity when the authorized service operator replaces an authentication key.

```text
Service Identity
    |
    +-- Key A (retired)
    +-- Key B (active)
```

The architecture must distinguish key rotation from service replacement.

## 6. Multiple binding mechanisms

The implementation may support multiple binding profiles. Examples to evaluate include:

- HTTPS authenticated metadata;
- `.well-known` resources;
- TLS/certificate-bound evidence;
- signed metadata;
- DNS-assisted binding;
- federation or external issuer assertions.

No single mechanism is mandatory at this architecture stage.

## 7. Binding strength

The adapter must not collapse different evidence strengths into a single universal trust boolean.

A future profile may classify evidence according to properties such as authenticated origin, cryptographic key proof, issuer assurance, freshness, lifecycle status, and protocol/profile scope.

The result is evidence for policy evaluation, not an unconditional trust score.

## 8. Fail-closed rule

For security-sensitive operations, verification fails closed if required binding evidence is missing, malformed, unauthenticated, invalid, expired, revoked, replaced without valid successor evidence, inconsistent with the requested origin/resource, outside its declared scope, or otherwise indeterminate.

## 9. Separation from authorization

Successful identity binding does not authorize an agent.

Authorization remains a separate evaluation using the agent principal, capability, authority/delegation evidence, request context, and consent where required.

## 10. Next gate

Phase 2 will turn these requirements into an explicit threat model and security invariant set before selecting concrete authentication/discovery profiles.
