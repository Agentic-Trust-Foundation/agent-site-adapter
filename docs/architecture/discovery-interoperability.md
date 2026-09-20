# Discovery and Interoperability Model

**Status:** Phase 4 architecture contract  
**Date:** 2026-09-21

## 1. Goal

Discovery allows an agent to learn how a Service Entity can be interacted with. Discovery does not establish trust or grant authority.

The design uses established HTTPS metadata patterns and does not require a centralized registry.

## 2. Discovery layers

~~~text
Service location
      ↓
Service metadata / manifest
      ↓
Identity and origin binding
      ↓
Protocol/profile compatibility
      ↓
Capabilities
      ↓
Authentication requirements
      ↓
Authenticated request
~~~

## 3. Service manifest

The Site Adapter architecture requires a machine-readable service manifest concept.

Conceptually it contains:
- service identity reference;
- origin/endpoint references;
- protocol versions;
- supported profiles;
- capabilities;
- authentication requirements;
- authorization requirements;
- consent requirements;
- financial-operation indicators;
- lifecycle/status;
- metadata integrity/binding information.

The exact serialization and URI are not frozen yet.

## 4. Established web discovery

The preferred foundation is normal HTTPS plus standardized web metadata mechanisms.

RFC 8615 defines the established /.well-known/ URI namespace. Where OAuth protected-resource authorization is used, RFC 9728 provides standardized protected-resource metadata.

## 5. Manifest versus OAuth metadata

These are different layers:

~~~text
Site Adapter Service Manifest
    = service integration metadata

OAuth Protected Resource Metadata
    = OAuth authorization metadata
~~~

A Site Adapter implementation may expose or reference both. The Site Adapter manifest must not contradict security-critical OAuth metadata.

## 6. Discovery integrity

A discovered document is not automatically trusted.

Before security-sensitive fields are used, the implementation must establish applicable transport security, origin relationship, identity binding, integrity/authenticity, freshness, lifecycle/status, and protocol compatibility.

Signed metadata may be used where a profile requires stronger integrity or offline verification.

## 7. Capability discovery

The manifest may advertise capabilities.

Capability discovery answers what the Service Entity can expose. It does not answer what an Agent may do. Authorization remains separate.

## 8. Authentication requirement discovery

Metadata may identify supported authentication profiles, such as OAuth, sender-constrained OAuth, or enterprise mTLS.

Discovery of an authentication method does not authorize its use.

## 9. Authorization-server discovery

When OAuth is used, implementations should use OAuth Protected Resource Metadata and Authorization Server Metadata according to the applicable standards.

MCP's current authorization specification demonstrates an interoperable pattern: protected-resource metadata identifies authorization servers and Resource Indicators explicitly bind tokens to the target resource.

Site Adapter adopts the principle, not MCP's application-specific protocol.

## 10. Interoperability profiles

A profile may define transport, discovery method, authentication method, capability serialization, authorization mapping, consent semantics, version requirements, and error behavior.

Profiles must not weaken the base security invariants.

## 11. No central registry requirement

Discovery must work without a global registry.

Implementations may use direct HTTPS location, .well-known metadata, enterprise configuration, application-specific discovery, or other profile-defined mechanisms.

A registry, if used by an ecosystem, is an optimization or governance layer rather than a mandatory trust authority.

## 12. Discovery attacks

Implementations must account for metadata substitution, stale metadata, malicious redirects, origin confusion, endpoint injection/SSRF, downgrade, capability spoofing, and authorization-server substitution.

Security-sensitive discovered values must be bound to the correct Service Entity and profile before use.

## 13. Interoperability rule

Two implementations are interoperable only when they agree on:
1. protocol/profile version;
2. transport expectations;
3. discovery representation;
4. authentication requirements;
5. capability semantics;
6. authorization semantics;
7. request/response and error semantics.

## 14. Next gate

Phase 8 defines compatibility, version negotiation, extensions, deprecation, and downgrade resistance.
