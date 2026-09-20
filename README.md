# Agent Site Adapter

Public integration layer for websites and online services participating in the agentic internet.

## Purpose

Agent Site Adapter provides a practical way for a website or service to expose an agent-accessible interface while integrating with the Agentic Trust Foundation and, where applicable, Agent-Pay.

The project is intentionally broader than a browser extension. The implementation may include SDKs, web components, server-side adapters, APIs, metadata, and other integration tools.

## Core principle

Installing or receiving an official adapter does **not** by itself mean that a website is trusted.

Trust and authorization require explicit evidence such as authenticated identity, origin/domain binding, capability declarations, credential verification, policy evaluation, and lifecycle/revocation controls.

## Relationship to the ecosystem

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
     Agent Commerce
          |
          v
      Agent-Pay
```

## Intended scope

Potential capabilities:
- site/service identity binding
- agent-facing discovery
- capability declaration
- authenticated requests
- consent hooks
- transaction initiation
- product/service APIs
- SDKs and web components
- integration validation
- versioning and revocation

## Non-goals

This project is not:
- a centralized trust registry
- a replacement for ATF
- a payment processor
- a merchant marketplace
- proof that every integrated site is trustworthy
- a frozen browser-extension-only architecture

## Status

Architecture phases 0–8 are complete. Phase 9 conformance and the Phase 10 semantic reference implementation baseline are complete.

The current implementation is intentionally profile-neutral: final credential serialization, manifest wire format, discovery endpoints, cryptographic suite, and transport profile remain open until the normative interoperability profile is frozen.

Run the reference tests with:

~~~bash
python -m pip install -e '.[test]'
pytest
~~~

See `docs/architecture/boundary.md` and `docs/roadmap/v1.md`.
