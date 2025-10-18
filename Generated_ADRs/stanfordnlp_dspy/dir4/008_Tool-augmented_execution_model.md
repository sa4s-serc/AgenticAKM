# ADR-008: Tool-augmented execution model

**Date**: 2025-10-13
**Status**: Proposed

## Context
Tools include PythonInterpreter, Embeddings, and ColBERTv2; modules include ReAct/CodeAct patterns.

## Decision
Provide tool integration primitives to enable retrieval-augmented and code-executing agents.

## Consequences
Pros: improved capability and grounding, supports common agent patterns. Cons: security/runtime risks (code execution), heavier dependencies, sandboxing concerns.