---
### ADR-002: Use Vite for development server and build tooling

Status: Inferred
Context: The project needs a fast local dev server and build pipeline for a client-side web app. package.json scripts (dev, build, preview) target vite, and the repo structure follows Vite conventions (src for code, public for static assets).
Decision: Adopt Vite@^4.1.0 as the dev/build tool with ES modules.
Consequences:
- Positive: Very fast HMR, lean configuration, first-class ES module support, and simple static asset handling via the public directory.
- Negative: Some tooling/plugins may require ESM compatibility; bundling very large static assets is still network-bound and outside Vite’s optimization unless further configured.