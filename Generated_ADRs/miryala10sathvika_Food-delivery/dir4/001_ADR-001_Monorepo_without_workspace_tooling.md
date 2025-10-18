# ADR-001: ADR-001: Monorepo without workspace tooling

**Date**: 2025-10-13
**Status**: Proposed

## Context
The repository contains three separate applications (backend, frontend, admin) in a single repo. Each has its own package.json and tooling. There is no npm/yarn/pnpm workspace configuration.

## Decision
Keep a simple monorepo without workspace/hoisting tooling for the MVP. Each app remains self-contained with its own dependency graph and scripts. Revisit introducing workspaces only if a shared library or significant cross-app dependency emerges.

## Consequences
- Simple onboarding; no cross-project tooling complexity.
- Install and build steps are per app (e.g., run npm install in backend, frontend, and admin separately).
- Potential duplication of dependencies across apps; longer overall install time.
- If shared code arises, consider extracting a package and introducing workspaces then.