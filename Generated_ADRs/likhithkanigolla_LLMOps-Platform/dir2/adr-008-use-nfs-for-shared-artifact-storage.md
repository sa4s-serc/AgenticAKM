---
### ADR-008: Use NFS for shared artifact storage

Status: Inferred
Context: bootstrap-service includes boot_nfs_server.sh and boot_nfs_client.sh; indicates reliance on NFS for sharing files (e.g., model artifacts) between services/VMs.
Decision: Configure NFS server/client for shared storage of artifacts across hosts/VMs.
Consequences:
- Positive: Simple shared filesystem semantics; easy integration with existing tools and scripts.
- Negative: Single-point performance bottlenecks; operational complexity (mounts, permissions); weaker durability and availability compared to object storage.