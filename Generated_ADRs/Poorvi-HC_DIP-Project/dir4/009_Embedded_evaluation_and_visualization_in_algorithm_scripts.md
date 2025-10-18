# ADR-009: Embedded evaluation and visualization in algorithm scripts

**Date**: 2025-10-14
**Status**: Proposed

## Context
Reconstruction scripts can compute ordering metrics and optionally play back or save reconstructed videos.

## Decision
Co-locate evaluation/visualization with reconstruction to streamline experimentation.

## Consequences
Pros: immediate feedback loop; fewer moving parts during research. Cons: mixes concerns; requires flags for headless runs; harder to reuse evaluation independently.