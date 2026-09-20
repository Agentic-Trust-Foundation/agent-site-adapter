# Integration Boundaries

**Status:** Architecture baseline — draft

## 1. ATF boundary

ATF owns:

- identity semantics
- delegation
- authorization
- trust semantics
- consent semantics
- revocation
- provenance/accountability

Site Adapter consumes these semantics; it does not replace them.

## 2. Site Adapter boundary

Site Adapter owns:

- site/service integration mechanics
- agent-facing service surface
- capability exposure
- discovery/integration metadata
- request mapping
- adapter lifecycle/versioning
- SDK/component implementations

It does not own global trust or payment execution.

## 3. Agent-Pay boundary

Agent-Pay owns:

- financial policy
- budgets/reservations
- approval workflow for financial policy
- payment instruments/routing
- transaction lifecycle
- ledger/journal
- provider operations
- settlement/reconciliation

It consumes authority evidence and does not expand it.

## 4. Agent-Pay Iran boundary

Agent-Pay Iran owns local product/deployment concerns:

- local providers and rails
- local authentication
- local settlement
- local UX
- local notifications
- local operational and compliance requirements

It must consume Agent-Pay rather than silently fork its normative semantics.

## 5. Boundary invariant

The following must remain true:

~~~text
Service capability != agent authority
Agent authentication != authorization
Adapter installation != trust
Human approval != authority creation
ATF authority != financial permission
Agent-Pay financial approval != general authorization
~~~

## 6. Change classification

Any proposed feature must first be classified as:

1. ATF protocol
2. Agent-Pay protocol
3. Site Adapter protocol/integration
4. Agent-Pay Iran product/deployment
5. documentation/research

If classification is unclear, architecture work comes before implementation.
