# ADR-002: Offline Learning / Online Adaptation Split

**Date**: 2025-10-10
**Status**: Proposed

## Context
The process of generating effective adaptation rules from large performance datasets is computationally intensive and cannot be performed in real-time without severely impacting the system's performance. The online system, however, needs to make adaptation decisions with very low latency.

## Decision
A two-phase architecture was chosen. An 'Offline Learning Engine' is responsible for analyzing performance data and pre-computing adaptation rules using machine learning. The 'Online Adaptive System' is a lightweight component that simply loads these pre-computed rules into its Knowledge Base and uses them for fast, efficient runtime decision-making.

## Consequences
This decouples the expensive training process from the live inference system, ensuring high-performance online adaptation. The online system remains simple and fast. The main drawback is that the system cannot learn from new patterns at runtime; its knowledge is static until the offline engine is re-run and the rules are updated.