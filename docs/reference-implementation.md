# Minimal Reference Implementation

**Status:** Phase 10 baseline — 2026-09-21

The reference implementation is intentionally small and dependency-light. It demonstrates the architecture's core authorization semantics without prematurely freezing the eventual protocol wire format.

## Included

- Python package under src/agent_site_adapter/;
- service/request/authority/consent data models;
- contextual authorization evaluator;
- fail-closed behavior;
- bounded delegation validity input;
- audience, subject, action, resource and financial-parameter checks;
- consent binding;
- ALLOW / DENY / REQUIRE_HUMAN outcomes;
- pytest conformance tests.

## Explicit non-goals

This implementation does not yet freeze:

- credential serialization;
- manifest wire format;
- discovery endpoint;
- OAuth token profile;
- delegation-chain serialization;
- cryptographic suite;
- payment provider integration;
- browser-extension packaging.

Those belong to concrete interoperability profiles after the architecture/security gates.

## Run

~~~bash
python -m pip install -e '.[test]'
pytest
~~~

The implementation is a reference for semantics, not a production security boundary. Deployments must perform profile-specific cryptographic verification, lifecycle/revocation checks, transport protection, and policy integration.
