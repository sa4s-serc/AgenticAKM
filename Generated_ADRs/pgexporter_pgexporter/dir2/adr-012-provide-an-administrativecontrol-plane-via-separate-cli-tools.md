---
### ADR-012: Provide an administrative/control plane via separate CLI tools

Status: Inferred
Context: Separate binaries (pgexporter, pgexporter-admin, pgexporter-cli), management.c, shmem.c indicate a runtime management interface with shared memory/IPC.
Decision: Expose administrative and introspection functions through dedicated CLI tools that communicate with the exporter via IPC/shared memory.
Consequences:
- Positive: Operational control without service restarts; scriptable management; separation of concerns.
- Negative: Additional interfaces to secure; IPC complexity; compatibility guarantees needed between daemon and tools.