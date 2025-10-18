# ADR-008: Frontend type safety and linting; backend JavaScript without TypeScript

**Date**: 2025-10-14
**Status**: Proposed

## Context
The frontend includes TypeScript and ESLint/Prettier configs; the backend appears to use plain JavaScript with Express conventions.

## Decision
Apply static typing and linting rigor to the client-side codebase while keeping the server code in plain JavaScript.

## Consequences
Improves correctness and developer experience on the client; keeps backend flexible but more susceptible to runtime type errors; introduces heterogeneous toolchains that must be maintained separately.