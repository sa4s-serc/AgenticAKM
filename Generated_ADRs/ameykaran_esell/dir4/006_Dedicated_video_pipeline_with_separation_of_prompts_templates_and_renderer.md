# ADR-006: Dedicated video pipeline with separation of prompts, templates, and renderer

**Date**: 2025-10-14
**Status**: Proposed

## Context
Video subsystem has prompts, templates, config, run_llm.py, renderer.py, and processing scripts (process_pdf.py, process_videos.py).

## Decision
Isolate video generation into a pipeline that separates LLM prompt orchestration from scene templates and rendering.

## Consequences
Pros: clear responsibilities, swappable templates, easier experimentation with prompts. Cons: multi-step orchestration increases failure surface; requires robust state/rerun logic and dependency checks (fonts, codecs).