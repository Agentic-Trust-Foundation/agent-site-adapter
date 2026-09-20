# AGENTS.md

## Mission

Provide a reusable integration layer that lets websites and services expose authenticated, capability-aware interfaces to agents while integrating with ATF and, where needed, Agent-Pay.

## Rules

- Do not equate adapter installation with trust.
- Preserve ATF authority semantics.
- Keep identity, capability, authentication, consent, and authorization explicit.
- Prefer fail-closed behavior for missing required evidence.
- Keep browser-specific implementation separate from the generic integration model.
- Do not freeze a wire protocol without interoperability and security review.
- Add conformance coverage for externally observable protocol behavior.
- Never commit secrets.
