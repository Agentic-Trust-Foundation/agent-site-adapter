# Site and Service Identity

**Status:** Architecture baseline — draft

## 1. Goal

A participating site or service must be distinguishable from the integration software used to connect to it.

The identity model therefore separates:

- **service identity**
- **integration/adapter identity**
- **origin or endpoint binding**
- **cryptographic/authenticated binding**
- **lifecycle state**

## 2. Conceptual identity object

A future implementation needs to represent, at minimum:

~~~text
Service Identity
  ├── stable service identifier
  ├── human-readable metadata
  ├── origin/endpoint bindings
  ├── authentication/key bindings
  ├── supported protocol/profile versions
  ├── capability references
  └── lifecycle state
~~~

This is a conceptual model, not a wire-format proposal.

## 3. Origin binding

A domain or URL is not sufficient proof of service identity on its own.

The system should be able to establish a verifiable relationship between:

~~~text
Service Identity <-> Origin/Endpoint <-> Authenticated Key/Credential
~~~

The exact mechanism is intentionally open.

Possible mechanisms to evaluate include authenticated HTTP metadata, DNS-based bindings, well-known resources, signed metadata, certificate/key bindings, or combinations of these.

No mechanism is selected by this document.

## 4. Adapter identity

The adapter implementation may have its own software identity and version, but that must not be confused with the identity of the service.

For example:

~~~text
Adapter package identity != Site identity
~~~

An official adapter can establish that a known integration implementation is being used; it cannot by itself prove that the connected service is trustworthy.

## 5. Identity lifecycle

Identity-related state must support, as appropriate:

- issuance/registration
- activation
- rotation
- expiration
- suspension
- revocation
- replacement
- auditability

The exact lifecycle protocol is deferred until the threat model and interoperability requirements are complete.

## 6. Identity and authorization

Identity answers:

> Who/what is this?

Authorization answers:

> Is this principal allowed to perform this operation under this context?

The adapter must preserve this distinction.
