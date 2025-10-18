---
### ADR-002: Asynchronous I/O via an Event Loop

**Status:** Inferred

**Context:** As a network service, the exporter must efficiently handle multiple concurrent network connections. These include incoming metric scrape requests from Prometheus, administrative connections, and potentially other I/O operations. A traditional thread-per-connection model would be resource-intensive and would not scale well, which is unacceptable for a lightweight monitoring agent.

**Decision:** The application uses an **event-driven architecture based on the `libev` library**. This is evidenced by the presence of `cmake/FindLibev.cmake` and the need for `libev-devel` in the Dockerfile.

**Consequences:**
*   **Positive:**
    *   **High Concurrency:** The event loop model allows the application to handle thousands of concurrent connections with a small, fixed number of threads (often just one), leading to very low memory usage.
    *   **Efficiency:** The application consumes CPU resources only when there is work to be done (e.g., an incoming request), avoiding the overhead of thread context switching.
    *   **Scalability:** The architecture scales well with the number of connections without a proportional increase in resource consumption.
*   **Negative:**
    *   **Programming Model:** Asynchronous, callback-based programming can be more complex to reason about and debug than simple, synchronous code. This can lead to "callback hell" if not managed carefully.
    *   **Blocking Operations:** Any long-running or blocking operation within an event handler will block the entire event loop, making the application unresponsive. All I/O must be non-blocking.