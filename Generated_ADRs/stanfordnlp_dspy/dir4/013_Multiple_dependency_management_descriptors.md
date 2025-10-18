# ADR-013: Multiple dependency management descriptors

**Date**: 2025-10-13
**Status**: Proposed

## Context
Presence of pyproject.toml, uv.lock, requirements.txt, and Pipfile.

## Decision
Support multiple workflows (uv, pip, Pipenv) for building docs and tooling.

## Consequences
Pros: flexibility for contributors and CI, easier adoption across environments. Cons: duplication risk and drift between lockfiles, higher maintenance burden.