---
### ADR-002: Use Vite + React 18 + TypeScript for the frontend

Status: Inferred
Context: The frontend uses Vite (vite.config.ts), React 18, and TypeScript (tsconfig*.json). Rapid iteration and modern tooling are suited to a highly interactive learning assistant UI.
Decision: Build the SPA with Vite bundler, React 18, and TypeScript.
Consequences:
- Positive: Fast dev server and HMR, modern ESM build, strong typing, improved DX.
- Negative: Requires TypeScript maintenance; ecosystem differences from CRA/Next.js may require custom integrations.