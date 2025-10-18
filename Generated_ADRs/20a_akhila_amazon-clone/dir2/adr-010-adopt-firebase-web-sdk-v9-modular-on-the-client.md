---
### ADR-010: Adopt Firebase Web SDK v9 (modular) on the client

Status: Inferred
Context: The client uses firebase ^9.1.1, which is the modular API release focused on tree-shaking and smaller bundles.
Decision: Use Firebase v9 modular SDK for client-side Firebase features (e.g., Auth, possibly Firestore/Storage).
Consequences:
- Positive: Smaller bundle sizes via tree-shaking; clearer API imports; long-term alignment with Firebase’s direction.
- Negative: Migration friction from namespaced v8 examples; some community tutorials/libraries may still assume v8 syntax.