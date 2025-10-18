---
### ADR-003: Application Layering and Structure

**Status:** Inferred

**Context:** To ensure the application is maintainable, testable, and scalable, its internal structure needed to be organized logically. A pattern was required to separate distinct responsibilities such as handling web requests, executing business logic, and accessing the database.

**Decision:** The application is structured using a classic **3-Tier (Layered) Architecture**. This is evident from the package structure shown in the file list, which is clearly segregated into:
*   `controller`: Presentation Layer (e.g., `QuestionController`, `QuizController`) for handling HTTP requests.
*   `service`: Service/Business Logic Layer (e.g., `QuestionService`, `QuizService`) for orchestrating application logic.
*   `dao`: Data Access Layer (e.g., `QuestionDao`, `QuizDao`) for interacting with the database.
*   `model`: Domain objects (e.g., `Question`, `Quiz`) that represent the core data structures.

**Consequences:**
*   **Positive:**
    *   Promotes strong separation of concerns, making the codebase easier to understand, navigate, and maintain.
    *   Each layer can be developed, modified, and tested independently, improving modularity and testability.
    *   Provides a clear and well-understood pattern for developers to follow.
*   **Negative:**
    *   For very simple CRUD applications, this layered approach can introduce unnecessary boilerplate code and indirection.
    *   Requires careful management of data transfer between layers (e.g., using DTOs like `QuestionWrapper` and `QuizResponse`).