---
### ADR-002: Automated Prompt Optimization via Teleprompters

**Status:** Inferred
**Context:** The performance of LLM applications is highly sensitive to the exact wording of prompts, the choice of few-shot examples, and the overall reasoning structure. Manually optimizing these elements is a time-consuming and often unscientific "prompt engineering" process.
**Decision:** A dedicated optimization layer, referred to as "Teleprompting" (`dspy/teleprompt`), was created to automate the process of finding high-quality prompts. This layer contains various optimizer algorithms (e.g., `BootstrapFewShot`, `MIPROv2`, `COPRO`, `GEPA`) that take a defined program, a metric, and a small dataset to systematically generate and validate effective prompts and model parameters. This treats prompt engineering as a compilation or optimization step.
**Consequences:**
*   **Positive:**
    *   **Systematic Improvement:** Replaces manual trial-and-error with a reproducible, metric-driven optimization process.
    *   **Performance Gains:** Can automatically discover prompts that outperform human-engineered ones.
    *   **Adaptability:** Programs can be re-optimized for different LLMs or different target metrics without changing the core program logic.
*   **Negative:**
    *   **Computational Cost:** The optimization process can be computationally expensive and time-consuming, as it involves making multiple calls to LLMs.
    *   **Data Requirement:** Effective optimization requires a set of labeled examples and a well-defined evaluation metric, which may not always be readily available.