---
### ADR-003: Implement backend with Node.js, Express, and Mongoose

Status: Inferred
Context: The backend package.json depends on express and mongoose, with routes (login, user, post, greddit, report) and an Express app structure (bin/www.js, views, public).
Decision: Build the backend as an Express application with Mongoose for data access to MongoDB.
Consequences:
- Positive: Popular, well-supported stack; straightforward REST API development; Mongoose provides schemas and validation.
- Negative: Requires careful schema design to avoid coupling; runtime type safety limited without TypeScript on the server.