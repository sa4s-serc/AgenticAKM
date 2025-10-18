---
### ADR-005: Adoption of Modern Python Packaging and Documentation Standards

**Status:** Inferred
**Context:** To ensure the project is maintainable, distributable, and user-friendly, it requires standardized tooling for dependency management, packaging, and documentation. Relying on ad-hoc scripts or outdated standards can lead to inconsistent development environments and poor developer experience.

**Decision:** The project adopted `pyproject.toml` for standardized dependency management and project metadata, aligning with modern Python standards (PEP 517/518). For documentation, MkDocs was chosen, as indicated by the `mkdocs.yml` file and the well-structured `docs/` directory, which covers everything from getting started guides to API references. A comprehensive `examples/` directory was also created to provide practical usage patterns.

**Consequences:**
*   **Positive:**
    *   **Reproducibility:** `pyproject.toml` enables deterministic dependency resolution with tools like Poetry or PDM, ensuring consistent environments for all developers.
    *   **Developer Experience:** A single configuration file simplifies project setup. High-quality, browsable documentation (thanks to MkDocs) and concrete examples significantly lower the barrier to entry for new users.
    *   **Maintainability:** Clear separation of source code (`moya/`), documentation (`docs/`), and examples (`examples/`) makes the repository easy to navigate and maintain.
*   **Negative:**
    *   **Tooling Dependency:** Developers must be familiar with build tools that support the `pyproject.toml` standard.
    *   **Documentation Overhead:** Maintaining high-quality documentation requires a continuous effort alongside code development.