# ADR-010: Explicit entry points for roles

**Date**: 2025-10-14
**Status**: Proposed

## Context
Operators need a simple way to launch each role.

## Decision
Expose run_edge.py and run_cloud.py as the canonical launchers for the client and server processes.

## Consequences
Simplifies local runs and testing; external orchestration (containers, service managers) must wrap these scripts for production-scale deployments.