# Site and Service Identity

**Status:** Architecture baseline — Phase 1  
**Date:** 2026-09-21

## 1. Goal

A participating service must be distinguishable from the integration software, agent, and user involved in a request.

The primary target is a **Service Entity**. See [service-entity.md](./service-entity.md).

The identity architecture separates Service Entity identity, origin/endpoint binding, cryptographic/key evidence, adapter identity, agent identity, user identity, and lifecycle state.

## 2. Conceptual identity object

```text
Service Identity
├── stable service identifier
├── human-readable metadata
├── origin/endpoint bindings
├── authentication/key bindings
├── supported protocol/profile versions
├── capability references
└── lifecycle state
```

This is a conceptual model, not a wire-format proposal.

## 3. Stable service identifier

A Service Entity needs a stable identifier that is not silently replaced by a URL, hostname, display name, or adapter package name.

The identifier should support long-lived reference, ownership/authority, correlation across multiple interfaces, lifecycle transitions, verification evidence, and future delegation/audit references.

The exact identifier syntax is intentionally not frozen yet.

## 4. Origin and endpoint binding

A domain or URL is an input to discovery, not sufficient proof of service identity on its own.

The target relationship is:

```text
Service Identity <-> Origin / Endpoint <-> Authenticated Key / Credential
```

A future verification mechanism must establish which Service Entity is represented, which origin/endpoint is bound to it, which key or authenticated credential proves the binding, what protocol/profile the evidence is valid for, and whether the evidence is current and not revoked or replaced.

Established HTTPS/web mechanisms should be evaluated first, including authenticated metadata, `.well-known` resources, certificate/key bindings, signed metadata, DNS-assisted mechanisms, or combinations where justified. No single mechanism is mandatory yet.

## 5. Adapter identity

The adapter implementation has its own software identity/version:

```text
Adapter software identity != Service identity
```

An official adapter may prove properties about the adapter implementation. It cannot, by itself, prove that the connected Service Entity is trustworthy.

## 6. Principal separation

```text
Service Identity
!= Adapter Identity
!= Agent Identity
!= User Identity
```

Authentication of one principal must not be silently reused as authorization evidence for another.

## 7. Lifecycle

Identity and binding evidence must support, as appropriate: active, suspended, expired, revoked, replaced, and unknown/indeterminate.

Security-sensitive verification fails closed when required identity evidence is missing, invalid, expired, revoked, inconsistent, or indeterminate.

Rotation must not silently change the Service Entity identity merely because its cryptographic key changed.

## 8. Identity vs authorization

Identity answers: **Who or what is this?**

Authorization answers: **Is this principal allowed to perform this operation in this context?**

A verified service identity does not grant an agent permission to invoke arbitrary capabilities.

## 9. Identity vs discovery

Discovery answers what service metadata can be retrieved from a location. It does not answer whether the service should be trusted for an operation.

Discovery metadata is therefore evidence subject to authenticity, integrity, freshness, and binding checks.

## 10. Next Phase

Phase 1 continues with Identity Binding and Verification: define identity evidence, compare established binding mechanisms, define key/credential binding, define verification steps, define lifecycle transitions, define failure semantics, and define the security properties required before discovery metadata can be trusted.
