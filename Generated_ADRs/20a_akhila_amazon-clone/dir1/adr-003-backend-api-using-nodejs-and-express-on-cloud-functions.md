---
### ADR-003: Backend API using Node.js and Express on Cloud Functions

**Status:** Inferred

**Context:** The frontend client requires a secure backend to handle sensitive operations that cannot be performed in the browser. This primarily includes processing payments, which requires secret API keys and server-side validation. A structured and recognizable API pattern was needed to handle these requests.

**Decision:** The backend API is implemented using Node.js and the Express.js framework, deployed as a collection of Firebase Cloud Functions.

The `functions/package.json` file confirms this by listing `firebase-functions`, `express`, and `cors` as dependencies. The use of Express suggests that the functions are likely exposed as a structured set of HTTP endpoints, creating a familiar REST-like API layer on top of the serverless functions.

**Consequences:**
*   **Positive:**
    *   **Language Consistency:** Using JavaScript (Node.js) on the backend allows for a consistent language and skillset across the entire stack.
    *   **Structured API:** Express.js provides a robust and familiar framework for defining routes, middleware, and handling HTTP requests and responses, making the API more organized than standalone functions.
    *   **Secure Operations:** Business logic involving secrets (like the Stripe API key) is securely isolated from the client application.
*   **Negative:**
    *   **Increased Complexity:** Adding Express introduces another layer of abstraction over the base Cloud Functions, which can add minor complexity and overhead.
    *   **Stateless by Design:** Serverless functions are stateless, meaning any state (like user sessions) must be managed externally, typically in a database or via tokens.