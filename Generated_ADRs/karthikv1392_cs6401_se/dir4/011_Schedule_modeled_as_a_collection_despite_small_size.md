# ADR-011: Schedule modeled as a collection despite small size

**Date**: 2025-10-08
**Status**: Proposed

## Context
The _schedules collection contains a single weekly.md entry and a dedicated layout.

## Decision
Use a collection for schedule content even when the current dataset is minimal.

## Consequences
Provides a scalable pattern for future schedule entries and templating, but introduces configuration overhead that may be unnecessary if the content remains small.