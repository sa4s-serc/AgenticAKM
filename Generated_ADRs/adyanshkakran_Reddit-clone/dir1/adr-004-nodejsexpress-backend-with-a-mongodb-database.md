---
### ADR-004: Node.js/Express Backend with a MongoDB Database

**Status:** Inferred
**Context:** The backend API requires a runtime and framework to handle HTTP requests, business logic, and data persistence. The database choice needs to support the application's data model, which may evolve during development.
**Decision:** The backend is built on the Node.js runtime using the Express.js framework. For data persistence, MongoDB was chosen as the database, indicated by the `mongoose` dependency in the `backend/package.json`. Mongoose is used as the Object Data Modeling (ODM) library to interact with MongoDB.
**Consequences:**
*   **Positive:**
    *   Node.js's non-blocking I/O model is well-suited for building efficient, I/O-bound API services.
    *   Using JavaScript/TypeScript across the full stack can streamline development.
    *   MongoDB's flexible schema is advantageous for rapid prototyping and applications with evolving data structures.
    *   The large `npm` ecosystem provides ready-made libraries for common tasks like authentication (`jsonwebtoken`, `bcrypt`) and file uploads (`multer`).
*   **Negative:**
    *   MongoDB is not ideal for highly relational data that requires complex joins and transactions.
    *   As a single-threaded environment, Node.js is not well-suited for long-running, CPU-intensive tasks.