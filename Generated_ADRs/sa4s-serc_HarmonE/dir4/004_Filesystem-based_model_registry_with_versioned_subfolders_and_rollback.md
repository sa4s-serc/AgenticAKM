# ADR-004: Filesystem-based model registry with versioned subfolders and rollback

**Date**: 2025-10-09
**Status**: Proposed

## Context
Multiple model variants are evaluated and switched at runtime, and retraining produces new versions that must be traceable.

## Decision
Store models in a central directory with versioned subfolders; record the active version in knowledge/model.csv to enable switching and rollback.

## Consequences
Low-friction model management and reproducible rollbacks. Lacks advanced governance, access control, and multi-user concurrency features of a full MLOps registry.