# Site Adapter Architecture Boundary

## Ownership

Site Adapter owns practical integration mechanics.

ATF owns trust, identity, delegation, authorization, consent, and revocation semantics.

Agent-Pay owns financial controls and payment execution.

## Trust model

The adapter may provide a standardized integration and evidence surface, but adapter possession is not equivalent to trust.

A future trust flow should establish at minimum:

1. site/service identity
2. domain/origin binding
3. authenticated key or credential binding
4. declared capabilities
5. protocol/version compatibility
6. lifecycle and revocation state
7. applicable ATF authorization policy

## Generic integration

The adapter must not assume e-commerce only.

Target service categories include:
- e-commerce
- booking
- travel
- SaaS
- APIs
- enterprise services
- healthcare services
- financial services
- infrastructure/cloud services

## Browser extension question

A browser extension may be one implementation of the adapter, but the architecture must not depend on browser execution.

The same integration model should be usable by:
- server-side applications
- APIs
- JavaScript SDKs
- web components
- mobile applications
- agent gateways

## Frozen vs open

Not yet frozen:
- exact metadata format
- exact credential format
- extension packaging
- discovery endpoint names
- capability wire format
- language-specific SDKs

These must be decided after requirements and interoperability research.
