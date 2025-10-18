---
### ADR-003: RESTful API for Service Exposure

**Status:** Inferred
**Context:** The application needs to expose its functionality and data to external clients (such as a web front-end or other services) over the network in a standardized, language-agnostic way.
**Decision:** A RESTful API has been implemented using the JAX-RS standard. The inclusion of the `com.sun.jersey` dependency, which is a JAX-RS implementation, strongly indicates this choice. The `jettison` dependency further suggests that JSON is a primary data format for the API.
**Consequences:**
*   **Positive:**
    *   Creates a decoupled architecture where the client and server can evolve independently.
    *   Leverages the ubiquity of HTTP, making the API widely accessible from virtually any platform or language.
    *   Statelessness improves scalability and reliability.
*   **Negative:**
    *   Requires careful design of resources and endpoints to maintain a clean and intuitive API.