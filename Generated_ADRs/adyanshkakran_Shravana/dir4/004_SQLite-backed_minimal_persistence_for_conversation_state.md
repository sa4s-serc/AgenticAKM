# ADR-004: SQLite-backed minimal persistence for conversation state

**Date**: 2025-10-14
**Status**: Proposed

## Context
The bot needs to track WhatsApp user IDs to OpenAI conversation thread IDs and store minimal state.

## Decision
Use a simple SQLite database (db.py, schema.sql, threads_db file) instead of ephemeral stores like Python shelve.

## Consequences
Improves reliability and portability for low-throughput use cases and simplifies local development; however, SQLite limits concurrent writes and horizontal scaling, and the DB file must be managed carefully in multi-instance deployments.