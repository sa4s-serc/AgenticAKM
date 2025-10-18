# ADR-010: Externalized application state directory

**Date**: 2025-10-13
**Status**: Proposed

## Context
The Jetty context sets the system property reader.home to /data.

## Decision
Store persistent application data under a configurable reader.home directory, with a default of /data for deployments.

## Consequences
Facilitates container volume mounting, backups, and upgrades; underscores the need for correct permissions and disk provisioning; misconfiguration can lead to data loss or startup failures.