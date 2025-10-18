# ADR-001: Stage-based, file-backed pipeline

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository organizes the workflow into distinct steps (shuffle, feature extraction, optional training, reconstruction, evaluation) with artifacts passed between steps.

## Decision
Decouple the process into CLI-driven stages that read/write files (features, models, mappings) rather than a single monolithic program.

## Consequences
Pros: modularity, easier debugging, caching/reuse of intermediates, parallelizable stages. Cons: I/O overhead, brittle path/format coupling, requires artifact versioning and cleanup.