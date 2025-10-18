---
### ADR-002: Implement server-side payment processing with Stripe via Cloud Functions and Express

Status: Inferred
Context: The functions package.json includes stripe, express, cors, firebase-functions, and firebase-admin, suggesting an Express app deployed as a Firebase HTTPS function to handle payment operations securely. The web app uses @stripe/react-stripe-js and @stripe/stripe-js on the client.
Decision: Expose a server-side REST API (e.g., payments/create) via Firebase Cloud Functions + Express to create and manage Stripe PaymentIntents, keeping Stripe secret keys off the client. Enable CORS for the frontend origin(s).
Consequences:
- Positive: Proper security posture (secrets on server), capability to validate amounts, and integrate order lifecycle with server-side data stores.
- Negative: Additional backend code to maintain, possible function cold starts, need for CORS configuration and error handling; must monitor Stripe API changes and SDK versions.