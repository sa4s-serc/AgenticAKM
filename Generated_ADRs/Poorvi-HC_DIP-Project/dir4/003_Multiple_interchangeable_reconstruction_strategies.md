# ADR-003: Multiple interchangeable reconstruction strategies

**Date**: 2025-10-14
**Status**: Proposed

## Context
Algorithms 1–5 implement distinct ordering heuristics but share inputs/outputs and evaluation conventions.

## Decision
Implement each strategy in its own script with a common artifact contract and CLI semantics defined by README.

## Consequences
Pros: encourages exploration and head-to-head evaluation; isolates complexity per method. Cons: risk of code duplication; requires discipline to keep interfaces and assumptions consistent.