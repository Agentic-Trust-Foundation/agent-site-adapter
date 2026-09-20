# Production Security Baseline V1

The reference implementation is semantic and profile-neutral. A production adapter must add concrete controls.

## Required
- real cryptographic verification
- issuer/audience/resource binding
- revocation/status checks
- key rotation
- secure secret storage
- SSRF-safe metadata retrieval
- strict TLS validation
- replay protection
- idempotency
- rate limiting
- abuse controls
- structured redacted audit
- privacy/data minimization

## Negative requirements
Never:
- infer trust from adapter installation
- infer authority from authentication
- treat capability declarations as permission
- accept expired/revoked/unknown evidence
- let consent create authority
- broaden delegated authority
- follow arbitrary metadata URLs

## Operational controls
- bounded metadata cache
- allowlisted schemes/hosts where deployment policy requires it
- outbound egress restrictions
- request size/time limits
- circuit breakers
- security alerts for repeated verification failures
