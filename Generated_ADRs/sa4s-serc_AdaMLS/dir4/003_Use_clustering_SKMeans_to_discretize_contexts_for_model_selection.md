# ADR-003: Use clustering (SKMeans) to discretize contexts for model selection

**Date**: 2025-10-10
**Status**: Proposed

## Context
Mapping telemetry to the best model is nonlinear with limited labeled data and must remain interpretable.

## Decision
Train SKMeans per YOLOv5 size, choose K via offline analysis, and derive adaptation rules from cluster assignments.

## Consequences
Fast, interpretable decisions and compact knowledge; sensitivity to chosen K and feature scaling; cluster boundaries may not capture rare edge cases.