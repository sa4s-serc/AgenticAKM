# ADR-007: DAO Layer Abstraction for Data Access

**Date**: 2025-10-16
**Status**: Proposed

## Context
The codebase separates concerns and wishes to isolate repository specifics from business logic.

## Decision
Introduce QuestionDao and QuizDao as the data access layer that mediates between services and the underlying persistence technology.

## Consequences
Allows technology swaps or custom query implementations without changing services; provides a clear boundary for data access policies; can duplicate Spring Data repository features and add abstraction overhead.