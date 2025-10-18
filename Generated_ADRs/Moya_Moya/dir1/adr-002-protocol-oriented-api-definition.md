---
### ADR-002: Protocol-Oriented API Definition

**Status:** Inferred

**Context:** Defining network API endpoints often involves managing numerous details: base URL, path, HTTP method, parameters, headers, and body data. Using simple string-based or dictionary-based approaches can be error-prone, lack type safety, and lead to scattered, hard-to-maintain API definitions. The architectural challenge was to create a type-safe, declarative, and organized way to define API endpoints.

**Decision:** The library's core abstraction is the `TargetType` protocol. Instead of creating request objects directly, developers create an enumeration (or any other type) that conforms to this protocol. Each case of the enum represents a specific API endpoint. The protocol requires implementers to provide all the necessary components of a network request (e.g., `baseURL`, `path`, `method`, `task` for parameters/body). This approach collocates all information for a group of related endpoints into a single, well-defined type.

**Consequences:**
*   **Positive:**
    *   **Type Safety:** The compiler ensures that all required components of a network request are provided for each endpoint, reducing runtime errors.
    *   **Improved Readability and Maintainability:** API definitions are centralized and self-documenting. It's easy to see all available endpoints and their configurations at a glance.
    *   **Enhanced Testability:** Mock implementations of `TargetType` can be easily created for unit testing without making actual network calls.
    *   **Compile-Time Discovery:** Adding, removing, or changing an endpoint often results in a compile-time error if usages are not updated, which is safer than runtime failures.
*   **Negative:**
    *   **Initial Learning Curve:** Developers new to the library must learn the protocol-oriented approach instead of a more traditional request-building pattern.
    *   **Boilerplate:** For very simple APIs, creating a type that conforms to `TargetType` might feel like more boilerplate than a one-off request function.