### ADR-001: Serverless Architecture with Firebase Platform

**Status:** Inferred

**Context:** The project, an e-commerce application clone, required a full-stack solution encompassing a user-facing web client, backend business logic, and hosting infrastructure. The architectural challenge was to choose a platform that could support these needs while minimizing operational overhead, enabling rapid development, and providing scalable infrastructure without manual server management.

**Decision:** The project adopted a serverless architecture built entirely on the Google Firebase platform. This includes:
1.  **Firebase Hosting:** To deploy and serve the static assets of the frontend Single-Page Application (SPA).
2.  **Firebase Cloud Functions:** To run backend logic in a managed, event-driven Node.js environment.

Evidence for this is found in the presence of `.firebaserc`, `firebase.json`, and the separate `functions/` directory with its own `package.json` specifying `"firebase-functions"` and `"firebase-admin"`.

**Consequences:**
*   **Positive:**
    *   **Reduced Operational Overhead:** No need to provision, manage, or patch servers.
    *   **Scalability:** The infrastructure scales automatically with user traffic.
    *   **Integrated Ecosystem:** Firebase provides a cohesive environment for hosting, backend functions, and potentially other services like authentication and databases.
    *   **Cost-Effective:** The pay-per-use model can be cheaper for applications with variable or low traffic compared to maintaining an always-on server.
*   **Negative:**
    *   **Vendor Lock-in:** The architecture is tightly coupled to the Google Cloud/Firebase ecosystem, making migration to another provider difficult.
    *   **Cold Starts:** Cloud Functions may experience latency on their first invocation after a period of inactivity, which can impact user experience.
    *   **Execution Limits:** Cloud Functions have constraints on execution time and resources, which may not be suitable for long-running processes.