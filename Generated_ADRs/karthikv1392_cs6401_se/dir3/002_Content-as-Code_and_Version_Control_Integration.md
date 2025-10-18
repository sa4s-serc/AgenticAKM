# ADR-002: Content-as-Code and Version Control Integration

**Date**: 2025-10-08
**Status**: Proposed

## Context
A sustainable process was needed for authoring, managing, and versioning the course curriculum, which includes lecture notes, project specs, and announcements. The process needed to separate content from presentation to allow for easy updates.

## Decision
A 'Content-as-Code' strategy was implemented. All course content is authored in Markdown files and stored directly in the Git repository alongside the application code. Jekyll's content organization features (like collections for announcements) are used to structure the data.

## Consequences
This provides a full version history for all content, enables collaborative authoring via standard Git workflows, and cleanly decouples the raw content from its visual presentation. The workflow is highly efficient for developers but may have a slight learning curve for non-technical content creators accustomed to WYSIWYG editors.