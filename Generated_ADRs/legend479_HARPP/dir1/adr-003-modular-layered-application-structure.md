---
### ADR-003: Modular, Layered Application Structure

**Status:** Inferred
**Context:** To manage complexity and improve maintainability, the application's code needed to be organized logically. A monolithic script would be difficult to test, debug, and extend. The challenge was to define clear boundaries between different aspects of the application.
**Decision:** The application is structured into distinct modules based on their primary responsibility. This is evident from the file structure within the `src/` directory:
*   `window.py`: Manages the user interface (View).
*   `shapes.py`, `object.py`, `group.py`: Define the core domain logic and data structures (Model).
*   `export.py`: Handles data serialization/persistence.
*   `main.py`: Acts as the application entry point, orchestrating the different components.
**Consequences:**
*   **Positive:** This separation of concerns improves code readability and maintainability. It allows developers to work on different parts of the application (e.g., UI vs. shape logic) independently. The dedicated `tests/` directory and `test_shapes.py` file show that this modularity makes the core logic easier to unit test in isolation.
*   **Negative:** This approach introduces some overhead in managing dependencies between modules (e.g., imports). Maintaining strict boundaries requires developer discipline.