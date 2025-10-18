# ADR-002: Automated Optimization via 'Teleprompters'

**Date**: 2025-10-13
**Status**: Proposed

## Context
Even with a well-structured program, its performance is highly dependent on the quality of the prompts, few-shot examples, and model weights. Manually finding the optimal combination is a significant bottleneck.

## Decision
Introduce a dedicated optimization layer called 'Teleprompters'. These are algorithms that take a declarative DSPy program, a dataset, and an evaluation metric, and then automatically compile the program by generating and validating high-quality prompts and few-shot examples.

## Consequences
This is the framework's core innovation, turning prompt engineering into a systematic, data-driven optimization problem. It leads to demonstrably better performance and saves immense developer time. The trade-off is the computational cost of the optimization (or 'compilation') step.