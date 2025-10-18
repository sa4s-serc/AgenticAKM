---
### ADR-009: Provide platform-specific setup scripts (Windows) including CUDA and firewall configuration

Status: Inferred
Context: Batch scripts exist: install_cuda_pytorch.bat, install_deps.bat, setup.bat, configure_firewall.bat. This indicates support for Windows developer environments and server exposure.
Decision: Supply Windows-friendly automation for installing CUDA-enabled PyTorch, dependencies, and configuring firewall rules for the server.
Consequences:
- Positive: Lowers onboarding friction; consistent dev setups; reduces misconfiguration for port access.
- Negative: Scripts are OS-specific; parity must be maintained for non-Windows platforms; security must be reviewed for opened ports.