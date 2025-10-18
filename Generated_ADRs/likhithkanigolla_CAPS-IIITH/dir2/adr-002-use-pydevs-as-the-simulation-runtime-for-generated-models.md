---
### ADR-002: Use PyDEVS as the simulation runtime for generated models

Status: Inferred
Context: The BASE/basic-model includes DEVS-like constructs (iot_node, sink, onem2m_interface) and references to PyDEVS. The root requirements mention PyDEVS as required but installed separately.
Decision: Standardize on PyDEVS (pypdevs) as the discrete-event simulation engine for executing generated models.
Consequences:
- Positive: Mature DEVS semantics; suitability for event-driven IoT simulations; established patterns.
- Negative: External dependency management (not pinned in requirements); version compatibility issues (Python 3.11 notes); additional installation step for users.