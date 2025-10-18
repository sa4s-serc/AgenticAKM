---
### ADR-003: Client-Side Navigation

**Status:** Inferred
**Context:** As a Single-Page Application, the user must be able to navigate between different views (e.g., a home page, a movie detail page) without a full-page reload from the server. This requires a mechanism to map browser URLs to specific component views on the client side.
**Decision:** **React Router (`react-router-dom`)** will be used to handle all client-side routing. This is confirmed by its inclusion as a dependency in `package.json`. The existence of different "page" components like `Home.js`, `Movie.js`, and `NotFound.js` strongly implies a multi-view application managed by a router.
**Consequences:**
*   **Positive:**
    *   **Improved User Experience:** Provides a fast, app-like feel by avoiding full-page reloads during navigation.
    *   **Declarative Routing:** Routes can be defined declaratively alongside the component structure, which fits well with the React paradigm.
    *   **Standardized Solution:** React Router is the de-facto standard for routing in the React ecosystem, with extensive documentation and community support.
*   **Negative:**
    *   **State Management Complexity:** Managing application state across different routes can become more complex.
    *   **SEO Considerations:** Requires specific techniques (like server-side rendering or pre-rendering) to ensure optimal search engine optimization, which may not be configured by default in a simple CRA setup.