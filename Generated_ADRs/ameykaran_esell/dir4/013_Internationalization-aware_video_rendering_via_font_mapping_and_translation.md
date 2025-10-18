# ADR-013: Internationalization-aware video rendering via font mapping and translation

**Date**: 2025-10-14
**Status**: Proposed

## Context
Video config includes lang_to_font.json and translate_slides.py for language-specific rendering.

## Decision
Integrate language-to-font mapping and translation steps into the video pipeline.

## Consequences
Pros: better non-Latin script support, broader audience reach. Cons: asset management complexity (fonts), additional QA for typography and line breaks across languages.