---
### ADR-007: Template-driven media generation (HTML posters, slides, videos)

Status: Inferred
Context: backend/poster.html is a base; per-user poster HTMLs generated under backend/posters; video/templates and prompts directories define scene templates and prompt files; infographic_slides.py and visual_overview.py exist.
Decision: Generate outputs from reusable templates and prompt assets for consistency across posters, slides, and videos.
Consequences:
- Positive: Consistent branding/format; easier to iterate on styles; supports automation.
- Negative: Template rigidity can limit customization; maintaining many templates increases complexity.