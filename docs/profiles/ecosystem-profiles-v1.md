# Ecosystem Integration Profiles V1

## Purpose

Site Adapter does not replace existing agent/service protocols. This document defines how their semantics fit into Site Adapter.

## Commerce

Commerce implementations MAY use UCP or another established commerce protocol. The Site Adapter commerce profile requires:
- merchant/service identity binding;
- capability declaration;
- quote/cart/checkout resource binding;
- deterministic lifecycle;
- idempotency for state-changing completion;
- user escalation where the commerce protocol requires trusted UI;
- Agent-Pay handoff before financial execution when Agent-Pay is used.

UCP remains authoritative for UCP checkout objects, bindings, transports and versioning.

## Booking

A booking profile MUST bind:
- provider/service identity;
- inventory or availability resource;
- booking intent;
- traveler/customer principal;
- dates/time zone;
- price/currency when payment is involved;
- cancellation/refund policy reference;
- idempotency key.

Final booking execution requires the service's authorization decision and, when financial, Agent-Pay controls.

## SaaS/API

The service exposes capabilities as API operations. OAuth-family authentication is preferred where applicable. Each operation is authorized against an ATF authority and resource/audience binding.

API schemas remain owned by the service or adopted protocol; Site Adapter does not duplicate them.

## Enterprise

Enterprise profiles MAY add organization/tenant, workload identity, mTLS, private network and policy-engine requirements. Local enterprise controls may further restrict authority but MUST NOT expand it.

## Healthcare

Healthcare profiles MUST treat clinical/patient data as high-sensitivity. They require deployment-specific identity, purpose, consent, minimum-necessary data access, audit and retention controls. Site Adapter does not define clinical authorization or regulatory compliance.

## Cloud/infrastructure

Cloud profiles bind:
- account/project/subscription;
- resource identifier;
- operation;
- environment;
- requested change;
- expiration;
- approval requirements.

Infrastructure adapters MUST fail closed on ambiguous resource scope and MUST support strong replay/idempotency controls for mutating operations.

## Agent-to-agent / service-to-service

A2A or another agent protocol MAY provide transport/task semantics. Site Adapter still requires distinct service/agent identity, authenticated principal, capability selection, bounded authority, request correlation and result evidence.

The external agent protocol remains authoritative for its own task/message wire format.
