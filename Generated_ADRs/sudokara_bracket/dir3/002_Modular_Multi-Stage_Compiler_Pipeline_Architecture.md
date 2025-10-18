# ADR-002: Modular Multi-Stage Compiler Pipeline Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
A clear and maintainable structure was needed to manage the complexity of transforming source code into a low-level representation.

## Decision
The compiler was architected as a traditional multi-stage pipeline, with distinct, decoupled phases for Lexing, Parsing, Semantic Analysis, and Code Generation. Each phase is implemented as a separate library, passing a progressively refined data structure (Tokens, then AST) to the next stage.

## Consequences
Positive: High degree of modularity and separation of concerns. Each stage can be developed, tested, and maintained independently. This classic design is well-understood and makes it easier to reason about the compilation process. Negative: Can introduce some overhead in passing data structures between stages and requires a well-defined interface for each component.