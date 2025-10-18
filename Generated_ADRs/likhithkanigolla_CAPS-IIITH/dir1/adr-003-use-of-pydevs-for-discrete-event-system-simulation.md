---
### ADR-003: Use of pyDEVS for Discrete-Event System Simulation

**Status:** Inferred

**Context:** The systems being modeled are composed of discrete components that interact asynchronously (e.g., sensors sending data, actuators receiving commands). A simulation paradigm capable of handling event-driven behavior is required to accurately model and analyze the system's dynamics over time.

**Decision:** To use the **pyDEVS** library for implementing the simulation backend. This is strongly indicated by the file `generate_pydevs.py` and the commented-out dependency `# pypdevs` in `requirements.txt`. DEVS (Discrete Event System Specification) is a formal and robust methodology for modeling event-driven systems. The generated Python code (ADR-002) creates a simulation model compatible with the pyDEVS framework.

**Consequences:**
*   **Positive:**
    *   The DEVS formalism provides a solid, mathematically-grounded basis for the simulation, which is excellent for verification and compositional modeling.
    *   It is naturally suited for the target domain of asynchronous, event-driven IoT or cyber-physical systems.
    *   Keeps the entire toolchain within the Python ecosystem, simplifying dependencies.
*   **Negative:**
    *   The DEVS formalism has a learning curve for developers not already familiar with it.
    *   There might be performance limitations compared to more optimized, compiled simulation environments for very large-scale models.
    *   Dependency management can be tricky, as hinted by the presence of a `pyDEVS-3.11-Fix` note.