# ADR-010: Repository modularization by concern

**Date**: 2025-10-09
**Status**: Proposed

## Context
Different lifecycle stages (parsing, generation, web, metrics) require focused codebases and evolving independently.

## Decision
Separate directories for parser, generators, web assets, metrics, and examples; include sample inputs/outputs for traceability.

## Consequences
Improves maintainability and navigability; enables targeted testing; increases need for cross-module interface contracts (e.g., model.json schema) and documentation.