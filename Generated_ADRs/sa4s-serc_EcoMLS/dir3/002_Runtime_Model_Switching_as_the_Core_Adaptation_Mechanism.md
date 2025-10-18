# ADR-002: Runtime Model Switching as the Core Adaptation Mechanism

**Date**: 2025-10-10
**Status**: Proposed

## Context
The primary objective was to actively manage the trade-off between energy consumption and model confidence (accuracy). A direct and impactful mechanism was needed to shift the system's operating point on this spectrum.

## Decision
The system's adaptation strategy is centered on dynamically switching between a suite of pre-trained YOLOv5 models of varying sizes (e.g., nano, small, medium, large). The Executor component unloads the current model and loads a new one based on the Planner's decision.

## Consequences
This provides a powerful and discrete method for controlling performance. Switching to a smaller model yields significant energy savings at the cost of confidence, and vice-versa. However, this approach introduces a brief latency during the model-switching event and limits the system to the specific performance points offered by the available models, with no ability to operate 'in-between' them.