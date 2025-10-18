---
### ADR-010: Integrate with Central Authentication Service (CAS)

Status: Inferred
Context: requirements.txt includes python-cas, commonly used to integrate with institution-wide SSO systems. The app branding (campus/cab sharing) suggests centralized auth needs.
Decision: Use python-cas to integrate the application with a CAS-based SSO provider.
Consequences: Centralized authentication improves security and user experience in institutional contexts. Adds operational dependencies (CAS server availability, HTTPS, callback URLs) and complexity for local development/testing.