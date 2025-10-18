### ADR-001: Plugin-Based Architecture for Extensibility

**Status:** Inferred

**Context:** A networking library often needs to handle cross-cutting concerns such as authentication, logging, and network activity indication. Hardcoding this logic into the core request pipeline would make the library inflexible and difficult to customize for different application needs. The challenge is to allow developers to inject custom behavior into the request/response lifecycle without modifying the core library code.

**Decision:** The architecture incorporates a "Plugin" system. A `Plugin` protocol is defined, allowing developers to create custom plugins that can intercept various points in the network request lifecycle (e.g., before sending a request, after receiving a response). The library provides several default plugins out-of-the-box, as seen in `Sources/Moya/Plugins/` (e.g., `AccessTokenPlugin`, `NetworkLoggerPlugin`, `CredentialsPlugin`). The `MoyaProvider` is initialized with an array of these plugins, which are then applied to every request it manages.

**Consequences:**
*   **Positive:**
    *   **High Extensibility:** Developers can easily add custom functionality like caching, specialized authentication schemes, or analytics tracking without forking the library.
    *   **Separation of Concerns:** Core networking logic is decoupled from peripheral concerns like logging or UI updates.
    *   **Reusability:** Plugins can be packaged and reused across different projects or API targets.
    *   **Testability:** The core provider and the plugins can be tested in isolation.
*   **Negative:**
    *   **Increased Complexity:** Developers using the library must understand the plugin lifecycle and how plugins interact with each other.
    *   **Potential for Misuse:** Poorly written plugins could negatively impact performance or introduce unexpected side effects (e.g., blocking the calling thread).