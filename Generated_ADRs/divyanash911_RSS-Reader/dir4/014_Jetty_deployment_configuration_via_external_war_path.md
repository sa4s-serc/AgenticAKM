# ADR-014: Jetty deployment configuration via external war path

**Date**: 2025-10-13
**Status**: Proposed

## Context
reader.xml locates the WAR at ${jetty.data}/webapps/reader.war and deploys it at the root context.

## Decision
Resolve the deployable WAR from Jetty's data directory to decouple deployment artifacts from server binaries.

## Consequences
Supports clean separation of runtime state and deployables; eases upgrades by replacing a single WAR file; requires correct configuration of jetty.data and consistent file placement.