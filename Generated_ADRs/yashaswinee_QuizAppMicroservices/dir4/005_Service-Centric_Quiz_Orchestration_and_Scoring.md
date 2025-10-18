# ADR-005: Service-Centric Quiz Orchestration and Scoring

**Date**: 2025-10-16
**Status**: Proposed

## Context
Quiz creation, question selection, and scoring are core business functions that must remain independent of controllers and storage details.

## Decision
Implement quiz assembly (including random selection by difficulty), question delivery without answers, and submission scoring inside QuizService and QuestionService.

## Consequences
Centralizes business logic for easier evolution and reuse; facilitates unit testing; introduces nondeterminism in random selection unless seeded or constrained; requires careful transaction and consistency handling.