---
### ADR-007: Secure password storage with jBCrypt

Status: Inferred
Context: The project declares org.mindrot:jBCrypt (0.3m), a library for BCrypt password hashing.
Decision: Use BCrypt for hashing and storing user passwords.
Consequences:
- Positive: Strong, adaptive hashing suitable for protecting credentials.
- Negative: Computational cost must be tuned; the specific library version is old and may lack newer improvements.