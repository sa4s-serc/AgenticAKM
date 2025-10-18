### ADR-001: Use a Static Site Generator for the Web Platform

**Status:** Inferred
**Context:** The primary requirement is to create a website for a university course. This involves publishing and organizing content such as announcements, lecture notes, schedules, and project descriptions. The content is mostly static, changes periodically (e.g., weekly), and needs to be easily updatable by course staff who may not be web developers. A solution that is simple, performant, secure, and low-cost is required, without the overhead of a database or a complex backend server.
**Decision:** The project will be built using Jekyll, a static site generator. All course content will be written in Markdown files. Jekyll will process these files, along with HTML templates and SASS stylesheets, to generate a complete, static HTML/CSS/JS website. The presence of `_config.yml`, `_layouts/`, `_includes/`, `_sass/`, and numerous `.md` files is direct evidence of this choice.
**Consequences:**
*   **Positive:**
    *   **Simplicity & Ease of Use:** Content can be created and edited in plain text using Markdown, which is easy to learn and use.
    *   **High Performance:** The output is static files, which can be served extremely quickly from any web server or CDN with minimal server-side processing.
    *   **Enhanced Security:** The lack of a database or server-side scripting languages drastically reduces the attack surface for common web vulnerabilities.
    *   **Version Control Friendly:** All content and code are text files, making them ideal for management with a version control system like Git.
*   **Negative:**
    *   **No Dynamic Functionality:** The site cannot support dynamic, user-specific features like login systems, forums, or real-time content submission without relying on external, client-side services.
    *   **Build Step Required:** Every content change requires a regeneration (build) of the entire site before it can be deployed, which can introduce a slight delay.