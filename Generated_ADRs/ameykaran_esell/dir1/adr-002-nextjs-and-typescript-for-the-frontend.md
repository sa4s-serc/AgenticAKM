---
### ADR-002: Next.js and TypeScript for the Frontend

**Status:** Inferred
**Context:** The application needs a modern, responsive, and interactive web interface to handle features like chat, PDF viewing, and displaying generated media. Maintainability and developer productivity are key concerns.
**Decision:** The frontend is built using the Next.js framework on top of React. TypeScript is used as the primary programming language, and TailwindCSS is used for styling. This is evidenced by `next.config.ts`, `package.json` dependencies (`next`, `react`, `typescript`, `tailwindcss`), and the `.tsx` file extensions.
**Consequences:**
*   **Positive:**
    *   **Rich User Experience:** React's component model allows for building complex, stateful UIs like `ChatInterface.tsx` and `PdfReader.tsx`.
    *   **Performance:** Next.js provides performance optimizations like server-side rendering and static site generation, which can lead to faster initial page loads.
    *   **Type Safety:** TypeScript reduces runtime errors and improves code quality and developer confidence during refactoring.
    *   **Rapid Styling:** TailwindCSS enables rapid UI development with a utility-first approach.
*   **Negative:**
    *   The complexity of the Next.js framework can be overkill for very simple applications.
    *   There is a dependency on the Node.js ecosystem and its associated tooling (`pnpm`, `eslint`).