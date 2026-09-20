# Agent Site Adapter

Public integration layer for websites and online services participating in the agentic internet.

## V1 status

**V1 FINAL — 2026-09-21**

Site Adapter V1 freezes the semantic contract, generic HTTPS/JSON binding, profile identifiers, conformance requirements and the Agent-Pay integration boundary.

## Purpose

Agent Site Adapter provides a practical way for a website or service to expose an agent-accessible interface while integrating with the Agentic Trust Foundation and, where applicable, Agent-Pay.

The project is intentionally broader than a browser extension. The implementation may include SDKs, web components, server-side adapters, APIs, metadata, and other integration tools.

## Core principle

Installing or receiving an official adapter does **not** by itself mean that a website is trusted.

Trust and authorization require explicit evidence such as authenticated identity, origin/domain binding, capability declarations, credential verification, policy evaluation, and lifecycle/revocation controls.

## Ecosystem boundary

```
Agentic Trust Foundation
          |
          v
   Agent Site Adapter
          |
          v
   Website / Service
          |
          v
   Agent Commerce / APIs
          |
          v
      Agent-Pay
```

ATF establishes authority and trust semantics. Site Adapter applies those semantics to service interaction. Agent-Pay evaluates financial controls and executes financial operations. Neither downstream layer may expand upstream authority.

## V1 profiles

- Web HTTP
- OAuth HTTP
- MCP
- A2A
- Commerce
- Booking
- SaaS/API
- Enterprise
- Healthcare
- Cloud/infrastructure
- Agent-Pay

External protocols remain authoritative for their own wire formats.

## Non-goals

This project is not:
- a centralized trust registry
- a replacement for ATF
- a payment processor
- a merchant marketplace
- proof that every integrated site is trustworthy
- a browser-extension-only architecture

## Reference implementation

The Python package is a dependency-light semantic/profile reference. It is not a production security boundary.

Run:

~~~bash
python -m pip install -e '.[test]'
pytest
~~~

Production deployments still require concrete cryptographic verification, key management, revocation/lifecycle enforcement, hardened transport clients, abuse controls and deployment-specific compliance/privacy controls.

See:
- `docs/protocol/site-adapter-v1.md`
- `docs/profiles/v1-profile-framework.md`
- `docs/profiles/agent-pay-v1.md`
- `docs/conformance/v1-profiles.md`
- `docs/release/v1-final-2026-09.md`
