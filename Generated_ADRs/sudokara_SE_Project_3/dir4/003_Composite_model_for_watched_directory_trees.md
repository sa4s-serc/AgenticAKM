# ADR-003: Composite model for watched directory trees

**Date**: 2025-10-14
**Status**: Proposed

## Context
Backups and audit logs need aggregated metrics across nested directories and files, and event scoping should reflect hierarchical structures.

## Decision
Represent watch targets using a Composite pattern (WatchDirComponent/Composite/Leaf) to compute aggregate counts and sizes and to navigate affected scopes.

## Consequences
Clean aggregation and extensibility for metrics and policies; consistent logging; added object management overhead and tree synchronization complexity with the live filesystem.