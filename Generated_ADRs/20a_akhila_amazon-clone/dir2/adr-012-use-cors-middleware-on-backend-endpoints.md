---
### ADR-012: Use CORS middleware on backend endpoints

Status: Inferred
Context: The functions package.json includes cors dependency alongside express, indicating CORS handling for the HTTPS API.
Decision: Apply CORS middleware to Cloud Functions/Express endpoints to allow the React frontend to call the backend securely from the browser.
Consequences:
- Positive: Enables controlled cross-origin requests from the hosted SPA; fewer browser-side integration issues.
- Negative: Requires careful origin configuration to avoid security risks; misconfiguration can either break calls or expose endpoints unnecessarily.