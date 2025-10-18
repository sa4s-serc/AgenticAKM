---
### ADR-004: Exploration of an Alternative LLM-Based Code Generation Path

**Status:** Inferred

**Context:** While the rule-based code generator (ADR-002) is effective, it is also rigid and requires significant effort to maintain and extend. The project is exploring a more flexible and potentially more powerful alternative for generating code and other artifacts from a high-level description.

**Decision:** To investigate using a Large Language Model (LLM) for code generation. A parallel approach is being developed within the `llmbased` directory. This module uses the `google-generativeai` library to interact with a Google LLM. The process likely involves feeding the LLM a combination of the SAML model and natural language prompts (`system_instructions.txt`) to generate not only the Python simulation code but also a web-based front-end (`web/web_generator.py`, `sample_output/index.html`) and other artifacts.

**Consequences:**
*   **Positive:**
    *   Offers greater flexibility; the LLM might be able to interpret more nuanced or complex requests than a rigid parser.
    *   Potentially lowers the effort needed to support new language features or target platforms by leveraging the LLM's existing knowledge.
    *   Enables the generation of a wider variety of outputs, including documentation, configuration files, and UI code, from a single source.
*   **Negative:**
    *   Introduces non-determinism; the quality and correctness of the generated code can vary between runs.
    *   Creates a dependency on an external, third-party API, which has cost, availability, and data privacy implications.
    *   Requires a new skill set in "prompt engineering" to achieve reliable and accurate results. The generated code must be rigorously validated.