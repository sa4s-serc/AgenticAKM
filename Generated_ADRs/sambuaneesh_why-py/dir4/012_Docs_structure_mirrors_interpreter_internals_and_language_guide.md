# ADR-012: Docs structure mirrors interpreter internals and language guide

**Date**: 2025-10-11
**Status**: Proposed

## Context
Teaching the interpreter and the language benefits from aligned structure.

## Decision
Organize docs into getting-started, implementation (lexer/parser/AST/interpreter), language-guide, and examples, matching the code layout.

## Consequences
Reduces cognitive load for readers and keeps concepts discoverable; increases documentation maintenance overhead whenever internal structures or semantics change.