# ADR-006: Dual model persistence (custom save and MLflow model logging)

**Date**: 2025-10-14
**Status**: Proposed

## Context
A save.py module exists alongside MLflow artifacts that include model.pkl and environment files.

## Decision
Persist trained models via both custom serialization and MLflow’s model packaging.

## Consequences
Offers flexibility for consumers inside and outside MLflow, but duplicates responsibility, risks divergence between artifacts, and adds maintenance overhead.