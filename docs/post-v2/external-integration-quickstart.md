# Post-V2 External Integration Quickstart

This guide is an ecosystem integration surface, not a new protocol version.

## Canonical V2 baseline

- ATF V2 FINAL / Phase 42:
  `afb9fc7c7d7115ef9d2e156baf57331f93d44f48`
- Agent-Pay V2 FINAL / Phase 43:
  `534b6a2021914d90d19485dc370eedb437ea9dba`

Use exact revisions in integration evidence. Do not rely on a moving `main` reference for certification evidence.

## Integration sequence

1. Identify the agent principal and trust domain.
2. Obtain and validate ATF authority evidence.
3. Apply the bounded delegation and authorization result.
4. Select the Site Adapter profile for the target interaction.
5. If a financial action is requested, pass the verified authority context to Agent-Pay.
6. Let Agent-Pay apply financial policy, approval, instrument and provider controls.
7. Record an auditable result and retain the exact protocol/profile revisions.

## External implementation rule

An external implementation MUST NOT infer authority from UI state, an adapter being installed, or a payment request alone.

The adapter applies service-interaction semantics; ATF remains authoritative for trust/authority semantics and Agent-Pay remains authoritative for financial controls.

## Evidence required for an independent integration

Record:

- implementation name and version;
- ATF commit;
- Agent-Pay commit, when applicable;
- Site Adapter commit/profile;
- selected profile identifiers;
- conformance vector set;
- test results;
- deployment environment identifier;
- evidence bundle digest.

A profile can be integrated without creating a new repository. A new repository is appropriate only when the integration is independently deployable and has its own lifecycle.

## Important status boundary

This document does not claim independent adoption or production deployment. Those claims require external-maintainer and target-environment evidence respectively.
