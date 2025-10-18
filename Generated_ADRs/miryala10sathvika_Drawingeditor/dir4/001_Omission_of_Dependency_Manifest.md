# ADR-001: Omission of Dependency Manifest

**Date**: 2025-10-13
**Status**: Proposed

## Context
No requirements.txt, pyproject.toml, setup.py, or Pipfile were detected in the repository.

## Decision
Rely on implicit environments and standard library, with any third-party dependencies (if used) left undeclared.

## Consequences
Non-reproducible setups, harder onboarding, hidden runtime failures due to version drift, impeded containerization and CI, and no straightforward vulnerability/license scanning of dependencies.