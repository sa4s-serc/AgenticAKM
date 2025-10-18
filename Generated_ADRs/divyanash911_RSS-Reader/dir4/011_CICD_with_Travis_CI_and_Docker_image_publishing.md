# ADR-011: CI/CD with Travis CI and Docker image publishing

**Date**: 2025-10-13
**Status**: Proposed

## Context
.travis.yml defines branch-based behavior: normal branches run tests; release/demo branches produce production builds (skipping tests) and publish Docker images on Ubuntu Trusty with Docker enabled.

## Decision
Use Travis CI to run tests on regular branches and to produce and publish Docker images on release/demo branches while skipping tests for speed.

## Consequences
Automates artifact creation and container distribution; accelerates release pipelines; skipping tests on release increases regression risk; reliance on legacy Travis and Ubuntu Trusty can constrain modernization and security posture.