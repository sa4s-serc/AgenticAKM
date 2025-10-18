---
### ADR-008: Manage Configuration via Environment Variables and .env Files

Status: Inferred
Context: docker-compose.yml references an .env file, and a .env.template is included, indicating environment-driven configuration.
Decision: Use environment variables sourced from a .env file for runtime configuration.
Consequences: Facilitates twelve-factor-style configuration and easy environment switching. Requires careful secret management to avoid committing credentials. Differences between local and production environments must be documented and managed consistently.