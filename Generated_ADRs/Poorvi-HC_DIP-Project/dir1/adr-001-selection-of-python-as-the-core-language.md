### ADR-001: Selection of Python as the Core Language

**Status:** Inferred
**Context:** The project requires the implementation of various data processing and machine learning algorithms, as indicated by filenames like `extract_features.py`, `svm_train.py`, and `linear_reg_train.py`. The architectural challenge is to choose a programming language that supports rapid development, provides a rich ecosystem for machine learning, and is suitable for scripting-based workflows.
**Decision:** The project will be implemented primarily in Python. This is evidenced by the consistent `.py` extension across all executable source files.
**Consequences:**
*   **Positive:**
    *   Enables rapid prototyping and experimentation due to Python's simple syntax and dynamic nature.
    *   Provides access to a vast and mature ecosystem of scientific computing and machine learning libraries (e.g., Scikit-learn, NumPy, Pandas), which are strongly implied by the file names.
*   **Negative:**
    *   May lead to performance bottlenecks for highly CPU-intensive tasks compared to lower-level languages like C++ or Rust, although this is often mitigated by using C-backed libraries.
    *   The lack of static typing can make larger, more complex systems harder to maintain and refactor without a disciplined approach to testing.