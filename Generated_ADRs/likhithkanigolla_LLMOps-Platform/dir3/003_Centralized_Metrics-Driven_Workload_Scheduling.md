# ADR-003: Centralized, Metrics-Driven Workload Scheduling

**Date**: 2025-10-09
**Status**: Proposed

## Context
To ensure optimal use of cluster resources and prevent overloading individual nodes, a sophisticated method for placing new container workloads was required.

## Decision
A central 'Controller' service was created to act as the brain of the orchestrator. It consumes real-time metrics from all agents and uses this data to select the most suitable host node for each new deployment request.

## Consequences
This approach enables intelligent and efficient resource allocation across the cluster, improving overall system stability and performance. The major drawback is that the Controller becomes a potential performance bottleneck and a single point of failure for all scheduling decisions.