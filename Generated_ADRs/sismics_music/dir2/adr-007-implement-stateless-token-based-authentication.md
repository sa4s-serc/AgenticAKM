---
### ADR-007: Implement stateless token-based authentication

Status: Inferred
Context: music-web-common includes TokenBasedSecurityFilter; music-core has AuthenticationToken DAO/model; no mention of container sessions; Android app and web clients call REST endpoints.
Decision: Authenticate API calls using application-issued tokens persisted in the database and enforced via a servlet/Jersey filter.
Consequences:
- Positive: Stateless scaling across instances; suitable for non-browser and mobile clients; avoids server-side HTTP sessions.
- Negative: Token lifecycle/rotation/revocation must be implemented; secure storage and transport required; risk surface if tokens leak.