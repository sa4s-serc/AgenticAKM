---
### ADR-012: Use environment-based configuration with dotenv and nodemon for backend development

Status: Inferred
Context: Server dependencies include dotenv and nodemon, and there is a dev script using nodemon.
Decision: Configure the server through environment variables loaded by dotenv; use nodemon for hot-reload in development.
Consequences:
- Positive: Secure, 12-factor friendly configuration; faster backend iterations.
- Negative: Must manage env files securely; differences between local and production envs can cause drift.