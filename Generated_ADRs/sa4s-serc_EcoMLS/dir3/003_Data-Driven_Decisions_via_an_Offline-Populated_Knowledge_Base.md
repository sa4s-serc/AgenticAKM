# ADR-003: Data-Driven Decisions via an Offline-Populated Knowledge Base

**Date**: 2025-10-10
**Status**: Proposed

## Context
The Planner component needs accurate data on the performance characteristics (energy usage, confidence, etc.) of each available ML model to make optimal decisions. Performing this characterization at runtime would be slow and unreliable.

## Decision
A static 'Knowledge.csv' file is used as the Knowledge Base. This file is populated offline by a dedicated 'Learning_Engine' component that benchmarks each model under controlled conditions to create a reliable performance profile. The runtime Planner simply queries this pre-computed data.

## Consequences
This design makes the runtime decision-making process extremely fast and deterministic. However, it makes the system's effectiveness dependent on the quality of the offline profiling. The system cannot adapt to environmental changes (e.g., different hardware, background load) that are not captured in the static knowledge base, which would require a full regeneration of the profiles.