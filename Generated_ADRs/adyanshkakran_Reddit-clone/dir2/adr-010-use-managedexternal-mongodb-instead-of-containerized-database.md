---
### ADR-010: Use managed/external MongoDB instead of containerized database

Status: Inferred
Context: Mongoose is used, but docker-compose does not define a MongoDB service, implying reliance on an external/managed instance (e.g., MongoDB Atlas or a local external instance).
Decision: Do not containerize MongoDB in the compose stack; connect to an external MongoDB instance configured via environment variables (dotenv is present).
Consequences:
- Positive: Reduces local stack complexity; mirrors production if using managed DB; avoids stateful container management.
- Negative: Requires network access to the DB; more setup for new developers; potential latency vs local containerized DB.