# ADR-006: Payment Processing Strategy: Stripe Integration

**Date**: 2025-10-10
**Status**: Proposed

## Context
A secure, reliable, and PCI-compliant method for processing online payments was a critical requirement for the e-commerce functionality. The system had to ensure that sensitive credit card information never touched the application's servers.

## Decision
Stripe was integrated for payment processing. The architecture uses Stripe Elements on the frontend to securely collect card details and a dedicated Firebase Cloud Function on the backend to create Payment Intents and process charges.

## Consequences
This offloads the complexity of PCI compliance to Stripe, a trusted third-party provider, which is a major security and legal benefit. The separation of concerns between frontend data collection and backend processing is a robust pattern. The trade-off is a dependency on an external service, including its transaction fees and potential service outages.