# ADR-012: Co-locating data and experiment artifacts with source code

**Date**: 2025-10-14
**Status**: Proposed

## Context
Datasets (CSVs) and MLflow run artifacts are stored within the repository tree.

## Decision
Keep datasets and experiment outputs in-repo alongside code.

## Consequences
Enables self-contained demos and offline workflows, but increases repository size, risks accidental exposure of sensitive artifacts, and encourages mixing transient outputs with source.