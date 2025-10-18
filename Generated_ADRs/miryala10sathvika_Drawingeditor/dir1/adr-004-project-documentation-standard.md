---
### ADR-004: Project Documentation Standard

**Status:** Inferred
**Context:** The project required a lightweight and accessible format for its primary documentation. The format needed to be easy for developers to write and maintain directly within the source code repository.
**Decision:** Markdown was selected as the standard for project documentation. This is evidenced by the presence of a `README.md` file, a conventional choice for top-level project information.
**Consequences:**
*   **Positive:** Markdown is easy to write and read. It is well-supported by version control systems and code hosting platforms (like GitHub, GitLab), which render it as formatted text. Documentation can be versioned alongside the code.
*   **Negative:** Lacks advanced features found in dedicated documentation systems (like Sphinx or AsciiDoc), such as complex layouts, automated API doc generation, and rich cross-referencing.
*   **Trade-off:** The ease of use and tight integration with the development workflow were chosen over the advanced capabilities of a more complex documentation generation system.