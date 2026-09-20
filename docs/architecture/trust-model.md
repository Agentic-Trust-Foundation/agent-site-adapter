# Trust Model

**Status:** Architecture baseline — draft

## 1. Fundamental rule

Adapter possession is not trust.

Installing an official adapter, receiving metadata from an adapter, or reaching a known domain does not by itself establish that a site is authorized, authentic, safe, or financially trustworthy.

Trust must be based on verifiable evidence and explicit policy.

## 2. Evidence categories

The architecture distinguishes at least these evidence categories:

1. **Service identity** — what service claims to be the target.
2. **Origin binding** — which domain/origin or service endpoint is bound to that identity.
3. **Key/credential binding** — what cryptographic or authenticated material represents the service.
4. **Capability declaration** — what operations the service exposes.
5. **Protocol compatibility** — which protocol/profile versions are supported.
6. **Lifecycle state** — whether relevant credentials, integrations, or capabilities are active or revoked.
7. **Authority evidence** — whether the requesting agent/principal has authority for the requested operation.
8. **Consent evidence** — whether required user consent or approval has occurred.

No single category should be treated as a substitute for all others.

## 3. Trust is contextual

The system must not produce one universal boolean such as "trusted=true" and use it for every decision.

A service may be:

- authenticated but not authorized for a requested operation
- identified but missing current capability evidence
- technically reachable but revoked
- authorized for read operations but not write operations
- authorized for a transaction but outside financial policy

Trust and authorization therefore remain contextual and policy-driven.

## 4. Trust domains

The architecture permits independent trust domains.

ATF does not need to become a global authority or registry.

A future implementation may support:

- organization trust domains
- enterprise trust domains
- provider-specific trust domains
- public interoperability profiles

Cross-domain trust must be explicit and verifiable rather than inferred from common software ownership.

## 5. Fail-closed rule

When required evidence is missing, invalid, expired, revoked, inconsistent, or indeterminate, the protected operation must not proceed.

The system may return a distinct REQUIRE_HUMAN outcome when the governing policy explicitly permits human intervention. Human approval must not create authority that the principal or agent did not already possess.

## 6. Security consequence

The adapter is a mechanism for presenting and consuming evidence.

It is not the authority that decides whether evidence is sufficient for every use case.
