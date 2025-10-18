---
### ADR-004: VM-based Isolation for Dynamic Workloads

**Status:** Inferred
**Context:** The system needs to execute or host deployed models. These workloads may have complex, conflicting, or untrusted dependencies that require a higher level of isolation than standard containers can provide. A mechanism was needed to provision these isolated environments dynamically.
**Decision:** Use Virtual Machines (VMs) managed by **Vagrant** for executing deployed model workloads. This is strongly indicated by the `vm-service` directory, which contains a top-level `Vagrantfile`, and subdirectories for specific models (e.g., `app/model-final-demo-091f7f2c/Vagrantfile`) that are also managed by Vagrant. The `create_vm.sh` script further supports this decision.
**Consequences:**
*   **Positive:**
    *   Provides strong security and resource isolation (kernel-level) between the host and the guest workload, which is beneficial for running untrusted code.
    *   Allows for complete customization of the guest operating system and environment.
*   **Negative:**
    *   VMs have significantly higher overhead (CPU, memory, disk space) and slower startup times compared to containers.
    *   This approach limits the density of deployments on a single host and may be a scalability bottleneck.
    *   Managing VM images and Vagrant configurations can be more cumbersome than managing Docker images.