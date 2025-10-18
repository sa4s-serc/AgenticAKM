### ADR-001: Modular and Composable Architecture for AI Programs

**Status:** Inferred
**Context:** Building applications with Large Language Models (LLMs) often involves complex chains of reasoning, tool usage, and data manipulation. A monolithic approach where prompts and logic are entangled is difficult to maintain, reuse, and reason about. The challenge is to structure LLM-based programs in a way that is both flexible and systematic.
**Decision:** The architecture is designed around a modular and compositional paradigm. This is evident from the distinct separation of concerns in the `dspy/` directory:
*   **Signatures (`dspy/signatures`):** A declarative way to define the expected inputs and outputs of an LLM task, decoupling the "what" from the "how".
*   **Modules (`dspy/predict`):** Reusable components that implement common prompting and reasoning strategies (e.g., `ChainOfThought`, `ReAct`, `ProgramOfThought`). These modules are the building blocks of the application.
*   **Primitives (`dspy/primitives`):** Foundational objects like `Example` and `Prediction` that form the data model for the framework.
Applications are built by composing these modules together, creating a clear, hierarchical program structure.
**Consequences:**
*   **Positive:**
    *   **Reusability:** Modules like `ChainOfThought` can be reused across different programs and tasks.
    *   **Maintainability:** The separation of signatures (intent) from modules (implementation) makes programs easier to understand and modify.
    *   **Testability:** Individual modules can be tested in isolation.
*   **Negative:**
    *   **Learning Curve:** Developers must learn the framework's specific abstractions (Signatures, Modules) rather than just writing free-form prompts.
    *   **Abstraction Overhead:** There might be a slight performance or conceptual overhead compared to a simple, direct LLM API call.