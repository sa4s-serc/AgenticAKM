# ADR-016: Deterministic dependency graphs via lockfiles (npm and pnpm)

**Date**: 2025-10-14
**Status**: Proposed

## Context
Both package-lock.json and pnpm-lock.yaml exist; Python uses requirements.txt.

## Decision
Pin frontend dependencies with lockfiles and backend with requirements.txt to ensure repeatable builds.

## Consequences
Pros: reproducibility across environments. Cons: dual Node lockfiles can create tool ambiguity; teams should standardize on one package manager to avoid drift.