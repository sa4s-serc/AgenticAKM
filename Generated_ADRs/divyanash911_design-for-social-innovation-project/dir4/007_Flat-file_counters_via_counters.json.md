# ADR-007: Flat-file counters via counters.json

**Date**: 2025-10-13
**Status**: Proposed

## Context
A counters.json file is present in the backend directory and appears to store counters or metadata.

## Decision
Maintain simple counters/metadata in a JSON file rather than a database.

## Consequences
Low implementation overhead, but risks race conditions, corruption under concurrent writes, and operational pain across multiple instances; requires locking or migration to a durable store.