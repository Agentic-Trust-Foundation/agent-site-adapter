# Authorization, Consent, and Delegation Model

**Status:** Phase 6 architecture contract  
**Date:** 2026-09-21

## 1. Purpose

Phase 6 defines how the Site Adapter consumes authority established by ATF, evaluates that authority against a concrete service capability and request, handles consent, and hands financially consequential operations to Agent-Pay.

The Site Adapter is an enforcement/integration point. It does not become a new cross-domain authority issuer.

The core rule is:

~~~text
ATF establishes authority
        ↓
Site Adapter binds authority to service + capability + request
        ↓
Authorization decision
        ↓
Consent if required
        ↓
Agent-Pay if financial
        ↓
Service execution
~~~

## 2. Authority versus capability

A capability describes what a Service Entity can do.

Authority describes what a principal or agent is permitted to do.

~~~text
Capability = service-side possibility
Authority   = principal-side permission
Authorization = contextual intersection
~~~

A request is eligible only when the requested operation is both:
1. exposed by an active compatible capability; and
2. within the authority available to the authenticated principal/agent.

Capability discovery never grants authority.

## 3. Authorization inputs

A security-sensitive authorization decision should consider, as applicable:

- authenticated agent/principal;
- user principal where relevant;
- service identity;
- service origin/endpoint binding;
- requested capability and capability version;
- operation/action;
- target resource/resource class;
- request parameters;
- authority/delegation evidence;
- authority issuer/trust domain;
- audience/resource binding;
- temporal validity;
- credential/evidence lifecycle state;
- revocation/status;
- delegation constraints;
- applicable policy;
- consent requirement and consent evidence;
- protocol/profile compatibility;
- financial intent where applicable.

Missing, invalid, expired, revoked, inconsistent, or indeterminate required evidence fails closed.

## 4. Contextual authorization

Authorization is not a boolean property of an agent.

The relevant question is:

> Is this principal authorized to perform this specific action on this specific resource, with these parameters, at this time, under the applicable delegation and policy?

A principal may be authorized for one capability or resource and denied for another.

## 5. Capability-to-authority matching

Authorization evaluation should establish an explicit match across:

~~~text
Authenticated principal
        ↕
Authority subject / delegate
        ↕
Requested capability
        ↕
Action / operation
        ↕
Resource / resource class
        ↕
Parameter constraints
        ↕
Time / lifecycle
        ↕
Service / audience / resource binding
~~~

Broad permission must not be inferred from a narrower permission.

Examples:

- order.create does not imply order.cancel.
- Read authority does not imply write authority.
- Authority for Service A does not imply authority for Service B.
- Authority for one account/resource does not imply authority for another.
- A monetary limit does not imply permission to pay an unauthorized recipient.
- A capability declaration does not compensate for missing authority.

## 6. Delegation

Delegation allows one principal to authorize another principal to act within bounded authority.

The Site Adapter consumes the resulting delegation evidence; it does not invent or extend the delegation chain.

A valid delegation chain must satisfy:

~~~text
Delegator authority
      ≥
Delegated authority
      ≥
Requested authority
~~~

Therefore:

- a delegate cannot grant more authority than the delegator possesses;
- delegation must remain within applicable service/resource boundaries;
- delegation must preserve relevant action, resource, parameter, and temporal constraints;
- an expired/revoked/invalid delegation cannot authorize execution;
- an ambiguous delegation chain fails closed.

Delegation depth, credential representation, and exact chain serialization remain profile-specific until a normative ATF profile defines them.

## 7. Authority attenuation

Delegation may narrow authority but must not silently broaden it.

A downstream operation may apply additional constraints:

~~~text
Upstream ATF authority
        ↓
Site/service constraints
        ↓
Capability constraints
        ↓
Request-specific constraints
        ↓
Effective authority
~~~

The effective authority is the intersection of applicable constraints, not their union.

A downstream component must not remove a security-relevant restriction merely because another component requested it.

## 8. Audience, resource, and service binding

Authority evidence must be usable for the intended security context.

Where applicable, verification must bind authority to:

- intended service/resource;
- service identity/origin;
- authenticated principal;
- requested capability/action;
- relevant resource;
- validity period;
- applicable protocol/profile.

Authority valid for one service must not automatically authorize an equivalent-looking operation at another service.

This prevents cross-service confused-deputy and credential-substitution attacks.

## 9. Parameter binding

Authorization must cover the operation that is actually executed.

Security-sensitive parameters must therefore be bound to the authorization decision or revalidated against its constraints.

Examples:

- amount;
- currency;
- recipient;
- account;
- product/service identifier;
- quantity;
- booking date;
- infrastructure target;
- data scope.

If a protected parameter changes after authorization, the adapter must re-evaluate authorization or reject the request.

## 10. Consent

Consent is evidence of a required human decision. It is not a replacement for authority.

The correct relationship is:

~~~text
Existing authority
       +
Policy requires human consent
       ↓
Human reviews the requested operation
       ↓
Consent bound to that operation
       ↓
ALLOW
~~~

Not:

~~~text
No authority
       ↓
Human approves
       ↓
Authority is created
~~~

Consent may be:

- pre-authorized;
- interactive;
- step-up;
- transaction-specific;
- capability-specific;
- policy-triggered.

The selected consent model is profile/deployment-specific.

## 11. Consent binding

For a security-sensitive operation, consent evidence should be bound to the material facts the user approved, including where applicable:

- principal/agent;
- service;
- capability/action;
- resource;
- security-sensitive parameters;
- financial intent;
- policy decision;
- consent timestamp;
- validity/expiry;
- correlation/request identifier;
- consent state.

A consent event for one operation must not be replayed as approval for a materially different operation.

Changes to materially approved parameters require re-consent or a new authorization decision when policy requires it.

Fine-grained authorization requests can use established mechanisms such as OAuth Rich Authorization Requests (RFC 9396) in an applicable profile; Site Adapter does not redefine that standard.

## 12. Authorization outcomes

The architecture uses three semantic outcomes:

~~~text
ALLOW
DENY
REQUIRE_HUMAN
~~~

### ALLOW

All mandatory authority, authentication, capability, policy, lifecycle, and consent requirements are satisfied.

### DENY

A required security or policy condition is not satisfied and the request must not execute.

Examples include insufficient authority, wrong resource, expired delegation, revoked evidence, unsupported capability, parameter mismatch, or failed policy.

### REQUIRE_HUMAN

The governing policy explicitly permits a human decision to complete the authorization workflow, and the underlying authority is already sufficient for the requested operation.

REQUIRE_HUMAN must not be used to bypass missing authority.

## 13. Human approval boundary

Human approval is a policy mechanism, not an authority issuer.

A human approval system may:
- satisfy a policy-required approval step;
- approve or reject a request within existing authority;
- require step-up authentication;
- bind a decision to a transaction/request.

It must not:
- create an otherwise nonexistent principal authority;
- expand a delegation chain;
- remove an ATF restriction;
- authorize a resource outside the delegator's authority;
- convert an invalid or revoked credential into valid authority.

## 14. Revocation and lifecycle

Authorization must account for authority lifecycle.

At minimum, protected operations must distinguish:

- active/valid;
- expired;
- revoked;
- suspended/blocked where the profile defines it;
- replaced;
- unknown/indeterminate.

Unknown lifecycle state must not be treated as active for security-sensitive authorization.

Where policy requires current status, a stale cached decision must not silently override a newer revocation.

## 15. Agent-Pay handoff

Financial operations cross into Agent-Pay only after Site Adapter authorization has established that the agent/principal is authorized for the requested financial capability.

~~~text
ATF authority
      ↓
Site Adapter authorization
      ↓
Financial intent + authorized constraints
      ↓
Agent-Pay financial policy
      ↓
Human approval if Agent-Pay policy requires it
      ↓
Payment execution
~~~

Agent-Pay may:
- apply budgets;
- apply spending limits;
- reserve funds;
- require financial approval;
- select payment instruments;
- execute and reconcile transactions.

Agent-Pay must not:
- manufacture ATF authority;
- broaden the authorized recipient/resource;
- raise an authorized amount beyond upstream authority;
- remove ATF restrictions;
- treat its own approval as general authorization.

The effective financial permission is the intersection of upstream authority and Agent-Pay financial policy.

## 16. Cross-domain authorization

Independent trust domains may establish different policies and evidence requirements.

Cross-domain authorization requires explicit interoperability and trust relationships.

The Site Adapter must not infer:

- common ownership;
- common software;
- common adapter;
- common protocol;
- common domain naming

as sufficient proof of authority.

## 17. Fail-closed rules

The following must fail closed for protected operations:

- missing authority evidence;
- invalid authority evidence;
- expired authority;
- revoked authority;
- invalid delegation chain;
- wrong audience/resource;
- principal mismatch;
- capability mismatch;
- operation/resource mismatch;
- parameter constraint violation;
- unknown security-critical extension;
- indeterminate required lifecycle status;
- invalid or unbound consent evidence.

Business-level uncertainty may produce a recoverable error. Security evidence uncertainty must not silently become ALLOW.

## 18. Evidence and audit correlation

A conforming implementation should be able to correlate:

~~~text
request
  ↕
principal/agent
  ↕
service
  ↕
capability
  ↕
authority/delegation evidence
  ↕
authorization decision
  ↕
consent decision
  ↕
Agent-Pay decision (if applicable)
  ↕
execution
  ↕
result/outcome
~~~

Correlation identifiers are evidence-management aids; they are not authority by themselves.

## 19. Wire-format boundary

This phase defines semantics, not one universal credential or consent wire format.

The following remain profile-specific/open unless a later normative profile freezes them:

- authority credential serialization;
- delegation-chain serialization;
- consent artifact format;
- exact authorization API;
- policy language;
- status/revocation protocol;
- cryptographic suite;
- token claims;
- transport details.

Established standards should be reused where they fit instead of creating parallel mechanisms.

## 20. Security properties required from future implementations

Implementations must prevent at least:

- privilege escalation through delegation;
- confused deputy across services;
- parameter substitution after approval;
- consent substitution/replay;
- authority/identity mix-up;
- capability-as-authority confusion;
- financial approval becoming general authorization;
- stale/revoked authority being accepted;
- cross-domain authority leakage;
- silent security downgrade.

## 21. Next gate

Phase 9 will turn these semantics into conformance cases covering:

- capability/authority matching;
- delegation attenuation;
- audience/resource binding;
- parameter integrity;
- consent binding;
- REQUIRE_HUMAN;
- revocation/fail-closed behavior;
- Agent-Pay non-expansion;
- replay and duplicate decision handling;
- version/profile compatibility.
