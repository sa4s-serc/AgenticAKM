---
### ADR-007: Build the frontend as a React SPA with TypeScript, Vite, and Tailwind CSS

Status: Inferred
Context: The frontend uses React 18, TypeScript, Vite, Tailwind, React Router v6, and Axios, with a Dockerfile running vite dev.
Decision: Use React with TypeScript and Vite for fast development/build, Tailwind CSS for styling, and React Router for SPA navigation.
Consequences:
- Positive: High developer productivity, type safety on the client, fast HMR, utility-first styling.
- Negative: Requires build tooling; Tailwind requires team familiarity; SPA routing needs server support for fallback routes.