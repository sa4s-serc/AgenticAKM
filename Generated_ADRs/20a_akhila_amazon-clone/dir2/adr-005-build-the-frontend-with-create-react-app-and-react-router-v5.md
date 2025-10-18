---
### ADR-005: Build the frontend with Create React App and React Router v5

Status: Inferred
Context: The root package.json uses react-scripts (CRA) and depends on react-router-dom ^5.3.0. CRA defaults are present (serviceWorker.js, index.js bootstrapping).
Decision: Scaffold the SPA with Create React App and client-side routing using React Router v5.
Consequences:
- Positive: Fast bootstrap, sensible defaults, stable React 17 stack, predictable dev/build scripts.
- Negative: Limited webpack customizations without ejecting; client-side routing requires hosting rewrites to index.html; upgrading to Router v6 later requires migration.