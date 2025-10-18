---
### ADR-006: Documentation-as-Code with a Static Site Generator

**Status:** Inferred
**Context:** A technical framework requires comprehensive documentation that is accurate, easy to navigate, and kept in sync with the source code. This includes tutorials, API references, and conceptual guides.
**Decision:** A "documentation-as-code" approach was chosen, utilizing the MkDocs static site generator. The configuration (`docs/mkdocs.yml`), content (Markdown files in `docs/docs`), and generation scripts (`docs/scripts`) are all stored and versioned within the Git repository. The inclusion of `mkdocs-jupyter` and `mkdocstrings-python` suggests that documentation is generated directly from source code docstrings and can include runnable Jupyter notebooks as tutorials.
**Consequences:**
*   **Positive:**
    *   **Version Control:** Documentation is versioned alongside the code, ensuring that changes to the code can be accompanied by corresponding documentation changes in the same commit.
    *   **Developer-Friendly:** Writing documentation in Markdown is simple and accessible to all contributors.
    *   **Automation:** API documentation can be automatically generated from the source code, reducing the risk of it becoming outdated.
    *   **Easy Deployment:** The output is a set of static HTML files, which are fast, secure, and simple to host (as suggested by `docs/vercel.json`).
*   **Negative:**
    *   **Build Step Required:** Documentation must be built before it can be viewed, unlike a wiki which can be edited live.
    *   **Non-technical Contributor Barrier:** While Markdown is simple, the full workflow (Git, build process) might be a barrier for non-technical contributors.