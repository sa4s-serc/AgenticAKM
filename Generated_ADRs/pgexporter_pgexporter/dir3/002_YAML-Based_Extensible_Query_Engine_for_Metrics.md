# ADR-002: YAML-Based Extensible Query Engine for Metrics

**Date**: 2025-10-16
**Status**: Proposed

## Context
A one-size-fits-all, static set of metrics is insufficient for the diverse needs of database monitoring. Users need the ability to collect custom application-specific, business-level, or extension-related metrics.

## Decision
Architect the system around a flexible, YAML-based configuration file. This allows users to define their own SQL queries and declaratively map the results to Prometheus metric types (gauges, counters, etc.).

## Consequences
This makes the exporter extremely powerful and adaptable to virtually any monitoring scenario. It empowers users to tailor monitoring to their exact needs. This approach, however, introduces a dependency on a YAML parsing library and requires users to learn the specific configuration schema.