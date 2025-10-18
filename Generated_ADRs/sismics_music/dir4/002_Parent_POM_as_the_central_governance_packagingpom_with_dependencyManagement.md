# ADR-002: Parent POM as the central governance (packaging=pom) with dependencyManagement

**Date**: 2025-10-14
**Status**: Proposed

## Context
The root pom.xml defines a parent POM named “Music Parent,” controlling plugin versions and dependencyManagement for all Maven modules.

## Decision
Centralize dependency and plugin versions via a parent POM and manage module inclusion through Maven profiles.

## Consequences
Improves consistency and reproducibility across Java modules and simplifies upgrades; couples modules to a shared BOM; Android (Gradle) is excluded, so it can diverge in versions and API expectations.