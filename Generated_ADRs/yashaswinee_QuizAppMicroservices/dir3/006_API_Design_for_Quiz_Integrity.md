# ADR-006: API Design for Quiz Integrity

**Date**: 2025-10-16
**Status**: Proposed

## Context
During a quiz, the API must serve questions to the user without revealing the correct answers to prevent cheating, while still using that information for scoring later.

## Decision
The API was designed with two distinct operations: one endpoint to fetch quiz questions (which deliberately omits the answer field) and a separate endpoint to submit user responses for scoring.

## Consequences
This secures the quiz-taking process by design. It necessitates the use of Data Transfer Objects (DTOs) to create a public-facing representation of a question that is different from its internal domain model, which is a best practice for creating secure and stable APIs.