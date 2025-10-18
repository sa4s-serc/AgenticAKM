# ADR-004: Device-aware draft model abstraction

**Date**: 2025-10-14
**Status**: Proposed

## Context
Edge hardware is heterogeneous across CPU, GPU, and NPU.

## Decision
Provide a pluggable draft model wrapper (edge/draft_model.py) with backends for CPU/GPU and an OpenVINO runner (edge/openvino_model.py) for NPU.

## Consequences
Enables portable performance across devices; expands test matrix and dependency surface; demands careful capability detection and fallback logic.