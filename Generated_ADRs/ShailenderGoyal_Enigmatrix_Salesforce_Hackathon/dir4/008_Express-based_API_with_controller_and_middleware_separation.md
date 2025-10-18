# ADR-008: Express-based API with controller and middleware separation

**Date**: 2025-10-16
**Status**: Proposed

## Context
The backend exposes routes for auth, AI, chat, notes, knowledge base, and pre-assessment.

## Decision
Implement the server with Node.js and Express, organizing logic into controllers and middlewares.

## Consequences
Familiar, flexible structure and quick iteration; requires conventions for error handling, logging, and input validation to avoid drift; less opinionated than frameworks like NestJS.