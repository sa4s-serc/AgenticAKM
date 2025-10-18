# ADR-005: Standardization on Hugging Face and PyTorch

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system needs a robust, flexible, and widely-supported framework for loading, managing, and executing both the draft and target LLM models. Reinventing this functionality would be time-consuming and error-prone.

## Decision
The project standardized on PyTorch as the core ML framework and the Hugging Face ecosystem (Transformers, Accelerate) for model loading and management. This provides a consistent interface for interacting with a vast library of pre-trained models.

## Consequences
This choice dramatically accelerates development by leveraging a mature ecosystem for complex tasks. It ensures access to state-of-the-art models and tools like `Accelerate` for multi-GPU inference. The downside is a strong dependency on this ecosystem and its associated abstractions.