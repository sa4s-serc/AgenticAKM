# ADR-004: Local JSON persistence

**Date**: 2025-10-14
**Status**: Proposed

## Context
Leaderboard results must persist across runs without external infrastructure.

## Decision
Store leaderboard data in a local JSON file (leaderboard.json) as a lightweight data store.

## Consequences
Zero‑dependency and offline‑first persistence with easy inspectability, but risks data corruption on concurrent writes, lacks schema/validation, can suffer performance issues at scale, and may face path/permission issues when packaged unless stored in a writable app data directory.