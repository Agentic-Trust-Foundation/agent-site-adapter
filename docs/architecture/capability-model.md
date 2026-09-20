# Capability Model

**Status:** Architecture baseline — draft

## 1. Purpose

A capability describes an operation that a site or service exposes to agents.

Capabilities are not the same as permissions.

- A **capability** says what a service can do.
- An **authority decision** says whether a particular agent/principal may invoke it.

## 2. Capability structure

Conceptually:

~~~text
Capability
  ├── identifier
  ├── operation/action
  ├── resource or resource class
  ├── input requirements
  ├── output/result shape
  ├── side effects
  ├── sensitivity/risk class
  ├── consent requirements
  ├── protocol/profile version
  └── lifecycle state
~~~

This is not yet a frozen serialization.

## 3. Capability categories

The model should support at least:

- discovery/read
- search/query
- availability
- create
- update
- cancel
- booking
- purchase/order
- account operations
- enterprise/API operations
- infrastructure operations

Financial capabilities should be identifiable so that Agent-Pay controls can be invoked when required.

## 4. Capability declaration requirements

A declaration should make it possible for an agent to determine:

1. what operation exists
2. what resource it affects
3. what inputs are required
4. what side effects can occur
5. what authority/consent may be required
6. whether payment may be involved
7. which version/profile governs the operation

Ambiguity in a capability declaration must not be interpreted as broader authority.

## 5. Capability vs authority

~~~text
Site declares capability
        ↓
Agent requests action
        ↓
ATF evaluates authority
        ↓
Policy/consent requirements
        ↓
Execution
~~~

A site cannot grant an agent authority merely by declaring a capability.

Likewise, an agent cannot assume that possessing a credential means every site capability is permitted.

## 6. Versioning

Capabilities must be versionable independently enough to allow compatibility checks without coupling implementation package versions to protocol semantics.

Exact compatibility rules remain open.
