### ADR-001: Adopt a monolithic architecture for Phoenix

**Status:** Inferred
**Context:** The repository contains a single Python package (src/phoenix) with cohesive subsystems (Observation, Compression_Encryption, Uploader, utils) and a CLI, plus a dedicated monolith_benchmarking directory and an ADR named Monolith.md. There is no evidence of service boundaries, inter-process communication, or deployment manifests typical of microservices.
**Decision:** Build Phoenix as a single monolithic application with internal modular boundaries rather than as multiple services.
**Consequences:** 
- Positive: Simpler deployment, easier local development, straightforward inter-module coordination, and lower operational overhead.
- Negative: Scaling is coarse-grained; all modules must be deployed together. Tight coupling can grow over time if boundaries aren’t maintained. Startup time and memory footprint may increase as features accumulate.