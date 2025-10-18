---
### ADR-009: Preserve third-party asset licenses within the repository

Status: Inferred
Context: Multiple asset directories under public/ contain license.txt files (e.g., mcqueen, stadium, fuel_can, chick_hicks, hudson, strip_weathers).
Decision: Include and distribute third-party 3D assets with their original licensing files.
Consequences:
- Positive: Legal compliance and clear attribution; easier provenance tracking for assets.
- Negative: Slightly increases repository and distribution size; requires diligence to maintain license visibility in distributions.