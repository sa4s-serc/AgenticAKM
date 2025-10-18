# ADR-012: GitHub Actions-based CI/CD with containerized publishing

**Date**: 2025-10-13
**Status**: Proposed

## Context
Workflows include build_and_release, docs-push, precommits_check; a generated action publishes to PyPI from Docker; TestPyPI helper provided.

## Decision
Automate quality checks, docs deploy, and package release via GitHub Actions and containerized builds.

## Consequences
Pros: reproducible releases, consistent environments, easier rollbacks, pre-merge quality gates. Cons: reliance on GitHub and container registry, secrets management complexity, longer pipeline times.