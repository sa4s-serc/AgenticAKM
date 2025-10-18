# ADR-008: JSON-based configuration and on-disk token storage

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system needs a simple, inspectable configuration and persistence for OAuth credentials.

## Decision
Use a central config.json for providers, strategies, and watch directories; store OAuth tokens on disk (Google token.json and credentials.json; MSAL token cache for OneDrive).

## Consequences
Simple and transparent setup; straightforward local development; increases risk of secret leakage if files are not protected or ignored; multi-environment management and rotation require process discipline.