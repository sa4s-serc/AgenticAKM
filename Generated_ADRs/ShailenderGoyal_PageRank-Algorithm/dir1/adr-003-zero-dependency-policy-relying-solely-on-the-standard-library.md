---
### ADR-003: Zero-Dependency Policy Relying Solely on the Standard Library

**Status:** Inferred
**Context:** Managing external dependencies introduces complexity, including version conflicts ("dependency hell"), security vulnerabilities (supply chain attacks), and setup overhead (requiring `pip install`, virtual environments, etc.). The project needed to be maximally portable and simple to deploy.
**Decision:** The project will not use any third-party libraries. All functionality will be implemented using only the Python standard library. This is inferred from the complete absence of a dependency manifest file (like `requirements.txt`, `pyproject.toml`, `Pipfile`, etc.).
**Consequences:**
*   **Positive:** Guarantees maximum portability; the project can run on any system with a standard Python installation without any extra steps. It eliminates an entire class of potential bugs and security issues related to external dependencies. The deployment process is trivial.
*   **Negative:** This is a highly restrictive constraint. The project cannot leverage the vast and powerful Python ecosystem of libraries for tasks like web development, data analysis, or machine learning. Developers may be forced to "reinvent the wheel" for complex functionality, increasing development time and potential for bugs.