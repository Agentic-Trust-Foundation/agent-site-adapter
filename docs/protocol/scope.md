# Site Adapter Protocol Scope

This document is a scope boundary, not yet a frozen wire specification.

## The adapter must answer

- What service is this?
- Which origin/domain is associated with it?
- Which capabilities does it expose?
- Which protocol versions does it support?
- How does an agent authenticate?
- What evidence can be verified?
- What requires user consent?
- What can be revoked?
- How are errors and unsupported capabilities represented?

## It must not silently answer

- Is this merchant financially trustworthy?
- Is this agent authorized to spend money?
- Is a user identity valid?
- May an agent perform an action outside its delegated authority?

Those decisions belong to the appropriate trust, authorization, or financial policy layer.

## Versioning

Any future normative protocol format must be versioned independently from implementation packages.

The first stable wire contract should only be frozen after security and interoperability review.
