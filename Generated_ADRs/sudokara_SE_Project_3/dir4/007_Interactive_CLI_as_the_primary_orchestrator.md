# ADR-007: Interactive CLI as the primary orchestrator

**Date**: 2025-10-14
**Status**: Proposed

## Context
Users need guided setup for credentials, provider selection, directories, and observation mode, plus lifecycle control.

## Decision
Provide an interactive CLI (src/phoenix/CLI/cli.py) that loads config.json, manages credentials, and starts/stops observation; leave top-level main.py as a banner/onboarding entry.

## Consequences
Improves user onboarding and discoverability; centralizes orchestration; not packaged as a console script yet, reducing ease of installation and automation; encourages manual, interactive workflows.