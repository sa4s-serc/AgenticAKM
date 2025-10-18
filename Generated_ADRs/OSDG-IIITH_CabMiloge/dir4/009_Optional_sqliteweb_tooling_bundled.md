# ADR-009: Optional sqliteweb tooling bundled

**Date**: 2025-10-14
**Status**: Proposed

## Context
A separate Dockerfile-sqliteweb exists; the actual database choice is not asserted.

## Decision
Bundle an optional container to run sqliteweb for inspecting SQLite databases during development/ops.

## Consequences
- Convenient local introspection if SQLite is used
- Must be gated and never exposed in production environments
- Presence does not mandate SQLite usage but suggests a lightweight dev-tooling path
- Additional maintenance overhead for an ancillary image