# Site Adapter → Agent-Pay Integration Profile V1

**Identifier:** `site-adapter/agent-pay/1`

**Status:** Normative V1

## Purpose

This profile defines the boundary from an authorized Site Adapter operation to Agent-Pay. It does not define a payment rail or payment credential format.

## Preconditions

Site Adapter MUST establish:
- authenticated agent/principal;
- service identity and audience binding;
- requested capability/action;
- target resource;
- valid ATF authority evidence;
- applicable consent/approval evidence;
- financial parameters.

If any required evidence is missing, invalid, expired, revoked or indeterminate, the handoff MUST NOT be ALLOW.

## Financial intent

The handoff MUST bind:
- `request_id`;
- `idempotency_key`;
- `agent_id`;
- `service_id`;
- `authority_evidence_id`;
- `authorization_context_hash`;
- `action`;
- `resource`;
- `amount`;
- `currency`;
- `recipient/payee` when known;
- `expires_at`;
- `approval_requirement`.

The authorization context hash MUST cover every security-sensitive value whose substitution could change the authorized transaction.

## Non-expansion invariant

Agent-Pay MAY:
- reject the operation;
- reduce the permitted amount;
- require additional approval;
- impose provider/account/policy restrictions;
- delay or fail execution.

Agent-Pay MUST NOT:
- broaden the ATF authority;
- replace the authorized subject with another principal;
- change the authorized audience/resource;
- increase the authorized amount;
- substitute a different payee without a fresh authorization decision;
- treat UI approval alone as authority.

## Approval

If Site Adapter returns `REQUIRE_HUMAN`, Agent-Pay MUST preserve the same authorization context while collecting approval. Approval attaches to the existing intent; it does not create authority.

Approval correlation MUST use the same request/transaction identity and authorization context hash.

## Lifecycle

`AUTHORIZED → HANDED_OFF → POLICY_EVALUATED → APPROVAL_PENDING? → EXECUTION_PENDING → EXECUTED | REJECTED | FAILED`

Retries MUST preserve the original idempotency key for the same logical operation.

## Result evidence

Agent-Pay returns:
- transaction/intent identifier;
- final outcome;
- authorization context hash;
- provider result reference where applicable;
- timestamps;
- machine-readable error code on failure.

The Site Adapter MUST NOT interpret a payment success as proof of broader service authorization.

## Provider neutrality

This profile does not standardize cards, PSPs, banks, wallets, settlement rails or country-specific payment providers. Those remain Agent-Pay responsibilities.
