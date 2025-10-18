# ADR-013: Accounting for control-loop energy overhead

**Date**: 2025-10-10
**Status**: Proposed

## Context
Adaptation can save energy but also adds compute; its net benefit must be measured.

## Decision
Measure and log the planner’s CPU energy per cycle alongside inference energy.

## Consequences
Enables net energy accounting and evidence of adaptation cost-effectiveness. Adds measurement overhead and complexity to attribution when components overlap in time.