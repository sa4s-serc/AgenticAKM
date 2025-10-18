# ADR-006: Data-Centric and Metrics-Driven Evaluation

**Date**: 2025-10-13
**Status**: Proposed

## Context
Assessing the quality of an LLM program can be subjective and unreliable. To enable automated optimization, a consistent and objective method for measuring performance is required.

## Decision
Establish a fundamentally data-centric and metrics-driven workflow. The optimization process (via Teleprompters) is explicitly guided by a user-provided dataset and a quantitative evaluation metric (e.g., `answer_exact_match`, `SemanticF1`).

## Consequences
This makes the development process rigorous, repeatable, and scientific. Program quality is no longer a matter of opinion but is objectively measured against a benchmark. The success of the entire system becomes highly dependent on the quality of the evaluation data and the chosen metric.