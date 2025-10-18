# ADR-009: MongoDB with Mongoose ODM

**Date**: 2025-10-16
**Status**: Proposed

## Context
The domain includes flexible entities like learning paths, notes, and progress artifacts.

## Decision
Persist data in MongoDB using Mongoose for schema modeling and validation.

## Consequences
Fits evolving, document-centric models and speeds iteration; complex relationships and transactions are harder than in relational databases; indexing and schema governance are essential for scale.