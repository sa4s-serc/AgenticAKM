---
### ADR-011: Embed instrumented tests and golden assets for model regression checks

Status: Inferred
Context: androidTest includes TFObjectDetectionTest and test assets (cat1.png, mobilenetv1.tflite). Generated AndroidTest artifacts verify detection behavior and scaling assumptions.
Decision: Maintain an instrumented test suite with known assets to verify inference correctness and stability.
Consequences:
- Positive: Protects against regressions in preprocessing, inference, and postprocessing; documents expected behavior.
- Negative: Test runtime on device/emulator; keeping golden expectations synced with model updates requires maintenance.