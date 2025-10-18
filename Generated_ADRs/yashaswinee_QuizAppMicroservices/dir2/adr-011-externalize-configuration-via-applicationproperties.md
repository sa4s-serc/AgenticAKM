---
### ADR-011: Externalize configuration via application.properties

Status: Inferred
Context: The application needs to configure datasource and other settings without changing code.
Decision: Use src/main/resources/application.properties to configure the application, including datasource properties for Postgres.
Consequences:
- Positive: Conventional Spring configuration; easy overrides via environment variables and profiles.
- Negative: Requires profile management for different environments (dev/test/prod) to avoid leaking dev credentials/settings.