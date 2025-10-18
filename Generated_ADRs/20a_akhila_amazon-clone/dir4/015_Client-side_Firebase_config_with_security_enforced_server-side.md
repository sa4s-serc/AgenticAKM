# ADR-015: Client-side Firebase config with security enforced server-side

**Date**: 2025-10-10
**Status**: Proposed

## Context
firebase.js initializes client Firebase; Cloud Functions exist for sensitive operations like payments.

## Decision
Expose only Firebase’s non-secret client config in the frontend and push sensitive logic (secrets, Stripe keys) to Cloud Functions.

## Consequences
Aligns with Firebase’s security model and best practices; requires careful Firestore/Storage rules if those services are used; environment management for Functions (e.g., Stripe secret keys) becomes critical.