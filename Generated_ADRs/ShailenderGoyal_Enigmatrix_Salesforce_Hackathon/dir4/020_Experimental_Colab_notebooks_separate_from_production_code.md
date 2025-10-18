# ADR-020: Experimental Colab notebooks separate from production code

**Date**: 2025-10-16
**Status**: Proposed

## Context
Colab notebooks are included for research and prototyping around learning workflows.

## Decision
Keep experiments in a segregated directory outside the runtime code paths.

## Consequences
Encourages rapid experimentation without risking production stability; results must be formalized before integration; ensures clearer boundaries for CI and deployments.