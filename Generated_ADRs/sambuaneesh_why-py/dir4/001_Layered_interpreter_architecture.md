# ADR-001: Layered interpreter architecture

**Date**: 2025-10-11
**Status**: Proposed

## Context
Core language implementation needs clear boundaries between lexing, parsing, representation, and execution.

## Decision
Split the interpreter into dedicated modules: lexer/token (lexer.py, tok.py), parser (parser.py), AST definitions (ast1.py), evaluator (eval.py), environment/scopes (environment.py), and runtime object model (object.py).

## Consequences
Clarifies responsibilities and supports incremental testing and refactoring; enables swapping or evolving layers independently; adds module overhead and cross-module contracts that must remain consistent.