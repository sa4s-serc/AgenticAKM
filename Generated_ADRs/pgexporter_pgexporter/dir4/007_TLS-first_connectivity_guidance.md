# ADR-007: TLS-first connectivity guidance

**Date**: 2025-10-16
**Status**: Proposed

## Context
Metrics collection often spans network boundaries and must meet security requirements.

## Decision
Support and document TLS for encrypted connections between the exporter and PostgreSQL and/or clients.

## Consequences
Improved security posture; operational overhead for certificate provisioning, rotation, and troubleshooting.