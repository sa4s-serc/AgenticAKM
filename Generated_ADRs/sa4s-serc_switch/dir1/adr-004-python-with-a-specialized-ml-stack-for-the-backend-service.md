---
### ADR-004: Python with a Specialized ML Stack for the Backend Service

**Status:** Inferred
**Context:** The core value of the backend service is its ability to perform machine learning tasks, specifically computer vision object detection. The chosen technology must have access to a mature and high-performance ecosystem of ML libraries, data manipulation tools, and frameworks for serving models via an API.
**Decision:** The backend service is implemented in Python. It leverages a specialized stack of libraries, including `torch`, `torchvision`, and `ultralytics` for ML model execution (specifically the YOLO family of models), `pandas` and `numpy` for data processing, and web frameworks like `Flask` or `fastapi` to expose its functionality as an API.
**Consequences:**
*   **Positive:** Python's extensive ecosystem provides immediate access to state-of-the-art ML frameworks, significantly accelerating development. The combination of data science libraries and web frameworks makes it an ideal choice for creating and serving ML-powered applications.
*   **Negative:** Python's Global Interpreter Lock (GIL) can be a limitation for certain types of highly concurrent CPU-bound tasks, although this is often mitigated as ML inference libraries typically release the GIL. Managing the large and complex set of Python dependencies requires careful versioning and environment control.