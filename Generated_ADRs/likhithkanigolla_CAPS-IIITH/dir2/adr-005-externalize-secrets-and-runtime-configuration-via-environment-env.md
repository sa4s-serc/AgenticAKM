---
### ADR-005: Externalize secrets and runtime configuration via environment (.env)

Status: Inferred
Context: python-dotenv is a dependency; an APIKEY file is present; .gitignore exists to avoid leaking secrets.
Decision: Load credentials and configuration from environment variables/.env files rather than hard-coding.
Consequences:
- Positive: Improved security practices; easier environment-specific configuration.
- Negative: Additional setup for users; runtime failures if env is misconfigured.