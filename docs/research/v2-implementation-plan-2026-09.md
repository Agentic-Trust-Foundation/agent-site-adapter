# Site Adapter V2 Implementation Plan

V1 is FINAL and frozen.

## Workstreams
1. dynamic trust-domain discovery
2. richer service capability negotiation
3. cross-domain authorization evidence
4. stronger federation profiles
5. agent-to-agent/service-to-service delegation
6. privacy-preserving provenance
7. assurance/reputation metadata
8. native MCP/A2A/commerce interoperability
9. multi-language SDKs
10. production crypto/key/revocation adapters

## Agent-to-agent delegation
The adapter must carry delegated authority as evidence, not infer authority from the fact that one agent invoked another. Each hop must preserve the original constraints and may only attenuate them.

## Federation
Federation metadata can establish membership/relationships, but authorization remains operation-specific.

## Reputation
Reputation and assurance are descriptive evidence. The adapter does not turn a score into ALLOW.

## Production security
V2 reference implementations should provide concrete cryptographic verification, key rotation, revocation checks, SSRF-safe metadata retrieval, replay protection, rate limits, and audit hooks.

## Wire-format rule
V2 may add concrete interoperable profiles only after semantic conformance tests exist. Native protocol semantics remain owned by MCP, A2A, OAuth, and other relevant standards.
