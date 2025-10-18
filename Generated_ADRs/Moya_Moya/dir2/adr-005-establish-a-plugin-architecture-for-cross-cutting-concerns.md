---
### ADR-005: Establish a Plugin architecture for cross-cutting concerns

**Status:** Inferred
**Context:** Authentication, logging, and activity indication concerns recur across apps. The codebase includes Plugin.swift and specific plugins (AccessTokenPlugin, CredentialsPlugin, NetworkLoggerPlugin, NetworkActivityPlugin).
**Decision:** Define a PluginType protocol and ship common plugins that can observe and modify request/response lifecycles.
**Consequences:** 
- Positive: Extensible, composable cross-cutting features; keeps core clean.
- Negative: Potential performance overhead; plugin ordering and side effects need careful handling.
- Trade-off: Extensibility and modularity over absolute simplicity.