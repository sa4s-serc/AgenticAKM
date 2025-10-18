# ADR-003: RESTful API with Spring Web

**Date**: 2025-10-16
**Status**: Proposed

## Context
Clients need to create, retrieve, update, and use questions to build and score quizzes over HTTP.

## Decision
Expose REST endpoints via spring-boot-starter-web, with QuestionController for CRUD and filtering, and QuizController for quiz creation, question retrieval, and scoring.

## Consequences
Enables straightforward integration with web/mobile clients; promotes stateless interactions; requires careful DTO design and validation; HTTP semantics and error handling become part of the contract.