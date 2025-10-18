# ADR-003: Use of the Visitor Pattern for AST Traversal

**Date**: 2025-10-14
**Status**: Proposed

## Context
Operations like type checking and code generation needed to be performed on the Abstract Syntax Tree (AST) without coupling the operation logic directly into the AST node classes themselves.

## Decision
The Visitor design pattern was implemented for traversing the AST. Separate visitor classes (e.g., for Semantic Analysis and a `ToIRVisitor` for Code Generation) encapsulate the logic for processing different node types, keeping the AST data structure clean and focused solely on representing the code's structure.

## Consequences
Positive: Excellent separation of concerns, allowing new operations (e.g., an optimizer pass, a linter) to be added by creating new visitors without modifying the core AST definitions. Negative: Can introduce boilerplate code for the visitor interface and requires double dispatch, which can sometimes be less intuitive than direct method calls.