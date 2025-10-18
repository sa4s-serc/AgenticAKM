# ADR-012: Software Bill of Materials (SBOM) generation with CycloneDX

**Date**: 2025-10-10
**Status**: Proposed

## Context
Security training and disclosure goals require transparent dependency inventories.

## Decision
Generate CycloneDX SBOMs (JSON and XML) via @cyclonedx/cyclonedx-npm in CI and release scripts.

## Consequences
Benefits: supports vulnerability management, audits, and advisories; aligns with industry standards. Drawbacks: upkeep required to keep SBOMs accurate; may introduce process overhead for publishing and signing.