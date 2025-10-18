---
### ADR-003: Node.js and Express.js for the Backend API

**Status:** Inferred

**Context:** A backend framework was needed to build a RESTful API for handling HTTP requests, routing, middleware, and communication with the database. The choice needed to be performant for I/O-bound operations and have a large ecosystem for extensibility.

**Decision:** The backend is built on the Node.js runtime using the Express.js framework. This is evident from the `backend/package.json` file listing `express` as a dependency and the file structure (`routes`, `controllers`, `middleware`) which is characteristic of an Express application.

**Consequences:**
*   **Positive:**
    *   Allows for using JavaScript across the entire stack, which can improve developer productivity.
    *   Express.js is lightweight and flexible, with a vast ecosystem of middleware for handling tasks like parsing (`body-parser`), authentication, and file uploads (`multer`).
    *   Node.js's non-blocking, event-driven architecture is highly efficient for data-intensive APIs that perform many I/O operations (like database queries).
*   **Negative:**
    *   The unopinionated nature of Express.js requires developers to define and enforce their own application structure.
    *   Being single-threaded, Node.js is not well-suited for CPU-intensive tasks, which would block the event loop and degrade performance.