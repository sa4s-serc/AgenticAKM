---
### ADR-010: Centralize configuration via environment variables and .env files

Status: Inferred
Context: Multiple services include python-dotenv/dotenv; bootstrap scripts exist for environment setup; API gateway also includes load_dotenv.
Decision: Externalize configuration using environment variables, loaded via .env files in development.
Consequences:
- Positive: Aligns with 12-factor principles; easy environment-specific configuration.
- Negative: Risk of leaking secrets in .env; requires secret management hardening for production.