# ADR-006: OS-specific packaging for broad distribution

**Date**: 2025-10-14
**Status**: Proposed

## Context
Parent POM references jdeb, rpm, nsis, and osxappbundle plugins and distribution modules.

## Decision
Produce native installers per OS (Debian, Red Hat, Windows NSIS, macOS app bundle) as part of production builds.

## Consequences
Greatly improves installation UX and adoption across platforms; increases build matrix complexity, signing/notarization needs, and maintenance of platform-specific scripts and metadata.