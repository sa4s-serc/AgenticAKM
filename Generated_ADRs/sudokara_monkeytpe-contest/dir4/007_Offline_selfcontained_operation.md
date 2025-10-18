# ADR-007: Offline, self‑contained operation

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository shows no external database or network dependencies for persistence.

## Decision
Run fully locally with no cloud services or remote storage for leaderboard data.

## Consequences
Provides privacy and reliability without network dependency, but forfeits multi‑device sync, centralized moderation, and easy sharing; backups and data recovery are manual.