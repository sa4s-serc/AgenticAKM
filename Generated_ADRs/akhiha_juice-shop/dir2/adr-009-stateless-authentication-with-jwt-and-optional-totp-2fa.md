---
### ADR-009: Stateless authentication with JWT and optional TOTP 2FA

Status: Inferred
Context: encryptionkeys/jwt.pub exists; routes include login, verify, and 2fa; jwt-related advisories present in CSAF.
Decision: Use JWT for stateless authentication, with support for TOTP-based two-factor authentication.
Consequences:
- Positive: Scales well across instances; easy integration with SPA; 2FA strengthens security posture.
- Negative: Key management is critical; token misuse is a risk; adds flows and UX steps to manage 2FA.