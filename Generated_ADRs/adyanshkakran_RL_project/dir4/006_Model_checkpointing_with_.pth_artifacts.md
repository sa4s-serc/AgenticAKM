# ADR-006: Model checkpointing with .pth artifacts

**Date**: 2025-10-14
**Status**: Proposed

## Context
models/ contains .pth files for various agents and checkpoints across environments.

## Decision
Save model weights as .pth files with descriptive names encoding algorithm and environment.

## Consequences
Suggests a PyTorch-centric workflow and straightforward reload for Python users; absent explicit versioning schemas or metadata may hinder long-term reproducibility and cross-framework portability.