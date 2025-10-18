---
### ADR-003: Monolithic Frontend Architecture

**Status:** Inferred
**Context:** The overall application architecture needed to be defined. For a web application, this involves deciding whether to build a Multi-Page Application (MPA), a Single-Page Application (SPA), or a more complex distributed system like micro-frontends.
**Decision:** The application is structured as a single, monolithic frontend unit. The existence of a single `index.html` as the entry point suggests that the user loads this one page, which in turn loads all the necessary CSS and JavaScript to run the entire application. This is the simplest form of a static site or a Single-Page Application.
**Consequences:**
*   **Positive:**
    *   **Simplified Deployment:** The entire frontend can be deployed as a simple set of static assets to any web server or CDN.
    *   **Reduced Complexity:** There is no need for complex routing, orchestration, or communication protocols between different parts of the frontend.
    *   **Fast Initial Development:** Getting the application up and running is trivial with this simple, self-contained structure.
*   **Negative:**
    *   **Poor Scalability for Teams:** A monolithic structure makes it difficult for multiple teams to work on the application independently without creating conflicts.
    *   **Potential for Performance Bottlenecks:** As the application grows, the single `index.js` file could become very large, leading to long initial load and parse times, negatively impacting user experience.
    *   **Single Point of Failure:** An error in the single JavaScript bundle can potentially break the entire application.