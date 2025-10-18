# ADR-001: Layered compiler architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project implements a small language compiler where clarity of responsibilities across phases is important for maintainability and evolution.

## Decision
Adopt a conventional multi-phase pipeline with distinct modules: Basic (diagnostics and token kinds), Lexer, Parser, Sema (semantic analysis), and CodeGen.

## Consequences
Improves separation of concerns, enables independent development and testing of phases, and allows future substitution of components. Introduces interface boundaries that require careful design and can add coordination overhead across modules.