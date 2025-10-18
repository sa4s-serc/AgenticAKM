---
### ADR-002: Use React + Vite for both SPAs

Status: Inferred
Context: admin and frontend use React 19 with Vite (vite.config.js present, @vitejs/plugin-react, React Router DOM).
Decision: Build SPAs with React and Vite for development and production builds.
Consequences:
- Positive: Fast HMR; modern tooling; small, optimized bundles; consistent developer experience across apps.
- Negative: Requires additional SSR/SEO work if needed later; two separate client codebases to maintain.