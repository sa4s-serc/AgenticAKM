# ADR-012: Explicit sequence and request lifecycle management

**Date**: 2025-10-14
**Status**: Proposed

## Context
High-throughput inference must track many concurrent sequences with different states and sampling parameters across distributed steps.

## Decision
Provide dedicated sequence managers and shared datatypes for requests, sequences, sampling, and step I/O, integrated with the engine and scheduler.

## Consequences
Improves correctness and debuggability for complex concurrent flows; adds bookkeeping overhead and more intricate state transitions to manage.