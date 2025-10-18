### ADR-001: Adoption of Model-Driven Engineering with a Domain-Specific Language

**Status:** Inferred

**Context:** The project requires the design and simulation of complex systems, likely in the Internet of Things (IoT) or cyber-physical systems domain. Manually writing code for such systems from scratch is time-consuming, error-prone, and makes it difficult to maintain a clear overview of the system architecture. There is a need for a higher-level, standardized method to define system components and their interactions before implementation.

**Decision:** To use a Model-Driven Engineering (MDE) approach. A Domain-Specific Language (DSL), which appears to be named SAML, is used to model the system architecture. This is evident from the numerous `.capssaml` and `.capssaml_diagram` files, the `metamodel-saml.puml` file defining the language's structure, and the presence of a `SAML-SAMPLE` directory containing an Eclipse-based modeling environment. The system's design is captured in these models, which then serve as the single source of truth.

**Consequences:**
*   **Positive:**
    *   Provides a high level of abstraction, allowing architects to focus on system design rather than implementation details.
    *   The SAML models serve as formal documentation and facilitate clear communication among team members.
    *   Enables automation by making the models machine-readable, forming the basis for code generation and analysis.
*   **Negative:**
    *   Requires team members to learn the SAML DSL and associated modeling tools (e.g., Eclipse).
    *   The initial investment in creating the DSL, its metamodel, and the tooling is significant.
    *   The design process is more structured and may feel restrictive compared to direct coding.