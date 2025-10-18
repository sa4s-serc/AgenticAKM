# ADR-005: Third-Party Integration for Payment Processing

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application needed to process online payments securely and reliably. Handling and storing sensitive credit card information directly would introduce significant security risks and PCI compliance burdens.

## Decision
The Stripe API was chosen and integrated as the third-party payment gateway. The backend handles the creation of payment intents and validation, while the frontend uses Stripe's client-side libraries to securely collect payment information.

## Consequences
This decision offloads the complexity and severe security requirements of payment processing to a trusted, PCI-compliant service. It drastically reduces the application's risk profile and allows developers to focus on core business features rather than building and securing a payment infrastructure.