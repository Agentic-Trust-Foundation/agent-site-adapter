# Request Lifecycle and Error Semantics

**Status:** Architecture contract — Phase 7  
**Date:** 2026-09-21

## Processing stages

~~~text
1. Discover
2. Verify service identity/binding
3. Verify protocol/security compatibility
4. Authenticate agent
5. Select capability
6. Validate request parameters
7. Verify authority/delegation
8. Evaluate authorization
9. Obtain/verify consent if required
10. If financial, evaluate Agent-Pay controls
11. Execute
12. Record result/evidence
13. Apply lifecycle/audit handling
~~~

A stage must not be skipped merely because an earlier stage succeeded.

## Request context

A protected request should be correlatable to, as applicable:

- request identifier;
- service identity;
- agent principal;
- user principal where relevant;
- capability identifier/version;
- resource;
- operation;
- parameters;
- authority evidence;
- consent evidence;
- financial intent/evidence;
- protocol/profile version;
- freshness/expiry data.

Exact field names remain open.

## Correlation

Security-relevant downstream events should be correlatable without relying solely on timestamps. Correlation identifiers are not proof of authority.

## Replay and idempotency

Side-effecting operations require appropriate controls for duplicate requests, retry, timeout, network ambiguity, client restart, provider retry, and captured-request replay.

An idempotency key is not a substitute for authorization or authentication.

## Parameter integrity

Authorization and consent must cover the operation actually executed. If a security-sensitive parameter changes after authorization, the request must be revalidated or rejected.

Examples include amount, currency, destination, quantity, account, booking date, and infrastructure target.

## Timeout and ambiguous outcome

If execution times out after the request may have reached the service, the client must not assume failure merely because no response was received. A status/reconciliation mechanism should exist where duplicate execution would be harmful.

## Partial failure

The protocol/profile must distinguish at least:

- not started;
- accepted;
- in progress;
- completed;
- failed;
- partially completed;
- outcome unknown.

Concrete state machines remain profile-specific.

## Structured error classes

Conceptual semantic classes:

~~~text
IDENTITY_ERROR
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
CONSENT_REQUIRED
CONSENT_ERROR
CAPABILITY_ERROR
PROTOCOL_VERSION_ERROR
REQUEST_VALIDATION_ERROR
REPLAY_ERROR
IDEMPOTENCY_CONFLICT
POLICY_ERROR
EXECUTION_ERROR
TIMEOUT
OUTCOME_UNKNOWN
TEMPORARY_UNAVAILABLE
~~~

These are semantic classes, not frozen wire error codes.

## Error disclosure

Errors should support legitimate recovery without disclosing credentials, cryptographic secrets, internal authorization policy, private resource existence where sensitive, or security signals that create an attacker oracle.

## Retry

Retries must be classified as safe, conditionally safe, or unsafe. A retry must not bypass changed authorization, expired consent, or a new policy decision.

## Financial operations

Financial execution must use Agent-Pay transaction/idempotency controls where the operation crosses the financial boundary.

~~~text
Agent request
   ↓
ATF authority
   ↓
Agent-Pay financial decision
   ↓
Payment transaction
   ↓
Service result
~~~

## Result evidence

Where applicable, result evidence should correlate requested operation, authorized operation, executed operation, service result, provider/transaction identifier, final state, timestamp, and relevant lifecycle status.

## Fail-closed security rule

Missing, invalid, expired, revoked, inconsistent, or indeterminate required security evidence must not be treated as successful verification. Business errors may be recoverable; security failures must not silently degrade into execution.

## Next gate

Phase 8 will define version negotiation, compatibility, extension, deprecation, and downgrade rules.
