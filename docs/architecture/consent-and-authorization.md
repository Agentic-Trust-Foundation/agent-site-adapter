# Consent and Authorization Boundary

**Status:** Phase 6 architecture contract  
**Date:** 2026-09-21

## 1. Separation of concerns

The architecture distinguishes:

- authentication
- authorization
- consent
- financial policy
- execution

They may interact, but none should silently substitute for another.

## 2. Authorization

ATF is responsible for the general authorization semantics.

Authorization is contextual: the decision must bind the authenticated principal to the requested capability, action, resource, relevant parameters, service/resource audience, validity, delegation constraints, and applicable policy.

The Site Adapter evaluates these semantics in the context of the Service Entity and request. It does not issue cross-domain authority.

The semantic outcomes are:

~~~text
ALLOW
DENY
REQUIRE_HUMAN
~~~


A missing, invalid, expired, revoked, inconsistent, or indeterminate required security condition fails closed.

## 2.1 Capability and authority

A capability describes what the service can do; authority describes what the principal may do.

A capability declaration is never an authorization grant.

Authorization requires an explicit match between the requested capability/action/resource/parameters and the available authority evidence.

ATF is responsible for the general authorization semantics.

The authorization question is contextual:

> Is this principal/agent allowed to perform this specific action on this resource under the applicable delegation, policy, and validity constraints?

## 3. Delegation

Delegation permits a principal to act within authority granted by another principal.

The Site Adapter consumes delegation evidence but must not extend it. Delegated authority must be no broader than the delegator's authority and must preserve applicable service, resource, action, parameter, and temporal constraints.

The effective authority is the intersection of upstream authority and downstream constraints.

Exact delegation credential and chain serialization remain profile-specific.

## 4. Consent

Consent represents the required human decision or approval event when policy requires it.

Consent may be:

- pre-authorized
- interactive
- step-up
- transaction-specific
- capability-specific

The exact models remain open.

## 5. Human approval rule

Human approval may satisfy a policy requirement when the underlying authority exists.

It must not manufacture authority that is absent.

~~~text
Existing authority + policy requires approval
             ↓
        Human approval
             ↓
          ALLOW
~~~

Not:

~~~text
No authority
     ↓
Human clicks approve
     ↓
Authority magically exists
~~~

## 6. Adapter responsibility

The Site Adapter may provide the integration hooks needed to:

- request consent
- present required context
- redirect to an approval surface
- receive an approval result
- bind the result to the operation

It must not define itself as the final authority for cross-system authorization.

## 7. Agent-Pay boundary

For financial operations:

~~~text
ATF authority
     ↓
Agent-Pay financial policy
     ↓
Human approval if required by financial policy
     ↓
Payment execution
~~~

Financial approval cannot enlarge the underlying ATF authority.

## 8. Auditability

A future implementation should be able to correlate:

- principal
- agent
- requested capability
- authorization evidence
- consent/approval event
- financial decision where applicable
- executed operation
- final outcome

Exact evidence schemas are deferred.
