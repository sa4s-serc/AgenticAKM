---
### ADR-008: Instrument energy consumption using pyRAPL

Status: Inferred
Context: pyRAPL appears in requirements.txt, implying interest in energy profiling for training/inference/monitoring tasks.
Decision: Integrate pyRAPL to measure and log energy/power usage during key workflows.
Consequences:
- Positive: Visibility into energy/performance trade-offs; supports sustainability and cost metrics in planning.
- Negative: Platform-specific support (e.g., Intel RAPL on Linux); adds measurement overhead; may not be available in all environments.