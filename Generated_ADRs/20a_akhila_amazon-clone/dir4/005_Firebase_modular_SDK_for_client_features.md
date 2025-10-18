# ADR-005: Firebase modular SDK for client features

**Date**: 2025-10-10
**Status**: Proposed

## Context
firebase (v9) is a dependency and firebase.js initializes client-side Firebase.

## Decision
Adopt Firebase v9 modular SDK for client features (e.g., Auth/Firestore if enabled) and project configuration.

## Consequences
Tree-shakeable imports reduce bundle size versus older SDKs; rapid feature enablement (Auth, Firestore, Storage) without managing servers; relies on correctly authored security rules; vendor lock-in and data egress considerations.