# AI Context — Agent Site Adapter

Agent Site Adapter is the **service integration layer** for websites and online services participating in the agentic internet.

## Relationship to ATF and Agent-Pay

- **ATF:** establishes identity, delegation, authorization, trust, and authority evidence.
- **Site Adapter:** applies those semantics to a service interaction and exposes integration profiles.
- **Agent-Pay:** applies financial controls and executes payment operations when the action is financial.

## Important classification

Site Adapter is not:

- a centralized trust registry;
- a replacement for ATF;
- a payment processor;
- a merchant marketplace;
- proof that an integrated site is trustworthy;
- a browser-extension-only architecture;
- a replacement for MCP, A2A, OAuth, or a site's native protocol.

The MCP and A2A profiles describe interoperability semantics and boundaries. They do not, by themselves, claim to implement production MCP/A2A servers or certify every integrated service.

See the ATF repository's canonical PROJECT.md, WHY.md, AI-CONTEXT.md, and STATUS.md for the ecosystem-level interpretation.
