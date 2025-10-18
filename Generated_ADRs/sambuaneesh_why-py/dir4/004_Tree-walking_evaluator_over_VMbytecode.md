# ADR-004: Tree-walking evaluator over VM/bytecode

**Date**: 2025-10-11
**Status**: Proposed

## Context
Execution strategy impacts performance, complexity, and debuggability.

## Decision
Use a direct AST-walking evaluator (eval.py) rather than compiling to bytecode or building a VM.

## Consequences
Simpler implementation and easier to reason about for teaching and debugging; slower execution and deeper call stacks on large programs; harder to optimize compared with a bytecode VM.