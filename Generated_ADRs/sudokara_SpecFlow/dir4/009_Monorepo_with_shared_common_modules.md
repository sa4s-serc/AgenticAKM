# ADR-009: Monorepo with shared common modules

**Date**: 2025-10-14
**Status**: Proposed

## Context
Edge and cloud share protocols and configuration logic.

## Decision
Host edge, cloud, and shared code in a single repository with common/protocol.py and common/config.py reused by both sides.

## Consequences
Simplifies coordinated changes and keeps interfaces aligned; tight coupling can complicate independent versioning and packaging for separate deployments.