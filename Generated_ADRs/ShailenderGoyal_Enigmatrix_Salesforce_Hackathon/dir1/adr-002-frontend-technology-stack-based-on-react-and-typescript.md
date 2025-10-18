---
### ADR-002: Frontend Technology Stack based on React and TypeScript

**Status:** Inferred
**Context:** A modern, performant, and maintainable frontend is required to deliver a rich user experience for the learning platform. Key considerations included developer productivity, ecosystem support, and the ability to build complex, interactive user interfaces.
**Decision:** The frontend is a Single-Page Application built using React with TypeScript. The build and development environment is managed by Vite. This is evidenced by the `react`, `typescript`, `vite` dependencies in `learn-spark-ai-buddy/package.json` and the presence of `.tsx` and `vite.config.ts` files.
**Consequences:**
*   **Positive:** React's component-based architecture promotes UI reusability and modularity. TypeScript adds static type-checking, which enhances code quality, maintainability, and reduces runtime errors. Vite provides an extremely fast development server and optimized build process, improving developer experience. Client-side routing is handled by `react-router-dom`, enabling a fluid, app-like navigation experience.
*   **Negative:** As a Single-Page Application, initial page load may be slower than a server-rendered equivalent. Search Engine Optimization (SEO) requires additional effort. The technology stack has a learning curve for developers unfamiliar with React, TypeScript, and modern tooling.