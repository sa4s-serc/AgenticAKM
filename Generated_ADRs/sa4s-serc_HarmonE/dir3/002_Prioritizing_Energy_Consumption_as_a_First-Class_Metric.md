# ADR-002: Prioritizing Energy Consumption as a First-Class Metric

**Date**: 2025-10-09
**Status**: Proposed

## Context
Traditional MLOps pipelines often optimize solely for predictive accuracy, ignoring the significant operational costs and environmental impact associated with energy consumption. The goal was to build a more sustainable and cost-effective system.

## Decision
Energy consumption was elevated to a first-class optimization target, co-equal with accuracy. The system's adaptation logic, particularly in the 'Analyze' phase, is designed to explicitly balance the trade-off between predictive performance and energy usage when selecting a model.

## Consequences
This 'Green AI' approach leads to more sustainable and cost-efficient operations. It incentivizes the use of simpler, less resource-intensive models where appropriate. The main trade-off is the potential to sacrifice some accuracy for energy savings, which may not be acceptable for all use cases. It also introduces a dependency on specialized monitoring tools like pyRAPL.