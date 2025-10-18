# ADR-009: Minimal evaluation harness

**Date**: 2025-10-14
**Status**: Proposed

## Context
test.py exists for evaluation or quick checks; testing_rewards.txt present.

## Decision
Provide a lightweight evaluation script instead of a full validation framework.

## Consequences
Fast manual checks and smoke tests; but limited standardized metrics, reproducible evaluation protocols, and CI integration, making cross-run comparisons less rigorous.