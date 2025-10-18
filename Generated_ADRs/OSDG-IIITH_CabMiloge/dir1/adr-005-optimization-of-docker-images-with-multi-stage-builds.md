---
### ADR-005: Optimization of Docker Images with Multi-Stage Builds

**Status:** Inferred
**Context:** To improve developer productivity and deployment efficiency, it is important to optimize Docker build times and reduce the size of the final container image. Re-installing all dependencies on every code change is inefficient.
**Decision:** A multi-stage build pattern is used in the `Dockerfile`. A first stage, named `python_cache`, is dedicated to creating a virtual environment and installing the dependencies from `requirements.txt`. A second, final stage copies this pre-built environment and the application source code, resulting in a leaner final image without build-time artifacts.
**Consequences:**
*   **Positive:**
    *   Leverages Docker's layer caching effectively. The dependency installation step is only re-run when `requirements.txt` changes, leading to significantly faster builds during development.
    *   The final image is smaller as it doesn't contain the build tools or source files used in the first stage.
    *   Enforces a clean separation between the build environment and the final runtime environment.
*   **Negative:**
    *   The `Dockerfile` becomes slightly more complex and may be harder for beginners to understand.