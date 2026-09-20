# Authentication Model

**Status:** Phase 3 architecture contract  
**Date:** 2026-09-21

## 1. Goal

Site Adapter authentication establishes the identity of the communicating principal and protects requests. It does not by itself grant authorization.

The design reuses established web security mechanisms rather than defining a new authentication protocol.

## 2. Authentication layers

~~~text
Transport security
      ↓
Service authentication
      ↓
Agent authentication
      ↓
Audience/resource binding
      ↓
ATF authority evidence
      ↓
Authorization
~~~

Each layer answers a different question.

## 3. Baseline requirements

For HTTP deployments, TLS is the baseline transport protection.

For agent-to-service authorization, OAuth-family mechanisms are the primary interoperability profile because they define token issuance, resource-server validation, scopes/authorization details, metadata discovery, and resource/audience binding.

The Site Adapter does not define a competing bearer-token protocol.

## 4. OAuth profile

Where OAuth is used:
- access tokens must be intended for the target protected resource;
- the service must validate token validity and applicable claims;
- authorization scope/action must be sufficient for the requested operation;
- tokens must not be accepted merely because they are validly signed;
- resource/audience binding must be checked;
- issuer/authorization-server relationships must be validated;
- least privilege is required.

OAuth 2.0 Security BCP requires protected access tokens to be restricted to intended resources/actions. Resource Indicators (RFC 8707) provide an established mechanism for explicit resource targeting.

## 5. Sender-constrained credentials

Where replay risk or deployment requirements justify it, a profile may use sender-constrained access tokens such as DPoP or mutual TLS.

These are profile choices, not a new Site Adapter cryptographic protocol.

## 6. Agent authentication

The adapter must distinguish the authenticated agent from the Service Entity, adapter software, user, and downstream payment provider.

Agent authentication evidence must be bound to the intended service/resource and applicable protocol profile. Exact credential representation remains profile-specific.

## 7. Service authentication

A service must establish its own identity/binding before security-sensitive metadata or requests are trusted.

Possible established mechanisms include TLS server authentication, authenticated metadata, OAuth protected-resource metadata, signed metadata where justified, and enterprise mTLS.

A hostname alone is not a universal service identity.

## 8. Audience/resource binding

A credential valid for Service A must not automatically be accepted by Service B.

Verification should consider, where applicable:
- issuer;
- subject/principal;
- audience/resource;
- scope or authorization details;
- expiry;
- status/revocation;
- proof of possession;
- request context.

## 9. Authorization evidence is separate

A successfully authenticated request still requires ATF authority evidence before a protected operation is authorized.

~~~text
Authenticated Agent
       !=
Authorized Agent
~~~

The Site Adapter consumes ATF authority semantics; it does not redefine them.

## 10. Key and credential lifecycle

Profiles must define issuance, activation, rotation, expiration, revocation/status, replacement, and unknown/indeterminate state.

Key rotation must preserve Service Entity identity when the identity remains the same.

Failure to establish required lifecycle state is fail-closed for protected operations.

## 11. Authentication failures

Conceptual outcomes:
- missing authentication;
- malformed authentication;
- invalid credential;
- expired credential;
- revoked credential;
- wrong audience/resource;
- wrong issuer;
- insufficient proof-of-possession;
- unsupported authentication profile;
- indeterminate verification.

These must not silently become anonymous or weaker authenticated requests.

## 12. No universal credential format in V1

The architecture does not mandate one universal JWT, VC, DID, mTLS certificate, or other credential format.

W3C Verifiable Credentials 2.0 is a standardized machine-verifiable credential model, but using VC/DID is not required merely to implement Site Adapter authentication.

## 13. Security constraints

The following are prohibited:
- accepting authentication as authorization;
- accepting a credential outside its intended audience/resource;
- silently downgrading to a weaker authentication method;
- substituting adapter credentials for agent identity;
- treating discovery metadata as authentication proof without verification;
- inventing a custom cryptographic handshake where an established mechanism satisfies the profile.

## 14. Next gate

Phase 4 defines discovery and interoperability around these authentication building blocks.
