# ADR-002: Configuration-driven behavior using node-config with YAML profiles and JSON schema validation

**Date**: 2025-10-10
**Status**: Proposed

## Context
The app must support many run modes (ctf, tutorial, unsafe, test, etc.) and remain reproducible in workshops, CI, and demos.

## Decision
Use the config package with multiple config/*.yml profiles and validate with config.schema.yml; allow environment-based overrides via .env.

## Consequences
Benefits: predictable toggling of features and challenges, safe defaults with schema enforcement, easier automated testing. Drawbacks: configuration sprawl and precedence complexity, potential runtime surprises if profiles overlap or are misapplied.