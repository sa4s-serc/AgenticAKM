---
### ADR-003: Layered Structure for the Backend Logic

**Status:** Inferred
**Context:** The `carbonQLBackend` project required an internal structure to organize its code effectively. A clear pattern was needed to separate data representation from the business logic that operates on that data.
**Decision:** A layered architectural pattern was adopted within the backend project. This is inferred from the directory structure, which includes a `Model` folder for data structures (`EtsyModels.cs`) and a `Controller` folder for business logic (`EtsyCalculations.cs`). This separates the domain entities (Models) from the application logic that orchestrates calculations (Controllers).
**Consequences:**
*   **Positive:**
    *   **Clarity:** The code organization is intuitive and follows established software design patterns, making it easier for developers to understand the system's design.
    *   **Scalability:** This separation allows for the independent evolution of data models and business rules. New calculations can be added to the `Controller` layer without necessarily changing the core `Model` definitions.
    *   **Domain Focus:** The file names (`EtsyModels.cs`, `EtsyCalculations.cs`) clearly indicate that the application's domain is focused on calculations related to Etsy.
*   **Negative:**
    *   For a very simple application, this level of separation could be considered minor over-engineering.
    *   The use of the term "Controller" might be slightly unconventional for a class library if not part of an API, but it effectively communicates its role in controlling application flow and logic.