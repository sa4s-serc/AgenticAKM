# ADR-002: Decouple offline learning from online decision-making via a knowledge base

**Date**: 2025-10-10
**Status**: Proposed

## Context
Training and rule induction are computationally expensive and do not fit real-time constraints.

## Decision
Perform clustering and rule induction offline and persist artifacts (pickles/CSVs) consumed by the runtime Analyzer/Planner.

## Consequences
Low-latency runtime decisions and reproducibility; supports versioned knowledge; risk of concept drift requiring periodic retraining and redeployment of artifacts.