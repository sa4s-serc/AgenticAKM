# ADR-007: Stripe integration using React Stripe libraries

**Date**: 2025-10-10
**Status**: Proposed

## Context
@stripe/react-stripe-js and @stripe/stripe-js are dependencies and a Payment component exists.

## Decision
Integrate payments with Stripe Elements on the client and rely on a server-side function to create PaymentIntents.

## Consequences
PCI scope minimized and a proven UX; requires secure secret management in Cloud Functions (never in client); mandates HTTPS and correctness of webhook/intent flows; testing across multiple payment methods and failure paths adds complexity.