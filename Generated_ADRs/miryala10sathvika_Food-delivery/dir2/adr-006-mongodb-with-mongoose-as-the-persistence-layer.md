---
### ADR-006: MongoDB with Mongoose as the persistence layer

Status: Inferred
Context: mongoose ^8.x and mongodb driver present; models for food, order, user; config/db.js exists.
Decision: Use MongoDB with Mongoose ODM for schema modeling and queries.
Consequences:
- Positive: Rapid development with schemas, hooks, validation; good fit for document data (menus, carts, orders).
- Negative: ODM abstraction can hide driver nuances; schema migrations and indexing need explicit handling; vendor lock-in to MongoDB.