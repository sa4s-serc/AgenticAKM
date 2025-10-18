# ADR-004: Plain CSV ingestion without schema or versioning

**Date**: 2025-10-14
**Status**: Proposed

## Context
Training and test data are committed as CSVs (data.csv, test.csv) and read directly by data utilities.

## Decision
Use local, committed CSV files as the data source without explicit schema enforcement or version tracking.

## Consequences
Enables quick, self-contained runs and demos, but risks silent data drift, unclear provenance, reproducibility gaps across environments, and weak governance for production use.