# ADR-006: Cloud provider abstraction with Google Drive and OneDrive implementations

**Date**: 2025-10-14
**Status**: Proposed

## Context
Users want to choose among cloud backends while keeping the core pipeline unchanged.

## Decision
Define an uploader strategy interface and implement Google Drive (OAuth InstalledAppFlow; upload/download) and OneDrive (MSAL + Microsoft Graph; upload implemented, download stubbed); provider selection is config-driven.

## Consequences
Easy to add providers; leverages official SDKs; differing capabilities across providers (e.g., resumable support not yet leveraged) lead to uneven feature parity; introduces external OAuth token management requirements.