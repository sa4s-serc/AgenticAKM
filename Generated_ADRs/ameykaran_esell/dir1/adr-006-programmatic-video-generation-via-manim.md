---
### ADR-006: Programmatic Video Generation via Manim

**Status:** Inferred
**Context:** A key feature is the automatic creation of short videos or "reels" based on input documents. A scalable and automated solution is needed, precluding the use of manual video editing software.
**Decision:** The Manim animation engine was chosen for programmatic video creation. The architecture includes a dedicated `backend/video/` module with a `core/renderer.py` and a `templates/` directory containing scene definitions (e.g., `intro_scene.py`, `keypoint_scene.py`). This indicates a template-based approach where scenes are dynamically populated with data and rendered into a final video using Manim.
**Consequences:**
*   **Positive:**
    *   **Automation & Scalability:** Allows for fully automated, "code-driven" video generation, which can be scaled to handle many requests.
    *   **Customization & Consistency:** Videos can be highly customized with data while maintaining a consistent brand style defined in the templates.
*   **Negative:**
    *   **High Computational Cost:** Video rendering is CPU and memory-intensive, which can lead to long processing times and require powerful server infrastructure.
    *   **Steep Learning Curve:** Manim is a complex, specialized library, which can make the video generation module difficult to maintain or extend for developers not familiar with it.