# ADR-008: Minimal tooling for development and distribution

**Date**: 2025-10-14
**Status**: Proposed

## Context
package.json includes only a start script and devDependency on Electron with no packaging or tests.

## Decision
Prioritize a simple development workflow (electron .) without test automation or packaging tooling.

## Consequences
Lowers initial setup cost and speeds iteration, but complicates distribution/updates, reduces reproducibility and QA confidence, and increases regression risk as the codebase grows.