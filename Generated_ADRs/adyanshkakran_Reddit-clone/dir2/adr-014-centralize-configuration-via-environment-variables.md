---
### ADR-014: Centralize configuration via environment variables

Status: Inferred
Context: Backend includes dotenv; no hardcoded DB container; typical pattern is to configure secrets/URIs via env.
Decision: Use environment variables (12-factor style) for configuration such as database credentials, JWT secrets, and host/port settings.
Consequences:
- Positive: Separation of config from code; easier environment promotion; safer secret handling (with proper process).
- Negative: Requires management of env files or secret stores; misconfiguration can be hard to diagnose across multiple services.