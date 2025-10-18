---
### ADR-002: Implement the custom skill in C#/.NET

**Status:** Inferred
**Context:** Azure Functions supports multiple languages. The repository includes a .csproj and C# source (BingCustomSearch.cs), indicating a choice of .NET for implementation.
**Decision:** Use C# with a .csproj-based Azure Functions project to implement the custom skill.
**Consequences:** 
- Positive: Strong typing, mature tooling (Visual Studio, debugging), good performance on Azure Functions, broad .NET ecosystem.
- Negative: Less convenient access to some non-.NET libraries; ties runtime to .NET versions supported by Azure Functions.