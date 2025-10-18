---
### ADR-011: Encrypt secrets at rest using AES

Status: Inferred
Context: aes.c and security.c suggest encryption utilities, likely for protecting credentials in configuration.
Decision: Implement AES-based encryption for sensitive data (e.g., stored passwords) in configuration or state.
Consequences:
- Positive: Improves security posture; reduces risk of credential leakage from files.
- Negative: Key management complexity; potential user friction; must avoid insecure modes/usages.