# ADR-005: Live Configuration Reloading for Operational Flexibility

**Date**: 2025-10-16
**Status**: Proposed

## Context
In dynamic production environments, monitoring requirements frequently change. Operators must be able to add, remove, or modify metrics without causing service interruptions or downtime for the exporter.

## Decision
The architecture was designed to support live reloading of its YAML configuration. The running process can be signaled to re-read and apply the configuration file without a restart.

## Consequences
This provides critical operational flexibility, enabling zero-downtime updates to monitoring logic. This feature is essential for maintaining service continuity in production settings but adds complexity to the application's internal state management.