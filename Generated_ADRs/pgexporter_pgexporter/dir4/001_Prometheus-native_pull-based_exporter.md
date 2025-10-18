# ADR-001: Prometheus-native, pull-based exporter

**Date**: 2025-10-16
**Status**: Proposed

## Context
The project targets operational observability of PostgreSQL nodes and integrates with Prometheus and Grafana.

## Decision
Expose metrics in Prometheus format with documented names, labels, and semantics, and provide a scrape helper to align with Prometheus' pull model.

## Consequences
Seamless integration with Prometheus and downstream Grafana dashboards; consistent labeling for alerting; limited suitability for non-Prometheus monitoring without additional adapters.