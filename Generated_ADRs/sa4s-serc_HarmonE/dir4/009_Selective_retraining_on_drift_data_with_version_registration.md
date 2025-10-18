# ADR-009: Selective retraining on drift data with version registration

**Date**: 2025-10-09
**Status**: Proposed

## Context
Full retraining is costly; the system should adapt models to recent drift efficiently.

## Decision
Retrain only the selected model on drift data using the established preprocessing; save as a new version in the registry for potential switch.

## Consequences
Faster adaptation and reduced compute cost. Risk of overfitting to recent drift; requires governance to prevent model proliferation and to validate new versions.