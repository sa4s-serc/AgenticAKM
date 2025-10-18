---
### ADR-005: Focus on Enterprise Linux and Containerized Deployments

**Status:** Inferred

**Context:** The target audience for a PostgreSQL exporter often includes enterprise users who run databases on stable, long-term support Linux distributions like RHEL and its derivatives. Additionally, modern infrastructure practices heavily favor containerization for deployment, management, and scalability, especially in cloud or Kubernetes environments. The deployment process must be simple and repeatable for both traditional and modern infrastructure.

**Decision:** The project provides first-class support for **RPM-based Linux distributions** and **Docker containers**. This is evidenced by the `pgexporter.spec` file for building RPMs, systemd integration files (`FindSystemd.cmake`, `pgexporter.service`), and multiple Dockerfiles (`contrib/docker/Dockerfile.alpine`, `contrib/docker/Dockerfile.rocky9`).

**Consequences:**
*   **Positive:**
    *   **Simplified Installation:** Users on enterprise Linux systems can use standard package managers (like `yum` or `dnf`) to install, upgrade, and manage the exporter. The systemd service file ensures it's managed correctly as a system daemon.
    *   **Modern Deployment:** Providing Docker images enables easy deployment in containerized environments like Docker Swarm or Kubernetes, aligning with modern DevOps practices.
    *   **Reproducible Builds:** The `contrib/docker/rpm/Dockerfile` provides a consistent, reproducible environment for building the RPM package itself.
    *   **Flexibility:** Offering different base images (lightweight Alpine, enterprise Rocky) allows users to choose the one that best fits their security and size requirements.
*   **Negative:**
    *   **Maintenance Overhead:** Maintaining multiple Dockerfiles and packaging for different systems (though only RPM seems to be the focus) adds to the project's maintenance burden.
    *   **Platform Bias:** While the C code is portable, the packaging and deployment artifacts are clearly focused on Linux, with less out-of-the-box support for other operating systems like Windows or macOS.