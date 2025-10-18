---
### ADR-004: Model course domains as Jekyll collections and structured content directories

**Status:** Inferred
**Context:** Presence of domain-specific directories such as _announcements, _modules, _schedules, _staffers, plus content directories like Lectures, Tutorials, Project.
**Decision:** Use collections (underscored directories) for structured entities (announcements, modules, schedules, staff) and dedicated content folders for lectures/tutorials/projects.
**Consequences:**
- Positive: Clear information architecture; easy generation of indexes and detail pages; consistent URLs; scalable content organization.
- Negative: Requires authoring with front matter; contributors must understand Jekyll conventions; potential need for _config.yml collection configuration.