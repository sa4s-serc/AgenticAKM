---
### ADR-002: Modern Frontend Development with Vite

**Status:** Inferred
**Context:** The project required a modern JavaScript build system and development server. Key requirements included support for ES Modules, efficient asset handling, a fast development feedback loop (Hot Module Replacement), and an optimized production build process. Traditional bundlers could introduce configuration complexity and slower development server start-up times.
**Decision:** **Vite** was chosen as the project's build tool and development server. This is explicitly declared in the `devDependencies` of `package.json` and is the tool used to run the `dev`, `build`, and `preview` scripts.
**Consequences:**
*   **Positive:** Vite provides an extremely fast development experience due to its native ESM-based dev server. It offers a simpler configuration out-of-the-box compared to alternatives like Webpack. It handles TypeScript, JSX, CSS, and other common web assets with minimal setup.
*   **Negative:** The development server relies on native ES module support, which means it does not support very old, legacy browsers. The plugin ecosystem, while robust, may be less extensive than that of more established bundlers like Webpack for certain edge cases.