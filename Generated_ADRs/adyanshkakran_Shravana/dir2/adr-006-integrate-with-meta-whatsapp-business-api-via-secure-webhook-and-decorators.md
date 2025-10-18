---
### ADR-006: Integrate with Meta WhatsApp Business API via secure webhook and decorators

Status: Inferred
Context: The repository includes meta/webhook.py, meta/utils.py, and meta/decorators/security.py, suggesting webhook verification and request validation logic specific to the Meta platform.
Decision: Use Meta’s webhook flow with custom security decorators to validate signatures/challenges and sanitize inputs.
Consequences:
- Positive: Standards-compliant integration; centralized security logic via decorators; easier auditing and testing.
- Negative: Additional complexity to maintain platform-specific security logic; breaking changes require close tracking of Meta API updates.