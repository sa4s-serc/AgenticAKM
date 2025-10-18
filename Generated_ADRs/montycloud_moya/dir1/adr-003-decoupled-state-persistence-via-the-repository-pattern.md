---
### ADR-003: Decoupled State Persistence via the Repository Pattern

**Status:** Inferred
**Context:** The framework needs to manage state, particularly conversation history (as implied by `moya/conversation/thread.py` and `message.py`). The required persistence mechanism can vary significantly based on the deployment environment. An in-memory solution is ideal for testing and simple scripts, while a file-based or database solution is necessary for production or stateful applications. Coupling the application logic directly to a specific storage method would make it difficult to test and adapt.

**Decision:** Abstract the data storage and retrieval logic using the Repository Pattern. A generic `Repository` interface is defined in `moya/memory/repository.py`. Concrete implementations are provided for different backing stores, such as `InMemoryRepository` and `FileSystemRepo`. The rest of the application interacts with the repository through the common interface, remaining agnostic to the underlying storage technology.

**Consequences:**
*   **Positive:**
    *   **Improved Testability:** The application can be tested using the fast and dependency-free `InMemoryRepository` without needing to set up a file system or database.
    *   **Flexibility:** The persistence layer can be swapped out easily. It is straightforward to add new repositories (e.g., for a SQL database, Redis, etc.) as the need arises.
    *   **Clean Architecture:** The core business logic is isolated from the data access infrastructure, leading to a cleaner and more maintainable codebase.
*   **Negative:**
    *   **Layer of Indirection:** For very simple applications that only ever need one type of storage, the abstraction adds boilerplate and an extra layer of complexity.
    *   **"Leaky" Abstraction:** The generic repository interface might not be able to accommodate performance optimizations or special features unique to a specific database technology.