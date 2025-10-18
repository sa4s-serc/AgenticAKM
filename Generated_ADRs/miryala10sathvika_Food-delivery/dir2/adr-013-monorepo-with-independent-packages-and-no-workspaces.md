---
### ADR-013: Monorepo with independent packages and no workspaces

Status: Inferred
Context: Three folders with their own package.jsons; no workspace manager (npm/yarn/pnpm workspaces) configured.
Decision: Use a simple monorepo layout without shared dependency/workspace tooling.
Consequences:
- Positive: Low complexity; each app can be developed/run independently.
- Negative: Duplication of dependencies and scripts; harder to share code and enforce consistent tooling across apps.