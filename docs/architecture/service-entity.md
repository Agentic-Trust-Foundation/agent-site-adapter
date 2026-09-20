# Service Entity Architecture

**Status:** Accepted architecture baseline  
**Date:** 2026-09-21

## 1. Purpose

The Site Adapter must not model participation as "a website with an extension". The participating target is a **Service Entity**: an independently operated service that exposes one or more agent-consumable interfaces.

A Service Entity may be:

- a website;
- an API;
- a SaaS application;
- an ecommerce service;
- a booking or travel service;
- an enterprise service;
- a healthcare service;
- a financial service;
- a cloud/infrastructure service;
- another machine-consumable service.

The same conceptual model must work across these forms.

## 2. Conceptual model

~~~text
Service Entity
├── Service Identity
├── Origin / Endpoint Bindings
├── Interfaces
├── Capabilities
├── Authentication Requirements
├── Authorization / Consent Requirements
├── Operational Policies
└── Lifecycle State
~~~

This is an architecture model, not a wire format.

## 3. Service identity vs adapter identity

These are separate principals:

~~~text
Service Identity
    ≠
Adapter Software Identity
    ≠
Agent Identity
    ≠
User Identity
~~~

An adapter is an integration mechanism. Possessing, installing, or invoking an official adapter does not establish that the target Service Entity is trusted.

## 4. Origin and endpoint binding

A Service Entity may expose multiple origins/endpoints. The architecture therefore treats origin/endpoint binding as evidence that must be verified, not as an identity string copied from an untrusted request.

A future binding mechanism must answer:

1. Which Service Entity does this endpoint claim to represent?
2. What evidence binds the endpoint to that identity?
3. Is the evidence current?
4. Is the evidence intended for this protocol/profile?
5. Has the binding been revoked, replaced, or otherwise invalidated?

## 5. Multiple interfaces

One Service Entity may expose several interfaces:

~~~text
Service Entity
├── Web UI
├── REST API
├── Agent Interface
└── Event/Webhook Interface
~~~

These interfaces may have different authentication and authorization requirements while remaining part of the same service identity model.

## 6. Identity is not authority

A verified Service Entity identity does not automatically authorize an agent to perform any operation.

The request must still pass:

~~~text
Identity
  ↓
Authentication
  ↓
Capability
  ↓
Authority / Authorization
  ↓
Consent (when required)
  ↓
Execution
~~~

## 7. Lifecycle

Identity and bindings must support at least these conceptual states:

- active;
- suspended;
- expired;
- revoked;
- replaced;
- unknown/indeterminate.

Security-sensitive verification must fail closed when required evidence is missing, invalid, expired, revoked, inconsistent, or indeterminate.

## 8. Design constraints

The Site Adapter architecture does not require:

- a centralized service registry;
- a universal trust score;
- a universal "trusted website" boolean;
- one credential format;
- one authentication mechanism;
- browser-extension-only deployment;
- a new cryptographic protocol.

Established web security mechanisms should be reused where they fit the deployment and threat model.

## 9. Next gate

The next normative architecture gate is **Identity Binding and Verification**. It will define the evidence model, verification flow, cryptographic/key binding options, lifecycle transitions, and failure semantics before a concrete wire format is selected.
