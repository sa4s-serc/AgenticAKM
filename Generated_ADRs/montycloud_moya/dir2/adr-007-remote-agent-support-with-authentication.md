---
### ADR-007: Remote Agent Support with Authentication

Status: Inferred
Context: Some agents must run remotely (separate process or host) for isolation, scaling, or language/runtime diversity. Calls must be secure.
Decision: Implement a RemoteAgent (moya/agents/remote_agent.py) and provide a remote agent server example with authentication (examples/remote_agent_server_with_auth.py).
Consequences:
- Positive: Enables distributed deployments and cross-language/process integration; supports horizontal scaling and isolation.
- Negative: Introduces network latency, error modes, and auth management; requires API versioning and backward compatibility strategies.