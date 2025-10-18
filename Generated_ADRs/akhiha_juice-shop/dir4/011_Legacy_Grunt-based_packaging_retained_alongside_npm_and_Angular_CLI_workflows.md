# ADR-011: Legacy Grunt-based packaging retained alongside npm and Angular CLI workflows

**Date**: 2025-10-10
**Status**: Proposed

## Context
Historical packaging tasks still exist even as modern tooling handles builds.

## Decision
Keep Gruntfile.js for packaging tasks while using tsc for backend and Angular CLI for frontend builds; orchestrate via npm scripts.

## Consequences
Benefits: preserves existing release artifacts and processes. Drawbacks: duplicated or overlapping build logic, potential contributor confusion and maintenance debt.