# System Architecture Overview

**Status:** Architecture baseline — draft  
**Scope:** Site/service integration layer for the agentic internet

## 1. Purpose

Agent Site Adapter is the integration layer between an agent and an online site or service.

It gives a site a defined agent-facing surface without making the adapter itself a trust authority, authorization engine, payment processor, or centralized registry.

The architecture is deliberately protocol-first and implementation-neutral. Browser extensions, SDKs, server-side adapters, APIs, web components, and agent gateways are implementation choices.

## 2. Layered model

~~~text
                         AGENTIC INTERNET
                                |
             +------------------+------------------+
             |                                     |
             v                                     v
        Agent / Principal                    Site / Service
             |                                     |
             |                              Site Adapter
             |                                     |
             +---------------+---------------------+
                             |
                             v
                    Authenticated Request
                             |
                             v
                    ATF Authority Check
                             |
                 +-----------+-----------+
                 |                       |
               ALLOW              REQUIRE_HUMAN
                 |                       |
                 +-----------+-----------+
                             |
                             v
                     Site Capability
                             |
                             v
                       Service Action
                             |
                    financial action?
                       /           \
                     no             yes
                     |               |
                     |               v
                     |          Agent-Pay
                     |               |
                     +-------+-------+
                             |
                             v
                        Outcome / Evidence
~~~

This diagram describes responsibilities, not a frozen wire protocol.

## 3. Core actors

### Agent

Requests an operation on behalf of a principal.

The adapter must not infer authority merely because a request originates from an agent.

### Principal / User

The party whose authority, consent, account, or delegated control may be involved.

### Site / Service

The real service provider exposing capabilities.

### Site Adapter

Binds the service to an agent-accessible integration surface. It exposes identity metadata, capabilities, protocol information, authentication mechanisms, and lifecycle state as defined by the eventual protocol.

### ATF

Provides trust, identity, delegation, authorization, consent, and revocation semantics.

### Agent-Pay

Evaluates financial policy and executes payment operations after upstream authority is established.

## 4. Request processing principle

Every meaningful operation follows this conceptual sequence:

1. Discover the service and its supported integration profile.
2. Establish or verify site/service identity and origin binding.
3. Establish request/agent authentication.
4. Identify the requested capability and action.
5. Obtain and verify applicable authority evidence.
6. Evaluate authorization and consent requirements.
7. If the operation is financial, hand off financial controls to Agent-Pay.
8. Execute only the authorized operation.
9. Return the result and relevant evidence.
10. Preserve lifecycle, audit, and revocation semantics.

A later protocol specification may optimize or combine steps, but it must not silently remove their security meaning.

## 5. Non-goals

This architecture does not define:

- a centralized trust registry
- a universal agent credential format
- a universal site credential format
- a mandatory browser extension
- a payment rail
- a merchant marketplace
- a single discovery network
- a universal reputation score

## 6. Frozen vs open

Not frozen yet:

- wire format
- endpoint names
- credential serialization
- discovery mechanism
- capability serialization
- transport requirements
- cryptographic suite
- SDK API
- browser-extension packaging

These remain design inputs until the threat model and interoperability review are complete.
