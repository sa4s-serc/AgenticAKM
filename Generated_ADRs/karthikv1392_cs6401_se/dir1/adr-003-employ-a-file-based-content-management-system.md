---
### ADR-003: Employ a File-Based Content Management System

**Status:** Inferred
**Context:** The website needs to manage different types of structured content, such as staff profiles, announcements, and course modules. A traditional database would be overkill for this project's scale and would violate the static-site principle. A structured, simple, and database-free method is needed to define, store, and display this information.
**Decision:** A file-based approach using Jekyll's "collections" and "front matter" will be used for content management. Specific directories prefixed with an underscore (e.g., `_staffers`, `_announcements`, `_modules`) are defined as collections. Each item in a collection is a separate Markdown file. Metadata for each item (e.g., a staff member's name and image URL) is defined in a YAML front matter block at the top of its corresponding file.
**Consequences:**
*   **Positive:**
    *   **Separation of Data and Presentation:** Content and its metadata are cleanly separated from the HTML templates (`_layouts/`) that render them.
    *   **Decentralized and Simple Updates:** Adding a new staff member or announcement is as simple as adding a new file to the appropriate folder, which can be done by anyone with repository access.
    *   **Atomicity:** Each piece of content is a self-contained file, making it easy to track changes, review pull requests, and manage contributions.
*   **Negative:**
    *   **Lacks Relational Capabilities:** Creating complex relationships between different content types is more difficult than in a relational database.
    *   **Potential for Scalability Issues:** While perfectly suitable for a course website, managing thousands of content files in this manner could become unwieldy and potentially increase site build times.