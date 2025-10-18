---
### ADR-006: Agent Discovery via Registry and Repositories

Status: Inferred
Context: Systems may need to dynamically register, discover, and manage agents (local or remote) at runtime. Hardcoded references reduce flexibility.
Decision: Provide an AgentRegistry with repository abstraction and an in-memory implementation (moya/registry/*).
Consequences:
- Positive: Decouples definition from usage; supports dynamic/dynamic loading of agents; facilitates environment-specific wiring.
- Negative: Requires consistency and lifecycle management; potential security and versioning concerns when combined with remote agents.