---
### ADR-011: Configuration via environment variables and dotenv

Status: Inferred
Context: Presence of example.env and python-dotenv indicates environment-driven configuration for secrets and environment-specific settings.
Decision: Manage configuration through environment variables loaded via dotenv in development.
Consequences:
- Positive: Twelve-Factor-friendly; easy separation of secrets from code; straightforward local dev setup.
- Negative: Requires secret management discipline in production; risk if .env files are mishandled.