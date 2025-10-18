# ADR-003: Centralized API layer and config-driven endpoints

**Date**: 2025-10-10
**Status**: Proposed

## Context
API.js encapsulates network calls; config.js holds base URLs/keys; helpers.js provides UI/data utilities.

## Decision
Abstract all remote data access through a single API module configured via environment-driven settings.

## Consequences
Cleaner separation of concerns, easier swapping/mocking of the data provider, and consistent error handling; risks creating a monolithic API module and tight coupling if the interface is not carefully maintained.