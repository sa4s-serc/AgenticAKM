---
### ADR-002: Adoption of a Monolithic Script-Based Architecture

**Status:** Inferred
**Context:** For a new or simple project, a key architectural challenge is to choose a structure that minimizes complexity and overhead. A multi-file, package-based, or microservice architecture can be overly complex for a small-scale application. The goal was to have a simple, self-contained, and easily executable unit.
**Decision:** The entire application logic is consolidated into a single script file (`project.py`). This is a monolithic, script-based architecture.
**Consequences:**
*   **Positive:** The architecture is extremely simple to understand and maintain for a single developer or small project. The entire logic is in one place, reducing the cognitive load. The application can be run with a single command (e.g., `python project.py`), simplifying execution.
*   **Negative:** This model scales poorly. As the application grows, the single file can become large, difficult to navigate, and hard to test. It leads to tight coupling of components and poor separation of concerns, making future refactoring or feature additions challenging.