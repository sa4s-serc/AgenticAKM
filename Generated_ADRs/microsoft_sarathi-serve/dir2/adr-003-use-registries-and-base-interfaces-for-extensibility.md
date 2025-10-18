---
### ADR-003: Use registries and base interfaces for extensibility

Status: Inferred
Context: Multiple registries exist: block_space_manager_registry.py, scheduler_registry.py, attention_backend_registry.py, and request generator registries. Base interfaces accompany each (e.g., base_block_space_manager.py, base_scheduler.py, base_attention_wrapper.py).
Decision: Adopt a registry + base-class pattern to enable plug-and-play replacement and easy introduction of new implementations across schedulers, block managers, attention backends, and workload generators.
Consequences:
- Positive: High modularity and testability; fosters experimentation; clear extension points.
- Negative: Slight indirection/boilerplate; requires consistent lifecycle and config handling across implementations.