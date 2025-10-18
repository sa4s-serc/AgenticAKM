---
### ADR-008: Programmatic video creation using Manim and AV stack

Status: Inferred
Context: Dependencies include manim, moderngl, av, pydub, mutagen, srt; backend/video/core and templates implement scenes and pipeline; run.py and run.sh orchestrate.
Decision: Build videos via a custom pipeline using Manim for scenes/animation, PyAV for media handling, and auxiliary libs for audio/subtitles.
Consequences:
- Positive: Fine-grained control over visuals; reproducible rendering; flexible templating per scene.
- Negative: Heavy runtime dependencies and GPU/GL nuances; long render times; complex local environment setup.