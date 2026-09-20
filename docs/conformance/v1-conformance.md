# Site Adapter V1 Conformance

**Status:** Phase 9 complete — semantic conformance baseline  
**Date:** 2026-09-21

## Purpose

Phase 9 converts the architecture contracts into executable negative and positive cases before implementation is expanded.

The suite tests security semantics rather than a frozen wire format.

## Required assertions

| Area | Required behavior |
|---|---|
| Authority presence | Missing authority fails closed |
| Subject | Agent/principal mismatch is denied |
| Audience | Cross-service authority is denied |
| Action | Capability/action mismatch is denied |
| Resource | Unauthorized resource is denied |
| Delegation | Invalid delegation is denied |
| Expiry/revocation | Stale or revoked authority is denied |
| Parameters | Amount/currency constraints are enforced |
| Consent | Consent is bound to request material |
| Human approval | Approval cannot manufacture authority |
| Human approval | Existing authority may produce REQUIRE_HUMAN |
| Replay/substitution | Mismatched consent is denied |
| Agent-Pay boundary | Downstream controls cannot expand upstream authority |
| Fail closed | Indeterminate required security evidence is not ALLOW |

## Phase 9 implementation

The current reference suite is intentionally small and dependency-light:

- tests/test_authorization.py
- semantic reason codes;
- deterministic test clock;
- positive and negative authorization cases.

The suite is not yet a complete interoperability matrix. Wire-format fixtures and cross-implementation tests belong to the later protocol/profile freeze.

## Conformance gate

Phase 10 may proceed because the core authorization semantics now have executable tests.

Future profiles must add fixtures for their concrete credential, manifest, transport, discovery, and interoperability requirements.
