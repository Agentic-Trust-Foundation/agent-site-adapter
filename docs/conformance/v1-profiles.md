# V1 Profile Conformance

## Required profile behavior

Every profile implementation MUST:
- advertise its exact profile identifier;
- reject incompatible major versions;
- authenticate before authorization;
- bind authority to subject and audience/resource;
- enforce capability/action/resource constraints;
- preserve request correlation;
- use idempotency for non-idempotent operations;
- fail closed on required indeterminate security evidence.

## Profile matrix

| Profile | Discovery | Auth | Domain semantics | Financial handoff |
|---|---|---|---|---|
| Web HTTP | HTTPS metadata | deployment-selected | generic resource/action | optional |
| OAuth HTTP | OAuth metadata | OAuth | API/resource | optional |
| MCP | MCP server metadata + selected auth | MCP + selected auth | tool/resource | optional |
| A2A | Agent Card | A2A-selected auth | task/service | optional |
| Commerce | service manifest + native commerce discovery | selected profile | catalog/checkout/order | Agent-Pay where used |
| Booking | service manifest | selected profile | availability/booking | Agent-Pay where used |
| SaaS/API | service manifest/API metadata | OAuth/mTLS/etc. | API operations | optional |
| Enterprise | service manifest | enterprise profile | tenant/resource | optional |
| Healthcare | service manifest | deployment-specific | patient/service/purpose | optional |
| Cloud | service manifest/provider metadata | strong provider auth | account/resource/change | optional |
| Agent-Pay | Site Adapter handoff | authenticated caller | financial intent | required |

## External protocol rule

MCP, A2A, UCP, OAuth and payment protocols retain authority over their native message formats. Site Adapter conformance tests the boundary semantics around them rather than cloning their schemas.
