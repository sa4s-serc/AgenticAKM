# ADR-010: Canonical artifact locations and schemas governed by README

**Date**: 2025-10-14
**Status**: Proposed

## Context
Inputs/outputs and expected file locations are standardized and documented as the source of truth.

## Decision
Treat README-defined paths and formats as the stable contract between stages and scripts.

## Consequences
Pros: shared understanding and smoother interoperability. Cons: changes are costly and require coordinated updates; risk of drift if code and docs diverge; needs explicit versioning.