---
### ADR-005: Monitoring of Energy Consumption as a Key Metric

**Status:** Inferred
**Context:** The system required monitoring beyond typical software performance metrics like latency, throughput, or prediction accuracy. There was a specific non-functional requirement to measure and track the system's energy consumption. This suggests that energy efficiency is a first-class concern, possibly for research in Green AI or for deployment in power-constrained environments.
**Decision:** The `pyRAPL` library was integrated into the system to monitor energy consumption. This library is listed in `requirements.txt` and is designed to read power usage information directly from Intel CPU's Running Average Power Limit (RAPL) interface. This monitoring logic is most likely implemented within the `mape/monitor.py` component.
**Consequences:**
*   **Positive:** The system gains visibility into its energy footprint, a critical metric for sustainable computing. This data can be used to analyze the energy cost of different models or operations and can be used by the MAPE loop's `plan.py` to make energy-aware adaptation decisions.
*   **Negative:** The solution is hardware-dependent; `pyRAPL` works specifically with Intel (and some AMD) CPUs that support the RAPL interface. This limits the portability of the energy monitoring feature to other hardware architectures. The monitoring itself introduces a minor performance overhead.