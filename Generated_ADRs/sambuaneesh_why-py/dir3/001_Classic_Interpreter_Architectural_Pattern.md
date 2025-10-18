# ADR-001: Classic Interpreter Architectural Pattern

**Date**: 2025-10-11
**Status**: Proposed

## Context
The project's primary goal was to create a functional interpreter for a new programming language. A robust, well-understood, and maintainable architecture was required to manage the complexity of transforming source code into executable logic.

## Decision
The interpreter was architected using a classic, decoupled three-stage pipeline: a Lexer to tokenize source code, a Pratt Parser to construct an Abstract Syntax Tree (AST), and an Evaluator to traverse the AST and execute the program.

## Consequences
This separation of concerns results in a highly modular and testable system. Each component has a single responsibility, simplifying development, debugging, and future extension. This standard pattern also makes the codebase more accessible to developers familiar with compiler and interpreter design.