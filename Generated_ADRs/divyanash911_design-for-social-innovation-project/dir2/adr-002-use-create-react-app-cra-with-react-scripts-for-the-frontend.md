---
### ADR-002: Use Create React App (CRA) with react-scripts for the frontend

Status: Inferred
Context: package.json uses react-scripts for start/build/test and React 18 dependencies.
Decision: Use Create React App as the build tool and runtime scaffolding for the SPA.
Consequences:
- Positive: Low setup overhead, standard conventions, integrated dev server and tooling.
- Negative: Slower builds and less flexibility vs Vite/Next; CRA is considered legacy by many teams.