# ADR-004: Pluggable learned scoring with heuristic fallback

**Date**: 2025-10-14
**Status**: Proposed

## Context
Some algorithms can use trained models (from svm_train.py or linear_reg_train.py) to score frame relationships, but must still function without them.

## Decision
Design reconstruction code to optionally load a model artifact; if absent, revert to a pure feature-based heuristic.

## Consequences
Pros: flexible deployment, graceful degradation, supports ablation studies. Cons: complexity in branching logic; must maintain compatibility between model features and algorithm expectations.