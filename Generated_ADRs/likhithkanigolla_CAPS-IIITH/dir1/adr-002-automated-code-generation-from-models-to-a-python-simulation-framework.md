---
### ADR-002: Automated Code Generation from Models to a Python Simulation Framework

**Status:** Inferred

**Context:** With a system architecture defined in SAML models (ADR-001), there is a need to translate these abstract designs into executable code for testing, validation, and simulation. Manually translating the models into code would defeat the purpose of MDE, as it would be slow and introduce the risk of inconsistencies.

**Decision:** To implement an automated code generation pipeline. The repository contains a `generator` directory with modules like `saml_parser.py`, `component_extraction.py`, and `file_generators.py`. This indicates a clear decision to create a tool that parses the `.capssaml` files and automatically generates Python source code. The output appears to be a complete, runnable application, as suggested by the files in `BASE/basic-model` (e.g., `iot_node.py`, `model.py`, `experiment.py`).

**Consequences:**
*   **Positive:**
    *   Ensures consistency between the design model and the executable code.
    *   Dramatically accelerates the development cycle; changes in the model can be quickly propagated to the implementation.
    *   Reduces the potential for human error in the implementation phase.
*   **Negative:**
    *   The code generator itself is a complex piece of software that must be developed and maintained.
    *   The generator is tightly coupled to the SAML metamodel and the target Python framework. Changes to either will require significant updates to the generator.
    *   The generated code's style and structure are dictated by the generator, which may limit flexibility for custom, low-level optimizations.