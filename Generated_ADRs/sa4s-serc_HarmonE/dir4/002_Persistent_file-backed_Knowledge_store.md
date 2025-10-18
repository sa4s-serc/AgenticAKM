# ADR-002: Persistent, file-backed Knowledge store

**Date**: 2025-10-09
**Status**: Proposed

## Context
The loop needs durable state across runs (active model, thresholds, drift stats, logs) without external dependencies.

## Decision
Use CSV/JSON files under a knowledge/ directory to persist thresholds, model choice, predictions, drift stats, and MAPE logs.

## Consequences
Simple, transparent, and easy to inspect or replay; no database required. Limits scalability, concurrency safety, and transactional integrity; file I/O can become a bottleneck.