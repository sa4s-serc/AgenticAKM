---
### ADR-012: Language-to-font mapping for internationalized video text

Status: Inferred
Context: backend/video/config/lang_to_font.json exists; video rendering requires fonts that support various scripts.
Decision: Map languages to fonts to avoid missing glyphs during video rendering.
Consequences:
- Positive: Correct text rendering across locales; fewer runtime font errors.
- Negative: Requires maintaining font assets and mappings; increased binary size and licensing considerations.