# ADR-004: File-system–backed storage of inputs and generated artifacts

**Date**: 2025-10-14
**Status**: Proposed

## Context
Artifacts are stored under backend/posters/, backend/video/final_output/, backend/uploads/, and intermediate JSON files.

## Decision
Persist inputs, intermediates, and outputs on the local filesystem with a structured directory layout.

## Consequences
Pros: simple, transparent, easy local reproducibility and debugging. Cons: limits horizontal scalability and multi-instance deployments; requires externalization (object storage) for production; backup/retention policy is manual.