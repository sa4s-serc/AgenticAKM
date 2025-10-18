---
### ADR-010: TLS support using OpenSSL

Status: Inferred
Context: openssl-devel in Dockerfile and security.c indicate TLS/crypto usage; docs include TLS.
Decision: Use OpenSSL to provide TLS encryption for management and metrics endpoints, and cryptographic utilities.
Consequences:
- Positive: Industry-standard TLS; wide platform support; strong cryptographic primitives.
- Negative: OpenSSL API complexity; security updates must be tracked; licensing considerations.