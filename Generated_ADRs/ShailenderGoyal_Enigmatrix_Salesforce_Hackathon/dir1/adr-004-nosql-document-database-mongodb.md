---
### ADR-004: NoSQL Document Database (MongoDB)

**Status:** Inferred
**Context:** The application requires a database to store varied and potentially evolving data structures, including user profiles, learning materials, chat sessions (`chatMessage.model.js`), and user notes (`note.model.js`). The choice of database needed to align with the backend technology and development philosophy.
**Decision:** A NoSQL document database, MongoDB, was selected as the primary data store. This decision is strongly inferred from the use of the `mongoose` library in the server's `package.json`, which is the most popular Object Data Modeling (ODM) library for MongoDB in the Node.js ecosystem.
**Consequences:**
*   **Positive:** MongoDB's flexible, schema-less nature is well-suited for rapid development and evolving application requirements. Storing data in JSON-like documents maps naturally to JavaScript objects, simplifying development with Node.js. It scales horizontally well for large datasets.
*   **Negative:** It lacks the rigid transactional guarantees and relational integrity (e.g., foreign key constraints) of traditional SQL databases. This responsibility is shifted to the application layer. Performing complex queries with joins across different collections is less straightforward than in SQL.