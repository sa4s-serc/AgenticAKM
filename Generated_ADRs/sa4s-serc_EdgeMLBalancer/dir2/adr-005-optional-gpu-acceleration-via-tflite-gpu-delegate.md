---
### ADR-005: Optional GPU acceleration via TFLite GPU delegate

Status: Inferred
Context: Merged native libs include libtensorflowlite_gpu_jni.so and libgpu_delegate_plugin.so for all major ABIs.
Decision: Package and enable the TensorFlow Lite GPU delegate to accelerate inference on capable devices.
Consequences:
- Positive: Significant speedup on supported GPUs; smoother real-time camera inference.
- Negative: Not all devices benefit; potential initialization overhead and device-specific compatibility issues; larger binary footprint.