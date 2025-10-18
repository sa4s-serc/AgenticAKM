---
### ADR-003: Backend Technology Stack based on Node.js and Express

**Status:** Inferred
**Context:** The backend needed a runtime and framework capable of building a RESTful API, handling user authentication, connecting to a database, and integrating with external AI services. The choice would impact performance, development speed, and scalability.
**Decision:** The backend is built on the Node.js runtime using the Express.js web framework. This is confirmed by the `express` dependency and the `start`: `node index.js` script in the `server/package.json`. The code is structured into routes, controllers, and models, indicating a layered API architecture.
**Consequences:**
*   **Positive:** Node.js's non-blocking, event-driven architecture is highly efficient for I/O-bound operations common in web APIs (e.g., database queries, third-party API calls). Using JavaScript (with ES Modules, as seen by `"type": "module"`) on the backend allows for potential code sharing and a unified language across the full stack. Express.js is a mature, minimalist, and highly extensible framework with a vast ecosystem of middleware.
*   **Negative:** Being single-threaded, Node.js is not ideal for CPU-intensive tasks without additional strategies like using worker threads. Managing asynchronous code can be complex if not handled carefully with modern async/await patterns.