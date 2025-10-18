---
### ADR-008: Performance monitoring and automated benchmarking

Status: Inferred
Context: Dependencies include psutil and nvidia-ml-py3; tests/performance_test.py and tests/comparative_performance_test.py exist.
Decision: Integrate system/GPU telemetry and provide automated benchmarks to measure end-to-end and comparative performance across configurations.
Consequences:
- Positive: Data-driven optimization; regression detection; hardware utilization insights.
- Negative: Additional complexity in test environments; access permissions may be needed for GPU telemetry; benchmarks can be brittle across machines.