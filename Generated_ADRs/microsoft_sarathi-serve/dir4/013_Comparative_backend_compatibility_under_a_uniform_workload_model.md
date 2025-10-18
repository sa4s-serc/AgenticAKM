# ADR-013: Comparative backend compatibility under a uniform workload model

**Date**: 2025-10-14
**Status**: Proposed

## Context
Research and capacity planning benefit from comparing different backend strategies while holding workloads constant.

## Decision
Design the core to run Sarathi-native, vLLM-like, FasterTransformer-like, and Orca-like strategies behind common interfaces and datatypes.

## Consequences
Enables fair comparisons and shared tooling; maintaining compatibility with evolving external paradigms increases maintenance effort.