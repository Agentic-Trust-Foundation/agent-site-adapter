# Consent and Authorization Boundary

**Status:** Architecture baseline — draft

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

The authorization question is contextual:

> Is this principal/agent allowed to perform this specific action on this resource under the applicable delegation, policy, and validity constraints?

## 3. Consent

Consent represents the required human decision or approval event when policy requires it.

Consent may be:

- pre-authorized
- interactive
- step-up
- transaction-specific
- capability-specific

The exact models remain open.

## 4. Human approval rule

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

## 5. Adapter responsibility

The Site Adapter may provide the integration hooks needed to:

- request consent
- present required context
- redirect to an approval surface
- receive an approval result
- bind the result to the operation

It must not define itself as the final authority for cross-system authorization.

## 6. Agent-Pay boundary

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

## 7. Auditability

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
