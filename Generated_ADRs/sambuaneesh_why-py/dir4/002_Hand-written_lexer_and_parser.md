# ADR-002: Hand-written lexer and parser

**Date**: 2025-10-11
**Status**: Proposed

## Context
Choosing between parser generators and custom implementations affects control and complexity.

## Decision
Implement both the lexer and parser manually in Python without external parsing frameworks.

## Consequences
Grants fine-grained control over syntax and error handling and reduces external dependencies; increases maintenance burden and requires careful testing to avoid subtle parsing bugs.