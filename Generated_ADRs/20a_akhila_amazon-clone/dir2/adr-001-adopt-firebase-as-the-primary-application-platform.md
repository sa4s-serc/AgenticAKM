### ADR-001: Adopt Firebase as the primary application platform

Status: Inferred
Context: The repository includes .firebaserc, firebase.json, a /functions folder for Cloud Functions, and a /public directory consistent with Firebase Hosting. The client depends on firebase ^9.1.1 and the backend on firebase-admin and firebase-functions, indicating reliance on Firebase services for hosting static assets and running serverless backend logic. Typical e-commerce flows (Login, Orders, Payment) suggest the need for authentication and persistent storage.
Decision: Use Firebase for static site hosting (Frontend), Authentication (client SDK), and serverless backend via Firebase Cloud Functions (with firebase-admin for privileged operations).
Consequences: 
- Positive: Rapid development, managed infrastructure, easy deployment (single Firebase project), local emulators for development, and tight integration between client and serverless functions.
- Negative: Vendor lock-in to Firebase; cold-start latency for functions; potential complexity scaling beyond Firebase’s service limits; costs tied to Firebase usage patterns.