# Site Adapter V2 — Federation, Reputation, Delegation

## Federation
The adapter may consume federation metadata to understand protocol compatibility and trust relationships. Authorization remains request-specific.

## Reputation
Reputation and assurance are metadata/evidence. They are never permission by themselves.

## Agent-to-agent delegation
Each delegated hop carries evidence identifying the delegator, delegate, audience, scope, constraints, expiry, and parent evidence. A hop may only attenuate authority.

## Privacy
Where possible, implementations should transmit only the claims necessary for the current authorization decision.
