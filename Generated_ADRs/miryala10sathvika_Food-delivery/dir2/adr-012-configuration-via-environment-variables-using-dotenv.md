---
### ADR-012: Configuration via environment variables using dotenv

Status: Inferred
Context: dotenv dependency; config/db.js; presence of mongodbatlaspass.txt suggests external connection strings.
Decision: Manage secrets and environment-specific settings (e.g., DB URI, Stripe keys, JWT secret) via environment variables loaded with dotenv.
Consequences:
- Positive: Twelve-Factor alignment; easy per-environment configuration; no secrets in source.
- Negative: Requires secure secret management in CI/CD; local env parity and .env hygiene are important.