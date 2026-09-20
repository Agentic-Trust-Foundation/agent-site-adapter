# Request Lifecycle

**Status:** Architecture baseline — draft

## 1. End-to-end lifecycle

~~~text
Discovery
   ↓
Identity / Origin Verification
   ↓
Protocol Compatibility
   ↓
Agent Authentication
   ↓
Capability Selection
   ↓
Authority Evidence
   ↓
Authorization + Consent
   ↓
[Financial?] ── yes ──> Agent-Pay Controls
   |                         ↓
   |                    Payment Outcome
   |                         |
   +<------------------------+
   ↓
Site Execution
   ↓
Result + Evidence
   ↓
Audit / Lifecycle Handling
~~~

## 2. Discovery

The agent learns that a service exposes an agent-accessible interface.

Discovery is not trust.

Discovery information must be treated as untrusted until the applicable identity and authenticity checks succeed.

## 3. Identity verification

The requester and target service are identified according to their respective mechanisms.

The system verifies the binding required by the operation.

## 4. Authentication

The site authenticates the requesting agent/principal using a supported mechanism.

Authentication establishes identity or possession of authenticated credentials. It does not itself establish authorization.

## 5. Capability selection

The agent selects a declared capability and supplies the required inputs.

The service must validate that the requested operation actually corresponds to the declared capability.

## 6. Authority and consent

Applicable ATF evidence and policy are evaluated.

Possible outcomes:

- ALLOW
- DENY
- REQUIRE_HUMAN

The adapter does not invent authority.

## 7. Financial handoff

If the requested operation has financial consequences, Agent-Pay evaluates financial policy and executes within the authority already established upstream.

Agent-Pay must not expand ATF authority.

## 8. Execution

The site performs only the operation that passed the applicable checks.

Any mismatch between the authorized operation and the requested execution must fail closed.

## 9. Result and evidence

The response should make it possible to distinguish:

- requested operation
- authorized operation
- executed operation
- result
- relevant identifiers/evidence
- failure reason where applicable

Exact response fields remain open.

## 10. Replay and idempotency

Operations with side effects must be evaluated for:

- replay resistance
- idempotency
- duplicate execution
- timeout/retry behavior
- partial failure
- reconciliation

These requirements become normative during protocol/security design.
