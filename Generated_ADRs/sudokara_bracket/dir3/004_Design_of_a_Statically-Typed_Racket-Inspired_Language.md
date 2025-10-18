# ADR-004: Design of a Statically-Typed, Racket-Inspired Language

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project's goal was to create a compiler for a new language, balancing the expressive, Lisp-like syntax of Racket with the safety and performance benefits of static analysis.

## Decision
A custom source language was designed. It borrows its S-expression syntax from Racket for simplicity and structural clarity, but critically, it enforces a static type system. This requires a dedicated Semantic Analysis phase for type checking before code generation.

## Consequences
Positive: Static typing allows for catching a large class of errors at compile-time, improving code reliability and enabling performance optimizations. The Racket-like syntax simplifies parsing. Negative: Designing a new language and its type system is a complex undertaking, requiring more compiler machinery (e.g., a robust type checker) than a dynamically-typed language would.