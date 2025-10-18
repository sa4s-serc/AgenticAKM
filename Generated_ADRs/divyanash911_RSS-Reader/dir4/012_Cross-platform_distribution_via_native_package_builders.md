# ADR-012: Cross-platform distribution via native package builders

**Date**: 2025-10-13
**Status**: Proposed

## Context
Build plugins include jdeb (DEB), RPM, NSIS (Windows installer), and macOS app bundling, in addition to WAR and Docker distributions.

## Decision
Produce native installers for Linux, Windows, and macOS alongside container and WAR artifacts.

## Consequences
Maximizes deployment flexibility across environments; increases build complexity and maintenance burden for packaging scripts and signing; requires CI support for multi-platform packaging.