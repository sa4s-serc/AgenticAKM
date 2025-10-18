# ADR-001: Monorepo housing Python backend and Next.js frontend

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository co-locates a Python backend and a Next.js/React frontend with shared example artifacts (uploads, posters, video outputs).

## Decision
Adopt a single monorepo to develop, run, and evolve backend orchestration and frontend UI together.

## Consequences
Pros: simplifies cross-cutting changes, shared versioning, easier local setup and artifact exchange. Cons: larger repo footprint, mixed toolchains, and potential CI/CD coupling; requires clear boundaries to avoid accidental cross-layer coupling.