---
### ADR-006: Camera pipeline built around a Camera Fragment with custom overlay rendering

Status: Inferred
Context: CameraFragment, PermissionsFragment (runtime camera permission flow), and OverlayView indicate a real-time camera + inference + overlay pipeline typical of CameraX-based apps. Compiled artifacts reference update loops and frame processing.
Decision: Implement a camera-driven inference loop in CameraFragment and render detections via a custom OverlayView on top of the preview stream.
Consequences:
- Positive: Clear separation of concerns (capture, infer, render); responsive UI for real-time detection.
- Negative: Tight coupling to camera lifecycle; careful threading and backpressure management needed to avoid frame drops and UI jank.