# ADR-008: Interactive REPL and CLI entry points

**Date**: 2025-10-11
**Status**: Proposed

## Context
Developer and learner ergonomics benefit from immediate feedback.

## Decision
Provide a REPL (repl.py) and a CLI entry script (main.py) for interactive and scripted execution.

## Consequences
Accelerates experimentation and debugging; requires resilient error reporting and consistent integration of the lexer/parser/evaluator in interactive contexts.