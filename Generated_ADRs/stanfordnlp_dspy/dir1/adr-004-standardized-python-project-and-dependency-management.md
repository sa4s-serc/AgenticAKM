---
### ADR-004: Standardized Python Project and Dependency Management

**Status:** Inferred
**Context:** To ensure the project is easy for developers to set up, contribute to, and for users to install, a modern and consistent approach to packaging and dependency management is required.
**Decision:** The project has adopted modern Python packaging and development standards.
*   **Packaging:** `pyproject.toml` is used as the central configuration file for project metadata, dependencies, and build system information, adhering to PEP 621.
*   **Dependency Management:** `uv.lock` is present in the root directory, indicating the use of `uv` for fast, deterministic dependency locking and installation. This ensures that all developers and CI/CD environments use the exact same versions of dependencies.
**Consequences:**
*   **Positive:**
    *   **Reproducibility:** Locked dependencies ensure that builds are reproducible across different machines and environments.
    *   **Clarity:** `pyproject.toml` provides a single, standardized source for project configuration.
    *   **Performance:** Using a modern tool like `uv` leads to faster dependency resolution and installation for developers.
*   **Negative:**
    *   **Tooling Familiarity:** Developers new to the Python ecosystem may be more familiar with older `requirements.txt` or `setup.py` files and might need to learn the `pyproject.toml` format and `uv` commands.