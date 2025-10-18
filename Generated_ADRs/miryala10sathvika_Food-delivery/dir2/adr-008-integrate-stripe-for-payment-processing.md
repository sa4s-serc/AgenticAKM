---
### ADR-008: Integrate Stripe for payment processing

Status: Inferred
Context: stripe ^18.x dependency; pages like PlaceOrder/Verify; order controller present.
Decision: Use Stripe’s APIs for capturing payments and verifying orders.
Consequences:
- Positive: PCI scope reduction; robust, global payments infrastructure; webhooks/verification flows available.
- Negative: External dependency; sandbox/live key management; webhooks add operational complexity.