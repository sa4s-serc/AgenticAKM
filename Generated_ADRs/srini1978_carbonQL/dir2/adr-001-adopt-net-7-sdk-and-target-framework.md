### ADR-001: Adopt .NET 7 SDK and target framework

Status: Inferred
Context: All projects in the solution compile to net7.0 (e.g., carbonQLBackend/bin/Debug/net7.0, carbonQLConsole/bin/Debug/net7.0). The repository contains SDK-style project artifacts and generated GlobalUsings files typical of modern .NET SDK projects.
Decision: Standardize on .NET 7 for the solution and use SDK-style .csproj projects.
Consequences: 
- Positive: Access to modern C#/.NET features, performance improvements, simplified project configuration.
- Negative: .NET 7 is not an LTS release; consumers must have .NET 7 runtime. Reduced compatibility with older runtimes and platforms that cannot run .NET 7.