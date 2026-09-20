# Interoperability Patterns Research — 2026-09

## Purpose

This document records external protocol patterns reviewed while designing Agent Site Adapter. It is research input, not a normative dependency list.

## Sources reviewed

- IETF RFC 9700 — OAuth 2.0 Security Best Current Practice
- IETF RFC 9635 — GNAP
- W3C Verifiable Credentials Data Model 2.0
- OpenID Connect Federation 1.0
- Model Context Protocol authorization specification
- Agent2Agent (A2A) protocol specification
- Universal Commerce Protocol (UCP) embedded protocol
- OAuth/OpenID discovery metadata patterns
- OpenAPI security scheme model

## Convergent patterns

### 1. Describe before invoking

Mature protocols commonly expose machine-readable metadata before an operation is invoked.

Examples:
- A2A Agent Card describes identity, capabilities, interfaces, and security requirements.
- MCP uses protected-resource and authorization-server metadata for authorization discovery.
- UCP separates shared transport/session mechanics from capability-specific contracts.
- OpenAPI provides machine-readable operation and security metadata.

**Architectural implication:** Site Adapter should have a machine-readable service description/manifest. It should be descriptive and verifiable, not an authorization grant.

### 2. Discovery is not trust

Discovery metadata can tell an agent where and how to interact, but it must not be treated as proof of authority or safety.

MCP explicitly validates issuer/resource metadata and uses protected-resource metadata to discover authorization servers.

**Architectural implication:** Discovery output is untrusted input until the applicable identity/authenticity checks succeed.

### 3. Reuse established web security

A2A explicitly aligns authentication with standard web mechanisms and advertises supported schemes in its Agent Card.

MCP's current HTTP authorization model builds on OAuth 2.1-era security practices, protected-resource metadata, resource indicators, and audience/resource validation.

RFC 9700 recommends sender-constrained tokens where appropriate and audience-restricted access tokens.

**Architectural implication:** Site Adapter should reuse HTTP/OAuth/OIDC/mTLS/DPoP-style mechanisms where appropriate instead of inventing a custom authentication protocol.

### 4. Resource/audience binding matters

MCP requires tokens to identify the intended protected resource and requires servers to validate that tokens were issued for them.

**Architectural implication:** Authorization artifacts used for Site Adapter requests must be bound to the intended service/resource and operation context as required by the applicable ATF profile.

### 5. Capability declarations do not equal authorization

A2A declares capabilities and skills, while authorization scoping remains an independent security requirement.

MCP treats tool descriptions as untrusted unless obtained from a trusted server and requires authorization checks before sensitive operations.

**Architectural implication:** Site Adapter capability metadata describes what the service offers; ATF authority determines what the agent may do.

### 6. Human consent is a first-class security boundary

MCP emphasizes explicit user consent and control for data access and tool invocation.

GNAP models interactive authorization/consent as part of delegated authorization.

**Architectural implication:** Consent/approval should be represented and correlated with the protected operation rather than hidden inside UI behavior.

### 7. Cryptographically verifiable claims are useful, but no single identity technology is mandatory

W3C Verifiable Credentials define issuer, holder, verifier roles and tamper-evident claims.

OpenID Federation demonstrates signed metadata and explicit trust chains between entities.

These are useful patterns, but neither implies that every Site Adapter deployment must use VC, DID, or federation.

**Architectural implication:** ATF evidence should remain technology-neutral at the semantic layer, with concrete credential mechanisms supplied by profiles/adapters.

## Architectural decisions resulting from this research

1. Site Adapter will expose a machine-readable service manifest.
2. The manifest will describe identity, endpoints/interfaces, capabilities, protocol versions, and authentication requirements.
3. The manifest is metadata, not an authorization grant.
4. Discovery will prefer established HTTPS/web metadata mechanisms and will not require a central registry.
5. Authentication will reuse established web security standards where possible.
6. Protected requests will require audience/resource/context binding appropriate to the authorization mechanism.
7. Capability declarations remain distinct from authorization.
8. Consent remains explicit and correlatable to an operation.
9. Exact wire format and credential technology remain open until threat-model and interoperability review.
