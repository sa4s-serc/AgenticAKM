# ADR-015: Notes feature prototyped with LocalStorage

**Date**: 2025-10-16
**Status**: Proposed

## Context
The front-end ships with note models and seeded mock data stored client-side.

## Decision
Implement notes locally in the browser for initial UX and iteration speed.

## Consequences
Enables fast prototyping with zero backend dependency; no multi-device sync, backup, or access control; requires a migration path to server-backed storage and data migration strategy.