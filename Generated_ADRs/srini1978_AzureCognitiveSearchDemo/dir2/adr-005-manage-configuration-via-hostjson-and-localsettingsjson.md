---
### ADR-005: Manage configuration via host.json and local.settings.json

**Status:** Inferred
**Context:** The project contains host.json and local.settings.json, implying environment-specific configuration and secret management needs (e.g., API keys, endpoints).
**Decision:** Use local.settings.json for local development settings and host.json for function runtime configuration, with the expectation of environment variables/app settings in deployed environments.
**Consequences:** 
- Positive: Clear separation of local vs. production configuration; standard Azure Functions practices; simplifies local testing.
- Negative: Risk if sensitive values are accidentally committed; requires secure management of app settings in production.