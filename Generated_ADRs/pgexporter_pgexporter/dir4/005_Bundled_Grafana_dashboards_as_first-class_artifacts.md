# ADR-005: Bundled Grafana dashboards as first-class artifacts

**Date**: 2025-10-16
**Status**: Proposed

## Context
Users want fast time-to-visualization with metrics that are known to be compatible.

## Decision
Ship versioned Grafana dashboards under contrib/grafana and document setup with Prometheus as a data source.

## Consequences
Accelerated adoption and consistent UX; dashboards remain in lockstep with metric packs; extra maintenance to evolve and test dashboards across versions.