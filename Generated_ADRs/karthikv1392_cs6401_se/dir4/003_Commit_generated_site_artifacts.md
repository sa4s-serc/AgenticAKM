# ADR-003: Commit generated site artifacts

**Date**: 2025-10-08
**Status**: Proposed

## Context
The built site directory (_site/) is checked into version control.

## Decision
Track the _site directory in the repository alongside sources.

## Consequences
Enables offline distribution and direct artifact access but bloats repo size, risks merge conflicts and stale content, and breaks the clean source-to-build separation typically expected with Jekyll.