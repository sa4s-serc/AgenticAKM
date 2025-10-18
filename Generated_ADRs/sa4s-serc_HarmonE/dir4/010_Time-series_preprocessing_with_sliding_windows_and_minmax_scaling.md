# ADR-010: Time-series preprocessing with sliding windows and min–max scaling

**Date**: 2025-10-09
**Status**: Proposed

## Context
Forecasting models require fixed-size inputs and consistent feature scales for training and inference.

## Decision
Use sliding windows to create supervised sequences and apply min–max scaling with inverse transforms for outputs.

## Consequences
Standardizes inputs across model families and simplifies pipeline integration. Scaling parameters must be carefully managed across versions; drift can invalidate static scalers.