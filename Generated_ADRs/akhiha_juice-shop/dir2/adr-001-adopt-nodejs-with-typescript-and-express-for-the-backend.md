### ADR-001: Adopt Node.js with TypeScript and Express for the backend

Status: Inferred
Context: The repository contains server.ts, app.ts, a routes/ folder, and tsconfig.json, indicating a TypeScript-based Node.js service with many REST endpoints. The project needs a flexible, event-driven runtime to support a broad feature set (auth, file upload, metrics, websockets, etc.) and intensive test coverage.
Decision: Use Node.js with Express, written in TypeScript, as the backend web framework.
Consequences: 
- Positive: Large NPM ecosystem; fast iteration; type safety; strong tooling (ts-node, tsc, ESLint).
- Negative: Transpilation adds build complexity; single-threaded model may require attention for CPU-bound work.