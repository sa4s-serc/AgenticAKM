---
### ADR-002: Java-based Backend with a RESTful API

**Status:** Inferred
**Context:** The system required a robust, platform-agnostic backend to manage the music library, handle user data, and serve content to various clients (web, Android). A standardized communication protocol was necessary for this client-server interaction.
**Decision:** A Java-based backend was implemented to serve a RESTful API.
*   **Framework:** JAX-RS (Java API for RESTful Web Services), with Jersey as the chosen implementation. This is evident from the `org.glassfish.jersey.*` dependencies in `music-web/pom.xml`.
*   **Application Server:** The application is packaged as a `.war` file, designed to run in a servlet container. Standalone distributions and the Docker image utilize an embedded Jetty server.
*   **Real-time Communication:** The Atmosphere framework (`atmosphere-runtime` dependency) is used to provide real-time updates to clients, likely for features like player status synchronization, using WebSockets with fallbacks.
**Consequences:**
*   **Positive:**
    *   Leverages the mature, stable, and performant Java ecosystem.
    *   A RESTful API provides a clean, stateless, and well-understood contract between the server and its multiple clients.
    *   The choice of Jetty for standalone deployment makes the application lightweight and easy to run without a pre-configured server.
*   **Negative:**
    *   Java can be more verbose and have a larger memory footprint compared to other modern backend languages.
    *   The JAX-RS and Servlet API approach can involve more boilerplate code than more modern, opinionated frameworks.