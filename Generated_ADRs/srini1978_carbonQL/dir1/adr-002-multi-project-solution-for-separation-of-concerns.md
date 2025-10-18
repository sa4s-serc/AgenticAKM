---
### ADR-002: Multi-Project Solution for Separation of Concerns

**Status:** Inferred
**Context:** The application's architecture needed to be organized to promote maintainability, reusability, and a clear separation of concerns. A monolithic, single-project structure could lead to tightly coupled code that is difficult to test and evolve.
**Decision:** The system is structured as a multi-project .NET solution (`carbonQL.sln`). The core business logic is encapsulated in a dedicated backend project (`carbonQLBackend`), while the user-facing entry point is a separate console application (`carbonQLConsole`). The presence of `carbonQLBackend.dll` in the console project's output directory (`carbonQLConsole/bin/Debug/net7.0/`) confirms that the console application depends on the backend project.
**Consequences:**
*   **Positive:**
    *   **Modularity:** The core logic in `carbonQLBackend` is decoupled from its presentation/execution layer, meaning it can be reused by other frontends (e.g., a web API or GUI) in the future.
    *   **Maintainability:** Changes to the user interface (the console app) are less likely to break the core business logic, and vice versa.
    *   **Testability:** The backend library can be unit-tested in isolation from the console application.
*   **Negative:**
    *   Introduces a slightly higher complexity in terms of project management and build configuration compared to a single-project solution.