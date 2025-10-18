---
### ADR-002: Monolithic Web Application with Python and Flask

**Status:** Inferred
**Context:** The project needed a web framework to build the core functionality of the cab-sharing application, including handling HTTP requests, managing business logic, and rendering user interfaces.
**Decision:** A monolithic application architecture was chosen, using the Python Flask framework. The file structure with a central `app.py`, along with `templates/` and `static/` directories, and the inclusion of `Flask` in `requirements.txt`, points to a single codebase responsible for both backend logic and server-side rendering of HTML.
**Consequences:**
*   **Positive:**
    *   Simplicity in development and deployment, as the entire application is a single unit.
    *   Flask's lightweight nature allows for rapid development and easy setup.
    *   Low initial complexity, making it easy for a small team to understand and manage the entire codebase.
*   **Negative:**
    *   The codebase can become tightly coupled and difficult to maintain as the application grows.
    *   Scaling different parts of the application independently (e.g., user management vs. booking service) is not possible.
    *   Refactoring or adopting new technologies can be challenging for the entire application at once.