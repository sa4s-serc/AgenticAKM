---
### ADR-002: TypeScript-based Stack with Node.js and Angular

**Status:** Inferred
**Context:** The project required a technology stack that is modern, maintainable, and suitable for building a complex, interactive web application. The choice of language and frameworks for both the server and the client side is a foundational architectural decision.
**Decision:** The application is built using a consistent language, TypeScript, across the entire stack.
*   **Backend:** A Node.js application, evidenced by `package.json`, `server.ts`, and `app.ts`. The file structure in `routes/` and `models/` is typical of an Express.js-based REST API.
*   **Frontend:** A Single-Page Application (SPA) built with the Angular framework, confirmed by the presence of `frontend/angular.json`, `frontend/package.json` with `@angular/*` dependencies, and the component-based structure within `frontend/src/app`.
**Consequences:**
*   **Positive:**
    *   TypeScript's static typing improves code quality, maintainability, and developer productivity by catching errors during compilation rather than at runtime.
    *   Using a single language reduces the cognitive load for developers working on both the frontend and backend.
    *   Node.js offers a performant, event-driven runtime suitable for I/O-heavy web applications.
    *   Angular provides a powerful and structured framework for building a feature-rich and scalable user interface.
*   **Negative:**
    *   Requires developers to be proficient in TypeScript, Node.js, and the Angular ecosystem.
    *   The initial setup and build configuration (`tsconfig.json`, `angular.json`) can be complex.