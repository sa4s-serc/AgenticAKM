---
### ADR-007: Provision isolated runtime environments using Vagrant/VirtualBox

Status: Inferred
Context: vm-service contains a Vagrantfile and VirtualBox artifacts under vm-service/app/...; scripts to bootstrap agents inside VMs are present.
Decision: Use Vagrant with VirtualBox to provision VMs that host agents and workloads, likely for on-prem/dev/demo isolation.
Consequences:
- Positive: Reproducible, isolated environments; consistent developer experience.
- Negative: Heavier resource footprint than containers; not cloud-native; slower provisioning and scaling.