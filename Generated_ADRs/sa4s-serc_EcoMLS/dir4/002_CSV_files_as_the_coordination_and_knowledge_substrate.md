# ADR-002: CSV files as the coordination and knowledge substrate

**Date**: 2025-10-10
**Status**: Proposed

## Context
Multiple components must exchange state (active model, metrics, knowledge) across processes with minimal tooling and high inspectability.

## Decision
Use CSV files (model.csv, knowledge.csv, monitor.csv, log.csv, MAPEK_energy.csv) for inter-component communication, persistence, and auditing.

## Consequences
Simple, portable, human-readable, and easy to debug, but risks file I/O bottlenecks, race conditions, lack of atomicity/transactions, and eventual consistency. It limits throughput and complicates distributed or multi-host deployments.