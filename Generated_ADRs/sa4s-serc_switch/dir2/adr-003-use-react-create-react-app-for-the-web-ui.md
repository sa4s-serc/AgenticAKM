---
### ADR-003: Use React (Create React App) for the web UI

Status: Inferred
Context: The UI source under src/ and package.json scripts indicate a Create React App setup using react-scripts with dependencies like react-router-dom and axios.
Decision: Implement the frontend as a single-page application using React, served by the CRA development server in a Node container on port 3000.
Consequences:
- Positive: Fast local development, hot reloading, familiar tooling; minimal server configuration.
- Negative: CRA dev server is not production-grade; server-side rendering is not provided; separate production build/serve path needed.