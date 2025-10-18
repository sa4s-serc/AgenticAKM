---
### ADR-004: AngularJS Single Page Application for Web Frontend

**Status:** Inferred
**Context:** To provide a rich, responsive, and interactive user experience for browsing a music library, a traditional multi-page web application architecture would be slow and cumbersome. A more fluid, desktop-like interface was required.
**Decision:** The web client is implemented as a Single Page Application (SPA) using the AngularJS (v1.x) framework. The file structure under `music-web/src/main/webapp/src/app` shows a typical AngularJS application with controllers, services, directives, and filters. Libraries like `angular.js`, `angular.ui-router.js`, and `angular.restangular.js` confirm this choice. The frontend build process is managed by Grunt (`Gruntfile.js`).
**Consequences:**
*   **Positive:**
    *   Provides a fast and fluid user experience after the initial load, as navigation and interactions don't require full page reloads.
    *   Enforces a strong separation of concerns between the frontend (presentation) and the backend (data/API).
*   **Negative:**
    *   AngularJS (v1.x) is now a legacy framework, which makes it difficult to maintain, find developers for, and leverage modern web development practices.
    *   SPAs can have a longer initial load time and can be more complex to optimize for search engines (though less of a concern for this type of application).