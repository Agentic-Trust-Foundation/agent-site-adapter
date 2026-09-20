# Versioning and Compatibility

**Status:** Phase 8 architecture contract  
**Date:** 2026-09-21

## 1. Versioning goals

Versioning must allow independent implementations to evolve without silently changing security meaning, silently broadening authority, breaking integrations without an explicit compatibility decision, or accepting a weaker security profile through downgrade.

## 2. Version dimensions

~~~text
Protocol version
Profile version
Manifest version
Capability version
Interface/API version
Implementation version
~~~

An implementation version must never be treated as proof of protocol compatibility.

## 3. Protocol version

The protocol uses a conceptual MAJOR.MINOR compatibility model.

**Major:** may introduce incompatible normative behavior or security semantics. Major versions are not silently interchangeable.

**Minor:** may add backward-compatible functionality when existing normative semantics remain valid. A consumer must not assume every feature of a newer minor version exists in an older implementation.

The exact wire representation remains open.

## 4. Profile negotiation

A Service Entity may support multiple profiles.

Negotiation must establish:
- mutually supported protocol version;
- mutually supported profile;
- required authentication/security profile;
- capability versions where relevant.

Unsupported combinations must fail explicitly.

## 5. No silent downgrade

If a client requires a security property that a service cannot provide, the client must not silently select a weaker profile.

~~~text
required sender-constrained token
        ↓
service supports bearer only
        ↓
FAIL / explicit policy decision
~~~

## 6. Capability versioning

Capabilities have their own compatibility lifecycle.

A capability change is compatible only when existing consumers can preserve the old operation's security and semantic meaning.

Changes to required parameters, resource scope, side effects, authorization requirements, consent requirements, or financial behavior should be treated as potentially incompatible even when transport is unchanged.

## 7. Manifest versioning

Manifest schema changes must be independently versionable.

A consumer may safely ignore unsupported optional metadata only where the profile says it is safe. Unknown security-critical fields must not be guessed.

## 8. Extension model

Extensions should be explicitly namespaced and discoverable.

An extension must define:
- identifier;
- version;
- purpose;
- required/optional status;
- compatibility rules;
- security considerations.

Extensions must not silently redefine a base capability or security invariant.

## 9. Deprecation

A profile or capability may enter:

~~~text
active → deprecated → sunset/removed
~~~

Deprecation metadata should provide migration information where deployment permits it.

## 10. Security-sensitive changes

Any change affecting authentication, audience/resource binding, authorization, consent, cryptographic requirements, replay protection, or financial controls requires explicit security review before being classified as backward-compatible.

## 11. Version selection

Version selection should be deterministic and policy-aware.

A client should consider:
1. security requirements;
2. supported protocol versions;
3. supported profiles;
4. capability requirements;
5. service compatibility.

The newest version is not automatically the correct version.

## 12. Error semantics

Version incompatibility must produce an explicit protocol/version error rather than an ambiguous authentication or business error.

## 13. Compatibility matrix

| Consumer | Service | Expected result |
|---|---|---|
| same major/minor | same major/minor | compatible if profile requirements match |
| older minor | newer compatible minor | compatible only for supported features |
| newer minor | older minor | use only mutually supported features |
| different major | different major | explicit incompatibility unless a bridge/profile exists |
| security profile mismatch | any | fail; no silent downgrade |
| capability version mismatch | any | fail or negotiate according to profile |
| unknown security-critical extension | any | fail closed where required |

## 14. Next gate

Phase 9 will turn these rules into normative conformance cases, fixtures, and interoperability tests.
