# ADR-005: Integration of Prompting and Fine-Tuning

**Date**: 2025-10-13
**Status**: Proposed

## Context
For peak performance, prompt engineering alone may be insufficient; fine-tuning the underlying model's weights is often necessary. These two processes are typically treated as separate, disconnected workflows.

## Decision
Bridge the gap between prompt engineering and fine-tuning by incorporating it as an advanced optimization strategy within the 'Teleprompter' layer. Optimizers like `GRPO` can automatically generate training data from program traces to fine-tune the model's weights for the specific task.

## Consequences
This creates a unified optimization pipeline that can tune the entire system, from prompts to model weights. It provides a path to state-of-the-art performance but introduces significant computational complexity and cost, requiring more data and infrastructure than prompt-only optimization.