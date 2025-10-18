---
### ADR-003: Integrate Stripe Elements on the client using @stripe/react-stripe-js

Status: Inferred
Context: The client depends on @stripe/react-stripe-js and @stripe/stripe-js, which are used to render PCI-compliant payment inputs and to confirm payments with client secret tokens returned from the backend.
Decision: Use React Stripe Elements for payment UI and client-side confirmation, delegating sensitive handling to Stripe’s JS SDK.
Consequences:
- Positive: Reduced PCI scope, secure payment UX, standardized integration patterns, easy customization of payment forms.
- Negative: Dependency on Stripe’s SDK and hosted payment flows; additional bundle weight; must maintain compatibility with backend Stripe API versions.