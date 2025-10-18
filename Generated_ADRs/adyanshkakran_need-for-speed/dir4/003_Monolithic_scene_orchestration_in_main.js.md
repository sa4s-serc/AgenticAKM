# ADR-003: Monolithic scene orchestration in main.js

**Date**: 2025-10-14
**Status**: Proposed

## Context
Initialization, asset loading, object placement, and gameplay parameters are coordinated in a single entry module.

## Decision
Centralize game bootstrap and core loop logic in src/main.js.

## Consequences
Speeds initial development and reduces indirection; increases coupling and complexity in one file; harder to test and evolve as features grow.