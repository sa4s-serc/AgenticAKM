# ADR-009: Operational packaging as part of the product surface

**Date**: 2025-10-16
**Status**: Proposed

## Context
Organizations require predictable deployment across environments.

## Decision
Offer Docker images (Alpine/Rocky), RPM packaging, and systemd unit files, with example configurations.

## Consequences
Lower barrier to deployment and standardization; ongoing effort to maintain multiple packaging targets; primary focus on Linux distributions covered by provided artifacts.