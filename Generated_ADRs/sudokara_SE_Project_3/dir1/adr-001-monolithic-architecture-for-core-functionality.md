### ADR-001: Monolithic Architecture for Core Functionality

**Status:** Inferred
**Context:** When starting a new project, a fundamental decision is the overall architectural style. The choice between a monolithic, microservices, or other distributed architecture impacts development speed, deployment complexity, and scalability. The challenge was to select a style that would allow for rapid initial development and a cohesive codebase for a file backup utility.
**Decision:** The project adopted a monolithic architecture. All core functionalities—file system observation, compression, encryption, and uploading—are developed and bundled together within a single application codebase, located under the `src/phoenix` directory. This decision is explicitly documented in `docs/ADRs/Monolith.md`.
**Consequences:**
*   **Positive:**
    *   **Simplified Development:** A single codebase makes it easier to manage dependencies, share utility code (e.g., `src/phoenix/utils`), and perform refactoring.
    *   **Simplified Deployment:** The entire application can be packaged and deployed as a single unit.
    *   **Easier Debugging:** Tracing the flow of execution across different components (e.g., from observation to uploading) is straightforward within a single process.
*   **Negative:**
    *   **Tight Coupling:** Modules might become tightly coupled over time, making it harder to modify or replace individual components.
    *   **Limited Scalability:** If one component, like encryption, becomes a bottleneck, the entire application must be scaled, which is less efficient than scaling a single service.
    *   **Technology Stack Rigidity:** The entire application is committed to a single technology stack (Python, in this case).